# Research Notes — Internal Knowledge Search

Research date: **2026-09-07**

---

## Research Goal

Understand what an "Internal Knowledge Search" application is as a market population and as a candidate Application Type: the stable core structure that makes a product recognizable as this Type, the standard capabilities of current products, the variant space, and — critically — the boundary against the sibling leaf **Enterprise Search Platform** (same directory section), whose research pass flagged this leaf as a probable scope Variant and requested joint review. Evidence from real products' official documentation, not vendor positioning alone.

## Initial Boundary (hypothesis before research)

- **Core use (hypothesis):** let members of an organization find answers and knowledge content (documents, wikis, KB articles, policies, Q&A) scattered across the organization's tools, through one search/ask surface, with results or AI answers grounded in — and access-controlled by — the underlying sources.
- **Primary users (hypothesis):** all employees as askers/searchers; knowledge owners / SMEs as curators; IT / knowledge-ops as administrators.
- **Nearest Types:** Enterprise Search Platform (§10 sibling — the flagged joint review), Knowledge Base Application / Enterprise Wiki (§02.06), Intranet Platform (§10), Enterprise Knowledge Assistant (§13), Search Platform (§13), Help Center (§02.07), General Web Search Engine (§02.02), eDiscovery (§11).
- **Suspected boundary rule:** the ESP pass hypothesized "knowledge-content-only scope" as the difference. Alternative hypothesis worth testing: this population is distinguished not by scope alone but by (a) answer-first AI delivery and (b) a knowledge-trust/verification layer (verified content, owners, review cadence) that ESP products treat as optional curation rather than central structure.
- **Unknowns:** whether permission-awareness is invariant here (ESP made it definitional); whether the KB-native pole (products that own the corpus) breaks the ESP-style "lens over content it does not own" model; how the historical pre-AI form (workplace search products) fits.

## Research Questions

1. What content enters the corpus, and how? (native authoring vs connectors vs both)
2. What does the member get — a results list, an AI answer, or both — and how is provenance shown?
3. How is trust in the knowledge maintained? (verification states, owners, review cadence, automated quality agents, drift detection)
4. How are permissions handled — mirrored from sources, product-scoped groups, or edition-gated?
5. Which surfaces carry the query capability (web app, browser extension, chat tools, MCP/API)?
6. How does this population relate to Enterprise Search Platform — same defining core with different scope, or a structurally distinct Type?
7. Does the historical pre-AI form (workplace/intranet search products) fit the same definition?

## Representative Products

Selected for market representation, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy / pole | Tier | Evidence quality |
|---|---|---|---|
| Guru | governed-knowledge pole: native Cards KB + connected sources; verification/trust as the central discipline; answers delivered in workflow | mid-market/enterprise | A — product pages + help-center operational docs directly fetched |
| Glean | work-search pole: connect the org's SaaS estate; search + assistant in one bar; knowledge graph | enterprise | A — user guide/connectors/security docs fetched 2026-09-06 during the Enterprise Search Platform pass; re-used here |
| Onyx (formerly Danswer) | open-source infrastructure pole: self-hosted RAG platform; connectors; dual Search/Chat UI | dev-team / OSS / mid-market | A — official docs directly fetched |
| Slite | team-KB-native pole: AI knowledge base that owns the corpus; verified-first ranking; self-maintaining docs | team/SMB–mid-market | B — product pages (home + AI-search) fetched; help center not fetched |
| Stack Internal (formerly Stack Overflow for Teams) | Q&A-native pole: trusted knowledge layer built on Q&A heritage; trust signals; scopes; expert validation | engineering orgs, mid/enterprise | B — product + features pages fetched; help center not fetched |

## Sources

