# Construction Reality Capture Platform

## Overview

A **Construction Reality Capture Platform** turns the physical state of a construction site into a hosted, dated, spatially organized visual record. Field teams capture the real work as it progresses — 360° imagery, drone data, smartphone photos and scans, laser-scan data — and the platform automatically organizes those captures against the project's floor plans, models, maps, or survey terrain. The result is a navigable visual history of the site that stakeholders can explore from anywhere, compare across dates, and check against design and schedule.

The problem it solves is visibility. Construction sites change daily, most decision-makers are not on site, and photographs scattered across phones and email folders cannot answer "what was built where, and when". This category of application exists to make the site itself the record: captured on a schedule, anchored to a location, accumulated over the project's life, and viewable without visiting.

Its boundary: the platform is the system of record for the site's *visual history* — not for field work items (defects, day logs), not for schedule and cost, not for authoring or coordinating models. It feeds those systems; it does not run them.

## Users & Context

The operating context is an active construction project, from groundbreak through handover.

Primary users:

- **Site personnel who capture** — superintendents, assistant project managers, and field engineers who walk the site with a 360° camera or phone, or pilot drones. In mature implementations capturing is designed to add little work: the walk someone was already doing becomes the capture.
- **Project staff who consume** — project managers and project engineers who review progress remotely, verify work in place, prepare reports, and answer questions from the record.
- **Remote stakeholders** — owners, owner's representatives, executives, consultants, and designers who need to see site conditions without traveling; a defining use of the platform is serving audiences who never hold a capture device.

Secondary users:

- **Specialists** — VDC/BIM staff who align models to captures, surveyors who supply high-accuracy data on earthworks-heavy projects, and quality/safety staff who use captures for verification.
- **External collaborators** — subcontractors and trade partners who receive location-pinned notes or limited viewing access.

At the analysis-focused end of the market, executives and owners are first-class users: portfolio views compare progress across many projects at once.

## Core Model

The defining structure of the Type has four parts. Each is load-bearing: remove one and the product stops being this kind of application.

### 1. The project site record

Everything hangs from a defined project or site — a named container, typically scoped to a location and a build. Captures, plans, models, annotations, and reports all attach to it. The container persists for the life of the project and is commonly retained after completion as the archived record of how the asset was built.

### 2. The dated capture

The unit of record is a **capture session** — a walked 360° pass, a drone flight, a phone-based scan or photo set, or a submitted survey dataset. Each capture is bound to its project and to the date it was taken. Captures are treated as historical evidence rather than working drafts: they are what later viewers will rely on when they need to know what the site looked like on a given day.

### 3. Spatial anchoring

A capture alone is just media. The platform's core transformation is binding captures to the project's **spatial reference** — floor plans for interiors, maps or survey terrain for sites, 3D models where BIM is used. Modern products do this automatically: imagery is mapped onto plans (often by AI that recognizes where the camera moved), drone data is processed into georeferenced maps and surfaces, and models are aligned to the captured imagery. Anchoring is what makes a capture *navigable* — a viewer can click a spot on the plan and stand in that room on that date.

### 4. The accumulated visual history

Captures accumulate into a **chronological series** across the project. The timeline is not an afterthought: the platform's value compounds with each capture, because any date can be compared with any other, and the series becomes the answer to "what was built when". This is the property that distinguishes a platform (a living record across the project) from a one-shot capture or scanning job (a single snapshot delivered as files).

### The hosted audience

The record exists to be viewed by people beyond whoever captured it. The platform hosts the history and controls access to it — project team members, other organizations, and outside stakeholders who may never hold an account. Without hosted remote access, a capture tool is just a camera workflow with a file drop.

### Standard capabilities layered on the core

Mature products commonly add, on top of the defining structure:

- **Design-versus-reality overlay** — floor plans, BIM models, CAD files, or design surfaces layered over the captured state, making visible what has been installed versus what was planned.
- **Progress tracking** — reading progress from captures, from a side-by-side visual comparison of dates up to AI-derived, element-level progress measured against the BIM model and schedule.
- **Measurement and quantification** — distances, areas, and (on the surveying-accurate end) earthworks volumes, stockpile quantities, and surface comparisons between dates.
- **Location-pinned notes and issues** — photos, comments, and markups pinned where they were made in the capture, often handed off to punch-list, observation, or issue workflows in field-management and project-management systems.
- **Processing pipeline** — captures are uploaded and processed before they become viewable; the capture is a managed object with a processing state, not an instantly visible file.
- **Sharing and reporting** — links, exports (images, PDFs, generated reports), timelapse-style outputs, and view-only access for outside parties.
- **Integration with construction platforms** — two-way connections to project-management and field systems, so captures and capture-pinned items flow into the tools where work is managed.
- **Administration** — user roles, per-project and per-site access control, and organization-level management.

