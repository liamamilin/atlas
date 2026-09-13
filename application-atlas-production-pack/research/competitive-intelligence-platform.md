# Research Notes — Competitive Intelligence Platform

Research date: 2026-09-07
Slug: competitive-intelligence-platform
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

---

## Research Goal

Understand what a Competitive Intelligence Platform actually is as an application type: what objects exist inside it, how intelligence enters and moves through it, who operates it and who consumes its output, what lifecycle and rules matter, and where its boundary sits against neighboring marketing/sales research types.

## Initial Boundary (hypothesis before research)

- It is an internal-facing (organization → its own employees) intelligence application, not an external research service.
- It is organized around tracked external entities — competitors first — not around the organization's own brand mentions (→ Media Monitoring) or around consumer studies (→ Market Research).
- It runs a standing loop: collect → filter/curate → package → distribute — not a one-off study.
- Nearest neighbors: Market Research Platform, Consumer Research Platform, Media Monitoring Platform, Social Listening Platform, Sales Enablement Platform, Sales Intelligence Platform, SEO Platform (digital measurement), Financial Market Data Terminal.

## Research Questions

1. What are the core objects? (tracked competitor, source, intelligence item, battlecard, dashboard, digest…)
2. How does intelligence enter the system? (automated monitoring, internal contributors, analyst research, purchased data)
3. How is raw intelligence processed into usable knowledge? (filtering, tagging, AI summaries, profiles)
4. How is knowledge packaged and distributed? (battlecards, newsletters, dashboards, alerts, embeds)
5. Who uses it, in which roles? (operator vs consumer vs contributor)
6. What lifecycle/state do intelligence items and deliverables have?
7. What is measured? (adoption, revenue influence, win/loss)
8. Where is the boundary against market research, media monitoring, social listening, sales enablement, sales intelligence?

## Representative Products

Selected for market representativity + different product philosophies + different customer tiers:

| Product | Philosophy | Tier / Segment |
|---|---|---|
| Klue | Competitive-enablement-first; CI + win-loss suite; agent/AI-led; deep CRM/chat delivery | Enterprise B2B |
| Crayon | Intelligence-to-enablement pipeline (Aggregate → Organize → Publish → Enable → Measure) | Mid-market → enterprise |
| Contify | Market-and-competitive intelligence (M&CI); source/coverage breadth first; analyst services + news API | Mid-market → enterprise, incl. non-tech industries (pharma, BFSI, manufacturing, consulting) |
| Kompyte | Competitor-tracking-first with battlecards; "an hour a week" automation positioning | SMB → mid-market; owned by Semrush |

Rejected/deferred samples: Similarweb / Semrush core (digital measurement — different Type), AlphaSense (investment/market research terminal — different Type), Highspot/Seismic (sales enablement content systems — different Type, integration partners of CI products). Not fetched; kept out of evidence.

## Sources

All fetched live 2026-09-07. All vendor surfaces below were reachable; vendor help-center subdomains (support.klue.com, help.kompyte.com) were NOT reachable (transport error); Crayon help center (help.crayon.co) returned an empty shell page; contify.com/how-it-works returned HTTP 503. Deep operational detail below therefore comes from vendor product pages and platform pages rather than authenticated help-center articles — assertion strength is calibrated accordingly (no precise limits, cadences, or plan-gated features asserted).

- Klue — https://klue.com/ (homepage), https://klue.com/compete-agent (product page)
- Crayon — https://www.crayon.co/ (homepage), https://www.crayon.co/product/organize (product page)
- Contify — https://www.contify.com/ (homepage), https://www.contify.com/platform/ (platform page incl. FAQs)
- Kompyte — https://www.kompyte.com/ (homepage), https://www.kompyte.com/kompyte-competitive-intelligence-automation-ai (AI features page)

---

## Product Observations

### Klue (evidence layer A — direct, from klue.com and klue.com/compete-agent)

