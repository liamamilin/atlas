# Academic Journal Management

## Overview

An **Academic Journal Management** application is the editorial-office system of record for a scholarly journal. It receives article submissions from authors, moves each submission through a tracked editorial workflow — in practice centered on peer review — records editorial decisions, and carries accepted works to publication as articles of the journal, either by publishing them inside the system or by handing them, in structured form, to downstream production and publishing systems.

It solves a coordination problem that is otherwise unmanageable by email: a journal's editorial office must simultaneously track dozens or hundreds of manuscripts, each with its own files, authors, reviewers, deadlines, and decision state, while coordinating participants (authors, reviewers, editors, copyeditors, production staff) who are mostly external and part-time. The system is the shared place where every manuscript's state lives and every transition is recorded and communicated.

The same category of software is marketed under several names: *manuscript submission system*, *peer review system*, *editorial management system*, or *journal publishing platform*, depending on how much of the publishing pipeline the vendor covers.

The boundary of the Type: it is journal-scoped editorial operations — not the review exchange alone (that is the territory of a Peer Review Platform), not trade-book or magazine editorial production, and not the storage of already-published works.

## Users & Context

**Primary operators (journal side):**

- **Editor-in-chief / senior editors** — own the journal's editorial policy; make or ratify final decisions (accept, reject); oversee the office.
- **Handling editors** (associate editors, section editors) — triage incoming submissions, run the evaluation stage, recommend or make decisions. In many products the authority to *recommend* versus *finalize* a decision is an explicit, assignable distinction.
- **Editorial office staff / journal managers** — configure the journal (sections, policies, forms, email templates, roles), assign editors, chase overdue reviews, handle correspondence and exceptions.

**External participants (brought in per submission):**

- **Authors** — submit manuscripts through a guided wizard, track status, upload revisions, respond to copyediting and proofing queries.
- **Reviewers** — accept or decline invitations, download manuscripts, submit structured or free-text reviews and a recommendation, per deadline.

**Downstream participants (depending on product scope):**

- **Copyeditors, typesetters, proofreaders, production editors** — in full-lifecycle systems they work inside the same application; in submission-and-review systems the accepted manuscript is exported to a publisher-side production platform and these roles work elsewhere.

The work context is a journal's editorial office, typically operating one journal per configured space; publishers and university presses operate many journals as a portfolio, and mature products provide portfolio-level management and cross-journal author/reviewer hubs.

## Core Model

The system's world is organized around one governing container, one central moving object, and the machinery that moves it.

```text
Journal (identity, policies, sections, roles)
  └── Submission (manuscript files + metadata + authors)  ← the central moving object
        └── staged workflow: Submission → Review → Copyediting → Production → Proofing
              ├── Review assignment (reviewer × round × visibility × form × recommendation)
              └── Editorial decision (accept / request revisions / decline)
                    └── Published article (metadata, galleys, DOI)
                          └── Issue (volume / number, table of contents)
```

### The defining core

Five properties. Remove any one and the software is no longer journal management:

- **Journal as governing container.** Everything happens on behalf of a journal — a recurring scholarly publication with its own identity, editorial governance, and configuration: sections and article types, submission policies, review policy, licenses, roles, and correspondence templates. The journal is the unit that is configured, staffed, and reported on.
- **Submission record.** A proposed work entering the system: manuscript files, bibliographic metadata (title, abstract, keywords, section, license), and author attribution. Created by the author through a submission wizard, or recorded by staff. Every later action attaches to this record.
- **Tracked staged workflow.** Each submission moves through named stages (submission, review, copyediting, production, proofing, publication), and its current stage and status are visible to the participants who need them. The workflow is the spine of the system; dashboards are views onto it.
- **Editorial evaluation leading to a recorded decision.** A submission is evaluated and a decision — accept, request revisions, or decline — is recorded and communicated to the author. In practice the evaluation is external peer review, but the invariant is the evaluation-and-decision step itself: desk decisions before review, and content types that skip review, exist in mature products.
- **Publication as the workflow's destination.** Accepted works become published articles of the journal. In full-lifecycle systems publication happens inside the system (issues, galleys, journal website, DOI registration); in submission-and-review systems the workflow ends at acceptance with a structured handoff to a downstream production/publishing platform. Either way, publication is what the workflow exists to produce.

### Standard capabilities layered on the core

Mature products across the researched sample carry most of the following. They make the system practical; they do not define the Type.

