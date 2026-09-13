# Museum Condition Reporting

## Overview

A **Museum Condition Reporting** application documents the physical condition of collection objects as dated, attributed records bound to each object's identity, and retains those records as a comparable history per object. Its purpose is evidentiary and preventive: to know what state an object was in at a given moment, who assessed it and why, so that change can be detected, responsibility can be assigned at handovers, and care decisions can be based on recorded observation rather than memory.

The defining core is small:

```text
Identified object (the collection register's record)
└── Condition record
    ├── dated, attributed, reason-coded (when, who, why checked)
    ├── structured condition content
    │   ├── overall state (rating / condition terms)
    │   ├── damage and deterioration descriptions
    │   └── damage location on the object
    ├── photographic / sketch documentation
    └── retained history (prior records stay referable)
        └── comparison → change detection → recommendations and escalation
```

Everything else commonly associated with the practice — material-specific templates, annotated photography, controlled damage vocabularies, permission-scoped sharing with lenders and couriers, next-check scheduling — is standard capability of mature products, not what makes the workflow condition reporting. A paper condition card filed by object number, with a date, a checker's name, a description of damage, and a sketch, satisfies the same structure; the domain standard for this practice is explicitly medium-agnostic.

The workflow documents **state**; it does not perform or record **treatment**. Treating objects — examination proposals, treatment records, treatment programs — is the neighboring discipline of conservation management. The two interlock (a condition record is made before treatment begins, and a worrying condition finding escalates to a conservator), but they are distinct workflows held apart by standards, by product field structures, and by product packaging alike.

## Users & Context

Primary users are the collection-care staff of museums, galleries, and conservation practices:

- **Conservators** — write full condition reports and technical assessments, especially as baselines before treatment and for complex objects; receive escalations when other staff find something concerning.
- **Registrars** — commission and verify condition documentation at the moments custody changes: loan release and return, transit departure and arrival, exhibition install and deinstall; condition documentation accompanies the loan workflow, and lenders, insurers, and indemnity providers may require photographic records of condition.
- **Collections managers** — conduct routine and scheduled checks across storage and display, record condition in the course of inventory and housekeeping, and act on care recommendations.
- **Couriers, art handlers, and installers** — capture condition at the handling moments they witness: unpacking, vehicle loading and unloading, placement, repacking.
- **Conservators in private practice and consultants** — document condition for client institutions and collectors, delivering condition reports and summaries as work products.

In small museums and historic houses the same duties are carried by one or two staff members plus volunteers, using the lighter end of the practice: a quick check with a rating and a note. The work environment is physical and point-of-work — storerooms, galleries, loading docks, conservation studios, transit crates — with mobile capture (photographing and annotating in situ) the current norm. The governing context is the institution's documentation policy: who is authorized to check what, at what depth, how often, and what must trigger a check.

## Core Model

### The condition record

The unit of the workflow is the **condition record** — one persistent record of one assessment of one object at one moment. Every condition record is bound to the object's identity (its object or accession number, or the equivalent record in a standalone product), so that all condition information for an object is findable through that number. Each record carries:

- **When** — the date of the check, in a standard format.
- **Who** — the condition checker or assessor, attributed by name.
- **Why** — the reason for the check (for example: loan release, arrival, exhibition, pre-treatment, periodic survey), which makes the record auditable against the procedure that prompted it.
- **What was found** — the condition content itself (below).

The record may be a dedicated record object, a repeating group of fields on the object record, or a generated report document filed against the object — realizations differ; the anchoring does not.

### Structured condition content

The substance of the record is a structured description of the object's physical state:

- **Overall state** — a rating or summary term. Products commonly capture this as a short rating scale or a controlled keyword; the exact scales and vocabularies vary by institution and product.
- **Damage and deterioration** — descriptions of what is observed: losses, cracks, flakes, stains, corrosion, pest activity, previous repairs — commonly drawn from a standard vocabulary so that records are consistent and searchable.
- **Location on the object** — which part is affected, recorded as a part reference, a note of position, or an annotation placed on a photograph.
- **Completeness and hazards** — whether anything is missing, and any hazard the object presents (for example pest infestation or hazardous materials).
- **Images** — photographs are the expected norm and may be required by lenders, insurers, and indemnity providers; sketches and diagrams mark areas of loss or damage; current-era products add video and annotated detail images.

