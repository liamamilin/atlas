# Reporting Platform

## Overview

A **Reporting Platform** is an organization's system for producing formatted, document-shaped reports from its data and delivering them to the people who consume them.

The defining core is small:

```text
Report definition (fixed layout bound to data queries + parameters)
└── Document-shaped rendering from live data
    └── Managed production and delivery to consumers
```

A reporting platform answers a different question than the neighboring analytics Types. A business intelligence platform lets people explore data interactively; a dashboard shows a live display consulted in place; a chart tool produces a single visualization. A reporting platform produces **the document**: a fixed-layout, commonly paginated report — an operational summary, an invoice run, a statement, a compliance pack — rendered fresh from current data and placed where its audience will read it, whether that is a web portal, an email inbox, a file share, a printer, or a screen inside a business application.

## Users & Context

Three roles recur across products:

- **Report authors** (report developers, analysts, power users) design report definitions: they connect to data sources, write or pick queries, lay out the report, define parameters, groups, and totals, preview the result, and publish it.
- **Report consumers** (business users, managers, external recipients) run or receive finished reports: they pick a report from a catalog, supply parameter values such as a date range or a region, read the rendered document, and export or print it. Many consumers never author anything — they subscribe and receive.
- **Administrators** operate the platform: they manage the report catalog and its folder structure, access rights, shared data sources and credentials, schedules, and execution settings.

A fourth role appears in the embedded posture: **application developers** who ship report rendering inside their own software, so end users of that software consume reports without knowing a reporting product exists.

Typical work: recurring operational reporting (weekly sales and operations summaries, inventory and production reports), document production (invoices, statements, letters, order confirmations), scheduled distribution (the Monday morning report in the inbox), and print-oriented output where page layout matters.

## Core Model

### The Defining Core

**1. The report definition — the unit of record.**
A report is a persistent, named, re-editable artifact that binds two things together: a **fixed layout** (the visual structure of the document — regions, tables, groups, headers and footers, totals) and **data retrieval** (queries or connections against external data sources). The definition also declares **parameters** — typed run-time inputs such as a date range, a customer, or a region that shape the data each time the report runs. The definition is stored, versioned, and re-runnable; it is not a one-off document.

**2. Document-shaped rendering from live data.**
Executing a definition is a pipeline: the definition is prepared (expressions evaluated), its queries run against the data sources, the returned data is bound into the layout, and a rendering step produces the final document — deciding how content flows across pages, where page breaks fall, and how headers, footers, and page numbers repeat. The output is a **fixed-layout document** in standard formats (PDF and print-oriented formats, spreadsheets, word-processor files, HTML). The same definition produces fresh output each run; the layout is the constant, the data is the variable. The fixed layout is the point: the deliverable is a document to read, not a surface to explore.

**3. Managed production and delivery.**
The platform stores definitions in a managed catalog, runs them on demand or on schedule, and places the outputs where consumers consume them: a report portal or library with access control, subscription-based distribution (email, file shares, printers), direct export, or embedding inside a host application. Consumption is reading the produced document.

All three structures are load-bearing together:

- a layout tool with no data binding is just a designer;
- rendering without a stored definition is one-off document generation (mail merge);
- delivery machinery without definitions and rendering distributes nothing;
- definitions and rendering without a delivery path leave reports stranded on the author's machine.

### Standard Capabilities

Mature products commonly add, without these defining the Type:

- **Parameters with value lists** — prompted at run time; allowed values often sourced from a query.
- **Multi-format export** — the same definition renders to PDF, spreadsheet, word-processor, HTML, CSV, and image formats; exact sets vary by product.
- **Scheduling and subscriptions** — a consumer or administrator binds a schedule, parameter values, a render format, and a destination (email, file share); the platform runs the report unattended and delivers it.
- **Shared data sources and datasets** — data access is managed separately from report definitions, so a connection can change (test to production) without touching reports.
- **Reuse machinery** — subreports, linked reports (one definition, multiple parameter sets), shared styles and templates.
- **Viewer interactivity** — drill-down (expand/collapse groups), drillthrough to detail, interactive sorting, hyperlinks, tooltips — inside the live viewer.
- **Access control** — who can view, run, export, or print which reports, commonly organized through folders and roles.
- **Authoring aids** — wizards for standard shapes (tabular lists, master-detail, charts, cross-tabs, labels).
- **Document elements** — barcodes, images, watermarks, page numbering ("Page N of M"), group totals and running sums.

