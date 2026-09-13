# Contaminated Site Management

## Overview

A **Contaminated Site Management** application keeps the authoritative record of land and water sites affected — or suspected of being affected — by contamination, and manages each site through its environmental lifecycle: investigation and assessment, remediation, long-term monitoring, and closure, with the site retained as a record even after closure.

Its purpose is to make a site's contamination condition knowable, provable, and manageable over years or decades: what was found, where and when it was measured, how results compare against regulatory criteria, what has been done about it, and what remains to be done — with every step attributable, because these records face regulators, auditors, land-use decisions, and sometimes litigation.

The defining core is small:

```text
Contaminated Site (identified, located place; persists across decades, incl. after closure)
└── Contamination profile (suspected vs confirmed; contaminants × media)
    └── Cumulative evidence (dated, attributed assessments, sampling events, results, documents)
        └── Managed progression (investigation → remediation → monitoring → closure)
            └── Retained register (closed sites remain part of the record)
```

Everything else commonly associated with the category — cloud delivery, GIS maps, automated electronic lab feeds, statistics, AI queries, public portals — is widespread in current products but not part of what makes the application this Type. Paper site registers with attached sampling reports and a status column satisfy the same core.

When the application's center shifts to the data corpus itself (any environmental program's lab and field data, without a site-contamination lifecycle), it is drifting toward a different Application Type (Environmental Data Platform). When it centers on executing remediation projects, it drifts toward Environmental Remediation Management; when it centers on performing the assessment fieldwork, toward Environmental Site Assessment.

## Users & Context

Primary users:

- **Environmental consultants** — plan and run sampling programs on contaminated sites, load and validate laboratory results, compare them against guideline values, and produce the chemistry tables, charts, and maps that go into regulatory reports.
- **Site owners and responsible parties** (industrial, petroleum, defense, utilities, landfills) — consolidate data from multiple consultants across a portfolio of sites, keep long-running obligations under control, and answer "where does contamination stand?" for management and regulators.
- **Regulator / cleanup-program staff** — receive data submissions from external parties, keep the register of contaminated and potentially contaminated sites, track program cases through their stages toward closure, and publish public information.

Secondary participants: laboratories (deliver results into the system), environmental auditors and reviewers, and — in agency-facing deployments — the public, who may consult published site information.

The working context is distinctive: site work runs for years to decades; project teams and consultancies turn over; evidence must stay attributable and defensible long after the people who produced it have moved on. Deliverables are formal — regulatory reports, verification documents, public registry entries.

## Core Model

### The Defining Core

Five elements. If any one is removed, the product is no longer recognizable as contaminated site management:

- **The contaminated site record** — an identified, located place (a named site with an identifier, address, coordinates, commonly parcel or facility references) held as a managed unit because of actual or suspected contamination of its media — soil, groundwater, surface water, sediment, soil vapor. Its identity persists across years or decades, including after work stops or the site is closed. Without the site anchor, the product is a data system, not a site record.
- **The contamination profile** — what is suspected or confirmed about the site: which substances, in which media, in which parts of the site. The profile starts as a concern (historical land use, a spill, a complaint) and firms up as evidence accumulates.
- **Cumulative evidence** — the site's understanding is built from dated, attributed records attached to the site: assessments and investigations, sampling events, laboratory and field results, inspections, reports. Evidence accumulates and is qualified rather than replacing what went before; superseded readings remain part of the history.
- **Managed progression** — the site's phase of work (investigation and assessment → remediation → monitoring / post-closure care → closure) is tracked as managed state, advanced by recorded activities and events — sampling events, exceedances, completed actions, submitted reports. The site's standing is always expressible.
- **The retained register** — the site remains part of the record after closure. Contamination does not disappear when work ends; registers keep closed sites so future land-use and re-development decisions can account for them, and new evidence can reopen a site's file.

### Capabilities Shared by Mature Products

These make the core work in practice. They are not what makes the product this Type, but they are how the Type is realized today.

