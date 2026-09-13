# Research Notes — Peer Review Platform

Research date: 2026-09-08
Slug: peer-review-platform
Directory leaf: Peer Review Platform (§23 Education, Research & Knowledge Institutions)

## Research Goal

Understand what a Peer Review Platform actually is in the real market: what objects exist inside it, who operates it, how the review exchange works end to end, which rules and states govern it, and where this Application Type ends relative to its neighbors — above all **Academic Journal Management** (processed sibling with a pre-hung joint-review flag), **Scholarly Conference Management** (unprocessed sibling), **Assessment Platform** (processed), and community review surfaces (PREreview-class).

## Initial Boundary (pre-research hypothesis)

- Core use: a platform whose product IS the review exchange — collect submissions (papers, abstracts, proposals, applications), pair them with reviewers, capture structured evaluations, and resolve them into decisions/scores/outcomes for an organizing body (conference, journal, agency, association).
- Primary users: program chairs / editors / program managers (operators); reviewers (evaluators); authors / applicants (submitters).
- Nearest neighbors: Academic Journal Management (the review stage inside a journal workflow — highest confusion risk, flag pre-hung), Scholarly Conference Management (event logistics + review machinery), Assessment Platform (scored instruments for takers), Code Review Platform (same name, different domain), community commentary surfaces (PubPeer/PREreview).
- Open questions: does the Type require a decision outcome, or is a certified review report enough? Is reviewer assignment platform-mediated by definition? Where does event machinery (registration, program building) stop being part of this Type? Does publication (camera-ready hosting, refereed preprints) break the boundary with journal management?

## Research Questions

1. What is the unit of record — what exactly gets reviewed, and how does it enter the system?
2. How are reviewers recruited, profiled, and paired with submissions (manual, bidding, matching)? How are conflicts of interest handled?
3. What does a review look like as a record (fields, scores, recommendations, visibility policy, lifecycle)?
4. How do reviews aggregate into outcomes (meta-review layers, judge roles, PC discussion, decisions, notifications)?
5. What roles exist and how is authority tiered?
6. What anonymity/blind-review postures exist and are they definitional or configurable?
7. What adjacent machinery do real products bundle (event logistics, registration, program building, proceedings, publication) — and what does that mean for the Type boundary?
8. Where is the line vs Academic Journal Management (discharge the pre-hung flag), vs Scholarly Conference Management, vs Assessment Platform, vs community review surfaces?
9. Historical check: would a paper-era program committee satisfy the same core?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer levels:

| Product | Operator / Owner | Philosophy | Customer level | Evidence tier |
|---|---|---|---|---|
| OpenReview | OpenReview.net (nonprofit, UMass Amherst heritage) | open peer review; public review records; venue-based service operated for organizers | ML/AI conferences and journal-like venues (e.g., TMLR) | Tier 1 (official docs, GitBook) |
| EasyChair | EasyChair (Andrei Voronkov) | free/low-cost conference management workhorse; review machinery + event/publishing services | individual conferences worldwide since 2002 (vendor: 4.9M users, 125k+ conferences) | Tier 2 (official product pages; help center 404) |
| Microsoft CMT | Microsoft Research | free cloud toolkit for academic conference workflows | conferences requesting per-year sites (vendor: 12,000+ hosted) | Tier 1 (official docs) |
| Indico | CERN (open source) | event platform with review workflows as modules (CFA + paper peer review) | institutional/event organizers (CERN heritage) | Tier 1 (official user guide) |
| ConfTool | ConfTool GmbH (Germany) | commercial SaaS + free Standard edition; submission/review/scheduling/registration | 5,000+ organizers (vendor claim); small-to-large academic events | Tier 1 (user docs) + Tier 2 (product pages) |
| OpenWater | OpenWater (ASI) | commercial application & review SaaS for associations/foundations/higher-ed | associations, foundations, universities (750+ orgs, vendor claim) | Tier 2 (official product pages) |

Boundary/variant probes (not primary samples): Review Commons (journal-independent review service, Tier 2), PREreview (community preprint review, Tier 2).

## Sources

### OpenReview — Tier 1 (docs.openreview.net, GitBook; .md endpoints fetched directly)

