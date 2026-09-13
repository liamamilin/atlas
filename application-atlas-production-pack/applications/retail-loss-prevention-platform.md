# Retail Loss Prevention Platform

## Overview

A **Retail Loss Prevention Platform** is a retailer-side operational system for detecting, recording, investigating, and resolving loss — theft, fraud, error, waste, and safety events — across a retail estate. It sits between the systems that generate business activity (point of sale, e-commerce, inventory, video, alarms) and the loss prevention / asset protection team that must respond to what that activity reveals.

The defining core is small:

```text
Loss event records (typed by cause, bound to location and time)
└── Managed response workflow (review → investigate → recorded disposition)
    └── Estate-level aggregation (patterns across locations and time)
```

Everything else commonly associated with the category — exception-based reporting over POS data, audit management, organized-retail-crime (ORC) case linking, law-enforcement collaboration, video correlation, recognition technology, returns-fraud decisioning — is standard or optional capability layered on that core, not what makes the product a loss prevention platform. A product that only generates exception reports without managing the response falls short of the Type; a product that only records incidents without estate-wide aggregation is a store-level tool, not a platform.

The platform is deliberately not several neighboring things: it does not own stock records (that is the inventory system), does not create transactions (that is the POS), does not manage cameras (that is a video management system), and does not run legal or corporate investigations in general (that is corporate investigation management). Its object is the retail loss event and the response to it.

## Users & Context

Primary users:

- **Loss prevention / asset protection analysts** — the central operators. They review exception alerts, decide what is a genuine loss signal, and open cases.
- **Investigators** — conduct case work: assemble evidence, link related incidents, identify repeat subjects, prepare law-enforcement packages, and manage recovery.
- **Field and district LP leaders** — supervise caseloads across a set of stores, prioritize what gets investigated, and drive prevention actions in their region.

Secondary users:

- **Store managers and associates** — report incidents from the floor, execute audits, respond to alerts and intelligence about known subjects.
- **Corporate LP executives** — consume the aggregate picture: shrink by cause and location, case close rates, time-to-close, recovery amounts.
- **Law enforcement officers** — in some deployments, a collaboration surface gives them access to packaged case evidence (see Variants).

The working context is a multi-location retailer. The rhythm of use is: a daily stream of exception alerts to review, incident reports arriving from stores as events happen, ongoing investigations that persist for days or weeks, and periodic audit campaigns. Work happens on desktop consoles for analysts and investigators, and on mobile devices for store staff and field leaders.

## Core Model

### The Loss Event

The central object is the **loss event** — a discrete, recorded occurrence of loss or loss risk. Every loss event carries:

- a **loss-cause classification** — external theft, internal (employee) theft, transaction fraud or abuse (refunds, voids, discounts, cash manipulation), administrative error, waste or damage, safety incidents
- a **location** — the store or site where it occurred; location is a first-class dimension of every record
- a **time**
- typically a **value** — the amount at risk or lost

Loss events enter the system through two inlets:

- **Field-reported incidents** — store staff, LP staff, hotlines, or automated imports file what happened: a shoplifting event, an injury, a robbery, a suspicious vehicle.
- **System-generated exception alerts** — the platform ingests transaction and operational data (POS above all, plus e-commerce, inventory, cash management, video, alarm events) and applies rules or machine-learning models to surface suspicious patterns: unusual refund behavior, excessive voids, discount abuse, no-sales, cash over/short, atypical employee or customer patterns.

### The Case / Investigation

Events that warrant response are organized into **cases** (investigations). A case aggregates related events, evidence, and subjects, and moves through a managed lifecycle:

```text
Open → Triage → Investigate → Disposition (closed)
```

A case carries:

- **Evidence** — video clips, photos, documents, transaction records, gathered and preserved in one place with timestamps
- **Subjects** — the people, vehicles, or organized groups attributed to the loss: employees, shoplifters, repeat offenders, persons of interest, known offender watch lists
- **Tasks and collaboration** — assigned work with due dates, notes, and team coordination
- **Links** — connections to related cases and events across stores, which is how organized retail crime becomes visible (the same subjects, vehicles, or methods recurring across locations)

### Disposition

