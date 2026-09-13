# Research Notes — Reporting Platform

## Research Goal

Understand what a **Reporting Platform** actually is as an Application Type: its defining structure (and how small it can be made), its authoring/production/consumption workflow, its interfaces, its rules, and its boundaries against neighboring Types — especially Business Intelligence Platform, Dashboard Platform, Data Visualization Application, Ad-hoc Query Application (all processed siblings with recorded seams), plus Customer Communication Management / Regulatory Reporting Platform (unprocessed, overlap zones).

## Initial Boundary

Temporary hypothesis before research:

- A Reporting Platform produces **formatted, document-shaped output** (reports) from an organization's data and **delivers** it to consumers — as opposed to interactive visual analytics (BI), live displays (dashboards), or chart artifacts (data viz).
- Nearest neighbors: Business Intelligence Platform (processed — recorded seam: "formatted document-shaped output and its delivery"), Dashboard Platform (processed — "report = document-shaped point-in-time output delivered to an audience"), Data Visualization Application (processed — "reporting = formatted document output that *contains* visualizations"), Ad-hoc Query Application (processed), Customer Communication Management (§07, unprocessed), Regulatory Reporting Platform (§08, unprocessed), ESG Reporting Platform (§21, processed — different center).
- Obvious unknowns: is scheduling/delivery definitional or common-mature? Is pagination definitional? Is the banded layout paradigm definitional? Does the embedded-component pole (reporting libraries shipped to developers) belong to this Type or a different one?

## Research Questions

1. What is a "report" as an object — definition vs instance/output?
2. How is a report authored? What layout paradigms exist?
3. How is data bound? (queries, datasets, parameters, shared data sources)
4. What does execution/rendering produce? (pipeline stages, pagination, formats)
5. How are reports delivered/consumed? (portal, subscription, email, file share, print, embedding)
6. What scheduling/subscription machinery exists?
7. What roles/permissions exist? (author, consumer, administrator)
8. What run-time interactivity exists, and where does it live (viewer vs delivered file)?
9. Where exactly is the line to BI/dashboard/data-viz/ad-hoc query?
10. Historical check: do older report-writer generations (desktop Crystal era, Access-style report writers, mainframe report program generators) fit the definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole / philosophy | Customer tier |
|---|---|---|
| Microsoft SQL Server Reporting Services / paginated reports (Report Builder, Report Designer, web portal) | server platform with paginated reports; paginated reporting embedded in a wider BI estate | enterprise IT |
| SAP Crystal Reports | classic standalone desktop report writer (lineage since 1991); free viewer; IDE-embedded editions | individual authors → SMB → enterprise (via BusinessObjects platform) |
| JasperReports Library + JasperReports Server | open-source reporting engine (library) + stand-alone/embeddable server + REST service | developers → enterprise |
| Telerik Reporting (Progress) | embedded .NET reporting component: designers + viewers + processing services shipped into business applications | .NET development teams |
| Stimulsoft (Reports.* / Dashboards.* / Server / Cloud) | embedded reporting components for 35+ platforms + server + cloud service | developers → SMB → enterprise |

Rejected/adjusted during sampling: Oracle Analytics Publisher (BI Publisher) — the template-based high-volume pole — **unreachable** (docs.oracle.com 404 ×2, product page 404); IBM Cognos Analytics — 403; Jaspersoft community docs — 403 (GitHub README + sourceforge sample reference used instead); TIBCO docs — JS-rendered shell; Bold Reports — 403. The template-based authoring paradigm (author layout in Word/Excel, merge data) is therefore **not claimed** in this pass.

## Sources

Research date: 2026-09-09. All Layer-A observations below come from these fetches:

- Microsoft Learn — "What Is SQL Server Reporting Services (SSRS)?" — https://learn.microsoft.com/en-us/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports
- Microsoft Learn — "Report Definition Language (SSRS)" — https://learn.microsoft.com/en-us/sql/reporting-services/reports/report-definition-language-ssrs
- Microsoft Learn — "Reporting Services Reports (SSRS)" — https://learn.microsoft.com/en-us/sql/reporting-services/reports/reporting-services-reports-ssrs
- Microsoft Learn — "Create and manage subscriptions for native mode report servers" — https://learn.microsoft.com/en-us/sql/reporting-services/subscriptions/create-and-manage-subscriptions-for-native-mode-report-servers
- SAP — Crystal Reports product page — https://www.sap.com/products/technology-platform/crystal-reports.html
- GitHub — JasperReports Library README — https://github.com/Jaspersoft/jasperreports
- JasperReports Sample Reference (v7.0.8) — https://jasperreports.sourceforge.net/sample.reference/README.html
- Telerik Reporting documentation welcome page — https://docs.telerik.com/reporting (served from telerik.com)
- Stimulsoft documentation hub — https://www.stimulsoft.com/en/documentation
- Stimulsoft Reports & Dashboards User Manual (TOC, GitHub-hosted) — https://stimulsoft.github.io/Stimulsoft.Reports.Dashboards.User.Manual/Introduction/

Unreachable (recorded per source-access limitation; no claims drawn): Oracle BI Publisher / Analytics Publisher, IBM Cognos Analytics, Jaspersoft community documentation portal, TIBCO JasperReports Server docs, Bold Reports, Wikipedia (RPG article, timeout).

## Product Observations

### Microsoft SSRS / paginated reports (Layer A — direct)

- Positioning: "a set of on-premises tools and services to create, deploy, and manage **paginated reports**"; "Paginated reports are perfect for **fixed-layout documents optimized for printing**, such as PDFs and Word files."
- Authoring: Report Builder (standalone authoring tool) or Report Designer in SQL Server Data Tools.
- Report definition: RDL — "an XML representation of a … report definition. A report definition contains **data retrieval and layout information** for a report." File extension `.rdl` (client-side variant `.rdlc`). After publishing, the report is "a report item stored on the report server."
- Parameters: `ReportParameters` element; typed values (Boolean, DateTime, Integer, Float, String).
- Processing stages: **Compile** (evaluate expressions, store compiled intermediate format) → **Process** (run dataset queries, combine intermediate format with data and layout) → **Render** (rendering extension "determine[s] how much information fits on each page and create[s] the **paged** report") → **Export** (optional, to other file formats).
- Reuse: "Define a report once and display it in a variety of ways. You can export the report to multiple file formats, or deliver the report to subscribers as e-mail or to a shared file. You can create multiple **linked reports** that apply separate parameter sets to the same report definition." Shared data sources, shared datasets, subreports; "Manage report data sources separately from the report definition. For example, you can change from a test data source to a production data source without changing the report."
- Layout: "Design reports in a **free-form layout**. Report layout is not restricted to bands of information." Data regions: tables, matrices, expand/collapse groups, charts, gauges, indicators/KPIs, maps.
- Interactivity: "drillthrough actions, expand/collapse toggles, sort buttons, Tooltips, and report parameters … enable report reader interactions with the report."
- Consumption surfaces: web portal (folder hierarchy; content organized by type: paginated reports, KPIs, Excel workbooks, shared datasets, shared data sources; "Schedule report processing, access reports on demand, and subscribe to published reports"), URL access, export from viewer toolbar (formats configured by administrator), print, integration into web/Windows applications via APIs.
- Subscriptions: standard subscriptions (individual users) deliver via **e-mail** (embed/attach in a render format, or include link) or **Windows file share** (UNC path, file name, render format, overwrite options); **shared schedule** or report-specific schedule; per-subscription parameter values ("can be different from those parameters used to run the report on demand"); data-driven subscriptions exist as a separate mechanism; prerequisites: SMTP configured, stored credentials on the data source. Key behavior: "**The report is delivered as a static file.** If the report includes interactive features (for example, links to other rows and columns), those features aren't available."
- Operations: report cache (schedule large reports off-peak), **snapshots** ("consistent results for multiple users who must work with identical sets of data"), **report history** ("a series of report snapshots … shows how data changes over time").
- Security: "Windows authentication, integrated security, and role assignment"; common strategy = folder structure + role-based access to reports and related items.
- Data alerts (SharePoint mode): email notification when report data meets conditions.
- Adjacent bundled artifacts: KPIs surfaced in the portal; mobile reports (responsive-layout reports, SQL 2017–2019 era); pinning SSRS visuals to Power BI dashboards.