- Example conference workflow (venue request → submission → matching → review → rebuttal → meta-review → decision → camera-ready): /venue-request-workflow/conferences.md
- Creating a New Venue (venue request form; conferences/workshops/class projects/symposia; journals via separate contact path; TMLR journal-like workflow): /getting-started/hosting-a-venue-on-openreview/creating-your-venue-instance-submitting-a-venue-request-form.md
- Default Review Form (title / review [markdown+LaTeX] / rating 1–10 enum / confidence 1–5): /reference/default-forms/default-review-form.md
- FAQ index (profiles, expertise selection, manual vs automatic assignment, due vs expiration dates, reviewer notification, letters of proof): /getting-started/frequently-asked-questions.md

### Microsoft CMT — Tier 1 (cmt3.research.microsoft.com/docs)

- Docs index (positioning: conference management system for academic conferences; Azure-hosted; scale claims)
- CHAIR HOW-TO: Enable Submissions (multi-track configuration, submission settings, deadlines, supplementary material, desk reject, withdraw)
- TOP 10 QUESTIONS FAQ (roles incl. senior meta-reviewer/track chairs; conflicts removing reviews; withdrawn papers; per-year sites; data retention)

### Indico — Tier 1 (learn.getindico.io, official user guide)

- Reviewing Abstracts (reviewer ratings/comments; judge accept/reject; conveners; undo decisions; bulk judging; export)
- Paper Peer Reviewing (module setup; content vs layout reviewing; custom questions; reviewing teams; competences; call for papers; paper assignment; permissions; author/reviewer/judge flows; corrections loop)

### ConfTool — Tier 1 user docs + Tier 2 product pages (conftool.net)

- Instructions for Reviewers and PC Members (account/invitation, priority topics, bidding, conflicts, confidentiality agreement, chair assignment, review forms, PC forum, reviews hidden until decision)
- Homepage / product pages (Standard vs Pro; submission+review+scheduling+registration scope; GDPR posture)

### EasyChair — Tier 2 (easychair.org; /help returned 404, abandoned after one attempt)

- Homepage (services: conference management, registration, publishing, Smart CFP/Slide/Program; scale claims; since 2002)
- Conference Management page (submission, reviewer management incl. COI and preference-based assignment, reviewing incl. discussion + rebuttal, models: standard vs multi-track; "evaluating project proposals" and teaching use)

### OpenWater — Tier 2 (openwater.com)

- Homepage (application & review software; modules: abstracts/awards/grants/scholarships/fellowships/applications; multi-round review; vendor category definition; integrations; scale claims)

### Review Commons — Tier 2 (reviewcommons.org)

- Homepage (journal-independent peer review of preprints; refereed preprints with reviews + author responses; affiliate journals; ASAPbio + EMBO)

### PREreview — Tier 2 (prereview.org)

- Homepage (open preprint reviews by self-selected community; review requests; clubs; live reviews; no assignment/decision machinery)

### Cross-reference (processed sibling)

- research/academic-journal-management.md + applications/academic-journal-management.md (OJS, Janeway, Editorial Manager, ScholarOne evidence) — used for the joint review.

---

## Product Observations

### OpenReview — evidence layer A (official docs)

**Positioning.** Open peer review platform; organizers request a "venue" (conference, workshop, class project, symposium, "or other event"); journals use a separate onboarding path ("If you are a journal hoping to use OpenReview, please email…"; "If you're following a journal-like workflow like TMLR, please get in touch").

**Venue lifecycle (workflow doc).** Venue request form → OpenReview team deploys → venue id + venue homepage + submission invitation + committee groups (Program_Chairs, Senior_Area_Chairs, Area_Chairs, Reviewers, Authors), each with a role console (assignments, pending tasks, review status).

**Submission phase.** Submissions open/close on configured dates; optional abstract-registration deadline; authors must have OpenReview profiles; desk rejection after a grace period (example: 24h for co-author profile signup); Post Submission stage controls readers and hides fields (e.g., hide PDFs from reviewers during bidding).

**Pairing.** Paper Matching Setup computes **affinity scores and conflicts**; optional **bidding** stage (bidding console sorted by affinity, conflicts filtered out); matching run per group (SAC→AC, AC→submission, reviewer→submission); proposed assignments reviewed/modified (ACs can reassign and invite external reviewers); deployed; manual assignment also supported. Conflict propagation: SAC conflicts transfer to their ACs.

