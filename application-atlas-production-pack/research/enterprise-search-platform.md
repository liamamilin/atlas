# Research Notes — Enterprise Search Platform

Research date: **2026-09-06**

---

## Research Goal

Understand what an Enterprise Search Platform actually is as an Application Type: the stable core structure that makes a product recognizable as this Type, the standard capabilities of mature products, the variant space (delivery form, packaging philosophy, AI depth), and the boundaries against adjacent Types — using evidence from real products' official documentation, not vendor positioning alone.

## Initial Boundary (hypothesis before research)

- **Core use:** let members of an organization find content that is scattered across the organization's many internal systems (file stores, wikis, cloud drives, business apps, email, records systems) through one query surface, with results respecting each user's access rights.
- **Primary users:** every employee (searchers); IT / search administrators (connectors, index, relevance, answers); content owners; developers (search APIs / embedding).
- **Nearest Types:** Internal Knowledge Search (same directory section), Search Platform (developer infrastructure), General Web Search Engine, Data Catalog, ECM, Intranet Platform, Knowledge Base Application, Enterprise Knowledge Assistant, eDiscovery.
- **Suspected boundary rule:** "many heterogeneous internal sources + one query surface + per-user authorization" is the candidate defining combination. Remove cross-source unification → single-system built-in search. Remove per-user authorization → an internal crawler/site search, not enterprise search.
- **Unknowns:** whether permission-awareness is truly invariant or only strongly common; how to classify the historical "engine/appliance" era; where the AI-answer layer lands (defining vs optional).

## Research Questions

1. How does content enter the system? (connectors, crawlers, push APIs, federation)
2. How are source permissions carried and enforced? (ACL mirroring, query-time trimming, who can see what)
3. What does the searcher see? (search box placement, results page, verticals, filters, people search, personal results)
4. What does the administrator do? (source management, curation, relevance controls, analytics)
5. What is the relationship between the search layer and newer AI assistant/answer layers?
6. How do engine-era / infrastructure-pole products fit the same Type as SaaS application-pole products?
7. What distinguishes this Type from Internal Knowledge Search, Search Platform, Data Catalog, web search engines?

## Representative Products

Selected for market representation, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy / pole | Evidence quality |
|---|---|---|
| Microsoft Search (in Microsoft 365) + Copilot connectors | platform-embedded cross-suite search, extensible by connectors; largest installed base | A — extensive admin/IT docs (Learn) directly fetched |
| Glean | standalone SaaS "work search"; connect many SaaS apps; assistant/agent layer on top | A — user guide, connectors docs, security docs directly fetched |
| Elastic (Elasticsearch + content connectors + search applications) | engine/infrastructure pole: developer assembles search experiences; connectors sync read-only replicas | A — connector reference docs directly fetched; application pole from product page |
| Sinequa | intelligent search platform for large/regulated enterprises; out-of-box search + build framework | B — product/positioning pages fetched; deep technical docs not fetched |
| Google Cloud Search | SaaS connector-model search | **not usable** — cloud.google.com timed out twice; dropped from sample, limitation recorded |

## Sources

- Microsoft Learn — Microsoft Search admin documentation hub: https://learn.microsoft.com/en-us/microsoftsearch/ (fetched 2026-09-06)
- Microsoft Learn — Microsoft Search Overview: https://learn.microsoft.com/en-us/microsoftsearch/overview-microsoft-search (fetched 2026-09-06)
- Microsoft Learn — Microsoft 365 Copilot connectors overview: https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview (fetched 2026-09-06)
- Glean docs — About connectors: https://docs.glean.com/connectors/about (fetched 2026-09-06)
- Glean docs — Search in Glean: https://docs.glean.com/user-guide/search/how-to-search-in-glean (fetched 2026-09-06)
- Glean docs — Security and Architecture hub: https://docs.glean.com/security (fetched 2026-09-06)
- Elastic docs — Content connectors reference: https://www.elastic.co/docs/reference/search-connectors (via /guide/en/enterprise-search/current/connectors.html; fetched 2026-09-06)
- Elastic — Enterprise Search product page: https://www.elastic.co/enterprise-search (fetched 2026-09-06)
- Sinequa — product pages: https://www.sinequa.com/ and https://www.sinequa.com/product/workplace-search/ (fetched 2026-09-06)
- Google Cloud Search — https://cloud.google.com/search/docs/overview and https://cloud.google.com/search — **timed out twice each; abandoned per retry limit.** No Google-specific claims made anywhere in these notes or in the final document.

