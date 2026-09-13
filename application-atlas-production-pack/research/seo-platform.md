# Research Notes — SEO Platform

Research date: 2026-09-10
Leaf: `SEO Platform` (DIRECTORY.md §06 Marketing, Advertising & Growth)
Slug: `seo-platform`

## Research Goal

Understand what an "SEO Platform" actually is as an Application Type: the multi-capability suite products (Semrush, Ahrefs, Moz Pro, SE Ranking, Conductor-class) that market themselves as SEO platforms / SEO toolsets / visibility platforms. Produce a vendor-neutral Application Document that explains the Type's defining core, standard capabilities, workflow, interfaces, rules, variants, and boundaries — without collapsing into the already-processed sibling Types (Keyword Research Application, SEO Site Audit Application, Search Engine Marketing Management Platform).

## Initial Boundary

Hypothesis before research:

- An SEO Platform is the umbrella/console product for organic-search work: keyword research + rank tracking + backlink analysis + site audit + competitor analysis + reporting, organized around the user's sites.
- Nearest neighbors: Keyword Research Application (keyword at center), SEO Site Audit Application (page population at center), Search Engine Marketing Management Platform (paid ad accounts at center), rank-tracker point tools, web analytics, social media management, content marketing platforms.
- Open questions going in:
  1. Is the backlink index definitional? (Enterprise platforms may lack one.)
  2. Is the project/campaign container definitional or just common?
  3. Is rank tracking definitional?
  4. What exactly separates the platform from its own modules (the center-of-gravity question flagged by the seo-site-audit pass)?
  5. Does the 2025–2026 "AI visibility" layer change the Type?

## Research Questions

1. What stable data domains exist across suites (keywords, rankings, backlinks, pages/health, competitors, traffic estimates)?
2. What is the organizing container (project / campaign / property / workspace) and what does it bind?
3. What is the canonical workflow loop (setup → research → act → track → report)?
4. How do the products treat the user's own sites vs competitors' sites (symmetry)?
5. How do enterprise platforms differ structurally from self-serve suites?
6. Where are the exact seams with Keyword Research Application, SEO Site Audit Application, and SEM Management Platform?
7. Historical check: would pre-cloud / desktop-era suites (SEO PowerSuite class, WebPosition class, early Moz) satisfy the same definition?

## Representative Products

| Product | Positioning (self-described) | Segment / philosophy | Docs accessed |
|---|---|---|---|
| Semrush | "The leading platform to grow and measure brand visibility across every digital channel"; SEO toolkit of "20+ tools" | All-in-one self-serve suite; freemium; agency→enterprise | Tier 1 (KB: Position Tracking, Domain Overview, KB index) + Tier 2 (homepage) |
| Ahrefs | "AI Marketing Platform Powered by Big Data"; tools: Site Explorer, Keywords Explorer, Rank Tracker, Site Audit, Dashboard | Data-first suite built on proprietary crawler + link index; self-serve | Tier 1 (Help Center: Dashboard collection, Rank Tracker collection, Dashboard-metrics article) + Tier 2 (homepage) |
| Moz Pro | "The SEO and AI Visibility growth platform"; "all-in-one suite of SEO essentials" | Accessible suite, campaign-centric; marketer-friendly | Tier 1 (Help Hub + Moz Pro FAQs) + Tier 2 (Moz Pro product page) |
| SE Ranking | "Complete AI SEO platform for every challenge" (verbatim "SEO platform") | Mid-market/agency pole; white-label agency packaging | Tier 1 (Help Center: project setup article, KB structure) + Tier 2 (homepage) |
| Conductor | "The enterprise platform for AI & search visibility"; "the only all-in-one enterprise AEO platform" | Enterprise pole; Intelligence + Creator + Monitoring + AgentStack | Tier 2 (homepage) + Tier 1 (Documentation index) |

Negative / boundary samples (noted, not deep-sampled):

