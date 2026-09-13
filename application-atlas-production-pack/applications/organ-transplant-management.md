# Organ Transplant Management

## Overview

An **Organ Transplant Management** application is the hospital transplant program's system of record for its transplant candidates and recipients — the software in which a patient is carried from referral through evaluation, held on the program's waiting list, matched against organ offers, transplanted, and then followed for the life of the transplanted organ.

Organ transplantation is not ordinary specialty care. A transplant program operates inside a regulated allocation regime: organs are scarce, donation is donor-driven rather than demand-driven, and allocation is executed by a designated national or regional allocation system under written policy. The program's software must therefore do two things a general clinical system does not: maintain the program's waiting-list position toward that external allocation machinery, and manage the time-critical accept/decline decisions when an organ is offered. Around that core, it manages a patient lifecycle unlike any other — a candidacy that must be earned through an evaluation workup, a waiting period of unknown length, a single definitive surgical event, and a recipient who then requires lifelong immunosuppression and structured surveillance of the transplanted organ (the graft).

The defining core is deliberately narrow:

```text
Transplant candidate of record
└── Evaluation workup → selection / listing decision
    └── Waiting list (allocation context) → status and waiting time
        └── Organ offer → accept / decline decision
            └── Transplant event (donor organ bound to candidate)
                └── Graft and recipient follow-up (lifelong, re-listing on failure)
```