- **Peer review machinery** — a reviewer pool with per-reviewer history (active, completed, declined assignments) and workload signals; review assignments with response and completion due dates, reminders, and cancellation/reinstatement; anonymization modes (single-blind, double-blind, open, and in some products triple-anonymous); structured review forms or free-text reviews with a recommendation; multiple review rounds per submission, with earlier reviews visible in later rounds; editor confirmation of submitted reviews; reviewer thanking and recognition (e.g., deposit of review activity to ORCID).
- **Role-differentiated portals** — an author dashboard (submit, track status, upload revisions, respond to copyediting/proofing requests), a reviewer dashboard (invitations, assignments, review forms), and editor dashboards with work queues such as "needs reviewers", "awaiting reviews", "reviews submitted".
- **Tiered editorial authority** — the ability to distinguish editors who may only recommend a decision from editors who may finalize it.
- **Decision correspondence** — a templated email system that drives every transition: editor assignments, review invitations, revision requests, decision letters, reviewer notifications. Correspondence is logged against the submission.
- **Revision loop** — revision requests (commonly distinguished as minor or major), author upload of revised files with a response letter, and optional re-review.
- **Post-acceptance stages** (full-lifecycle systems) — copyediting with tracked changes and author query response; production/typesetting producing galleys in one or more formats; proofing with preview rendering and correction rounds.
- **Issue management** (full-lifecycle systems) — issues as volume/number/year containers with a table of contents, per-article section, pages, and publication date; scheduling, previewing, publishing, and unpublishing issues.
- **Journal website and hosting** (full-lifecycle systems) — public article pages, issue pages, announcements, theming.
- **Integrity screening** — plagiarism/similarity checks at submission or before review; increasingly image-integrity, paper-mill, and reference checks, native or through integrations.
- **Identifier and metadata infrastructure** — ORCID for authors and reviewer recognition, organization identifiers, licenses, and DOI registration with Crossref deposit.
- **Editorial analytics** — submission counts, review turnaround, editor performance, custom reports.
- **Multi-journal operation** — press- or publisher-level administration of many journals; portfolio-wide author/reviewer hubs.

### One structure, two pipeline postures

The deepest structural difference between products is where the publishing pipeline ends:

```text
Concept:   Publication of accepted works
Posture A: in-system publishing — copyediting, typesetting, issues, website, DOIs
           all live inside the application (open-source journal platforms)
Posture B: handoff at acceptance — the system ends at the recorded decision;
           production/publishing happens in a downstream platform
           (dominant commercial submission-and-review systems)
```

Both postures satisfy the defining core; they differ in how far the staged workflow extends.

## How It Works

### Configure the journal (once)

The editorial office defines the journal's operating rules: sections and article types, submission requirements and author guidelines, declarations (competing interests, licensing, fee disclosures), review policy and default visibility mode, review forms, user roles, and the email templates that will drive correspondence. In multi-journal operations this is repeated per journal under a press/publisher umbrella.

### Author submits

```text
Author starts a submission
→ completes a guided wizard: agreements & declarations → article metadata → authors & affiliations → file upload
→ submission record is created and enters the Submission stage
→ an editor is assigned (automatically by section/category rules, or manually by the office)
```

The wizard collects what the journal's policy requires: title, abstract, keywords, section, license, competing-interest and checklist confirmations, and the manuscript plus supplementary files. Co-authors are added by identifier lookup or manual entry; author order and corresponding author are set.

### Editor triages (desk decision)

The assigned editor screens the submission — often with automated integrity checks — and makes a desk decision:

- **send to review** — the normal path into the evaluation stage;
- **accept without review** — for content types the journal does not referee;
- **decline** — reject before review (typically reversible for a defined period).

### Run a review round

```text
Prepare files for review (anonymize if the mode requires it)
→ assign reviewers from the pool (due dates, files, review form, visibility mode)
→ reviewers accept/decline, then read and review
→ editors track progress via queues and reminders
→ reviews come back; editor reads, discusses if needed, confirms each review
```

Reviewers see only what the visibility mode allows; the system hides identities accordingly, but the editor remains responsible for anonymizing the manuscript files themselves. Editors see reviewer history and workload to pick candidates, can invite unregistered reviewers, and can keep private notes about them. A submission may go through several rounds; in later rounds reviewers can be shown earlier reviews and the author's response letter.

### Decide

When the editor has enough evidence, they record one of:

- **accept** — moves the submission to post-acceptance stages;
- **request revisions** — the author uploads revised files and a response letter; the editor may open a new review round or proceed;
- **decline** — the submission is archived (usually with a revert window).

Each decision triggers templated correspondence to the author and, optionally, to reviewers. Where authority is tiered, a handling editor records a *recommendation* and a senior editor finalizes the decision.

### Post-acceptance to publication

In full-lifecycle systems:

```text
Copyediting (tracked changes; author answers queries; rounds until final)
→ Production / typesetting (galleys generated in one or more formats)
→ Proofing (proofreaders and the author check rendered proofs; correction rounds)
→ Pre-publication (verify metadata and DOI, select rendering galley, set publication date)
→ Schedule into an issue (volume/number, section, pages) and publish
```

In handoff-posture systems, acceptance produces a structured export — accepted manuscript, metadata, decision record — that feeds the publisher's production and hosting platform.

After publication, the article's record is treated as citable history: substantial changes (retractions, content or contributor changes) are made by publishing a new version rather than silently editing, and identifier deposits are updated deliberately.

## Interfaces

- **Author portal.** Purpose: let an external author submit and follow their manuscript without help. Typical information: submission wizard steps, status timeline, review timeline where policy allows, revision and copyedit/proof requests. Primary actions: start submission, upload files, upload revisions with response letter, respond to queries.
- **Reviewer portal.** Purpose: let an external reviewer complete an assignment. Typical information: invitation with due dates, manuscript files, review form, prior-round reviews when shared. Primary actions: accept/decline, download files, complete review form, submit recommendation.
- **Editor dashboard.** Purpose: let editors run their queue. Typical information: submissions grouped by stage and need (needs reviewers, awaiting reviews, reviews submitted), per-assignment status with due-date countdowns, overdue flags. Primary actions: open a submission record, assign, remind, decide.
- **Submission record.** Purpose: the workspace for one manuscript. Typical information: metadata, files by stage, participants and their roles, review rounds and reviews, discussions, decision history, correspondence log. Primary actions: assign participants, upload/select files, run stage actions (send to review, request revisions, accept, decline), record decisions.
- **Journal configuration.** Purpose: let the editorial office define policy. Typical information: sections/article types, submission fields and checklists, review settings and forms, licenses, email templates, roles and permissions. Primary actions: edit settings, manage users, enroll roles.
- **Issue manager / publication scheduling** (full-lifecycle systems). Purpose: compose and publish the journal's issues. Typical information: future and back issues, table of contents, per-article placement. Primary actions: create issue, schedule/unschedule articles, order TOC, publish/unpublish.
- **Public journal site** (full-lifecycle systems). Purpose: present the published journal. Typical information: current issue, archives, article pages with metadata and galleys, announcements. Primary actions (reader): read, download.
- **Reports / statistics.** Purpose: editorial oversight. Typical information: submission volumes, stage durations, review turnaround, editor activity. Primary actions: filter, export.

## Important Rules / Behaviors

- **Anonymization is policy plus editor responsibility.** The system hides participant identities according to the review mode, but identifying information inside manuscript files (title pages, metadata, document properties) must be removed by authors or editors before blind review. Editors always see all participant identities.
- **Review is a stage, not a gate that always applies.** Desk decisions and review-skipping paths exist for content the journal does not referee; the recorded decision is still required.
- **Decisions are recorded state changes.** A decline or acceptance changes the submission's stage, disables the decision actions, and generates correspondence; declines are typically revertible within a window.
- **Revision rounds re-enter the workflow.** Revised files land in a dedicated area of the submission record; a new review round is opened deliberately, and only files from the revision area can be sent into it.
- **Published content is immutable history.** Post-publication corrections are handled through versioning (including retractions), with prior versions remaining accessible and flagged as outdated; identifier deposits are updated explicitly, not automatically.
- **Editorial authority can be split.** The recommend-versus-finalize distinction lets journals run section editors under a final-decision editor; the system enforces who may record which decision.
- **Reviewer state is tracked and visible to editors.** Invitation response, completion, decline, cancellation, and overdue status are all first-class states with reminders; cancelled and declined assignments remain in the reviewer's history.
- **Correspondence is systematic.** Every meaningful transition has a template-driven notification; the correspondence log is part of the submission record.
- **Integrity checks gate the workflow.** Similarity and related screening typically run between submission and review; flagged submissions are handled as editorial exceptions before reviewers are involved.