- Guru — product page: https://www.getguru.com/ ; Help Center home: https://help.getguru.com/ ; "How Sources Work in Guru": https://help.getguru.com/docs/linking-sources-for-guru-answers ; "How Content is Verified in Guru": https://help.getguru.com/docs/verifying-and-unverifying-cards (all fetched 2026-09-07)
- Onyx — docs home: https://docs.onyx.app/ ; "RAG and Search / Internal Search": https://docs.onyx.app/overview/core_features/internal_search (fetched 2026-09-07)
- Slite — product page: https://slite.com/ ; AI Search page: https://slite.com/ai-search (fetched 2026-09-07)
- Stack Internal — overview: https://stackoverflow.co/teams/ ; features: https://stackoverflow.co/internal/features/ (fetched 2026-09-07)
- Glean — About connectors: https://docs.glean.com/connectors/about ; Search in Glean: https://docs.glean.com/user-guide/search/how-to-search-in-glean ; Security: https://docs.glean.com/security (fetched 2026-09-06 in the sibling Enterprise Search Platform pass; observations re-used with that pass's evidence grade)

Evidence layers: **A** = directly observed in fetched official documentation for that product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + Type-boundary reasoning.

---

## Product Observations

### Guru

Key observations (**A**, getguru.com + help.getguru.com):

- **Positioning.** "The Governed Knowledge Layer for Enterprise AI… Guru structures, governs, and continuously improves your company's knowledge—so every AI tool and every person gets answers they can trust." Solutions include "Enterprise AI search," "Agentic Knowledge Base," "Team Hubs," "Workplace AI Chat & Research," "Knowledge Management Automation," "Enterprise AI Governance."
- **Two content classes.** *Guru Cards* — knowledge authored natively (product documentation, policies, runbooks, playbooks, escalation procedures, meeting summaries…); *External Sources* — documents from connected systems (Google Drive, Confluence, SharePoint, Slack…).
- **Source connection (operational).** Manage > Sources → authenticate → optional Selective Sync → choose content to sync → assign Guru Groups that can access → assign a Source Owner; sync status moves Initializing → Synced; confirmation email on first sync. Sources re-checked "multiple times per day"; files moved out of a synced folder become unsearchable "within 3 days"; 50 MB per-file sync limit; "% Indexed" progress indicator; sync-failure notifications to source managers; service-account recommendation for connection durability.
- **Two permission models — a documented choice.** (1) *Guru Groups*: "Guru connects as a single user and indexes only what that user can access. Access is controlled entirely within Guru, independent of Source app permissions" — best for "exposing content outside that tool's access or seat availability." (2) *Inherited permissions* (supported for some sources): "Guru automatically respects the native access controls from your Source app… When permissions change in the Source app, they automatically update in Guru." → per-user source-ACL mirroring is one option, not the only mode.
- **Verification as the central discipline.** "Verification is Guru's way of marking content as trustworthy and current. Think of it like a 'freshness date'." States: ✅ Verified / ❔ Unverified / none, shown "in search results, AI-generated answers, the AI Agent Center, and when browsing." Every Card has a designated **verifier** (person or Group accountable); optional **verification intervals** (30/60/90 days, 6 months, 1 year, or "does not expire") trigger review reminders; edits by non-verifiers flip the Card to unverified; any user can unverify or comment to flag.
- **Automated quality agents.** Knowledge Agents review content daily with **behavioral rules** (thumbs up/down, views, feedback) and **content-based rules** (AI analysis for dates, time-sensitive info, evergreen topics); unverification rules run before verification rules; 7-day review cooldown; Quality Log with confidence scores and reasons; Source Verification Manager for bulk oversight; agents can be scoped to "Verified only / Verified and no status / All sources" — i.e., **trust state gates what the agent may use**.
- **Answers & surfaces.** AI answers with citations delivered in Slack, Teams, Chrome extension ("Search Guru without leaving the tools you're already using"), MCP ("Accurate AI query via MCP"), web app. Knowledge-gap analysis ("identify knowledge gaps," "unanswered questions found," "repeated Slack questions captured").
- **Governance posture.** Permission-aware AI, full audit trails, enterprise SSO, DLP, configurable guardrails (product-page claims — positioning strength).

### Glean

Key observations (**A**, docs.glean.com — fetched in the ESP pass, re-used):