### SAP Crystal Reports (Layer A — direct, product page)

- Positioning: "Create, design, and deliver **formatted and dynamic business reports and invoices**"; "richly formatted, **pixel-perfect, and multipage reports** from virtually any data source, delivered in **over a dozen formats**."
- Output examples: "ready-to-consume information as pixel-perfect **invoices, letters, statements, sales and operations reports**, promotion campaigns, and loyalty card reports."
- Authoring: drag-and-drop with "product wizards and parameters"; guidance on sorting and grouping; embed dynamic images and bar codes.
- Data access: flat files (Excel, text, web logs, XML, file systems), databases (SAP HANA, Access, SQL Server, DB2, Oracle, MySQL, PostgreSQL), JDBC/ODBC, applications (Sage, Salesforce).
- Rights: "Manage user rights to **access, view, refresh, export, or print** reports."
- Consumption: free **viewer** — "Open, view, explore, save, and share your reports without IT support, even while working offline"; view `.RPT` files; export to PDF; "save them to the SAP BusinessObjects Business Intelligence platform."
- Embedded editions: free versions for Visual Studio (.NET) and Eclipse (Java) — "Embed interactive reports into Java applications."
- Deployment posture: desktop on-premise product, named-user license; lineage "since 1991"; more than one million regular users claimed.

### JasperReports Library + JasperReports Server (Layer A — direct)

- Library positioning: "the world's most popular open source **reporting engine** … able to use data coming from **any kind of data source** and produce **pixel-perfect documents** that can be **viewed, printed or exported** in a variety of document formats including HTML, PDF, Excel, OpenOffice, MS Word and other."
- Definition lifecycle: report templates are XML files (`.jrxml`), compiled to `.jasper`; filled with data (`.jrprint` objects); Jaspersoft Studio (Eclipse-based designer) and JasperReports Web Studio (web designer) author templates.
- Deployment targets: "reports can be built out of any data source and can have their look and feel formatted for printing or on-screen reading, or can be deployed to a **JasperReports Server** instance, **JasperReports IO** repository or to a **custom application** using the JasperReports Library."
- Server positioning: "a stand-alone and **embeddable reporting server** … can be embedded into a web or mobile application as well as operate as a **central information hub** for the enterprise by delivering mission critical information on a **real-time or scheduled basis** to the browser, mobile device, or **email inbox** in a variety of file formats … optimized to **share, secure, and centrally manage** your Jaspersoft reports and analytic views."
- IO: "a RESTful reporting and data visualization service built on JasperReports Library" — the engine exposed over REST "from any other software development platform."
- Feature map (sample reference): report design — data grouping, crosstabs, subreports, book reports/report parts, table of contents, hyperlinks, barcodes, charts, i18n/unicode, style templates, conditional styles, multi-column, landscape, watermarks; compilation — multiple expression-language compilers (Groovy, Java, JavaScript); data — query executers (SQL, HQL, EJBQL, MDX/Mondrian, XPath, JSON/JSONQL), data sources (JavaBean, CSV, Excel, XML, JSON, TableModel, custom, HTTP data adapters), parameterized queries; filling — scriptlets, virtualizers for very large documents, suppress pagination; export — batch export, encrypted PDF, PDF/A, PDF forms, printing via Java Print Service API, text, XLS formulas, CSV/XLSX/XLS/JSON metadata export, PPTX.

### Telerik Reporting (Layer A — direct)

- Positioning: "a .NET **reporting solution for designing, processing, exporting, and embedding reports** in web, desktop, and cloud-based applications … build **pixel-perfect reports** and the **viewers and services required to deliver those reports inside business applications**."
- Use cases named: "operational reports, invoices, statements, dashboards, or printable business documents that pull data from multiple sources and render consistently across technologies."
- Lifecycle: "designing the report, **processing and rendering the report with data**, and exporting or displaying the final output."
- Components map to stages: **report designers** (standalone desktop designer, web report designer embeddable in web apps, Visual Studio designer), **report viewers** (HTML5, MVC/WebForms wrappers, native Angular/React/Blazor, WinForms/WPF/WinUI), **report processing services** (hosted in ASP.NET Core; "receives a report definition, processes it with data, and returns the rendered result to the viewer or the export pipeline"), **export formats** (PDF, Word, Excel, PowerPoint, PNG/TIFF, CSV).
- Data: "relational, multidimensional, ORM-based, and custom data sources."