- **Majestic** — backlink-intelligence point tool; shows a single data domain is not a platform.
- **STAT (Moz)** — "SERP tracking and analytics for enterprise SEO experts"; a rank-tracking point tool sold beside the Moz Pro suite; shows 1+2-without-3 is not the platform Type.
- **SEO PowerSuite** — desktop suite (Rank Tracker, WebSite Auditor, SEO SpyGlass, LinkAssistant); historical/desktop packaging witness (used from background knowledge only; not fetched — flagged in Uncertainties).

## Sources

Fetched 2026-09-10 (all successful on first attempt unless noted):

- Semrush homepage — https://www.semrush.com/
- Semrush Knowledge Base index — https://www.semrush.com/kb/
- Semrush KB — Position Tracking — https://www.semrush.com/kb/32-position-tracking
- Semrush KB — Domain Overview — https://www.semrush.com/kb/254-domain-overview
- Ahrefs homepage — https://ahrefs.com/
- Ahrefs Help Center — https://help.ahrefs.com/
- Ahrefs Help Center — Dashboard collection — https://help.ahrefs.com/en/collections/87942-dashboard
- Ahrefs Help Center — Rank Tracker collection — https://help.ahrefs.com/en/collections/87927-rank-tracker
- Ahrefs Help Center — Understanding the Metrics in the Dashboard Overview — https://help.ahrefs.com/en/articles/5373022-understanding-the-metrics-in-the-dashboard-overview
- Moz Pro product page — https://moz.com/products/pro
- Moz Help Hub — https://moz.com/help
- SE Ranking homepage — https://seranking.com/
- SE Ranking Help Center — https://help.seranking.com/hc/en-us
- SE Ranking Help Center — Setting up your project — https://help.seranking.com/hc/en-us/articles/20877217235740-Setting-up-your-project
- Conductor homepage — https://www.conductor.com/
- Conductor Documentation index — https://www.conductor.com/docs/

Note: a prior production attempt (2026-09-07, batch-B3) recorded that the Semrush KB was unreachable; on 2026-09-10 it fetched normally. All Semrush claims in this pass are Tier 1.

## Product Observations

### Semrush (evidence layer: A — directly observed, Tier 1 KB + Tier 2 homepage)

- Self-positioning: "The leading platform to grow and measure brand visibility across every digital channel." Product organized as **toolkits**: SEO, AI Visibility, Traffic & Market, Content, Local, Advertising, AI PR, Social; "Semrush One" unifies "SEO authority and AI visibility". SEO toolkit described as "20+ tools".
- SEO toolkit tool list (KB sidebar): SEO Dashboard, Site Audit, Position Tracking, Domain Overview, Organic Rankings, Top Pages, Compare Domains, Keyword Gap, Backlink Gap, Keyword Overview, Keyword Magic Tool, Keyword Strategy Builder, SEO Writing Assistant, Topic Research, Backlinks, Referring Domains, Backlink Audit, Sensor, SEOquake, Semrush Rank, On Page SEO Checker, Organic Traffic Insights. Plus My Reports, Folders, Teamwork.
- **Position Tracking** (KB): "monitors your website's search rankings daily for specific keywords… across devices (mobile, tablet, desktop), locations (down to postal code), and search engines including Google, Bing, Baidu, ChatGPT Search, and Google AI Mode." "Tracks any keyword and domain, even those not in the main Semrush database. You can track and compare multiple targets… within a single campaign." "Measuring ranking changes helps you understand the impact of your SEO efforts." Reports: Overview (visibility %, estimated traffic, average position), Rankings Distribution (top 3/10/100), Pages, Tags, Devices & Locations, Landscape ("benchmarks your search visibility against competitors in one view"), Competitors Discovery, Cannibalization, Featured Snippets, AI Search. Campaigns live in **Folders**; deleting a folder removes "all other Website Monitoring campaigns within that folder, such as Site Audit, Backlink Audit, and On Page SEO Checker" — i.e., the folder is the per-site container binding the monitoring campaigns. Historical mechanics: daily data for 60 days, then weekly snapshots (Wednesdays) for 140 weeks (vendor-specific precision — L3). Plan limits: 500/1,500/5,000 tracked keywords by tier; up to 20 competitors per campaign; multitargeting on higher tiers (L3).
- **Domain Overview** (KB): "shows a website's organic traffic, paid traffic, backlinks, and comprehensive AI visibility in a single report… Use this snapshot to assess competitor strengths… Click any metric to open the corresponding detailed report." "Research domains, subdomains, subfolders, or specific URLs." Aggregates four tools: Organic Search (Organic Rankings), Paid Search (Advertising Research), Backlinks, AI Visibility. Daily request limits by tier (L3).
- Data scale claims (homepage): 28B keywords, 43T backlinks, 808M domain profiles, 142 geo databases (marketing figures — L3).
- Users: agencies, SEO specialists, content marketers, enterprises, mid-market, small teams, solopreneurs, freelancers.
- AI-era layer: AI Visibility toolkit, Prompt Research, AI Brand Sentiment; Adobe acquisition announced.