## How It Works

### Set up the project record

```text
Create the project/site
→ upload the spatial reference (floor plans; optionally a BIM model; or define the site on a map)
→ invite team members and set access
```

The spatial reference is the substrate: without plans or a map, captures would have nowhere to anchor.

### Capture the site

```text
Walk the site with a 360° camera (or fly a drone / scan with a phone / survey with conventional instruments)
→ the capture session is recorded against the project and its date
→ upload (often automatic from the capture device)
→ platform processes the capture
→ imagery is pinned to plans / data is processed into maps and surfaces
→ the capture becomes viewable in the record
```

Who captures varies by product posture: some products are built so that any field worker can capture as a by-product of normal walks; others assume trained drone pilots or surveyors; several offer a managed service in which the vendor performs the capture.

### View and navigate remotely

```text
Open the project from anywhere
→ pick a plan, floor, or map area
→ open the capture from that location (click the plan point; follow the walked path)
→ look around the 360° imagery; step between capture points; move along the timeline
```

Navigation is plan-driven or map-driven rather than file-driven — the defining experience of the Type.

### Compare

Three recurring comparisons, all built on the same record:

```text
Date vs date:        same location, two dates, side by side — what changed, what is now covered up
Design vs reality:   plan or model overlaid on the capture — installed vs planned
Progress vs plan:    captures analyzed against schedule or model — what is complete, at what pace
```

The last of these ranges from manual visual judgment to AI-generated progress and delay-risk analysis depending on the product.

### Act on the record

```text
Measure something (distance, area, volume)
→ pin a note, photo, or issue at a location in the capture
→ route it to a trade partner or hand it off to a field/PM system
→ generate a report or share a view with someone outside the project
```

### Retain

The record persists through completion and handover. Documented uses include resolving disputes, answering post-completion questions about what was built inside finished assemblies, supporting insurance and claims processes, and feeding closeout documentation.

## Interfaces

Exact layouts vary by product; the following surfaces are the common vocabulary.

### Project dashboard

- Purpose: entry point listing the user's active projects/sites.
- Typical information: project list, recent captures, processing status, activity.
- Primary actions: open a project, start a capture, upload data, manage settings.

### Plan/map-anchored viewer

- Purpose: the main surface — navigate the site's visual history from its spatial reference.
- Typical information: floor plan or map with capture points, the 360° image or map view itself, timeline of available dates, capture coverage.
- Primary actions: open a capture at a point, move between points and dates, compare dates side by side, toggle design/model overlays, enhance imagery.

### Capture app (mobile)

- Purpose: field-side capture and quick reference.
- Typical information: current project/plan, recording state, capture checklist, nearby notes.
- Primary actions: record a walk, take pinned photos/notes, upload, review recent captures on the go.

### Upload / processing area

- Purpose: manage captures and survey datasets in flight.
- Typical information: capture list with status, processing progress, coverage and gaps.
- Primary actions: upload data, check status, review coverage, manage or delete captures.

### Measurement / analysis tools

- Purpose: extract quantities and conditions from the record.
- Typical information: measurement marks, surfaces compared between dates, volumes and stockpile figures, model or design overlays.
- Primary actions: draw and measure, compare surfaces between dates, inspect against design, review AI-flagged progress or defects where offered.

### Annotation / issue surfaces

- Purpose: turn observations from the record into tracked items.
- Typical information: location-pinned notes and photos, assignees, status of handed-off items.
- Primary actions: create a pin/note/issue, assign, export or convert into another system's workflow.

### Reporting and sharing

- Purpose: deliver the record to people who do not use the platform day to day.
- Typical information: selected captures and views, generated progress or condition reports.
- Primary actions: generate PDF/image/report outputs, create share links, grant view-only access, export data.

### Administration

- Purpose: govern access and configuration.
- Typical information: users and roles, per-project/site permissions, integrations.
- Primary actions: invite users, assign roles, share site access, connect external systems.

## Important Rules / Behaviors

### Captures are historical records, not drafts

The record's defining discipline is that dated captures persist and are not silently overwritten. Later captures do not replace earlier ones; the earlier state remains viewable. This is what makes the platform usable as evidence in payment verification, dispute resolution, and post-completion questions.

### A capture must be locatable

A capture that cannot be anchored to the plan or map cannot be navigated or compared, which is the point of the system. Products therefore invest in automatic image-to-plan mapping and allow manual correction of where media sits. Coverage matters too: a capture that missed rooms leaves gaps in the record, and products surface coverage so teams can see what was not documented.

### Processing intervenes between capture and view

Captured data is processed into a viewable, anchored state before stakeholders can use it. The latency and mechanics vary by product and data type; the structural point is that a capture is a managed object with a processing lifecycle, not an instantly visible photo.

### The record's value compounds with cadence

