# Child Welfare Management

## Overview

A **Child Welfare Management** application is the statutory casework system used by child protection and child welfare agencies to safeguard children: it holds identified child and family records, receives and screens reports of concern about a child's safety or wellbeing, structures safety and risk assessments, carries each accepted concern as a casework episode under an accountable caseworker, and — when a child cannot remain safely at home — manages the out-of-home placement and permanency machinery (kinship and foster homes, residential resources, reunification, adoption) through to closure of the case.

The defining core is deliberately small:

```text
Identified child (protected person record)
└── Family / caregiver context around the child
    └── Report of concern → recorded screening decision
        └── Safety / risk assessment with recorded findings
        └── Casework episode under an accountable caseworker
            └── Placement & permanency structures (when removal happens)
```

Everything sits under need-to-know confidentiality enforced by the system's permission model.

What the definition excludes matters as much as what it includes: the specific statutory vocabulary (which differs by country), national reporting codes, court procedures, payment engines, hotline phone numbers, and AI assistance are all real parts of how modern products are packaged, but systems from different eras and jurisdictions run the same type of work without any of them.

## Users & Context

The primary user is the **caseworker** (social worker / child welfare worker): a government or contracted-agency employee who carries a caseload of children and families, conducts home visits, completes assessments and safety plans, documents contacts, refers families to services, and prepares court-related material. Field work is a large share of the job, so the system must travel with the worker.

Around the caseworker:

- **Intake / screening staff** — receive reports of concern (phone, web, referrals from police, schools, health services), record them, and make or support the initial screening decision.
- **Supervisors** — review and approve worker documentation (especially safety and support plans), assign and balance caseloads, monitor deadlines and milestones.
- **Foster care / licensing staff** — recruit, assess, license, and support foster and kinship carers and adoptive applicants; run placement matching.
- **Administrators** — configure forms, workflows, programs, users, and permissions; prepare regulatory reports.
- **External professionals** — with scoped, limited access or through delegated forms: service providers, health or education professionals, other agencies contributing to an assessment.

The operating context is a legal one: the agency exercises statutory authority over family life. Every significant action — accepting a report, substantiating maltreatment, removing a child, changing a placement, closing a case — happens inside a framework of mandates, deadlines, and potential court review, and the record must be defensible.

## Core Model

### Person records: the child at the center, the family around it

The center of the system is the **child**: an individually identified protected person record holding demographics, identifying information, involvement history, and everything else that attaches to the case. Child welfare work is family-based, so the child record never stands alone: **caregiver/parent records**, **sibling and household relationships**, and wider family connections are modeled and linked to the child. Products make this family context explicit in different ways — shared family forms that keep individual child records separate, or relationship maps generated from the case file — but the child-plus-family structure is constant.

Alongside children, the system holds **carer and resource records**: foster homes, kinship caregivers, special guardians, adoptive applicants, and residential providers — each with an assessment/licensing status of its own. These are the resources that placement draws on.

### Report, screening, and assessment

Work enters as a **report of concern** (referral): an allegation or worry about a child's safety, received from the public, professionals, or other agencies. Each report gets a recorded **screening decision** — accept for investigation or assessment, redirect to another agency or a lower-threshold service, or close without action. Accepted reports move into **assessment**: structured instruments that record the safety and risk situation of the child, often alongside a **safety plan** (immediate protective arrangements) and, where the family stays engaged, a longer-term plan built from assessed strengths and needs.

### The case (casework episode)

The durable unit of work is the **case**: an episode of statutory involvement with a child and family, owned by an accountable caseworker, carrying its own status within the agency's program pathway (for example: investigation/assessment → in-home services → out-of-home care → permanency and closure; in UK terms, children in need, child protection, looked-after children). The case accumulates:

- **case notes / contact records** — the dated narrative of every visit, call, and observation;
- **documents and forms** — assessments, safety plans, consents, court-related paperwork;
- **tasks and workflow items** — with due dates, priorities, and supervisor approval gates;
- **placements** — where children are living over time, with start/end and moves;
- **services** — referrals made to providers and their status;
- **legal status** — the court involvement and orders that condition what the agency may do.

### Placement and permanency

When a child cannot remain at home, the system manages the **placement**: matching the child against available carers/homes using recorded criteria, recording the placement start, monitoring it, and recording moves or disruptions. The carer side runs in parallel — recruitment, application, eligibility assessment, licensing or approval, and ongoing support of foster, kinship, and adoptive families. The case carries a **permanency direction** — reunification with family, kinship/guardianship, or adoption — that organizes the endgame of the episode. Care-experienced young people (those leaving care) remain in the record after placement ends.

### One structure, many implementations

```text
Concept:  program pathway of the case
Implementations:  US investigation/in-home/foster/adoption stages;
                  UK child-in-need / child-protection-plan / looked-after-child pathways

Concept:  carer/resource record
Implementations:  foster home license, kinship approval, connected-person
                  assessment, adoptive applicant home study

Concept:  regulatory reporting
Implementations:  US federal data submissions; UK statutory returns;
                  agency-level compliance/audit reports
```

