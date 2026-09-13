# Restoration Contractor Management

## Overview

A **Restoration Contractor Management** application is the business-management system of a property-restoration company: a firm that responds to damage events — water intrusion, fire and smoke, mold, storm — at buildings and restores them. The system anchors each job to a loss event at a property, builds a documented, evidence-grade record of the loss and the work performed, coordinates the crews who mitigate, dry, clean, pack out, and rebuild, and carries the job through review by the party that pays for it — most commonly an insurance claim handled by an adjuster or a carrier's contractor program.

The defining core is small:

```text
Loss-driven restoration job (the unit of record)
│   a damage event at a property: water, fire/smoke, mold, storm
│   carried from loss response through mitigation and
│   (commonly) reconstruction to completion
├── Evidentiary job file
│   photos, notes, readings, floor plans, scope, contents —
│   captured in the field as the defensible record that
│   justifies the scope and the cost
└── Payer-review payment path
    the job carries its payer context — commonly an insurance
    claim (carrier, adjuster, loss details), in program work a
    program assignment with response-time and documentation
    obligations — and payment follows review of the file
```

Everything else commonly associated with these products — moisture maps, drying logs, contents inventories, Xactimate hand-offs, dispatch boards, dashboards, CRM — is standard capability that mature products add around this spine. The spine itself is what separates restoration from every other trade: in plumbing or HVAC the job file answers to the customer and the office; in restoration it must also survive scrutiny by a reviewing payer, and the products are built around that fact. Vendors in this market state it plainly: you can't bill for what you can't prove.

## Users & Context

Primary users:

- **Owner / executive** — monitors the job board, revenue, profitability, and referral sources; decides which carrier programs and referral relationships to pursue; handles escalations.
- **Project manager / production manager** — runs active jobs: assigns crews, monitors drying progress across many water jobs from the office, keeps documentation complete, manages estimate revisions and deadlines, runs production meetings around jobs that are behind schedule.
- **Field technician / restoration tech** — works the loss: responds to the emergency, captures photos, video, notes, and moisture readings on site, places drying equipment, performs mitigation and cleaning, tags and packs out contents, collects signatures.
- **Estimator / office staff** — builds scopes and estimates (commonly in the industry-standard estimating platform, fed by the field documentation), prepares the job file for submission, generates the reports the adjuster reviews, invoices and tracks payment.

Secondary participants:

- **Adjuster / carrier / program administrator** — not an operator of the contractor's business, but a first-class *consumer* of the system's output: reports, photos, drying documentation, contents inventories, and estimates flow to them, and their approval gates payment. Some products serve adjusters directly as users (letting them open claims, request photos from policyholders, and price contents).
- **Customer (policyholder / property owner)** — the recipient of emergency response and restoration work; signs work authorizations, receives updates, and is often the source of on-site access and decisions.
- **Subcontractors** — often used for reconstruction-phase trades and large losses; some products support collaboration with them in the system.

Typical context: restoration companies ranging from small local firms to national franchise systems, with work mix spanning emergency water mitigation, fire and smoke cleanup, mold remediation, contents restoration, and rebuild work. Demand is loss-driven and urgent — water does not wait — and much of the revenue is insurance-funded, which makes documentation quality, response time, and file completeness business-critical rather than administrative. The office works in a web dashboard; technicians work in a mobile app that must function in wet, dark, connectivity-poor buildings; adjusters consume generated reports.

## Core Model

### The Defining Core

