# Litigation Management Platform

## Overview

A **Litigation Management Platform** is a party-side system of record for litigated disputes: it holds each litigated case as a persistent record — the dispute's adverse parties, their representation, the court or forum, and the case's current posture — and works that case through the operating machinery of a proceeding: litigation stages, calendared litigation events with limitation-period risk, and the case's discovery and evidence layer.

The defining core is deliberately small:

```text
Litigated Case of Record
└── Parties & representation (claimant, defendant, counsel, co-counsel, experts)
    └── Forum/court context and current procedural posture
        └── The proceeding worked as litigation
            ├── Litigation stages / phase plans
            ├── Litigation events + deadline & limitation-period calendaring
            └── Discovery & evidence layer (requests, productions, experts, key documents)
```

Everything else commonly associated with these products — settlement and demand tracking, litigation budgets and billing-guideline compliance, medical-damages material, client portals, portfolio dashboards, AI summaries — is widespread but not what makes the software a litigation management system. The same is true on the buyer side: budgets, panel-counsel management and spend control are the oversight layer that dispute-owning organizations (corporations, insurers, governments) add on top.

The Type is realized in two market poles: **litigation firms** running plaintiff or defense caseloads (the standalone product family), and **dispute owners** — in-house legal, insurers, government agencies — whose litigated-case oversight is usually packaged inside matter management, enterprise legal management suites, or claims systems.

## Users & Context

The primary users are the people who conduct or oversee lawsuits:

- **Litigation attorneys** — responsible for case strategy and outcome; they review posture, events, and the dispute's value record.
- **Litigation paralegals and case managers** — operate the machinery daily: entering events and deadlines, tracking discovery requests and responses, chasing records, maintaining the case file.
- **On the defense/firm side**: partners and litigation support managing a caseload for clients (including insurance-carrier clients whose billing guidelines bind each case).
- **On the dispute-owner side**: in-house counsel, litigation managers, claims and legal-operations staff who assign cases to defense counsel or staff counsel, control budgets against guidelines, and report exposure and outcomes to management or insurers.

Typical context: a personal-injury or insurance-defense firm working a high-volume concurrent caseload; a corporate legal department or insurer overseeing litigated claims across a panel of firms; a government agency defending or prosecuting litigation. The work environment is desk-and-calendar driven: the calendar of litigation events and deadlines is the operational heartbeat, while the case file (pleadings, discovery, evidence, correspondence) is the memory.

## Core Model

### The Litigated Case of Record

The central object is the **case**: a persistent, individually identified record of one dispute prosecuted or defended in a forum (court, arbitration, tribunal, administrative body). A case carries:

- **Parties and representation** — who claims, who is claimed against, who represents or defends each side, and the working roles around the case (co-counsel, expert witnesses, vendors). Adverse-party identity is structural: a case is a dispute *between* parties. Conflict checking against the organization's existing clients and adverse parties typically happens before a case is accepted.
- **Forum and court context** — the court or tribunal, venue, case number, judge where applicable, and the governing procedure that shapes deadlines.
- **Posture** — where the case currently stands in its life (pre-suit/claim stage, pleadings, discovery, motions, trial preparation, resolution) and who owns it.

### The Proceeding Worked as Litigation

What separates this Type from general matter tracking is that the application carries the proceeding's own operating machinery:

- **Litigation stages and phase plans** — configurable stage/phase models for how a case type progresses (in the plaintiff personal-injury pole: intake through investigation, treatment, litigation, and settlement; in defense work: matter plans templated per case type). Stage machinery drives task lists and visibility: each case shows its phase, next actions, and aging.
- **Litigation events and deadline calendaring** — filings, hearings, depositions, mediations, and conferences recorded as dated events; statutes of limitation and court-rule deadlines tied directly to the case record; increasingly computed by court-rules engines (trigger event plus jurisdictional rules produce the deadline set, accounting for holidays and service-method extensions) rather than hand-derived. Missed deadlines are treated as malpractice-level risk, so reminders, calendar sync, and attribution are structural.
- **The discovery and evidence layer** — the case's factual machinery: discovery requests and responses tracked to completion, productions monitored, expert witnesses managed, and the evidence material of the dispute organized on the case (in injury litigation: medical treatment, records and bill requests, chronologies of encounters; in general litigation: key documents and correspondence).

### What Mature Products Add

Nearly every product also carries the **dispute's value-and-resolution record**: the amounts at stake (claims, damages, exposure), demands and offers, negotiation history, and the settlement machinery that ends plaintiff-side cases (lien balances, costs, fee and disbursement calculations through final payout) or the resolution record that ends defense-side and buyer-side cases. On the funded pole, the same layer extends to litigation budgets, billing-guideline compliance, invoice review, and defense-counsel/panel management — and, where insurance funds the defense, to coverage and reserve context carried with the case.