Every case ends in a **recorded resolution**: closed as unfounded, resolved through coaching or HR action (internal theft), referred to prosecution, resolved through civil recovery or restitution, or closed with a process/policy fix. The disposition — like everything in the case — is recorded with attribution and timestamps.

### The Aggregation Layer

Individual events and cases roll up into the estate-level picture: loss by cause, location, and time; hotspots; repeat subjects; case close rates and time-to-close; recovery totals. This aggregation is what turns record-keeping into prevention — it tells the LP organization where to focus, which controls are failing, and which subjects drive disproportionate harm.

### The Audit Layer

Alongside event response, mature platforms carry **audit management**: configurable audit forms (brand standards, health and safety, operational policy) with scoring, executed in the field on mobile devices, with recurring schedules and automated follow-up actions. Audits are the preventive instrument — they find the process gaps that produce loss before those gaps become cases.

### Concept vs. Implementation

The core model is conceptual. Common implementations realize it in different ways:

```text
Concept:  Loss event
Implementations:  field incident report, exception alert, accident/injury report

Concept:  Detection
Implementations:  rule-based exception reporting, ML/AI anomaly models,
                  video analytics, alarm/EAS events, staff reports

Concept:  Subject
Implementations:  employee record, customer identifier, person of interest,
                  vehicle plate, organized group

Concept:  Disposition
Implementations:  case closure codes, prosecution referral, civil recovery /
                  restitution records, HR/coaching outcomes, policy fixes
```

## How It Works

### The detection-to-disposition loop

The platform's defining workflow is a loop from signal to prevention:

```text
Ingest data (POS, e-commerce, inventory, video, alarms)
→ generate exception alerts (rules / models)
→ review alert queue (genuine signal vs. false positive)
→ open or merge into a case
→ assemble evidence (transaction detail, video, photos, documents)
→ link related events and subjects across stores
→ investigate (tasks, collaboration, law-enforcement package if needed)
→ record disposition (closed / coached / prosecuted / recovered)
→ aggregate: dashboards, hotspots, repeat subjects
→ prevent: audits, coaching, policy and process fixes
→ (feeds back into detection rules and store practice)
```

### Exception-based reporting in practice

Exception-based reporting (EBR) is the dominant detection mechanism. Transaction data flows in from the POS (and increasingly e-commerce and inventory systems); the platform applies configurable rules and, in current products, adaptive models to flag transactions and behavior patterns that deviate from norms — refunds without matching sales, repeated voids, discounts beyond policy, register cash variances. Analysts work through the resulting alert queue in a centralized console, drilling into transaction detail (often alongside linked video) to decide whether an alert is a genuine loss signal or a false alarm, then disposition it accordingly.

### Incident reporting in practice

Store staff report events through short mobile or web forms — what happened, who was involved, what was lost — often with photo or video attachment. Some products accept reports from hotlines, text messages, or automated imports (for example, insurance-carrier incident feeds). Reports land in the same system of record as exception alerts, so field events and data-detected events are investigated in one place.

### Investigation in practice

An investigator opens or expands a case, attaches evidence, and — critically — looks for connections: has this subject appeared at other stores, does this method match other cases, is this an organized group rather than an individual? Linking related cases across the estate is the step that converts isolated incidents into organized-retail-crime investigations. Where prosecution is pursued, the platform assembles the case package for law enforcement.

### Audit in practice

LP or operations staff build audit forms once, schedule them across locations, and field teams execute them on mobile devices. Scores and failed items trigger follow-up actions automatically. Audit results feed the same aggregate picture: a store with recurring audit failures is a store likely to produce loss.

### Capability tiers

**Defining core** — without these, the product is not a loss prevention platform:

- loss event records typed by cause, bound to location and time
- a managed response workflow from review to recorded disposition
- estate-level aggregation across locations and time

**Standard capabilities** — present in essentially all mature products:

- exception-based reporting over POS/transaction data with an alert review queue
- case management with evidence attachment, tasks, linking, and audit trails
- subjects / persons of interest and watch lists
- dashboards, reports, and custom queries (close rate, time-to-close, recovery, loss by cause)
- role-based access and case-history audit trails
- mobile incident entry and mobile audit execution
- POS integration (the data foundation for detection)