### Stimulsoft (Layer A — direct)

- Positioning: "libraries and scripts for reporting and data analysis, with report and dashboard **designers and viewers for 35+ frameworks, platforms, and technologies**" (Reports.NET/WEB/JS/WPF/JAVA/PHP/PYTHON/Angular/React/Vue/Blazor/Avalonia; Dashboards.* line; PDF Forms; Cloud; Designer; Server).
- Server: "a complete set of tools for working with reports and dashboards, as well as **user management and automation tools**."
- User manual anatomy (banded model, extensive): report structure and **report rendering**; **bands** (standard and cross-bands, rendering order); **data band** (data source binding, list output, header/footer, sorting, filtering, PrintOn properties); **master-detail** (master component, data relation, multilevel nesting, keep-details-together); **groups** (grouping conditions, group header/footer bands, nested groups, row numbering); **page bands** (page header/footer, even/odd pages); **report bands** (report title, report summary, print-at-bottom, print-if-empty); **columns** (on page / in data band, across-then-down vs down-then-across); **page and column breaks**; **pagination** (page number, total page count, Page N of M, reset page number); **breaking** (bands/text/panels/images, auto-break); hierarchical band; child band; empty band; watermarks/overlay band; panels (side-by-side, multiple tables); **cross-tab** (rows/columns/summary cells); expressions (dictionary variables, data fields, functions, conditional); conditional formatting (value/expression conditions, data bars, color scales, icon sets); styles; text formatting (currency/date/percentage); barcodes (large library incl. GS1); HTML/markdown/rich text in components; **wizards** (standard report, master-detail, chart, cross-tab, label report); **drill-down** (via page in report or external report); dynamic sorting and collapsing in preview; invoice report; invoice report with parameters.
- Adjacent signals: "Migration from Crystal Reports" solution page (same market family); ZUGFeRD/Factur-X e-invoicing documentation (document-output compliance use).

## Cross-product Comparison