A reader who has only seen one implementation (say, a US state system) should still be able to recognize a UK local authority children's services system — or a private foster-care agency's case management — from the structure above.

## How It Works

### Receive and screen a report

```text
Report arrives (phone / web form / professional referral)
→ intake staff create a report record (child, family, allegation, source)
→ screening: check prior history of the child, family, and alleged persons
→ record the screening decision
→ accepted: assign and open a case
→ redirected: hand off to another agency or a support service
```

History matters here: prior intakes, prior cases, and prior involvement of the same people are surfaced to the screener, because pattern history changes the decision.

### Assess and decide

```text
Open the case
→ complete structured safety/risk assessment (often within mandated deadlines)
→ where danger exists: record and share a safety plan
→ record findings and the program decision
→ in-home services, or removal and placement
→ supervisor reviews and approves key documents
```

### Run the case

```text
Visit the family (field/mobile capture, offline if needed)
→ document contacts as case notes and forms
→ complete and route tasks before their due dates
→ refer family members to services; track enrollment and outcomes
→ supervisor approval gates on plans and significant documents
→ recurring reviews keep the record current and legally defensible
```

This loop is the daily life of the application: field visit → documentation → tasks → approvals. Mobile capture (photos, audio, signatures, auto-linked to the child and case) feeds it, and deadline/milestone alerts police it.

### Place a child and work toward permanency

```text
Removal decision (with legal authority)
→ search carers/homes matching the child's needs (kinship and foster options)
→ record the placement; start carer payments where applicable
→ monitor: visits, placement stability, the child's needs
→ work the permanency plan (reunify / kinship / guardianship / adoption)
→ record the outcome; close the placement, then the case
```

### Core, standard, and optional capabilities

**Defining core** — without these, the software is not child welfare management:

- identified child record with linked family/caregiver context
- report intake with recorded screening decision
- safety/risk assessment with recorded findings
- casework episode under an accountable caseworker, tracked to closure
- out-of-home placement and permanency as built-in structures
- need-to-know confidentiality over the record

**Standard capabilities** in mature products:

- case notes and structured documentation
- configurable forms and assessment instruments
- task/workflow routing with due dates and supervisor approval
- service referrals and provider/service tracking
- family and kinship relationship mapping
- mobile/offline field capture
- family, carer, and provider portals (document exchange, e-signatures)
- scoped multi-agency information sharing
- reporting, dashboards, and audit preparation
- regulatory reporting data capture
- integration with state or national systems

**Common variants / optional** — depending on jurisdiction, tier, and posture:

- carer recruitment and licensing workflow depth
- placement- and provider-linked payments and finance modules
- early-help/prevention casework below statutory thresholds
- AI assistance (transcription-to-form, case-file analysis, policy Q&A)
- tribal/First Nations program adaptations

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Intake / report record

The entry surface for concerns. Typical information: source, child and household, allegation, prior-history flags, screening decision. Primary actions: create report, record decision, convert to case, or redirect.

### Case file (child and family view)

The worker's home surface — usually a person-centric view of the child with tabs or sections for the family group, the case status, notes, documents, placements, services, and legal events. Primary actions: open documentation, add notes/forms, view history, follow links to related people.

### Assessments and forms

Structured instruments with required fields, validation, and often versioning; completed in the office or in the field. Primary actions: fill, save, submit for approval, review prior versions.

### Task / workflow queue

The worker's to-do surface: assigned tasks and routed documents with due dates and priorities; the supervisor's counterpart view shows the team's queue, approvals, and caseload health.

### Placement matching and carer records

Search-and-match surfaces over the carer/home pool (filter by capacity, needs, location, approval status), plus carer detail records tracking application, licensing status, and support history. Primary actions: match, place, record moves, update carer status.

### Reporting and dashboards

Caseload summaries, milestone/deadline compliance, activity gaps, and regulatory-report preparation. Primary actions: run reports, drill into exceptions, export.

### Portals and mobile

Family/carers/providers get scoped portals (upload documents, sign forms); caseworkers get a mobile surface for field capture that works offline and attaches media to the right child and case automatically.

## Important Rules / Behaviors

### Need-to-know access is structural

Records are held confidentially by the agency and, inside it, visible on a need-to-know basis by role and assignment. Workers see the children they are responsible for; external professionals see only the scoped pieces delegated to them; every product in the researched sample treats record-level access restriction as a first-class feature. Deletion is generally not the model — the record is retained and auditable.

### Supervisory approval gates the record

Key documents — assessments, safety plans, case closings — typically require supervisor review and approval before they take effect. The approval chain is part of the record's defensibility.

### Mandates drive deadlines

