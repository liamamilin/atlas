# Research Notes — Knowledge Base Application

## Research Goal

Understand the Application Type behind the directory leaf **Knowledge Base Application** (§02.06 Wiki & Knowledge Base): what a "knowledge base application" actually is as a structure, who operates and reads it, how its corpus is organized and kept current, and where it separates from its three closest siblings — Help Center (processed), Enterprise Wiki (processed), and Wiki Application (unprocessed) — plus the adjacent processed Types (Self-service Support Portal, Internal Knowledge Search, Intranet Platform, Enterprise Content Management).

This pass also carries **two joint-review obligations** recorded by earlier passes:

1. **help-center (§02.06, processed 2026-09-07)** proposed a seam for this pass: Help Center = external-facing support publication vs Knowledge Base Application = internal curated corpus; keep-both recommended; packaging must not drive the boundary.
2. **enterprise-wiki (§02.06, processed 2026-09-07)** flagged real market-language blur (products self-label "knowledge base") and proposed the discriminator curated/owned/review-managed answer set vs emergent member-maintained corpus; joint review recommended.

## Initial Boundary

Working hypothesis before research:

- A knowledge base application is a system for building and maintaining a **curated, organized corpus of articles that answer questions** — with authoring, ownership, review/publish lifecycle, and retrieval.
- Closest confusions: (a) Help Center — the market sells external-facing support publications as "knowledge base software"; (b) Enterprise Wiki / Wiki — products self-label as knowledge bases while structurally remaining wikis; (c) note-taking/PKM — personal knowledge tools; (d) document repositories — files with search but no answer-oriented curation.
- Open question going in: is the KB Type defined by its **audience** (internal) as the help-center pass proposed, or by its **machinery** (curated corpus + governance), with audience as a variant axis?

## Research Questions

1. What is the unit of knowledge (article/card/page), and what does "curated" mean operationally (authorship, ownership, review)?
2. How is the corpus organized (categories/hierarchy/tags/workspaces) and retrieved (search/browse/AI answers)?
3. What lifecycle do articles pass through (draft → review → publish → verify → update → retire), and how does that machinery differ across generations and segments?
4. Who uses it — operators (authors, reviewers, knowledge managers, admins) vs readers (employees, customers) — and how do the two planes relate?
5. How do audience and visibility work (public vs restricted; per-article/category; internal vs external corpora; dual-audience tools)?
6. What feedback/analytics machinery exists (views, search terms, gaps, verification status), and what loops does it feed?
7. How does the corpus reach its readers (published site, in-app widget, browser extension, chat bots, AI agents)?
8. Where are the boundaries: wiki (open editing), help center (support publication), docs portal (release-versioned genre), PKM (personal), ECM (records), intranet (comms estate), internal knowledge search (discovery layer)?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Philosophy | Evidence depth |
|---|---|---|---|
| Document360 | standalone "knowledge base software" pure-play | authoring/workflow/governance-first; dual-audience by design | A (deep official docs) |
| Guru | internal knowledge-management platform | verification-first ("knowledge health"); AI agents; delivery in workflow | A (deep official docs) |
| Zendesk (Knowledge/Guide) | help-desk-suite component | knowledge embedded in the support operation; internal + external KBs as one machinery | A (official help articles) |
| KBPublisher | legacy self-hosted KB application (open-source lineage) | classic two-plane KB: public area + admin area | A (official user manual, operational level) |
| Tettra | internal KB for SMB teams | Slack-first delivery; verification automation | B (product-page level) |

Market-structure context (Tier 2, third-party framing): Zendesk's own "Best knowledge base software" guide (2026) typologizes the category as **internal / external / both** and lists Zendesk, Knowmax, Slab, Nuclino, Freshworks, Bloomfire, Document360, Help Scout, Crescendo, Slite — used only to confirm market structure, not for product claims about the listed vendors.

## Sources

Research date: **2026-09-08**

