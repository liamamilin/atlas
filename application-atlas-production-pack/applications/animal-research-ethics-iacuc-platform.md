# Animal Research Ethics / IACUC Platform

## Overview

An **Animal Research Ethics / IACUC Platform** is the system an institution uses to manage the ethical review and continuing oversight of research, teaching, or testing that involves animals. Investigators describe a proposed use of animals in a structured **protocol**; the institution's animal care and use oversight body — in the United States the IACUC, with differently named counterparts in other regions — reviews that protocol through a recorded workflow; the recorded approval serves as the institution's authorization for the described animal work; and the approved protocol then remains under active oversight: modifications are reviewed before implementation, review recurs on a defined cycle, and reportable events can be attached at any time.

The defining core is small:

```text
Protocol (investigator-authored record of proposed animal use)
  → Committee review (structured, recorded)
  → Recorded decision and approval status (the institutional authorization)
  → Ongoing oversight of the approved protocol
```

What the platform is *not* is equally defining. It does not manage the animals themselves — housing, census, husbandry, ordering, billing — which is the territory of animal facility / vivarium management systems (though the two integrate). It is also not the human-subjects side: the same review machinery applied to research with human participants is the IRB platform Type, which ships as a sibling product in the same market.

## Users & Context

**Primary users:**

- **Principal investigator (PI) and research staff** — author and submit protocols describing the animal work (species, procedures, rationale, welfare measures), respond to reviewer questions, request modifications to approved protocols, add personnel to the study team, file reportable events, and complete recurring reviews.
- **Committee members / reviewers** — read assigned protocols, comment on specific content, check submissions against review checklists, and record recommendations or votes.
- **Attending veterinarian / veterinary staff** — review the animal-welfare aspects of protocols (procedures, anesthesia, analgesia, endpoints) and often act as a required screening step before or during review.

**Operational users:**

- **IACUC administrator / coordinator** — the operational hub: triages submissions, routes them into the right review pathway, manages agendas and committee meetings, tracks renewals and expirations, monitors compliance status, and prepares reports.
- **Compliance office / institution** — owns the configuration (forms, workflows, training requirements, roles) and consumes the audit trail and institutional reports.

The context is institutions that use animals in science: universities, academic medical centers, research institutes, and pharmaceutical or biotech laboratories. The regulatory framing differs by country, but the underlying loop — propose, review, approve, keep watching — is the same; modern products support region-specific forms and workflows in one system.

## Core Model

### The Defining Core

Four properties. Remove any one and the product stops being recognizable as this Type:

- **Protocol record.** The central object: an investigator-authored, institution-owned structured record describing a proposed or ongoing use of animals — typically the species and numbers, the scientific rationale, the procedures, the personnel who will work with the animals, and how welfare and pain or distress are addressed. The protocol is not a static document; it is a living record whose content the institution configures and whose state the system manages.
- **Committee review process.** The protocol moves through a structured, recorded review by the oversight body. Review is a workflow in the system sense: triage, routing into a review pathway, reviewer assignment, comments and questions, revisions, and a recorded outcome. Institutions differ in how many pathways exist and who must review what; the platform models these pathways as configurable workflows rather than hard-coded steps.
- **Recorded decision and approval status.** Review outcomes are recorded and become the protocol's status — approved, revisions required, not approved, or equivalent labels that vary by institution. An approved status is not just bookkeeping: it is the institutional authorization that the described animal work may proceed. This is what makes the platform a *governance* system rather than a form tool.
- **Ongoing oversight of the approved protocol.** Approval is not an endpoint. The approved protocol stays under active management: material changes must be submitted and reviewed before implementation, review recurs on the institution's cycle, and reportable events (adverse or unexpected events affecting animals) can be filed against the protocol at any time. The platform's value is largely in policing the gap between what was approved and what is actually happening.

### Standard Capabilities

Mature products commonly add the following around the defining core. They are expected in the market but do not define the Type:

- **Configurable protocol forms** — institution-defined sections capturing animal care, housing, handling, and experimental procedures, with conditional visibility so authors only see content relevant to their species and procedures. Some products offer pre-approved procedure libraries that authors can reference instead of describing techniques from scratch.
- **Review machinery** — triage queues, reviewer assignment, reviewer checklists, version comparison, tracked changes, and in-line comments so reviewers can see exactly what changed between protocol versions and comment at the point of concern.
- **Committee and meeting management** — agenda building, meeting support, and documentation of what the committee considered and decided.
- **Amendments and modifications** — change requests processed through a proportionate review loop rather than a full resubmission.
- **Recurring review / renewal** — the periodic review of continuing protocols, with automatic reminders and notifications so approvals do not silently lapse; some institutions use de novo review for renewals.
- **Reportable events** — structured capture and routing of adverse or unexpected events tied to a specific protocol.
- **Facility inspections** — tracking of animal facility and lab inspections and their findings, feeding the oversight program's quality-assurance record. (Common, though itemized explicitly only by some products.)
- **Personnel and training tracking** — who is qualified to work on which protocol; configurable training requirements at the personnel, species, activity, or procedure level, checked while the protocol is being authored. Unqualified personnel surface before submission rather than at audit time.
- **Status dashboards** — for the PI (what is pending on my protocols) and for administrators (what is aging, expiring, or non-compliant across the institution).
- **Institutional reporting** — audit-ready records and reports supporting oversight obligations and accreditation processes, such as materials for regulator site visits, assurance filings, and accreditation program descriptions.
- **Integration points** — to the human-ethics sibling product, to hazard/biosafety committees for cross-committee approvals (protocols involving hazardous agents may need both committees), to sponsored-projects records for protocol–grant congruency checks, and to vivarium or animal-ordering systems where an approved protocol is the prerequisite for obtaining animals.

### One Structure, Many Implementations

```text
Concept:        Protocol
Implementations: institution-built forms, vendor templates, per-species/per-activity templates

Concept:        Oversight body
Implementations: institutional IACUC, regional committees under other names, multi-site program structures

Concept:        Review pathway
Implementations: full-committee review, expedited or designated-member review, veterinary screening steps — configured per institution

Concept:        Approval status
Implementations: product-specific status vocabularies (approved / revisions required / not approved / expired / closed)

Concept:        Recurring review
Implementations: annual review, de novo renewal, continuing review on the institution's regulatory cycle
```

A reader who has only seen one product should be able to recognize any other from this structure: the vocabulary and pathway names change, the loop does not.

## How It Works

### Author and submit a protocol

```text
PI starts a protocol in the institution's configured form
→ fills sections (rationale, species, procedures, welfare measures)
→ adds study-team personnel (system checks qualifications/training)
→ attaches supporting documents
→ submits → record enters the review queue
```

Guided navigation and built-in help are common authoring aids; the system enforces the institution's content requirements structurally (required sections, conditional questions), not by email reminders.

### Review and decide

```text
Administrator triages the submission
→ administrative completeness / veterinary or scientific screening
→ routed into a review pathway (full committee or a designated pathway)
→ assigned reviewers comment and check against checklists
→ PI answers questions; revised versions are compared against the original
→ committee considers and records an outcome
→ status updated; participants notified
```

The signature review experience is version-aware: reviewers see the current content, the change history, and reviewer comments in context, so a revision cycle is a comparison, not a re-read.

### Maintain the approval

```text
Approved protocol in force
→ material change needed → amendment submitted → (proportionate) review → recorded outcome
→ recurring review falls due → reminders fire → PI completes review → committee records outcome
→ adverse event occurs → reportable event filed against the protocol → reviewed and dispositioned
→ work ends → protocol closed out
```

This maintenance loop is where the platform spends most of its life: at a large institution, the population of protocols in amendments, renewals, and events dwarfs the new-submission queue.

### Support the committee itself