| Aspect | SSRS | Crystal Reports | JasperReports | Telerik | Stimulsoft | Evidence |
|---|---|---|---|---|---|---|
| Report definition as persistent artifact | .rdl (XML: data retrieval + layout) | .rpt file | .jrxml → compiled .jasper | report definition processed by service | report template (dictionary, bands) | A×5 |
| Dedicated authoring surface | Report Builder / Report Designer | desktop designer; VS/Eclipse editions | Jaspersoft Studio / Web Studio | standalone / web / VS designers | designers per platform + wizards | A×5 |
| Data binding via queries/connections to external sources | data sources + datasets; shared variants | "virtually any data source" (files, DBs, JDBC/ODBC, apps) | any data source (SQL, HQL, MDX, XPath, JSON, JavaBean, CSV…) | relational, multidimensional, ORM, custom | data connections + relations + transformations | A×5 |
| Run-time parameters | typed report parameters; per-subscription values; linked reports | wizards and parameters | parameterized queries | report parameters | invoice-with-parameters; parameter machinery | A×5 |
| Rendering pipeline producing fixed-layout document | compile→process→render (paged)→export | pixel-perfect multipage | fill → pixel-perfect documents | process with data → render | report rendering | A×5 |
| Multi-format export | PDF/Word/Excel/PowerPoint/MHTML/image/CSV… | "over a dozen formats" | HTML/PDF/Excel/ODF/Word/CSV/text/PPTX, PDF/A, encrypted PDF | PDF/Word/Excel/PowerPoint/PNG/TIFF/CSV | export formats in viewers | A×5 |
| Portal / catalog consumption | web portal (folders, types, KPIs) | save to BusinessObjects BI platform; free viewer | JasperReports Server repository | (host application is the surface) | Server | A×4 (Telerik pole: host app) |
| Scheduled/subscription delivery | subscriptions (email/file share, schedules, per-subscription params) | (not confirmed in fetched sources) | Server: "real-time or scheduled basis… email inbox" | (not in fetched page) | Server automation tools | A×3 |
| Access control on reports | Windows auth + role assignments + folders | user rights: access/view/refresh/export/print | Server: share, secure, centrally manage | (host app responsibility) | Server user management | A×4 |
| Interactivity in viewer | drillthrough, expand/collapse, sort, tooltips | "interactive reports" (embedded editions) | hyperlinks; drill-down samples | interactivity documentation section | drill-down, dynamic sort/collapse in preview | A×5 |
| Embedding in applications | APIs, app integration, .rdlc | VS/Eclipse editions | library in Java apps; IO REST | core value proposition | core value proposition | A×5 |
| Print orientation | print reports; fixed-layout for printing | pixel-perfect printable documents | "viewed, printed or exported"; print service | printable business documents | print machinery (PrintOn, keep-together) | A×5 |
| Bundled dashboards/KPIs | KPIs in portal; mobile reports | — | analytic views (Server) | dashboards named as use case | Dashboards.* product line | A×3 |
| Snapshots / report history | snapshots + report history + cache | — | — | — | — | A×1 (product-specific) |
| Data alerts | SharePoint data alerts | — | — | — | — | A×1 (product-specific) |
| Banded layout paradigm | explicitly NOT banded ("free-form… not restricted to bands") | band-style classic model | band model (detail section, groups) | (definition-based, paradigm not asserted in fetched page) | full band model | A×4 + A×1 counter-example |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The report definition as the unit of record** — a persistent, named, re-editable artifact that binds a fixed layout to data retrieval (queries/connections against external data sources) and declares run-time parameters. Remove → ad-hoc query tool (no standing definition), chart tool (no document), or a static template (no data binding).
2. **Document-shaped rendering from live data** — executing the definition against its data sources produces a formatted, fixed-layout (commonly paginated) document; the same definition re-runs against fresh data; the fixed layout is the deliverable, not an exploration surface. Remove → BI/dashboard territory (interactive analytics / live display); without live data → static template / mail merge.
3. **Managed production and delivery to consumers** — definitions are stored and run (on demand and/or on schedule) and outputs are placed where consumers consume them: a report portal/catalog with access control, subscription distribution (email, file share, print), export, or embedding in a host application; consumption is reading the produced document. Remove → a bare layout designer or rendering library with no consumption path (below the platform bar).

Jointly-held load-bearing:

- 1 alone = layout designer / template editor
- 2 without 1 = one-off document generation (mail merge)
- 3 without 1+2 = file distribution with nothing to deliver
- 1+2 without 3 = authoring tool with no consumption path
- 2+3 without 1 = pre-canned output with no authored definitions

### L1 — Common Mature Structure

- Typed run-time parameters (with value lists sourced from data)
- Multi-format export (PDF/print/Excel/Word/HTML/CSV family; exact sets vary)
- Scheduling and subscriptions (shared schedules; per-subscription parameter values; email/file-share destinations)
- Shared data sources / shared datasets managed separately from report definitions
- Reuse machinery: subreports, linked reports (parameter-set variants), shared styles/templates
- Viewer interactivity: drill-down (expand/collapse), drillthrough, interactive sort, hyperlinks, tooltips
- Access control over reports (view/export/print rights; folder/role security)
- Wizards for standard report shapes (tabular, master-detail, chart, cross-tab, label)
- Grouping/aggregation machinery (group headers/footers, totals, crosstabs)
- Document-oriented elements: images, barcodes, watermarks, page numbering (Page N of M)
- Print machinery (page setup, keep-together, print-on rules)

### L2 — Variant / Optional Structure