What is *not* this Type: the national allocation platform that executes matching across all centers (a separate system run by the allocation authority), and donor-side procurement software (the organ-acquisition organization's own record world). Both interlock with this Type but are not it.

## Users & Context

The software serves the multidisciplinary team of a hospital transplant program (kidney, liver, heart, lung, and other organ programs), typically coordinated by nurse coordinators who work in it daily.

**Primary users:**

- **Pre-transplant transplant coordinator** — receives referrals, drives the evaluation workup to completion, presents candidates to the selection process, and manages waiting-list status and updates for the program's listed patients.
- **Post-transplant transplant coordinator** — manages the recipient's follow-up schedule, tracks graft-function results and complications, and coordinates surveillance visits and labs.
- **Transplant surgeon and transplant physician (e.g., nephrologist / hepatologist / cardiologist by organ)** — make the clinical decisions the system records: candidacy and listing decisions, organ-offer accept/decline decisions, and changes to the recipient's ongoing management.

**Secondary users:**

- **Program administrator / quality manager** — owns compliance with the allocation regime and the national registry: data completeness, report submission, quality metrics, audit trails.
- **Financial coordinator** — evaluates insurance coverage and financial clearance as part of candidacy (in markets where coverage determines whether a candidacy can proceed).
- **Social worker, dietitian, and other consult roles** — contribute required evaluation elements and post-transplant care inputs.
- **Data coordinators / registry staff** — maintain the accuracy of waiting-list records and outcome data that the program is accountable for.

The context is a clinic-and-office team around a surgical service. Offer decisions happen at any hour, because donor organs arrive on the donor's schedule, not the program's; the software is therefore used for both scheduled clinical work (evaluations, follow-up visits) and urgent, interrupt-driven work (offer response).

## Core Model

### The Defining Core

Four structures together make the Type what it is. Each is load-bearing: remove any one and the software collapses into a neighboring kind of tool.

**1. The transplant candidate of record.**

A patient referred to the program becomes a managed candidacy — not just a chart. The candidacy record carries the referral, the organ-specific evaluation workup (clinical screening, testing, specialist consults — e.g., infection, cardiovascular, malignancy-risk screening, because post-transplant immunosuppression raises the stakes of each), and the explicit outcome of the selection process: an acceptance decision to list, a deferral with conditions to resolve, or a decline. The candidate is individually addressable, attributed, and status-bearing from the first day.

**2. The waiting list in its allocation context.**

Candidates who are accepted are held as listed waiting patients. The waiting list is not a simple queue: each entry carries the attributes that allocation depends on (blood type, size, and — by organ and jurisdiction — tissue-typing and sensitization attributes), a waiting state that changes as the patient's situation changes (active, temporarily inactive, updated, removed, reinstated), and waiting time that only accrues under the regime's rules. Critically, the program is responsible for maintaining this list as its interface to the external allocation system; in regulated deceased-donor regimes the hospital's duty to keep its waiting candidates correctly registered is a compliance obligation, not an internal convenience.

**3. The organ-offer loop.**

When a donor organ becomes available, the allocation system matches it against waiting candidates under written policy (medical urgency, donor–recipient match criteria, and jurisdiction-defined priorities such as proximity). The program receives the resulting offer for one of its listed patients and must decide — quickly, because organ viability is measured in hours — whether to accept or decline, recording the decision and its reason. An accepted offer converts into the **transplant event**: the record that binds a specific donor organ (with its donor data, handed over from the acquisition side) to a specific candidate, who now becomes a recipient. The offer loop is the defining interaction of the Type: it is where the program's care management meets the external allocation machinery, and it is what distinguishes transplant software from every other clinic-management software.

**4. Graft-and-patient continuity after the transplant event.**

The transplant event does not close the record. The recipient and the graft remain under the program's management: scheduled surveillance visits and labs, immunosuppression regimen management (a lifelong treatment while the graft functions, with its own monitoring demands), rejection episodes and infections, metabolic and malignancy-related complications, and graft-function outcomes. If the graft fails, the patient re-enters the candidacy world — dialysis or device support resumes, and re-listing is considered. The Type's scope is the whole continuum, which is also what the regulatory frame requires: outcome reporting follows the recipient for years.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical; they are not what defines it.

- **Referral intake and triage** — capturing referrals, their sources, and their progress toward an evaluation decision.
- **Evaluation workup checklists** — organ-program-specific templates of required tests and consults, with outstanding-item tracking so candidacy workups can be driven to completion.
- **Selection-committee documentation** — recording the multidisciplinary meeting outcome per candidate.
- **Offer-management tooling** — offer notification and tracking, decline-reason capture, and a searchable history of offers received, so programs can audit and refine their acceptance criteria. Many programs configure center-specific criteria for which offers they will consider (a heart program's tolerance for donor risk factors differs from another's, and the software makes the criteria explicit).
- **Post-transplant schedules and flowsheets** — visit and lab schedules by post-transplant phase, graft-function trend views, complication and rejection-episode records, immunosuppression regimen and level tracking.
- **Registry and compliance reporting** — producing the data submissions the allocation authority and regulator require, quality-metric views (for example delayed graft function and primary non-function rates are standard quality indicators in kidney programs), and audit trails supporting the regime's traceability requirements.
- **Financial clearance workflow** — insurance evaluation steps embedded in the candidacy pipeline where the market requires it.
- **Living-donor pathway** — managing the living donor's own evaluation and the linkage between a living donor and their intended recipient (most prominent in kidney and liver programs; depth varies by product and market).
- **Interfacing** — integration with the hospital EHR, laboratory systems, and (directly or via staff workflow) the national allocation system.

### One Structure, Many Implementations

The core is written conceptually; implementations differ by regime and product form.

```text
Concept:  Waiting list with allocation context
Forms:    registration maintained in a national allocation system,
          mirrored/synced into the program's software, or maintained
          by the program and exchanged with it — depends on the regime

Concept:  Organ offer and decision
Forms:    offer received through the allocation platform's own interface
          and then documented in program software; or delivered into the
          program software directly — depends on the product and regime

Concept:  Transplant event
Forms:    a dedicated lifecycle record in the transplant system, or an
          EHR surgical encounter referenced from it
```

A reader who has only seen one regime's tooling should still be able to recognize the others from the concepts.

## How It Works

### Carry a patient from referral to listing

```text
Referral received
→ candidacy opened; referral details and indication recorded
→ evaluation workup started (program checklist per organ)
→ tests and consults completed and tracked to closure
→ multidisciplinary selection decision recorded
→ accepted: candidate registered on the waiting list
   deferred: conditions recorded, candidacy held
   declined: rationale recorded
```

The workup is long and itemized by design — screening classes exist because post-transplant immunosuppression changes the risk calculus for infection, malignancy, and cardiovascular disease. The software's job is to make the candidacy's completeness visible: what is done, what is outstanding, what blocks presentation.

### Maintain the waiting list

```text
Candidate listed with allocation attributes
→ waiting time accrues under regime rules
→ status changes as the clinical situation changes
   (activation, temporary inactivation, updates, removal, reinstatement)
→ list kept accurate as the program's interface to allocation
```

Waiting-list hygiene is a compliance duty. A stale or wrongly-active entry is not a data-quality nit; it misrepresents the program to the allocation system. Status changes are recorded with reasons and attribution.

### Respond to an organ offer

```text
Donor organ enters allocation; policy matching runs externally
→ offer arrives against one of the program's listed candidates
→ donor and organ data reviewed against the candidate's
   situation and the program's acceptance criteria
→ decision made by the responsible surgeon/physician:
   accept — or decline with recorded reason
→ accepted: transplant event created, binding
   donor organ → candidate (now recipient)
→ logistics and surgery follow; the decision trail is retained
```

This is the Type's interrupt-driven workflow: it happens at any hour, it is time-critical, and both the decision and its reasons must be captured — declined offers and their reasons are operational memory that programs use to refine criteria, and accepted offers start the accountable chain from donor to recipient.

### Follow the recipient and the graft

```text
Transplant event recorded
→ follow-up schedule established by post-transplant phase
→ surveillance visits and labs recorded; graft function trended
→ immunosuppression regimen managed and adjusted over time
→ complications recorded (rejection, infection, metabolic, malignancy risk)
→ outcomes reported to the registry per regime requirements
→ graft failure: patient returns to the candidacy world; re-listing considered
```

The follow-up loop is long-horizon and scheduled — the mirror image of the offer loop's urgency. Together they give the Type its two tempi: minutes-for-offers, years-for-outcomes.

## Interfaces

Conceptual surfaces; exact layouts vary by product.

### Candidate / workup view

The per-candidacy workspace.

- referral and indication, workup checklist with outstanding items, consult results, committee decision
- primary actions: advance workup items, record committee outcome, list / defer / decline the candidate

### Waiting list

The program's listed population at a glance.

- per-entry: allocation attributes, waiting state, waiting time, last update
- primary actions: change status with reason, update attributes, review due updates, register the patient with the allocation context

### Offer view

The time-critical decision surface.

- donor and organ data for the offered organ, the matched candidate's attributes, the program's acceptance criteria
- primary actions: record accept or decline with reason, document the decision trail

### Transplant event / recipient record

The record of the surgery and its binding.

- donor organ linked to recipient, operative context, post-transplant phase
- primary actions: record the event, open the follow-up schedule

### Follow-up view

The long-horizon management surface.

- visit and lab schedules, graft-function trends, complication and rejection-episode history, current immunosuppression regimen
- primary actions: record results, adjust regimen documentation, flag concerns, report outcomes

### Compliance / reporting surface

The program's accountability view.

- data-completeness status, required submissions, quality-metric views, audit trails for list changes and offer decisions
- primary actions: generate and submit registry data, review metrics, inspect change history

## Important Rules / Behaviors

### Allocation is executed by an external authority, not by the program

In regulated deceased-donor regimes, matching and allocation run in a designated allocation system under written policy, and allocation outside it is prohibited. The program's software records, prepares, and responds — it does not allocate. The program's authority is the accept/decline decision on offers addressed to its patients.

### The waiting list is a compliance object

The hospital is accountable for the correctness of its listed waiting candidates. Status changes, updates, and removals carry reasons and attribution; waiting time accrues under the regime's rules rather than by the program's preference. Software enforces the discipline: unexplained status changes are flagged, updates come due, and the list's history is auditable.

### Offer decisions are time-critical and must leave a trail

Organs remain viable for only a short span outside the donor, so offers cannot wait: the offer workflow is built for rapid, attributable decisions, and declined offers are recorded with reasons. The trail matters twice over: for the regime's traceability requirements and for the program's own criterion refinement.

### Listing is earned, and its loss is explicit

Candidacy begins at referral but listing happens only after the evaluation workup supports it. Conversely, a listed patient can be made temporarily inactive (their situation changed) or removed (they became unsuitable, transferred, or died) — with the state change and reason recorded. A candidacy record never silently disappears.

### Immunosuppression is a lifelong program commitment

While the graft functions, the recipient requires ongoing immunosuppression with its monitoring demands, and rejection remains a permanent vigilance item — the clinical reality that structures the post-transplant half of the software. Follow-up schedules and outcome reporting continue for years, which is why the recipient record outlives the surgical episode.

### Traceability runs the whole chain

From the donor data received with an offer, through the decision and the event, to follow-up outcomes, the regime expects an auditable chain. The software supports this with attributed, timestamped records across the continuum.

## Variants

- **By organ program** — kidney, liver, heart, lung, and multi-organ programs differ in workup content, allocation attributes, post-transplant surveillance patterns, and bridge therapies (e.g., mechanical circulatory support in heart programs). The model is the same; the content templates differ.
- **Standalone vs EHR-embedded** — dedicated transplant software (the traditional form) versus transplant modules realized inside the general EHR. The transplant-lifecycle objects are first-class either way; the difference is whether they live beside the EHR or inside it.
- **By regime** — national regimes differ in which system runs allocation, what the waiting-list registration duty looks like, and what reporting is required. Some regimes mandate a single national allocation system with automated matching and prohibit any allocation outside it; software in those markets is shaped around that interface.
- **Dual-side platforms** — some vendors serve both transplant programs and organ-acquisition organizations from one platform; the donor case world and the recipient world remain distinct record worlds that interlock at the offer/handover.
- **Living-donor depth** — programs with heavy living-donor activity (commonly kidney and liver) carry living-donor evaluation and paired-exchange participation; in others the deceased-donor loop dominates.
- **Patient-facing surfaces** — some products expose portal-style access for waitlisted and transplanted patients.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Electronic Health Record / EHR | containing or adjacent | the EHR holds the patient's general clinical record; this Type holds the transplant-lifecycle objects (candidacy, allocation-context listing, offers, graft) the EHR does not natively model; EHR-embedded transplant modules are a variant of this Type |
| Blood Bank Management | adjacent, same scarcity logic | blood bank runs an inventory model — pooled stored products dispensed on request; transplant has no inventory shelf — each unique organ arrives as a one-off policy-matched offer to a specific waiting patient |
| Referral Management | component-like adjacency | generic referral routing exists inside this Type as intake, but without candidacy/evaluation/listing semantics it is the referral Type, not transplant management |
| Patient Scheduling | component-like adjacency | visits and labs are scheduled here as one workflow among many; scheduling alone has no allocation, offer, or graft structures |
| Care Coordination Platform | adjacent | task and team coordination is generic; this Type's identity is the allocation-bound lifecycle, not coordination mechanics |
| Clinical Trial Management System | adjacent, different regulatory frame | both carry protocolized workflows and regulatory reporting; CTMS manages research subjects under study protocols, this Type manages care under an allocation regime |
| National organ allocation platform (UNet/COTRS class) | interconnecting counterpart — not this Type | operated by/for the allocation authority to execute policy matching across all centers and OPOs; the program software maintains its list toward it and responds to its offers |
| Donor-side / OPO software | interlocking adjacent — not this Type | the acquisition organization's donor case record world (identification, consent, maintenance, procurement, handover); interlocks with this Type at the offer and the organ handover |

The most important boundary is the allocation platform's. The regulation-cited pattern in mandated regimes is clean: the hospital maintains its waiting candidates; the authority's system matches and allocates; the program decides on the offers it receives. Software that only embeds that allocation interface is still this Type; the allocation platform itself never becomes this Type, because it holds no care-management objects.

## Representative Products

- Dedicated transplant-program management software (long-standing category; e.g., HCL Transplant Management)
- Platform vendors covering transplant centers and OPOs (e.g., Transplant Connect / iTransplant)
- EHR-embedded transplant modules (e.g., Epic Transplant)
- National allocation platforms, as the interconnecting counterpart (e.g., UNet in the US; COTRS in China)

## Sources

Research date: **2026-09-08**

Fetched and read this pass:

- 器官移植 — Baidu Baike ("科普中国" reviewed entry) — https://baike.baidu.com/item/%E5%99%A8%E5%AE%98%E7%A7%BB%E6%A4%8D — post-transplant follow-up and immunosuppression obligations; complication classes; regulatory context
- 中国人体器官分配与共享系统 (COTRS) — Baidu Baike — https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E4%BA%BA%E4%BD%93%E5%99%A8%E5%AE%98%E5%88%86%E9%85%8D%E4%B8%8E%E5%85%B1%E4%BA%AB%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B3%BB%E7%BB%9F — mandated allocation system; automated policy-based matching; urgency and match-degree ranking; traceability
- 器官获取组织 (OPO) — Baidu Baike (citing 《人体捐献器官获取与分配管理规定》) — https://baike.baidu.com/item/%E5%99%A8%E5%AE%98%E8%8E%B7%E5%8F%96%E7%BB%84%E7%BB%87 — donor-side duties; transplant hospital's waiting-list maintenance duty; prohibition of off-system allocation; handover and traceability; quality indicators
- 肾移植 — Baidu Baike ("科普中国" reviewed entry) — https://baike.baidu.com/item/%E8%82%BE%E7%A7%BB%E6%A4%8D — evaluation screening classes; lifelong immunosuppression; graft complications

> Sourcing limitation: official product documentation for the named vendors (unos.org, optn.transplant.hrsa.gov, epic.com, transplantconnect.com, hclsoft.com) and general references (Wikipedia, web archive) were not reachable from the research environment on 2026-09-08. Product names above are listed as market anchors by category position; no product-specific capabilities, numeric limits, status codes, or time windows are stated in this document, and none were filled in from unverified recall. Structural claims rest on the fetched regulatory and clinical sources plus cross-regime structural reasoning; details that would require vendor documentation remain in the Research Notes as open items.

Detailed evidence, product observations, cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