- Document360 — official documentation site (docs home, llms.txt index, Organizing your knowledge base, Managing workflow status, Article access control): https://docs.document360.com/ , https://docs.document360.com/llms.txt , https://docs.document360.com/docs/organizing-your-knowledge-base , https://docs.document360.com/docs/managing-workflow-status , https://docs.document360.com/docs/article-access-control-knowledge-base-site
- Guru — official help center (How content is verified in Guru; Managing permissions): https://help.getguru.com/ , https://help.getguru.com/docs/verifying-and-unverifying-cards , https://help.getguru.com/docs/guru-roles-admin-collection-owner-author-read-only
- Zendesk — official support documentation (Best practices for creating an internal knowledge base; Understanding Knowledge user permissions for knowledge base access; plus the help-center pass's category/section/arrange articles): https://support.zendesk.com/hc/en-us/articles/4408821238938 , https://support.zendesk.com/hc/en-us/articles/4408827797274 , https://support.zendesk.com/hc/en-us/articles/4408845897370 , https://support.zendesk.com/hc/en-us/articles/4408824317594
- Zendesk — product marketing guide "Best 10 knowledge base software for 2026" (market typology only): https://www.zendesk.com/knowledge-base/
- KBPublisher — official product site and 8.0 User Manual (operational level): https://www.kbpublisher.com/ , https://www.kbpublisher.com/kb/user-manual-v60-1/
- Tettra — official product site (positioning level): https://tettra.com/

> Sourcing limitations: Zendesk's Help Center search API returned results but two intended deep fetches were limited to the two articles above; Zendesk plan-gating (Enterprise-only features) is recorded as observed plan references, not asserted as Type structure. Tettra's help center (support.tettra.co) was not fetched; Tettra evidence stays at product-page level. Bloomfire/Slab/Slite/Crescendo/Nuclino/Help Scout were observed only through Zendesk's third-party market guide and are used solely as market-structure evidence. The ITSM-segment KB (ServiceNow, Freshservice) was not directly sampled; claims about that segment are kept weak. No pricing, plan entitlements beyond observed plan references, or numeric limits are asserted in the final document; observed numbers live only in these notes.

## Product A — Document360 (standalone KB software pure-play)

### Key observations (evidence layer A unless noted)

- Self-positioning: "create knowledge bases, API docs, SOPs, and deploy AI chatbots — all in one powerful platform"; the docs home markets "structured workflows, powerful editing tools, and built-in governance" for the knowledge base.
- **Five-level hierarchy**: Project → Workspace → Language → Category → Article. A workspace is "a separate, self-contained knowledge base" with its own content tree, URL, and visibility (public / beta / deprecated). Categories have types (Folder, Index, Page) and nest into subcategories. Articles are "the core building blocks" and "follow a draft-to-published workflow".
- **Audience-as-structure rule** (official best-practice guidance): use a new *workspace* when "the audience is completely different and you'd never want both groups searching the same content"; use a new *category* when "it's the same audience, just a different topic". Direct vendor articulation of the audience axis as configuration, not identity.
- **Workflow machinery**: workflow statuses configured in a Workflow designer (e.g., draft → peer review → SME review); per-article assignees, due dates, comments, workflow history; read-only statuses block direct publishing; a Tasks page aggregates assigned articles with tabs Workflow / Feedback / Review reminder; bulk status updates; per-language workflow states. Article statuses include New, Draft, Published, Needs review.
- **Publication lifecycle**: publish, schedule publishing, unpublish, delete (recycle bin with 30-day restore window), mark as deprecated, hide/unhide; revision history (editing a published article creates a new unpublished version); article lock during editing.
- **Two access planes**: portal users (team accounts: Editor, Draft writer, Reviewer, SEO Optimization Specialist, Localization manager/administrator; user groups) vs knowledge-base-site readers (reader accounts, reader groups). Projects are public, private, or mixed; per-article and per-category access with deny overrides and inheritance blocking. Direct evidence that one tool serves both an operator plane and an external reader plane.
- **Feedback & analytics**: article analytics (reads, views, likes/dislikes), feedback manager (article-level and AI-response feedback), search analytics including no-result searches, health-check metrics, read receipts (reader acknowledgement).
- **Retrieval**: search plus "Ask Eddy" AI assistive search (answers grounded in the KB), AI-related-article recommendations, tags/labels, glossaries, related articles, decision trees as guided retrieval.
- **AI layer**: Eddy AI writer suite (draft generation, translation, SEO descriptions, tag/title recommenders), AI chatbots over KB sources with ticket escalation to Zendesk/Freshdesk, MCP server exposing the KB to external AI assistants.
- **Reuse machinery**: snippets, variables, templates, drive (central media/file store), clone/replicate articles.
- Enterprise posture: SSO (SAML/OIDC/JWT), SCIM, RBAC, audit trail, private hosting, IP restriction.

## Product B — Guru (internal knowledge-management platform)

### Key observations (evidence layer A)

- Unit of knowledge: the **Card**; organization: Collections → Folders → Cards; additional objects: Pages (doc-style), **Sources** (external systems — Google Drive, Confluence, SharePoint — indexed alongside native cards), **Knowledge Agents** (AI assistants over the corpus).
- **Verification as the central knowledge-health mechanism**: every Card carries a trust status (Verified ✅ / Unverified ❔ / no badge), a designated **verifier** (person or Group), a **verification interval** (30/60/90 days, 6 months, 1 year, or "does not expire"), and last-verified metadata. Verification status "appears everywhere content is used: in search results, AI-generated answers … and when browsing".
- **AI-maintained currency**: Knowledge Agents run daily automated verification using behavioral rules (thumbs up/down, views, copies, feedback) and content-based rules (dates, time-sensitive info); unverification rules run before verification rules; a 7-day cooldown; decisions logged in a Quality Log with confidence and reasoning; humans can override. Auto-unverify off by default.
- **Human verification workflow**: Tasks → Unverified Cards queue ("Up First" curated list); editing a Card without being the verifier makes it unverified and triggers a verification request; any user can flag problem text via comments; "Check Quality" runs an agent evaluation on demand.
- **Roles/permissions**: 2-step model — roles (Admin workspace-level; Creator; Owner object-level; Viewer; custom roles) assigned to users/groups across objects (Collections, Folders, Cards, Pages, Sources, Agents). Card permissions include create drafts, publish, archive, delete, verify/unverify, comment, announce.
- **Delivery in workflow**: browser extension ("Use Guru where you work" — search Guru without leaving other tools); Answers (AI answers from linked sources); Slack/Teams integrations.
- Analytics: user/author/card analytics; verification activity monitoring (Source Verification Manager).
- Positioning: internal/team knowledge; no external customer-facing publication surface observed in the fetched docs.

## Product C — Zendesk Knowledge/Guide (help-desk-suite component)

### Key observations (evidence layer A)

- **Internal and external KBs as one machinery**: "You can think of an internal knowledge base as serving the same need as an external one — if there is a question that many employees ask … take the pressure off Support by adding this content to a knowledge base." Internal content: HR/legal processes and policies, IT instructions, presentations, sales collateral, design templates, support-use docs.
- **Audience/visibility as configuration**: single shared help center (internal + external content in one hierarchy, separated by user-segment view permissions) vs multibrand help centers (physically separate sites per audience); Zendesk itself moved from multibrand to a single shared help center so staff "can search across all articles, whether they were internal or external".
- **Permission model**: view permissions (internal + external users) vs management permissions (internal only); built on **user segments** (signed-in users; agents and managers; custom segments by tags/organizations/groups); applied **at the article level** (up to 10 segments per article); management permissions define editing vs publishing rights (managers by default; editors-and-publishers split on Enterprise).
- **Governance machinery**: article owners; verification with reminders (Enterprise); review cadence; scheduled unpublishing for content with a shelf life; **Team Publishing** workflows (review → approve → publish, Enterprise); agents contribute articles from the Agent Workspace Knowledge panel; agents flag outdated content.
- **Feedback/analytics loops**: article views, votes, subscriptions, comments; search-term analysis; "Analyzing your help center knowledge base activity"; Knowledge activity in tickets (agent engagement targets); content seeded from top internal tickets (KCS-style practice).
- Structure: categories → sections (→ subsections on Enterprise); article lists as curated views; labels; translations; archiving (soft removal) vs permanent deletion.
- Suite context: the knowledge base powers the help center, AI agents, and agent-side knowledge search; contact affordances hand off to the support operation (help-center pass evidence).

## Product D — KBPublisher (legacy self-hosted KB application)

### Key observations (evidence layer A — official 8.0 User Manual, operational level)

- Self-labels: "Knowledge Management Software" / "Knowledge base"; dual-audience positioning: "Better Customer Support" (self-serve, reduce call volume), "Improved Employee Support" (internal KB, faster training, retained knowledge), "Centralized Knowledge Repository" (user manuals, policies, project documents, training materials).
- **Two-plane architecture**: Public Area (front-end, readers) vs Admin Area (back-end, operators) — the classic generation's realization of the operator/reader split.
- **Corpus machinery**: categories (with category types and best-practice guidance), articles (input screen, HTML editor, pictures, attachments, related articles, article history, autosave, edit locking, bulk update, import), **custom article statuses and types**, **drafts with approve/reject**, **workflows** (create/edit workflows, workflow examples), featured articles, **required reading (Must Read)** with reports.
- **Feedback loop**: article comments, ratings, feedback subjects, reply-to-feedback, and "Add an article as a result of user feedback" — the feedback→new-article loop documented in the legacy generation.
- **Users & governance**: user roles, privileges, companies, API keys; private articles; private files.
- **Retrieval**: search (with advanced search, spell suggest, search-in-files via Sphinx), tags/labels, glossary, RSS feeds, site map.
- **Measurement**: usage reports, views reports, user activity, statistics, **search-query tracking** (logs what readers searched for).
- **Automation**: scheduled tasks, incoming-email automation, email notifications, letter templates.
- Authentication breadth for its era: SAML SSO, LDAP, remote auth, social login.
- The vendor runs its own manual *on* KBPublisher (dogfooding) — the manual is itself a KB with categories, articles, news, downloads, glossary.

## Product E — Tettra (internal KB, SMB teams)

### Key observations (evidence layer B — product-page level)

- Self-labels: "AI Internal Knowledge Base & Knowledge Management"; headline promise: "Stop answering repetitive questions in Slack".
- Corpus: create pages in a simple editor **or** ingest existing content (Google Docs, Notion, local files) — corpus aggregation from heterogeneous sources.
- **Delivery in workflow**: AI bot (Kai) answers questions in Slack channels/DMs from the KB; if no answer exists, routes to the right person.
- **Knowledge-health automation**: subject-matter experts "regularly verify the accuracy of important pages", knowledge-gap identification, approval of suggested edits from teammates.
- Use cases: entire companies, support teams, agencies, HR/operations — internal audiences.

## Cross-product Comparison

| Dimension | Document360 | Guru | Zendesk | KBPublisher | Tettra |
|---|---|---|---|---|---|
| Unit of knowledge | Article | Card (+ Pages, Sources) | Article | Article | Page |
| Organization | Workspace → Language → Category tree | Collection → Folder | Category → Section (→ subsection) | Category tree | Collections/pages |
| Restricted authorship | Yes (content roles; reader plane separate) | Yes (roles; verify permission) | Yes (management permissions; user segments for view) | Yes (roles/privileges; public vs admin area) | Yes (SME verification; suggested edits) |
| Question-oriented retrieval | Search + AI answers + browse + decision trees | Search + AI Answers + browse | Search + browse + article lists | Search + browse + tags + glossary | Search + AI bot answers |
| Publish/review lifecycle | Workflow designer, statuses, due dates, Tasks page | Draft → publish; verification states | Team Publishing (review/approve/publish); drafts | Drafts with approve/reject; custom statuses; workflows | Suggested-edit approval; verification |
| Currency machinery | Review reminders, deprecation, unpublish | Verification intervals + AI auto-verify | Owners + verification reminders + scheduled unpublish | Article history; Must Read; feedback loop | SME verification automation |
| Feedback | Likes/dislikes, feedback manager | Thumbs, comments, flags | Votes, comments, subscriptions | Comments, ratings, feedback→article | Suggested edits |
| Analytics | Views, search terms, no-result searches, health metrics | User/author/card analytics | Views, votes, search terms, Knowledge activity | Views, usage, search-query logs | Gap identification |
| Audience axis | Dual by design (public/private/mixed; workspaces per audience) | Internal | Internal + external in one machinery | Dual by positioning | Internal |
| Delivery surfaces | KB site, widgets, AI chatbots, MCP | Extension, Slack/Teams, AI answers | Help center, Agent Workspace, AI agents | Public site, RSS | Slack bot, web app |
| Corpus aggregation | Import (Word/PDF), migration | External Sources indexed | Agent-contributed articles; macros/tickets as sources | Import articles/files/users | Google Docs/Notion ingestion |
| AI layer | Deep (writer, search, chatbots, MCP) | Deep (agents, auto-verify, answers) | AI builder, generative search, copilot (EAP) | None observed | AI bot answers |

**Stable across all five** (evidence layer B): curated article corpus with restricted authorship; deliberate organization (categories/hierarchy) plus retrieval (search/browse); a governed publish/update lifecycle; an operator/reader separation; feedback and measurement loops feeding corpus maintenance; ownership/accountability for content.

**Variable across the sample**: audience (internal/external/dual), packaging (standalone/suite/legacy self-hosted), verification machinery depth, AI depth, delivery surfaces, corpus aggregation.

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures. If any one is removed, the product stops being recognizable as a knowledge base application:

1. **The curated article corpus** — a persistent body of individually addressable articles, each holding one piece of the organization's own knowledge (an answer, how-to, policy, procedure, reference); authorship restricted to designated contributors. Remove → open member editing makes it a wiki; member-generated answers make it a community Q&A.
2. **Question-oriented organization and retrieval** — the corpus is deliberately structured (categories/hierarchy, tags) and retrievable (search/browse) so that a question maps to its answer. Remove → a document repository or shared drive with files.
3. **Governed currency** — articles are owned and pass through a managed lifecycle (draft → review/approval → published → updated → retired); keeping the corpus current is an explicit responsibility, not drift. Remove → a stale archive that no longer functions as a base of answers.

Jointly-held is load-bearing: 1+2 without 3 = a categorized document dump; 2+3 without 1 = a workflow tool with no corpus; 1+3 without 2 = a pile of governed documents with no answer retrieval.

### L1 — Common Mature Structure

Present in most mature products; makes the corpus maintainable and findable but does not define the Type:

- authoring environment (rich/markdown editor, templates, media, snippets/variables)
- draft → review → publish workflow (statuses, reviewers, due dates, scheduled publishing)
- version/revision history; soft retirement (unpublish/archive/deprecate) with restore
- search (increasingly AI answers grounded in the corpus)
- feedback (ratings/votes/comments) and analytics (views, search terms, no-result searches, content gaps)
- visibility & access control (public vs restricted; per-article/per-container; reader vs team planes)
- roles & permissions (admins, editors, authors, reviewers; reader groups/user segments)
- ownership & verification machinery (owners, review reminders, verification status/intervals — strongest in the internal segment)
- related articles, tags/labels, glossaries
- notifications (updates, review due, required reading)
- import/export/migration; multi-language
- branding/custom domain (external realization)
- delivery surfaces beyond the site: in-app widgets, browser extension, chat bots, AI agents

### L2 — Variant / Optional Structure

- **Audience axis**: internal (team/company) vs external (customers) vs dual — the market's dominant segmentation; realized through visibility configuration, separate workspaces/spaces, or separate sites. Zendesk's market guide: "Knowledge base software can serve employees, customers, or both… Most platforms support either internal or external knowledge bases, while some combine both in one system."
- **Packaging**: standalone pure-play vs help-desk/ITSM-suite component vs knowledge-management platform vs workspace-embedded.
- Community/Q&A sections beside the corpus; documentation genres (manuals, SOPs, API reference) produced with the same tooling.
- AI layer depth: AI-assisted drafting, AI answers with citations, corpus exposed to AI agents (API/MCP), AI-maintained verification.
- Corpus aggregation from external sources (Google Docs, Notion, Drive, Confluence, SharePoint).
- Deployment: cloud SaaS vs self-hosted; enterprise security posture (SSO/SCIM/audit/private hosting).
- Required-reading/acknowledgment machinery; decision trees as guided retrieval.

### L3 — Vendor-specific Structure

- Guru: Cards/Collections/Folders; verification intervals (30/60/90 days, 6 months, 1 year, does not expire); Knowledge Agent auto-verify/unverify rules with 7-day cooldown; Quality Log with confidence/reasoning; Card Manager; "Up First" queue; Source Verification Manager.
- Document360: Project→Workspace→Language→Category→Article five-level hierarchy; Eddy AI suite; workflow designer with read-only states; Tasks page tabs; Drive; private hosting; MCP server; 30-day recycle bin.
- Zendesk: user segments (up to 10 per article); management permissions (managers / editors-and-publishers split on Enterprise); Team Publishing; multibrand help centers; Knowledge panel in Agent Workspace; verification on Enterprise; subsections on Enterprise.
- KBPublisher: public area vs admin area; custom statuses/types; incoming-email automations; Sphinx search; RSS; Must Read reports.
- Tettra: Kai bot; verification automation; suggested-edit approval.

## Vendor-specific Findings

See L3. Additionally: Guru's framing of verification as "a partnership between people and AI" with agents handling "the bulk of verification work" is the most fully articulated knowledge-health system in the sample (A, one product; treated as a modern variant layer, not a Type requirement). Document360's audience-vs-category rule ("new workspace when the audience is completely different…") is the sharpest vendor articulation of the audience axis as configuration (A, one product; used as evidence for the L2 audience axis, not as Type structure). Zendesk's own migration from multibrand to a single shared help center for internal+external content is direct evidence that audience separation is configuration, not identity (A, one product).

## Rejected Findings

- **"A knowledge base application is internal-facing by definition"** — rejected. The market's self-labeled "knowledge base software" is dual-audience by design (Document360 public/private/mixed projects; KBPublisher's customer-support AND internal-employee positioning; Zendesk's internal+external-as-one-machinery guidance). Audience is the L2 variant axis; the machinery is the Type. This refines the help-center pass's proposed seam (see Boundary Findings 1).
- **"A knowledge base is any searchable document library"** — rejected: the answer-oriented curation (question-mapped organization, governed currency) distinguishes it from repositories/shared drives.
- **"Verification intervals / AI verification are definitional"** — rejected: single-segment machinery (Guru strongest; Zendesk Enterprise-level; absent in KBPublisher's generation); L1/L2.
- **"AI answers are definitional"** — rejected: era-typical (4 of 5 sampled products at some level), absent from the legacy generation; L1/L2.
- **"Multi-language is definitional"** — rejected: varies by audience; L1/L2.
- **"The KB is a wiki with restricted editing"** — rejected as identity: the organizing principles differ (curated answer corpus vs emergent interlinked page graph); products straddle because a wiki can host KB-shaped spaces, but the structures are distinct (see Boundary Findings 2).
- **"Workflow statuses with named stages are definitional"** — rejected: the lifecycle posture is L0; the specific status machinery varies (Guru has none of Document360's stage machinery; KBPublisher's is custom-field based); L1.

## Boundary Findings

1. **vs Help Center (§02.06, processed) — JOINT REVIEW DISCHARGED; keep-both RATIFIED with a refined seam.** The help-center pass proposed: HC = external support publication vs KB = internal curated corpus. KB-side evidence forces a refinement: the market's "knowledge base software" is **audience-agnostic machinery** — Document360 ships public/private/mixed projects and workspaces per audience; KBPublisher positions the same product for customer support and internal employees; Zendesk documents internal and external KBs as the same machinery with different visibility, and its market guide typologizes the category as internal/external/both. Therefore: **audience alone cannot define the KB Type**. The ratified seam is **purpose and center of gravity**: the Help Center is the organization's *external-facing support publication* (the reader-facing site is the product's center; success measured by deflection/resolution; contact affordances hand off to the support operation); the Knowledge Base Application is the *curated corpus and its governance machinery* (the corpus + authoring/ownership/review lifecycle is the product's center; success measured by questions answered and knowledge kept current). A customer-facing KB deployment is the KB machinery realizing the help-center purpose — which is why the market uses the labels interchangeably for that realization. Removal tests, both directions: strip the corpus governance machinery (ownership, review, publish lifecycle) from a help center → a static hand-published FAQ page, not a managed KB; strip the external support-publication purpose from a dual-audience tool → the internal KB machinery remains, unambiguously the KB Type (Guru/Tettra-class products have no reader-facing public site at all and remain KBs). Packaging (suite component vs standalone) drives neither Type.
2. **vs Enterprise Wiki (§02.06, processed) — JOINT REVIEW DISCHARGED; keep-both RATIFIED.** Discriminator confirmed from the KB side: KB = curated, owned, review-managed answer corpus with restricted authorship; wiki = emergent interlinked page corpus with open member editing and durable version history. Removal tests: give every member direct edit rights and let structure emerge from links → wiki; restrict authorship to designated owners with a review-managed lifecycle and question-oriented organization → KB. Market-language blur acknowledged (Slite self-labels "AI knowledge base"; Confluence documents "use as a knowledge base"; Zendesk's market guide lists wiki-adjacent products as KB software): the products straddle because the wiki pattern can host KB-shaped spaces, but the organizing principles differ. Both passes now record the same seam.
3. **vs Wiki Application (§02.06 sibling, unprocessed)** — same discriminator as (2) minus organizational scope; the KB Type is organization-scoped in all sampled realizations (internal corpora) or organization-published (external corpora). Advance note for the wiki-application pass: the KB/wiki seam is organizing principle (curated answer corpus vs emergent page graph), not audience.
4. **vs Self-service Support Portal (§07, processed)** — consistent with that pass's ratified seam: the portal adds tracked request intake + the requester's own request view; the content-only pole is where the Help Center/KB Types begin. The KB's feedback machinery (comments, ratings, "add an article as a result of user feedback") is corpus-improvement input, not a tracked request record.
5. **vs Product Documentation Portal (§02.07, unprocessed)** — genre and lifecycle seam: answer corpus (problem-shaped, question-driven, continuously maintained, success = questions answered) vs structured product documentation (reference/tutorial/API, release-versioned). Tooling overlap is vendor-declared (Document360 sells API documentation as a use case of the same tool; KBPublisher lists "online help, APIs" among content types). Advance note for that pass.
6. **vs Internal Knowledge Search (§13, processed)** — that Type is the discovery/answer layer over a multi-source corpus; the KB is one of the authoring/governance systems such a layer indexes. The KB's built-in search is single-system. Guru's Sources/Answers machinery straddles deliberately (indexes external sources and answers over them) — recorded as a modern variant posture, not a Type merger.
7. **vs Intranet Platform (§10, processed)** — intranet = organization-published estate of news/pages/resources (comms + services); KB = answer corpus. An internal KB can live inside an intranet as a section; the corpus-and-currency machinery is the KB's center.
8. **vs Enterprise Content Management (§10, processed)** — ECM = controlled capture, organization-defined metadata, records retention/disposition; KB = curated answer corpus with knowledge-currency lifecycle. Records compliance vs answer utility is the seam.
9. **vs Note-taking / Personal Knowledge Management (§03.02)** — personal scope vs shared organizational corpus; the KB's authorship/ownership/review machinery presupposes multiple contributors and a defined audience.
10. **vs Online Encyclopedia (§02.05)** — public reference about the world with editorial/community governance vs the organization's own knowledge curated for its own audience.
11. **vs Q&A Community / Community Platform (§01.06)** — member-generated answers vs organization-curated record copy; a community can sit beside a KB as a section (proving separability).
12. **vs Help Desk (§07, processed)** — the support team's operating application vs the knowledge machinery; suites bundle both; structurally independent (standalone KB pure-plays exist).
13. **vs Collaborative Document Editor (§03.01, processed)** — freeform long-form document composition vs a governed corpus of short, question-shaped, individually addressable articles.

## Historical / Market-Sample Check

Question: would older, regional, platform-native, or differently positioned products still fit the L0? Yes:

- **Legacy self-hosted generation** (KBPublisher 8.0 manual, operational level): categories, articles, drafts with approve/reject, custom statuses, article history, feedback→article loop, roles/privileges, search-query tracking, public/admin areas — satisfies all three L0 structures without AI, cloud, workspaces, verification intervals, or analytics dashboards.
- **Pre-software antecedent**: the maintained FAQ document, policy binder, or operations manual — a curated question-ordered list with an owner who updates it, consulted by question. Satisfies the conceptual core (restricted authorship, question-oriented organization, maintained currency) with no software at all.
- **Wiki-pattern products running KB-shaped spaces** (Confluence "use as a knowledge base"): satisfy the L0 when the space is curated/owned/review-managed; the straddle is real and recorded, not a merger.
- Therefore nothing era-specific enters the definition: no AI, no cloud delivery, no verification intervals, no analytics, no multi-language, no specific packaging. Conversely, the definition does not depend on the suite-embedded packaging that dominates today's market — standalone pure-plays and the legacy self-hosted generation both pass.

## Uncertainties

- The ITSM-segment KB (ServiceNow, Freshservice) was not directly sampled; its formal lifecycle states are known only through third-party framing (Zendesk's market guide describes Freshservice KB at feature level). Variant claims about that segment are kept weak.
- Tettra evidence is product-page level; the mechanics of its verification automation and suggested-edit approval are not directly observed.
- Bloomfire/Slab/Slite/Crescendo/Nuclino/Help Scout appear only as market-structure evidence via Zendesk's third-party guide; no product claims rest on them.
- Guru's Collections/Folders hierarchy was observed through the permissions documentation; deeper organization mechanics (templates, announcements) were not fetched.
- Zendesk plan-gating (Enterprise-only verification, Team Publishing, subsections) is recorded as observed plan references; no claims treat plan-gated features as Type structure.
- The boundary with Product Documentation Portal and Wiki Application is flagged for their respective passes; this pass records the seam from the KB side only.

## Final Synthesis

A **Knowledge Base Application** is the organization's system for building and governing a curated corpus of answers: a persistent body of individually addressable articles holding the organization's own knowledge, authored by designated contributors, deliberately organized and retrievable so that a question maps to its answer, and kept current through owned, governed lifecycles (draft → review → publish → update → retire). Around this defining core, mature products add a consistent standard layer — authoring environments, publish/review workflow, version history, search (increasingly AI answers), feedback and analytics loops, visibility/access control with separate operator and reader planes, roles, ownership/verification machinery, translations, and delivery surfaces that push the corpus into sites, widgets, chat tools, and AI agents. The Type's dominant variant axes are audience (internal / external / dual — configuration, not identity), packaging (standalone pure-play / suite component / knowledge-management platform / workspace-embedded), and knowledge-health machinery depth (from simple review reminders to AI-maintained verification). The two discharged joint reviews both ratify keep-both: against the Help Center the seam is purpose and center of gravity (support publication vs corpus governance machinery), against the Enterprise Wiki it is organizing principle (curated answer corpus vs emergent member-maintained page graph).