**Review stage.** Review period started via Review Stage; **customizable review form** (default: title; review [markdown + LaTeX]; rating 1–10 with anchored descriptions; confidence 1–5); rating/confidence field names configurable for stats; **review readers configurable** (common: assigned SAC/AC/reviewers only); reviews can be **released to authors and other reviewers** (immediately or on posting).

**Discussion.** Optional **rebuttal stage** (authors reply; free or one-per-review); **comment stage** (threaded discussions among reviewers); submission revision stage (field-limited).

**Aggregation & decision.** **Meta-review stage** (ACs post recommendations); optional **meta-review confirmation** by SACs; optional AC ratings of reviews; **Decision Stage** (PCs submit decisions based on meta-reviews; bulk upload for large venues with decision stats); **release decisions** with per-decision email templates; optional public release of submissions and deanonymization of authors.

**Post-decision.** Camera-ready revision period for accepted submissions (revision enabled for accepted only). Reviewer recognition: letters of proof; expertise selection feeds matching.

### EasyChair — evidence layer B (official product pages; operational help unreachable)

**Positioning.** "Conference management system… From managing program committees to publishing proceedings"; since 2002; vendor claims 4.9M users, 125,283 conferences, 21M+ pages/month.

**Scope (conference management page).** (1) Call for submissions (Smart CFP); (2) abstract and paper submission (flexible forms, multiple file types); (3) **reviewer management** — PC management/monitoring, reviewer database, "sophisticated and flexible management of the access of PC members and referees to papers and conflicts of interests", **review assignment based on preferences of PC members**; (4) **reviewing** — submission of reviews, **online discussion of papers**, **author rebuttal phase**; (5) communication and monitoring (email to reviewers/authors/attendees, analytics); (6) program editing/publishing (Smart Program); (7) proceedings preparation; (8) attendee registration and online payment.

**Models.** Standard (single PC; papers distributed among PC members "normally based on their preferences") and **multi-track** (per-track PCs + track chairs + superchair supervising tracks). Anonymous submissions optional.

**Non-conference uses (vendor-stated).** "Evaluating project proposals"; "teaching students paper writing and peer reviewing".

### Microsoft CMT — evidence layer A (official docs)

**Positioning.** "Conference management system for hosting academic conferences, sponsored by Microsoft Research"; Azure-hosted; handles "the most complex workflows of academic conferences"; vendor claims 12,000+ conferences hosted, 1M+ users.

**Roles.** Author, Reviewer, **Meta-Reviewer, Senior Meta-Reviewer**, Track Chairs; chairs administer users and roles (registered CMT accounts required).

**Multi-track.** Each track enabled and configured separately (own settings, own submission dropdown for authors); track-level review behavior.

**Submission configuration (chair docs).** Welcome/instructions; abstract required with character range (documented default range 1000–10000 chars); submission file min/max, size (documented up to 100MB), formats; **supplementary material as a separate activity** with own deadlines/limits; revision files; subject areas; **desk reject** status visibility; **withdraw** options (incl. whether authors see reviews of withdrawn papers); author-editing permissions; submission questions surfaced in chair console.

**Deadlines.** Activity timeline (Paper Submission, Edit Submission, Supplementary Material) with enable/disable + dates; extensions by re-dating.

**Operational rules (FAQ).** A review can disappear from the chair's view because the **reviewer acquired a conflict** with the paper, the paper changed track, the paper was withdrawn, or an account was deleted; conference sites are requested per year; data retained ~2 years post-conference then deleted.

### Indico — evidence layer A (official user guide)

**Positioning.** Open-source event platform (CERN): categories, events (lectures/meetings/conferences), timetable, registration, room booking — with "reviewing workflows for scientific papers and their abstracts" as feature modules.

**Abstract review (CFA module).** Abstracts submitted to tracks; **Reviewers** leave feedback: numeric **ratings per question defined by the event manager** + comments + proposed presentation type; **Judges** accept/reject based on the reviews — "a Judge may Reject an Abstract even if all Reviewers have given positive comments"; **conveners** have privileged access to all reviews in their tracks; event managers can **undo judge decisions**; bulk judging; export (pdf/excel).