### One Structure, Many Implementations

```text
Concept:            Report definition
Implementations:    XML definition files, compiled templates, proprietary report files

Concept:            Fixed layout
Implementations:    banded layouts (header/data/group/footer bands),
                    free-form positioned layouts, table/region models

Concept:            Data retrieval
Implementations:    SQL queries, ORM objects, MDX cubes, JSON/XML/CSV sources,
                    application APIs, flat files

Concept:            Delivery
Implementations:    web portal/catalog, email subscription, file-share drop,
                    print, embedded viewer inside a business application
```

A reader who has only seen one implementation — say, a web portal with scheduled email delivery — should still be able to recognize a desktop report writer whose output is a printed report, or a reporting library embedded in an invoicing application, as the same Type.

## How It Works

### Author a report

```text
Connect to data sources
→ define datasets/queries (and parameter value lists)
→ lay out the report (regions/bands, groups, totals, headers/footers)
→ declare parameters
→ preview with sample data
→ publish the definition to the catalog (or save it into the application)
```

Authoring is iterative: preview, adjust layout and expressions, publish, collect feedback from readers, revise.

### Consume on demand

```text
Find the report in the portal/catalog
→ supply parameter values (date range, entity, region…)
→ the platform runs the definition against current data
→ read the rendered report in the viewer
→ export to a format or print
```

### Consume on schedule

```text
Create a subscription: report + schedule + parameter values + render format + destination
→ at each scheduled time the platform runs the report unattended
→ the rendered document is delivered (email attachment/embed, file share, printer)
```

Unattended runs require stored credentials on the data sources — the platform, not a user, supplies the identity when the query executes.

### Consume inside an application (embedded posture)

```text
Application passes a report definition + data/parameters to the rendering service
→ service processes the definition with data and returns the rendered document
→ an embedded viewer displays it; the user exports or prints from there
```

### Operate

Administrators manage the catalog (folders, types, search), access rights, shared data sources and credentials, shared schedules, and execution settings (caching, snapshots, execution history on platforms that offer them).

## Interfaces

### Report designer

The author's workbench: a layout canvas (banded or free-form), a data pane listing connections, queries, and fields (often called a dictionary), a parameter editor, an expression editor for computed values and conditional formatting, and a preview surface that renders the report with real or sample data.

### Report portal / catalog

The consumer's and administrator's entry surface: a navigable folder hierarchy or catalog of reports (often alongside related items such as shared data sources and datasets), with search, run-with-parameters, subscribe, export, and manage actions, plus access control per folder and item.

### Report viewer

The reading surface: the rendered document with page navigation, a parameter bar for re-running with different values, and a toolbar for export, print, search, and (where offered) interactive drill-down and sorting. In the embedded posture, the viewer is a component inside the host application.

### Subscription / schedule editor

The unattended-delivery surface: pick the report, the schedule (shared or report-specific), the parameter values for each run, the render format, and the destination.

## Important Rules / Behaviors

- **The definition is re-runnable; the output is an instance.** The same definition produces a fresh document each run; what consumers receive is one rendering of it at one point in time.
- **Delivered output is static.** Interactivity (drill-down, sorting, hyperlinks) lives in the live viewer. A report delivered by subscription — as an email attachment or a file-share document — is a static file; interactive features do not survive delivery.
- **Parameters gate execution.** A parameterized report prompts for values before running; subscriptions carry their own fixed parameter values, which can differ from the values used for on-demand runs.
- **Data access is governed separately from definitions.** Shared data sources hold the connections and credentials; changing a connection (test → production) does not change the reports that use it. Unattended execution requires stored credentials.
- **Pagination is computed at render time.** The rendering step decides page breaks, repeated headers/footers, and page numbering from the data and layout — the same report can produce a different page count as data changes.
- **Access control is report-level and folder-level.** Rights distinguish viewing from running, exporting, printing, and managing; authors and consumers hold different rights by design.
- **Point-in-time consistency is an operational concern.** Platforms commonly offer caching, snapshots, and report history so that many readers see identical data, and so past outputs remain comparable; availability varies by product.

