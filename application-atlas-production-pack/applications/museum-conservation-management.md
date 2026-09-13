# Museum Conservation Management

## Overview

A **Museum Conservation Management** application is the museum's conservation-work system of record: it manages and documents care and treatment work performed on collection objects — from the initial proposal through authorization and treatment to the recorded outcome and any planned follow-up.

The defining structure is small:

```text
Identified collection object (the collection register's record)
└── Conservation work record
    ├── object-bound (findable through the object number), attributed, reason-coded
    ├── proposal side (scope, priority, reason — agreed and authorized before work)
    ├── outcome side (method, materials, dates, result — the treatment report)
    └── accumulated care history
        ├── retained per object and referable across years
        ├── outcomes written back to the object record (handling, storage, display, hazards)
        └── planned follow-up (recall dates, further treatment, periodic care)
```

Everything commonly associated with the discipline — treatment templates, before/during/after photography, controlled vocabularies for methods and materials, external-conservator contracting, priority scoring — is standard capability of mature products, not what makes the workflow conservation management. A paper treatment card filed by object number, with a written proposal, an authoriser's signature, the materials and dates of the work, and a recall note, satisfies the same structure; the domain standard for this practice is explicitly medium-agnostic.

The workflow manages **intervention**. It does not merely document **state** — the dated assessment of an object's physical condition is the neighboring discipline of condition reporting. The two interlock constantly (an object's condition is recorded before treatment begins, and a worrying condition finding escalates to a conservator), but they are distinct workflows, held apart by the domain standard's own procedure split, by product field structures, and by product packaging alike.

## Users & Context

Primary users are the conservation and collection-care staff of museums, galleries, and historic houses, and conservators serving them from outside:

- **Conservators** — the central users. They examine objects, propose and scope treatment, perform and record the work, and produce the treatment reports. In small institutions the conservator may be a single in-house staff member or an external specialist.
- **Collection managers and registrars** — initiate and receive conservation work in the course of other procedures: an object going on loan needs treatment or a condition baseline; an exhibition requires assessments; a scheduled survey finds work to do. They rely on the conservation history when preparing loans and display plans.
- **Approvers / department heads** — authorize conservation work under the institution's policy; the domain standard treats authorization as a distinct step ("no conservation work happens without the knowledge of those responsible for the objects").
- **External conservators and consultants** — carry out contracted work; the institution manages their agreements and receives their records back into its documentation. Private-practice conservators run the same workflow for many clients at once, holding the records themselves and delivering reports, summaries, and treatment plans to clients.

The work environment is physical — conservation studios and labs, stores, galleries, loading docks — with the objects themselves unique and irreplaceable. The governing context is the institution's collections-care policy: who may propose, who must authorize, who may treat, what depth of documentation each kind of work requires, and when objects must be re-examined after treatment.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the application stops being conservation management.

**The object-bound conservation work record.** Every item of care or treatment work — proposed or performed — exists as a record bound to the identified collection object, so that all conservation information for an object is findable through its object number. Each record carries its attribution (who performs the work, who authorized it, when) and the reason for the work (a condition finding, a loan or exhibition requirement, routine care). The record may be a dedicated record, a repeating group of fields on the object record, or a document filed against it — realizations differ; the anchoring does not. Without it, the product is either descriptive cataloguing with conservation notes, or a generic task board.