Statutory requirements attach concrete deadlines (time to see the child, time to complete an assessment, frequency of visits, periodic reviews). Products commonly encode these as milestone dates and alerts; the specific durations are jurisdiction-specific and vary.

### Legal status conditions action

What the agency may do — where a child may live, whether reunification services are required, whether an adoption can proceed — depends on the legal posture of the case (voluntary services vs court order vs custody). Legal events and orders therefore attach to the child welfare case even though the court's own docket lives in a separate system.

### Placement must land on an eligible resource

A child can only be placed in a carer home or facility with the appropriate approval status and capacity; placement records and carer records constrain each other. Moves and disruptions are recorded events with consequences for the case.

### History is never discarded

Prior reports, prior placements, and prior involvement of the same individuals are surfaced during screening and assessment — the record is longitudinal, often spanning years and multiple episodes for the same family.

## Variants

- **State system of record (US)** — a comprehensive statewide system holding the full statutory record and producing national data submissions; historically large government-built systems, now also commercial products operating under federal approval waivers.
- **Agency-side casework layer (US)** — products used by county or contracted agencies for day-to-day casework that exchange data bidirectionally with the state system rather than replacing it.
- **Local authority children's services (UK)** — case management organized around children in need, child protection plans, and looked-after children, with carer assessment and placement-linked finance typically integrated.
- **Private / nonprofit delivery agencies** — contracted foster-care and family-service agencies running the casework record for the children they serve; the same core structure at a smaller, organization-scoped scale.
- **Tribal / First Nations programs** — child welfare under tribal authority, often with additional sovereignty and data-governance considerations.
- **Prevention / early-help tier** — the same person/case spine applied to families below statutory intervention thresholds, usually as a module of the main system.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Social Services Case Management | broader sibling | general casework for human services without the statutory child-protection loop, safety-assessment machinery, or placement/permanency structures |
| Public Sector Case Management | broader | generic government request/case handling; no child/family person model, no placement resources |
| Nonprofit Case Management | adjacent | service-delivery casework for nonprofit programs; child welfare adds mandated intake and legal authority regardless of operator |
| Court Case Management System | adjacent | manages the court's own docket; child welfare systems attach legal status and court events to the case but do not run hearings |
| Care Plan Management / Care Coordination | adjacent (health) | organizes clinical care around a person; no statutory screening, custody, or placement semantics |
| Beneficiary Management | adjacent | population registry and what was delivered; child welfare is a bounded casework episode under an accountable worker |
| Adult Protective Services software | adjacent analog | same protective casework pattern (report → screen → investigate → case) for vulnerable adults; different protected population and program law |
| Child Support Enforcement software | commonly confused | financial support between parents (paternity, orders, collections) — a different domain that some vendors ship as a separate product line |

The most important boundary is with **Social Services Case Management**: the test is whether the system carries the statutory protection loop — mandated report screening, safety assessment, placement and permanency. Remove that, and the same records become generic social services case management; add a placement search, and a generic case system does not become child welfare.

## Representative Products

- **Casebook** (Casebook PBC) — configurable commercial child welfare and foster care/adoption case management; US state, county, and private agencies
- **Northwoods Traverse** — agency-side child welfare casework and electronic case files for US county human services, exchanging with state systems
- **System C Liquidlogic Children's Case Management** — UK local authority children's social care case management (children in need, child protection, looked-after children)

The type was additionally checked against an adjacent analog (adult protective services software) and against platform-tier public-sector case management positioning, to avoid over-fitting the definition to one country's or one vendor's structure.

## Sources

Research date: **2026-09-06**

Official vendor sources (product pages and FAQ):

- Casebook — Child Welfare, Foster Care & Adoption, and Platform Overview pages: https://www.casebook.net/casebook-child-welfare-software/ , https://www.casebook.net/casebook-for-foster-care-and-adoption/ , https://www.casebook.net/platform-overview/
- Northwoods — Traverse for Child Welfare and Traverse Modules: https://www.teamnorthwoods.com/traverse/traverse-program-areas/traverse-for-child-welfare/ , https://www.teamnorthwoods.com/modules/
- System C (Liquidlogic) — Children's Case Management: https://www.systemc.com/local-government/liquidlogic-childrens-case-management/
- WellSky — Protective Services (adult; boundary context only): https://wellsky.com/solutions/community/protective-services/
- Salesforce — Public Sector (positioning context only): https://www.salesforce.com/industries/public-sector/

> Sourcing limitation: vendor help centers and knowledge bases were not reachable from the research environment on 2026-09-06 (extendedReach blocked ×2; Casebook and Northwoods help centers not fetchable; System C customer centre login-gated). All product evidence is Tier-2 official product pages and FAQs. Statements in this document are therefore calibrated to that evidence: no case-state vocabularies, numeric limits, deadline durations, or default settings are asserted, and jurisdiction-specific program rules are described only where the sampled products document them. Detailed observations and comparisons are recorded in the paired Research Notes.