### Ahrefs (evidence layer: A — directly observed, Tier 1 Help Center + Tier 2 homepage)

- Self-positioning: "Make your business discoverable—in search, AI, and beyond." Tools: Site Explorer ("Study your competitors' websites"), Keywords Explorer, Rank Tracker, GSC Insights, Brand Radar (LLM visibility), Site Audit, Web Analytics, Bot Analytics, Content Explorer, AI Content Helper, Social Media Manager, Dashboard ("Track performance and progress across projects"), Portfolios, Report Builder, GBP Monitor.
- **Dashboard / projects** (Help Center): projects are added, deleted, organized in the Dashboard; project scope definable "using different modes"; FAQ frames projects as the unit that counts websites ("Is this how many websites I can check with Ahrefs?").
- **Dashboard Overview metrics article** (Tier 1 — the integration point made explicit): "These metrics along with the corresponding graphs are pulled from different tools within Ahrefs" —
  - Health Score (source: Site Audit; "proportion of internal URLs on a target site that don't have errors"; plus crawled/redirects/broken/blocked counts)
  - Domain Rating (source: Site Explorer; "strength of a website's backlink profile… on a 100-point scale"; updated every 12 hours)
  - Referring domains (total + delta; new/lost)
  - Backlinks (total + delta; new/lost)
  - Organic traffic ("Estimated monthly organic traffic from all ranking keywords in all countries… within the first 100 results in SERP"; plus traffic value = PPC-equivalent cost)
  - Organic keywords (count ranking in top 100, by country; per-keyword update cadence varies "anywhere between 3 days to 2 months, depending on the popularity" — L3 precision)
  - Tracked keywords (source: Rank Tracker; current count + improved/declined changes; ranking groups 1–3, 4–10, 11–50, 51–100)
  - New sites may show N/A "until… backlinks and ranking for keywords within the first 100 results" exist.
- **Rank Tracker collection**: tracked keywords with locations, mobile rankings, tags, competitor websites added to projects, automated email notifications, Share of Voice (SoV) metric, "How to check my website's SEO visibility", positions may not match what the user sees in Google (FAQ).
- Data scale claims: 41.9B keywords tracked, 170T pages in web index, 8B pages crawled daily by AhrefsBot, "#1 SEO crawler" (per Cloudflare Radar) — L3.
- AI-era layer: Brand Radar, Custom Prompts, Ask Ahrefs, AI Content Helper; separate products (Letaido, Firehose, Yep).

### Moz Pro (evidence layer: A — directly observed, Tier 1 Help Hub + Tier 2 product page)