Evidence layers: **A** = directly observed in fetched official documentation for that product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + Type-boundary reasoning.

---

## Product Observations

### Microsoft Search (in Microsoft 365) + Copilot connectors

Key observations (all **A**, Microsoft Learn):

- **Scope & unified index.** "Microsoft Search shows the content that your organization has stored in Microsoft 365 or has indexed through connectors." Unified cloud search index across SharePoint, OneDrive for Business, Exchange. Cross-tenant search explicitly excluded.
- **Permission-aware results, explicitly stated.** "They only see results that they already have access to, Microsoft Search doesn't change permissions." Privacy section: "only the content that a user has permission to see can appear in search results." Access can derive from authorship, sharing to user or group, or location permissions.
- **Personal / contextual.** "Whichever app users are working in; Microsoft Search is personal… Each user might see different results, even if they search the same words." Results are contextual per app (Outlook → mail, SharePoint → sites/pages/files). Suggestions based on previous activity, recent files, collaborators, org-trending content.
- **Connectors (Copilot connectors) — two ingestion modes.** *Synced connectors* crawl and index external content into Microsoft Graph: "Each item includes content, metadata (like title and URL), and an access control list (ACL) that enforces permissions." *Federated connectors* fetch in real time via MCP, no indexing, read-only, respect source permissions and OAuth. Self-serve variants let individual users connect personal sources with their own credentials; content is removed when disconnected.
- **Continuous sync.** "Connectors periodically check for changes… Admins can configure sync frequency and trigger full crawls as needed."
- **Prebuilt + custom connectors.** 100+ prebuilt (Box, Dropbox, Google Drive, Confluence, MediaWiki, file shares, Salesforce, ServiceNow, Jira, Zendesk, Workday, SAP, SQL/Oracle…); custom connectors via Graph connectors API (define schema, register in Entra ID, push data); on-prem sources via connector agent.
- **Admin-crafted answers.** Bookmarks, acronyms, Power BI results — admins provide fast authoritative results by keywords; can target groups (new hires, geographies).
- **UX machinery.** Verticals (result tabs), result types, SERP layout, custom filters, results clusters; search box in the header of M365 apps; search history is personal, reviewable, clearable; admins see popular queries but not who searched (usage reports).
- **Hybrid.** Cloud hybrid search returns results from both online and on-premises SharePoint content.
- **Query processing.** Intent parsing ("how to change my password" → "change password"), intelligent ranking; semantic indexing AI on ingested items.

### Glean

Key observations (**A**, Glean docs):

- **Connector model.** "A Glean connector integrates Glean with a platform, service, or application where your content lives… They let Glean index content, mirror permissions from the source, and keep that data current in your isolated tenant." Connector types: native (direct API crawling: content data, people data, activity data), web-history connectors (browser-extension; page titles from personal browsing; results private to the individual), push-API connectors (custom apps, self-hosted, behind firewalls), partner connectors.
- **Permission mirroring.** "They also fetch the permissions map from each source, ensuring search results strictly adhere to the access permissions set in the source application." Query time applies "the permission snapshot that was mirrored during crawling and incremental updates."
- **Access modes.** Indexed access (default; content + permissions crawled ahead of time), live access (fetched at query time; subject to source rate limits; some sources require per-user auth), hybrid access (index for recall + live calls for recent/long-tail data).
- **People & activity data as first-class.** Connectors must expose identities, roles, permissions, groups, plus creation/edit/view/share activity — used for the Knowledge Graph and relevance ranking. "Connectors collect activity signals — such as views, edits, and shares — that Glean uses to rank search results by relevance."
- **Searcher UX.** One bar serves search and chat; keyword or natural-language question queries; full-document (not title-only) matching; autocomplete including previously visited docs; quoted-phrase operators; filters — `updated:`, `from:me`, `type:`, `my:history`, `app:`; dynamically suggested per-app filters; advanced custom-field filters (e.g., Salesforce `status:"closed won"`).
- **People search.** Search a person → contact info, org chart, recent documents and activity; search by department or role.
- **Surfaces.** Web app, browser extension (also surfaces docs from enterprise apps that are not indexed), desktop app, Slack integration; shareable query URL — "Their results are personalized, so they won't see any sensitive content they don't have access to, even if you see it in your results."
- **Knowledge curation layer.** Answers, Collections, Go Links, Pinned results, document verification, announcements — a curated knowledge layer on top of search.
- **Tenant isolation & governance.** Isolated tenant, encryption in transit/at rest; admin audit logs; MCP servers/tools configuration for acting in connected apps.