## Variants

- **Server platform** — a managed catalog with portals, scheduling, security, and operations (the classic enterprise deployment).
- **Embedded component** — designers, rendering engines, and viewers shipped as libraries that developers integrate into business applications; the host application is the delivery surface and often the security boundary.
- **Standalone authoring tool** — a desktop report writer whose output is consumed through a viewer, export, or print; delivery machinery is minimal and the definition file is the artifact.
- **Layout paradigm** — banded layouts (header/data/group/footer bands) vs free-form positioned layouts vs table/region models; products differ, the fixed-layout invariant does not.
- **Audience emphasis** — internal operational reporting vs customer-facing document production (invoices, statements) vs developer-embedded reporting.
- **Bundled neighbors** — some products add dashboards, KPI tiles, or alerting beside their reporting core; these are adjacent capabilities, not the reporting center.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Business Intelligence Platform | interactive visual analytics over a governed hosted repository is the center; formatted reporting ships there as a capability (paginated-report engines), not as the center |
| Dashboard Platform | a standing live display consulted in place; a report is a document-shaped point-in-time output delivered to an audience |
| Data Visualization Application | produces the chart artifact itself from user-supplied data; reports *contain* charts among other document content |
| Ad-hoc Query Application | question-time interrogation with immediate results and in-place refinement; no standing formatted definitions, no delivery machinery |
| OLAP / Multidimensional Analytics Platform | the cube/multidimensional model is the defining object; reporting consumes data sources without requiring a cube |
| Customer Communication Management | high-volume customer-facing correspondence (bills, statements, policies) with personalization and regulatory content; overlap zone — reporting platforms also produce invoices and statements, but the organization-internal data report is the center |
| Regulatory Reporting Platform | filing/submission machinery for regulator deliverables (taxonomies, validations, submissions); a reporting platform has no submission machinery |
| ESG Reporting Platform | disclosure-production center (disclosure structure + data of record + deliverable); shares only the word "reporting" |
| Spreadsheet Application | the cell grid is the center; formatted output is a by-product, not a managed production-and-delivery pipeline |
| SQL Workbench / Analytical Query Editor | query-first tools with result grids; no standing report definitions or delivery |

The closest seam is the Business Intelligence Platform: modern BI estates ship paginated reporting as a capability, and reporting products add interactive elements. The structural test is the deliverable — if the product's center of gravity is the fixed-layout document produced and delivered to readers, it is this Type; if it is interactive exploration over a governed repository, it is BI.

## Representative Products

- Microsoft SQL Server Reporting Services / Power BI paginated reports (Report Builder, web portal)
- SAP Crystal Reports
- JasperReports Library + JasperReports Server
- Telerik Reporting
- Stimulsoft Reports

The sample spans the server-platform, standalone-writer, open-source engine, and embedded-component postures; the Core Model was checked against the desktop report-writer generation to avoid over-fitting to modern server deployments.

## Sources

Research date: **2026-09-09**

- Microsoft Learn — SQL Server Reporting Services overview, Report Definition Language (RDL), Reporting Services Reports, Subscriptions — https://learn.microsoft.com/en-us/sql/reporting-services/
- SAP — SAP Crystal Reports (product page) — https://www.sap.com/products/technology-platform/crystal-reports.html
- JasperReports Library (project README and Sample Reference) — https://github.com/Jaspersoft/jasperreports , https://jasperreports.sourceforge.net/sample.reference/README.html
- Telerik Reporting documentation — https://docs.telerik.com/reporting
- Stimulsoft documentation and user manual — https://www.stimulsoft.com/en/documentation

> Sourcing limitation: official documentation for Oracle Analytics Publisher (BI Publisher), IBM Cognos Analytics, the Jaspersoft community documentation portal, and Bold Reports could not be fetched from the research environment (blocked or JS-rendered). The template-based authoring paradigm sometimes associated with high-volume enterprise reporting is therefore not characterized in this document, and scheduling claims rest on the products whose documentation was reachable. Precise per-product format lists, limits, and defaults are intentionally not stated.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