A single capture is a snapshot; the platform's defining value emerges from repeated captures over the project's life. Irregular capture weakens every downstream use — comparison, progress tracking, dispute evidence — which is why capture discipline (who captures, how often) is an explicit operating concern for adopting organizations.

### Access is organization-aware

Projects involve multiple independent organizations. Mature products let the project side invite members and outside stakeholders broadly, with roles distinguishing who can administer, who can capture and upload, who can annotate, and who can only view. Sharing to people without accounts (links, view-only access, shareable deliverables) is a standard pattern, because a large share of the audience is external.

### Content ownership and exit

Export paths are standard across the researched products — images, reports, measurement outputs, and in some products a complete project archive — so the record survives beyond the subscription. Explicit customer-ownership commitments are documented at some vendors; the strength of that posture varies by product.

## Variants

- **Capture-modality poles** — walk-first 360° documentation (the dominant pattern for building construction), aerial-first drone mapping, and multi-modal platforms that fuse 360 + drone + scan in one record.
- **Accuracy posture** — visual documentation grade for interiors and general progress vs survey-grade capture (ground control, precision positioning, processed surfaces) for earthworks, where quantities must be trusted.
- **Analysis depth** — from hosted visual history with manual comparison, to AI-derived element-level progress, schedule-integrated delay forecasting, and trade-performance analytics.
- **Earthworks machinery** — site-survey accumulation with volume-over-time comparisons, surface design conformance, and (in some products) live machine data overlaid on the same map.
- **Interior 3D scanning** — phone-based LiDAR/scan capture producing measurable interior records alongside 360° imagery.
- **Managed capture services** — the vendor performs captures (walks, flights, or full capture programs) as an alternative to self-capture.
- **Side of the table** — contractor-operated platforms focused on documentation and coordination vs owner/CM-operated deployments focused on oversight, verification, and portfolio visibility.
- **Adjacent extensions** — workforce/safety modules, AI safety and defect detection, fixed-camera or robotics integrations, and facilities-assessment postures that continue the record into operation.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Construction Field Management | manages field work items (day records, punch/defect items) with routing and verification; this Type produces the visual record those items are raised *from* — capture-pinned notes convert into field work items as a designed handoff |
| Construction Project Management | owns the project container, schedule, cost, and coordination records; this Type supplies dated visual ground truth into that container through integrations |
| BIM Authoring / BIM Coordination | author and coordinate models; here the model is a consumed reference for alignment and overlay, never authored |
| Photogrammetry Application | general-purpose 3D creation from photos of arbitrary subjects; here photogrammetry is one processing mechanism inside a construction-scoped record system with timeline and stakeholder semantics |
| Building Condition Assessment | quantified condition of existing buildings (element ratings, deficiencies); this Type accumulates construction-phase visual history without condition-rating machinery |
| Construction Closeout Management | assembles handover documentation at project end; the capture platform is one of the record sources it may draw on |
| Digital Twin Platform (operations-oriented) | centers on the operating asset's twin machinery; the overlap is the "as-built visual twin" idea, not operational twin management |
| Progress Billing | payment verification is a documented *use* of capture evidence, but money machinery lives in the billing/cost Types |

The nearest seam is Construction Field Management: both live on the site and both feed the same projects. The structural test is the unit of record — a dated, spatially anchored capture of site state (this Type) versus a routed work item or day record (Field Management). Products blur it deliberately by offering both, but the center of gravity differs.

## Representative Products

- OpenSpace — 360° walk-first documentation with automatic image-to-plan mapping, multi-modal ingestion, and AI progress tracking
- Reconstruct — multi-modal reality mapping fused with design overlay and schedule integration
- Buildots — AI progress intelligence comparing recurring captures against BIM and schedule
- DroneDeploy — aerial-first unified reality capture with ground/interior capture and AI analysis
- Propeller — survey-grade map-based earthworks and site analytics

## Sources

Research date: **2026-09-07**

- OpenSpace — product page (openspace.ai/products/capture) and Help Center incl. "Using OpenSpace" category (support.openspace.ai)
- Reconstruct — main site and product/solution pages (reconstructinc.com)
- Buildots — main site and product page incl. FAQ (buildots.com, buildots.com/product)
- DroneDeploy — main site (dronedeploy.com) and Help Center incl. Ground category (support.dronedeploy.com, help.dronedeploy.com)
- Propeller — main site (propelleraero.com) and Help Center incl. "Getting Started with the Propeller Platform" (help.propelleraero.com)

> Sourcing limitation: one vendor's operational help center was unreachable during research; that product's behaviors are evidenced by official product pages only, and vendor-stated figures (processing times, accuracy figures, capture rates, outcome percentages) were deliberately excluded from this document rather than asserted. Detailed product-by-product evidence is recorded in the paired Research Notes.