- Self-description: "a platform used by competitive professionals to monitor their competitive landscape and enable individuals in their organization with competitive insights and content."
- Compete Agent positioned as "AI research analyst + deal assistant": continuously collects and analyzes intel → auto-generates insights, creates competitor profiles, uncovers trends.
- Deal Assistant: "continuously monitors competitive activity across open opportunities and proactively delivers actionable insights" to sellers; Q&A answered in Slack ("Ask Klue" — answers in Slack, Salesforce, and Klue).
- Named surfaces: Knowledge Hub (consistent messaging/positioning), Competitor Profiles (AI-generated), Klue Insights (auto-analyzed from G2 reviews and win/loss interviews), Deal Tips (deal-specific insights to inbox), Email Digests (intel digests on a regular cadence).
- Battlecards: "build dynamic battlecards … for Tier 1 competition"; battlecards updatable by curators/PMMs; even via LLM conversation ("Update the Acme Corp battlecard — we just closed a win on this exact pricing objection").
- Company context: upload internal docs / GTM context to ground the intelligence.
- Win-loss suite: buyer interviews (human analysts, AI interviewer, "blindspots" interviews from lost evaluations), Win & Loss Story Agent auto-generated from CRM data + call recordings the moment a deal closes.
- Measurement: Klue Reports — threats to pipeline, adoption of competitive content, revenue influence.
- Delivery surfaces: Slack, Salesforce; MCP server / Claude directory (intelligence consumable by internal LLMs, with cited answers).
- LLM-facing query examples: competitive positioning, objection handling, win/loss patterns, buyer voice, deal-specific intel, claim validation.

### Crayon (evidence layer A — direct, from crayon.co homepage and /product/organize)

- Product framed as a five-stage pipeline: Aggregate → Organize → Publish → Enable → Measure (+ Analyze marketing pages). This is a near-canonical articulation of the type's loop.
- Homepage: "monitors your competitors and alerts you to relevant intel"; insights to inbox ("start your day by reviewing the high-priority insights"); AI news summarization; AI importance scoring (sort insights high→low).
- Content creation: battlecards delivered in Salesforce, Slack, Highspot "and other tools"; announcements ("spotlight recent insights and battlecard updates"); newsletters.
- Sales enablement: intel in Salesforce/Slack; team leaderboard (winners of competitive deals); 1:1 coaching on performance vs competition.
- Measurement: win/loss analysis (which competitors cause trouble), engagement data (who uses battlecards and effect on competitive deals), influenced revenue.
- Organize page: Sparks (AI assistant, pre-built templates or custom prompts, schedulable recurring runs); Call Clips (finds competitive moments in call recordings — Gong integration — and summarizes); Saved Searches (create, store, automate searches across competitors; "reliable stream of relevant insights"); Labels ("organize, retrieve, act on competitive intelligence… accessible to the right stakeholders").

### Contify (evidence layer A — direct, from contify.com and contify.com/platform)

- Self-description: "AI-native market and competitive intelligence (M&CI) platform … decision-ready insights on your market, industry, competitors, key accounts, and other strategic entities."
- Collection: proprietary web crawlers over 1M+ vetted sources (news, company websites, SEC filings, social); add your own sources via a built-in sourcing module; internal sources — SharePoint documents, sales-call transcripts from Gong/Fireflies, first-hand intel from customer-facing teams via Slack, MS Teams, Email.
- Coverage: 700,000+ companies, 100+ industry segments; 117+ languages auto-translated; two years historical data.
- Processing: "AI-driven 7-step curation process, deduplication, and human oversight"; business facts auto-extracted from articles; Athena AI (agentic engine) derives "insights" from multiple facts; Ask Athena answers ad-hoc questions grounded on curated intelligence datasets; Knowledge-Graph-based accuracy controls; custom fact & insight prompts.
- Organization: custom tags on top of hundreds of pre-configured standard tags; custom taxonomy; custom KIQs (key intelligence questions) per the FAQ.
- Delivery: newsfeeds (global, curated, smart filters by company/business event/content type/location); automated alerts; personalized newsletters with user commentary + engagement analytics; role-specific dashboards (auto-updating widgets; template library); automated battlecards "powered by AI and real-time data"; embeddable widgets (HubSpot, Power BI); integrations with Slack, MS Teams, Salesforce.
- Dashboard widget types named in FAQ: battle cards, win-loss analyses, company profiles, market landscape, word clouds, benchmarking comparisons, auto-updating knowledge graphs.
- Business model notes: unlimited-user access positioning; bundled analyst hours (managed services: secondary research, custom reporting, dashboards, battlecard creation); Business News API sold as a separate data product.
- Users named by function: M&CI/research/strategy professionals, sales, marketing, product; industries: IT, pharma, BFSI, consulting, manufacturing.