**Paper peer reviewing module.** Enabled per event; paper templates; **content reviewing and layout reviewing as separate processes** with own (enforceable) deadlines; **custom review questions** (rating / yes-no / free text; required flags; configurable rating scale — rescaling existing answers on change); **judging deadline**; **reviewing teams** (content reviewers, layout reviewers, judges, paper managers) + **competences** (expertise keywords) to aid matching; call for papers scheduled (start/end); **paper assignment by paper managers — "Reviewers and judges can only work on papers that have been explicitly assigned to them"**; reviewer proposes **accept / reject / request corrections**; **judge has the final say** (one judge per paper; judgment resettable); **corrections loop** (author uploads new version, judged again); comments with per-audience visibility (e.g., judges-only); accepted papers published onto the contribution.

**Permissions.** Explicit table: submit (abstract/contribution submitters), review (assigned reviewers + event managers), judge (assigned judges + event managers), assign/manage (paper + event managers).

### ConfTool — evidence layer A (user docs) + B (product pages)

**Positioning.** "Web-based event management system… to support the organization of academic conferences, workshops, congresses and seminars": submission and review of contributions, program scheduling, participant registration/invoicing, communication. Two editions: **ConfTool Standard** (free, ≤150 participants, local install, basic functions) and **ConfTool Pro** (hosted SaaS, full features, support). Vendor claims 5,000+ organizers, 15+ languages, GDPR posture (German hosting, per-conference databases).

**Reviewer flow (user docs).** Invited account (organizer-created, role pre-set) → update details → **select priority topics** (expertise, "directly affects the quality of the review process") → **bid for contributions** (Pro; mark preferred submissions + flag those outside expertise; **state conflicts of interest** — "contributions you cannot review objectively"; usually cannot decline after assignment) → **confirm the Reviewer Confidentiality Agreement** (Pro) → chairs assign based on topics + bids → **enter reviews** ("each contribution is scored across several categories"; different review criteria/forms per submission type, e.g., papers vs posters; session timeout warning) → **PC discussion forum** (Pro; usually after the review process, for contributions still undecided) → register for the event.

**Visibility rule.** "Reviews are not made visible to authors until the review process is finished and the chairs have decided the final acceptance status based on all evaluations."

**Conflict detection.** "One account for everything… makes it easier for the system to detect conflicts of interest."

### OpenWater — evidence layer B (official product pages)

**Positioning.** "Application and Review Software to Power Your Mission" for associations, foundations, higher education. Modules: Abstracts ("abstract collection, peer review, session scheduling"), Awards, Grants, Scholarships, Fellowships, Applications, Speakers, Accreditation.

**Vendor category definition (FAQ).** "Application and review software refers to specialized technology platforms for managing programs where users submit content and a formal committee evaluates it (e.g., abstracts, awards, grants, scholarships, or fellowships)."

**Features.** Program website builder; drag-and-drop submission forms with conditional logic and attachments; **multi-round review** ("give reviewers access to all of their assigned applications… then compile every score on every submission in one place"); automated communications (email wizard); reporting/analytics; process-specific capabilities (award winner galleries, conference session builder from approved abstracts, funding distribution tracking). Since 2012; 750+ organizations (vendor claim); AMS/CRM integrations (iMIS, Salesforce).

### Review Commons — evidence layer B (Tier 2, variant probe)

"Journal-independent peer review": authors submit preprints; the platform coordinates peer review **before journal submission**; refereed preprints publish the reviews + author responses alongside the preprint; **affiliate journals** use the reviews for their decisions ("make informed decisions without having to start the process from scratch"). Launched by ASAPbio + EMBO; journal editors participate in coordinating review (blog post on journal-editor-coordinated pilots). The outcome is a **certified review record**, not an accept/reject decision.

### PREreview — evidence layer B (Tier 2, boundary probe)

"Open preprint reviews. For all researchers." Community members **self-select** preprints to review (plus author-initiated **review requests** and club-based group reviews); reviews are published openly under CC-BY with named reviewers. **No platform-mediated assignment, no confidentiality gate, no accept/reject outcome, no organizing body consuming the outcome.** (A "matchmaking experiment" survey exists but is experimental.)

