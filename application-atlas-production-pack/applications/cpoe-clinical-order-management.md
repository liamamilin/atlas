# CPOE / Clinical Order Management

## Overview

A **CPOE / Clinical Order Management application** is the clinician-facing application through which care teams record requests for clinical action — medications, laboratory tests, diagnostic imaging, procedures, nursing tasks, consults, referrals — as **patient-specific orders**, make those orders available to everyone who must act on them, and manage each order through its life from creation through revision, renewal, and discontinuation.

It solves the problem that paper order sheets and verbal instructions could not: orders that are illegible, incomplete, unattributable, invisible to the departments that must fulfill them, and impossible to track. In this application, every request for action is a structured record with an identified ordering clinician, an identified patient, a named item of work, and a traceable state.

Its defining core is deliberately small:

```text
Identified ordering clinician
└── Order bound to one identified patient (usually a care encounter)
    └── Named orderable item from a catalog + execution parameters
        └── Shared visibility to the care team and fulfilling departments
            └── Managed lifecycle: new → revise / renew / discontinue, persistent order history
```

Everything commonly associated with hospital ordering — order-time decision support, order sets, STAT priority flags, electronic signature and countersignature, electronic transmission to labs and pharmacies, charge capture, mobile ordering — is widespread in mature products but is not what makes this the Type it is. Older, smaller, and resource-constrained ordering systems function as this Type without any of them.

In practice the Type is almost always realized as a module of an Electronic Health Record rather than as a standalone product; in US regulation, order entry for medications, laboratory, and diagnostic imaging is among the anchor criteria of a certified EHR. It remains a distinct Type because its objects, users, lifecycle, and interfaces are specific and independently recognizable.

## Users & Context

**Primary users — ordering clinicians:**

- physicians, nurse practitioners, and physician assistants who direct care and must express it as orders
- residents and supervised clinicians, whose ordering may be subject to review or secondary sign-off depending on product and jurisdiction
- covering clinicians, who need to see the active order set of a patient they are taking over

**Receiving/acting users (same record, different surface):**

- nurses, who receive orders as work to perform and acknowledge or act on them
- pharmacists, laboratory and radiology staff, who receive orders as fulfillment queues
- department clerks and coordinators who schedule and track the ordered work

**Maintenance users:**

- clinical informatics staff and pharmacy/therapeutics committees, who maintain the orderable catalog, order sets, and decision-support content

Typical context: inpatient units and emergency departments (the highest-density ordering environments), ambulatory clinics (fewer but still structured orders), and, in open-source and global-health deployments, district hospitals and clinics. The application is used repeatedly through every shift; ordering is one of the most frequent clinician interactions with an EHR.

## Core Model

### The defining core

**The order.** The central object. An order is a request from an identified clinician that a specific clinical action be carried out for a specific patient. An order records an intention — not whether or when the action is actually performed. That separation (request vs execution) is the structural seam between this Type and the systems that fulfill orders.

**The orderable item.** Every order names a specific item of work drawn from a catalog of orderable things: a medication, a laboratory test, an imaging study, a procedure, a consultation, a nursing task, a referral. The catalog is the application's vocabulary; a request without an identifiable item is documentation, not an order. Catalogs range from small locally configured lists to large governed libraries with typed classes of items.

**The orderer and the patient.** Each order is attributed to an identified clinician and bound to one identified patient — usually additionally tied to a care encounter (an admission, a visit) that frames the clinical context.

**Execution parameters.** The parameters needed to act on the request: for a medication, the drug, dose, route, frequency, and duration; for a test, the specimen, timing, and handling; for any order, instructions, effective dates, and urgency. The depth of structure varies by product and order class, but the principle holds: the order must contain enough for someone else to act.

**Shared accessibility.** Orders are recorded in a place where other authorized participants can see and act on them — this is what makes the application order *management* rather than a clinician's private notes.

**Managed lifecycle.** Orders change over time, and the system keeps those changes straight: new orders, revisions (typically recorded as a replacement linked to the prior order), renewals (re-activating a prior order), and discontinuations (stopping an order before or during execution). The per-patient order history persists; active and past orders remain distinguishable.