### Elastic (Elasticsearch + content connectors)

Key observations:

- **Connector concept (**A**, connector reference):** "A connector is an Elastic integration that syncs data from an original data source to Elasticsearch. Use connectors to create searchable, read-only replicas of your data in Elasticsearch." Connectors extract files/records/objects and transform them into Elasticsearch documents. Catalog: Box, Confluence (Cloud/DC/Server), Dropbox, GitHub, Gmail, Google Drive/Storage, Jira, MS SQL/MySQL/PostgreSQL/Oracle/MongoDB, network drives, Notion, OneDrive, Outlook, S3, Salesforce, ServiceNow, SharePoint Online/Server, Slack, Teams, Zoom. Per-connector feature matrix: advanced sync rules, incremental syncs, binary content extraction, **document level security (DLS)** where supported.
- **Setup modes (**A**):** self-managed (open-source Python connector service you deploy, customizable) vs Elastic-managed (hosted on Elastic Cloud).
- **Application pole (**A/B**, product page):** Elasticsearch positioned as a platform for building "search-driven applications": ingest via API, tune relevance, query rules, synonyms, semantic/vector/hybrid retrieval, RBAC and document-level controls; Agent Builder / conversational search on top. The buyer is a developer assembling search experiences rather than an end-user searching out of the box.
- Interpretation: Elastic demonstrates the **infrastructure pole** of this Type — the same defining structure (sources → connectors → common index → permission-aware query surface) exists, but the "single query surface" is typically delivered as an app the customer builds or embeds, with document-level security enforced at the engine layer.

### Sinequa

Key observations (**B** for platform claims — product pages fetched, deep docs not fetched):

- **Positioning.** "Enterprise AI Search… enables organizations to securely find, understand, and activate knowledge across all enterprise data sources using AI." Large-enterprise segment (industrials, life sciences, aerospace/defense, legal); scale claims in marketing numbers (not used as facts).
- **Connectors.** Extensive prebuilt connector catalog (claimed 200+ on product page — vendor figure, treated as marketing claim); custom connector development explicitly supported (connector list page + "unique ability to develop new ones" quote).
- **Permissions.** "Sinequa honors the permissions already present in your existing systems, so employees only see what they're supposed to see"; document-level security emphasized across pages.
- **AI layer.** AI assistants and agents grounded in the search platform; hybrid/neural retrieval positioned as the relevance engine; LLM-agnostic; no-code assistant builder; MCP server offered.
- **Framework.** SBA (search-based application) framework for building custom search applications — again the dual application/infrastructure pole.

---

## Cross-product Comparison

