# Org Chart Management

## Overview

An **Org Chart Management** application is the organization's system of record for its reporting structure: the people who make up the organization, organized under their managers, held as maintained records and rendered as the org chart the whole company sees.

The defining structure is small:

```text
People (and commonly positions/units) organized under managers
└── the reporting structure held as maintained records
    └── the org chart as the synchronized rendering of those records
        └── standing maintenance as people join, move, and leave
```

What makes this a distinct type of application rather than a drawing tool is that the chart is *data*: every box is backed by a record, and changing the chart changes the record (and vice versa). What makes it distinct from an HR system is where its center of gravity sits: not employee data or HR processes, but the who-reports-to-whom structure itself, kept current and made visible. What makes it distinct from organization design software is that it maintains and shares the structure *as it is* — proposing, measuring, and applying alternative future structures is a different type of application.

## Users & Context

Primary users:

- **HR / people-ops administrators** — own the chart of record: bring in people data, verify the structure, make or review changes, configure what the chart shows, and control who sees what
- **Leaders and managers** — navigate the structure, inspect their own part of the organization, and (in many products) maintain their own subtree

Secondary users:

- **All employees** — consume the chart and its directory layer to find out who does what, who someone's manager is, and who to contact
- **HR partners, finance, and auditors** — read the structure for staffing decisions, cost and compliance questions, and audit evidence

The context is standing, not episodic: the chart is consulted continuously as part of everyday collaboration ("who's who"), and it becomes especially active around onboarding, reorganizations, and reporting periods — the moments when the structure changes and when the organization needs a trustworthy current picture.

## Core Model

### The Defining Core

```text
Person record (and commonly: position, unit/group)
└── reporting line (manager ↔ direct report) as the structural edge
    └── the whole maintained as the structure of record
        └── rendered as the org chart — the structure's authoritative view
```

Three properties. If any one is removed, the product is no longer recognizable as this type:

- **The reporting structure of record.** People are held as records and organized under managers; the manager relationship is the edge that gives the structure its shape. Departments, teams, and other groupings commonly ride on top of this tree. Without the reporting structure, the product collapses into a flat contact list.
- **Chart and record as one thing.** The chart is not a drawing that someone redraws; it is generated from — and editable into — the maintained records. Edit the chart, and the record changes; change the record (directly or through a synced source), and the chart updates. Without this, the product is either a drawing tool (shapes with nothing behind them) or a bare data table.
- **Standing maintenance.** The product's ongoing job is absorbing organizational change: new hires appear, movers change managers, leavers disappear, branches are re-parented — and the chart stays current without being rebuilt. Without this, it is a one-off chart generator, and the "management" is gone.

### What Mature Products Add

These capabilities are widespread in current products and expected by the market, but none of them is what makes the product an org chart manager:

- **Employee directory and profiles** — photos, titles, contact details, and often bios or interests layered around the chart's people cards; many products are marketed as "org chart and directory"
- **Search** — finding people, jobs, or groups across the structure
- **Data sourcing** — people data arrives by automated HRIS/ERP integration, spreadsheet import, or manual entry; the sourcing mechanism is an implementation choice, not the definition
- **Visualization controls** — filtering and color-coding the chart by any attribute (department, location, level), zoom and orientation, saved views
- **Sharing and publishing** — interactive links for the whole company, exports to PDF/PowerPoint/PNG, print
- **A time dimension** — viewing the chart as it was in the past or as it will look when planned hires arrive
- **Open jobs in the structure** — some products show vacancies as part of the chart, not just in a recruiting tool
- **Permission-scoped visibility** — what each viewer sees on a card depends on their role

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:   the structure of record
Implementations:  records maintained in the product itself,
                  records mirrored from an HRIS/ERP by sync,
                  records built from spreadsheet import

Concept:   chart edits writing to the record
Implementations:  direct on-chart editing (drag to a new manager),
                  record forms behind each card,
                  changes made in the source system and flowed in

Concept:   publishing
Implementations:  always-live interactive links,
                  periodic PDF/PowerPoint exports,
                  embedded views in intranets