Around the case, mature products accumulate the **case file** (documents, email, calls and texts, tasks, activity timeline), maintain **communication surfaces** (client portals and status updates on the plaintiff side; service-request intake and outside-counsel collaboration on the buyer side), and provide **portfolio reporting** (caseload health, stage distribution, spend versus budget, outcomes, counsel performance).

### One Structure, Many Implementations

The core is written conceptually. Products realize it differently:

```text
Concept:   Litigated case of record
Realizations:  case file, matter/case object, claim-litigation record inside a claims system

Concept:   Litigation stage machinery
Realizations:  case plans/phase templates, per-practice workflows, tab-per-phase case layouts

Concept:   Deadline machinery
Realizations:  built-in event calculators and litigation event plans; partner court-rules
               engines and docket-automation integrations; manual entry with reminders

Concept:   Dispute economics
Realizations:  settlement/demand ledgers with liens and disbursements (plaintiff pole);
               billing-guideline compliance, budgets and panel metrics (defense/buyer pole);
               dispute logs with claim amounts and coverage (in-house pole)
```

## How It Works

### Open the case

```text
Dispute arises (claim made, suit filed, or service request)
→ run conflict check against existing parties/clients
→ create the case record: parties, representation, forum, case type
→ attach the opening material (complaint, claim, referral, engagement)
→ set owner/team and the stage plan for this case type
```

On the firm side the case usually originates from an intake process; on the buyer side it originates from a claim, a served complaint, or a legal-service request, and may be assigned to staff counsel or to an outside firm.

### Work the proceeding

```text
Enter or compute deadlines (statutes, court rules, response dates)
→ events land on the calendar with reminders and owners
→ run discovery: track requests/responses, productions, depositions
→ assemble evidence: records, chronologies, experts, key documents
→ move the case through its stages; posture updates as the court acts
```

The calendar is the operational surface: each day's hearings, filings and deadlines belong to specific owners, and limitation periods are guarded as malpractice-level risk. When a court changes a date, dependent deadlines and tasks are recomputed or re-attributed.

### Manage the dispute's value

```text
Track what the case is worth (claim/exposure amounts, damages material)
→ record demands and offers; negotiation history accumulates
→ plaintiff pole: settlement machinery — liens, costs, fee and disbursement calculations to payout
→ defense/buyer pole: budget vs actual, billing-guideline compliance, invoice review
→ record the resolution (settlement, judgment, dismissal)
```

On the oversight pole this loop is also the control loop: assigning cases to the right firm or staff counsel, holding them to guidelines and budgets, and reporting outcomes and spend upward — including, in insurance-funded matters, the coverage and reserve context of each case.

### Oversee the portfolio

Across cases, the same records roll up: caseload by stage and age, spend versus budget, outcomes by court/case type/counsel, cycle times, and malpractice-risk views (approaching limitation periods, unowned deadlines). This portfolio layer is what makes the software *management* rather than a case notebook.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Case list / dashboard

The working entry surface: the caseload as filterable lists or boards — by stage, owner, court, client, carrier, or age — with at-a-glance posture, next event, and flagging of risk (approaching deadlines, stalled stages).

### Case detail (the case file)

The center of work: summary/posture header, parties and representation, the event and deadline calendar for this case, discovery tracker, documents and correspondence, tasks from the stage plan, and the case's activity timeline. Primary actions: update posture, add events/deadlines, log discovery activity, attach documents, assign tasks.

### Calendar / deadlines

Dated events and deadlines across the caseload, syncable to external calendars; per-event owner, reminder ladders, and limitation-period flags. Rules-engine computed deadlines appear alongside manually entered dates, with the source visible.

### Discovery / evidence surfaces

Trackers for requests and responses, productions, depositions and experts; in injury litigation, the medical layer (treatment, records and bills status, chronologies) that supports valuation and demand preparation.

### Settlement / negotiation ledger (plaintiff and resolution surfaces)

Demands, offers, negotiation history, liens, costs, and fee/disbursement calculations for cases moving to settlement; on defense and buyer deployments, the corresponding resolution record and (where applicable) budget-versus-actual on the case.

### Oversight / reporting (buyer pole and firm leadership)

Budgets and guideline compliance per case and in aggregate, counsel/panel performance, spend views, outcome reporting, and caseload-health dashboards.

## Important Rules / Behaviors

- **Deadlines are guarded as malpractice-level risk.** Limitation periods and court-rule deadlines attach to the case record with owners, reminders, and attribution; computation from jurisdictional rules is the mature implementation, manual entry the baseline.
- **Posture follows the forum.** The case's stage changes as the court or tribunal acts, not merely as internal work completes; the case record mirrors a proceeding conducted outside the system.
- **Adverse-party identity is structural.** Conflict screening against existing parties happens before acceptance; parties and representation are recorded on the case, not just in a contact list.
- **Economics couple to the case, not the timesheet alone.** Plaintiff-side value lives in the settlement/demand record; defense- and buyer-side control lives in budgets and guidelines applied per case; timekeeping and billing exist around these, not instead of them.
- **The case file is a durable record.** Documents, communications, events and history persist on the case across staff changes and handoffs — litigation is long-lived work that passes through many hands.
- **Roles and access matter most on the buyer side.** Assignment of cases to firms or staff counsel, visibility to outside collaborators, and audit trails for reporting to insurers or management are common governed behaviors.