---

## Cross-product Comparison

| Dimension | OpenReview | EasyChair | CMT | Indico | ConfTool | OpenWater |
|---|---|---|---|---|---|---|
| Submission as unit of record | Yes (submission + files + authors + metadata) | Yes (abstract/paper submission) | Yes (paper + supplementary + questions) | Yes (abstracts; papers for accepted abstracts) | Yes (contributions) | Yes (applications/abstracts/entries) |
| Pairing mechanism | Manual + affinity-score matching + optional bidding | Preference-based assignment ("based on preferences of PC members") | Chair-driven assignment (roles administered by chairs) | Manual assignment by paper managers ("only… explicitly assigned") | Chair assignment from topics + bids | Admin assigns; reviewers see "assigned applications" |
| Conflict-of-interest machinery | Yes (computed in matching; conflicts filtered in bidding; SAC→AC propagation) | Yes ("access… and conflicts of interests" management) | Yes (conflict removes review from view) | Not evidenced in fetched docs | Yes (bid-time conflict flagging; single-account detection) | Not evidenced in fetched pages |
| Review as structured record | Yes (customizable form; default rating 1–10 + confidence 1–5 + markdown review) | Yes (review submission; specifics at page level) | Yes (reviewer + meta-reviewer reviews) | Yes (ratings per manager-defined question + comments + proposed action) | Yes ("scored across several categories"; per-type forms) | Yes (review forms; compiled scores) |
| Review visibility policy | Configurable readers; release-to-authors option | Access management for PC/referees | Status-dependent visibility (e.g., withdrawn-paper reviews) | Per-audience comment visibility; conveners see all | Hidden from authors until chairs decide | Role-scoped (admin/reviewer) |
| Anonymity postures | Configurable (public release + deanonymization optional) | Anonymous submissions optional | Not evidenced in fetched pages | Not evidenced in fetched pages | Confidentiality agreement step | Not evidenced |
| Discussion / rebuttal | Rebuttal stage + threaded comments | Online discussion + author rebuttal phase | Meta-reviewer layer implies discussion (not directly documented) | Comments with visibility control | PC discussion forum (post-review) | Not evidenced |
| Aggregation layer | AC meta-reviews + SAC confirmation + PC decisions | PC discussion → chairs | Meta-reviewer → senior meta-reviewer → chairs | Judge (final say; one per paper) | Chairs decide from reviews + forum | Committee decides from compiled scores |
| Outcome forms | Accept/reject decisions (bulk-uploadable), released with templates | Accept/reject (implied by rebuttal/decision flow) | Decisions incl. desk reject; statuses | Accept / reject / corrections (abstracts: accept/reject + type) | Final acceptance status decided by chairs | Scores → committee decisions (awards/grants/fellowships) |
| Revision loops | Submission revision + camera-ready stages | Not evidenced in fetched pages | Revision files + edit-submission window | Corrections loop (new version re-judged) | Authors update contributions | Multi-round review |
| Event machinery bundled | Venue homepage only (no registration/logistics) | Registration + payments + program + proceedings | Conference site (per-year) | Full event platform (timetable, registration, room booking) | Scheduling + registration + invoicing | Session builder + award galleries |
| Publication machinery | Camera-ready hosting on submission record; journal-like venues (TMLR) via special path | Proceedings preparation + publishing services | Not evidenced | Accepted papers published onto contribution | Not evidenced | Award galleries / funding distribution |
| Multi-program operation | Many venues on one platform | 125k conferences (vendor) | Per-conference sites | Per-event modules | Per-event instances | Multiple programs per organization |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as a peer review platform:

1. **The reviewable submission as the unit of record.** A work, abstract, proposal, or application enters the platform as a persistent, individually identified record — files + metadata + contributors — created for the purpose of being evaluated. Remove → a submission form / file store.
2. **Platform-mediated reviewer–submission pairing.** The platform connects each submission to one or more eligible reviewers drawn from a managed pool — assigned directly by organizers/editors, bidded-then-assigned, or algorithmically matched — under the process's conflict-of-interest rules. The pairing is the platform's act, not self-selection. Remove → an open commentary board.
3. **The review as a first-class record.** Each reviewer's evaluation is captured as a structured record bound to the submission × reviewer pair — written assessment + rating/score + recommendation — with its own lifecycle (draft → submitted → visible per policy) and a visibility policy (who may see which reviews when). Remove → an assignment tracker / survey form.
4. **The evaluation outcome loop.** Reviews are aggregated and considered by the operating roles and resolved into a recorded per-submission outcome — a decision (accept/reject/revise), a ranking or score summary, or a certified review report — that is communicated to submitters and serves the organizing body's next action (admit, fund, award, publish elsewhere). Remove → a review collection with no process.

