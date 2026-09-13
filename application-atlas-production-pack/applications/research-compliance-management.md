# Research Compliance Management

## Overview

A **Research Compliance Management** system is the research institution's compliance-program system of record. It manages the institution's obligations for how research may be conducted — protection of human subjects, animal welfare, conflicts of interest, biosafety and hazardous materials, export control, data protection — as a set of managed compliance domains. Within each domain, researchers submit protocols, disclosures, registrations, and plans; compliance staff and faculty committees review them and record determinations; and the resulting approvals, conditions, events, and training records are retained as the institution's evidence of compliance for regulators, auditors, accreditors, and its own leadership.

The defining core is small:

```text
Institution's research-compliance obligations (managed compliance domains)
└── Compliance submission (protocol / disclosure / registration / plan)
    └── Review-and-determination loop (triage → review → recorded determination)
        └── Audit-ready compliance record (retained evidence of compliance)
```

Everything else commonly associated with these products — committee meeting machinery, configurable form builders, training tracking, dashboards, integrations with grants systems — is widespread in mature products but is not what makes the system a research compliance system. A paper-era compliance office running on protocol files, minute books, and approval letters satisfies the same core.

When the system narrows to a single domain — only human-subjects protocols, or only animal-use protocols — it becomes the territory of the single-domain ethics-review Types (IRB / Research Ethics Management, Animal Research Ethics / IACUC Platform). The multi-domain program frame is what distinguishes this Type.

## Users & Context

The system serves a research institution — a university, academic medical center, hospital research program, nonprofit institute, or national research organization — that must operate a compliance program over the research conducted under its name.

Primary users:

- **Investigators and study teams** — create and submit protocols, disclosures, and registrations; respond to reviewer questions; file renewals, amendments, and reportable events; keep their training current.
- **Compliance staff / administrators** — the operational core of the system. They triage submissions, route them through review paths, correspond with researchers, issue determination letters, track renewals and events, and maintain the institution's compliance records.
- **Committee members and reviewers** — faculty and staff who evaluate assigned submissions against the applicable rules, record comments and rationale, and convene as committees to decide.

Secondary users:

- **Institutional officials and leadership** — read the aggregate compliance picture across domains: pending work, approval times, open events, training gaps.
- **Auditors, regulators, and accreditors** — external parties served from the retained records during inspections, site visits, and accreditation reviews.

The work environment is administrative and calendar-driven: submissions arrive continuously, committees meet on cycles, approvals expire and must be renewed, and events must be reported within institutional or regulatory timeframes.

## Core Model

### The Defining Core

**Compliance domains.** The system's organizing frame is the institution's set of research-conduct obligations. Each obligation regime is held as a managed compliance domain with its own submission types, review process, and rules. The specific domain set varies by institution and jurisdiction — a US university typically runs human subjects, animal welfare, conflicts of interest, and biosafety; a UK institution commonly adds data-protection assessment and export control; a corporate research lab may run a narrower set. What does not vary is the frame itself: the system exists to operate the institution's compliance program across its obligation domains, not to run any single workflow.

**Compliance submissions.** The unit of record is a researcher-initiated submission: a protocol application (human, animal, biosafety), a conflict-of-interest disclosure, an export-control project registration or technology control plan, a data-protection assessment, a determination request. Each submission is an individually addressable record carrying its researcher(s), its research context, its domain-specific content, and its own status. Submissions are the objects every workflow advances.

**The review-and-determination loop.** A submission enters a configured review path: administrative intake and triage, then evaluation by reviewers or a committee against the domain's rules, then a recorded determination — approval, approval with conditions, deferral for more information, denial, or a determination that no full review is required (for example, that an activity does not constitute human-subjects research, or that a disclosure raises no conflict). The determination is the system's central output: it is what authorizes the research activity to proceed, and it is always recorded with its rationale and its reviewers.

**The audit-ready compliance record.** Submissions, determinations, conditions, events, training, and correspondence are retained as the institution's evidence of compliance. The record is additive and attributable — review histories, versions, and decisions stay inspectable — because its consumers are external oversight parties (regulators, auditors, accreditors) as well as internal leadership. The system is not just a review tool; it is where the institution proves, after the fact, that its research was properly reviewed and managed.

### What Mature Products Add

These capabilities appear across the researched products and make the program practical, but a system remains a research compliance system without any single one of them:

- **Committee machinery** — meeting management, agendas, minutes, reviewer assignment, review checklists, captured reviewer comments, digital signatures. The dominant realization of review, though determinations can also be made administratively.
- **Configurable forms and workflows** — form builders and workflow designers that let each institution encode its own processes and adapt them as regulations change. This is how the same product serves different institutions and regimes.
- **A shared compliance substrate** — person records, training and certification records, and external-entity (organization) records reused across all domains, plus links from compliance records into the research context: proposals, awards, contracts, and the institution's other protocols for the same project.
- **Training tracking** — researcher training status held in the system, often fed from external training providers, and commonly checked as part of review.
- **Post-approval lifecycle** — renewals and continuing review that keep approvals alive, amendments and modifications to approved records, reportable events and incidents filed during the life of the research, and closeout when the work ends.
- **Reporting and oversight surfaces** — dashboards, activity views, key measures such as time-to-approval, scheduled reports, and role-based access appropriate to sensitive content such as personal financial disclosures.

### One Structure, Many Implementations

The core model is conceptual. Implementations vary:

```text
Concept:            Compliance domain
Implementations:    separately configured modules over one platform, or
                    one suite with per-domain apps; domain set institution-specific

Concept:            Compliance submission
Implementations:    protocol application, COI/COC disclosure, export-control
                    project + technology control plan, DPIA, determination request

Concept:            Reviewer / deciding body
Implementations:    convened committee with meetings and minutes, assigned
                    individual reviewers, administrative determination by staff

Concept:            Retained compliance record
Implementations:    audit trails and review histories, version control,
                    document storage, scheduled and ad-hoc reporting
```

## How It Works

### Submit

```text
Researcher opens a submission form for the relevant domain
→ guided smart forms capture the required content
  (study design, personnel, funding links, disclosures of interests…)
→ the system checks completeness and routes the submission
→ status becomes visible to the researcher and the compliance office
```

Submissions are created by the researchers themselves, not by the compliance office. Guided forms with conditional questions and built-in help exist because each domain's rules are complex and institution-specific.

### Review and determine

```text
Compliance staff triage the submission
→ routed through the configured review path
  (administrative pre-review, assigned reviewers, or full committee)
→ reviewers evaluate against the domain's rules, record comments and rationale
→ committee convenes (agendas, discussion, minutes) or reviewers decide individually
→ determination recorded: approved / approved with conditions / deferred / denied
   / no-full-review-required
→ determination letter issued to the researcher
```

The loop is the heart of the system. Multiple review levels and ancillary reviews (other offices that must also look at a submission) are common at larger institutions; some determinations — exempt-class and no-conflict outcomes — resolve without full committee review.

### Live under the determination

```text
Approved research proceeds under recorded conditions
→ amendments/modifications submitted as the study changes
→ renewals filed before approvals lapse (continuing review)
→ reportable events / incidents filed when something happens
→ management plans (conflicts) and control plans (export) monitored over time
→ closeout when the research ends
```

An approval is not a one-time event. The approved record stays live in the system: it must be renewed, amended, monitored, and eventually closed. Events that occur during the research are filed back into the same record.

### Maintain the program

```text
Compliance office works the queue across all domains
→ training status tracked and checked per person
→ dashboards surface pending work, aging submissions, lapsing approvals
→ records retained with review histories and versions
→ reports prepared for regulators, auditors, accreditors, leadership
```

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Researcher portal

The researcher's entry surface.

- lists the researcher's own submissions across domains with status
- primary actions: start a new submission, respond to reviewer questions, file an amendment or renewal, report an event, view determination letters

### Submission detail / protocol record

The working surface for one submission.

- full content of the submission, its review history, its versions, attached documents, linked research context (funding, related protocols, disclosures)
- primary actions: edit (in draft states), submit, respond, view determination

### Reviewer / committee workspace

The reviewer's evaluation surface.

- assigned submissions with review checklists and captured comments
- committee surfaces: meeting agendas, minutes, member view of the full submission
- primary actions: record evaluation and rationale, recommend or vote, sign

### Administrator console

The compliance office's operating surface.

- work queues across domains, triage and routing controls, correspondence and determination letters, renewal and event tracking
- configuration surfaces: form builders, workflow designers, role management
- primary actions: triage, route, correspond, issue determinations, configure

### Oversight / reporting surface

The leadership and audit-facing surface.

- cross-domain activity dashboards, key measures (e.g., time-to-approval), scheduled and ad-hoc reports, retained records for inspection
- primary actions: monitor, report, export evidence

## Important Rules / Behaviors

### The determination gates the research

The recorded determination is the institution's authorization. Research activity in a regulated domain proceeds under an approved record and its conditions; the system's value is that this authorization is explicit, attributable, and retrievable.

### Approvals lapse and must be renewed

Approved records carry time-bounded approvals. Renewal (continuing review) keeps the record alive; a lapsed approval stops authorizing the research. Renewal-date monitoring is a standard administrator behavior.

### Changes go back through the system

Material changes to approved research are filed as amendments and re-reviewed; events that occur during the research are filed as reportable events or incidents against the same record. The record accumulates the study's compliance history rather than being overwritten.

### Conflicts are managed, not just disclosed

A disclosed conflict typically resolves into a management plan — a recorded set of conditions referenced against the disclosure and the affected research, and monitored over time. Disclosure alone does not close the loop.