- Self-positioning: "Moz Pro is the SEO and AI Visibility growth platform designed for marketers…"; "Your all-in-one suite of SEO essentials."
- **Campaigns** (product page): "Track your SEO progress and prove your success with Campaigns — Manage your websites, monitor competitors, and generate custom reports."
- Tools (product page + Help Hub): Keyword Explorer (1.25B+ keyword index), Keyword Suggestions (grouped by intent), Search Intent, Search Visibility Score, Competitive Research & SERP Analysis, On-page Grader, Rank Tracker ("Track your rankings across multiple search engines and locations"), Brand Authority, Domain Overview ("quickly assess a site's online authority, performance, and health by aggregating key SEO metrics all in one easy-to-access report"), Site Crawl ("Find and fix technical errors… in-depth site audits, detailed error reports, and clear instructions for fixes") + On-Demand Crawl ("Quickly re-crawl your site to validate fixes"), Custom Reports, MozBar.
- **Search Visibility definition** (Help Hub FAQ, Tier 1): "the percentage of clicks we estimate you receive based on your organic rankings positions, across all of the keywords you're tracking in your Campaign"; 0% means "not currently ranking in the top 50 results for your tracked keywords."
- **Two crawlers** (Help Hub FAQ, Tier 1): Rogerbot = "our Campaign site crawler" (site audits); DotBot = web crawler feeding "the Moz Link Index… available in the Links section of your Moz Pro campaign, Link Explorer, and the Moz Links API." Spam Score in Link Explorer.
- Moz family split: Moz Pro (suite) / Moz Local (listings) / STAT (enterprise SERP tracking point tool) / Moz API (link index) — the suite vs point-tool split is explicit in one vendor's own catalog.
- AI-era layer: "AI Research toolkit… measure your presence in ChatGPT, Gemini, Google AI Mode, and Perplexity."

### SE Ranking (evidence layer: A — directly observed, Tier 1 Help Center + Tier 2 homepage)

- Self-positioning: "Complete AI SEO platform for every challenge." Structure: AI Visibility / **SEO Research** (Keyword Suggestion Tool, Competitive Research, Backlink Checker, SERP Checker) / **SEO Monitoring** (Rank Tracker, Website Audit, Backlink Monitor, On-Page SEO Checker) / Content Marketing / Local Marketing / Agency Success Kit / Integrations.
- **Project definition** (Help Center, Tier 1): "SE Ranking's Projects are dedicated workspaces for tracking one website and all its SEO data. This includes keyword rankings, competitors, audit results, and more. Each project is tied to a specific domain or URL."
- Project mechanics (Tier 1): search engines + regions per project; keywords with **Groups** (folders, one keyword one group) and **Tags** (labels, multiple per keyword); **Target URL** = "the page you intend to rank for a keyword… helps in detecting if the wrong page is ranking… and in avoiding keyword cannibalization"; keyword lists per search engine (Google Desktop/Mobile, YouTube, Bing, Yahoo!); competitor benchmarking guidance ("Add 3 to 5 competitors to your project to monitor their keyword strategy, landing pages, and backlinks"); separate projects per country/region.
- Agency pole (homepage + help): Agency Pack — white label, client seats, lead generator, agency catalog; scheduled SEO reports.
- Data claims: 188 country databases, 5.5B keyword database, 2.2B domain profiles (L3).
- AI-era layer: AI Search Toolkit (AI Overviews/AI Mode/ChatGPT/Gemini/Perplexity trackers), SE Visible (separate product).

### Conductor (evidence layer: A for homepage/docs structure; B− for operational detail — enterprise docs are shallower publicly)

- Self-positioning: "The enterprise platform for AI & search visibility"; "the only all-in-one enterprise AEO platform"; "#1 for Enterprise AEO."
- Products: **Conductor Intelligence** ("Track your brand's visibility across ChatGPT, Gemini, Copilot, Claude, and traditional search, and connect that presence directly to traffic, conversions, and revenue"; docs: "One source of truth for organic and AI search performance—including data about your website"), **Conductor Creator** (AI content creation/optimization), **Conductor Monitoring** ("24/7 always-on monitoring… Real-time alerts and prioritized fixes"; docs: "site health scores, log-file analysis, alerts"), **Conductor AgentStack** (MCP, APIs, agents).
- **Platform docs**: "manage users, configure web properties, build workspaces" — the enterprise container is web properties + workspaces.
- "Unified Data Engine": "10+ years of proprietary search data. Intent signals, content signals, and technical signals in a unified engine."
- **No native backlink module appears in the product lineup** — the clearest witness that the link graph is not definitional for the Type. (Uncertainty: Conductor may surface third-party link data inside Intelligence; not verified.)
- Enterprise services layer: customer stories, services & support, industries.

## Cross-product Comparison