| Dimension | Microsoft Search | Glean | Elastic | Sinequa |
|---|---|---|---|---|
| Content scope | org's M365 estate + connector sources | org's SaaS app estate via connectors | any sources with a connector; data synced as read-only replicas | enterprise content across systems (documents + records) |
| Ingestion | synced connectors (index into Microsoft Graph, ACL per item) + federated (live MCP) | native crawl + push API + web-history; indexed / live / hybrid access modes | connectors sync into Elasticsearch index; self-managed or managed service | connectors into platform index; custom connectors supported |
| Permissions | ACL ingested per item; query-time filtering; "doesn't change permissions" | permissions map mirrored; query-time snapshot; strictly source-adherent | document-level security per connector (feature matrix) | honors source permissions; document-level security |
| Query surface | search box in every M365 app header + SERP | one bar for search + chat; browser extension; desktop; Slack | built/embedded search apps; Kibana tooling | out-of-box search UI + SBA framework apps + assistant |
| Result organization | verticals, filters, result types/clusters, source labels | filters (`updated/from/type/app`), dynamic facets, source labels | app-defined (developer) | configurable results UI |
| Curation / answers | bookmarks, acronyms, Power BI; targeted audiences | Answers, pins, Collections, Go Links, verification | app-defined | assistants; curated starters |
| People | people/org-chart results; people-filtered search | people search with org chart + activity; dept/role search | — (buildable) | expert identification (SME) |
| Personalization | personal results; same query, different results per user | activity-signal ranking; my-history filter; personalized sharing | implementable (signals available) | "personalize" step in assistant flow |
| Admin analytics | usage reports (popular queries, not who); user feedback | admin insights; audit logs | engine observability | platform governance |
| AI layer | Copilot Search / Copilot answers with citations | Assistant/agents with citations; deep research | Agent Builder, RAG | assistants, agents, RAG |
| Delivery | SaaS tenant (index in Microsoft cloud) | SaaS isolated tenant; customer-hosted option | cloud, on-prem, self-managed | cloud/on-prem; multiple deployment options |

**B-level commonalities across the sample (evidence: ≥3 products each):**

1. Connectors are the canonical ingestion unit: prebuilt catalog + custom/SDK/push path. (MS, Glean, Elastic, Sinequa)
2. Permissions travel with the content (ACL mirroring) and are re-asserted at query time; the search system never widens access. (MS, Glean, Elastic-DLS, Sinequa)
3. A common searchable representation that merges sources — either a unified index or query-time federation; modern products mix both. (MS synced/federated; Glean indexed/live/hybrid; Elastic index; Sinequa hybrid)
4. Cross-source result list with per-result source identification and metadata (who, when, where). (MS, Glean; others via UI)
5. Filtering/refinement machinery (verticals/facets/filters). (MS, Glean; Elastic app-level; Sinequa UI)
6. People as a searchable object class (colleagues, experts, org context). (MS, Glean, Sinequa)
7. Personalization from user activity / signals; same query can yield different results per user. (MS, Glean; Sinequa)
8. Admin-curated answers/boost layer on top of algorithmic results. (MS bookmarks/acronyms; Glean answers/pins; Sinequa starters)
9. Activity signals (views/edits/shares) feed relevance. (Glean explicit; MS trending/personal; Sinequa personalization)
10. Continuous/incremental sync with configurable cadence and full-recrawl trigger. (MS, Glean, Elastic)
11. Search APIs for embedding and downstream apps. (MS Graph connectors API; Glean indexing/search API; Elastic APIs; Sinequa SBA)
12. AI answer/assistant layer grounded in the index, citing sources, subject to the same permission model. (MS Copilot, Glean Assistant, Sinequa assistant, Elastic Agent Builder)

**C-level canonical inference:** the Type is best modeled as *content sources → ingestion carrying content+metadata+permissions → common searchable representation → one query surface → merged relevance-ranked results → trimmed to the searcher's rights*, with curation, people, analytics, and AI answers as mature layers on top. Whether the searchable representation is a pre-built index or live federation is an implementation choice, not part of the definition. Whether the query surface is a product results page, an embedded box, or a developer-built app determines the *packaging pole*, not the Type.

---

## Abstraction Hierarchy (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (kept deliberately minimal)

An Enterprise Search Platform exists iff all of the following hold:

1. **Organization-scoped content estate** — the searchable domain is the organization's own content, spread across multiple heterogeneous systems (files, wikis, drives, email, business apps, records). Not the public web; not one system's contents alone.
2. **Ingestion into a common searchable representation** — a connector/crawler/push/federation layer brings each source's content, metadata, and access rights into a form queryable as one space.
3. **A single query surface open to organization members** — one place (page, box, API, embedded chat) where a member queries across all connected sources.
4. **Cross-source merged, relevance-ranked results** — results from different sources compete in one ranked list (or verticals of one experience), not as parallel unconnected searches.
5. **Results trimmed to the searcher's existing rights** — the platform re-asserts source-system access control; a user discovers only content they could already access in the source systems.

Historical check: appliance/engine-era products (crawler + index + query API, no polished SERP) satisfy this via the API/embedded query surface; the definition does not require SaaS, AI answers, knowledge graphs, or a productized results page. Removal test: remove (1) → web search engine or single-app search; remove (2) → a portal of links or a manual directory; remove (3)/(4) → scattered per-system searches; remove (5) → an internal content crawler, not enterprise search.

### L1 — Common Mature Structure (standard in modern products, not definitional)

- Connector catalog + custom connector path (API/SDK/push); on-prem bridge agents
- Crawl/sync management: scheduling, incremental sync, full recrawl, inclusion/exclusion scoping, sync-frequency configuration
- Metadata/schema mapping across sources; content extraction from common file formats
- Relevance controls: synonyms, query rules, boosting/pinning, semantic/hybrid ranking, activity-signal ranking
- SERP machinery: source-labeled result cards, snippets/previews, verticals, filters/facets, autocomplete, did-you-mean
- Curated answers layer (bookmarks/answers/pins/acronyms) with audience targeting
- People search: profiles, org charts, recent docs/activity, dept/role search; expertise surfacing
- Personal results and search history; personalization from user signals
- Search analytics for admins: top/popular queries, zero-result queries, adoption, feedback loop
- Search APIs/SDKs; embeddable surfaces (app-header box, browser extension, chat assistant)
- Governance: audit logs, tenant isolation, admin roles

### L2 — Variant / Optional Structure

- **Delivery/packaging pole:** platform-embedded (suite search extensible by connectors) ↔ standalone SaaS work-search ↔ engine/infrastructure (customer assembles apps) ↔ intelligent-search platform with build framework
- **Representation strategy:** pre-built unified index vs query-time federation vs hybrid (per-source choice)
- **AI depth:** none / AI answers with citations / full assistant+agent layer on the index
- **Knowledge-graph enrichment depth** (entity/people relations beyond search)
- **Capture breadth:** app connectors only vs plus browser-history/web connectors vs meetings transcripts, code search
- **Deployment:** SaaS / customer-hosted cloud / self-hosted; regional/regulatory posture; certifications
- **Customer segment:** M365-scale suite audience, mid-market work search, large regulated enterprise, developer platform

### L3 — Vendor-specific (kept out of the final document)

- Microsoft: Microsoft Graph as index substrate; Copilot connectors terminology; bookmarks/acronyms/Power BI answer types; verticals/result-types/result-clusters config model; cloud hybrid search; personal search-history mechanics
- Glean: Knowledge Graph; web-history connectors; Go Links; Collections; document verification; `updated:`/`from:`/`my:history` operator vocabulary; Slack/desktop/extension surface set
- Elastic: read-only-replica framing; open-source Python connector service; per-connector DLS support matrix; sync rules; ES|QL; Kibana; Agent Builder
- Sinequa: SBA framework; ChapsVision ownership; neural-hybrid positioning; connector count claims
- Vendor marketing figures (connector counts, ROI numbers, adoption stats) — recorded here only, excluded from the final document as marketing claims.

## Rejected Findings (considered, not promoted)

- *"AI answers are defining"* — rejected: all sampled products added AI layers, but the Type predates them (historical form check) and products remain recognizable without them. AI answers = L1/L2 layer.
- *"Knowledge graph / expertise graph is defining"* — rejected: product-specific depth varies; people search is L1; graphs are L2/L3.
- *"Unified pre-built index is defining"* — rejected: Microsoft federated connectors and Glean live-access mode show the same Type operating without pre-indexed content; canonical concept is "common searchable representation."
- *"Connector counts / catalog size as a Type property"* — rejected: vendor marketing.
- *"Enterprise search requires web-crawling of intranets"* — rejected: crawler is one ingestion mechanism among connectors/APIs/push; not invariant.