Jointly-held is load-bearing:

- 1 alone = submission intake form
- 2 without 1 = reviewer roster
- 3 without 1+2 = survey/comment form
- 1+3 without 2 = community commentary surface (PREreview/PubPeer territory)
- 1+2 without 3 = assignment tracker
- 2+3 without 1 = review forms with nothing to review
- 1+4 without 2+3 = decision log / ballot
- 3+4 without 1+2 = generic scoring machinery (assessment territory)

**Historical / market-sample check (§24-style, conceptual + in-sample).** The paper-era program committee satisfies all four legs: submissions mailed to the chair; the chair pairs them with PC members (avoiding conflicts); reviewers return structured review forms; the PC meeting aggregates and records accept/reject decisions communicated to authors. The 2000s web generation (EasyChair since 2002; CMT; ConfTool) satisfies the legs with no matching algorithms, no public reviews, no cloud dashboards. The definition therefore names **no anonymity mode, no scoring scale, no event, no publication pipeline, no matching algorithm** — all are era- or posture-specific realizations. OpenReview's own default review form (rating 1–10, confidence 1–5) is a venue-customizable default, not an invariant; Indico's judge role and OpenReview's meta-review layer are two realizations of the same aggregation leg.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Reviewer pool management** — recruitment/invitation, role administration, reviewer profiles with expertise/topics/competences, per-reviewer assignment history and workload signals.
- **Preference expression** — bidding on submissions (EasyChair preference-based assignment, ConfTool Pro bidding, OpenReview optional bid stage) and/or expertise/topic selection feeding assignment.
- **Conflict-of-interest handling** — declared and/or computed conflicts gating assignment (documented in 5 of 6 primary samples; not evidenced for Indico in fetched docs).
- **Structured, customizable review forms** — ratings/scores + free text + recommendation; per-submission-type forms; required questions; configurable scales.
- **Review lifecycle & deadlines** — due dates, enforceable deadlines, reminders, late-review handling.
- **Tiered evaluation authority** — reviewers → meta-reviewers / area chairs / judges → chairs/PC; recommend-vs-finalize distinctions.
- **Discussion machinery** — PC discussion forums, threaded comments, author rebuttal phases.
- **Revision/correction loops** — revised submissions re-entering review; correction requests.
- **Decision recording & correspondence** — recorded per-submission outcomes, decision letters/notifications via templates, status visibility rules.
- **Role consoles/dashboards** — author, reviewer, and operator consoles with queues (assigned, pending, overdue).
- **Review visibility policy** — who sees which reviews when (hidden from authors until decision is the classic posture; release-to-authors and public reviews as configured postures).
- **Exports/reports** — submission/review data exports, statistics.
- **Reviewer recognition** — letters of proof, review-record exports (OpenReview), ORCID-class recognition in the journal sibling.

### L2 — Variant / Optional Structure

- **Anonymity posture** — single/double-blind, anonymous submissions, open/deanonymized review; configurable, not definitional.
- **Public review records** — reviews (and rebuttals) published openly (OpenReview venues; Review Commons refereed preprints; PREreview-style community review as the boundary case).
- **Algorithmic matching** — affinity scores from expertise profiles (OpenReview); competence keywords (Indico).
- **Tracks / multi-track** — per-track PCs, settings, and chairs (EasyChair, CMT).
- **Meta-review formalization** — dedicated meta-review stages and confirmation layers (OpenReview, CMT roles) vs judge roles (Indico) vs PC forum (ConfTool).
- **Event machinery packaging** — registration, payments, program building, proceedings (EasyChair, CMT, Indico, ConfTool, OpenWater) — adjacency packaging, not the review core.
- **Program-family packaging** — awards/grants/scholarships/fellowships as configured program types over the same review machinery (OpenWater).
- **Journal-like venues** — review exchange operated for a journal without the journal's production pipeline (OpenReview/TMLR path).
- **Independent review service posture** — the platform runs the review and hands certified reviews to journals (Review Commons).
- **Camera-ready / proceedings handoff** — accepted-submission revision and hosting (OpenReview camera-ready; Indico contribution publication; EasyChair proceedings).
- **Integrity screening** — plagiarism/similarity gates (common in the journal sibling; integration-level here).
- **Payments** — registration fees, APCs (adjacent modules).
- **AI assistance** — reviewer matching, integrity checks (emerging, integration-level).

