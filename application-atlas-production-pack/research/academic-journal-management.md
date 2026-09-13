# Research Notes — Academic Journal Management

## Research Goal

Understand what software for running an academic/scholarly journal actually does: what objects exist inside it, who operates it, how a submission becomes a published article, which rules and states govern the process, and where this Application Type ends relative to neighbors (Peer Review Platform, Publishing Editorial Workflow, Institutional Repository, Scholarly Conference Management).

## Initial Boundary

Working hypothesis at start:

- Academic Journal Management = editorial-office software for a scholarly journal: receive article submissions, orchestrate editorial evaluation (typically peer review), record decisions, and move accepted manuscripts toward publication within the journal's publishing program.
- Nearest neighbors: **Peer Review Platform** (sibling leaf in §23 — highest confusion risk), Publishing Editorial Workflow (§27, trade publishing), Institutional Repository (§23), Scholarly Conference Management (§23), CMS/website hosting.
- Known market terminology: "manuscript submission system", "peer review system", "editorial management system", "journal management/publishing software". The market rarely uses the literal phrase "journal management".

## Research Questions

1. What are the core objects (journal, submission/manuscript, author, reviewer, review assignment, decision, issue, published article)?
2. What are the canonical workflow stages and statuses?
3. What roles exist, and how is editorial authority tiered?
4. How does submission intake work (wizard steps, declarations, files)?
5. How does the evaluation stage work (reviewer pool, assignment, anonymization modes, rounds, forms, recommendations)?
6. What decisions exist, and how do revisions re-enter the workflow?
7. What happens after acceptance (copyediting, production/typesetting, proofing, issue scheduling, publication, DOI/indexing)?
8. What journal-level configuration exists (sections, article types, policies, licenses, emails, access)?
9. How do multi-journal operators work (press/publisher level)?
10. Where is the boundary vs Peer Review Platform and other neighbors?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer levels:

| Product | Operator / Owner | Philosophy | Customer level |
|---|---|---|---|
| Open Journal Systems (OJS) | Public Knowledge Project (PKP) | Open source, self-hosted; full lifecycle from submission to published issues; journal website included | Universities, libraries, small/society journals; 10,000+ journals (vendor-stated) |
| Janeway | Birkbeck, University of London / Open Library of Humanities | Open source, mission-hosted; editor-first staged workflow incl. production and publishing | Library/publisher-hosted OA journals |
| Editorial Manager (EM) | Aries Systems Corporation | Commercial SaaS incumbent; manuscript submission + peer review tracking at scale; production handed downstream | Large publishers, societies, high-volume journals |
| ScholarOne Manuscripts | Silverchair | Commercial SaaS incumbent (25 years in market); submission-to-acceptance workflow management | Prestigious publishers/associations; vendor claims 3M+ submissions/year, 9,000+ journal sites |

Note: Scholastica was initially considered as a modern SaaS representative but its homepage (fetched 2026-09-06) now markets "publishing infrastructure for independent newsrooms" with no academic-journal product visible — it appears to have exited this market and was dropped.

## Sources

### Open Journal Systems (PKP) — Tier 1 (official docs, fetched via GitHub mirror)

- docs.pkp.sfu.ca is protected by an anti-bot challenge (Anubis); two fetch attempts failed. The same official documentation is maintained in the `pkp/pkp-docs` GitHub repository; chapters were fetched from there (raw + blob views).
- Learning OJS 3.5 — Editorial Workflow: submission.md, review.md, publication.md (fetched in full); copyedit.md / production.md (timeouts — not fetched; stage existence corroborated by chapter titles, the publication chapter's reference to articles "returned to the Production stage", and Janeway's equivalent stages).
- Learning OJS — Journal Managers SUMMARY (settings areas).
- pkp-docs README / index data ("flagship software for open access journal publishing, used by more than 10,000 journals worldwide").

### Janeway — Tier 1 (official docs, docs.janeway.systems)

