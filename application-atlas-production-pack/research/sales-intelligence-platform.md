# Research Notes — Sales Intelligence Platform

Research date: **2026-09-07**

## Research Goal

Understand what a Sales Intelligence Platform actually is as an Application Type: what it delivers to a selling organization, what its core objects and workflows are, and — critically — how it differs from the sibling leaves of the same market family (Sales Data Enrichment, Contact Discovery, Sales Prospecting) and from adjacent Types (ABM, Competitive Intelligence, Lead Generation, CRM, Revenue Intelligence).

This pass also carries a **joint-review obligation** from the sales-data-enrichment-platform pass (2026-09-07): that pass flagged that enrichment / contact-discovery / sales-intelligence / sales-prospecting may be "one market family behind multiple directory leaves", that vendors self-label the whole family "sales intelligence" (Cognism's flagship line; Lusha's home page), and recommended keep-both on loop direction + primary job or a documented overlap zone. This pass must take a position from the sales-intelligence side.

## Initial Boundary

Working hypothesis at start:

- **Is:** a platform that maintains external intelligence about business companies and people and delivers it to sales organizations as decision support — which targets to pursue, when to act (signals/alerts), and what context to act with (account/people intelligence) — plus the targeting machinery (search, lists, personas, territories) that focuses the intelligence on the customer's market.
- **Closest neighbors:** Sales Data Enrichment (completes records the customer already holds), Contact Discovery (sources net-new records), Sales Prospecting (outreach-preparation workflow), ABM (marketing orchestration over target accounts), Competitive Intelligence (competitor/market knowledge), Lead Generation (capturing net-new demand), CRM (system of record), Revenue Intelligence (internal deal/pipeline mirror), Conversation Intelligence (analysis of the seller's own calls), B2B data providers / DaaS (supply without application).
- **Suspected taxonomy risk (confirmed by prior pass):** the vendor label "sales intelligence" is applied to the whole data family; the directory splits the family into four leaves. This pass defines the intelligence-primary core and resolves the enrichment-side flag; the discovery/prospecting flags remain open until those leaves are processed.

## Research Questions

1. What is the unit of consumption — a record, a list, or a selling decision? What does the seller actually walk away with?
2. What intelligence families exist (firmographics, contact, technographics, intent, news, funding, hiring, relationship)?
3. How is targeting done — search/filters, saved lists, personas, territories, recommendations, scores?
4. How does the timing layer work — alerts, digests, signals, intent — and what triggers delivery?
5. How does account/people research work before outreach (profiles, org charts, relationship paths, AI summaries)?
6. How does intelligence reach action — CRM push, exports, extension, embedded surfaces, engagement handoff?
7. What rules govern the loop (saved-target requirement for alerts, credits, verification, compliance, data currency)?
8. Where are the exact seams vs enrichment, discovery, prospecting, ABM, CI, and pure data providers?
9. Historical check: does the older business-information/dossier era fit the definition, or is the definition over-fitted to the modern alert/AI era?

## Representative Products

Selection rationale: market representativeness + documentation quality + different product philosophies + different customer tiers + coverage of the family-naming question.

| Product | Segment / philosophy | Documentation accessed |
|---|---|---|
| LinkedIn Sales Navigator | Platform-native pole: intelligence over the professional social graph rather than a compiled contact database; relationship-led; no contact-credit unlock model | Tier 1: Help Center (glossary, saved searches, alerts) + Tier 2: product page |
| Apollo.io | Mid-market all-in-one GTM suite (database + engagement + ops); database-led with ICP/signal machinery | Tier 1: developer docs (docs.apollo.io) + knowledge base (knowledge.apollo.io) |
| Lusha | SMB/mid-market, extension-led, self-described "B2B data and intelligence layer"; explicit two-layer data architecture | Tier 1: Knowledge Hub (Search Layer, Deep Intelligence docs) |
| Cognism | EU/compliance-first premium data vendor; flagship product line literally named "Sales Intelligence" | Tier 2: product pages (help center timed out in prior pass; not retried) |
| ZoomInfo | Enterprise owned-database leader; the category's reference point | **Unreachable** (www.zoominfo.com 403 this pass; all four domains 403/transport in the enrichment pass). Recorded as source-access limitation; no claims made. |
| Bombora | Boundary case: pure intent-data co-op, self-described "a data company, not a platform" | Tier 2: product site |

## Sources

- LinkedIn Sales Navigator Help — Glossary — https://www.linkedin.com/help/sales-navigator/answer/a122541 — fetched 2026-09-07 (Tier 1, A)
- LinkedIn Sales Navigator Help — Save lead and account searches — https://www.linkedin.com/help/sales-navigator/answer/a102024 — fetched 2026-09-07 (Tier 1, A)
- LinkedIn Sales Navigator Help — Sales Navigator alerts — https://www.linkedin.com/help/sales-navigator/answer/a105133 — fetched 2026-09-07 (Tier 1, A)
- LinkedIn Sales Navigator product page — https://business.linkedin.com/sell/sales-navigator — fetched 2026-09-07 (Tier 2, B)
- Apollo Developer Docs — index, Capabilities, Find People Using Filters — https://docs.apollo.io/ , https://docs.apollo.io/docs/capabilities.md , https://docs.apollo.io/docs/find-people-using-filters.md — fetched 2026-09-07 (Tier 1, A)
- Apollo Knowledge Base — Save, Share, and Set Alerts for Searches — https://knowledge.apollo.io/hc/en-us/articles/4409803718669 — fetched 2026-09-07 (Tier 1, A)
- Apollo Knowledge Base — Create and Use a Signal — https://knowledge.apollo.io/hc/en-us/articles/13152837789837 — fetched 2026-09-07 (Tier 1, A)
- Apollo Knowledge Base — category structure (Search and Prospect / Buying Intent / Scores / Personas / Territories) — https://knowledge.apollo.io/hc/en-us — fetched 2026-09-07 (Tier 1, A)
- Lusha Knowledge Hub — Search Layer — https://docs.lusha.com/search-layer — fetched 2026-09-07 (Tier 1, A)
- Lusha Knowledge Hub — Deep Intelligence — https://docs.lusha.com/deep-intelligence — fetched 2026-09-07 (Tier 1, A)
- Cognism — Sales Intelligence product page — https://www.cognism.com/sales-intelligence — fetched 2026-09-07 (Tier 2, B)
- Bombora — product site (positioning, Data Co-op, "data company, not a platform") — https://bombora.com/ — fetched 2026-09-07 (Tier 2, B)
- ZoomInfo — https://www.zoominfo.com/ — 403; source-access limitation (consistent with enrichment pass)
- Apollo Buying Intent Overview article — 403 on direct fetch (https://knowledge.apollo.io/hc/en-us/articles/8047704465933); Search Filters Overview also 403; buying-intent capability evidenced indirectly via the alerts article's references and the KB category structure (Tier 1 structure, B for intent specifics)

## Product Observations

### LinkedIn Sales Navigator (evidence layer: A — Tier 1 help center; B — product page)

**Core vocabulary (Glossary, Tier 1):**
- **Account** — "Companies that you already do business with or companies you'd like to pursue and save." The target population is a first-class saved object.
- **Lead** — "A person you already do business with or people you'd like to pursue and save on Sales Navigator."
- **Account Lists / Lead Lists** — "Includes all saved companies / an organized list that includes all saved individuals or leads."
- **Alerts** — "notifications about your saved leads and accounts"; also available inside CRM embedded experiences (Salesforce, HubSpot, Dynamics 365, Oracle Sales, Freshworks, Gong) for Advanced Plus.
- **Buyer Intent** — "key insights on accounts that show intent… reach out to the right people in the right accounts at the right time."
- **Discover** — "receive 'New Matches' based on your sales preferences"; **Recommended Accounts/Leads** — "based on your sales preferences, search history, and profile interactions."
- **Personas** — target buyer definition by function, seniority, job title, geography; used to zero in on the right leads and to filter suggested-lead alerts.
- **Relationship Explorer** — "uncover hidden allies and supporters, find warm paths in, and multi-thread"; **TeamLink** — "view your team's connections… to find the best path to a lead through a 1st degree connection."
- **Account Map** — visualize account relationships, arrange leads in tiers, identify stakeholder gaps.
- **Saved Searches** — saved criteria incl. keyword strings and filters; **Sales Spotlights** — spotlight filters such as "Changed jobs in the last 90 days", "Posted on LinkedIn in 30 days", "TeamLink introduction".
- **Embedded Profiles / CRM Sync** — view LinkedIn/Sales Navigator information inside the CRM; log and import sales activity to/from CRM.
- **InMail** — private messages to anyone on LinkedIn without introduction/contact info; credit-per-send.

**Saved searches (Tier 1):** save criteria → get notified of new matching leads/accounts via weekly emails + homepage alerts; run again anytime; share with colleagues; documented saved-search count limit (50 lead + 50 account searches — vendor number, kept out of final doc).

**Alerts taxonomy (Tier 1 — the most complete signal taxonomy observed):**
- To receive alerts you **must save** the leads/accounts (explicit precondition).
- **Account updates** — account shared a post/article (rate-limited per account per day).
- **Account growth** — preparing to grow (job postings increased over past 90 days), accelerated growth (hiring + headcount YoY), raised money, merger/acquisition event, talent moving in.
- **Account risk** — slowing growth (employee growth decrease over past 90 days).
- **Lead changes** — lead changed jobs / changed roles (requires notification opt-ins).
- **Lead shares / engagement** — lead shared a post; lead engaged with your company's content (organic or sponsored); lead viewed your profile; lead accepted connection; lead viewed your Smart Link.
- **Buyer intent** — employees/leadership of a saved account viewed your company page or website (requires LinkedIn Insight Tag on the website); leadership-level intent distinguished from all-employee intent.
- **New decision makers** — senior hires (director level or above) at a saved account.
- **Shared activity** — colleague shared a list/search, added/removed leads, commented.
- **Suggested leads** — recently viewed lead; account decision makers.
- **CRM updates** — sales lead submitted a CRM form (Advanced Plus + CRM Sync).
- Alerts are bookmarkable with retention (60 days — vendor number, kept out of final doc).

**Product page (Tier 2):** positioning "Find the right buyers, grow your pipeline, and close deals faster"; three-pillar feature story (find the right people / engage effectively / elevate every conversation); 50+ search filters over "1+ billion members"; AI features (Account IQ — AI account insights and account plans; Lead IQ — AI buyer summaries; Message Assist — AI drafts); CRM integrations incl. Lead/Contact Creation to CRM (Advanced Plus); mobile apps; admin/usage reporting; plan-gating of features (documented per-feature tier notes).

### Apollo.io (evidence layer: A — Tier 1 docs + KB)

**Positioning (developer docs):** "Search, enrich, create, and manage Apollo data programmatically"; database of "hundreds of millions of people" (docs claim 240M+ contacts in MCP/CLI descriptions — vendor number); MCP/CLI supply the same database to AI tools.

**Search & targeting (Tier 1):**
- People search endpoint filters by job title, location, seniority, company, industry; returns availability indicators (`has_email`, `has_direct_phone`, organization firmographic availability) and `last_refreshed_at` per record — data currency is surfaced per record.
- Companies search endpoint; organization job postings endpoint; news articles search endpoint (signal families exposed via API).
- **Saved searches** — save filters for people/companies/deals/tasks; share with visibility levels (restricted / everyone / specific people with can-edit/can-view); admin can manage sharing and team-wide defaults.
- **Search alerts (subscription alerts)** — daily/weekly/monthly email notifications "of the newest people or companies that fit your saved search criteria"; docs recommend combining the buying-intent filter with alerts ("get notified when new companies match your buying intent criteria").
- **Signals (Scores category)** — "Signals enable you to prospect based on the demographic and behavioral filters that are most important to you… consistent, repeatable criteria." Created under Settings → Ideal customer profile → Signals; target People or Companies; built from filters (e.g., # employees, revenue); can carry **talking tips/snippets** ("Communication guides help prepare your team to engage with prospects who match the signal"); usable as search filters, as criteria inside custom scores (with assigned impact), and in the Chrome extension ("Compatibility check" showing score/signals on person/company views). Apollo ships default signals; custom signals allowed.
- **Personas** — create and use personas; **Suggested Leads** — recommendation surface.
- **Territories** — "Create Territories to Control Prospecting Access" (org-level targeting governance).
- **Buying Intent** — KB category (Buying Intent Overview; Use Buying Intent to Prioritize Prospects; Track Website Visitors; Use Website Visitors Data). Direct article fetch 403'd; capability evidenced via KB structure + alerts article references. Bombora's partner list includes Apollo (observed on bombora.com), consistent with third-party intent supply.
- **Scores** — Scores Overview; custom scores combining filters/signals with impact weights; score filters to tighten lists.

**Engagement adjacency (Tier 1 KB structure):** Sequences, Dialer, Tasks, Meetings, Email deliverability, Conversations (call recording/coaching), Deals, Workflows (incl. "Automate Lead Prioritization", "Account-based Sales Motion"), Enrichment (incl. CRM Enrichment, Waterfall, Data Health Center), Analytics. Apollo is the suite-drift pole: intelligence + engagement + enrichment + deals in one product.

**Data supply notes (from enrichment pass, reused):** Living Contributor Network (data sharing program), removal-request handling, credit metering, email verification states.

### Lusha (evidence layer: A — Tier 1 Knowledge Hub)

**Two-layer architecture (docs portal, Tier 1):**
- **Search Layer** — "Lusha's core data API — 78 verified contact and company fields plus real-time buying signals… Use it to search, enrich, and prospect at scale." Two data categories:
  - **Data Points** — "static, verified attributes — contact identity, employment history, emails, phones, and company firmographics… refreshed continuously" (documented refresh cadences: weekly for most fields, monthly for some).
  - **Signals** — "event-driven triggers — headcount changes, job moves, promotions, hiring surges, website traffic shifts, and news events. Signals fire when something meaningful changes and can be polled or streamed depending on your plan." 26 documented signal types across contacts and companies: moved to a new company, promotion, headcount changes over 1M/3M/6M/12M windows (increase/decrease), hiring surges (overall/by department/by location), new job post, website traffic increase/decrease, IT spend increase/decrease, LinkedIn activity intent, and six news families (commercial activity, corporate strategy, financial events, market intelligence, people, product activity, risk).
  - Scale claims (vendor numbers): 290M contacts, 28M companies; four endpoints (`/search`, `/enrich`, `/search-and-enrich`, `/prospecting`) for both contacts and companies.
- **Deep Intelligence** — "pairs your data with AI to deliver recommendations and predictive scores tailored to your ICP":
  - **Recommendations** — "AI-driven contact and company recommendations tailored to your ICP. Refreshes as your usage patterns evolve — the more you engage, the sharper the recommendations get."
  - **ICP Hub** — "Ideal Customer Profile matching and scoring hub. Consolidates fit signals into a single workspace and ranks accounts by likelihood-to-buy so reps work the right list first."
  - **Lookalikes** — "AI-powered discovery of contacts and companies similar to your best existing customers."
  - **Website Visitors** — "Intent signal derived from website visit activity matched to known companies in our identity graph. Surface accounts showing interest before they fill out a form."
  - **Predictive Scoring (TOF/MOF)** — "likelihood-to-convert scores based on historical conversion patterns from the Lusha network and your own pipeline data."

**Platform surfaces (docs portal):** workspace tables (AI-chat table building), Chrome extension for prospecting, Engage (sequences — engagement adjacency), CRM integrations, API/webhooks/MCP ("connect Claude, ChatGPT, or any MCP-compatible AI assistant to the same verified data" — from enrichment pass), team management (roles/permissions), security/legal.

**Positioning (from enrichment pass, reused):** home page self-labels "B2B data and intelligence layer for GTM teams and AI agents… Find, enrich, and reach the right person"; FAQ distinguishes its signals from "anonymous intent data" ("named, dated signals tied to a specific account").

### Cognism (evidence layer: B — Tier 2 product pages)

**Flagship product line literally named "Sales Intelligence"** — "The revenue growth centre for GTM teams": "Turn your market into a list of the accounts and contacts that matter. Cognism connects your teams to the decision-makers you need to grow your business. With account buying signals and verified mobile numbers your teams never miss a window of opportunity."

**Documented workflow (product page, five steps):**
1. **Build your target lists & persona** — "refine your target audience with precision segmentation… set up the key personas you know convert."
2. **Standardise best practices** — "Assign target companies and personas to your chosen teams to keep reps focused on the right things."
3. **Discover new opportunities** — "The browser extension combines buying signals with quality contact data, and works over LinkedIn and websites."
4. **Accelerate outreach with AI** — "AI Search and research tool enable sellers to speed up their prospecting, by searching, preparing and dialling faster."
5. **Export and action, fast** — "Integrate with leading CRM or sales engagement tools and keep the conversation flowing."

**Decision-support language (product page):** "Surface company context, signals and targeting intelligence so reps know **who to contact, when to engage and what to say**." "Surface daily recommendations for high-value accounts and contacts to uncover new opportunities." RevOps: "Set team-wide workflows, target markets, and personas to ensure alignment. Monitor performance with admin-level dashboards."

**Data supply (from enrichment pass, reused):** data fusion engine, phone-verified mobiles as premium differentiator, compliance-first posture (DNC coverage in Europe), CRM Enrichment as a separate product line, DaaS delivery.

### ZoomInfo (limitation)

www.zoominfo.com returned 403 this pass; the enrichment pass already recorded all four official domains unreachable (help/knowledge/api/www). ZoomInfo is the enterprise owned-database reference for the category (two sampled vendors publish direct comparison pages against it), but **no first-hand observation was possible; no claims about ZoomInfo internals are made anywhere in the outputs.**

### Bombora (boundary case, Tier 2)

- Self-description: "**Bombora is a data company, not a platform.** Whether you use one Bombora solution or the entire suite, we empower teams to activate, measure, and scale go-to-market strategies exactly where you already work." And: "We deliver our data where you already work: directly into your CRM, MAP, and ad tech stack. **No new infrastructure, no new workflows.**"
- Supply: B2B Data Co-op ("thousands of trusted and influential B2B data sources"; "86% of the data in our Co-op is shared exclusively with Bombora" — vendor numbers); Company Surge® Intent data (intent topics taxonomy, 21,600+ topics claimed); identity/enrichment (website visitor identification); digital audiences; campaign measurement; insights suite.
- Use cases listed include sales outreach and ABM activation — i.e., the *consumption purpose* is selling/marketing decisions, but the delivery is data-into-your-stack, not a seller-facing application.
- Partner list includes Apollo, Cognism, LinkedIn, Demandbase, RollWorks — i.e., intent data is a *supply* to sales-intelligence platforms, not itself the platform.

This product anchors the boundary: **a signal/data supply without the seller-facing application surface is a data provider, not a Sales Intelligence Platform.**

## Cross-product Comparison

| Dimension | Sales Navigator | Apollo | Lusha | Cognism |
|---|---|---|---|---|
| Intelligence substrate | professional social graph (member profiles, connections, content, company pages) | owned compiled contact/company database (+ third-party intent) | owned verified database (Search Layer) | owned database via "data fusion" sourcing + verification layers |
| Target population as managed object | saved Accounts/Leads + Account/Lead Lists + Personas | saved searches + ICP Signals + Territories + Personas | ICP Hub + workspace tables + lookalikes | target lists + personas assigned to teams |
| Search & filtering | 50+ filters (vendor claim), Boolean/keyword, Spotlights | filter families incl. intent; signals as filters | /search + /prospecting endpoints; extension search | precision segmentation; AI Search |
| Timing layer | Alerts feed (account growth/risk/news, lead job changes, buyer intent, new decision makers, shared activity, CRM updates); saved-search notifications | search alerts (daily/weekly/monthly); signals; scores | 26 named real-time signals (poll/stream); website visitors | buying signals; daily recommendations |
| Recommendation machinery | Discover, Recommended Accounts/Leads, Suggested Leads, Persona-filtered alerts | Suggested Leads; custom scores (signals × impact) | Recommendations, Lookalikes, ICP Hub ranking, Predictive Scoring | daily recommendations for high-value accounts/contacts |
| Account/people research surface | Account page, Account Map, Relationship Explorer/Map, TeamLink paths, Account IQ/Lead IQ (AI) | person/company pages; extension "Compatibility check" | company/contact profiles; extension | company context; extension over LinkedIn/websites |
| Contact-data access | no contact-email unlock model; InMail outreach instead (Lead/Contact Creation to CRM on top plan) | emails/phones with verification states; credits | verified emails/phones with scores; credits | phone-verified mobiles as premium differentiator |
| Handoff to revenue stack | CRM Sync, Embedded Profiles/Experiences, Lead/Contact Creation | CRM integrations, CSV, API, workflows, native engagement | CRM push integrations, API/webhooks/MCP | CRM/engagement integrations, extension push |
| Team machinery | shared lists/searches, admin center, usage reporting | territories, permission profiles, shared searches w/ access levels | roles/permissions, team management | team assignment of targets/personas, admin dashboards |
| AI posture | Account IQ, Lead IQ, Message Assist | AI assistant/research, MCP/CLI supply to AI tools | AI recommendations/scoring, AI-chat tables, MCP | AI Search, AI research tool |
| Engagement bundled? | light (InMail messaging only) | full suite (sequences, dialer, tasks, deals, conversations) | Engage (sequences) | no (integrations to engagement tools) |
| Enrichment bundled? | CRM record auto-fill on top plan (Lead/Contact Creation) | full enrichment pillar (CRM enrichment, waterfall, data health) | /enrich endpoint + CRM auto-update | separate CRM Enrichment product line |
| Compliance posture | platform data policies; regulatory-compliance partners (financial services) | GDPR/CCPA statements; removal requests | audited certifications (GDPR/CCPA, SOC 2, ISO) | compliance-first; DNC coverage in Europe |

**Vocabulary caution (important for abstraction):** "signal" does not mean the same thing across products. In Apollo, a Signal is a **saved targeting-criteria set** (ICP-scoped demographic/behavioral filters, optionally with talking tips). In Lusha, Signals are **event triggers** (dated changes). In Sales Navigator, the event layer is called **Alerts** and the criteria layer is called **Spotlights/Personas/Saved Searches**. In Cognism, "buying signals" is marketing language covering both. The canonical abstraction must therefore separate three concepts: **targeting criteria** (who fits), **change events** (what changed), and **delivered triggers** (what the seller is told, when). No single vendor term maps to all three.

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product is not a sales intelligence platform:

1. **An external entity intelligence supply** — a maintained store of structured intelligence about business companies and people (firmographics, roles/contactability, technologies, funding, hiring, news, intent, relationships), compiled and kept current by the vendor, not the customer. The platform is a lens over data the customer does not own. *(Remove → reporting/analytics over the customer's own CRM data.)*
2. **A managed target population** — the customer's selling targets (companies/accounts and the people at them) held in the platform as saved, organized, shareable objects (lists, saved searches, personas, territories), which focus the supply on the customer's market. *(Remove → a raw data publisher or one-shot lookup service; the standing population is what makes the intelligence the customer's.)*
3. **The decision-delivery loop** — the platform continuously converts supply + population into seller-facing decision support: which targets merit attention (qualification/recommendation), what changed that creates a reason to act now (signals/alerts), and the context to act with (account/people intelligence). The unit of consumption is the selling decision and conversation preparation — not a completed record. *(Remove → a data supply without an application = a B2B data provider / DaaS, per Bombora's own self-description.)*

All three are necessary. Remove the external supply → CRM analytics; remove the managed population → data publisher/lookup; remove the delivery loop → data supply without application.

Not in L0: contact databases, intent data, AI, browser extensions, credits, CRM sync, org charts, phone-verified data, engagement tooling, enrichment.

**Historical / market-sample check:** the core pattern — a vendor-maintained body of business intelligence consumed by sellers to decide whom to pursue and how to approach them — predates the modern SaaS category: business-information/dossier services (company profiles, firmographic registries, compiled contact directories) served exactly this consumption job, and list-building/periodic-update services realized the managed-population structure without any of today's machinery. Intent data, AI summaries, extensions, credits, CRM sync, and website-visitor identification are modern realizations, not definitional. Check passed — the definition does not depend on the current alert/AI era.

### L1 — Common Mature Structure

- **Search & filtering** over the supply against ICP criteria (firmographics, seniority/function, geography, technology, funding).
- **Saved searches / lists with sharing** and team collaboration; personas as reusable target-buyer definitions; territories as org-scoped targeting governance.
- **Signal/alert layer**: dated change events on saved targets (job changes, hiring surges, funding, leadership additions, news, intent spikes, website visits) delivered as notifications, digests, or feeds.
- **Recommendation & scoring machinery**: suggested leads/accounts, lookalikes, relevance ranking, likelihood-to-buy/convert scores combining signals with impact weights.
- **Account/people intelligence views**: profile pages aggregating firmographics, contacts/decision-makers, org structure, news, technology, and relationship paths.
- **Handoff to the revenue stack**: save/push records to CRM, exports, embedded profiles inside CRM pages, sync of activity.
- **Browser extension** surfacing intelligence over LinkedIn, company websites, and CRM records.
- **Contact-data access with verification states and usage metering** (in database-led products; the graph-native pole substitutes messaging reach instead).
- **Team/organization machinery**: shared lists/searches with access levels, admin governance, usage reporting.
- **AI assistance**: account/lead summaries, drafting, research agents; supply of the same intelligence to third-party AI tools (MCP-style).

### L2 — Variant / Optional Structure

- **Intelligence substrate**: compiled contact database vs professional-graph-native vs provider-network aggregation vs intent co-op supply.
- **Signal families emphasized**: firmographic events vs intent (co-op/web) vs relationship events vs web-visitor identification.
- **Contact-data depth**: full contact export with credits vs no-export relationship intelligence (outreach via platform messaging instead).
- **Suite drift**: intelligence-only vs bundled engagement (sequences/dialer/deals) vs bundled enrichment as a separate pillar/product line.
- **Regional/compliance orientation**: EU phone-verified + DNC-led vs global; certification bundles as differentiators.
- **Customer tier**: self-serve SMB (extension-led, free tiers) vs mid-market suites vs enterprise (governance, DaaS, procurement-level compliance).
- **AI posture**: AI features as assistive layer vs AI-native repositioning vs supply-to-AI-agents.

### L3 — Vendor-specific (research notes only)

- Sales Navigator: InMail credit model; TeamLink/TeamLink Extend; Account Map; Smart Links; bookmarked-alert retention (60 days); saved-search count caps (50+50); per-feature plan gating; Social Selling Index.
- Apollo: Signal = saved ICP criteria set with talking tips/snippets; default signals; custom scores with signal impact weights; territories controlling prospecting access; Living Contributor Network; MCP/CLI; 240M+ contact claim; waterfall enrichment invariant (Apollo first).
- Lusha: Search Layer (78 fields, 26 named signals with documented refresh cadences) vs Deep Intelligence (Recommendations/ICP Hub/Lookalikes/Website Visitors/Predictive TOF-MOF) split; 290M/28M scale claims; MCP docs.
- Cognism: phone-verified premium tier; data-fusion sourcing description; five-step workflow; "who to contact, when to engage and what to say" positioning; DNC Europe.
- Bombora: Data Co-op exclusivity claim (86%); Company Surge®; 21,600+ intent topics claim; "data company, not a platform" self-description.
- ZoomInfo: none observed (unreachable).

## Vendor-specific Findings

See L3. None promoted into the final document. The "signal" vocabulary divergence (criteria-set vs event vs notification) is recorded here and handled in the final document by describing the three underlying concepts generically.

## Boundary Findings

**vs Sales Data Enrichment Platform** — JOINT REVIEW FLAG FROM THE ENRICHMENT PASS, DISCHARGED FROM THIS SIDE. Adopted discriminator = **direction of the loop + primary job** (as pre-agreed by the enrichment pass): enrichment starts from records the customer already holds and completes them (match-and-append, write-back); sales intelligence starts from the customer's market and equips selling decisions over a managed target population (targeting → timing → context). The unit of work differs: a completed record vs a selling decision. Overlap zone documented: signals appear on both sides (enrichment attaches job-change signals as record attributes; SI delivers them as decision triggers), and SI products ship enrichment as a capability (Apollo's enrichment pillar, Cognism's CRM Enrichment line, Lusha's /enrich). **Keep-both.** Vendor naming does not respect the split (Cognism's flagship "Sales Intelligence" line is a prospecting-data product; Lusha self-labels "data and intelligence layer") — recorded; the directory split is by primary job, not by vendor label.

**vs Contact Discovery Platform** — same substrate (external business data supply), different primary job: discovery's unit of work is sourcing net-new records the customer does not hold (search → produce records for outreach lists); SI's unit of work is standing decision support over the target population (whom/when/why + context). In practice every database-led SI product ships discovery-style search, and the seam is the softest in the family. **Joint review remains flagged** (that leaf is unprocessed); this pass's position: keep-both on primary job, with the managed-target + delivery-loop structure as the SI-side discriminator.

**vs Sales Prospecting Platform** — prospecting is the outreach-preparation workflow (build lists → find contacts → hand to engagement); SI is the intelligence layer that feeds it (which accounts, when, with what context). Products bundle both. **Joint review remains flagged** (leaf unprocessed).

**vs ABM Platform** — consistent with the ABM pass: SI serves sellers (target discovery, signals, outreach context); ABM serves marketing orchestration and account-level measurement over a target account list. Suites bundle both (Bombora's partner list shows the same intent supply feeding both). Remove activation + marketing measurement → SI.

**vs Competitive Intelligence Platform** — consistent with the CI pass: SI supplies intelligence about **prospect** targets for selling decisions; CI supplies knowledge about **competitors and the market** for strategy and deal defense. They meet at "account triggers". Replace prospect targets with tracked competitors → CI.

**vs Lead Generation Platform** — lead gen captures net-new demand (forms, ads, campaigns); SI equips decisions about the existing market. Form-fill/website-visitor identification sits at the seam (Lusha Website Visitors, Sales Navigator Buyer Intent via Insight Tag) but is delivered inside SI as a targeting signal, not as demand capture.

**vs CRM** — CRM is the system of record for relationships, deals, and activities; SI is a lens over external market intelligence that feeds CRM records and embeds surfaces inside CRM pages. CRM-native intelligence features are capability realizations, not the Type.

**vs Revenue Intelligence Platform** — revenue intelligence mirrors the organization's **own in-flight deals** (CRM sync + captured engagement + derived pipeline health/forecast); SI looks **outward** at the market (external entities, signals, targets). Inward mirror vs outward lens.

**vs Conversation Intelligence Platform** — conversation intelligence analyzes the seller's **own customer conversations** (calls/meetings); SI supplies intelligence about **external prospects**. Different data direction entirely.

**vs B2B data providers / DaaS (e.g., intent co-ops)** — a supply without the seller-facing application (no managed targets, no delivery loop) is a data company, not a sales intelligence platform (Bombora's own self-description is the anchor). DaaS is a delivery variant of the data supply, not the Type.

## Uncertainties

- ZoomInfo internals unverified (all official domains unreachable across two passes); the enterprise owned-database pole is represented indirectly (competitor comparison pages, Bombora partner list). No claims made.
- Apollo's Buying Intent mechanics come from KB structure + cross-references (direct article fetches 403'd); intent specifics (scoring semantics, topic supply) not asserted.
- Cognism evidence remains marketing-tier only (help center timed out in the prior pass; not retried per network rules); operational mechanics not asserted.
- Whether the managed-target population is strictly definitional for the historical dossier era: the dossier/reference era clearly satisfies the external-supply + selling-decision core; list-building/periodic-update services are the documented-era realization of the population structure, but specific historical product features were not directly verified — the historical check is argued at the conceptual level.
- Exact alert-cadence defaults, credit prices, list-size caps, and refresh intervals are vendor numbers kept in research notes only.

## Final Synthesis

A Sales Intelligence Platform is defined by three structures: **an external, vendor-maintained intelligence supply about business companies and people**, focused on **a managed target population** (saved accounts/leads, lists, personas, territories), and converted continuously into **seller-facing decision support** — who merits attention, what changed that makes now the time to act, and the context to act with — then handed off into the revenue stack. The unit of consumption is the selling decision, which separates the Type from enrichment (completed records), discovery (sourced records), and prospecting (outreach workflow); the application surface separates it from pure data providers. The market family shares one substrate and vendors bundle all four jobs; the directory keeps the leaves distinguished by primary job, and the enrichment-side joint-review flag is discharged on that basis while the discovery/prospecting flags remain open.