### Kompyte (evidence layer A — direct, from kompyte.com and its AI page)

- Self-description: "Competitive Intelligence and Sales Battlecards Software" (by Semrush).
- Tracking: "automatically tracks your competitors' updates across hundreds of sources and millions of data points including: websites, reviews, content, social, ads, job postings"; positioning "an hour a week is all you need".
- AI: filters noise, surfaces "actionable updates"; AI Daily Summaries (one daily roundup, filterable by update type or competitor, trainable with preferences); AI Auto Summarize on any insight incl. PDFs and win/loss reports, with edit/regenerate.
- Battlecards: "always up-to-date Battlecards that live where your sales teams work"; sales-ready templates curating "key intelligence from any source"; "bi-directional CRM and sales tool integrations".
- Integrations shown: Salesforce, HubSpot, Slack, Microsoft Teams, Google Drive, OneDrive, Highspot, Showpad.
- Measurement: battlecard adoption; "automated win/loss calculations"; competitive revenue, competitor frequency, win rates "with and without battlecards"; win/loss interview takeaways (via research partner IcebergIQ) populate Reports and Battlecards.

---

## Cross-product Comparison

| Structure | Klue | Crayon | Contify | Kompyte | Evidence |
|---|---|---|---|---|---|
| Tracked external entities (competitors) | yes | yes | yes (+ accounts, industry, strategic entities) | yes | A (4/4) |
| Automated external collection (websites/news/social/reviews) | yes ("continuously collects") | yes | yes (proprietary crawlers, 1M+ sources) | yes (hundreds of sources) | A (4/4) |
| Internal/conversational sources as intel input | yes (CRM data, call recordings, G2/win-loss interviews) | yes (call recordings via Gong) | yes (SharePoint, Gong/Fireflies transcripts, Slack/Teams/Email submissions) | partially (win/loss reports; interview takeaways via partner) | A (strong 3/4, partial 4/4) |
| AI filtering/summarization/importance | yes | yes (summarization, importance scoring) | yes (facts→insights, Ask Athena) | yes (daily summaries, auto-summarize) | A (4/4) |
| Human curation layer | yes (curators/PMMs update battlecards) | yes (labels, saved searches, Sparks scheduling) | yes (7-step curation + human oversight; custom tags/taxonomy) | yes (train AI with preferences; edit summaries) | A (4/4) |
| Competitor profiles | yes (AI-generated) | implied (organize stage) | yes (dashboard widget "company profiles") | n/f (not directly observed) | A (2–3/4) |
| Battlecards | yes (dynamic, Tier 1) | yes (in Salesforce/Slack/Highspot) | yes (automated, AI-powered) | yes (flagship) | A (4/4) |
| Alerts / digests / newsletters | yes (Deal Tips, Email Digests) | yes (inbox insights, newsletters, announcements) | yes (alerts, newsletters with commentary) | yes (AI daily summaries shared) | A (4/4) |
| Dashboards/reports | yes (Klue Reports) | yes (measure stage) | yes (role-specific dashboards, widget library) | yes (reports; win/loss analytics) | A (4/4) |
| Delivery into CRM / chat / enablement tools | yes (Slack, Salesforce; MCP/LLM) | yes (Salesforce, Slack, Highspot) | yes (Slack, Teams, Salesforce; embeddable widgets) | yes (bi-directional CRM + Highspot/Showpad) | A (4/4) |
| Win/loss analysis | yes (suite: interviews + stories) | yes (which competitors hurt; influenced revenue) | yes (dashboard widget) | yes (automated calcs + partner interviews) | A (4/4) |
| Adoption/engagement measurement | yes | yes (who uses battlecards) | yes (user analytics on reports) | yes (battlecard adoption) | A (4/4) |
| Market breadth beyond competitors (customers, suppliers, industry) | secondary | secondary | primary positioning ("360°") | secondary | A — differentiating emphasis |
| Analyst/managed services | yes (win-loss analyst team) | n/f | yes (bundled analyst hours) | partner (IcebergIQ) | A (partial) |
| Data/API supply as product | n/f (MCP/LLM exposure instead) | n/f | yes (Business News API) | n/f | A (1/4) |
| Non-tech industry packaging | n/f | n/f | yes (pharma, BFSI, consulting, manufacturing) | n/f | A (1/4) |