- Documentation index (full TOC), Workflow Guides (author guide fetched in full), Editor Guide (full TOC + review/copyediting/production/proofing/pre-publication structure), Manager → Review settings (fetched in full).

### Editorial Manager (Aries) — Tier 2 (official product pages)

- Product page (positioning, roles, workflow claims, ProduXion Manager pairing).
- Ecosystem page (integration catalog: integrity checks, reviewer search, reviewer recognition, references, ROR, APC/RightsLink).
- Limitation: support.ariessys.com (operational help) unreachable (transport error). EM operational mechanics are asserted only at product-page level.

### ScholarOne Manuscripts (Silverchair) — Tier 2 (official product pages)

- Silverchair Products page and ScholarOne Manuscripts product page (positioning, workflow scope "from submission to acceptance", integrations, scale claims).
- Limitation: support.scholarone.com unreachable (transport error); support.silverchair.com not fetched. Operational mechanics asserted only at product-page level.

Research date: 2026-09-06.

---

## Product Observations

### Open Journal Systems (OJS) — evidence layer A (official docs)

**Positioning.** "Flagship software for open access journal publishing, used by more than 10,000 journals worldwide" (pkp-docs index data). Self-hosted or hosted; a journal website + editorial workflow + publishing in one system.

**Editorial workflow (Learning OJS 3.5).** Four stages: Submission → Review → Copyediting → Production, then Publication/Post-Publication.