```

## How It Works

### Get the people in

```text
Connect a source (HRIS/ERP integration) or upload a spreadsheet
→ map fields (names, titles, departments, managers)
→ the product builds people records and links them by manager
→ verify and fix the structure (orphaned people, wrong managers)
```

There is no job architecture to author and no HR process to configure. The input is people and their reporting lines.

### Maintain the structure as the organization changes

```text
A person joins → added under their manager (from the source or by hand)
A person moves → their reporting line changes; their subtree moves with them
A branch is reorganized → teams re-parented; the chart re-shapes
A person leaves → removed (or marked vacant); downstream lines re-attach
```

In many products the chart itself is the editing surface: dragging a card to a new manager performs the reassignment on the record. In integration-coupled products, maintenance often happens in the source system and the chart follows automatically. Either way, the rule is the same: the chart always reflects the record.

### Consume and share

```text
Open the chart → navigate, zoom, expand reporting lines
→ search for a person, job, or group
→ filter or color-code by attribute; switch to a saved view
→ (where supported) slide back to a past date or forward to a planned state
→ share: send a live link, export to PDF/PowerPoint/PNG, print
```

The same structure serves two audiences at once: the maintainers who keep it truthful, and everyone else who reads it. The consumption loop is the reason the record is maintained.

### Core vs Common vs Optional

**Defining core** — without these, not org chart management:

- people held as records under manager relationships
- the chart as the synchronized, authoritative rendering of those records
- standing maintenance against joins, moves, leaves, and reorganizations

**Standard capabilities** — present in most mature products:

- directory/profile layer with photos and details
- search across people/jobs/groups
- HRIS/ERP sync or file import as the data path
- visualization controls (filters, color-coding, saved views)
- interactive publishing and document exports
- past/future time views
- permission-scoped card content

**Optional** — depends on segment and product:

- open jobs visible in the structure
- matrix / dotted-line rendering for complex structures
- summary (aggregated) chart views for very large organizations
- KPI overlays (span of control, layers, headcount) on the chart
- private planning charts — light copies of the structure for resource discussion
- audit/compliance export of structure data
- engagement features around the directory (interests, "who's who" activities)
- AI assistance over the structure

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Interactive chart canvas

The primary surface.

- typical information: people cards (name, title, department, often photo and key attributes), reporting lines, aggregate counts over subtrees, open jobs
- primary actions: navigate and zoom, expand or collapse branches, search, filter/color-code by attribute, inspect a card, open a profile

### Directory / people list

The table-style face of the same records.

- typical information: one row or card per person — photo, title, department, contact details
- primary actions: search, sort, filter, open a profile, jump to the person in the chart

### Person profile

One person's record.

- typical information: role, manager, direct reports, location, contact details, sometimes interests or extended attributes — constrained by the viewer's permissions
- primary actions: view reporting context (up and down), contact, edit (for authorized users)

### Maintenance surface

Where the structure is kept truthful.

- typical information: the chart in editing mode; import/mapping screens; field configuration
- primary actions: add/remove people, change managers (drag or form), re-parent branches, run an import or sync, resolve structural defects

### Share/export settings

- typical information: who can view the chart, what a shared view contains
- primary actions: create share links, export to document formats, configure what sensitive fields appear in shared artifacts

### Administration

- typical information: data-source connections, field mappings, permissions
- primary actions: configure sync, set visibility rules, manage roles

## Important Rules / Behaviors

- **The chart cannot drift from the record.** The chart's authority comes from being synchronized with the records behind it. Where the records come from an HRIS/ERP, synchronized fields follow that source; in-product edits and source updates need to be reconciled rather than silently diverging.
- **What you see depends on who you are.** Card content is permission-scoped — an employee, a manager, and an HR admin looking at the same card may see different detail.
- **Shared artifacts are curated.** When a chart leaves the product (export, screenshot, link), some products give maintainers control over what goes with it — for example, stripping sensitive or personal fields from exported images.
- **Structural defects are visible.** People without managers, people with impossible placements, and vacant positions are surfaced for correction, because every one of them distorts the structure everyone reads.
- **One tree, usually.** The primary reporting structure is a hierarchy; complex real-world organizations add secondary relationships (matrix or dotted lines) in some products rather than replacing the tree.
- **History and future are views, not forks.** Past and planned states are renderings of the record at a point in time; the current chart of record remains the single live structure. (Sandboxed copies of the structure for redesign work belong to organization design software, not this type.)

## Variants

- **Standalone chart builder** — self-serve products focused on building and sharing the chart and directory, often for smaller organizations, with spreadsheet import as the main data path
- **People-platform-centered** — org chart as the home surface of a broader people-operations platform (planning, reviews, surveys orbiting the same structure)
- **Enterprise charting over HR systems** — dedicated charting products that mirror large organizations out of ERP/HRIS systems, visualize complex structures, and serve compliance and reporting needs
- **Directory-forward vs record-forward** — some products emphasize the people-discovery experience (profiles, photos, connection); others emphasize structural fidelity to HR data
- **Scale extremes** — a two-hundred-person company's single chart versus a global enterprise needing aggregated summary views, multi-region structures, and historical comparison

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Organization Design Platform | closest sibling | shares the structural model but adds the scenario loop: propose alternative structures in an isolated copy, measure impact (cost, headcount, spans/layers), apply. This type maintains and publishes the *current* structure only — vendors ship the two as separate products, though some platforms bundle both |
| HRIS / HCM | upstream system | system of record for employee data and HR processes; its org chart is a feature view. This type's center is the reporting structure and its chart; its people data typically comes *from* the HRIS |
| Diagramming Application | superficially similar | draws org charts as shapes with connectors; no person records, no synchronization between chart and roster, no standing maintenance. The drawing tool is the pre-history this type replaced |
| Succession Planning Platform | adjacent talent process | works on coverage of key roles (slates, readiness); commonly navigates *via* an org chart but holds no structure-of-record semantics |
| Career Pathing Application | adjacent talent process | owns the career structure — roles, levels, progression links, requirements — not people placed in reporting lines |
| Workforce Planning Platform | adjacent planning | models headcount demand and supply over a time horizon; structure changes flow *out* toward the org chart of record |
| Intranet / Employee Portal | adjacent surface | may embed a people directory or chart as a feature; the structure is not the portal's managed record |

The most important boundary is with **Organization Design Platform**: both hold the same structural data, and modern products increasingly bundle both. The working test is the scenario loop — remove the ability to propose, measure, and apply alternative structures, and what remains is this type; remove the maintained current-structure chart of record, and what remains is organization design.

## Representative Products

- **Pingboard** (by Workleap) — standalone cloud org chart and employee directory for self-serve teams; HRIS integrations and spreadsheet import; planning charts for resource discussion
- **ChartHop** — org chart at the center of a mid-market people-operations platform; roster-driven chart with a time slider, permission-scoped profiles, and export
- **Nakisa Org Chart Suite** — enterprise charting over HRIS/ERP data (native integrations, matrix/dotted lines, historical charts, share links and PDF/PowerPoint/PNG export), sold alongside — but separately from — the vendor's org design suite

## Sources

Research date: **2026-09-08**

- Pingboard (Workleap) — product page and FAQ — https://www.pingboard.com/
- ChartHop Help Center — "Org Chart"; Help Center index — https://docs.charthop.com/org-chart , https://docs.charthop.com/
- Nakisa — Org Chart Suite product page — https://nakisa.com/products/org-chart-software/

> Sourcing limitation: two additional dedicated org-chart vendors (Organimi, OrgChart Now) and two diagramming-side sources could not be reached from the research environment (blocked or failed requests, two attempts each). Findings are calibrated to the three reachable products; details about unreachable products were not filled in from memory, and no market-share or numeric claims are made. The diagramming-tool boundary is supported by vendor statements and by the paired research notes' cross-references to previously documented sources.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