n/f = not found on the fetched surfaces (absence of observation, not evidence of absence).

### Stable commonalities (candidate canonical structures)

1. A maintained list of tracked external entities, competitors at the center.
2. Continuous or recurring collection of discrete intelligence items about those entities from external sources (and, commonly, internal artifacts).
3. A filtering/curation layer that converts raw items into organized knowledge (tags/taxonomy, summaries, profiles, battlecards, dashboards) — AI-assisted but with human oversight present in all four.
4. Recurring distribution of that knowledge to internal consumers in their work context (alerts, digests, in-app views, embedded cards in CRM/chat/enablement tools).
5. Program measurement (consumption/adoption, competitive win/loss, revenue influence) closing the loop.

### Stable roles (cross-product)

- Operator/curator: competitive-intelligence manager, product marketing, analyst — maintains sources, tags items, authors/updates battlecards, sends digests. (4/4)
- Consumer (primary): sales reps / account teams — receive deal-relevant intelligence, read battlecards, ask questions. (4/4, most explicit in Klue/Kompyte)
- Consumer (secondary): product, marketing, strategy/executive teams — dashboards, trends, reports. (explicit in Contify; present in others' measurement/reports)
- Contributor (implicit→explicit): customer-facing teams feeding field intel — directly documented in Contify (Slack/Teams/Email) and Klue (call recordings/CRM data as ingested artifacts). Employee-initiated submission as a first-class flow is only directly documented in one product (Contify) → keep as common-but-not-universal.

---

## Abstraction Hierarchy

### Level 0 — Defining Invariant (deliberately minimal)

A Competitive Intelligence Platform is an internal intelligence system that holds, at minimum:

1. **Tracked external entities** — a maintained set of competitors (extensible to customers, partners, suppliers, market segments) that the organization monitors. Remove it → the system tracks the organization's own brand (Media Monitoring / Social Listening).
2. **Collected intelligence items** — discrete captured updates/observations/reports about those entities, from external monitoring, internal artifacts/contributors, or analyst work, each attributable and retrievable. Remove it → there is no intelligence program, only a report library.
3. **Curation into organized, reusable knowledge** — items are filtered, structured (tags/taxonomy), analyzed, and assembled into standing knowledge artifacts (profiles, battlecards, dashboards, digests). Remove it → a raw news feed/aggregator, not an intelligence platform.
4. **Recurring internal distribution to consumers in their work context** — intelligence reaches internal stakeholders (sales, product, strategy) on a standing basis, inside the platform and/or embedded in their tools. Remove it → personal research tooling, not an organizational intelligence program.

Historical check: pre-AI and pre-SaaS CI practice (clip services + Google Alerts + a curated wiki/newsletter/battlecard deck maintained by a competitive-enablement person) satisfies all four invariants with purely manual collection and distribution. The definition therefore does not depend on AI, automated crawlers, battlecard software, or CRM embedding. AI-first packaging is era-typical, not definitional.

### Level 1 — Common Mature Structure

Present across essentially all four sampled products; expected in a modern product but not definitional:

- automated external monitoring engine (websites, news, social, reviews, ads, job postings)
- AI summarization / importance scoring / daily digests
- battlecards (sales-facing competitive knowledge artifacts)
- competitor profiles
- alerts, email digests/newsletters (with human commentary)
- win/loss analysis (quantitative from CRM; qualitative from interviews) feeding back into knowledge
- delivery integrations: CRM (Salesforce/HubSpot), chat (Slack/Teams), sales-enablement platforms (Highspot/Showpad), email
- adoption/engagement analytics and revenue-influence reporting
- tags/taxonomy + saved searches as the curation toolkit

### Level 2 — Variant / Optional Structure

- breadth pole: competitor-centric (Klue/Kompyte style) vs "360° market & competitive" including key accounts, customers, suppliers, industry/regulation (Contify style)
- internal-source depth: employee-submitted intel via chat/email as a first-class flow (directly documented in one product) vs ingested conversational artifacts (call recordings, transcripts) (common) vs external-only collection (minimal)
- win/loss program depth: dashboard metric → AI-generated deal stories → managed interview programs (human analysts / AI interviewer / "lost-eval" interviews)
- analyst/managed-services layer (bundled research hours)
- data-supply orientation: intelligence exposed as API/MCP/LLM-consumable corpus
- pricing/user model: unlimited-seat vs per-user (vendor marketing claims — not definitional, kept vague in final doc)
- industry packaging (pharma, BFSI, consulting, manufacturing) and non-tech verticalization
- deployment/security postures (SSO, access levels) — common enterprise requirements, not defining

### Level 3 — Vendor-specific (Research Notes only)

- Klue: Compete Agent (Research Analyst + Deal Assistant), Deal Tips, Klue Insights, Klueless, MCP server / Claude Connector Directory positioning, acquisitions of Goldpan.ai and Ignition.
- Crayon: Sparks (scheduled AI prompts/deliverables), Call Clips, the Aggregate→Organize→Publish→Enable→Measure stage naming, "State of Competitive Intelligence" annual report as marketing franchise.
- Contify: Athena AI (business facts → insights → Ask Athena), Business News API as separate product, Contify Taxonomy public index, 7-step curation, 117+ languages, 700k+ companies, two-year historical coverage, unlimited-user positioning, "Visionary in inaugural Gartner MQ for Competitive and Market Intelligence Platforms" (2026).
- Kompyte: Kompyte GPT, AI Daily Summaries, IcebergIQ win/loss research partnership, Semrush ownership, direct "Kompyte vs Klue / Crayon" comparison pages.

---

## Vendor-specific Findings

See Level 3 above; none of these may be promoted into the canonical document. Note that one product's own stage naming (Crayon's five verbs) was used as a hint for describing the workflow, but the final document describes the loop generically (collect → curate → package → distribute → measure) because it is cross-product.