## Variants

- **Full-lifecycle publishing systems vs submission-and-review systems.** The former publish in-system (copyediting through issues, website, DOIs); the latter end at acceptance and hand off downstream. This is the deepest variant and changes which roles work inside the application.
- **Open-access vs subscription journals.** Determines whether the system handles article processing charges (at submission or acceptance, or via licensing integrations) and access control on published content, or leaves distribution to the publisher's platform.
- **Small/society journals vs large publisher portfolios.** The same core runs single-journal operations with volunteer editors and portfolio operations with hundreds of journals, portfolio-wide reviewer hubs, and cross-journal submission transfers.
- **Review-policy variants.** Single-, double-, or triple-anonymous; open review with published reviews (reviewer consented); structured forms vs free text; author-suggested reviewers.
- **Discipline and language variants.** Multilingual submission and publication; humanities vs STM workflow emphases (e.g., heavier production pipelines in STM).
- **Adjacent work handled by sibling products.** Conference abstract/paper management and preprint repositories are usually separate products or separate subsystems, even from the same vendor.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Peer Review Platform | closest sibling; partial overlap | centers on the review exchange itself (assignments, reports, completion) as the primary object — often submission-agnostic or conference-oriented; journal management's center of gravity is the whole submission → decision → publication lifecycle plus journal-level configuration. Peer review is a stage inside it, and desk decisions / non-reviewed content exist without it |
| Scholarly Conference Management | adjacent | event logistics plus abstract/paper collection and review for a conference; vendors ship it as a separate product from their journal system |
| Publishing Editorial Workflow | adjacent (different domain) | trade/book/magazine editorial: acquisitions, contracts, titles; no peer review, issues, or DOI machinery |
| Institutional Repository | adjacent | stores and exposes already-published works or preprints; no editorial decision workflow (some journal platforms ship a repository framework as a separate subsystem) |
| Content Management System / CMS | surface only | full-lifecycle products host the journal website, but the website is an output of the editorial workflow; a CMS alone is not this Type |
| Academic Integrity / Plagiarism Platform | capability relationship | screening is integrated as a submission/review gate; the standalone Type centers on similarity analysis and integrity case handling |
| Reference Manager | different user job | individual researcher's bibliography tooling; no editorial workflow |

The boundary with Peer Review Platform is the one most worth a dedicated pass, because the two commercial incumbents market themselves as "submission and peer review" systems — the review-heavy end of this Type — while the open-source platforms demonstrate that the journal lifecycle, not the review exchange, is the organizing whole.

## Representative Products

- **Open Journal Systems (OJS)** — Public Knowledge Project; open source, self-hosted; full lifecycle from submission to published issues; widely used by university and society journals.
- **Janeway** — Open Library of Humanities / Birkbeck, University of London; open source, mission-hosted; editor-first staged workflow through production and publishing.
- **Editorial Manager** — Aries Systems; commercial SaaS incumbent for publisher and society journals; submission and peer-review tracking with downstream production handoff.
- **ScholarOne Manuscripts** — Silverchair; long-established commercial SaaS incumbent; submission-to-acceptance workflow management at publisher scale.

## Sources

Research date: **2026-09-06**

- Open Journal Systems (PKP) — Learning OJS 3.5, Editorial Workflow chapters (Submission, Review, Publication) and Journal Managers guide — https://docs.pkp.sfu.ca/learning-ojs/en/ (fetched via the official documentation source repository, https://github.com/pkp/pkp-docs)
- Janeway — official documentation: Workflow Guides (Author, Editor, Reviewer, Copyeditor, Typesetter, Proofreader), Manager → Review settings — https://docs.janeway.systems/
- Editorial Manager (Aries Systems) — product page and Ecosystem page — https://www.ariessys.com/products/editorial-manager/ , https://www.ariessys.com/ecosystem/
- ScholarOne Manuscripts (Silverchair) — product pages — https://www.silverchair.com/products/scholarone-manuscripts/

> Sourcing limitation: operational help-center documentation for Editorial Manager and ScholarOne Manuscripts was not reachable from the research environment on 2026-09-06; claims for those two products are calibrated to official product-page level, and no precise operational details (stage names, statuses, limits, defaults) are asserted for them. The PKP documentation site was bot-protected; its official documentation source repository was used instead. Vendor-stated market-scale figures were treated as marketing claims and are not repeated as facts.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
