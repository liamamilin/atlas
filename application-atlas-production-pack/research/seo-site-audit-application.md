# Research Notes — SEO Site Audit Application

Research date: 2026-09-07
Slug: seo-site-audit-application
Directory leaf: SEO Site Audit Application (§06 Marketing, Advertising & Growth)

---

## Research Goal

Understand what an SEO Site Audit Application really is as an Application Type: its core objects, its defining workflow, what its issue model looks like, how findings are organized and acted upon, and where its boundaries sit against the SEO Platform, the Keyword Research Application, security scanners, and website monitoring tools.

## Initial Boundary (working hypothesis before research)

- Core hypothesis: the Type is software that crawls a website, evaluates each page against SEO rules, and organizes the findings into a prioritized, fixable report.
- Likely users: SEO specialists, agencies, site owners.
- Likely confusions:
  1. SEO Platform (broader suite; audit is one module in many suites)
  2. Keyword Research Application (query-centered vs site-centered; sibling leaf already processed with boundary note "keyword at center vs sites/pages/backlinks")
  3. Security/vulnerability scanners (same crawl→evaluate→report shape, different rule library and audience)
  4. Website monitoring / uptime tools (live availability vs point-in-time semantic evaluation)
  5. A raw web crawler without evaluation (component, not the audit Type)
- Unknowns: is a recurring/scheduled crawl definitional or common? Is a health score definitional? Is JavaScript rendering definitional or era-dependent? Do older desktop crawlers satisfy the core (historical check)?

## Research Questions