- Layout paradigm: banded (Stimulsoft, JasperReports, classic Crystal model) vs free-form (SSRS documents this explicitly) vs template-based (Oracle BI Publisher class — **unverified in this pass, not claimed**)
- Deployment posture: server platform (SSRS, JasperReports Server, Stimulsoft Server) vs embedded component/library (Telerik, Stimulsoft Reports.*, Crystal for VS/Eclipse, JasperReports Library) vs standalone desktop authoring (Crystal Reports desktop)
- Security substrate: platform-native auth + role/folder model (SSRS) vs host-application security (embedded pole) vs server user management (Stimulsoft Server)
- Data substrate breadth: relational DBs, flat files, ORM objects, JSON/XML, multidimensional (MDX), application APIs
- Expression/automation languages (SSRS expressions; Jasper Groovy/Java/JavaScript compilers; Stimulsoft expressions/events)
- Bundled dashboards/KPI surfaces (Stimulsoft Dashboards.*, SSRS KPIs/mobile reports) — neighboring capability
- E-invoicing compliance outputs (Stimulsoft ZUGFeRD/Factur-X)
- Cloud-service posture (Stimulsoft Cloud)
- Operational extras: report cache, snapshots, report history, data alerts (SSRS-documented; generality unverified)

### L3 — Vendor-specific (research notes only)

- RDL as a published interchange schema for report definitions (Microsoft)
- File-format ecosystems: .rdl/.rdlc, .rpt, .jrxml/.jasper/.jrprint, .mrt
- SSRS report parts (deprecated), mobile reports (Datazen lineage), Power BI pinning, SharePoint-mode data alerts
- JasperReports virtualizers, scriptlets, book reports
- Crystal ↔ SAP BusinessObjects BI platform integration; Crystal migration paths marketed by competitors (Stimulsoft)
- Stimulsoft 35+ platform matrix; per-platform product split

### Rejected Findings (anti-overfit)

- **Banded layout as definitional** — rejected. SSRS explicitly documents a free-form layout ("not restricted to bands of information"). The layout paradigm is a variant axis; the invariant is a fixed layout bound to data, however expressed.
- **"Paginated" as the strict invariant** — calibrated. All five sampled products are page-oriented (paging machinery is deep in SSRS, Stimulsoft, Jasper), but HTML/streaming output formats exist (Jasper HTML export; SSRS MHTML). The invariant is **fixed-layout document output**; page orientation is the dominant realization.
- **Scheduling/subscriptions as definitional** — rejected. The desktop/viewer/export consumption path (Crystal-class) satisfies the Type without server-side scheduling; scheduling is common-mature, not defining.
- **SQL as the data language** — rejected. Query executers/data sources span MDX, HQL, EJBQL, XPath, JSON, ORM objects, flat files, application APIs. The invariant is "queries/connections against external data sources," not SQL.
- **Dashboards as part of the Type** — rejected as identity. Dashboards appear as bundled neighboring capability (Stimulsoft Dashboards.*, SSRS KPIs); the dashboard center is a separate processed Type.
- **Specific security substrate** — variant, not invariant (Windows auth vs host-app security vs server user management).

## Boundary Findings

1. **vs Business Intelligence Platform (processed)** — DISCHARGED from this side. The BI pass recorded: "Reporting Platform seam = interactive visual analytics over a governed hosted repository vs formatted document-shaped output and its delivery (BI ships formatted reporting as a capability via paginated-report/companion engines)." This pass confirms keep-both: the reporting center is the document-shaped output and its production/delivery; interactive exploration over a governed repository is the BI center. Removal test: remove document-shaped output → BI; remove interactive exploration → Reporting. BI products ship paginated reporting as a capability (SSRS paginated reports sit inside the Microsoft BI estate) — capability, not identity.
2. **vs Dashboard Platform (processed)** — keep-both. Dashboard pass: "Dashboard = standing live display consulted in place; report = document-shaped point-in-time output delivered to an audience." Vendors police the seam (dashboard vendors' own dashboard-vs-report distinctions were documented in that pass). Reporting products bundle dashboards (Stimulsoft Dashboards.*, SSRS KPIs) as neighboring capability.
3. **vs Data Visualization Application (processed)** — DISCHARGED from this side. DVA pass flagged: "reporting = formatted document output that *contains* visualizations (charts feed reports) vs the chart artifact itself." Confirmed: charts are report content elements (SSRS data regions; Jasper chart components; Stimulsoft chart-in-band); the DVA center is the standalone chart artifact authored from user-supplied data. Keep-both.
4. **vs Ad-hoc Query Application (processed)** — keep-both. Ad-hoc = question-time query + immediate result + in-place refinement; reporting = standing definitions producing recurring formatted output. The persistent definition and the formatted document are the seam.
5. **vs Customer Communication Management / CCM (§07, unprocessed)** — overlap zone flagged for joint review. Crystal's own examples (invoices, letters, statements) and Stimulsoft's e-invoicing compliance work sit in the overlap. Proposed seam: CCM = customer-facing correspondence production at volume (personalization, branding, regulatory content, transaction-triggered); Reporting Platform = organization-internal data reporting where the formatted document is the unit of production. Both may share rendering engines.
6. **vs Regulatory Reporting Platform (§08, unprocessed)** — adjacent. Regulatory reporting's center (per the financial-risk pass's recorded seam) is report production/submission machinery for regulator filings (taxonomies, validations, submissions); the generic Reporting Platform's center is formatted output from org data with no submission machinery. Flag for joint review when that sibling is processed.
7. **vs ESG Reporting Platform (processed)** — no conflict. ESG reporting's center is the disclosure-production loop (disclosure structure + data of record + deliverable); naming-cluster adjacency only.
8. **vs word-processor mail merge / document generation** — mail merge = template + data rows → documents, a capability of document editors; the Reporting Platform is data-centric (queries, parameters, managed production, delivery, security). Mail merge lacks the standing definition + managed production legs.
9. **vs Spreadsheet Application (§03.03, unprocessed)** — spreadsheets can produce formatted output, but the center is the cell grid, not the report definition + rendering + delivery pipeline. No conflict.
10. **vs SQL Workbench / Analytical Query Editor (processed)** — query-first tools with result grids; no standing formatted report definitions, no delivery machinery. Keep-both.