## Boundary Findings

| Neighboring Type | Boundary rule ("remove X → becomes that Type") |
|---|---|
| **Internal Knowledge Search** (same §10) | Scope subset: knowledge/content corpora (wikis, KBs, docs) vs organization-wide estate including business records, email, people. Remove the organization-wide multi-source breadth and business-record scope → knowledge-content search. Likely a Variant of Enterprise Search Platform rather than an independent Type — flagged for joint review. |
| **Search Platform** (§13) | Operator/pole distinction: Search Platform serves developers building search into arbitrary applications (no organizational content estate implied); Enterprise Search Platform serves the organization's employees searching the organization's own estate. Engine-pole products (Elastic) legitimately serve both; the packaging pole does not change the Type when the L0 structure targets an organization's estate. |
| **General Web Search Engine** | Content scope: public web, ad-funded, no per-user ACL → remove org-estate scope and permission trimming → web search engine. |
| **Data Catalog** | Object class: metadata about data assets (tables, dashboards, pipelines) for data practitioners vs content/records for everyone → swap object class → data catalog. Some enterprise-search products search metadata too; overlap noted. |
| **Enterprise Content Management** | ECM manages document lifecycle (capture, records, retention, disposal); search is one capability inside it → remove lifecycle/records management, keep discovery → enterprise search. |
| **Intranet Platform** | Intranet is a communication/content surface; search is embedded → remove content authoring/communication, keep unified discovery → enterprise search. |
| **Enterprise Knowledge Assistant / AI assistants** | Interaction model: answers-first conversational surface vs results-first discovery; assistants ground in the search index. Remove the index/ingestion layer → assistant with no enterprise grounding. Convergence risk recorded. |
| **eDiscovery** | User/purpose: legal investigation with holds, exports, chain of custody vs everyday discovery → swap users/purpose → eDiscovery. |
| **Customer-facing site search** | Audience: external shoppers/visitors over one site's catalog vs employees over the org estate → swap audience/scope → site search. |

**Product-pollution check:** every sentence of the final document must survive deletion of product names; vendor vocabularies (Graph, Knowledge Graph, SBA, Copilot connectors, Go Links) appear only in Research Notes.

## Uncertainties

- **Google Cloud Search unreachable** (two timeouts): the SaaS-connector-model pole is evidenced via Microsoft/Glean instead; no Google-specific claims made. Research limitation recorded in final Sources.
- **Historical form** (appliances, engine-era products) kept conceptual: no historical vendor docs fetched; the L0 was broadened deliberately (API/embedded query surfaces count; AI/SaaS not required) rather than asserted from memory.
- **Permission-lag behavior**: Glean documents the query-time "permission snapshot"; Microsoft documents continuous sync. Exact revocation-propagation windows are product- and configuration-specific — final document states the general "index freshness lags source systems" behavior without numeric windows.
- **Personal search history**: directly documented for Microsoft; not verified for others — final document marks it as product-documented behavior, not a universal rule.
- **Whether Internal Knowledge Search should be a separate leaf**: evidence suggests Variant status; recorded in STATUS.md Boundary Issues for joint review rather than unilaterally merged.

## Final Synthesis

An Enterprise Search Platform is the organization's unified discovery layer: it ingests the organization's own content from many heterogeneous systems through connectors that carry content, metadata, and access rights into a common searchable representation (index or live federation), exposes one query surface to members, merges results across sources in relevance-ranked form, and re-asserts the searcher's existing source-system rights on every result. Mature products add connector catalogs, crawl management, relevance controls, source-labeled results pages with verticals/filters, curated answers, people search, personalization from activity signals, admin analytics, and search APIs; current implementations increasingly add AI answers and assistants grounded in — and permission-bound to — the same index. Packaging varies from platform-embedded to standalone SaaS to developer-assembled engine without changing the Type.