### Standard capabilities

Mature products add a stable set of structures around that core:

- **Order catalog governance** — order classes/types, grouped catalogs (for example, laboratory services organized into groups with defined expected results), and maintenance of the orderable vocabulary.
- **Priority and timing** — urgency levels and scheduled/as-needed timing patterns (in products that support them), so work can be sequenced. Exact priority values vary by product.
- **Order-time decision support** — checks and guidance surfaced inside the entry flow: duplicate-therapy warnings, interaction and allergy warnings for medication orders, dose guidance, corroboration prompts. The checks are a capability of the ordering flow, distinct from standalone decision-support systems.
- **Status tracking** — orders carry a state that advances over time (requested, accepted/in process, completed, cancelled — conceptual labels vary); in deployments that include the receiving loop, the fulfilling side updates that state and completed work links back to the order.
- **Transmission and routing** — sending orders to the responsible party: internal departments, external laboratories, pharmacies — with paper requisitions remaining a common fallback leg. The order record stands on its own even where transmission is absent; the record/change/access capability does not depend on it.
- **Authority and sign-off** — ordering implementations commonly commit orders under the ordering clinician's authority and support sign-off of results on the receiving side; mechanics — including secondary sign-off for supervised orderers and handling of orders placed on another clinician's behalf — vary substantially between products and jurisdictions.
- **Clinician personalization** — favorites, personal order lists, quick orders, and a chart-level orders summary (active orders first, historical below).
- **Access control and audit** — role-scoped access to ordering, and a record of who ordered, changed, and acted on each order.

### One structure, many implementations

```text
Concept:            Orderable item
Implementations:    code-system-backed concepts, locally configured procedure
                    catalogs, drug databases, department-specific catalogs

Concept:            Priority / timing
Implementations:    fixed urgency vocabularies, scheduled-date fields,
                    as-needed instructions, effective date ranges

Concept:            Getting the order to those who act on it
Implementations:    internal routing within the EHR, electronic transmission
                    to departments or external organizations, printed
                    requisitions, shared fulfillment worklists

Concept:            Authority to order
Implementations:    order entry limited by role, electronic signature at
                    submission, secondary/cosignature rules, jurisdiction-
                    dependent verbal-order handling
```

A reader who has only seen a large hospital EHR should still recognize a small clinic's ordering module from the defining core.

## How It Works

### Placing an order

```text
Select the patient (and care context)
→ find the orderable item
   (catalog search, favorites, or an order set)
→ configure the execution parameters
   (dose/route/frequency, specimen, timing, urgency, instructions)
→ observe order-time checks
   (duplicates, interactions, missing information — where provided)
→ commit the order under the clinician's authority
→ the order becomes active and visible to the care team
```

The entry step is deliberately structured: the clinician composes an order from catalog items and parameters rather than typing prose, because everything downstream (fulfillment, checking, tracking) depends on the order being discrete and machine-readable. In deployments with maintained order bundles, the "find the orderable item" step is often replaced by placing a whole set with adjustments.

### Moving work forward

```text
Active order
→ routed / transmitted / made visible to the fulfilling party
   (department, pharmacy, external lab — or a printed requisition)
→ fulfilling side accepts and performs the work
→ status advances; results or completed work link back to the order
→ ordering clinician reviews and signs off results
```

The ordering side and the fulfillment side work on the same order record through different surfaces. The ordering clinician sees state and results; the department sees a queue of work to accept, perform, and close.

### Maintaining the order set over a patient's stay

```text
New orders added as care evolves
→ revised (a replacement order linked to the prior one)
→ renewed (a prior order re-activated)
→ discontinued (stopped)
→ history retained: what was ordered, by whom, when, what happened
```

At care transitions, clinicians commonly review the active order set as a whole — deciding what continues and what stops — which is why the chart-level orders view is as important as the entry dialog.

### Core vs standard vs optional

**Defining core** — without these it is not this Type:

- patient-specific order record with identified orderer
- named orderable item from a catalog, with execution parameters
- shared accessibility to the care team and fulfilling parties
- managed lifecycle (new / revise / renew / discontinue) with persistent history

**Standard capabilities** — present in most mature products:

- catalog governance; priority/timing; order-time decision support;
  status tracking; results linkage and review; transmission incl. requisitions;
  authority/sign-off; personalization; access control and audit

**Optional / variant** — depends on setting, region, and product:

- order sets; charge capture coupling; mobile ordering; AI-drafted orders; deep
  structured medications with dose calculation; regional certification
  packaging; standalone vs embedded realization

## Interfaces

### Order composer (entry dialog)

The moment of ordering.

- shows the selected orderable item and its configurable parameters
- primary actions: set parameters, view warnings, sign/commit, cancel

### Patient orders view (chart)

The standing picture of what is ordered for this patient.

- lists active orders grouped by class or status, with historical orders below
- typical information: item, key parameters, ordering clinician, time, status
- primary actions: place new order, revise, renew, discontinue, view linked results

### Catalog / search

How clinicians find what to order.

- searchable orderable catalog, filtered by class; personal favorites
- primary actions: search, select, save favorite

### Order set library (where supported)

Curated bundles for conditions and pathways.

- organized by specialty/condition; hospital-customizable where supported
- primary actions: preview contents, place selected orders, adjust parameters

### Fulfillment-side worklist

The receiving department's view of the same orders.

- queues of orders to accept, perform, and close; status per order
- primary actions: acknowledge/accept, update status, record results/completion

### Results review

Where fulfilled work comes back to the clinician.

- results and reports linked to their orders; abnormal-result flags where supported
- primary actions: review, acknowledge/sign off, compare with history

### Catalog administration

Informatics-facing maintenance of the orderable vocabulary and order sets.

## Important Rules / Behaviors

### An order is a request, not the execution

The order record captures intent and state; the work itself happens in fulfilling systems and comes back as results and status. An order can be complete while its action is pending, and an action can be recorded only if its order existed.

### Authority gates the order

An order changes care when it is committed under an ordering clinician's authority — which is why orderers are identified individuals and why many products place signature, role checks, or secondary sign-off in the flow. Rules for orders placed on another clinician's behalf (for example, verbal orders later countersigned) are product- and jurisdiction-dependent.

### Revision preserves history

Changing an active order is commonly recorded as a linked replacement rather than an in-place overwrite: the record must show what was originally ordered, by whom, and when — because clinical and legal accountability attach to the order trail.

### Discontinuation is first-class

Stopping an order is as structurally important as placing one. Orders that are discontinued remain visible in history; they do not vanish.

### Fulfillment depends on catalog correctness

Status tracking and fulfillment flows generally work only for orderables that are correctly configured in the catalog; an item configured incompletely may order fine but fall out of tracking. Catalog maintenance is therefore operational, not cosmetic.

### Access is controlled and attributed

Ordering is high-stakes: implementations scope who may order what, and every order, change, and action is attributable to an identified user. This is reinforced in the US by certification requirements that attach privacy, security, and auditability criteria to CPOE.

### Transmission is common but not the essence

Many deployments transmit orders electronically; others print requisitions or rely on shared worklists inside the same system. The record, its accessibility, and its lifecycle stand regardless of the transmission mechanism.

## Variants