**Optional / variant capabilities** — depend on product and customer:

- law-enforcement collaboration surfaces and case packages
- cross-retailer intelligence sharing networks
- recognition technology (facial recognition, license-plate recognition) as privacy-regulated add-ons
- civil recovery / restitution program automation
- returns & claims fraud decisioning (real-time approve/warn/decline at the return boundary)
- safety and HR case extensions (injury reports, regulatory filings, HR cases)
- video-first delivery with POS-video correlation at the center
- vertical tuning for grocery, pharmacy, restaurant, and convenience operations

## Interfaces

### Exception alert queue / review console

The analyst's daily work surface.

- lists generated alerts with risk indicators, filtered by location, type, and employee
- typical information: transaction detail, employee, register, pattern matched, linked video
- primary actions: review detail, mark legitimate / false positive, convert to case, assign

### Case record

The system of record for an investigation.

- typical information: case type, status, location, events included, subjects, evidence files, tasks, full timestamped history
- primary actions: attach evidence, add/link subjects, link related cases, assign tasks, record disposition, generate law-enforcement package

### Incident entry forms

The store-facing capture surface (mobile and web).

- short structured forms for theft, fraud, safety, and accident events
- primary actions: file report, attach photo/video, submit to the central system

### Analytics dashboards and reports

The management surface.

- typical information: loss by cause/location/period, case close rates, time-to-close, recovery totals, top subjects, hotspot maps
- primary actions: build and save custom reports and queries, configure dashboards, export

### Audit builder and mobile audit execution

- builder: create audit forms with question types and scoring, schedule and assign them
- field surface: execute audits on mobile, capture results, trigger follow-up actions

### Collaboration surface

Where case information leaves the retailer: law-enforcement packages, evidence requests, and — in network-style products — controlled sharing with other retailers. Sharing is explicitly governed: the retailer controls what is shared and with whom.

### Administration

Configuration of case forms and workflows, detection rules, audit templates, roles and permissions, and data integrations.

## Important Rules / Behaviors

- **Every event is typed, located, and timed.** The loss-cause taxonomy and the location dimension are structural: without them, nothing aggregates and the platform loses its purpose.
- **The case history is preserved.** Cases carry complete, timestamped histories — who changed what and when. This audit trail is both an investigative tool and a governance requirement, since cases may support prosecution or employment action.
- **Evidence is centralized and preserved.** Video clips, photos, documents, and transaction records attach to the case rather than living in email threads or spreadsheets; preserving the link between transaction data and video is a core behavior of modern products.
- **Alerts must be dispositioned.** The alert queue is a managed workflow: every alert is reviewed and resolved as a genuine signal or a false positive. Letting alerts age out unreviewed defeats the detection layer.
- **Detection depends on integration.** Exception-based reporting requires POS (and optionally e-commerce/inventory/video) data feeds. Without them, the platform degrades to field incident reporting and case management.
- **Internal and external loss follow different paths.** Employee-attributed loss typically resolves through HR/coaching processes with strict confidentiality; external loss resolves through prosecution, recovery, or deterrence. The same case machinery serves both, with different disposition semantics.
- **Investigations are confidential and access-controlled.** Role-based access governs who sees cases and subjects; subject data (especially where recognition technology is involved) is privacy-regulated, and sharing outside the organization is explicitly controlled by the retailer.
- **Linking across stores is the point.** A single store cannot see that a subject or method is recurring across a region; the estate-level record is what makes organized retail crime visible and what makes repeat-offender prevention possible.

## Variants

Common shapes of the Type:

- **Analytics-first suites** — exception reporting at the center, with case management and audits attached; strongest for data-driven LP organizations.
- **Case-management-first platforms** — incident and investigation management at the center, with exception reporting and audits attached; strongest for departments consolidating many processes into one system.
- **Crime-intelligence / network platforms** — incident capture and investigation connected to cross-retailer intelligence sharing and direct law-enforcement collaboration; prevention-oriented rather than documentation-oriented.
- **Total-loss suites** — combine shrink/exception analytics, returns & claims fraud decisioning, and case/audit management to span in-store and online loss.
- **Video-first delivery** — video management with POS-data correlation at the center, delivering loss prevention through camera intelligence (this shape straddles the boundary with video management systems).
- **Vertical tunings** — grocery (perishable and expiring-inventory shrink), pharmacy (controlled-substance diversion), restaurants (waste, cash handling), convenience (fuel and after-hours risk).
- **Extension modules** — safety/incident management (injuries, regulatory filings, disaster alerts), HR case management, inventory-loss analytics (RFID, physical inventory, direct-store-delivery).

A variant remains a variant while the loss-event core applies. When the center of gravity moves fully away from loss events — to cameras (video management), to payment fraud (fraud detection), or to legal matters (corporate investigation) — it has become a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Retail Shrink Management | sibling (same directory group) | measurement/program layer: quantifying shrink by cause and location, inventory accuracy, reduction targets; the LP platform is the event/response layer that acts on those signals. The seam needs joint review — LP platforms include shrink analytics as a capability |
| Fraud Detection Platform | adjacent | payment/card/transaction fraud with real-time decisioning and financial-crime typologies; the LP platform is investigation-centric with retail-loss typologies. Returns/claims decisioning sits exactly on the seam |
| Corporate Investigation Management | adjacent | legal/corporate investigations (matters, legal holds, compliance); LP case management is retail-loss-specific (ORC linking, recovery, prosecution, law-enforcement collaboration) |
| Retail POS | upstream | POS creates transactions; the LP platform consumes POS data as its primary detection input. POS built-in exception reports are a lightweight, store-level precursor |
| Retail Inventory Management | adjacent | owns stock records; shrink surfaces there as count variance. The LP platform investigates causes of the variance; it does not own the stock record |
| Video Management System (physical security) | adjacent | VMS manages cameras and footage; the LP platform uses video as evidence and context. Video-first LP products straddle this boundary |
| Insider Risk Management | adjacent | employee digital-data risk; the LP platform covers physical and transactional loss including employee theft via POS exceptions |
| Transaction Monitoring / AML Platform | adjacent | financial-crime monitoring on banking rails; different domain, different data, different regulators |

The most important internal boundary is with **Retail Shrink Management**: the two share vocabulary (shrink, loss causes) and overlap in shrink analytics. The working distinction — measurement and program governance versus loss-event detection and response — should be validated when the sibling leaf is processed.

## Representative Products

- **Agilence** — analytics-first: exception-based reporting with case management and audit management
- **ThinkLP** — case-management-first "loss and safety" platform: cases, audits, exception reporting, ORC, HR and safety extensions
- **Auror** — crime-intelligence platform: incident capture, case connection, and retailer–law-enforcement collaboration network
- **Appriss Retail** — total-loss suite: returns/claims decisioning, shrink & exception analytics, case & audit management

Solink (video-first vision-intelligence platform with loss prevention use cases) was additionally reviewed as a boundary marker toward video management systems.

## Sources

Research date: **2026-09-07**

- Agilence — Loss Prevention Analytics & Reporting (root): https://www.agilenceinc.com/
- Agilence — Analytics Platform: https://www.agilenceinc.com/platform
- Agilence — Case Management: https://www.agilenceinc.com/platform/case-management
- Agilence — Audit Management: https://www.agilenceinc.com/audit-management
- ThinkLP — root: https://www.thinklp.com/
- ThinkLP — Case Management: https://www.thinklp.com/lp-case-management/
- Auror — root: https://www.auror.co/
- Auror — Product Overview: https://www.auror.co/product/overview
- Appriss Retail — root: https://apprissretail.com/
- Solink — root: https://www.solinkcorp.com/

> Sourcing limitation: no public help-center or user-guide documentation was reachable for the sampled products on 2026-09-07; all evidence comes from official product pages (marketing/product-documentation tier). Appriss Retail subpages were unreachable (server errors), so its observations rest on the root product page only. Accordingly, this document intentionally avoids precise operational parameters (numeric thresholds, exact state names, plan restrictions); such details were not verifiable and are not asserted. Vendor-published scale statistics were treated as marketing claims and excluded from the description of how the Type works.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
