# Business Intelligence Platform

## Overview

A **Business Intelligence Platform** is an organizational analytics system: it connects to data sources the organization already owns (databases, warehouses, files, business applications), lets analysts author curated analytics content — dashboards and reports built from visualizations and tables — hosts that content persistently in an organized repository, and distributes it to business consumers who view and interact with it without authoring rights, under permissions that govern both content and data.

Its purpose is to industrialize what ad-hoc spreadsheet analysis does informally: turn the organization's raw data into shared, governed, continuously refreshed insight that reaches decision-makers on their own terms.

The defining core is deliberately narrow:

```text
Connected external data sources
└── User-authored analytics content (dashboards / reports)
    └── Hosted persistent repository
        └── Consumer audience beyond the author
            └── Controlled access to content and data
```

Remove any element and the product becomes something else: remove the consumer audience and it is a single-user visualization tool; remove the hosted repository and it is desktop authoring software passing files around; remove authoring and it is a fixed metrics portal; remove the external data connection and it is analytics embedded inside one application; remove access control and it cannot safely serve an organization.

## Users & Context

Three roles recur across the category, with the first two structurally separated:

- **Authors / designers** (analysts, data-savvy business roles): connect and model data, build visualizations, compose dashboards and reports, manage the content lifecycle. Authoring is their job.
- **Consumers / business users** (managers, operators, executives): open published dashboards and reports, filter and drill into them, monitor metrics, receive scheduled deliveries and alerts. They do not build content; their interaction is exploration and reading.
- **Administrators** (IT, platform owners, governance teams): manage connections, users and groups, permissions, licenses, deployment, and the platform's health.

Typical context: an organization has data spread across operational systems and warehouses. Individuals already analyze fragments of it in spreadsheets. The platform exists so that analysis of the shared, important numbers happens once, on governed data, and is published — rather than recreated privately, inconsistently, and on extracts of unknown freshness.

## Core Model

### The defining core

```text
Data source (external, connected)
  → Data model (prepared, related — often shared and reused)
    → Analytics content (visualization → composed dashboards / reports)
      → Repository (hosted, organized, persistent)
        → Distribution (publish / share with an audience)
          → Consumers (view and interact, without authoring)
            → Access control (content permissions + data permissions)
```

Five structural elements, each essential to the Type:

- **Data source connection** — the platform connects to data that lives outside itself: relational databases, cloud warehouses, files, uploads, third-party business applications. The platform is a lens over the organization's data estate, not a self-contained data silo.
- **Analytics content** — authored artifacts composed of visualizations and tables: dashboards (curated screens for monitoring a topic) and reports (paginated or interactive analyses addressing a question). Content is created inside the product and is persistent, nameable, and versioned — not a throwaway query result.
- **Hosted repository** — content lives in the platform's own storage, organized into containers (workspaces, projects, spaces, collections), searchable, and current. This is what makes content a shared organizational asset rather than a file passed between people.
- **Consumer audience** — a distinct population beyond the authors views and interacts with published content. The author/consumer split is the Type's most characteristic structural feature: content is produced by few and consumed by many, and consumption does not require (or grant) building rights.
- **Controlled access** — permissions operate at two layers: over content (who can view, edit, manage each artifact) and over data (which rows and columns a viewer's identity may reach). Access control is a first-class subsystem, not an afterthought, because the repository would otherwise expose the whole organization's data to everyone.

### Standard capabilities

Mature products commonly add the following. They make the platform practical, but the product remains a BI platform without any single one of them:

- **Shared data/semantic layer** — data prepared, related, and (to varying depth) modeled once and reused across content: shared datasets, defined measures and metrics, curated starting points for new analysis. Depth ranges from thin field metadata to a fully governed model layer with its own permissions.
- **Interactive consumption** — consumers filter, sort, highlight, and drill into published content; personal views or bookmarks let individuals keep their own angle on shared artifacts.
- **Self-service exploration** — an interactive question loop for authors and, within governed limits, consumers: visual query builders, field-drag composition, search over data, natural-language questions, drill-through from any chart to finer detail.
- **Scheduled delivery** — subscriptions that email or push dashboard/report snapshots on a schedule, so consumers who never open the platform still receive its output.
- **Data-driven alerts** — notifications when a metric crosses a threshold, monitored against the live data.
- **Data freshness management** — scheduled refresh of connected data; a choice between live querying and cached/extracted data; schema syncing of sources.
- **Content organization and discovery** — containers, search, tags, favorites; in some products explicit certification or verification marks that distinguish trusted, endorsed content from exploratory work.
- **Content lifecycle** — revision history, restore, deletion; the ability to update published content without breaking its audience.
- **Embedded analytics** — distributing content inside other applications: links, embeddable views, SDKs, white-labeling — often for serving analytics to customers rather than employees.
- **Mobile surfaces** — apps for consuming dashboards on phones, in the larger enterprise products.
- **AI assistance** — natural-language Q&A over governed data, automatic insight generation, AI agents scoped to the platform's content.
- **Administration** — user and group management, single sign-on, usage analytics about the platform itself, licensing.

### One structure, many implementations

The core model is written conceptually. Products realize it differently, and a reader familiar with only one realization should still recognize the others:

```text
Concept:      Data source connection
Realizations: direct database connections, warehouse connectors,
              file/upload pipelines, SaaS application connectors

Concept:      Shared data model
Realizations: published shared datasets, semantic models with defined
              measures, modeled tables/metrics layers, thin field metadata

Concept:      Analytics content
Realizations: interactive dashboards, multi-page reports, story/narrative
              formats, formatted printable reports

Concept:      Repository container
Realizations: workspaces, projects, sites, spaces, collections

Concept:      Distribution container
Realizations: published app bundles, shared folders/links, embeddable
              surfaces, scheduled email digests
```

## How It Works

The platform runs a continuous lifecycle rather than a single workflow:

### 1. Connect and model the data

```text
Register a connection to an external source
→ prepare the data (clean, relate tables, define fields)
→ (commonly) define shared measures/metrics once
→ save as a reusable, permissioned data model
```

This step creates the platform's data foundation. Everything built later inherits from it, which is why models are typically shared objects with their own access rules.

### 2. Author analytics content

```text
Pick a data source or shared model
→ build visualizations (select fields, choose chart forms, set filters)
→ compose them into a dashboard or report (layout, text, cross-filtering)
→ save into a workspace/project
→ iterate: revise, version, (in some products) request certification
```

Authoring ranges from drag-a-field visual composition to structured page design. The platform usually re-renders the visualization live as fields are chosen, so authoring is itself an exploratory loop — a question, a chart, an adjustment, a re-render.

### 3. Govern

```text
Assign content permissions (who may view / edit / manage each artifact)
→ assign data permissions (which rows/columns each person may reach)
→ (commonly) mark trusted content as certified or endorsed
→ track revisions
```

Governance is continuous, not a setup step: every published artifact carries an access policy, and the data beneath it is filtered by the viewer's identity at query time in mature products (data-level security).

### 4. Distribute

```text
Publish content from the working area to a consumption surface
→ grant an audience (group, department, whole organization, external users)
→ optionally bundle related dashboards/reports into a named deliverable
→ add scheduled delivery (email digests) and alerts on key metrics
→ (commonly) embed into other applications or expose mobile views
```

Distribution is the step that distinguishes a platform from an authoring tool: content moves from a building context to a consumption context. Products realize the handoff in two postures — some stage content in a working area and release it to the audience through an explicit publish step, while others treat saved content as immediately live and rely on permissions and revision history to manage what the audience sees.

### 5. Consume and explore

```text
Open the platform (web, mobile, embedded) or receive a scheduled digest
→ find the relevant dashboard/report via containers or search
→ interact: filter, drill, sort, highlight
→ (within granted rights) explore further or even build personal content
   from the same shared models
→ unresolved questions flow back to authors or to self-service
```

Consumers without authoring rights still interact meaningfully — the published content is live analytics, not a static picture. Where rights allow, consumers extend the system themselves: personal copies, new reports built on shared models, saved questions.

### 6. Maintain

```text
Data refreshes on schedule (or queries live)
→ content is revised; revisions are tracked
→ usage analytics show what is actually consumed
→ stale content is retired; breaking changes are managed
```

The loop then repeats: new questions produce new content, which is governed and distributed again.

## Interfaces

The following surfaces recur across the category. Exact layouts and names vary by product.

### Authoring canvas (desktop or web)

Where content is built.

- data/model picker, field lists, visualization area, property panes
- live re-rendering as fields and options change
- primary actions: build a visualization, compose a dashboard/report, save to a workspace

### Dashboard / report consumer view

Where published content is read.

- the composed artifact with its visuals, filters, and drill affordances
- personalization hooks (bookmarks, custom views) where offered
- primary actions: filter, drill into detail, export, share, subscribe

### Content repository browser

The platform's catalog of what exists.

- containers (workspaces/projects/spaces/collections), search, recent/favorites
- per-item metadata: owner, last modified, description, certification status
- primary actions: open, organize, share, manage access

### Data and model management surface

Where the data foundation is shaped.

- connections, tables, relationships, defined measures/metrics, refresh schedules
- primary actions: add/edit connections, model data, publish a shared model

### Administrative console

Where the platform itself is run.

- users/groups, permission policies, license/capacity settings, audit/usage views
- primary actions: grant access, configure governance, monitor adoption

### Mobile and embedded surfaces

- read-oriented renderings of published content, scaled to phones or to the UI of another application
- primary actions: view, filter, drill; limited or no authoring

## Important Rules / Behaviors

### Viewing and building are separate rights

The platform's permission model decouples consumption from authorship. A viewer can see a dashboard without being able to edit it, see the model beneath it, or even export its data. Escalation paths (build rights on shared models, edit rights in workspaces) are granted explicitly, not implied by visibility.

### Content and data access are separate layers

Two permissions govern every interaction: whether the person may open this content, and which data they may see within it. Data-level security means two viewers of the same dashboard can see different numbers, filtered by their identity at query time. Product-specific implementations differ in mechanism, but the two-layer structure is common to mature products.

### Dependencies create permission chains

A dashboard typically depends on reports, which depend on data models. Removing, hiding, or restricting access to a dependency can break or empty the content that references it, and sharing downstream content usually requires that the audience can also reach what it is built on. Mature products document and enforce these chains explicitly.

### Published content is stateful

Distribution creates a consumption context that can accumulate consumer-side state — personal bookmarks, comments, subscriptions. In products that stage content behind an explicit publish step, updates flow through republishing and are managed deliberately; in products where content is edited live, changes reach the audience immediately and safety rests on permissions and revision history. Under either posture, removing published content typically destroys the consumer-side state attached to it, which makes retirement a governed operation rather than a file deletion.

### Freshness is a managed property

Every artifact stands on data that is either queried live or served from a cache/extract refreshed on a schedule. Which mode applies is a consequential configuration choice (latency versus load), and content typically indicates or depends on its freshness.

### The question loop is bounded by governance

Self-service exploration exists inside limits: which sources a person may query, which models they may build on, which rows their queries return. The platform's openness ("everyone can analyze") is always realized through its permission system.

## Variants

Common forms of the Type:

- **Enterprise analytics standard** — large organizations, IT-governed, full governance stack, capacity/licensing tiers, content DevOps.
- **Team self-service BI** — lightweight deployment (often open-source or low-cost cloud), fast setup, permissions kept simple; governance depth traded for adoption speed.
- **Ecosystem suite module** — the BI platform sold inside a broader data stack (data integration, catalog, ML, automation in one vendor cloud); workspaces may hold neighboring artifact types side by side.
- **Embedded/OEM analytics** — the platform repurposed to serve analytics inside another vendor's product; multi-customer isolation, white-labeling, and embedding SDKs become first-class.
- **Desktop-author + cloud-consume hybrid** — heavy authoring in an installed application, consumption in the web/mobile service; the repository bridges them.
- **Web-only platforms** — authoring and consumption both in the browser; no installed component.
- **Search/AI-first analytics** — conversational and search interactions promoted to the primary surface, with dashboards as one output among several.
- **Deployment postures** — vendor-operated cloud, client-managed/self-hosted installations (including open-source editions), and hybrids.

A variant remains a variant while the defining core holds. When a product's center of gravity moves wholly into a neighboring Type's structure — pure formatted-report production, pure ad-hoc querying without a repository/audience, code-first analysis — it is drifting toward that Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Ad-hoc Query Application | closest capability seam | centers the interactive question loop itself (compose → run → refine); its saved questions may feed BI content, but the loop alone has no hosted repository, no consumer audience, no governance lifecycle. In today's market the loop is commonly bundled inside BI platforms as a capability |
| Dashboard Platform | partial overlap | centers one artifact form (dashboards) as a lightweight composition/sharing surface; a BI platform adds the data-model layer, full governance, and the broader artifact/lifecycle estate |
| Reporting Platform | adjacent | centers formatted, document-shaped output and its scheduled delivery; BI centers interactive visual analytics over a governed repository. BI platforms commonly ship formatted reporting as a capability |
| Data Visualization Application | adjacent | centers chart/visual authoring; typically single-user or file-based, without a hosted repository, consumer audience, or access governance |
| OLAP / Multidimensional Analytics Platform | adjacent | centers the multidimensional cube model (dimensions/measures, slice-drill navigation); BI is model-agnostic and consumption-lifecycle-centered, and has largely absorbed OLAP-style interactions |
| Data Warehouse Platform | substrate | stores and serves data at scale; no authored consumer content. The BI platform connects to it and is one of its principal clients |
| Analytical Query Editor / SQL Workbench | feeding tool | authors and runs queries and returns result sets; BI curates analyses into persistent governed content. Editors feed BI surfaces; the center of gravity differs |
| Data Science Workbench | adjacent | code-notebook analysis for modeling/statistics; BI serves governed visual analytics to business consumers. Some platforms host both as sibling surfaces |
| Data Explorer / Public Data Portal | different core | explores curated published datasets through a portal frame, without user-owned connections, authoring, or organizational governance |
| Process Mining Platform | different derivation | derives case sequences and process models from event logs; BI aggregates generic measures over governed data |
| Enterprise AI Assistant | different center | conversational access to knowledge and tasks; AI features inside BI platforms are capabilities of this Type, not the assistant Type |

The most consequential seam is with the **Ad-hoc Query Application**: the interactive question loop is a core capability of every BI platform, and query-first products name that loop's artifact as their core object. The structural test in both directions — strip the platform to the loop, or wrap the loop in repository + audience + governance — keeps the two Types distinguishable even though one is almost always bundled inside the other.

## Representative Products

- Tableau
- Power BI
- Qlik Cloud Analytics
- Metabase

These span the visual-analysis, ecosystem-suite, associative-exploration, and lightweight self-service philosophies, and four customer tiers from teams to global enterprises. ThoughtSpot and Zoho Analytics were additionally examined in a paired research pass on the ad-hoc query capability.

The definition was checked against forms outside the current market: classic enterprise BI suites of the 2000s (server-hosted metadata models, report authoring, security, scheduled distribution) satisfy the core without any modern feature; reporting-first products sit nearer the Reporting Platform; spreadsheet analysis lacks the platform structure and sits outside the Type.

## Sources

Research date: **2026-09-06**

- Tableau — Get Started; Build a Basic View to Explore Your Data; Use Tableau on the Web (help.tableau.com, current release)
- Power BI — Power BI service basics: key concepts and terms; Publish an app in Power BI (learn.microsoft.com)
- Qlik — Qlik Cloud Help: Welcome; Using analytics to explore data (help.qlik.com)
- Metabase — Dashboards overview with documentation structure (metabase.com/docs)
- Paired-pass sources (same research date): ThoughtSpot docs index and Answer experience (docs.thoughtspot.com); Zoho Analytics help center and User Guide (zoho.com); Power BI Desktop overview pages (learn.microsoft.com)

> Sourcing limitations: Looker (Google Cloud) documentation was unreachable (repeated timeouts across two research passes), so the semantic-model-first philosophy is evidenced through other products and no product-specific claims are made about it. IBM Cognos documentation returned access errors, so the classic-enterprise historical check rests on documented category history rather than fetched pages, and the final document avoids precise historical claims. Qlik evidence is at help-structure level; deep engine mechanics are not asserted. Product-specific numeric limits, license tiers, and defaults appearing in vendor documentation were deliberately excluded from this document and kept in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, capability-tier classification, and boundary analysis against all neighboring Types are recorded in the paired Research Notes.