```text
Administrator assembles an agenda from items in review
→ committee meets (platform supports agenda and meeting records)
→ decisions recorded back onto each item
```

### Report upward

```text
System-of-record data
→ status/compliance dashboards for administrators
→ filtered reports for regulators, assurances, and accreditation program descriptions
→ audit trail of every action on every protocol
```

### Capability tiers

**Defining core** — protocol record; committee review workflow; recorded decision/approval status; ongoing oversight (modifications, recurring review, reportable events).

**Common mature structure** — configurable forms; version comparison and review tooling; committee/meeting management; renewal automation; training/qualification tracking; status dashboards; institutional reporting; role-based access.

**Common variants / optional** — facility inspection tracking; animal ordering and transfer extensions; vivarium operations integration; cross-committee (biosafety/hazard) approvals; protocol–grant congruency review; region-specific form packs; pre-approved procedure libraries.

## Interfaces

### PI dashboard / protocol workspace

- **Purpose:** the investigator's home for their own protocols.
- **Typical information:** protocol list with status, items awaiting my action, upcoming renewals, recent decisions and comments.
- **Primary actions:** start a protocol or amendment, respond to reviewer questions, file a reportable event, view approval letters and history.

### Protocol form

- **Purpose:** author the structured record of proposed animal use.
- **Typical information:** institution-configured sections (rationale, species, procedures, personnel, welfare measures), required-field and conditional-visibility logic, attachments.
- **Primary actions:** edit sections, add personnel (with qualification checks), upload documents, submit.

### Review workspace

- **Purpose:** let reviewers and administrators work a submission to a decision.
- **Typical information:** current version, change history, side-by-side version comparison, in-line comments, reviewer checklists, routing state.
- **Primary actions:** assign reviewers, comment, request revisions, record votes/recommendations, record the outcome.

### Committee agenda & meetings

- **Purpose:** run the committee's meeting cycle.
- **Typical information:** agenda items by protocol, supporting materials, prior meeting records.
- **Primary actions:** build agenda, mark items reviewed, record decisions back onto protocols.

### Administrative console

- **Purpose:** configure and operate the program.
- **Typical information:** form and workflow definitions, training requirement rules, user roles and groups, notification rules.
- **Primary actions:** configure forms/workflows, manage users and roles, adjust training requirements, tune renewal and notification rules.

### Compliance / monitoring dashboards

- **Purpose:** institution-level visibility and reporting.
- **Typical information:** protocol population by status, expirations and upcoming renewals, inspection findings, event reports, training gaps.
- **Primary actions:** filter, drill into protocols, generate regulator/accreditation reports.

## Important Rules / Behaviors

- **The approved protocol is the precondition for animal work.** The platform's central control: animal procurement, housing, and use are expected to trace to a protocol whose approval is current. This is also why integration with animal-ordering or vivarium systems is a common (optional) extension — the approved protocol functions as the permit those operations check against.
- **Material changes require review before implementation.** Amendments flow through a review loop proportionate to their scope; the system keeps the approved version and the proposed version distinct until a decision is recorded.
- **Approval has a recurring cycle.** Approvals are time-bounded by the institution's regulatory framework; the platform automates reminders and tracks renewal outcomes. Exact cadences are institution- and regulator-defined, not product constants.
- **Personnel eligibility is enforced against the protocol.** Study-team members are checked for training/qualification relevant to the species, activities, and procedures named in the protocol; gaps surface during authorship rather than at audit.
- **Cross-committee coupling.** Protocols involving hazardous agents or recombinant DNA may require approvals from other institutional committees; mature products route or link these so neither approval silently proceeds alone.
- **Reportable events attach to specific protocols** and are tracked to disposition, supporting the institution's obligation to notify oversight or accreditation bodies of significant events.
- **Status vocabularies vary.** Labels such as approved, revisions required, not approved, expired, or closed are conceptual states; exact names and the rules for moving between them are configured per institution.
- **Everything is attributed.** Because the record is the institution's compliance evidence, actions on a protocol carry identity and timestamps, producing an audit trail that reporting draws on.