1. What is the unit of work — the crawl, the audit, the page, or the issue?
2. How does a site enter the tool (crawl from a seed URL; sitemap; URL-list import; project setup)?
3. What is the canonical issue taxonomy? (response codes, redirects, titles/meta, headings, content/duplicates, canonicals, directives, hreflang, images, links, structured data, sitemaps, performance, security, etc.)
4. How are findings classified and prioritized? (issue/warning/opportunity; errors/warnings/notices; importance levels; severity ranking; per-issue URL counts)
5. What is the issue lifecycle? (found → reported → fixed → verified on recrawl; ignored issues; issue trends across crawls)
6. What surfaces exist? (overview/health dashboard, issue reports, per-URL explorer, crawl configuration, exports)
7. What rules/constraints matter? (crawl limits, robots.txt, rendering, authentication, scope/segmentation)
8. How do standalone crawler-specialists differ from suite modules in structure (if at all)?
9. Historical check: do older desktop crawlers (Xenu Link Sleuth era; Screaming Frog's own 2010-era form) still satisfy the definition?

## Representative Products

Chosen for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Form | Philosophy | Tier |
|---|---|---|---|
| Screaming Frog SEO Spider | Standalone desktop app (Win/mac/Linux) | raw crawl data first; issue layer on top; configurable crawler | free tier + low-cost annual licence; agencies/pros |
| Sitebulb | Standalone desktop + Cloud | audit workflow guidance; prioritized Hints; in-built education; client communication | professional SEOs, consultants, agencies |
| Semrush Site Audit | Suite module (cloud) | severity-ranked issues, industry-benchmarked health score, beginner-friendly explanations | SMB → enterprise (suite subscription) |
| Ahrefs Site Audit | Suite module (cloud) | data-first; issue categories + explorers over crawled data; fix-priority segmentation | free tier → suite subscription |
| Moz Pro Site Crawl | Suite module (cloud) | accessible mid-market; weekly automatic crawl; ignore/mark-fixed lifecycle | SMB/mid-market |

Deliberately covered both packaging poles (standalone specialist vs suite module) and both delivery forms (desktop vs cloud).

## Sources

All fetched 2026-09-07 (Tier 1 where noted):

- Screaming Frog — product overview page: https://www.screamingfrog.co.uk/seo-spider/
- Screaming Frog — SEO Issues library (Tier 1, issue taxonomy): https://www.screamingfrog.co.uk/seo-spider/issues/
- Sitebulb — product homepage: https://sitebulb.com/
- Sitebulb — Hints explanation library (Tier 1, issue taxonomy + metadata model): https://sitebulb.com/hints/
- Ahrefs — Site Audit product page: https://ahrefs.com/site-audit
- Moz — Site Crawl product page: https://moz.com/products/pro/site-crawl
- Semrush — Site Audit features page: https://www.semrush.com/features/site-audit/

Source-access limitation: Semrush help-center (KB) article URLs were not reachable (404 on attempted KB paths; the features page was reached via navigation). Semrush observations below are limited to the features page level; no operational details (limits, defaults) are claimed from memory. Moz evidence is at product-page level; its in-app issue list beyond examples named on the page is not documented here. Screaming Frog's User Guide itself was not fetched (the Issues library served the same evidentiary role for the issue model); crawler mechanics (breadth-first discovery, storage engine) come from the vendor's own FAQ summary on the product page.

---

## Product Observations

### Screaming Frog SEO Spider (evidence: A — directly observed, product page + issues library)

- Self-description: "a website crawler that audits your site for over 300 SEO issues"; positioned for "technical SEO site audits"; used by SEOs/agencies.
- Form: desktop application for Windows/macOS/Linux. Free tier limited to 500 URLs per crawl; paid licence removes the limit. (Vendor-stated figures; recorded as vendor facts, not generalized.)
- Crawl mechanics (vendor FAQ summary): crawls "like Googlebot discovering hyperlinks in the HTML using a breadth-first algorithm"; configurable hybrid storage engine for large sites; raw HTML by default, optional headless Chromium rendering for JavaScript sites.
- Issue model (Issues library): 300+ issues each carrying a **type** — Issue (error to fix) / Warning (check, potentially fix) / Opportunity (potential improvement) — and an estimated **priority** — High / Medium / Low — "based upon the potential impact… from broadly accepted SEO best practice. They are not hard rules… they lack context. Issues provide direction to users who can make sense of the data."
- 24 issue categories: Response Codes; Security; URL; Page Titles; Meta Description; H1; H2; Content; Images; Canonicals; Pagination; Directives; Hreflang; JavaScript; Links; AMP; Structured Data; Sitemaps; PageSpeed; Mobile; Accessibility; Analytics; Search Console; Validation.
- Example issues: Internal Client Error (4XX) [Issue, High]; Internal Server Error (5XX) [Issue, High]; Redirect Loop [Issue, High]; Noindex [Warning, High]; Page Title Missing [Issue, High]; Page Title Duplicate [Opportunity, Medium]; Canonical Multiple Conflicting [Issue, High]; Hreflang Missing Return Links [Issue, High]; Exact Duplicates [Issue, High]; Spelling Errors [Issue, Medium].
- Per-issue explanation pages ("guidance on how to fix", "handwritten by professional SEOs, not AI") linked from each issue.
- Workflow affordances: bulk export of errors + source URLs "to fix, or send to a developer"; export of onsite elements (URL, title, meta, headings) as a base for SEO recommendations; crawl comparison ("track progress of SEO issues… see what's changed between crawls"); staging-vs-production URL-mapped comparison; scheduled crawls with auto-export (incl. Google Sheets); command-line automation; segmentation; site-architecture visualisations; XML sitemap generation.
- Integrations: Google Analytics, Google Search Console, PageSpeed Insights APIs; external link metrics (Majestic/Ahrefs/Moz); AI-prompt extraction (OpenAI/Gemini/Ollama/Anthropic).
- Companion product exists (Log File Analyser) — separate product, not part of this Type's core.

### Sitebulb (evidence: A)

- Self-description: "the revolutionary website crawler for better SEO audits"; "makes technical SEO easier… with prioritized Hints, in-built education, and data visualizations"; "fast-track the audit phase, get to actionable insights quicker, and have total confidence in your recommendations."
- Form: Desktop (up to 500,000 URLs per audit) and Cloud (up to 10m URLs per audit; real-time team collaboration on the same crawl data; scheduled recurring crawls). (Vendor-stated figures.)
- Audit-workflow framing, in the vendor's own four stages: Discovery (crawl any website) → Prioritization (300+ issues "automatically checked and prioritized") → Understanding (in-depth, "client-friendly" explanations for every issue) → Communication (visualizations, spreadsheet exports, PDF reports).
- Hint model (Hints library): Hints = "SEO issues and opportunities, presented via 300+ prioritized Hints", organized in 15 sections: Indexability; Links; On Page; Redirects; Internal; Search Traffic; XML Sitemaps; Security; International; Accessibility; AMP; Duplicate Content; Mobile Friendly; Performance; Rendered.
- Each Hint carries two classification dimensions: **Importance** (Critical / High / Medium / Low / Insight) and **Warning Type** (Issue / Opportunity / Potential Issue), plus **No. of URLs affected** and **Coverage** (affected as a percentage of all URLs that could be affected) — "these two values give you an idea of the scale of the issue."
- Every Hint links to a public explanation page: why it matters, examples, how to fix.
- URL List per Hint with export (CSV or direct Google Sheets upload).
- Integrations: GA, GSC, Google Sheets, Data Studio. JavaScript crawling included ("no extra cost").
- Explicitly positions itself between desktop crawlers (Screaming Frog) and enterprise cloud crawlers (Botify) — market-structure evidence for the packaging poles.

### Semrush Site Audit (evidence: A at features-page level; KB unreachable — see limitation)

- Self-description: "Find the technical issues hurting your site's visibility. Get lists of site errors that prevent search engines and AI systems from ranking and mentioning your site, along with tips for fixing each one." Framed as "Technical Site Health" feature of the Semrush platform.
- Issue list "ranked by severity. Fix the highest severity issues first"; "issues are weighted by severity."
- **Site health score**: "a single metric [that] reflects your site's overall technical condition so you can easily track progress over time"; vendor claims scores are personalized "based on your industry" (product-specific claim, kept here only).
- **Thematic reports**: "score and group issues to help you spot (and improve) your site's weakest areas."
- Every issue "comes with a tooltip explaining how to fix it — no technical SEO background required."
- Recurring operation: "daily, weekly, and monthly data refreshes"; real-time alerts and notifications; automated email reports; white-label reporting; shareable exports.
- AI-era checks: site audit checks AI-crawler accessibility (vendor lists specific AI bots) — "fix issues keeping you out of the conversation."
- Handoff: Trello integration to "send issues directly to my dev team" (vendor FAQ) + CSV export for other task-management workflows.
- Enterprise variant exists: "Enterprise Site Intelligence… JavaScript rendering, crawling for millions of pages, built-in compliance and QA, and accessibility management."

### Ahrefs Site Audit (evidence: A)

- Self-description: "Run a complete SEO audit of your website. Identify, prioritize, and fix 170+ SEO issues."
- Core loop stated on the page: "Site Audit crawls all your website's pages. It flags all possible technical and on-page SEO issues, provides recommendations on how to fix them, visualizes key data in a chart, and delivers an overall SEO health score."
- Issue categories: Slow Pages; Core Web Vitals; Heavy CSS or HTML; Titles; Meta Descriptions; H1 Tags; Content; Duplicates; Indexability; Social Tags; Localization; Links; Redirects; Images; JS; CSS; Robots; Sitemaps; Structured Data.
- Severity segmentation: "segments issues into errors, warnings, and notices, so you know which ones to fix first. You can also adjust their importance for ongoing projects."
- Charts: crawl history (trend), HTTP status distribution, indexability distribution, duplicates, page speed, Lighthouse score history, CrUX performance history, links by destination status.
- Per-issue fix instructions; bulk export of the full issue list (ZIP/CSV) "to fix them or send it to your developers — fixing instructions included."
- Data exploration beyond issues: Page explorer & Link explorer ("250+ data points" per page, vendor-stated); URL details panel (content fields, inlinks/outlinks, hreflang, structured data, duplicates); raw/rendered HTML and text search across the crawl; hreflang network graph; structured-data validation against Google/Schema.org requirements.
- Crawl control: crawl speed, JS rendering, crawl depth, mobile user-agent, authentication for staging/restricted sites, robots.txt review, sitemap verification, segments (isolate subfolder/subdomain issues).
- Recurring: scheduled/recurring crawls and "always-on audits" (24/7) as a product push; IndexNow submission integration; "Patches" — publishing SEO fixes to the site live from the platform (all three are vendor-specific extensions; see L3).
- Packaging: included with the free Ahrefs plan (limited) and suite plans.

### Moz Pro Site Crawl (evidence: A)

- Self-description: "Moz Pro's Site Crawl identifies roadblocks that may keep search engines from successfully crawling your site. Easily spot technical issues and learn how to fix them."
- Purpose framing: "Find and learn how to fix common technical SEO issues that may impede your site's ability to receive high quality traffic, rank, or be indexed… monitor a wide range of site issues like broken redirects, missing title tags… Then prioritize which issues to fix first for maximum effectiveness."
- Tracking over time: "keeps track of new and recurring issues over time. Colorful charts show the breakdown of issue categories, new issues, and total issues; allowing you to easily discover trends…"
- **Issue lifecycle, explicit**: "We explain each issue, its potential impact on your SEO, and tell you how to fix it. Flag issues you wish to ignore, mark issues as fixed, and recrawl instantly to check your work."
- Recurring operation: "automatically crawls weekly and alerts you to any new and critical issues so you can fix them before they cause major problems." (Weekly cadence is vendor-specific implementation; recurring+alerting is the common pattern.)
- Form: part of Moz Pro campaigns (suite module), web-based.

---

## Cross-product Comparison

| Dimension | Screaming Frog | Sitebulb | Semrush Site Audit | Ahrefs Site Audit | Moz Pro Site Crawl | Evidence layer |
|---|---|---|---|---|---|---|
| Site entered by crawl of its own pages | yes (breadth-first, seed-based) | yes (any website, any time) | yes (project-based crawl) | yes ("crawls all your website's pages") | yes (Site Crawl) | B |
| Evaluation produces per-page/URL findings | yes (300+ issues) | yes (300+ Hints) | yes (severity-ranked issue lists) | yes (170+ issues) | yes (issue range incl. broken redirects, missing titles) | B |
| Issue type classification | Issue / Warning / Opportunity | Issue / Opportunity / Potential Issue | (severity ranking; types not enumerated on page) | Errors / Warnings / Notices | (not enumerated on page) | B (all sampled classify; labels vary) |
| Priority/importance level per issue | High / Medium / Low | Critical / High / Medium / Low / Insight | severity weight | fix-first ordering, adjustable importance | prioritization guidance | B |
| Scale shown per issue (URL counts) | per-issue URL sets in app | URLs affected + Coverage % | issue lists with counts (page implies) | issue lists + charts | issue category charts | B |
| Fix guidance per issue | yes (in-app + public explainer pages) | yes (public Hint explanations, client-friendly) | yes (tooltips) | yes ("clear instructions", "fixing instructions included") | yes ("explain each issue… tell you how to fix") | B |
| Health/score metric | (no overall score observed on pages; priorities only) | (scoring metrics referenced in testimonial; not documented) | yes (site health score) | yes ("overall SEO health score") | (overall SEO performance framing; no score named) | B partial — common in cloud suites, not definitional |
| Trend / comparison across crawls | yes (crawl comparison, staging mapping) | yes (scheduled recurring crawls) | yes ("track progress over time") | yes (crawl history charts) | yes (new/recurring issues over time) | B |
| Scheduled/recurring crawls + alerts | yes (scheduling; automation via CLI) | yes (Cloud scheduling) | yes (refreshes, alerts, email reports) | yes (scheduled + always-on) | yes (automatic weekly + new-issue alerts) | B |
| JavaScript rendering | yes (headless Chromium) | yes (included) | yes (enterprise tier) | yes (toggle) | (not documented on page) | B common, not definitional |
| Exports (CSV etc.) / developer handoff | yes (bulk exports, "send to a developer") | yes (CSV, Google Sheets) | yes (CSV, Trello) | yes (ZIP/CSV, "send to your developers") | (charts/reporting documented; exports implied by suite reporting) | B |
| Search-console / analytics integration | yes (GSC, GA, PSI) | yes (GSC, GA, Sheets, Data Studio) | (suite-integrated) | yes (PSI; GSC/GA "soon" per page) | (suite-integrated) | B |
| Segments / scope isolation | yes (segmentation) | (sections per audit; not observed) | (thematic reports) | yes (segments) | (campaign-scoped) | B partial |
| Desktop vs cloud | desktop | desktop + cloud | cloud | cloud | cloud | variant axis |
| Standalone vs suite module | standalone | standalone | suite module | suite module | suite module | variant axis |

Reading of the comparison:

1. The crawl→evaluate→report core is present in every sampled product regardless of form, price, or era — this is the Type's spine.
2. Classification vocabularies differ per vendor (issue/warning/opportunity vs errors/warnings/notices vs importance/insight) but every product classifies and ranks findings. The conceptual invariant is *typed, ranked findings* — not any specific label set.
3. The health score is common in cloud-suite products but absent/unnamed in the desktop pole — common mature structure, not definitional.
4. Recurring crawls + alerts + trend tracking are common modern structure; a one-shot manual crawl audit (Screaming Frog's historic core use; the free-tier pattern) still satisfies the Type.
5. JS rendering is era-typical common structure (post-2010s), not definitional (older crawlers audited raw HTML).

## Canonical Model (synthesis)

**L0 — Defining Invariant** (smallest structure without which the Type is unrecognizable):

1. **The site's own page population as the object of work** — the application discovers/enumerates the pages of the target site itself (crawl from a seed; supplemented by sitemaps/URL lists). Remove → a tool that audits only manually submitted pages is a page checker, not a site audit; a keyword database is a different Type.
2. **SEO evaluation of those pages against a rule library, producing per-page findings** — each discovered page is checked for search-visibility problems (crawlability/indexability, response codes, redirects, on-page elements, content duplication, directives, internationalization, etc.). Remove → a raw crawler/link harvester, not an audit.
3. **The issue report as the managed output** — findings aggregated by issue type, each issue carrying scale (affected URLs), a severity/priority ordering, and fix guidance, organized so someone can work through and act on them. Remove → crawl data without judgment or actionability.

**L1 — Common Mature Structure** (present in most modern products, not definitional):

- typed finding vocabulary (issues vs warnings vs opportunities / errors vs notices) on top of severity ranking
- overall site health score (cloud-suite pattern) and score/issue trends
- recrawl comparison: new/recurring/resolved issues, "mark fixed/ignore" affordances, progress tracking
- scheduled/recurring crawls with alerting on new critical issues
- per-URL data explorer over the crawled population (all page fields, in/outlinks)
- crawl configuration (scope, depth, speed, user-agent incl. mobile, robots handling, authentication for staging)
- JavaScript rendering for client-side sites
- export machinery (CSV/ZIP/sheets) framed as handoff to developers; sometimes direct ticketing integration
- search-console/analytics/PageSpeed integrations layered onto the crawled URL set
- visualizations of site architecture / link structure
- segmentation (isolate subfolder/subdomain/template issues)

**L2 — Variant / Optional Structure** (depends on segment, era, form):

- delivery form: desktop application vs cloud service (both poles satisfy the core)
- packaging: standalone specialist vs SEO-suite module (dominant axis in the market)
- scale ceiling and metering (free tiers with URL caps, licence vs subscription)
- audit-occasion variants: pre-migration/staging audits, periodic health monitoring, client deliverable audits (PDF/white-label reports)
- adjacent evaluation domains bundled in the same crawl: security headers/HTTPS, accessibility (WCAG/axe), spelling/grammar, structured-data validation, mobile usability — present in some products as secondary rule domains
- white-label/agency reporting; collaboration (shared crawl data); PDF client reports
- AI-era additions: AI-crawler accessibility checks; AI-generated explanations; MCP-style query surfaces

**L3 — Vendor-specific Structure** (research notes only):

- Ahrefs: "Patches" (publishing SEO fixes live from the platform), IndexNow submission integration, "always-on" 24/7 crawl positioning, 250+ data-point explorers framing
- Semrush: industry-personalized health scores, named AI-bot accessibility list, Trello integration, Enterprise Site Intelligence packaging, thematic-report branding
- Screaming Frog: custom extraction (XPath/CSSPath/regex), custom JavaScript snippets during crawl, Looker Studio crawl reports, AMP validation, spelling/grammar engine, companion Log File Analyser product
- Sitebulb: "Hints" vocabulary, in-built education positioning, Importance × Warning Type two-dimension metadata, Coverage % metric
- Moz: Campaigns framing, automatic weekly crawl cadence, ignore/mark-fixed implementation

## Rejected Findings (considered, then excluded from the core)

- **"300+/170+ issue counts"** — vendor marketing figures that differ per product; counts belong in research notes, not the definition.
- **Health score** — rejected as definitional: absent/unnamed in the desktop pole; the Type predates scores.
- **Scheduled/recurring crawls** — rejected as definitional: one-shot crawl audits remain a primary usage mode (Screaming Frog's free tier; migration audits).
- **JavaScript rendering** — rejected as definitional: era-typical; raw-HTML crawlers still perform site audits (historical check below).
- **Search-console/analytics integrations** — enrichment layer, not the evaluation itself.
- **Any specific taxonomy label set** (issue/warning/opportunity etc.) — vendor vocabularies differ; the invariant is typed+ranked findings.
- **Fix execution on the site** (e.g. Ahrefs Patches) — single-product; the Type finds and organizes issues, it does not need to fix them.

## Historical / Market-Sample Check (§24 discipline)

- **Older desktop crawlers**: Xenu's Link Sleuth (late-1990s freeware) crawls a site and reports broken links — crawl + evaluation + report, in minimal form. Screaming Frog itself (2010+) began as exactly this shape before growing its issue library. Both satisfy the L0; therefore L0 cannot include scores, schedules, JS rendering, or cloud delivery.
- **Suite modules vs standalone**: the audit capability exists in both packages with the same core; packaging is not part of the definition.
- **Regional products**: local-market crawlers/auditors (e.g., European/Asian SEO toolkits) ship the same core; no region-specific structure is needed.
- **Pre-software "site audit"**: the consulting deliverable (manual expert review) predates the software; the software Type is defined by the tool doing the discovery+evaluation, which the manual form lacks. No conflict.
- Conclusion: L0 passes the historical check. The modern cloud-suite shape (score + schedule + integrations) is the current dominant packaging, not the definition.

## Boundary Findings

| Neighbor Type | Boundary test | What to remove / add to flip |
|---|---|---|
| **SEO Platform** (same directory section) | center-of-gravity: platform = many capabilities (keywords, backlinks, ranks, audit) with sites/pages/backlinks as objects; audit = crawl→issues→fix as the whole loop | remove audit → platform still a platform; add keyword/backlink/rank databases + make audit one tab → becomes platform. Keep both leaves; audit is a frequent suite module (packaging variant, like content-marketing vs content-planning) |
| **Keyword Research Application** (processed sibling) | object of record: query vs page population | keyword tool's unit is the search query and its demand/competition; audit's unit is the site's pages and their SEO condition. Swap object → the other Type |
| **Raw crawler (capability, not a Type here)** | evaluation layer | remove the rule library and issue reporting → link harvester; the audit Type is crawler + evaluator + report |
| **Vulnerability scanner / DAST** | rule library + audience | same crawl→evaluate→report shape, but rules target security flaws and consumers are security teams; SEO rules target search visibility. Shared surface: HTTPS/security-header checks appear in both domains |
| **Website Monitoring / uptime tools** | time semantics + evidence | monitoring = continuous live availability/performance signals with alerting on incidents; audit = point-in-time semantic evaluation of page content/structure. Speed metrics overlap; the rule libraries do not |
| **Browser Compatibility Testing Platform** | evaluation target | cross-browser rendering correctness vs SEO rule satisfaction; different rule sets and audiences |
| **Content Marketing Platform / content quality tools** | lifecycle position | CMP manages production of planned content; site audit evaluates the existing site's technical/on-page condition. Content-quality scoring overlaps at the "content" issue category only |
| **APM / performance tools** | purpose framing | APM measures live performance for engineering; audit evaluates page speed as one SEO issue among many |
| **Log-file analyzers** | evidence source | log analysis infers search-bot behavior from server logs; it is a companion/adjacent analysis, sometimes bundled (Screaming Frog sells one as a separate product) — not the audit core |

## Uncertainties

- Semrush KB-level operational detail unreachable → its in-app issue taxonomy and defaults are not documented here; only features-page claims recorded.
- Moz's full in-app issue list and configuration depth not documented (product-page evidence only).
- Screaming Frog User Guide not fetched; crawler mechanics rely on the vendor's own FAQ summary. Scheduling/comparison features are documented on the product page itself (safe).
- Sitebulb "scoring metrics" mentioned only via a customer testimonial on the homepage — not treated as documented score behavior.
- Whether a health score is now universal in cloud suites is unverified beyond the sampled products (Ahrefs, Semrush yes; Moz not named on the page).
- The exact boundary against an "enterprise SEO crawler/monitoring" category (e.g. Botify-class products: crawl at scale + log files + monitoring) was not directly researched; Sitebulb's own comparisons position Botify as the enterprise cloud-crawler pole. Flagged, not resolved.

## Final Synthesis

An SEO Site Audit Application is defined by a small core: it takes a website's own page population as the object of work (discovering the pages itself), evaluates every page against an SEO rule library to produce per-page findings, and turns those findings into a managed, prioritized, fixable issue report. Everything else commonly seen — health scores, scheduled crawls, trend charts, JS rendering, explorers, integrations, segments, exports — is mature common structure that makes the audit practical at scale, and varies by product form (desktop vs cloud) and packaging (standalone specialist vs SEO-suite module). The issue report is the Type's deliverable: typed and ranked findings, each with scale and fix guidance, worked through and re-verified on later crawls. The Type's boundary is sharpest against the Keyword Research Application (query-centered) and the SEO Platform (multi-capability suite of which the audit is one tool), and structurally closest to security scanners (same shape, different rule library and audience).