- **Submission stage.** New submissions land here and are assigned to Section Editors — automatically (by section/category assignment rules) or manually. When assigning an editor, the assigner chooses whether the assignee can *finalize* an editorial decision or only *recommend* one, and whether they may edit publication details. A "Pre-Review Discussion" is auto-created. Desk decisions: **Send to Review**, **Accept and Skip Review** ("useful for certain types of content that don't require peer review" — direct evidence that review is a stage, not the definition), **Decline Submission** (revertable via Revert Decline).
- **Review stage.** Editors prepare files for review (anonymization is the editor's responsibility; system hides identities per review type). Review types: Anonymous Reviewer/Anonymous Author (double-blind), Anonymous Reviewer/Disclosed Author (single-blind), Open. Reviewer assignment from a reviewer list showing affiliation, number of active reviews, days since last assignment, and review history (completed/declined counts); author-suggested reviewers appear in the list; editors can create new reviewer accounts or enroll existing users. Per assignment: response due date, review due date, files to be reviewed, review type, and optionally a structured **review form** (else a default extended text box). Private editorial notes on reviewers; reviewer rating; reminders for overdue requests; cancel/unassign/reinstate. Dashboard views: All in peer review / Needs reviewers / Awaiting reviews / Reviews submitted, with per-assignment status icons (due-date countdowns, declined, cancelled, submitted-awaiting-confirmation, confirmed). Editor reads the review, can discuss with the reviewer, then **Confirms** it (thank reviewer / revert decision).
- **Decisions.** Request Revisions (with optional new review round), Accept Submission (→ Copyediting), Create New Review Round (unlimited rounds; previous reviews shown to reviewers in later rounds), Decline Submission (→ Declined view, revertable). APC/payment prompt can appear at acceptance if the journal charges fees.
- **Publication.** Editors create **Issues** (volume, number, year, title, description, cover), schedule accepted articles into issues, set section/category/pages/publication date, order the table of contents, add whole-issue galleys, preview, then **Publish Issue** (optional reader notification). Unpublish/delete returns articles to the Production stage.
- **Post-publication.** Published metadata/galleys are immutable; substantial changes (retractions, content changes, contributor changes) require creating a new **version**; versions are listed publicly with outdated-version warnings; DOI/Crossref deposits are not auto-updated. Statistics on articles/readership.

**Journal management (Journal Managers guide).** Settings areas: basic journal info; submission settings & author guidelines; review settings; copyright/licensing; users & roles (permissions, ORCID); communications (announcements, role-targeted email, automated email templates); content access (site access, distribution); theme/display; archiving & SEO; DOIs; import/export; publisher library.

### Janeway — evidence layer A (official docs)

**Positioning.** Open source journal platform developed/maintained by Birkbeck, University of London and the Open Library of Humanities; guides cover "running articles through the workflow, configuring journals and setting up an install".

**Workflow (Workflow Guides).** Stages visible in guides: submission (author) → review → revisions → copyediting → production (production manager + typesetter + galleys) → proofing → pre-publication → published. Role guides exist for Author, Editor, Reviewer, Copyeditor, Typesetter, Proofreader.

- **Submission (author guide).** 5-step wizard with a timeline bar: Author Agreement (publication fees/APC disclosure, submission checklist, copyright notice, competing interests, comments to the editor — configurable, some required) → Article Information (title, subtitle, abstract, language, **section** = article type e.g. Research/Review/Editorial, license, keywords; journals can add custom fields) → Author Information (add co-authors by ORCID/email search or manually; ROR-linked affiliations; author ordering; corresponding author) → Article Files (one manuscript file + labeled figure/data files) → Review (confirmation page).
- **Review (editor guide).** Unassigned articles queue; review page with rounds (add/delete round); add reviewer; manage reviews; make reviews available to authors (per-answer visibility control, editable answers); **Decision Helper**; request revisions; **draft a decision**; sharing peer reviews (share-reviews decision, display completed reviews in later rounds, share author response letters); **triple-anonymous peer review** mode with anonymization areas.
- **Review settings (manager).** Review guidelines; default review visibility (Open / Anonymous / Double Anonymous); default review days (initially 56 — vendor default); one-click access tokens for reviewers; **draft decisions** (section editors recommend; senior editors accept); open peer review (reviews public with reviewer consent + editor selection at pre-publication); default review form; reviewer form download (DOCX offline); save review progress; accept-article warning with Crossref registration preview; controls for what review data authors see.
- **Review forms.** Form builder: elements (text field/area, checkbox, select, email, upload, date), required flag, ordering, width, per-element default visibility to authors; preview.
- **Copyediting.** Editor assigns copyeditor(s); author participates in copyediting rounds (tracked changes; author accepts changes, answers queries, uploads revised file, decision "Accept"/"Corrections Required"); multiple rounds.
- **Production.** Assign production manager; assign typesetter; upload **galleys**; typesetting plugin can generate typeset files (XSL/CSS); manage/replace typeset files.
- **Proofing.** Assign proofreaders (incl. author proofing); preview rendering of HTML/PDF/XML; notes or annotated files; correction rounds; acknowledge.
- **Pre-publication.** View metadata → set issue → verify DOIs → select galley for rendering → set publication date → select article image → notify author.
- **Published content.** Articles (metadata, galleys, issues, publisher notes, identifiers), Issues (issue types, TOC management), publication schedule. DOI manager + Crossref settings; Crosscheck (iThenticate) settings. Press manager for multi-journal operation; repository framework (preprints) as a separate subsystem; metadata standards ROR + CRediT.

### Editorial Manager (Aries) — evidence layer B (official product pages; operational docs unreachable)

- Positioning: "industry leading, cloud-based **manuscript submission and peer-review tracking system** for scholarly journals, reference works, books and other publications"; "highly-configurable workflow management system"; "trusted by thousands of publications across hundreds of multinational publishers, societies, and organizations".
- Roles (product page): **Authors** — submit manuscripts and supplemental files, act on revision requests, track manuscript status. **Editors** — process submissions, use quality check tools, assign and manage reviewers, set final disposition. **Reviewers** — manage peer review invitations/assignments, submit review commentary, optionally receive credit for contributions.
- Customizable workflows "at any time through flexible configuration settings".
- **Production is downstream**: "EM seamlessly connects with downstream systems, such as Aries' ProduXion Manager® (PM), to provide a comprehensive workflow solution **beyond peer review**" — i.e., EM's own scope is submission → peer review → editorial decision; production/publishing is a separate product or publisher-side system.
- Reporting suite ("Editorial Intelligence") for editorial decisions and strategies; client quotes mention tracking editor performance, custom reports, reviewer search and letter customization.
- Ecosystem integrations: research integrity (image manipulation, paper-mill detection, plagiarism/AI-generation detection, reference checking), reviewer search (Scopus, Web of Science, Prophy), reviewer recognition (ORCID, ReviewerCredits), ROR identifiers, APC management (RightsLink).
- Enhanced Researcher Experience (powered by ChronosHub): centralized author dashboard, journal catalog, recommendation services across a publisher's portfolio.

### ScholarOne Manuscripts (Silverchair) — evidence layer B (official product pages; operational docs unreachable)

- Positioning: "comprehensive **workflow management** solution used by millions of researchers... for 25 years"; "SaaS-based submission management platform"; "highly configurable workflows... **from submission to acceptance**".
- Stated workflow scope: "best practice workflows across the full lifecycle of the manuscript review process — including **submission, pre-review screening, administrative checklists, assignment of editors, selection of peer reviewers, recommendations, and final decision**".
- Integrations: Crossref, ORCID, Copyright Clearance Center, Ringgold; research-integrity tooling ("filter out predatory journals and plagiarized work"); reviewer finding/screening.
- Vendor-stated scale: 3M+ manuscripts processed/year, 9,000+ journal sites, 1.1M average monthly active users, "over 20% of the world's scholarly journals" (marketing claims — recorded as vendor claims, not verified).
- **ScholarOne Conferences** is a separate sibling product for event/abstract management — vendor-confirmed structural split between journal workflow and conference workflow.
- ScholarOne Gateway: centralized hub giving researchers/reviewers a unified view across a publisher's entire portfolio (vendor-specific).

---

## Cross-product Comparison

| Dimension | OJS | Janeway | Editorial Manager | ScholarOne |
|---|---|---|---|---|
| Journal as container with config | Yes (settings: policies, sections, licenses, emails, access, theme) | Yes (journal settings, review settings, content, licenses) | Yes (per-journal configurable workflows) | Yes (per-journal configurable workflows) |
| Submission record (files + metadata + authors) | Yes | Yes (5-step wizard) | Yes ("submit manuscripts and supplemental files") | Yes (submission + administrative checklists) |
| Author portal (submit, track status, revise) | Yes | Yes | Yes (product page) | Yes (implied; Gateway hub) |
| Tracked staged workflow | Yes (Submission → Review → Copyediting → Production) | Yes (submission → review → copyediting → production → proofing → pre-publication) | Yes (configurable; submission + peer review tracking) | Yes (submission → screening → editors → reviewers → recommendations → decision) |
| Desk decision before review | Yes (Send to Review / Accept and Skip Review / Decline) | Yes (unassigned-article queue; editor triage) | Yes ("process submissions", quality check tools) | Yes ("pre-review screening") |
| Peer review stage | Yes (stage; skippable for non-reviewed content) | Yes (stage; draft decisions possible) | Yes (core of product) | Yes (core of product) |
| Anonymization modes | Double-blind / single-blind / open | Open / single / double / triple-anonymous | Configurable (peer review invitations; specifics not verified) | Configurable (not verified in detail) |
| Reviewer pool with history/workload | Yes (active reviews, completed/declined, last assignment) | Yes (reviewer management; interests) | Yes ("assign and manage reviewers") | Yes ("find, screen and connect with reviewers") |
| Review forms (structured) | Yes (optional; default free text) | Yes (form builder with element types) | Yes (review commentary; specifics not verified) | Yes (recommendations; specifics not verified) |
| Multi-round review | Yes (unlimited rounds; prior reviews visible) | Yes (rounds; prior reviews shareable) | Yes (revision requests; specifics not verified) | Yes (recommendations → decision; specifics not verified) |
| Revision loop (author uploads revised files) | Yes | Yes (minor/major revisions) | Yes ("act on revision requests") | Yes (within review lifecycle) |
| Decision set | Accept / Request Revisions / Decline / new round | Accept / revisions (minor/major) / decline; draft decisions | "Set final disposition" | "Recommendations, and final decision" |
| Decision correspondence | Yes (email templates, notify author/reviewers) | Yes (email templates, decision letters) | Yes (customizable letters per client quote) | Yes (workflow communications) |
| Copyediting stage | Yes | Yes (copyeditor role, tracked changes) | Not in EM scope (downstream) | Not in S1 scope (downstream) |
| Production/typesetting/proofing | Yes (Production stage; galleys) | Yes (production manager, typesetter, proofreader, galleys) | Downstream (ProduXion Manager is a separate product) | Downstream (publisher's platform) |
| Issue management (volume/number, TOC) | Yes (create/schedule/publish issues) | Yes (issue manager, set issue at pre-publication) | Not evidenced in EM scope | Not evidenced in S1 scope |
| Journal website / publishing host | Yes (full site, themes, announcements) | Yes (full site, news, contacts) | No (links to publisher platforms) | No (links to publisher platforms) |
| DOI / Crossref registration | Yes (DOI plugin, Crossref export) | Yes (DOI manager, Crossref settings, registration preview) | Integration ecosystem (Crossref) | Yes (Crossref integration) |
| Integrity screening | Plugin ecosystem (iThenticate guide exists in pkp-docs) | Crosscheck settings (iThenticate) | Ecosystem: image manipulation, paper mills, plagiarism, references | "Filter out predatory journals and plagiarized work" |
| Reviewer discovery/recognition | Reviewer history in-product; ORCID support | Reviewer management; ORCID login | Ecosystem: Scopus/WoS/Prophy search; ORCID/ReviewerCredits recognition | "Find, screen and connect with reviewers"; ORCID |
| Editorial analytics/reporting | Statistics (articles/readership) | Expanded review details; dashboards | "Editorial Intelligence" reporting suite | Workflow management at scale (reporting implied) |
| Multi-journal operation | Yes (site admin hosts many journals; press context) | Yes (Press Manager) | Yes (publisher portfolio; Enhanced Researcher Experience across portfolio) | Yes (publisher portfolio; Gateway hub) |
| Access/subscription control for published content | Yes (content access settings) | License manager; OA focus | Publisher-side | Publisher-side |
| APC / payment handling | Yes (payments at acceptance) | Yes (publication fees in submission) | Ecosystem (RightsLink APC) | Copyright Clearance Center integration |
| Open/published peer review | Not evidenced in fetched chapters | Yes (open peer review with consent) | Not evidenced | Not evidenced |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as academic journal management:

1. **Journal as governing container** — a recurring scholarly publication with its own identity, editorial governance, and configuration (policies, sections, roles). Operations happen *on behalf of a journal*.
2. **Submission record** — a proposed work entering the system: manuscript files + bibliographic metadata + author attribution, created by the author (or recorded by staff).
3. **Tracked staged editorial workflow** — each submission moves through named, status-tracked stages operated by editors; its state is visible to the participants who need it.
4. **Editorial evaluation → recorded decision** — the submission is evaluated (in practice, almost always by external peer review) and a decision (accept / revise / decline) is recorded and communicated to the author.
5. **Publication as the workflow's destination** — accepted works become published articles of the journal (published inside the system, or handed off to a downstream production/publishing system as a structured handoff).

Historical check: ScholarOne Manuscripts has run this same core for ~25 years (submission → screening → editor assignment → reviewer selection → recommendations → decision), and OJS has run submission → review → copyediting → production → issues since 2001. Subscription-era society journals (EM/ScholarOne's base) and open-access journals (OJS/Janeway's base) both satisfy this definition; nothing in L0 depends on open access, APCs, DOIs, or modern AI tooling.

Deliberately **not** in L0 (despite being near-universal): peer review machinery (it is the standard evaluation mechanism but OJS explicitly supports "Accept and Skip Review" for content that does not require peer review, and desk decisions exist everywhere), issues/volumes, copyediting/production stages, journal website hosting, DOIs, plagiarism screening, ORCID.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Peer review machinery**: reviewer pool with history/workload signals; assignments with response/review due dates and reminders; anonymization modes (single/double/open at minimum); structured review forms or free-text reviews; multi-round review with prior reviews visible; editor confirmation of reviews; reviewer thanking/recognition.
- **Role-differentiated portals**: author dashboard (submit, track status, upload revisions, copyedit/proof responses), reviewer dashboard (invitations, assignments, complete reviews), editor dashboards with work queues (needs reviewers / awaiting reviews / reviews submitted).
- **Tiered editorial authority**: editors who recommend vs editors who decide (OJS assignment option; Janeway draft decisions; EM "set final disposition" at senior level).
- **Decision correspondence**: templated email system driving every transition; decision letters; optional reviewer notification.
- **Revision loop**: revision requests (minor/major), revised-file upload, re-review.
- **Post-acceptance stages** (in full-lifecycle products): copyediting, production/typesetting, proofing, galleys.
- **Issue management & scheduling** (in full-lifecycle products): volume/number/year containers, TOC ordering, publication dates.
- **Journal website / publication hosting** (in full-lifecycle products): public article pages, issues, announcements.
- **Integrity screening**: plagiarism/similarity checks at minimum; increasingly image manipulation, paper-mill and reference checks (native or via integrations).
- **Metadata & identifier infrastructure**: ORCID, ROR, licenses, keywords, DOI/Crossref registration.
- **Editorial analytics**: submission/review turnaround statistics, editor performance, custom reports.
- **Multi-journal operation**: press/publisher-level management of many journals; portfolio-level author/reviewer hubs.

### L2 — Variant / Optional Structure

Depends on market segment, publisher model, or deployment:

- **Where production/publishing happens**: in-system (OJS, Janeway) vs downstream handoff to a production/publishing platform (EM, ScholarOne) — the deepest structural variant in the sample.
- **Access model of published content**: open access vs subscription/controlled access (OJS content-access settings; EM/S1 publisher-side).
- **APC / payment processing**: at submission (Janeway), at acceptance (OJS), via rights/licensing integrations (EM ecosystem).
- **Open/published peer review**: reviews published with reviewer consent (Janeway); not present in all products.
- **Anonymization depth**: up to triple-anonymous review (Janeway).
- **Reviewer suggestion by authors**; reviewer search services; reviewer credit/reward schemes.
- **Preprint/repository integration** (Janeway repository framework).
- **Conference/proceedings handling** (separate sibling products: ScholarOne Conferences; OJS ecosystem historically).
- **Multilingual operation** (OJS multilingual guide; Janeway translations).
- **AI assistance**: integrity checks, reviewer matching, quality checks (emerging; mostly integration-level today).

### L3 — Vendor-specific (research notes only)

- OJS: PKP preservation network, QuickSubmit plugin, versioned docs, specific dashboard status-icon system, "Login As" (logged), section/category-based auto-assignment of editors.
- Janeway: one-click access tokens (UUID4, deleted after use), 56-day default review window, typesetting plugin (XSL/CSS galleys), Crossref registration preview on accept, per-element review-form visibility control.
- Editorial Manager: Enhanced Researcher Experience (ChronosHub), ProduXion Manager pairing, quality check tools, "Editorial Intelligence" branding.
- ScholarOne: ScholarOne Gateway portfolio hub, ScholarOne Conferences sibling, vendor scale claims (3M+/year, 9,000+ sites, 1.1M MAU, "20% of world's journals", "more than half the world's scholarly output" for S1+S1 Conferences).

## Vendor-specific Findings / Rejected Findings

- **Rejected from core**: "journal management includes subscription/circulation management" — only OJS shows content-access settings in the fetched evidence; circulation/subscription fulfillment is a publisher-side concern in the commercial sample. Kept as L2 (access model), not core.
- **Rejected from core**: "peer review is the definition" — contradicted by OJS's explicit "Accept and Skip Review" and desk-decision paths in all four products.
- **Rejected from core**: "the system publishes the journal website" — false for the two commercial incumbents, which hand off downstream.
- **Rejected**: precise numeric claims (review-day defaults, scale figures) — vendor-stated only; kept out of the canonical document.
- **Rejected**: "AI is part of the workflow" — currently integration-level; not structural.

## Boundary Findings

1. **vs Peer Review Platform (sibling leaf, §23) — the critical boundary.** In all four sampled products, peer review is a *stage inside* the journal's editorial workflow, not the whole system. The journal management system's center of gravity is the full submission → evaluation → decision → publication lifecycle plus journal-level configuration (sections, policies, issues, roles). A standalone peer review platform would center on the review exchange itself (reviewer assignment, review reports, review completion) as the primary object, potentially submission-agnostic or conference-oriented. Structural test: remove review → journal management survives (desk decisions, non-reviewed sections, production/publishing continue — OJS evidence); remove everything except the review exchange → a peer review platform remains. The two commercial incumbents market themselves as "submission and peer review" systems — they are the review-heavy end of *this* Type. **Flag for joint review when Peer Review Platform is processed**: probable overlap/capability relationship; the directory may intend Peer Review Platform to mean review-exchange-centric products (including conference abstract review).
2. **vs Scholarly Conference Management (§23).** Conference abstract/paper collection and review plus event logistics is a distinct Type; Silverchair ships ScholarOne Conferences as a separate product from ScholarOne Manuscripts — vendor-confirmed structural split.
3. **vs Publishing Editorial Workflow (§27).** Trade publishing editorial (acquisitions, contracts, book/magazine production) has different objects (titles, contracts, ISBNs) and no peer-review/issue/DOI machinery. Related but distinct.
4. **vs Institutional Repository (§23).** Repositories store and expose already-published works or preprints without an editorial decision workflow. Janeway ships a separate "repository framework" for preprints alongside its journal workflow — same-vendor evidence that the two are different structures.
5. **vs CMS / website builder.** Full-lifecycle products host the journal website, but the website is an output surface of the editorial workflow, not the core; stripping the workflow leaves a plain CMS, which is not this Type.
6. **Naming observation.** The market calls this category "manuscript submission system", "peer review system", or "editorial management system" more often than "journal management". The leaf name is defensible (the system manages the journal's editorial operation) but should be documented with the common synonyms.

## Uncertainties

- Editorial Manager and ScholarOne operational detail (exact stage names, statuses, permission granularity) could not be verified from Tier-1 documentation (support sites unreachable). Claims for these two products are calibrated to product-page level.
- OJS copyediting/production chapter details were not fetched (network timeouts); stage existence is corroborated by chapter titles, the publication chapter's "returned to the Production stage" reference, and Janeway's equivalent stages.
- Whether EM/ScholarOne offer any in-system issue composition — not evidenced; assumed downstream.
- Market-share figures are vendor-stated and unverified.
- The exact current ownership chain of ScholarOne (Clarivate → Silverchair era) was not independently verified beyond Silverchair's own product pages.

## Final Synthesis

Academic Journal Management is the editorial-office system of record for a scholarly journal. Its world is organized around a **journal** (governing container with policies, sections, and roles), **submissions** (manuscript + metadata + authors) that move through a **tracked staged workflow** operated by tiered editors, an **evaluation** step that in practice means external peer review (reviewer pool, assignments, rounds, recommendations), a **recorded editorial decision** with correspondence, and **publication** of accepted works as the journal's articles — either inside the system (issues, galleys, website, DOIs) or via a structured handoff to downstream production/publishing systems. Peer review machinery, copyediting/production stages, issue management, hosting, integrity screening, identifier infrastructure, analytics, and multi-journal operation are the common mature structure layered on this core; access models, payments, open review, and AI assistance are variants. The deepest structural variant is where the publication pipeline ends: full-lifecycle systems publish in-system, while the dominant commercial incumbents end at acceptance and hand off downstream.