**Restoration job (loss job).** The unit of record and the center of the whole system. One job represents one engagement with one loss: what happened (the cause — a burst pipe, a fire, a storm), where (the affected property), who is involved (the customer, and commonly the payer's claim), and how the work progresses. A job carries:

- the customer and the loss property
- the loss context — cause, date of loss, and commonly the insurance claim: carrier, adjuster, claim and policy details; in program work, the program assignment and its obligations
- the documentation: photos and video organized by room, notes, moisture readings, floor plans or sketches, forms and signatures
- the scope of work and its estimate
- contents inventory where personal property is affected
- schedule, assigned crews, and status through the job's phases
- the invoices and payments attached to it

Jobs follow a recognizable trade arc: **loss response** (emergency call, rapid contact, site inspection) → **mitigation** (extraction, demolition of unsalvageable material, drying, cleaning, deodorization; mold remediation; smoke removal) → **contents** (pack-out, cleaning, storage, return — where personal property is involved) → **reconstruction** (rebuilding what was removed) → **completion and payment**. A water job may be days; a fire rebuild may be months. The phases can carry different crews and different kinds of billing, but they stay on one job.

**Evidentiary job file.** The documentation layer is not an accessory to the job — it is a load-bearing structure. Photos, notes, readings, sketches, scope, and contents are captured in the field, organized per job, and assembled into reports whose explicit purpose is to justify the work and its cost to a reviewing party. The file is the difference between a paid invoice and a scrubbed one: incomplete drying data means equipment charges get questioned; missing photos mean line items get removed. Mature products treat the file as the job's product as much as the work itself.

**Payer-review payment path.** The job carries its payer context, and payment follows review. In the dominant pattern the payer is an insurance carrier: the job binds to a claim, the documented file and estimate go to the adjuster (or to a third-party administrator running the carrier's contractor program), the reviewer checks scope, pricing, and documentation against program guidelines, and payment is released on approval — with revisions and reinspections when the file falls short. Direct-pay work (the customer pays out of pocket) exists and uses the same job structure minus the claim; the system is built for the claim case because that is where the money and the risk live.

### Standard Capabilities of Mature Products

These are near-universal in current products and make the core practical, but a product lacking some of them can still be recognized as this Type:

- **Field documentation app** — a mobile app that captures photos, video, 360° imagery, notes, e-signatures, and custom forms, organized by room, working offline (restoration happens in basements and buildings without signal) and syncing when connectivity returns.
- **Water-loss machinery** — moisture-content and psychrometric readings (temperature, relative humidity, dew point, vapor pressure) logged across repeated monitoring visits; drying logs; moisture maps with drying equipment placed on them; equipment calculation for drying chambers aligned to the industry drying standard (IICRC S500); alerts when a chamber stalls or conditions drift. This is the trade's signature machinery and the most trade-specific structure in the product class.
- **Floor plans and sketches** — 2D floor plans captured by walking the property with a phone; room dimensions feed both documentation and estimating.
- **Scope → estimate flow into the estimating standard** — the field documentation generates a scope of work (increasingly with AI assistance), which is sent into the industry-standard estimating platform (Xactimate in the North American market) with quantities and room data, where the estimator finalizes the estimate. Some products also produce rough-order-of-magnitude estimates internally.
- **Contents / pack-out** — itemized inventory of affected personal property, organized by room, commonly tagged with barcodes or QR codes on items and boxes; pack-out and pack-back tracking; cleaning and storage status; pricing; total-loss versus salvage determination; replacement pricing for non-salvageable items; schedule-of-loss and contents reports for the adjuster.
- **Job milestones and stage workflows** — configurable job stages with automated task assignment (when one stage completes, the responsible person for the next step is tasked), milestone tracking, and alerts on jobs falling behind.
- **Crew scheduling and dispatch** — a calendar and often a map view of active jobs; crew assignment that lands on both the schedule and the job; time tracking.
- **In-file communication** — messages, photos, and updates posted inside the job file with time stamps, so the job's story accumulates in one place.
- **Carrier/adjuster-facing reports** — generated, professional report packages: documentation reports, drying reports with moisture maps and readings, contents and total-loss reports, ready to send to the reviewing party.
- **CRM with referral sources and programs** — the demand side is institutional: carriers, third-party administrator programs, insurance agents, property managers, and franchise programs appear as tracked referral sources whose performance is reported.
- **Payments, forms, and accounting sync** — e-signatures and work authorizations, payment collection, and synchronization with accounting software.
- **Dashboards and reporting** — job progress, milestone performance, profitability by job or by referral source, documentation-quality indicators.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  The job's frame
Implementations:  job created as a claim (claim number, carrier,
                  adjuster on the job record); job with claim
                  fields attached; job with program assignment
                  and service-level obligations

Concept:  The evidentiary file
Implementations:  documentation-first product where the file IS
                  the product; operations-first product where the
                  file is one tab of the job; dedicated contents
                  product feeding the job file

Concept:  Drying machinery
Implementations:  guided S500 workflows with equipment calculators
                  and alerts; moisture mapping and equipment
                  scanning as base features; manual reading logs

Concept:  The estimate
Implementations:  scope generated from field data and sent to the
                  external estimating standard; internal estimating
                  with line items; rough-order-of-magnitude tools
                  for early triage

Concept:  The payer
Implementations:  carrier claim via adjuster; third-party
                  administrator program with scorecards and
                  required technology; property manager or
                  direct-pay customer
```

The market also realizes the Type in two recognizable product shapes: **documentation-first** platforms whose center of gravity is the field record and the reports built from it, and **operations-first** platforms that run the whole business — CRM, scheduling, financials, assets — with the trade machinery included. The two shapes coexist and are even integrated with each other in real customer stacks: an operations platform may use a documentation platform as its field layer.

## How It Works

The canonical flow of a restoration engagement:

```text
Loss occurs; emergency call arrives (or program assignment lands)
→ create the job: customer, property, cause of loss,
  claim details if insured
→ [program work] accept the assignment within the response window;
  contact the customer and inspect within the program's clocks
→ document the loss on site: photos, video, notes, moisture
  readings, sketch/floor plan — offline-capable
→ [water work] place drying equipment; log readings on monitoring
  visits until the structure is dry; remove equipment
→ [contents] inventory, tag, pack out affected personal property;
  clean, store, and return it — or document total loss
→ build the scope from the field documentation
→ send scope and quantities to the estimating platform;
  estimator finalizes the estimate
→ submit the file (documentation + estimate) for review
→ [program work] reviewer checks guidelines, pricing, documentation;
  revisions and reinspections as needed
→ approval → work proceeds / completes → invoice → payment
→ reconstruction phase runs as its own arc of the same job
  where rebuild is required
→ close-out: signatures, final documentation, payment reconciled
```

Four loops are worth distinguishing:

**The response loop (per loss).** Restoration starts with urgency. The job is created fast — often from an emergency call or an electronically delivered program assignment — and the early clocks (first contact, on-site inspection, initial documentation) are measured in hours for program work. The system's job is to make the first hours produce a complete record, because everything billed later depends on what was captured before the scene changed.

**The drying loop (per water job).** Equipment goes in; readings come out. Technicians visit on a cadence, log moisture and humidity readings, and the system tracks drying progress against targets — alerting when a drying chamber stalls so the office can intervene without driving to the site. When the structure is dry, equipment comes off. Every reading and every equipment-day is billable, and every one of them must be provable.

**The contents loop (per pack-out).** Affected personal property is inventoried item by item (commonly with scanned tags), packed out to a facility, cleaned or declared a total loss, stored, and returned. The inventory list doubles as the adjuster-facing contents report, with replacement pricing for non-salvageable items.

**The money loop (per job).** The documented file becomes a scope, the scope becomes an estimate in the estimating standard, the estimate goes for review, and approval releases the work and the payment. Estimate revisions, supplements (additional work discovered mid-job), and reinspections are normal events, not exceptions — and each one is another round of documentation. Payment may come from the carrier, through the program, or from the customer, and deposits or progress billing appear on longer rebuilds.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Job board / dashboard

The office's primary surface.

- active jobs by stage or status, with indicators for jobs missing documentation, behind on milestones, or awaiting review
- primary actions: create job, open a job, assign crews, check drying status across jobs, review deadlines

### Job detail / job file

The record of one engagement; the most information-dense surface.

- loss and claim context, customer and property, documentation (photos by room, notes, readings, floor plan), scope and estimate, contents list, schedule and crews, status and milestones, invoices and payments, in-file communication feed
- primary actions: capture or upload documentation, build scope, generate reports, schedule crews, record readings, invoice, message participants

### Field mobile app

The technician's working surface, built for wet, dark, signal-poor environments.

- assigned jobs with loss details and customer information
- primary actions: capture photos/video/notes (offline), log moisture readings, place and scan equipment, tag and list contents, collect signatures, complete stage tasks

### Drying / moisture workspace

Where water jobs are managed over their monitoring life.

- moisture maps by floor plan, reading history per point, equipment placed per chamber, drying targets and alerts
- primary actions: add readings, add or remove equipment, check drying status, generate the drying report

### Contents workspace

- itemized inventory by room, item photos and descriptions, tags, pack-out and storage status, pricing, total-loss determinations
- primary actions: list items, scan tags, update status, price, generate contents or total-loss reports

### Estimate / scope surface

- scope of work by room and line item, quantities from field data, connection to the external estimating platform
- primary actions: generate scope, review and edit, send to the estimating platform, track revisions and approvals

### Reporting surface

- generated report packages for external review: documentation report, drying report, contents report, schedule of loss
- primary actions: assemble, review, share with the adjuster or program

### CRM / referral surface

- customers, referral sources (carriers, programs, agents, property managers), and their performance
- primary actions: record a referral source, track program performance, follow up on leads

## Important Rules / Behaviors

### The file must justify the invoice

The governing rule of the Type. Work that is not documented is work that may not be paid: equipment left off the invoice because no readings support it, line items scrubbed for lack of justification, estimates revised when the file is thin. Mature products therefore make documentation continuous (captured in the field, time-stamped, offline-safe) rather than reconstructed at the office, and treat report quality as a revenue issue.

### Payment follows review, not completion

Unlike a retail transaction, the completed work does not automatically produce money. The documented file and estimate go to a reviewer — adjuster or program — whose approval gates payment; revisions, supplements, and reinspections are normal. The job's financial state is therefore entangled with its documentation state.

### Response clocks are contractual in program work

Carrier programs assign work with service-level expectations — rapid first contact, timely inspection, documentation and estimate submission deadlines, daily status updates — and score contractors on them. Performance feeds future assignment volume, so the system tracks the clocks, not just the work.

### Drying is a standard of care, not a guess

Water work follows an industry drying standard (IICRC S500): equipment quantities are calculated from chamber conditions, readings are logged on a cadence, and drying targets gate equipment removal. The machinery exists both to dry the building correctly and to prove the drying was professional — the same reading serves science and invoice.

### Contents are someone's property, item by item

A pack-out creates custody: each item is identified, photographed, tagged, tracked through cleaning and storage, and returned or declared a total loss with the owner's and adjuster's visibility. The inventory is simultaneously an operational tool and a claim document.

### The job outlives its phases

Mitigation and reconstruction can be weeks apart with different crews, but they stay on one job: the loss's documentation feeds the rebuild's scope, and the payer sees one claim, not many. Products that split phases into separate jobs lose the thread the adjuster is following.

### The field is offline-first

Losses happen in flooded basements and burned buildings. Field capture is expected to work without connectivity and sync safely later; data loss in the field is treated as an existential product failure, because the scene cannot be re-photographed.

### Roles gate configuration

Day-to-day job work is open to office staff and field technicians; business-wide configuration — stage workflows, forms, price lists, user roles, program settings — is restricted to admin-level roles. Field technicians see and change their assigned jobs, not the business's settings.

## Variants

- **Water mitigation-focused companies** — the emergency-drying core; the drying loop is the daily work; high job velocity, shorter jobs.
- **Full-service restorers (mitigation + rebuild)** — one job from emergency through reconstruction; rebuild adds project-like machinery (budgets, phases, subcontractors).
- **Contents-focused operations** — pack-out, cleaning, and storage as the specialty; dedicated contents tooling and facilities.
- **Program contractors** — most work arrives through carrier programs and third-party administrators; SLA compliance, scorecards, and required technology shape daily operations.
- **Independent contractors (non-program)** — direct relationships with adjusters, agents, and property managers; the same job structure without program overhead.
- **CAT (catastrophe) responders** — storm and hurricane surge work; volume spikes, traveling crews, and mass-scale documentation.
- **Franchise systems** — national brands with standardized workflows and reporting across many locations.
- **Mold remediation and specialty cleanup** — biohazard, trauma, and specialty cleaning as job content within the same structure.

A variant should remain a **Variant**, not become a separate Type, unless it changes the core objects, workflow, or rules so much that the defining core no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Small Business Field Service Management | family sibling; shares the service spine | generic service jobs answer to the customer and the office; restoration jobs also answer to a reviewing payer, and carry the evidentiary file, drying loop, and contents stream as structural objects |
| Construction Project Management | adjacent at the reconstruction pole | construction runs on project containers with schedules, contracts, and cost control; restoration centers on the loss job and its file; rebuild work drifts toward project machinery but the loss spine remains |
| Insurance Claims Management | seam across the payer side | carrier-side claim administration owns the policy and the payment decision; this Type is the contractor-side execution system; the claim object appears on both sides with different ownership |
| Claims Adjuster Platform | adjacent, different seat | the adjuster's workbench reviews and prices claims; some restoration products serve adjusters directly, but this Type's seat is the contractor performing the work |
| Carrier compliance apps (field-audit tools) | different product class entirely | built for carriers to audit contractor files with rigid linear workflows; restoration management products are the contractor's primary field system and position themselves against the audit-first tools |
| Estimating platforms (e.g. Xactimate) | capability boundary | the industry-standard estimating tool is external; this Type feeds it scope, quantities, and floor plans and receives approved amounts back — estimating is a capability here, not the Type |
| Cleaning Business Management | trade sibling with a structural difference | routine cleaning is recurring, direct-pay, and file-light; restoration cleaning is loss-driven, documented to claim standard, and payer-reviewed |
| Environmental Remediation Management | adjacent at the contamination boundary | environmental-sector remediation is site-scale and regulator-facing; restoration is building-scale and payer-facing; mold remediation sits near the seam but appears here as job content |
| Home Improvement Contractor Management | trade sibling, different trigger | improvement work is voluntary and customer-funded; restoration work is loss-driven and commonly claim-funded with third-party review |
| CMMS / Enterprise Asset Management | different ownership side | equipment tracking here manages the contractor's own drying equipment and vehicles in deployment, not maintained plant or customer assets |
| Property Maintenance Management | different seat | property managers coordinate maintenance across portfolios; here the property manager is a counterpart or customer, not the operator |
| Local Service Marketplace | demand-side adjacent | marketplaces are consumer discovery; restoration demand often arrives from carriers and programs instead — which is why referral sources, not listings, are the CRM objects |

The most important boundary is with generic field service management: the structural spine is shared, but restoration's payer-review economy gives the job file a second audience and the trade its own machinery. The second most important is with the carrier side (claims management and compliance apps): the claim is shared, but the seats, the workflows, and the definition of "done" are different.

## Representative Products

- **Encircle** — documentation-first restoration platform (field documentation → scope → estimate); ships the deepest trade machinery documentation (drying workflows, contents, adjuster-facing surface) and documents the carrier-program layer in depth
- **Albi (Albiware)** — operations-first all-in-one restoration management built by restorers; trade machinery (moisture mapping, equipment scanning) in its base tier
- **Assured Software (JobCheck / PackOut / TrackIt)** — job management plus a dedicated contents/pack-out product, on a franchise-scale platform; also serves independent adjusters

The Core Model was checked against the market's product-shape spread (documentation-first vs operations-first vs job-management-plus-contents) rather than a single vendor's packaging.

## Sources

Research date: **2026-09-09**

- Encircle (Tier 2, official site): https://www.getencircle.com/ — platform overview and solutions; https://www.getencircle.com/solutions/water-mitigation/ — drying workflows, equipment calculation, defensible-documentation framing
- Encircle Help Center (Tier 1): https://help.encircleapp.com/hc/en-us — Restorers and Adjusters audiences; claim setup, documentation, scoping/estimating, hydro, contents, payments sections
- Encircle TPA program page (Tier 2): https://discover.getencircle.com/tpa-program/ — third-party administrator programs, scorecards, service-level expectations, program workflow
- Albiware (Tier 2, official site): https://albiware.com/ — positioning and plan tiers; https://albiware.com/features/job-management/ — job management, dry plans, equipment; https://albiware.com/features/business-operations/ — financials, referrals, assets
- Albi Help Center (Tier 1): https://help.albiware.com/ — projects, scheduler, assets, CRM, payments, communications sections
- Assured Software (Tier 2, official site): https://www.assuredsoftware.com/ — JobCheck/PackOut/TrackIt overview; https://www.assuredsoftware.com/job-check/ — claim context in job files, workflow engine, milestone tracking, budgeting

> Sourcing limitation: DASH by Next Gear Solutions and iRestore — major restoration-management products — could not be accessed (empty responses / HTTP 403), so the enterprise, claims-program-centric pole is under-sampled and market coverage is calibrated to the three researched products. Xactimate/Verisk official pages were also unreachable (404/403); the estimating platform's role is documented only through integration partners' pages. Service-level figures published on one vendor's program page carry that vendor's own "programs vary" annotation and are deliberately not stated as precise numbers in this document. Regional markets outside North America could not be verified, and no region-specific claims are made.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