### The retained comparable history

Condition records accumulate. Earlier records are not overwritten when a new check is made; they remain attached to the object and are consulted when the next check is performed. This is what turns isolated reports into an **audit trail of changes to the object**: a new finding is read against the prior record, and a difference between them is itself a signal — the standard's own escalation rule treats "condition differs from that recorded in previous condition checks" as a trigger to consult a conservator. The history is also the evidence base when damage is alleged: the records establish what state the object was in before and after a given custody moment.

### What the assessment feeds

A condition record is not only a description; it feeds action:

- **Recommendations** for handling, packing, display, storage, and environmental conditions.
- **Treatment priority** — whether and how urgently the object needs conservation attention.
- **The next check date** — scheduled re-examination, so surveillance is planned rather than accidental.
- **Hazard and handling notes** made available to everyone who will move or use the object.

### One structure, many implementations

The core is conceptual; realizations differ. Condition content ranges from a free-text note with a rating to material-specific templates with dozens of structured fields. Images range from attached photographs to annotations drawn directly on images. History ranges from a list of dated entries to side-by-side comparison views. The defining structure — object-bound, dated, attributed, structured, retained — does not vary.

## How It Works

The workflow is a recurring loop, usually prompted by another procedure rather than run for its own sake:

```text
Trigger (movement / loan / exhibition / intake / treatment / schedule)
→ consult prior condition records for the object
→ examine (good light; photographs; sketches for damage areas)
→ record the check (date, checker, reason)
→ record the result (state, damage, locations, completeness, hazards)
→ record the outputs (recommendations, treatment priority, next check date)
→ update the object's record so others can act
→ escalate concerns to conservation, or return to the prompting procedure
```

**A check is requested.** Most checks are prompted by another procedure: an object is about to move, be lent, be exhibited, or be treated; an object has arrived; a scheduled survey falls due. When many objects are involved, a sample may be checked rather than every object. The institution's policy defines who may check at which depth — a practice the domain standard describes as three levels: a basic check any trained staff member or volunteer can perform (arrivals, simple loans); a condition report by staff with conservation skills or a conservator (objects going on loan, pre-treatment); and a full technical assessment by a professional conservator before major treatment.

**Prior records are consulted.** The checker reads the object's previous condition records, hazard notes, and handling recommendations before examining. This is the comparable-history structure in use: the new assessment is made against the documented past.

**The object is examined.** In good light, with camera and (for the deeper tiers) technical equipment. Photographs are taken; areas of loss or damage are marked with sketches or annotations. If objects must be moved to be checked, that movement is recorded through the institution's location-and-movement procedure — condition checking does not track location itself.

**The check and its result are recorded.** The event (date, checker, reason) and the finding (overall state, damage descriptions, damage locations, completeness, hazards) are recorded against the object. Depth follows the moment: a brief comment suffices when an object enters the building; a full structured report is expected before treatment or an outward loan.

**The outputs are produced and acted on.** Recommendations and hazard notes are written back so that anyone handling the object benefits. A report document may be generated for the file or for an external party — a lender, a courier, a client. A next check date may be set. If the object's condition gives cause for concern, or differs from the previous record, the case goes to a conservator; otherwise the workflow returns to the procedure that prompted it.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Object condition view

The hub surface — the condition picture of one object.

- Typical information: the object's identity and images, its current recorded condition, and the list of past condition records with dates and checkers
- Primary actions: open or create a condition record, compare records, jump to the object's full record

### Condition record editor

The capture surface — where an assessment is written.

- Typical information: template-driven form organized by material or object type — overall rating, structured damage descriptions, part references, hazards, completeness
- Primary actions: rate or classify overall state, describe damage from controlled terms, annotate images (placing damage markers and notes on photographs), attach detail images or video, save against the object with date, checker, and reason