- **Connector model.** Connectors "integrate Glean with a platform, service, or application where your content lives… index content, mirror permissions from the source, and keep that data current in your isolated tenant." Native (API crawl: content + people + activity data), web-history (browser extension; personal browsing titles, private to the individual), push-API, partner connectors. Indexed / live / hybrid access modes.
- **Permission mirroring.** "Search results strictly adhere to the access permissions set in the source application"; query time applies the permission snapshot mirrored during crawling.
- **Searcher UX.** One bar for search and chat; keyword or natural-language queries; full-document matching; filters (`updated:`, `from:me`, `type:`, `app:`); people search with org chart and activity; shareable query URLs whose results re-trim per recipient.
- **Curation/trust layer.** Answers, Collections, Go Links, pinned results, **document verification**, announcements.
- **Surfaces.** Web app, browser extension, desktop app, Slack; APIs for embedding.

### Onyx (formerly Danswer)

Key observations (**A**, docs.onyx.app):

- **Positioning.** "Open Source AI Platform for Work… a natural language interface for any LLM while integrating seamlessly with your knowledge and applications." Explicitly compared against ChatGPT, Copilot, Gemini, **and Glean**.
- **Internal Search feature (the leaf's literal namesake).** "RAG and Search — Enterprise Search across all your applications… Onyx uses Connectors to index knowledge from your team's applications to build an understanding of the documents, people, and concepts within your organization. Documents, metadata, and access permissions are all kept up to date in near real time."
- **Dual delivery with intent classification.** Search UI (document results; filters by time range, authors, tags such as `Folder: Engineering`, source type) vs Chat UI (answers; agents; deep research). "Users do not need to explicitly select this mode — when a query is classified by Onyx as a document search, it will automatically go into this UI experience."
- **Permission retrieval is edition-gated.** "Onyx's context retrieval respects user level permissions which is only configurable via the Enterprise Edition." → per-user permission-aware retrieval is a paid-tier capability in this product, not a universal invariant of the population.
- **Retrieval stack.** Contextual retrieval, advanced RAG, hybrid search, AI-generated knowledge graphs; plug-and-play LLMs; self-host or cloud.

### Slite

Key observations (**B** — product pages fetched; help center not fetched):

- **Positioning.** "Self-maintaining AI knowledge base… Verified knowledge, kept in sync with reality. The AI knowledge base that stays accurate: synced with your tools, verified by your team, trusted by every agent that depends on it."
- **Corpus = native KB + connected tools.** Docs/collections/channels authored natively; AI search spans "Slack, Notion, Google Drive, Jira, and 20+ sources" (integration logos also include Salesforce, HubSpot, Zendesk, Confluence, SharePoint, Linear, GitHub, GitLab, Asana, Intercom, Attio, BigQuery, Zoom).
- **Answer-first, trust-ranked delivery.** "One answer, cited, ranked by trust… Verified docs lead. Unverified or stale sources rank lower, with a trust signal on every citation… Always cited. Every response cites the exact sources that shaped it." "Permission-aware. Yes, even for third-party agents. Every query inherits the user's permissions."
- **Self-maintenance loop.** Slite Agent "detects knowledge drift across your tools" (watches Slack, Linear, GitHub, codebase), drafts the doc fix, routes it to the right expert for approve/reject; scheduled maintenance routines; verification states and review states on docs; humans stay in the loop.
- **Agent supply.** MCP server exposing the verified knowledge as context for Claude, ChatGPT, Cursor ("Search every source, Read a doc, Verify a doc…").
- **Surfaces.** Slite app, Chrome extension ("answers from all your sources — and reads the page you're on"), Slack ("Ask in any channel or thread").
- **Security posture.** SOC 2 Type II, HIPAA, GDPR, EU-hosted; SSO, SCIM, granular RBAC, reader-only seats; audit logs, version history (product-page claims — positioning strength).
- **Tier.** Per-user pricing at team scale ($10–20/user/month bands); team/SMB–mid-market.

### Stack Internal (formerly Stack Overflow for Teams)

Key observations (**B** — product/features pages fetched; help center not fetched):

- **Positioning.** "The trusted knowledge layer… captures, curates, validates and delivers enterprise knowledge with trust built-in – your own version of our iconic green check mark." Heritage: "Two decades of Q&A."
- **Capture.** Connectors for "your Stack Internal community, Google Docs and Slack channels"; "automatically captures and synthesizes data from your AI tools, chat threads, wikis, breaking them into units of knowledge"; permission-aware ingestion ("information only gets pulled from the sessions, folders and channels you want").
- **Validate (trust system).** "Every unit of knowledge carries a record of where it came from, who wrote it, and how trustworthy it is"; "confidence indicators — reviewer, recency, and corroboration labels on every answer"; "automatic SME validation only when there are critical gaps"; expert-validation workflow converts an expert's answer into trusted knowledge; SME auto-detection from platform interaction.
- **Organize.** "Scopes" — role-based workspaces mapping context so "knowledge is used by the right people, team, or AI agent"; "AI agents are treated as first-class citizens with permission-aware knowledge access."
- **Govern.** Control Center: permissions, curation-activity tracking, audit logs; role-based permissions; app authentications for API/MCP.
- **Deliver.** Chat; API, MCP server, plugins; "verified, scoped knowledge gets sent into the tools you use everyday, then that activity feeds back into the platform."
- **Community (native corpus).** Q&A ("time-tested Q&A surfaces trusted answers"), Articles, Tags & Collections.
- **Product UI units.** Chat, Inbox, Scopes, Control Center.

---

## Cross-product Comparison

| Dimension | Guru | Glean | Onyx | Slite | Stack Internal |
|---|---|---|---|---|---|
| Corpus composition | native Cards + connected sources (Drive, Confluence, SharePoint, Slack…) | connected SaaS estate (content + people + activity) | connected applications ("documents, people, concepts") | native KB + 20+ connected sources | native Q&A/Articles + connectors (community, Google Docs, Slack) |
| Ingestion | source connection w/ selective sync; sync multiple times/day | connectors (native/web-history/push); indexed/live/hybrid | connectors; near-real-time updates | integrations + native authoring | connectors; capture from chat/docs/AI tools |
| Query surface | search + AI answers in web app, extension, Slack/Teams, MCP | one bar for search + chat; extension; desktop; Slack | dual Search/Chat UI with auto intent classification | AI search in app, extension, Slack | chat + Q&A browse; API/MCP/plugins |
| Delivery form | cited AI answers + search results | results + assistant answers w/ citations | results list or answer, auto-selected | one cited answer, trust-ranked | answers w/ confidence labels + Q&A results |
| Provenance | citations; verification badge on results/answers | citations; document verification | results link to sources; answers grounded | citation with trust signal on every answer | reviewer/recency/corroboration labels |
| Trust/verification machinery | verification states + verifiers + intervals + automated quality agents + quality log | document verification; curated answers | none documented | verified-first ranking; drift detection; agent-drafted fixes routed to experts | trust signals; SME validation workflow; staleness/gap detection |
| Permissions | choice: product-scoped Groups OR inherited source permissions | mirrored from sources, query-time | respects user-level permissions (Enterprise Edition) | query inherits user's permissions, incl. third-party agents | role-based scopes; agents as first-class citizens |
| Knowledge maintenance | verification intervals; auto-verify/unverify; gap analysis | curation layer (answers/collections) | — | self-maintaining docs; drift→draft→expert approval | curation engine; expert validation on gaps |
| People | — (not central) | people search, org chart, activity | "people" in index scope | — | SME auto-detection |
| Agent/API supply | MCP; developers portal | APIs; MCP/tool config | agents; API | MCP server; custom connectors | API; MCP server; plugins |
| Deployment | SaaS | SaaS (isolated tenant; customer-hosted option) | self-hosted OSS or cloud | SaaS (EU-hosted option) | SaaS |
| Tier | mid-market/enterprise | enterprise | OSS/dev-teams → mid-market | team/SMB–mid-market | engineering orgs, mid/enterprise |

**B-level commonalities across the sample (evidence: ≥4 of 5 products each):**

1. The corpus is the organization's own knowledge content — docs, wikis/KBs, Q&A, chat-derived knowledge — held natively and/or ingested from the organization's tools. (all 5)
2. Multi-source assembly: native authoring plus connectors, or connectors alone; a single system's contents alone is not the shape of any sampled product. (all 5)
3. One member-facing query surface — a search/ask bar — reachable both in a web app and inside work tools (browser extension, Slack/Teams). (all 5)
4. Grounded delivery with provenance: results open the source document; AI answers cite the sources that shaped them. (all 5 current; provenance-by-link is the historical form)
5. AI answers with citations as the flagship delivery form. (all 5 current — but the pre-AI workplace-search era lacked this; see historical check)
6. A knowledge-trust layer: verification/trust states on knowledge items, accountable owners/reviewers, and trust signals surfaced on results/answers. (Guru, Glean, Slite, Stack Internal = 4/5; absent in Onyx)
7. Continuous sync keeping the searchable copy current with sources. (Guru, Glean, Onyx, Slite, Stack Internal — all documented at some strength)
8. Access control over what enters and who sees results — implemented variously (mirrored ACLs, product-scoped groups, role-based scopes). (all 5; form varies, see L0 discussion)
9. Knowledge-gap detection and curation loops (unanswered/repeated questions → capture/fix knowledge). (Guru, Slite, Stack Internal = 3/5 — common in the KM-native pole)
10. Programmatic supply of the corpus to AI agents (MCP/API). (Guru, Glean, Onyx, Slite, Stack Internal — all current; rapidly standardizing)

**C-level canonical inference:** the population is best modeled as *the organization's knowledge corpus (authored natively and/or gathered from its tools) → assembled into one searchable body → one member-facing query surface → grounded delivery (source-linked results or cited answers)*, with a knowledge-trust layer (verification, owners, review cadence, trust-ranked delivery) as the current market's central discipline, and in-workflow surfaces plus agent/API supply as standard extensions. All five sampled products simultaneously satisfy the Enterprise Search Platform defining core (multi-source estate → ingestion → one query surface → merged results → permission trimming where deployed); the differences are scope emphasis (knowledge content), delivery emphasis (answers), the trust layer, and the KB-ownership pole.

---

## Abstraction Hierarchy (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (kept deliberately minimal)

An Internal Knowledge Search application exists iff all of the following hold:

1. **Internal knowledge corpus** — the searchable domain is the organization's own knowledge content (documents, wiki pages, KB articles, policies, Q&A, knowledge captured from work tools); not the public web, not transactional business records as the focus.
2. **Multi-source assembly** — the corpus is gathered from more than one source: authored/curated natively and/or ingested from the organization's tools and systems. A single system's built-in search is a feature of that system, not this Type.
3. **One member-facing query surface** — a search/ask entry point through which members query the corpus.
4. **Grounded delivery** — what the member receives leads back into the corpus: a result that opens the source document, or an answer citing its sources.

Removal tests: remove (1) → public web search or generic app search; remove (2) → a single wiki/KB's built-in search feature; remove (3) → a knowledge base with no discovery layer; remove (4) → an ungrounded chatbot or a link dump.

**Deliberately NOT in L0** (with the evidence that justified exclusion):

- *Per-user permission trimming mirrored from sources* — Guru documents a second, first-class model (product-scoped Groups, "independent of Source app permissions"), and Onyx gates per-user permission-aware retrieval to its Enterprise Edition. Access control is universal in mature deployments, but its mechanism (mirrored ACLs vs product-scoped groups vs coarse workspace visibility) varies; the historical intranet-search form often ran without per-user trimming. → L1.
- *AI answers* — universal in the current sample but absent from the pre-AI workplace-search form. → L1.
- *Verification/trust machinery* — 4/5, absent in Onyx. → L1.
- *Native KB/authoring* — pole-dependent (Glean and Onyx have none). → L2.

Historical check (§24 discipline): the pre-AI form of this population — workplace-search products that connected knowledge sources (cloud drives, wikis, chat) into one permission-aware search UI, and intranet search appliances crawling multiple intranet sites — satisfies L0 items 1–4 without AI answers, verification layers, or MCP surfaces. Wiki/KB built-in search (single-system) fails item 2, confirming the multi-source invariant as the Type separator. The definition does not over-fit to the current AI-answer implementation.

### L1 — Common Mature Structure (standard in current products, not definitional)

- Connector/integration catalog over knowledge sources (wikis, drives, chat, ticketing, docs) with continuous/incremental sync and sync-status monitoring
- AI answers with citations as the flagship delivery, alongside a results-list form (some products auto-classify which to show)
- Knowledge-trust layer: verification/trust states on knowledge items; accountable owners/reviewers; review cadence; trust signals displayed on results/answers; trust state can gate or re-rank what answers may use
- Access control over results: mirrored source permissions and/or product-scoped groups/roles/scopes; permission-aware behavior extended to third-party agents in current products
- In-workflow surfaces: browser extension, chat-tool integration (Slack/Teams), alongside the web app
- Knowledge-gap detection: unanswered/repeated questions, staleness flags, gap analytics
- Curation/maintenance loops: capture knowledge from work activity; draft updates; route to experts for approval
- Programmatic supply: APIs and MCP servers exposing the corpus to AI agents and custom integrations
- Search mechanics: filters (source, time, author, tags), semantic/hybrid retrieval, autocomplete
- Admin analytics: usage, query and gap analytics; audit logs at enterprise depth

### L2 — Variant / Optional Structure

- **Corpus-ownership pole:** KB-native (product is the system of record for part of the corpus — Cards/docs/Q&A, with authoring and lifecycle) ↔ search-native (pure lens over external sources) ↔ hybrid (the dominant current shape)
- **Trust-machinery depth:** none → trust signals on delivery → full verification workflows with automated quality agents and quality logs
- **AI depth:** keyword results → cited answers → agents that act on/with the corpus
- **Scale/tier:** team/SMB → mid-market → enterprise (governance depth: SSO, SCIM, RBAC, audit, AI guardrails, residency)
- **Deployment:** multi-tenant SaaS ↔ customer-hosted ↔ self-hosted open source
- **Scope breadth:** knowledge-content center extending into business apps (tickets, deals, tables) — blurring edge toward the ESP estate
- **People dimension:** people search/org charts/SME detection — central in some products, absent in others

### L3 — Vendor-specific (kept out of the final document)

- Guru: Cards/Collections/verifiers/verification intervals; Knowledge Agents; AI Agent Center; Quality Log; Source Verification Manager; two-model source permissions; specific sync cadences and limits (multiple syncs/day, 3-day removal, 50 MB file cap); "Up First" review queue
- Glean: Knowledge Graph; web-history connectors; Go Links; Collections; `updated:`/`from:`/`my:history` operator vocabulary; indexed/live/hybrid access modes
- Onyx: Enterprise Edition permission configuration; auto intent classification between Search/Chat; AI-generated knowledge graphs; plug-and-play LLM configuration
- Slite: Slite Agent drift detection; self-maintaining doc routines; verified-first ranking; MCP toolset (verify a doc, resolve a comment…); EU hosting
- Stack Internal: Scopes; Control Center; SME auto-detection; confidence indicators (reviewer/recency/corroboration); capture from AI-tool sessions
- Marketing figures (adoption stats, "90% fewer questions", company counts) — recorded here only, excluded from the final document.

## Rejected Findings (considered, not promoted)

- *"AI answers are the defining structure"* — rejected: the pre-AI workplace-search form satisfies the corpus+surface+grounding core; answers are the current flagship delivery, not the invariant.
- *"Verification/trust layer is definitional"* — rejected: absent in Onyx and in the historical form; it is the current market's central discipline (L1) and the KM-native pole's differentiator, not the invariant.
- *"Per-user source-permission mirroring is definitional"* — rejected: Guru's product-scoped Groups model and Onyx's edition gating show mechanism variance; access control in some form is standard (L1), mirrored ACL trimming specifically is not invariant here (unlike the ESP sample).
- *"People search is definitional"* — rejected: central in Glean, marginal elsewhere; L1/L2.
- *"This is just a knowledge base with search"* — rejected: the multi-source assembly invariant separates the Type from single-system built-in search; KB-native products still assemble beyond their own corpus.

## Boundary Findings

| Neighboring Type | Boundary rule ("remove X → becomes that Type") |
|---|---|
| **Enterprise Search Platform** (§10 sibling — joint review) | Shared defining core: multi-source estate → ingestion → one query surface → merged results → access control. Differences are of scope emphasis (knowledge content vs whole estate incl. records/email/people), delivery emphasis (cited answers vs results-first discovery), the knowledge-trust layer (central here, optional curation there), and the KB-ownership pole (this population includes products that own part of the corpus; ESP is a lens over content it does not own). **Verdict from this side: the evidence supports the ESP pass's hypothesis — Internal Knowledge Search is a scope/emphasis Variant of Enterprise Search Platform rather than a structurally independent Type.** All five sampled products satisfy the ESP defining core. Recorded for taxonomy-level decision; this leaf documented as the directory defines it. |
| **Knowledge Base Application / Enterprise Wiki** (§02.06) | The KB/wiki is content authoring/publishing with built-in single-system search; this Type is the discovery/answer layer over a multi-source knowledge corpus. Remove multi-source assembly and the discovery-first mission → a KB/wiki. KB-native products here bundle authoring, but their defining search structure spans sources. |
| **Intranet Platform** (§10) | Communication/content publishing surface with search embedded; remove publishing/communication, keep knowledge discovery → this Type. |
| **Enterprise Knowledge Assistant** (§13) | Answers-first conversational product grounded in an index; when the corpus layer is included it sits on/overlaps this Type; remove the corpus assembly/permission layer → a chat product. Convergence watch (same as ESP pass noted). |
| **Search Platform** (§13) | Developer infrastructure for building search into arbitrary applications; no organizational knowledge corpus implied. Swap the org-knowledge corpus for arbitrary apps → Search Platform. |
| **Help Center** (§02.07) | External-facing knowledge for customers; this Type serves internal members over internal knowledge. Audience flip. |
| **General Web Search Engine** (§02.02) | Public web, ad-funded, no org access rules. Scope flip. |
| **eDiscovery** (§11) | Legal investigation over the estate with holds/exports/chain of custody; this Type is everyday knowledge discovery for everyone. Purpose/user flip. |
| **Data Catalog** (§13) | Metadata about data assets for data practitioners; this Type serves knowledge content to everyone. Object-class flip. |

**Product-pollution check:** every sentence of the final document must survive deletion of product names; vendor vocabularies (Cards, Knowledge Agents, Scopes, Control Center, Slite Agent, Knowledge Graph, Go Links) appear only in these Research Notes.

## Uncertainties

- **Slite and Stack Internal evidence is product-page level** (help centers not fetched): their operational specifics (sync behavior, permission configuration depth, verification mechanics) are kept at positioning strength; no precise operational claims rest on them.
- **Glean evidence re-used from the sibling ESP pass** (fetched 2026-09-06, one day earlier): treated as A-level; no re-fetch performed.
- **Onyx permission-gating sentence is ambiguous** ("context retrieval respects user level permissions which is only configurable via the Enterprise Edition") — interpreted as: per-user permission-aware retrieval is an Enterprise-Edition capability. The final document states only the calibrated conclusion (permission machinery varies and can be edition-gated), not the edition detail.
- **Historical form asserted from market knowledge, not fetched archives**: the pre-AI workplace-search/intranet-search form is used only to calibrate abstraction level (keep AI answers and trust machinery out of the defining core), not as a source of specific product claims.
- **Population naming is fluid**: sampled products self-describe as "enterprise AI search," "AI knowledge base," "trusted knowledge layer," "open source AI platform" — no vendor markets primarily under the literal words "internal knowledge search"; the leaf name is the directory's label for the population, not a market term of art. This weakens any claim that the leaf name maps to a distinct market category — further support for the Variant verdict.

## Final Synthesis

Internal Knowledge Search, as the market actually builds it, is the knowledge-centered member of the enterprise/workplace search family: it assembles the organization's own knowledge content — authored natively and/or ingested from its tools — into one searchable body, gives members a single search/ask surface (in a web app and inside their work tools), and delivers what it finds as source-linked results or cited answers. Current products wrap this core in a knowledge-trust discipline (verification states, accountable owners, review cadence, trust-ranked delivery), detect and close knowledge gaps, and supply the same corpus to AI agents through APIs and MCP. The defining core is deliberately smaller than the current feature set: AI answers, trust machinery, permission-mirroring specifics, and native authoring are all standard-or-common capabilities rather than invariants — the pre-AI workplace-search form satisfies the core without them. Joint-review verdict for the ESP flag: the population satisfies the Enterprise Search Platform defining core in every sampled product; the leaf is best treated as a scope/emphasis Variant of Enterprise Search Platform (knowledge-content corpus, answer-first delivery, trust layer, KB-ownership pole), with the merge/canonicalization decision left to taxonomy maintainers.