### L3 — Vendor-specific (research notes only)

- **OpenReview**: venue request form operated by the OpenReview team; venue id scheme; SAC/AC/reviewer three-layer with conflict propagation; bulk decision upload for large venues (>2000 submissions threshold stated in docs); expertise selection; mandatory profiles; letters of proof; TMLR journal-like workflow; default rating/confidence enums.
- **EasyChair**: Smart CFP / Smart Slide / Smart Program services; PC-expert; superchair multi-track model; per-conference licensing; publishing services list.
- **CMT**: per-year site requests; ~2-year data retention then deletion; Azure hosting; account link/merge; documented defaults (abstract 1000–10000 chars, 100MB files); supplementary material as separate activity; desk-reject visibility options.
- **Indico**: CFA + paper peer review as event modules; convener role; content-vs-layout review split; one judge per paper; competence keywords; rating rescaling on scale change; accepted papers published onto contributions.
- **ConfTool**: Standard (free, ≤150 participants, local) vs Pro (hosted) split; reviewer confidentiality agreement step; session timeout; priority topics; German hosting/GDPR posture; per-conference databases.
- **OpenWater**: program website builder; iMIS/Salesforce/Higher Logic integrations; email wizard; award galleries; session builder; funding distribution tracking; vendor scale claims.

## Vendor-specific Findings / Rejected Findings

- **Rejected from core**: "peer review platform = conference management system" — 5 of 6 primary samples bundle event machinery, but OpenReview (a canonical in-type product) operates the review exchange with no registration/logistics at all; event machinery is packaging.
- **Rejected from core**: "double-blind anonymity is the definition" — anonymity postures are configurable everywhere they are documented; OpenReview's flagship venues run open review with public records.
- **Rejected from core**: "accept/reject decision is the only outcome" — Review Commons produces certified review reports consumed by journals; award programs produce rankings/winners. The invariant is the recorded evaluation outcome, not its form.
- **Rejected from core**: "algorithmic matching is definitional" — manual assignment satisfies the pairing leg everywhere; matching is an implementation.
- **Rejected**: precise numeric defaults (review-day windows, reviewer counts, file limits) — vendor-documented defaults (CMT abstract range, OpenReview rating enum) kept in research notes only.
- **Rejected**: "peer review platform = journal peer review system (Editorial Manager/ScholarOne)" — those products' center of gravity is the journal editorial lifecycle (see Boundary Findings 1).

## Boundary Findings