- **Setting packaging** — inpatient ordering (high volume, care-team coordination, STAT urgency) vs ambulatory ordering (fewer orders, more test-and-referral focus) vs emergency department ordering (speed, trauma pathways). Care-setting context is often carried on the order itself.
- **Class breadth** — US certification anchors the Type on medications, laboratory, and diagnostic imaging; deployments extend the catalog to nursing orders, consults, dietary requests, supplies, blood products, and referrals.
- **Medication ordering with a prescribing rail** — medication orders may stay inside the order record while transmission to pharmacies runs through dedicated e-prescribing machinery.
- **Embedded vs standalone** — almost always an EHR module; standalone ordering surfaces exist mainly as narrow add-ons.
- **Order-set-centric vs catalog-search-centric** — some deployments drive most ordering through maintained order sets; others rely on search and personal favorites.
- **Regional and regulatory context** — the modern US feature set (certified CPOE, attached decision support, privacy/security criteria) reflects its incentive framework; deployments elsewhere vary in structure and governance.
- **AI-era additions** — draft orders generated from notes or conversations, with clinician review before commitment; emerging and product-dependent.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Electronic Health Record / EHR | parent container | the EHR owns the whole chart (notes, problems, results, documents); this Type owns the request-for-action record and its lifecycle inside it |
| Electronic Prescribing | adjacent, medication-specific | prescribing centers on medication orders and external pharmacy transmission; this Type spans all order classes and internal fulfillment routing |
| Clinical Decision Support System | adjacent capability vs standalone system | CDS here is embedded checks inside the ordering flow; a CDSS centers on evaluation and advice over clinical data in its own right |
| Laboratory Information System / LIS, RIS, PACS | fulfillment-side receivers | they receive orders, perform the work, and return results; this Type is the ordering side of the hand-off |
| Pharmacy Management System | fulfillment-side receiver (medications) | dispensing and medication supply; ordering side belongs to this Type |
| Nursing Information System | executor surface | nursing works from orders (task lists, care activities); it does not define the order record |
| Care Plan Management | plan vs discrete orders | care plans express goals and intended interventions; this Type expresses discrete, actionable, trackable requests |
| Referral Management | overlapping class | a referral can be an order class here; a dedicated referral Type centers on the referral workflow itself rather than the general order record |
| Patient Scheduling | different object | scheduling books appointments; ordering requests clinical action independent of appointment slots |
| Order Management System / OMS (commerce) | lexical collision only | goods orders, inventory and logistics; no shared model beyond the word "order" |

The most consequential boundary is with the EHR: if a product cannot record, change, and make accessible per-patient clinical orders as its own managed record, it is not providing this capability — however complete its chart otherwise is. Conversely, a standalone product that does nothing but structured, lifecycle-managed clinical orders still qualifies.

## Representative Products

- **OpenMRS** — open-source medical records platform widely deployed in global-health settings; its order model is small, explicit, and concept-driven.
- **OpenEMR** — open-source ONC-certified ambulatory EHR; documents the full ordering-to-results loop for procedure/lab orders within a single system.
- **MEDITECH Expanse** — commercial EHR with a large community/rural and acute install base; orders are a core physician workflow with customizable order sets and department-side modules.
- **Oracle Health (Cerner Millennium heritage)** — commercial EHR suite co-dominant in US acute care; included as a market-structure anchor (detailed operational documentation not publicly accessible).

## Sources

Research date: **2026-09-07**

- OpenMRS — REST API documentation, Order / Order type resources — https://rest.openmrs.org/#orders
- OpenEMR — Project Wiki: home & certification listing — https://www.open-emr.org/wiki/index.php/OpenEMR_Wiki_Home_Page
- OpenEMR — Project Wiki: Procedure configuration & order process — https://www.open-emr.org/wiki/index.php/Procedure_configuration_%26_order_process
- MEDITECH — Expanse for Physicians — https://ehr.meditech.com/ehr-solutions/expanse-for-physicians
- Oracle Health — product page — https://www.oracle.com/health/
- ONC Health IT Certification Program — CPOE certification criteria (medications / laboratory / diagnostic imaging; Base EHR definition) — https://www.healthit.gov/test-method/computerized-provider-order-entry-medications

> Sourcing limitation: operational documentation for the largest vendors (Epic; Oracle Health user guides) is not publicly accessible from the research environment — Epic's site rejected access and Oracle Health documentation is gated; those products were used for market structure only, and no workflow claims are made about them. The medication-specific ONC criterion page redirected to the laboratory criterion. Accordingly, precise operational details (exact status vocabularies, signature mechanics, numeric limits, default settings) are intentionally not asserted in this document; the record of what was and was not directly observed is in the paired Research Notes.