### Report output and sharing

The deliverable surface — the record as a document that can leave the institution.

- Typical information: the formatted condition report with images and annotations, institutional branding, report date and author
- Primary actions: generate/print/export the report, share it with a named external party under permissions (view-only or editing), revoke access

### Review and comparison

The history surface — reading the record over time.

- Typical information: prior reports in sequence or side by side, changes between checks, treatment and handling notes accumulated from past assessments
- Primary actions: compare records, flag changes, escalate a finding

### Scheduling and triggers

The planning surface — making sure checks happen when they should.

- Typical information: objects due for scheduled checks, checks outstanding as part of a loan or exhibition workflow, next-check dates recorded from past assessments
- Primary actions: schedule a check, record that a prompted check has been completed

### Mobile capture

The point-of-work surface.

- Typical information: the object's identity (via search or barcode/label), its prior condition summary
- Primary actions: photograph, annotate, complete a check in situ

## Important Rules / Behaviors

**The object number is the anchor.** Condition information is accessible through the object's identity; a check that cannot be tied to an identified object does not serve the discipline. Condition-reporting products that operate outside a collection system carry their own object records for exactly this reason.

**Attribution and dating are mandatory.** Every record names its checker and its date, together with the reason for the check. This is what makes the record auditable and what gives it evidentiary weight when damage is alleged.

**History is retained, not overwritten.** New checks add records; prior records stay referable. Difference from a prior record is itself a finding that warrants attention. Institutions depend on this across staff turnover and decades.

**Assessment is not treatment.** Condition records document state and recommend; they do not record treatment work. Treatment belongs to the conservation workflow, with one standing interlock: the object's condition is recorded before any treatment takes place, so the treatment has a documented baseline.

**Depth follows the moment.** A brief comment at intake, a structured report for a loan, a full technical assessment before major treatment — the same record structure serves all three, but institutional policy specifies who may check at which depth and when a conservator is required.

**Condition data is sensitive and shared deliberately.** Records are internal by default; external parties (lenders, couriers, partner institutions, clients) see reports only when they are purposefully shared, under permissions the owner controls. Damage and valuation-adjacent detail is the kind of information institutions restrict by role.

**Photography is expected, sometimes required.** Visual documentation is the norm for anything beyond the lightest check, and may be a formal requirement from lenders, insurers, or indemnity providers.

## Variants

- **Module of a collection management system** — the dominant packaging: condition records as a module, tab, or field group on the object record, alongside location, loan, and exhibition machinery. This is the small-museum norm; the lightest realizations are little more than dated, attributed condition fields.
- **Dedicated standalone product** — purpose-built condition-reporting platforms serving museums, galleries, conservators, and art shippers together, with their own object/artwork records, template libraries, annotation tools, and cross-party sharing. Different packaging, same structure.
- **Conservation-suite component** — condition and damage reporting inside conservation documentation software, where condition reports sit beside treatment records; typically synced with the institution's collection system.
- **Conservator-in-practice posture** — the same workflow run as client work: condition documentation, reports, and summaries delivered to client institutions and collectors, with objects moving between clients and the conservator's lab.
- **Transit and shipping posture** — condition documentation bound to shipment legs: departure checks, unloading checks, unpacking reports; the evidence layer for the transport of art.
- **Paper-based realization** — condition cards and forms filed by object number, with photographs and sketches; the historical and still-valid form, and the direct ancestor of the digital templates and vocabularies in current products.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Conservation Management | closest sibling — assessment vs intervention | conservation documents and governs treatment of objects (examinations, treatment proposals, treatment records); condition reporting documents state and escalates to it; they interlock at the pre-treatment baseline report |
| Museum Collections Management | container | the collection system of record owns the object records condition documentation attaches to, plus location, loans, and the other custody events; condition reporting is one care-event family given its own workflow here |
| Museum Loan Management | trigger and consumer | the loan agreement requires condition documentation at release and return; the loan owns the transaction and its terms, condition owns the assessment |
| Exhibition Installation Management | consumer | installation tracks what is in the show and its install state; it consumes condition documentation at arrival/install/deinstall handovers, but condition reporting exists at any moment without a display occasion |
| Artwork Exhibition Logistics | consumer | logistics owns the movement chain and its handover paperwork; condition reporting owns the assessment discipline that the handover documents cite |
| Museum Object Movement Management | trigger sibling | movement control owns the location picture and move transactions; it prompts before/after condition checks but does not record condition |
| Provenance Research Platform | content sibling | provenance documents the history of ownership and origin; condition documents physical state — both attach to object records, different content classes |
| Building Condition Assessment | name neighbor | the same assessment-documentation shape applied to buildings and facilities; different object world — no collection-object identity, custody moments, or conservation vocabularies |