1. **vs Academic Journal Management (§23 sibling, processed) — JOINT REVIEW DISCHARGED, verdict keep-both.** The pre-hung flag asked whether Peer Review Platform is just the review stage of journal management. Findings: (a) in all four journal-side sampled products (OJS, Janeway, Editorial Manager, ScholarOne), peer review is a stage inside the journal's submission→decision→publication lifecycle, governed by a journal container (sections, policies, issues) — remove review and journal management survives (desk decisions, non-refereed content, production continue; OJS ships "Accept and Skip Review"); (b) conversely, every primary sample of THIS pass operates the review exchange as the whole product with no journal container and no production pipeline — remove the journal container and publication machinery and the review platform survives intact (OpenReview, EasyChair, CMT, Indico modules, ConfTool, OpenWater all do exactly this). The seam is the organizing whole: **review exchange (this Type) vs journal editorial lifecycle (that Type)**. Straddling is real and acknowledged: Editorial Manager/ScholarOne market themselves as "submission and peer review" systems (the review-heavy end of the journal Type), and OpenReview hosts journal-like venues (TMLR) — but in both cases the journal/publication posture is what makes them journal-side. Keep both leaves; cross-reference both documents.
2. **vs Scholarly Conference Management (§23 sibling, UNPROCESSED) — NEW FLAG for joint review.** EasyChair, CMT, Indico, ConfTool, and OpenWater all pair review machinery with event/program machinery (registration, payments, program building, proceedings, session scheduling). The seam proposed: remove event/program/registration machinery → a peer review platform remains (OpenReview proves the product shape); remove the review exchange → an event management system remains. Because the conference-management leaf is unprocessed, this pass does NOT resolve whether conference review systems belong to this Type, that Type, or a documented straddle — flagged for joint review when Scholarly Conference Management is processed.
3. **vs Assessment Platform (§23, processed).** Clean structural split: assessment = scored instrument → administration to a taker population → response capture → evaluation → attributed durable results (takers are the subjects; the instrument is the object). Peer review platform = works/applications → peer evaluators → recorded evaluation outcomes serving an organizing body's decision (the work is the object; peers are the evaluators). Different object, different evaluator relationship, different outcome semantics. No merge.
4. **vs community review surfaces (PREreview, PubPeer-class).** PREreview documented as a boundary probe: reviews of preprints by self-selected community members, published openly, with review requests and clubs — **no platform-mediated pairing, no outcome loop, no organizing body**. Fails L0 legs 2 and 4 → community commentary territory (closer to discussion/community Types), not this Type. Recorded as a boundary, not a variant.
5. **vs Code Review Platform (§12).** Same abstract shape (review exchange: changes → reviewers → comments → approve/reject) but a different domain object (code changes in version control vs scholarly/program submissions) and different operator context (engineering teams vs program committees). Name collision only; no taxonomy conflict.
6. **vs Research Grant Management (§23, unprocessed).** OpenWater's grants module shows the seam: grant management spans the full program lifecycle (application intake, funds distribution, reporting); the review exchange is its evaluation stage. When evaluation is the center → this Type; when funding administration is the center → grant management territory. Flagged as a note for that leaf's pass.
7. **Naming observation.** The market says "conference management system", "abstract management", "application & review software", "submission and review" more often than "peer review platform". The leaf name is defensible: the review exchange is the defining structure the sampled products share; everything else is packaging.

## Uncertainties

- EasyChair operational detail (exact review-form fields, assignment UI, anonymity configuration) could not be verified — help center unreachable (404); claims calibrated to official product-page level.
- CMT reviewer-assignment UI detail not fetched (two page guesses 404; abandoned per network rules) — roles, tracks, conflicts, and submission configuration are documented; assignment mechanics asserted only at "chair-driven" level.
- Indico conflict-of-interest machinery not evidenced in fetched docs — COI treated as common (5/6 documented) with Indico unverified.
- OpenWater operational depth rests on product pages (help center exists but not fetched) — association-pole claims kept at page level.
- Whether EasyChair supports journal-style workflows — not evidenced; not asserted.
- Vendor scale figures (EasyChair 4.9M users/125k conferences; CMT 12k conferences; OpenWater 750+ orgs; ConfTool 5,000+ organizers) are vendor-stated marketing claims, recorded as such.
- The exact set of venue types OpenReview supports for journals (beyond the TMLR-style path) is not documented publicly.

## Final Synthesis

A Peer Review Platform is the organized evaluation exchange: submissions (papers, abstracts, proposals, applications) enter as identified records; the platform pairs each with eligible reviewers from a managed pool under conflict-of-interest rules (assigned, bidded, or matched); each reviewer's evaluation is captured as a structured record with its own visibility policy; and the operating roles aggregate reviews into a recorded per-submission outcome — decision, ranking, or certified review report — that serves the organizing body's next action. Anonymity postures, public reviews, matching algorithms, meta-review layers, tracks, revision loops, and reviewer recognition are the common mature structure layered on this core; event machinery and journal publication pipelines are adjacent packaging, not the organizing whole. The Type is bounded against journal management (which owns the journal lifecycle with review as a stage), against conference management (which owns the event with review as a workflow — joint review flagged), against assessment platforms (instruments for takers, not works for peers), and against community review surfaces (no pairing, no outcome).