## Variants

- **Suite module vs standalone.** In the researched sample, both products are modules inside broader research administration and compliance suites (alongside human ethics, biosafety, conflict-of-interest, and sponsored programs). Standalone and institution-built systems exist, particularly at large programs.
- **Regulatory regime.** US deployments carry IACUC-specific artifacts (USDA, PHS Assurance, AAALAC accreditation reporting); other regions configure the same machinery around their own frameworks and committee structures. Global products expose region-specific forms and workflows rather than a single regime.
- **Program scale.** Single-committee institutions vs multi-site, multi-committee programs with shared configuration and cross-campus reporting.
- **Depth of animal-operations coupling.** From no coupling, to data-sharing integrations with vivarium operations and veterinary care, to full animal ordering/transfer workflows built as extensions of the same platform.
- **Configuration philosophy.** Pre-built, deep IACUC workflows that institutions adapt, vs form-builder/workflow-designer platforms where the institution assembles its process from primitives.
- **Maturity spectrum.** The same defining loop predates these products; institutions moving from paper or homegrown databases adopt the platform as the digitization of a process they already ran. Any definition must therefore hold for paper-era and regional equivalents, not just modern suites.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| IRB / Research Ethics Management | sibling | same review-platform shape applied to research with human participants; different review object, protections, and regulatory artifacts — vendors ship them as sibling products |
| Research Animal Facility Management | adjacent, heavily integrated | manages the animals themselves (housing, census, husbandry, vet care, ordering, billing); remove the committee review loop and this Type becomes facility management — that is the boundary |
| Research Compliance Management | broader container | multi-committee compliance programs (human ethics, biosafety, COI, export control) that typically include this Type as one member |
| Research Administration / Grant Management | adjacent | sponsored-projects and award lifecycle; the touchpoint is protocol–grant congruency checking, not animal-use review |
| Accreditation / Certification Management | supportive overlap | institution-level accreditation cycles (e.g., program accreditation for animal care and use) consume reports and evidence from this platform but are not organized around the protocol |

The two boundaries that matter most in practice: **against IRB platforms** the discriminator is the review object (animal use vs human participants); **against animal facility management** the discriminator is the central object (the authorization to use animals vs the animals in care).

## Representative Products

- **Cayuse — Animal Oversight** (compliance module of the Cayuse research suite; higher education, healthcare, life sciences)
- **Kuali — Animal Ethics Review** (compliance module of Kuali Research; higher education)

Both sampled products are suite modules from vendors serving higher education and research institutions; the wider market also includes legacy and standalone systems that were not directly verifiable during research (see Sources).

## Sources

Research date: **2026-09-06**

- Cayuse — Animal Oversight product page: https://www.cayuse.com/compliance-management/animal-oversight/
- Cayuse — corporate site and suite structure: https://www.cayuse.com/
- Kuali — Animal Ethics Review product page: https://www.kuali.co/products/animal-ethics-review
- Kuali Help Center — "What is Kuali Research?" (suite and module definitions): https://kuali.zendesk.com/hc/en-us/articles/27090467314075-What-is-Kuali-Research
- Kuali Help Center — Research category: https://kuali.zendesk.com/hc/en-us/categories/23343502783771
- AAALAC International — accreditation process, Program Description, and adverse-event reporting context: https://www.aaalac.org/

> Sourcing limitation: vendor support portals with step-by-step operational manuals were not accessible this pass (login-gated support site; several other vendors in this market unreachable). Findings rest on official product pages, the Kuali help-center suite definition, and one accreditor's public materials. Operational specifics that were not directly observed — exact protocol section taxonomies, review pathway names, voting mechanics, renewal cadences, numeric limits — are intentionally not stated in this document. Product-by-product observations and evidence calibration are recorded in the paired Research Notes.
