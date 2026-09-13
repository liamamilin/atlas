# Peer Review Platform

## Overview

A **Peer Review Platform** is the organized evaluation exchange: it collects submissions — papers, abstracts, proposals, applications — as identified records, pairs each submission with eligible reviewers drawn from a managed pool, captures each reviewer's evaluation as a structured record, and resolves the reviews into a recorded per-submission outcome (a decision, a ranking, or a certified review report) that the organizing body — a conference, journal, funding agency, or association — acts on.

It solves a coordination problem that email and spreadsheets cannot: an organizing body must simultaneously move dozens to thousands of submissions through evaluation while coordinating participants — reviewers, authors, program committee members — who are mostly external, part-time, and unknown to each other. The platform is the shared place where every submission's evaluation state lives, where reviewer–submission pairing is made under conflict-of-interest rules, and where reviews, discussions, and decisions accumulate as a record.

The boundary of the Type: it is the review exchange itself — not the event a conference review feeds (that is conference management territory), not the journal a review feeds (that is the journal's editorial system), and not a community commentary board where anyone reviews anything.

## Users & Context

**Operators (the organizing body's side):**

- **Program chairs / organizers** — own the process: configure submission and review forms, recruit and administer the reviewer pool, run or oversee assignment, chase overdue reviews, record or ratify final outcomes.
- **Editors / program managers** (in journal-like and association programs) — triage submissions, coordinate review, prepare decision materials.
- **Intermediate evaluators** — area chairs, meta-reviewers, or judges who read the reviews and produce recommendations or final calls; in some products this layer is a formal role, in others an informal discussion among the committee.

**Evaluators:**

- **Reviewers / PC members / judges** — external experts, usually volunteers, who are invited into the process, state their expertise, are paired with specific submissions, and return structured evaluations by a deadline under a confidentiality obligation.

**Submitters:**

- **Authors / applicants** — external parties who submit work for evaluation, track its status, respond to reviews (where the process allows), and receive the outcome.

The work context is a bounded program with a calendar: a call for submissions opens, a deadline closes it, review happens in a window, and decisions are released on a date. Everything in the platform is organized around that cycle. The same machinery serves conference paper committees, journal-like review venues, grant and scholarship panels, and award judging — the objects and outcome forms vary, the exchange does not.

## Core Model

The system's world is organized around one central moving object — the submission — and the three structures that act on it.

```text
Submission (files + metadata + contributors)  ← the central moving object
  ↕ paired with
Reviewer pool (eligible evaluators, expertise, conflicts)
  ↓ produces
Review record (evaluation bound to submission × reviewer)
  ↓ aggregated by
Operating roles (chairs / editors / judges)
  ↓ resolves into
Outcome (decision / ranking / certified review report)
```

### The defining core

Four properties. Remove any one and the software is no longer a peer review platform:

- **The reviewable submission as the unit of record.** A work enters the platform as a persistent, individually identified record — manuscript or abstract files, metadata, contributor list — created for the purpose of being evaluated. Every later action (assignment, review, discussion, decision) attaches to this record. Without it there is nothing to review.
- **Platform-mediated reviewer–submission pairing.** The platform connects each submission to one or more eligible reviewers from a managed pool. Pairing may be done by direct assignment, by collecting reviewer preferences (bidding) and assigning accordingly, or by computing matches from expertise profiles — but it is always the platform's act, performed under the process's conflict-of-interest rules, not self-selection by reviewers. Without mediated pairing the surface becomes an open commentary board.
- **The review as a first-class record.** Each reviewer's evaluation is captured as a structured record bound to the specific submission–reviewer pair: a written assessment, ratings or scores against defined criteria, and a recommendation. The review has its own lifecycle (draft, submitted, confirmed) and a visibility policy — who may see which reviews at which point. Without it, assignment is just a tracker and evaluation is just a survey.
- **The evaluation outcome loop.** Reviews are aggregated and considered by the operating roles and resolved into a recorded per-submission outcome — accept/reject/revise decisions, a ranking or score summary, or a certified review report — communicated to the submitters and used by the organizing body for its next action (admit to a program, fund, award, publish elsewhere). Without it, reviews accumulate but no process completes.

### Standard capabilities layered on the core

Mature products across the researched sample carry most of the following. They make the exchange practical; they do not define the Type.

- **Reviewer pool management** — invitation and recruitment of reviewers, role administration, reviewer profiles with areas of expertise, and per-reviewer history (active, completed, declined assignments) with workload signals.
- **Preference expression** — bidding on submissions and topic/expertise selection that feed the assignment.
- **Conflict-of-interest handling** — declared and/or computed conflicts that gate or undo assignments; a reviewer who acquires a conflict with a paper loses access to it.
- **Customizable review forms** — ratings and free text with defined criteria, required questions, per-submission-type forms, configurable scales.
- **Deadlines and reminders** — review due dates, enforceable cutoffs, overdue surfacing, notification emails driving every transition.
- **Tiered evaluation authority** — reviewer → meta-reviewer / area chair / judge → chair layering, with recommend-versus-finalize distinctions.
- **Discussion machinery** — committee discussion forums, threaded comments on submissions, and author rebuttal phases.
- **Revision loops** — revised or corrected submissions re-entering review.
- **Decision correspondence** — templated decision notifications; status visibility rules for authors.
- **Role consoles** — separate author, reviewer, and operator views with queues (assigned, pending, overdue, decided).
- **Exports and reporting** — submission and review data exports, process statistics.
- **Reviewer recognition** — records of review service, such as letters of proof offered by the open-review sample.

### One structure, many realizations

The core is written conceptually; products realize each part differently.

```text
Concept:      Reviewer–submission pairing
Realizations: direct assignment by chairs; bidding then assignment;
              matching from expertise profiles and computed conflicts

Concept:      Aggregation layer
Realizations: meta-review stages with confirmation layers; judge roles
              with final say; committee discussion forums; chair decision meetings

Concept:      Outcome form
Realizations: accept/reject/revise decisions; rankings and score summaries;
              certified review reports handed to journals
```

## How It Works

### Set up the program (once per cycle)

The organizing body configures the call: submission form and file requirements, submission types and tracks, review questions and scales, deadlines for submission and review, visibility and anonymity postures, and the reviewer pool to be recruited. In many products the program is a per-cycle instance — a new site or venue is created for each edition.

### Collect submissions

```text
Call opens → authors/applicants submit (files + metadata + contributors)
→ submissions close at the deadline
→ operators screen and prepare the pool for assignment
```

Submitters track their submission's status; operators can screen out submissions that fail formal requirements before review begins.

### Pair reviewers with submissions

```text
Reviewers state expertise / bid on submissions / declare conflicts
→ operators assign directly, or run matching from expertise and conflicts
→ assignments deploy; reviewers are notified
→ conflicts bar or remove assignments
```

Pairing is the platform's most distinctive act: it balances expertise coverage, workload, and conflict avoidance across the whole pool rather than submission by submission.

### Review

```text
Reviewer receives assignment → downloads the submission
→ submits a structured evaluation (ratings + written assessment + recommendation)
→ before the deadline, under the visibility policy
```

Reviews are typically hidden from submitters until the process reaches its disclosure point; some postures release reviews to authors and co-reviewers as they arrive, and some publish them openly. Reviewers may discuss submissions in committee forums or threaded comments; authors may be given a rebuttal phase to respond to reviews.

### Aggregate and decide

```text
Reviews complete → intermediate evaluators (meta-reviewers / judges / ACs)
weigh the reviews and record recommendations
→ chairs record the final per-submission outcome
→ outcomes are released to submitters with notifications
```

The outcome forms vary by program type: conference programs record accept/reject (with revision paths); panels record rankings and funding recommendations; award programs record winners; journal-independent services certify the review report itself as the deliverable.

### Close the loop

Accepted or corrected submissions may re-enter (revision rounds, camera-ready uploads); the evaluation record is retained for the organizing body's reporting, and reviewers may receive recognition records for their service.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Operator console

The organizing body's cockpit.

- submissions grouped by state (submitted, under review, decided), review progress per submission, overdue assignments, reviewer workload
- primary actions: configure forms and deadlines, recruit reviewers, assign and reassign, send reminders, record or release decisions, export data

### Reviewer workspace

The evaluator's queue.

- assigned submissions with deadlines, the submission files, the review form, discussion threads where enabled
- primary actions: accept/decline or bid, download files, enter or edit a review, comment

### Author / applicant portal

The submitter's window into the process.

- submission wizard or form, status timeline, review timeline where policy allows, rebuttal or revision uploads where enabled
- primary actions: submit, revise, respond to reviews, view outcome

### Submission record

The workspace for one submission.

- files and metadata, contributors, assigned reviewers and their review states, reviews and discussions, decision history, correspondence log
- primary actions: assign participants, read reviews, record recommendations or decisions

### Program configuration

Where the organizing body defines the process.

- submission fields and types, review questions and scales, deadlines and stages, visibility and anonymity settings, roles and permissions, email templates

## Important Rules / Behaviors

- **Pairing is governed by conflicts.** Conflict-of-interest rules are structural: reviewers declare conflicts (and expertise), the system computes or enforces them, and a review can be invalidated or hidden when a conflict emerges after the fact.
- **Reviews have a visibility policy.** Who sees which review when is a configured property of the process — hidden from authors until decisions, released to authors and reviewers during the process, or published openly. The default posture in most sampled products is confidentiality until decision.
- **The review record is attributed and durable.** Reviews bind to the specific reviewer and submission, persist through the process, and remain part of the submission's evaluation history; operators can typically undo or reset aggregation decisions but the review trail remains.
- **Deadlines are enforced states.** Submission and review windows open and close on configured dates; late reviews require operator intervention; enforceable cutoffs prevent post-deadline evaluation.
- **Authority is tiered.** Reviewers recommend; meta-reviewers, judges, or chairs finalize. The system enforces who may record which outcome, and intermediate layers can override reviewer recommendations.
- **Outcomes are recorded state changes.** A decision changes the submission's state, triggers templated correspondence, and is typically irreversible except through explicit operator action (revert, reopen).
- **Submitters see status, not (by default) the deliberation.** Author portals expose submission state and outcome; the internal review record is exposed only as the visibility policy allows.

## Variants

- **Conference review** — the dominant habitat: paper/abstract submission, committee review, discussion and rebuttal, accept/reject, camera-ready handoff; often bundled with event machinery (registration, program building, proceedings).
- **Journal-like review venues** — the review exchange operated for a journal without the journal's production pipeline; reviews may be public and discussions open.
- **Independent review services** — the platform runs the review before journal submission and certifies the review report as the deliverable; affiliate journals consume the reviews for their own decisions.
- **Panel and program review** — grants, scholarships, fellowships: applications reviewed and scored by panels; outcomes are rankings and funding recommendations.
- **Award and competition judging** — entries evaluated by judge committees; outcomes are winners and galleries.
- **Anonymity postures** — single-blind, double-blind, anonymous submissions, or fully open review with published review records; configurable, not definitional.
- **Track structures** — multi-track programs with per-track committees and chairs under a supervising chair.

A variant remains a variant unless it changes the core: if the platform stops mediating pairing and stops resolving outcomes, it has become a community commentary surface, not a peer review platform.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Academic Journal Management | closest sibling; partial overlap | centers the journal's whole editorial lifecycle — journal container, submission workflow, copyediting/production, issues, publication — with peer review as one stage; this Type is the review exchange alone and is journal-agnostic. Remove review and journal management survives (desk decisions, non-refereed content); remove the journal container and publication pipeline and a peer review platform remains |
| Scholarly Conference Management | adjacent; packaging overlap | centers the event — registration, logistics, program building, proceedings — with review as one workflow; many products bundle both, but the review exchange stands alone without any event machinery |
| Assessment Platform | different object and evaluator relationship | administers scored instruments to a taker population and returns attributed results (grades); here works are evaluated by peers to produce admission/funding/publication outcomes |
| Code Review Platform | same name, different domain | reviews code changes inside an engineering workflow, not scholarly or program submissions; no program committee or submission cycle |
| Community review surfaces (preprint commentary platforms) | boundary case, not this Type | reviews are self-selected community contributions with no platform-mediated pairing and no recorded outcome loop serving an organizing body |
| Research Grant Management | adjacent at the program level | spans the full grant lifecycle (intake, funds, reporting); the review exchange is its evaluation stage — when evaluation is the center, this Type; when funding administration is the center, grant management |
| Online Form Builder / Survey Platform | capability relationship | provides configurable forms, but no reviewer pool, no pairing, no evaluation outcome loop |

## Representative Products

- **OpenReview** — open peer review platform hosting conference and journal-like venues; public review records, matching from expertise profiles, meta-review layers.
- **EasyChair** — long-established conference management workhorse with deep review machinery (preference-based assignment, discussion, rebuttal); also used for proposal evaluation.
- **Microsoft CMT (Conference Management Toolkit)** — free cloud toolkit for academic conference workflows with multi-track and meta-reviewer role structures.
- **Indico** — CERN's open-source event platform whose call-for-abstracts and paper peer review modules realize the review exchange inside an event system.
- **ConfTool** — commercial SaaS (with a free Standard edition) for conference submission, review, scheduling, and registration.
- **OpenWater** — commercial application & review platform for associations and foundations: abstracts, awards, grants, scholarships, fellowships over one review core.

The defining core was checked against a journal-independent review service (Review Commons) and a community review surface (PREreview) to separate the review exchange from both journal workflows and open commentary boards.

## Sources

Research date: **2026-09-08**

- OpenReview — official documentation (workflow, venue creation, default review form, FAQ) — https://docs.openreview.net/
- Microsoft CMT — official documentation (docs index, chair how-tos, FAQ) — https://cmt3.research.microsoft.com/docs/
- Indico — official user guide (reviewing abstracts, paper peer reviewing) — https://learn.getindico.io/
- ConfTool — official user documentation (instructions for reviewers and PC members) and product pages — https://www.conftool.net/
- EasyChair — official product pages (home, conference management) — https://easychair.org/
- OpenWater — official product pages — https://openwater.com/
- Review Commons — official site — https://reviewcommons.org/
- PREreview — official site — https://prereview.org/

> Sourcing limitation: EasyChair's help center was unreachable (the /help path returned 404), so EasyChair claims are calibrated to official product-page level. CMT's reviewer-assignment pages could not be located publicly (two documentation paths returned 404), so its assignment mechanics are described only at the level its FAQ and chair docs support. OpenWater's operational depth rests on product pages rather than its help center. Precise operational details that depend on inaccessible documentation (exact review-form fields per product, default reviewer counts, numeric deadline defaults) are intentionally not stated; vendor scale figures are recorded as vendor claims, not verified facts. Detailed evidence and cross-product comparison are recorded in the paired Research Notes.