## Historical / Market-Sample Check

- **Crystal Reports desktop generation** (lineage since 1991, still sold as a desktop named-user product): definition (.rpt) + pixel-perfect multipage rendering + viewer/export/print + optional BusinessObjects platform — satisfies all three legs with no cloud, no web portal, no AI.
- **Access-style desktop report writers** (report definition bound to local database queries, preview/print output) — satisfy the legs conceptually; not fetched in this pass, held as conceptual corroboration.
- **Mainframe-era report program generators** (stored report programs/layouts bound to data files, producing printed reports on batch schedules) — conceptually satisfy the three legs (definition, rendering to print, distribution); **no source fetched** (Wikipedia timeout), so this is held as conceptual lineage with low confidence, not an evidence-backed claim.
- The definition does **not** depend on: web delivery, cloud, specific file formats, banded layout, SQL, Windows authentication, or any specific security substrate. Older and regional products fit.

## Uncertainties

- **Template-based authoring pole unverified**: Oracle BI Publisher (author layout in Word/Excel, merge data at scale) was unreachable. The pass does not claim template-based authoring as a variant; it is recorded as a probable variant axis awaiting evidence.
- **Scheduling in the Crystal desktop product** was not confirmed from fetched sources (BusinessObjects platform scheduling exists but was not fetched); scheduling claims rest on SSRS + JasperReports Server + Stimulsoft Server.
- **Snapshots/report history/data alerts** are SSRS-documented only; treated as product-specific/optional, not promoted.
- **Exact export-format sets** vary per product and version; only "multiple standard document formats" is claimed, with observed examples.
- **Interactivity depth** (drillthrough vs drill-down semantics) varies; only the presence of viewer interactivity is claimed as common.
- Whether the embedded-component pole should eventually split into its own leaf is **not** recommended here: designers/viewers/processing are the same structures with a different delivery channel (the host application), and vendors span both postures (Jasper library↔server; Stimulsoft components↔server; Crystal desktop↔IDE editions).

## Final Synthesis

The Reporting Platform is the organization's **formatted-report production system**: the unit of record is the **report definition** (fixed layout bound to data retrieval, with run-time parameters); execution **renders document-shaped output** (fixed-layout, commonly paginated) from live data; and the platform **produces and delivers** that output to consumers — through a portal, subscriptions, export/print, or embedding in a host application. Everything else — layout paradigm, format sets, scheduling depth, security substrate, dashboards, AI — is variant or bundled capability. The Type is distinct from BI (interactive analytics), dashboards (live display), data viz (chart artifact), and ad-hoc query (question-time interrogation), while sharing data-access substrates with all of them.