## Rejected Findings

- "Battlecards are the defining object" — rejected. All four sampled products have battlecards, but Contify's center of gravity (dashboards, newsfeeds, accounts, industry intelligence, analyst reports) shows the type stands without battlecard-centrality; battlecards are the sales-facing packaging of curated knowledge (Level 1). Historical CI programs also ran on digests/reports.
- "AI is part of the definition" — rejected. The historical check passes without AI; all four products happen to be AI-led today (era-typical).
- "The platform is external-facing (a research service bought like data)" — rejected as the type's core; only Contify sells a news API as a separate product, and that is a data-product adjacency, not the platform type.
- "Per-user vs unlimited licensing is structural" — rejected; marketing/packaging variance only.
- "Competitive Intelligence Platform = SEO/digital measurement of competitors (Similarweb-style)" — rejected; different Type (measurement of digital properties), no curation/distribution program at its core.

## Boundary Findings

| Neighboring Type | Distinction | "Remove what → becomes the other" |
|---|---|---|
| Market Research Platform | market research produces studies about markets/consumers (often commissioned, survey/panel-based, periodic); CI platform runs a standing monitored loop over external entities for internal decision support. Contify self-labels "M&CI", showing real overlap at the market-intelligence pole. | Remove standing entity tracking + recurring collection → commissioned research service (Market Research). |
| Media Monitoring Platform | media monitoring tracks the organization's OWN brand/mentions across media; CI tracks external entities. | Remove tracked external competitors (track own brand) → Media Monitoring. |
| Social Listening Platform | social-listening is source-bound (social networks) and topic/consumer-conversation-centric; CI is entity-bound and source-agnostic. | Restrict sources to social + own-brand/consumer topics → Social Listening. |
| Sales Enablement Platform | enablement systems manage sales content/training generally (Highspot/Seismic are integration partners of CI tools); CI keeps competitive knowledge current from live collection. Enablement consumes battlecards; CI produces and maintains them. | Remove collection/curation engine (serve static content library) → Sales Enablement. |
| Sales Intelligence Platform | sales intelligence supplies prospect/account data (firmographics, contacts, buying signals) for prospecting; CI supplies competitor/market knowledge for competitive strategy and deal defense. Adjacent at "account triggers" (Contify). | Replace tracked competitors with prospect accounts as the unit → Sales Intelligence. |
| SEO Platform / digital measurement | measures web/search performance of properties; competitor comparison is an analytic view, not a monitored intelligence program with curation/distribution. | — |
| Financial Market Data Terminal / Investment Research Platform | securities-and-markets research for investment decisions; a different audience and object world (instruments, filings, estimates) — shared only in the abstract "monitor + digest" loop. | — |