- **Criteria comparison** — managed libraries of regulatory guideline values and action levels (regional sets pre-loaded is the common pattern), plus site-specific limits, with matrix and depth dependencies supported. Results are compared against criteria on summary chemistry tables, maps, and graphs; exceedances surface as flags and alerts.
- **Validated data ingestion** — laboratory results arrive as electronic deliverables and are loaded, unit-converted, checked (holding times, duplicates, blanks, ionic balance), and flagged; manual entry and field capture are parallel paths.
- **Sampling machinery** — planning and scheduling of sampling events, recurring monitoring programs, field data capture (increasingly mobile), and sampling-location registers (wells, boreholes, soil points).
- **Location and spatial context** — sampling locations bound to coordinates; map surfaces showing results in place; interchange with GIS platforms.
- **Analysis and visualization** — time-series trends, summary statistics, contouring and subsurface views of plumes and concentrations.
- **Reporting outputs** — reproducible, formatted tables, charts, and reports; exports into regulatory program formats where a regime requires them.
- **Portfolio / multi-site operation** — querying and rolling up across many sites and projects (e.g., every recent exceedance of a substance across an entire portfolio), with enterprise access control.
- **Notifications and tasks** — exceedance alerts, monitoring reminders, and task tracking for remediation-phase and post-closure work such as equipment maintenance.
- **Governance** — roles and permissions, provenance of data and edits, audit-ready retention; security certification posture in cloud products.
- **Integration spine** — GIS, business intelligence tools, spreadsheets, and APIs feeding the site data into wider reporting landscapes.
- **Transparency surfaces** — publishing approved results or site information outward, from internal stakeholder transparency to public portals, depending on the deployment.

### One Structure, Many Implementations

The core model is conceptual. Current products realize each element differently:

```text
Concept:            Contaminated site record
Implementations:    named site/project with ID + coordinates + address; parcel-linked records

Concept:            Evidence
Implementations:    electronic lab deliverables, field forms/mobile capture, data-logger
                    feeds, scanned historical reports

Concept:            Managed progression
Implementations:    phase fields and project structure (data-led products);
                    explicit status codes in a case register (agency-style deployments)

Concept:            Criteria
Implementations:    pre-loaded regional guideline libraries; site-specific action limits

Concept:            Retained register
Implementations:    internal portfolio lists; published public site indexes
```

A reader who has only seen one realization (e.g., a consultant lab-data workbench) should still be able to recognize an agency site register, or a custodian's multi-consultant portfolio system, from the core model.

## How It Works

### A site enters the system

```text
Concern arises (spill report, complaint, historical land use, transaction or
redevelopment screening)
→ site created as a record: identity, location, initial contamination profile
→ historical data and documents loaded or scanned
```

### Evidence accumulates

```text
Plan a sampling event (locations, analyses, QC samples)
→ field crews collect samples and field measurements
→ laboratory delivers validated results
→ results loaded, checked, and qualified (errors flagged, units converted)
→ results compared against guideline values → exceedances flagged
→ trend charts, maps, statistics updated; the site's record grows
```

This is the recurring interaction loop of the Type, and it repeats for years — monitoring rounds on long-running sites are scheduled events, not one-off projects.

### Assessment and decisions

Assessment findings, chosen options, and regulator decisions are recorded on the site. The profile firms from suspected to confirmed (or is cleared); the site's standing moves forward through recorded milestones rather than informal edits.

### Remediation and monitoring

```text
Remediation phase recorded
→ ongoing data streams (treatment systems, monitoring wells) tracked
→ tasks for operation and maintenance scheduled and completed
→ recurring monitoring events compare results against cleanup criteria
→ trends and statistics evidence progress toward the cleanup goal
```

### Closure and after

```text
Verification and closure decision recorded
→ site moves to closed standing — and remains in the register
→ monitoring may continue; the history stays queryable
→ new evidence can reopen the file
```

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- the site record (identified, located, persistent)
- the contamination profile
- cumulative, attributed evidence
- managed progression across the lifecycle
- retention after closure