The load-bearing boundary is with **Museum Conservation Management**: the two share authors (conservators), media (photographs, annotations), and even specific moments (the pre-treatment report), but the record classes differ — state assessment versus treatment intervention — and the domain standard, product field structures, and product packaging all keep them separate.

## Representative Products

- **Articheck** — dedicated standalone condition-reporting platform for museums, galleries, conservators, and shippers; template-driven multimedia reports, image annotation, condition history, and permission-scoped sharing
- **TMS Collections** (Gallery Systems) — enterprise museum incumbent; condition checking supported as a documented procedure family within the collections system, alongside its conservation-documentation companion **TMS Conservation Studio**
- **CatalogIt** (It Unlimited) — cloud system for small institutions and collectors; condition tracked on entries, with a conservator-focused posture built on the same core (condition history as repeating entries, client-facing condition reports)
- **eHive** (Vernon Systems) — mid-market cloud collection system; condition recorded on a dedicated conservation section of the object record with separate treatment fields

The definition was checked against the domain standard (Spectrum, the UK museum collections-management standard used internationally, whose condition-checking procedure and minimum requirements are publicly documented and medium-agnostic) and against the sibling leaves already documented in this atlas.

## Sources

Research date: **2026-09-08**

- Collections Trust — Spectrum 5.1, Condition checking and technical assessment: procedure page, the standard (minimum requirements), and suggested procedure — https://collectionstrust.org.uk/spectrum/procedures/condition-checking-spectrum-5-0/ , https://collectionstrust.org.uk/resource/condition-checking-and-technical-assessment-the-spectrum-standard/ , https://collectionstrust.org.uk/resource/condition-checking-and-technical-assessment-suggested-procedure/
- Collections Trust — software directory entry "TMS Collections and eMuseum" (Spectrum procedures supported; suite composition) — https://collectionstrust.org.uk/software/tms/
- Articheck — product site and Condition Reporting product page — https://www.articheck.com/ , https://www.articheck.com/risk-management/art-condition-reports/
- Gallery Systems — Collections Management (TMS Collections) and Conservation Documentation (TMS Conservation Studio) — https://www.gallerysystems.com/solutions/collections-management/ , https://www.gallerysystems.com/solutions/conservation-documentation/
- CatalogIt — product site, Conservator plan page, and Help Center (museum features; collections forms) — https://www.catalogit.app/ , https://www.catalogit.app/products/conservator , https://support.catalogit.app/en_US/museum-features
- eHive (Vernon Systems) — Help Center, field-level documentation of the conservation section (condition, risk and handling, proposed and completed treatment fields) — https://help.ehive.com/ , https://help.ehive.com/conservation-fields.htm

> Sourcing limitation: detailed operational documentation for the enterprise incumbents (TMS Collections, MuseumPlus) is login-gated, and several other market products (Axiell Collections, Vernon CMS desktop, Lucidea, PastPerfect) were unreachable from the research environment on 2026-09-08 (consistent with prior sibling passes). Evidence for those products rests on vendor product pages and the Collections Trust software directory; screen-level claims are avoided for them. The condition-record structure asserted in this document is anchored on the public domain standard and on the products with public documentation (eHive at field level; Articheck and CatalogIt at feature level). Precise product-specific details (field limits, exact rating scales, plan terms, security specifications) are deliberately not stated here; they are recorded in the paired Research Notes.