## Variants

- **Firm-run litigation case management (plaintiff pole)** — personal-injury and mass-tort practices; deep medical/damages treatment, lien and settlement machinery, client communication; case value tracked per case.
- **Firm-run litigation case management (defense pole)** — insurance-defense and panel firms; carrier billing guidelines commonly applied per case, pre-bill compliance, transcript/deposition work, panel-performance reporting.
- **Dispute-owner oversight (buyer pole)** — corporate legal, insurers (including staff counsel), and government agencies; realized most often as litigation depth inside matter management or ELM suites (dispute records with proceedings, claim amounts, coverage; budgets; counsel assignment) and as litigation modules inside claims/RMIS systems.
- **Practice-area instantiations** — mass tort (case inventories across a tort), workers' compensation, commercial and employment litigation, government litigation; each tunes the stage model and the evidence layer.
- **Delivery variants** — standalone platforms, ELM-suite modules, claims-system modules, and (beside the software) managed litigation-management service programs that combine bill review, counsel management and outcome reporting as a service.
- **Geography** — the sampled market's deadline machinery is court-rule and statute-centric (US-shaped); in other jurisdictions the same structure appears with lighter procedural automation.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Legal Matter Management | closest sibling | the matter (any legal work) is the system of record with a file and progression; litigation machinery (stages, discovery, litigation events, dispute economics) is the addition that defines this Type. Litigated matters inside a matter system that grow proceeding-level depth are this Type's objects |
| Law Practice Management System | adjacent, frequently bundled | the client-anchored firm business system (intake→work→billing→trust); litigation-firm products carry firm operations but their litigation identity is the case/proceeding machinery |
| Legal Docket Management | complementary | the dated-obligation register (rules-engine deadline computation, dual-entry control) as a system of record; docketing appears here as one embedded capability |
| Court Case Management System | opposite side | the court's official record and authority vs the party's working record; court docket events feed the party's case |
| Insurance Claims Management | upstream container | the claim is the payer's system of record; litigated claims spawn cases worked here — claims systems commonly embed a litigation-management module |
| eDiscovery Platform | pipeline neighbor | processes the case's document corpora (holds, collection, review, production); this Type tracks discovery state but does not process corpora |
| Legal Hold Management | pipeline neighbor | preservation duties owed for a matter; triggered by the prospect of litigation, operated beside the case |
| Outside Counsel Management / Legal Spend Management | oversight layers | the firm relationship and the money records that this Type's buyer pole oversees; bundling is packaging, not merger |
| Case Law Research Platform | research neighbor | research over published law and external dockets vs management of the organization's own cases; litigation analytics is adjacent |
| Prosecutor / Public Defender Case Management | government neighbor | criminal courtroom-side caseload grammar (charging through disposition) vs civil/commercial litigation management |

## Representative Products

- Litify — litigation-firm solutions (plaintiff, insurance defense) and corporate ELM on one platform
- CasePeer (8am) — personal-injury litigation case and practice management
- TrialWorks (Assembly Software) — classic litigation case management (Needles/Neos lineage)
- Legal Files (Onit) — case and matter management for government, corporate, and insurance legal teams (staff counsel and litigation workflows)
- Xakia — in-house matter management with dispute tracking

The Core Model was checked against both market poles and against claims-system and ELM-suite embeddings to avoid defining the Type by the standalone firm-side product form alone.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Litify — https://www.litify.com/ , https://www.litify.com/platform , https://www.litify.com/insurance-defense-practice-management-software , https://www.litify.com/enterprise-legal-management-software
- CasePeer (8am) — https://www.casepeer.com/ , https://www.casepeer.com/feature-case-management/ , https://supportcenter.casepeer.com/
- TrialWorks (Assembly Software) — https://support.trialworks.com/
- Legal Files (Onit) — https://www.onit.com/products/elm/legal-files/ , https://www.onitacademy.com/page/legal-files-academy/
- Xakia — https://www.xakiatech.com/
- Onit (ELM suite context) — https://www.onit.com/
- Mitratech (portfolio context) — https://mitratech.com/products/ , https://success.mitratech.com/Legal_Solutions

> Sourcing limitation: direct product-domain access failed for Legal Files (legalfiles.com, transport errors), and dedicated litigation-management product pages were not found at Mitratech or Onit (404s) — the dispute-owner pole is therefore evidenced at matter-management/claims-module level, and its budget/guideline/reserve machinery is asserted more cautiously than the firm-side machinery. Help-center article bodies were reached at index level only for CasePeer and Legal Files. Precise operational parameters (stage taxonomies, permission matrices, reminder defaults) are intentionally not stated; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis against Legal Matter Management, Law Practice Management, Legal Docket Management, Court Case Management, and Insurance Claims Management are recorded in the paired Research Notes.