Taxonomy note: "Competitive Intelligence Platform" sits in directory section 06 (Marketing) alongside Market Research Platform, Media Monitoring Platform, and Social Listening Platform. The research supports these as distinct Types with a genuinely shared "monitor → distribute" skeleton but different tracked objects and audiences. No boundary issue requiring directory change was found; the Contify self-label "market AND competitive intelligence" is recorded as an overlap observation, not a merge proposal.

## Uncertainties

1. Help-center-level operational detail (item states, editor permissions, exact alert configuration surfaces, battlecard editor anatomy) was not reachable for any of the four products (transport errors / empty shells / 503). All claims above are calibrated to product-page-level evidence; no precise limits, cadences, or plan-gated features are asserted.
2. Internal employee-submission flows as a first-class feature are directly documented in only one product (Contify); treat as common-but-not-universal.
3. Whether "competitor profiles" are a first-class object in Crayon/Kompyte was not directly observed (implied in Crayon via Organize stage; absent from Kompyte's fetched pages).
4. Pricing/user-model claims (e.g., unlimited seats) are vendor marketing statements; not verified and excluded from the final document's factual claims.
5. The sample is B2B-SaaS-heavy; CI practice in other industries (pharma, BFSI) is represented only through Contify's packaging claims, not through independent products in the sample.

## Final Synthesis

A Competitive Intelligence Platform is an organization's standing intelligence loop over its competitive environment: it maintains tracked external entities (competitors at the center, commonly extended to accounts, customers, suppliers, and market segments), continuously or recurrently collects discrete intelligence items about them (from automated external monitoring, internal conversational artifacts and contributors, and analyst research), curates those items into organized reusable knowledge (tags/taxonomy, AI- and human-filtered summaries, competitor profiles, battlecards, dashboards), and distributes that knowledge to internal consumers — sales first, then product, marketing, and strategy — through alerts, digests, embedded cards in CRM/chat/enablement tools, and searchable in-app surfaces, while measuring adoption, competitive win/loss, and revenue influence to close the loop. AI automation and sales-facing battlecards are the current era's dominant packaging, not the definition: the same four-part core (tracked entities → collected items → curated knowledge → recurring internal distribution) describes a human-run CI program from before the SaaS era.