### Training status is checked, not assumed

Person-level training and certification records are held in the shared substrate and commonly checked during review; out-of-date training is a visible, actionable state.

### Access is role-gated and the record is attributable

Compliance content includes sensitive personal financial disclosures and participant-risk material; access is role-based. Records are additive and attributable — review histories, versions, and decisions remain inspectable — because oversight parties consume them after the fact.

### Regulations change; the configuration follows

Because obligations are set by external regimes, mature products hold the rules in configurable forms and workflows so institutions can adapt their processes when regulations or policies change, without rebuilding the system.

## Variants

- **By institutional type** — research-intensive universities (high submission volume, multi-level review), academic medical centers and hospitals (clinical research overlap), nonprofit and government research organizations, corporate research.
- **By jurisdiction and regime** — US federal-grantee regime (human-subjects rules, financial-conflict rules, animal-welfare oversight, accreditation and inspection machinery); UK/EU regime (data-protection assessment, export control and "trusted research" concerns); national research organizations with their own review structures.
- **By packaging** — standalone compliance suites vs compliance modules inside a wider research-administration platform; the same structures appear in both.
- **By scale tier** — enterprise deployments add multi-level and ancillary reviews, multi-site studies, single-IRB-style reliance arrangements, and regulated-record support; smaller institutions run simpler single-path reviews.
- **By domain set** — which obligation domains the institution runs; the program frame accommodates different sets.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| IRB / Research Ethics Management | single-domain subset | runs only the human-subjects protocol lifecycle; here it appears as one domain inside the multi-domain program; suite products bundle it as a module |
| Animal Research Ethics / IACUC Platform | single-domain subset | same pattern for animal-use protocols |
| Research Administration Platform | adjacent, deeply integrated | centers on the funding lifecycle (proposals, awards); this Type centers on conduct obligations (protocols, disclosures, determinations); products link data both ways and are often sold as one suite |
| Research Grant Management | adjacent | grant lifecycle and sponsor terms vs the institution's compliance program over research conduct |
| Research Information Management / CRIS | adjacent | records research activity and outputs vs recording compliance determinations and evidence |
| Compliance Management Platform | neighboring generic Type | generic corporate compliance (policies, controls, audits across business domains) vs researcher-facing submission/review machinery over research-specific regulatory regimes |
| Governance, Risk & Compliance Platform | neighboring generic Type | enterprise risk and control frameworks vs operation of research protocol and disclosure lifecycles |
| Research Data Management | adjacent | data stewardship and planning vs compliance determinations; data-protection assessment modules bridge the two |
| EHS / Lab Safety platforms | adjacent | facility and lab safety operations (chemical inventory, inspections) vs the research compliance program; biosafety protocol review sits on the compliance side |
| Life Sciences QMS / CTMS | different regulated context | quality systems and clinical-trial operations for regulated industry vs institutional research compliance |

The most important boundary is with the single-domain ethics-review Types: those leaves own one domain's protocol-review machinery; this leaf owns the institution's multi-domain compliance program. The second most important is with research administration: money and funding versus obligations and determinations — integrated in practice, distinct in center of gravity.

## Representative Products

- Cayuse (Compliance Management Suite)
- Kuali Research (compliance modules: Conflict Management, Human/Animal Ethics Review, Biosafety Review, Export Control)
- InfoEd Global (Research Compliance suite)
- Infonetica (Ethics RM / Research Flow)

These were the researched sample: two US suite vendors, one modular higher-ed platform, one UK/international platform — chosen for market representation, documentation quality, different packaging philosophies, and different regulatory regimes.

## Sources

Research date: **2026-09-09**

- Cayuse — Compliance Management: https://www.cayuse.com/products/compliance/
- Cayuse — Risk & Compliance Suite: https://www.cayuse.com/compliance-management/risk-and-compliance-suite/
- Kuali — Research Administration & Compliance: https://www.kuali.co/
- Kuali — Conflict Management: https://www.kuali.co/products/conflict-management
- Kuali — Human Ethics Review: https://www.kuali.co/products/human-ethics-review
- Kuali — Export Control: https://www.kuali.co/products/export-control
- InfoEd Global — Research Compliance: https://www.infoedglobal.com/products/research-compliance/
- Infonetica — platform overview: https://www.infonetica.net/
- Infonetica — Ethics RM: https://www.infonetica.net/solutions/ethics-rm

> Sourcing limitation: evidence is product-page and module-page level. Vendor help-center-level operational documentation (exact form fields, state names, deadlines) was not reachable in this pass, so this document deliberately states no precise numeric limits, deadlines, or lifecycle state names. Two candidate products (a major US compliance suite and a mid-market platform) could not be reached (unreachable pages); the US enterprise pole is represented by one sampled vendor. Detailed observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