| Structure | Semrush | Ahrefs | Moz Pro | SE Ranking | Conductor |
|---|---|---|---|---|---|
| Per-site container | Folder of "Website Monitoring campaigns" (Position Tracking, Site Audit, Backlink Audit, On Page SEO Checker) | Project in Dashboard | Campaign | Project ("dedicated workspaces for tracking one website and all its SEO data") | Web properties + workspaces |
| Rank/visibility tracking over time | Position Tracking (daily; devices/locations/engines incl. AI; visibility %; estimated traffic) | Rank Tracker (tracked keywords, locations, mobile, SoV) | Rank Tracker in campaign (Search Visibility %) | Rank Tracker (per engine/device/region; target URL) | Intelligence (traditional + AI search visibility) |
| Keyword research data | Keyword Magic Tool / Overview / Gap / Strategy Builder | Keywords Explorer | Keyword Explorer | Keyword Suggestion Tool + Grouper | Intelligence keyword/topic + intent signals |
| Backlink data | Backlinks, Referring Domains, Backlink Audit, Backlink Gap | Site Explorer backlink reports + DR | Link Explorer + campaign Links section + Spam Score | Backlink Checker + Backlink Monitor | **not native** (no backlink module in lineup) |
| Technical site health | Site Audit | Site Audit (Health Score) | Site Crawl (Rogerbot) + On-Demand Crawl | Website Audit | Monitoring (24/7, log-file analysis, alerts) |
| Domain/competitor research on any domain | Domain Overview (any domain/subdomain/subfolder/URL; aggregates Organic+Paid+Backlinks+AI) | Site Explorer (competitors' websites) | Domain Overview + Competitive Research | Competitor Analysis Tool + SERP Checker | Intelligence (website + competitive data) |
| Derived visibility measures | Visibility %, estimated traffic | SoV, estimated organic traffic, traffic value | Search Visibility % | visibility metrics | visibility + traffic/conversion connection |
| Reporting/exports | My Reports (branded, scheduled; GA4/GSC/Looker Studio) | Dashboard, Report Builder, Portfolios | Custom Reports | Report Generator, white label, scheduled | enterprise reporting + API |
| Competitors in container | up to 20 per campaign (tier-capped) | added to projects | monitored in campaign | 3–5 recommended | competitive benchmarking |
| AI-visibility layer (2025–26) | AI Visibility toolkit, prompts | Brand Radar, Custom Prompts | AI Research toolkit | AI Search Toolkit, SE Visible | AEO throughout, AgentStack |
| Agency packaging | Agency Partners, branded reports | agency directory | agency solutions | Agency Pack (white label, client seats, lead gen) | enterprise services |
| Own index / data engine | yes (28B keywords, 43T backlinks claimed) | yes (own crawler + index) | yes (DotBot link index) | yes (own databases) | yes ("10+ years proprietary search data") |

### What is universal (evidence layer B)

1. **The website as the persistent unit of record** — every product organizes ongoing work in a per-site container (folder-of-campaigns / project / campaign / project / property+workspace) bound to a domain or URL, holding that site's SEO data. 5/5.
2. **Keyword rankings for that site, tracked over time** — a tracked keyword set with positions accumulated as history (daily/weekly cadence varies). 5/5. This is the feedback loop: "Measuring ranking changes helps you understand the impact of your SEO efforts" (Semrush).
3. **Keyword-demand research data** — a query universe with volume/difficulty/intent, queried from a seed or browsed. 5/5.
4. **Own-site / competitor symmetry** — the same data model (domain overview, rankings, keywords, links) applies to any domain; competitors are added inside the same container and benchmarked against the user's site. 5/5.
5. **Derived visibility measures** — visibility %, share of voice, estimated organic traffic computed from rankings × demand × click models. 5/5 (names differ).
6. **Technical site-health module** — 5/5 (audit or 24/7 monitoring form).
7. **Backlink data** — 4/5 (Conductor lacks a native module). Common, not definitional.
8. **Reporting/exports outward** — 5/5.
9. **Search engine / device / location targeting of measurement** — 5/5.
10. **Vendor-maintained data foundation** (own crawlers/keyword databases) — 5/5 in the current market, but see historical check: not definitional.

### What varies (evidence layer B/C)

- Packaging: self-serve suite (Semrush/Ahrefs/Moz/SE Ranking) vs enterprise platform (Conductor) vs desktop suite (SEO PowerSuite, background) vs suite-plus-point-tools catalog (Moz: Pro/Local/STAT/API).
- Container strictness: project-required workflows (Moz campaigns, SE Ranking projects, Semrush folders) vs ad-hoc-first research with projects for monitoring (Ahrefs tools usable on any domain without a project).
- Backlink depth: native index + audit tooling (Semrush/Ahrefs/Moz/SE Ranking) vs none native (Conductor).
- Monitoring cadence: scheduled crawls + daily rank checks vs 24/7 monitoring with log-file analysis (enterprise pole).
- Scope drift: suites bundle content tools, local SEO, paid-search research, social publishing, digital PR — adjacent-Type modules, not platform identity.
- AI-era layer: all five now ship AI/LLM visibility tracking; era-specific (see historical check).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

The SEO Platform is the SEO team's organic-visibility workbench. Its defining core is three jointly-held structures:

1. **The tracked website as the unit of record.** A persistent per-site container (project / campaign / property) binds one website with its SEO data — rankings, keywords, competitors, health, links. The site is the thing whose visibility is managed.
   *Remove → disconnected point tools with no site of record.*
2. **Measured keyword rankings over time for that site.** A tracked keyword set whose positions are re-measured on a cadence and accumulated as history — the feedback loop that evaluates SEO work (plus derived visibility/traffic measures computed from it).
   *Remove → a research database with no feedback loop.*
3. **The shared research estate with own/competitor symmetry.** Keyword-demand data (and commonly link data) over the whole query/domain space, queryable for the user's own sites and for competitors' sites, feeding keyword selection and competitive comparison inside the same workspace.
   *Remove → a bare rank tracker / single-site monitor (the STAT-class point tool).*

Jointly-held load-bearing:
- 1 alone = a site folder with no living data.
- 2 without 1+3 = a standalone rank tracker.
- 3 without 1+2 = a keyword/backlink research database (Keyword Research Application territory).
- 1+2 without 3 = monitoring console with no strategy input.
- 1+3 without 2 = research workbench with no feedback loop.
- 2+3 without 1 = ad-hoc lookups with no site of record.

Anti-overfit notes on L0:
- **Backlinks are NOT in L0** — Conductor (a flagship enterprise SEO platform) ships no native backlink module; the link graph is common mature structure (4/5), not definitional.
- **Site audit is NOT in L0** — the audit is one module (and its own Application Type); early suites predate full crawlers.
- **"Own proprietary index" is NOT in L0** — all five sampled products maintain their own crawlers/databases today, but the L0 concept is the research estate however sourced (early/desktop-era tools queried engines directly or licensed data). Requiring an own index would overfit to the current big-data era.
- **AI-visibility tracking is NOT in L0** — era artifact (see historical check).
- **"Platform = many modules" is NOT the definition** — module count is packaging; the L0 is the data integration around site + rankings + research estate.

### L1 — Common Mature Structure

Present in most mature products; expected by the market; not definitional:

- backlink / link-graph data with authority metrics (vendor-proprietary scores: DR/DA-class)
- technical site-health module (crawl/audit or 24/7 monitoring; the deep form is the SEO Site Audit Application Type)
- competitor analysis tooling (competitor discovery, keyword/backlink gap, landscape/share-of-voice views)
- derived visibility measures (visibility %, share of voice, estimated organic traffic, traffic value)
- SERP-feature tracking (featured snippets, AI Overviews)
- reporting/exports (scheduled branded reports, dashboards, BI connectors) and integrations (GSC, GA4, Looker Studio)
- search-engine / device / location targeting of measurement
- alerts/notifications; API access
- team machinery (users, permissions, client seats at the agency pole)

### L2 — Variant / Optional Structure

- **AI-visibility layer** (LLM answer/prompt tracking, brand sentiment, AI Overviews tracking) — shipped by all five sampled products in 2026 but absent from pre-2023 products; current-market common, era-specific, not definitional.
- **Agency packaging** — white label, client seats, lead generation, agency catalogs (SE Ranking Agency Pack; Semrush/Moz agency programs).
- **Content tools** — briefs, writing assistants, content editors, AI writers (drift toward Content Marketing territory).
- **Local SEO modules** — listings/GBP management (Moz Local, Semrush Local, SE Ranking Local, Ahrefs GBP Monitor).
- **Paid-search research data** (ad copies, spend estimates) — research-only in this Type; not account management.
- **Deployment/packaging poles** — cloud self-serve suite vs desktop suite (SEO PowerSuite) vs enterprise platform with services (Conductor) vs vendor catalog splitting suite and point tools (Moz Pro vs STAT).
- **Container posture** — project-required vs ad-hoc-first research.
- **Monitoring cadence** — scheduled crawls/daily checks vs 24/7 real-time monitoring with log analysis (enterprise pole).

### L3 — Vendor-specific (research notes only)

- Semrush: toolkit packaging and plan limits (500/1,500/5,000 tracked keywords; 20 competitors/campaign; multitargeting on Guru/Business); Position Tracking history mechanics (daily 60 days → weekly Wednesday snapshots × 140 weeks); Sensor, SEOquake, Semrush Rank; Semrush One; Adobe acquisition; data-scale marketing figures.
- Ahrefs: Domain Rating (DR) 100-point backlink-authority score; 12-hour refresh on Site Explorer metrics; per-keyword update cadence 3 days–2 months by popularity; credits system; ranking groups 1–3/4–10/11–50/51–100; AhrefsBot scale claims; Letaido/Firehose/Yep ecosystem; Ask Ahrefs.
- Moz: Domain Authority / Page Authority; Spam Score; Rogerbot (campaign crawler) vs DotBot (link index crawler) split; MozCast; Search Visibility 0% = not ranking in top 50 for tracked keywords; STAT as separate enterprise SERP-tracking product.
- SE Ranking: Groups-vs-Tags keyword organization semantics; Target URL cannibalization detection; per-engine keyword lists (Google Desktop/Mobile, YouTube, Bing, Yahoo!); Agency Pack components; SE Visible as separate product; plan pricing structure.
- Conductor: AgentStack (MCP/APIs/agents); log-file analysis in Monitoring; "10+ years proprietary data"; workspaces/web-properties container vocabulary.

## Historical / Market-Sample Check (§24)

Question: would older, regional, platform-native, or differently positioned products still fit the L0?

- **SEO PowerSuite (desktop era, ~2005+)**: four desktop tools (Rank Tracker, WebSite Auditor, SEO SpyGlass, LinkAssistant) organized in per-site projects; rank tracking over time; keyword research (historically via external data sources); backlink research; competitor tracking in Rank Tracker. Fits L0 (site container + rankings-over-time + research estate with competitor symmetry). Background knowledge only — not fetched; flagged in Uncertainties.
- **WebPosition Gold class (late 1990s–2000s)**: per-site projects, scheduled rank checks against competitors, page-analysis advice; keyword suggestions via partner data. Site + rankings + research core holds; no own web index (queried engines directly) — confirming that an own index is not definitional. Background knowledge only — flagged.
- **Early Moz (2007–2012)**: rank tracker + keyword tool + Linkscape (2009) before full site crawls — fits L0 without a site-audit module, confirming site audit is not definitional.
- **Regional products (Sistrix in DACH; Yandex-era tools)**: module-structured suites around rankings/keywords/links — same structure. Not fetched; asserted weakly.
- **AI-era check (forward-looking)**: all five sampled products now track LLM/AI visibility. If L0 were defined to include AI visibility, 2023-era products would fail the check — so AI visibility stays L2 (current-market common, era-specific).

Conclusion: L0 passes the historical check. The definition is deliberately implementation-agnostic (no own-index requirement, no backlink requirement, no audit requirement, no AI layer).

## Vendor-specific Findings

See L3 above. The most consequential vendor pattern for the final document: **the suite-module relationship** — every sampled suite ships site health (audit/monitoring) and keyword research as modules, and the sibling Types (Keyword Research Application, SEO Site Audit Application) describe those modules' standalone forms. The platform document must describe the integration, not re-describe the modules.

## Boundary Findings

1. **vs Keyword Research Application** (sibling leaf, processed 2026-09-07): the keyword Type's unit of record is the search query (demand measurement + query-space discovery + attainability); the platform's unit of record is the website with measured visibility. The keyword tool is one module of every sampled platform. Test: remove the site-of-record + tracking loop → keyword research application. Keep both Types. (Ratifies the keyword pass's boundary: "keyword at center vs sites/pages/backlinks".)
2. **vs SEO Site Audit Application** (sibling leaf, processed 2026-09-07; joint review discharged here): center-of-gravity test confirmed from this side — in every sampled suite, site health is one module among several; removing keyword/backlink/rank capabilities from the suite leaves exactly the crawl→evaluate→report loop, which is the audit Type. Removing the audit from the suite leaves the platform standing (Conductor's Monitoring is a different form of the same module). Keep both Types; the audit pass's keep-both working assumption is ratified.
3. **vs Search Engine Marketing Management Platform** (sibling leaf, processed 2026-09-07): SEM management operates linked ad accounts it does not own, with spend-controlling parameters written back to engines. The SEO platform's paid-search data (Semrush Advertising toolkit, Ahrefs PPC use case) is *research* — ad copies, spend estimates — with no ad-account write-back. Different object of record (ad account vs website visibility).
4. **vs rank-tracker point tools (STAT class)**: 1+2 without 3 = rank tracker. Moz itself sells STAT beside Moz Pro — the vendor's own catalog demonstrates the boundary.
5. **vs web analytics (GA-class)**: web analytics measures actual first-party traffic across all channels; the SEO platform measures *search visibility* (rankings, estimated organic traffic) from its own third-party data, no site tracking required. GSC/GA integrations import first-party data into the platform, but the platform's native data is its own index/estimates. Estimated ≠ measured is a defining data rule.
6. **vs Social Media Management / Content Marketing Platform**: suites bundle social publishing and content tools (Semrush Social, Ahrefs Social Media Manager, SE Ranking Content Marketing) — adjacent-Type modules inside the platform, not platform identity.
7. **vs General Web Search Engine**: the platform studies search results; it does not serve results to searchers.
8. **vs Marketing Analytics Platform**: aggregate cross-channel marketing measurement/attribution vs the SEO-specific visibility workbench.

## Uncertainties

- Conductor's operational depth is evidenced at product-line level (homepage + docs index); whether Intelligence surfaces third-party backlink data inside its reports was not verified. The "no native backlink module" finding is stated at product-lineup level only.
- SEO PowerSuite and WebPosition Gold were used as historical witnesses from background knowledge, not fetched; the historical check for the desktop era is therefore asserted at moderate confidence.
- Whether any market product exists with rank tracking + research estate but *no* per-site container (pure ad-hoc) was not found; all sampled products ship the container. The container's L0 status rests on 5/5 presence + the platform-vs-point-tool boundary, not on a counterexample.
- Enterprise platforms' team/permission models (roles, approval flows) were not researched in depth; team machinery is treated as common structure without detail.
- The AI-visibility layer's staying power (module vs future definitional core) is unresolved; recorded as era-specific per the historical check.

## Final Synthesis

An SEO Platform is the SEO team's organic-visibility workbench: it holds the user's websites as persistent records, measures where their pages rank for tracked keywords over time (with derived visibility/traffic measures), and puts that measurement next to a research estate over the whole query/domain space — keyword demand and, in most products, the link graph — queryable equally for the user's own sites and for competitors. Around that core, mature products add backlink data, technical site-health modules, competitor-gap analysis, SERP-feature tracking, reporting machinery, and (currently) AI-answer visibility; agencies get white-label reporting and client seats, enterprises get 24/7 monitoring and services. The Type's identity is the *integration* — one workspace where research, measurement, and diagnosis share the same site/keyword records — and its hardest boundaries are with its own modules' standalone Types (Keyword Research, Site Audit), with SEM account management (write-back vs research), and with web analytics (estimated visibility vs measured traffic).