**Standard capabilities** — present in most modern products:

- criteria/guideline comparison with exceedance machinery
- validated lab-data ingestion and QA checks
- sampling planning and field capture
- maps/GIS interchange
- trends, statistics, visualization
- regulatory-format reporting
- multi-site/portfolio operation
- notifications, tasks, governance, integration spine

**Variant / optional** — depends on operator, regime, and deployment:

- public portals and registry publishing
- AI-assisted querying
- financial/liability tracking depth
- any specific regulatory format, region, or program packaging

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Site register / portfolio list

The entry surface: the population of sites with identity, location, and standing.

- lists sites with status/phase, key dates, and headline indicators
- filters by status, program, geography, organization
- primary actions: open a site, add a site, run a cross-site query

### Site detail (timeline)

The heart of the product for a single site.

- the site's profile, phase/standing, and its history as a timeline of events — sampling events, results loaded, exceedances, reports, actions, decisions
- primary actions: add or review evidence, update standing, attach documents, generate outputs

### Data workbench

Where results are worked.

- result grids, exceedance tables, query builders (from quick filters to structured custom queries, sometimes saved and shared)
- primary actions: load/validate data, query and compare against criteria, produce tables and charts

### Map view

Results and locations in space.

- sampling locations, wells, exceedances plotted on basemaps; plume visualization at the deeper pole
- primary actions: inspect locations, visualize results spatially, export GIS layers

### Sampling / monitoring planner

The forward-looking surface.

- planned and recurring events, assignments, QC planning, completion state
- primary actions: schedule events, dispatch crews, record completion

### Document library

The site's paper trail.

- reports, assessments, verification documents held against the site
- primary actions: attach, retrieve, publish

### Reporting / exports

Regulatory and stakeholder outputs.

- formatted tables and charts, report-ready exports, regulatory program formats where applicable

### Administration

- standards and criteria libraries, valid values and synonyms, user roles, data governance settings

## Important Rules / Behaviors

### Evidence is bound, dated, and attributed

Every result belongs to a site, a location, and a date. This binding is what makes the record defensible; the application enforces it structurally rather than trusting free-form entries.

### Results are qualified, not silently overwritten

When values change or are re-analyzed, the discrepancy is flagged and the history retained — validation checks surface issues such as expired holding times, duplicate results, and blank contamination on load. The old value does not vanish; it is superseded.

### Criteria comparison drives the system's attention

Exceedances are computed against the managed criteria set and surface automatically as table highlights, map symbols, and alerts — users do not hunt for them by hand. Site-specific limits sit alongside regional guideline sets.

### Standing changes are recorded events

A site's phase or status advances through recorded, attributable actions (a completed assessment, a remediation milestone, a closure decision), not through untracked edits. Exact status vocabularies vary by product and regime; the managed-progression discipline is the constant.

### The record outlives the team

Retention is a designed behavior: long-running sites accumulate decades of data; closed sites remain in the register; consistency machinery (saved queries, shared formats, documented provenance) keeps the record usable across staff and consultant turnover.

### Visibility is a deployment decision

Owner and consultant deployments are typically confidential with role-scoped access; regulator deployments add public transparency — published site indexes or approved-results portals. Both postures fit the Type.

### Regional regimes shape vocabulary, not structure

Program names, status labels, and report formats differ by jurisdiction (state and federal cleanup programs, national risk-management frameworks, regional guideline sets). The lifecycle discipline — assess, remediate, verify, monitor, retain — is the shared structure beneath them.

## Variants

Common forms of the Type:

- **Consultant workbench** — per-project environmental data management for consultancies running site investigation and monitoring on behalf of clients
- **Owner / custodian portfolio** — organizations (defense estates, industrial groups, utilities) consolidating multi-consultant data for their own portfolio of contaminated sites into one system of record
- **Agency / program register** — regulator-side platforms receiving third-party data submissions, keeping the cleanup-program site register, and tracking cases toward closure, often with public lookup surfaces
- **Center-of-gravity poles** — data-led products (the lab-data engine first) vs register/case-led deployments (site status and program workflow first)
- **Regime packaging** — products oriented to specific regulatory frameworks and their report formats; regional guideline libraries as the criteria substrate
- **Program contexts** — petroleum and leaking-tank sites, industrial and chemical sites, defense and legacy sites, mining, landfills, emerging contaminants (e.g., PFAS), vapor intrusion
- **Scale and delivery** — single-site SaaS to multi-tenant enterprise platforms to self-hosted installations; AI-assisted querying appearing at the current era's leading edge

## Related Application Types

| Application Type | Distinction |
|---|---|
| Environmental Data Platform | centers the environmental data corpus across any program (compliance monitoring, water/air quality) without a site-contamination lifecycle; here the site record, its lifecycle, and its retention are the spine — the sampled market overlaps heavily, so the seam deserves joint review |
| Environmental Site Assessment | the assessment process and fieldwork application; here an assessment is a record attached to the site and its results become evidence — a designed handoff, not the same Type |
| Environmental Remediation Management | execution of remediation projects (plans, contractors, treatment systems, schedules); here remediation is a lifecycle phase plus its data streams and tasks — one overlap zone where products span both |
| Environmental Monitoring Platform | ongoing monitoring of operating facilities and parameters; here monitoring is the investigation and post-closure phase of a contaminated site, evaluated against cleanup criteria |
| Environmental Incident Management | a spill or release event and its response; here an incident is typically one discovery path that opens a site record |
| Hazardous Materials / Waste Management | materials and waste logistics; here the concern is the site and its media, not the movement of materials |
| Government GIS / Land Records | the spatial and cadastral base is consumed as context; the site record is owned by the contamination frame, not the land-registry frame |
| Environmental Compliance Management | organization-wide compliance programs and obligations; here the managed unit is the individual contaminated site and its evidence |

## Representative Products

- **ESdat** (EScIS) — consultant- and government-facing environmental data management with contaminated-land lineage; guideline libraries, exceedance machinery, public portal
- **EQuIS** (EarthSoft) — enterprise environmental data platform widely used in site investigation and remediation, including agency and federal program data flows
- **Locus EIM** (Locus Technologies) — cloud environmental information management spanning remediation projects and post-remediation operation, with multi-site portfolio querying
- **EnFlection** (Trihydro) — system of record for site remediation, post-closure monitoring, and active site operations across US regulatory frameworks

The core model was checked against the operator poles (consultant, custodian, agency) and against pre-software practice (paper site registers with attached sampling reports) to avoid over-fitting to the current data-led implementation.

## Sources

Research date: **2026-09-07**

- ESdat — https://esdat.net/ , https://esdat.net/government/ , https://esdat.net/environmental-standards/ , https://esdat.net/nz-department-of-defence-manage-their-contaminated-sites-data/
- EarthSoft (EQuIS) — https://earthsoft.com/products/professional/ (product-family structure from official site navigation)
- Locus Technologies (EIM) — https://www.locustec.com/applications/environmental-information-management/ , https://www.locustec.com/applications/environmental-information-management/remediation/
- Trihydro (EnFlection) — https://www.trihydro.com/digital-services/enflection/
- GOV.UK, Land Contamination Risk Management (Environment Agency et al.) — https://www.gov.uk/guidance/land-contamination-how-to-manage-the-risks (domain process context)

> Sourcing limitations: several candidate sources could not be reached on 2026-09-07 — TerraBase (403), a US state cleanup-site portal (403), and a state public-lookup site (404). The regulator/agency register pole is therefore documented at reduced strength, from structural evidence (agency data-intake features, named state/federal data formats in product documentation, and public risk-management guidance) rather than direct examination of an agency register product. Precise numeric claims (vendor-published data-volume counters, user counts) are excluded from this document and kept in the Research Notes. No precise operational parameters (limits, defaults, status-code sets) are asserted.