**The proposal-to-outcome progression.** Conservation work exists as a proposal before it exists as an intervention. The proposal records the scope of work, its priority, and its basis (usually a condition assessment or the conservator's recommendations), and is agreed in writing and authorized before anything happens to the object — with the owner's consent when the object is not owned (for example, proposed treatment on a borrowed object). Only then is the work executed and recorded as completed intervention: what was done (procedure, method, materials used), when it began and ended, and what the result was — together forming the treatment report, the record's deliverable. Without this progression, the system is either a bare log of care actions with no managed intent, or condition reporting (assessment without intervention).

**The accumulated care history that feeds back.** Conservation records accumulate per object and stay referable: the institution can always read an object's full conservation history. The workflow does not end at the treatment report — key outcomes are written back to the object record so everyone who handles the object benefits (revised handling, packing, storage, and display recommendations; hazard notes; new information about how the object was made, which belongs in the catalogue, not buried in conservation files). And further care is planned: recall dates for follow-up examination, scheduled further treatment, periodic care activities. Without this, the system is episodic paperwork; the institutional memory and the "management" collapse.

### Capabilities Shared by Mature Products

A typical modern product carries most of the following. They make the workflow practical; they do not define the Type.

- **Pre-treatment condition baseline** — the object's condition is documented before work begins, usually by reusing the institution's condition-checking workflow. The standard makes the prior assessment the basis of the proposal.
- **Conservation priority** — a recorded rating of how urgently an object needs attention, feeding what gets treated next.
- **Treatment reports as documents** — formatted, exportable reports with images, for the file, for owners, for clients, for insurers.
- **Before/during/after photography** — images attached at each stage, commonly with annotations marking damage or treatment areas on the object.
- **Controlled terminology** — methods and materials recorded from standard term sources or thesauri so that records stay consistent and searchable.
- **Per-component tracking** — treatments recorded at the level of individual parts of composite or multi-part objects.
- **Hazard and handling write-back** — the outcomes of treatment that affect everyone who touches the object, transferred to the object record itself.
- **External-conservator contracting** — agreement contents, timetable, and the transport, handling, security, insurance, and access arrangements for objects leaving for treatment; the returned records filed with references from the object record.
- **Searchable consolidation** — all conservation documentation for the institution in one searchable place, rather than scattered across paper files and spreadsheets.
- **Concurrent work tracking** — many treatments in progress across many objects, organized as projects or worklists.

### One Structure, Many Implementations

The core is conceptual; realizations differ:

```text
Concept:   Object-bound work record
Realized:  field groups on the object record · a module record · a standalone studio record synced
           to the collection system · an entry-level history in a practice tool

Concept:   Proposal → authorization → treatment → outcome
Realized:  separate proposed/completed field groups · procedure stages with authoriser fields ·
           plan deliverables followed by treatment-stage entries

Concept:   Retained care history
Realized:  accumulating dated fields on the object record · a searchable documentation corpus ·
           repeating per-stage entries
```

A reader who encounters only one realization — say, treatment fields inside a small museum's cataloguing system — should still recognize the dedicated conservation studio and the private-practice tool as the same Type.

## How It Works

The workflow is a loop, usually entered from another procedure rather than run for its own sake:

```text
Trigger (condition finding / loan / exhibition / intake / scheduled care)
→ consult the object's conservation history and prior condition records
→ examine the object (baseline condition; recommendations)
→ propose the work (scope, priority, reason)
→ agree and authorize (owner consent if the object is not owned)
→ prepare the work (reference the object; provide object information to the conservator;
   move the object through the movement procedure if needed)
→ carry out the treatment
→ record it (method, materials, dates, result; attach photographs and analysis)
→ produce the treatment report; write outcomes back to the object record
→ schedule follow-up (recall date, further treatment, periodic care)
→ on the recall date, re-examine and record condition — the loop continues
```

**A need is identified and scoped.** Most conservation work results from condition checks and is prompted by other procedures — an object is going on loan, entering an exhibition, or a survey has found deterioration. If the conservator has previously assessed the object, those recommendations form the basis of the proposal; otherwise the conservator examines the object first and recommends treatment.

**The work is agreed and authorized before it happens.** The proposal is agreed in writing. When the objects belong to the institution and the conservator is in-house this may be simple; when the objects are borrowed, the owner's written consent is required; when an external conservator is contracted, a formal agreement covers the assessment and recommendations, the timetable, the authority to carry out the work, terms, and the transport, handling, security, insurance, and access arrangements for the period the objects are with the conservator. The system holds the authoriser and the authorization date alongside the work reference.

**The conservator is given the object's context.** The work record connects to what the conservator needs: the object number, description and materials, location, technical descriptions and prior condition assessments, previous conservation history, the recommended treatment, the reason and requester, the completion date, and any hazards. If the object must move — to an in-house studio or out to an external conservator — that movement is recorded through the institution's location-and-movement procedure, not through the conservation record itself.

**The treatment is carried out and recorded.** As the work proceeds or as soon as possible afterwards, the record captures when the work began and ended, what was actually done — the procedure, the method, the materials used, the duration, and the result — plus reference numbers of the reports, photographs, drawings, and technical images generated along the way. Any parts newly fitted or made are recorded. Where a treatment will destroy evidence (for example, removing material that could later be analyzed), that too is noted, along with any steps taken to preserve it beforehand.

**Outcomes are written back and the future is planned.** The treatment report is produced for the file or for an external party. New or revised handling, packing, storage, and display recommendations and hazard notes are transferred to the object record so they are immediately available to everyone. New knowledge gained about how the object was made goes into the catalogue record, not just the conservation file. If follow-up examination is needed, a recall date is set; when it arrives, the object is re-examined and its condition recorded — the longer-term success of the treatment is itself checked through the condition workflow.

**Depth follows the kind of work.** Routine housekeeping (such as dusting objects on open display), preventive care measures, emergency stabilization after a disaster, bulk treatment campaigns, and full single-object treatments are all conservation events, and the depth of documentation varies accordingly — with emergency records completed in full once conditions allow.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Object conservation view

The hub surface — the conservation picture of one object.

- Typical information: the object's identity and images, its conservation history (proposals, treatments, dates, conservators), current conservation priority, handling and hazard notes from past work
- Primary actions: open or create a proposal or treatment record, read past records, jump to the object's full catalogue record

### Proposal / treatment record editor

The capture surface — where work is proposed, authorized, and recorded.

- Typical information: proposal fields (scope, priority, reason, basis in prior assessment) and treatment fields (method, materials, begin and end dates, result), organized as separate proposed and completed sections in common implementations
- Primary actions: write and revise the proposal, record authorization, log the treatment as it proceeds, attach images and documents, save against the object with attribution

### Treatment report output

The deliverable surface — the record as a document that can leave the studio.

- Typical information: the formatted treatment report with images, the methods and materials used, the result, and the recommendations, with attribution and dates
- Primary actions: generate, print, or export the report; deliver it to an owner, client, or the institution's files

### Care-history and search views

The memory surface — reading and finding the institution's conservation corpus.

- Typical information: all proposals and treatments for an object in sequence; institution-wide search over conservation documentation
- Primary actions: review a treatment history, find records by object, conservator, method, or reason, compare past work

### Work planning surface

The management surface — the conservation program as a whole.

- Typical information: objects awaiting or undergoing treatment, priorities, agreed work and its timetable, recall dates coming due, ongoing periodic care
- Primary actions: prioritize, schedule, assign, track progress across concurrent treatments

### Mobile and in-studio capture

The point-of-work surface.

- Typical information: the object at hand (found via search or number), its conservation and handling summary
- Primary actions: photograph, annotate damage or treatment areas, update the record as the work happens

## Important Rules / Behaviors

**No work without authorization.** A decision to treat an object — or to change its standard of care — requires the knowledge and authorization of those responsible for the objects. The record itself carries the authoriser and the authorization date. When the object is not owned (a borrowed object, a client's object), the owner's written consent is part of the agreement.

**The object number is the anchor.** All conservation information is accessible through the object's identity. Work that cannot be tied to an identified object does not serve the discipline; products that operate outside a collection system carry their own object records for exactly this reason.

**Every record is attributed and dated.** Who proposed, who authorized, who treated, when the work began and ended. This is what makes the conservation history auditable and why it survives staff turnover and decades.

**History is retained, not overwritten.** New work adds records; prior records stay referable. A conservator proposing new work reads the object's full conservation history first — and the institution can check other objects that might be affected by the same materials or the same past treatment.

**Outcomes return to the object record.** Handling, packing, storage, and display recommendations, hazard notes, and new information about the object's make-up are written back to the catalogue so they are generally accessible. Conservation knowledge locked inside conservation files is treated by the standard as a failure state.

**Assessment is not treatment.** The condition workflow documents state and escalates; this workflow intervenes and records. The standing interlocks run in both directions: a condition report is made before treatment begins, and treatment ends by scheduling call-back condition checks.

**Documentation depth varies by event type — and is completed.** Mass treatment, preventive measures, and housekeeping warrant lighter recording than a full treatment; emergency treatment performed under pressure is recorded in full once conditions allow. Where a treatment will eliminate evidence (analysis opportunities, original material), the loss and any countermeasures are recorded as part of the result.

**Movement belongs to the movement procedure.** Objects travelling to and from conservation — including out to external conservators — move through the institution's location-and-movement and exit procedures. The conservation record documents the work, not the whereabouts.

## Variants

- **Field-group realization** — conservation recorded as proposed/completed field groups directly on the object record in lighter collection systems; the small-museum norm, and proof the Type does not require a dedicated module.
- **Suite-module realization** — conservation as a core module of a full collection management suite, alongside location, loans, exhibitions, and valuation machinery.
- **Dedicated conservation studio** — a standalone conservator-facing product holding the institution's conservation documentation in one searchable place and syncing object data with the collection system.
- **Private-practice posture** — the conservator, not the museum, holds the records: many clients, many concurrent projects, objects moving between clients and the lab, deliverables (reports, condition summaries, treatment plans) sent to clients.
- **Scope variants within the workflow** — interventive treatment, preventive conservation programs, housekeeping, emergency and disaster response, and bulk/mass treatment campaigns; the same record structure with different depth.
- **In-house vs external execution** — work done in the institution's own studio versus contracted out, with agreement and returned-records handling in the external case.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Condition Reporting | closest sibling — state vs intervention | condition reporting documents an object's physical state as dated, attributed assessments and escalates concerns; conservation management proposes, authorizes, performs, and records care and treatment. They interlock at the pre-treatment baseline report and the post-treatment recall check |
| Museum Collections Management | container | the collection system of record owns the object records that conservation work attaches to, plus location, loans, and the other custody events; conservation management is one care-event family given its own workflow here |
| Museum Object Movement Management | procedure neighbor | objects move to and from conservation through movement control and exit procedures; conservation records the work, not the location |
| Museum Loan Management | trigger and constraint | loans prompt treatment and require owner consent for work on borrowed objects; the loan owns the transaction, conservation owns the work |
| Exhibition Installation Management | consumer | installation consumes condition documentation at handovers; treatment decisions made here feed what can safely be displayed and handled |
| CMMS / Equipment Maintenance | shape neighbor | similar work-order-and-schedule shape, but a different subject world: unique irreplaceable collection objects, documentation-first practice where the record permanently captures new knowledge of the object, and no failure/preventive-maintenance asset machinery |
| Conservation Management (environment) | name neighbor only | protection of natural areas, species, and habitats — no collection objects and no treatment records |
| Cultural Heritage Asset Management | registry neighbor | place-based heritage inventories (monuments, buildings, sites) as the unit of record, not object-level treatment workflow |
| Building Condition Assessment | assessment neighbor | the same assessment-documentation shape applied to buildings, without the treatment workflow or collection-object identity |

The load-bearing boundary is with **Museum Condition Reporting**. The two share authors, media, and even specific moments (the pre-treatment report), but the record classes differ — state assessment versus treatment intervention — and the domain standard, product field structures, and product packaging all keep them separate.

## Representative Products

- **TMS Conservation Studio** (Gallery Systems) — dedicated conservation-documentation studio for museum conservators; condition, damage, and treatment reporting, image annotation, vocabulary control, and record syncing with its companion collection system
- **MuseumPlus** (zetcom) — enterprise museum suite with conservation as a core module; validated as supporting the domain standard's conservation and condition procedures
- **eHive** (Vernon Systems) — mid-market cloud collection system; conservation handled as proposed-treatment and completed-treatment field groups (with priority, risk, and handling) on the object record
- **CatalogIt (Conservator plan)** (It Unlimited) — small-tier system for conservators in private practice; per-stage condition and treatment history across many client projects, with reports, summaries, and treatment plans as client deliverables

The definition was checked against the domain standard — Spectrum, the UK museum collections-management standard used internationally, whose "Collections care and conservation" procedure, minimum requirements, and suggested procedure are publicly documented and medium-agnostic — and against the sibling leaves already documented in this atlas.

## Sources

Research date: **2026-09-08**

- Collections Trust — Spectrum 5.1, Collections care and conservation: procedure page, the standard (minimum requirements), and suggested procedure — https://collectionstrust.org.uk/spectrum/procedures/collections-care-and-conservation-spectrum-5-0/ , https://collectionstrust.org.uk/resource/collections-care-and-conservation-the-spectrum-standard/ , https://collectionstrust.org.uk/resource/collections-care-and-conservation-suggested-procedure/
- Collections Trust — software directory entries for MuseumPlus and eHive (module lists, Spectrum procedure support, compliance) — https://collectionstrust.org.uk/software/museumplus/ , https://collectionstrust.org.uk/software/ehive/
- eHive (Vernon Systems) — Help Center, field-level documentation of the conservation section (condition, risk and handling, proposed treatment, completed treatment) — https://help.ehive.com/conservation-fields.htm
- Gallery Systems — Conservation Documentation (TMS Conservation Studio) product page and conservation-management editorial — https://www.gallerysystems.com/solutions/conservation-documentation/ , https://www.gallerysystems.com/conservation-management-for-museums-operational-excellence/
- zetcom — MuseumPlus product page — https://www.zetcom.com/en/museumplus-en/
- CatalogIt — Conservator plan page — https://www.catalogit.app/products/conservator

> Sourcing limitation: detailed operational documentation for the enterprise products (MuseumPlus, TMS Conservation Studio) is login-gated, and several other market products (Axiell Collections, Vernon CMS desktop, Lucidea, PastPerfect) were unreachable from the research environment — consistent with prior sibling passes. Evidence for those products rests on vendor product pages and the Collections Trust software directory; screen-level claims are avoided for them. The workflow structure asserted in this document is anchored on the public domain standard and on the products with public documentation (eHive at field level; TMS Conservation Studio and CatalogIt at feature level). Product-level existence of scheduling machinery for recall dates, time and cost tracking, and in-product preventive-care programs is not asserted; those structures are documented at standard level only. Precise product-specific details are deliberately not stated here; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison matrix, and the historical / market-sample check are recorded in the paired Research Notes.
