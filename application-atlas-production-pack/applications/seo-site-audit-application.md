# SEO Site Audit Application

## Overview

An **SEO Site Audit Application** evaluates a website's own pages for problems that hurt its visibility in search engines. It discovers the site's pages itself — by crawling — checks every page against a library of SEO rules, and organizes everything it finds into a prioritized, fixable issue report.

The defining structure is small:

```text
The site's own page population (discovered by the application itself)
└── SEO evaluation of every page against a rule library
    └── per-page findings
        └── the issue report (typed, ranked, scaled, fix-guided)
```

What this application is *not*, by definition: it does not need a health score, scheduled recurring crawls, JavaScript rendering, analytics integrations, or cloud delivery — all of those are widespread in current products but a plain desktop crawler producing a crawl plus an issue report is still recognizably this Type. And it does not fix the site: it finds and organizes the problems for someone else to fix.

The object of work is the site's *page population*, not search queries and not backlinks. That is what separates it from keyword research and from the wider SEO platform, of which it is frequently one module.

## Users & Context

Primary users:

- **SEO specialists / technical SEOs** — run audits to find crawlability, indexability, and on-page problems on sites they own or manage; triage the issue report; coordinate fixes
- **Agency practitioners** — run audits as a recurring client deliverable, typically across many client sites; produce exportable, presentable findings
- **Site owners / webmasters** — run occasional audits to understand their site's technical condition

Secondary participants: **developers**, who receive the exported issue lists and do the actual fixing; **marketing managers and clients**, who read the overview dashboards and progress trends.

The work has two rhythms: **episodic** (before a launch, during or after a migration, after a redesign — find and fix everything) and **recurring** (scheduled crawls that watch for new problems and track progress over time). The work happens on a web application or a desktop crawler; the output leaves the application as exports, reports, or tickets handed to developers and stakeholders.

## Core Model

### The defining core

**The site's page population** — the object of work. The application discovers the target site's pages itself: it starts from a seed (typically the homepage) and follows links, commonly supplemented by sitemaps and imported URL lists. Every discovered page becomes a record carrying its crawled properties: URL, response status, redirect path, on-page elements (page title, meta description, headings), content, links, images, robot directives and canonicals, structured data, and — where rendering is enabled — the JavaScript-executed version of the page.

**The rule library** — the evaluator. Each page is checked against a large set of SEO rules. The rule areas are recognizable across products, even though each product's exact check list differs:

- crawlability and indexability — broken links and server errors (4xx/5xx), redirect chains and loops, robots.txt blocks, noindex/nofollow directives, canonical tag problems
- on-page elements — missing, duplicate, too long, too short, or multiple titles, meta descriptions, headings
- content — exact and near-duplicate pages, thin/low-content pages, placeholder content
- links — broken internal and external links, internal linking structure
- international targeting — hreflang problems
- structured data and sitemaps — invalid markup, missing or unparsable sitemap entries
- page performance — slow pages, oversized resources
- security basics — HTTP pages, mixed content

**The issue** — the unit of findings. When a rule triggers on one or more pages, the result is an *issue*: an aggregated finding that carries its list of affected URLs, the scale of the problem, a classification (roughly: an error that should be fixed, a warning to check, an opportunity to improve — every product labels these differently), a severity or priority, and an explanation of why it matters and how to fix it.

**The issue report** — the deliverable. All issues for a crawl, organized by type and ranked by severity, with drill-down from the overview to the issue to the affected URLs to any individual page. The report is what gets exported, handed to developers, and re-checked after fixes.

### One structure, many implementations

The core model is conceptual. Specific implementations vary and must not be confused with the Type itself:

```text
Concept:   discovering the page population
           → link crawl from a seed; sitemap ingestion; URL-list import; staging crawls

Concept:   typed, ranked findings
           → issue/warning/opportunity labels; error/warning/notice labels;
             high/medium/low or weighted severity

Concept:   showing scale
           → affected URL counts; percentage coverage of the site

Concept:   making findings actionable
           → in-app fix guidance; public explanation pages; CSV/sheet exports;
             ticketing handoffs
```

Severity vocabularies and priority weights are vendor-proprietary: the same condition can be ranked differently in different products, and the labels do not transfer between tools.

## How It Works

The canonical workflow is a loop: discover → evaluate → report → fix → re-verify.

```text
Set up the audit (site/scope, crawl settings: speed, limits, user agent, rendering, credentials)
→ crawl the site (fetch pages from the seed, follow links, record every URL's properties)
→ evaluate every page against the rule library
→ review the report (overview → issues ranked by severity → affected URLs → page detail)
→ act (export the issue list, hand to developers or a ticketing tool, fix, ignore what doesn't matter)
→ re-verify (recrawl: fixed issues disappear, new and recurring issues surface)
```

**Set up and crawl.** The user names the target site and its scope, and configures the crawl — how fast, how deep, which user agent, whether to render JavaScript, and which credentials to use for staging or authenticated areas. The crawl then fetches pages and records what each URL returns.

**Evaluate.** The rule library runs over the crawled population. Nothing is judged in isolation: many rules are relational (duplicates across pages, redirect chains, orphan pages, link depth), which is why the whole site — not a single page — is the audit's object.

**Review and triage.** The report's overview summarizes the site's condition (issue categories, distributions, and, in most cloud products, an overall health score). The issue list is the working surface: ranked so the biggest problems surface first, each issue showing how many URLs it affects. The user drills from issue to URLs to individual pages, judging which findings matter in context.

**Act.** Findings leave the application: bulk exports (spreadsheets, ZIP archives, sheets) framed explicitly as handoffs to developers, direct integrations with ticketing tools in some products, or formal client reports.

**Re-verify and track.** After fixes, a recrawl confirms whether issues cleared. Users can flag issues as ignored or fixed, and products track new, recurring, and resolved issues across crawls so progress is visible over time. In mature cloud products this becomes a standing rhythm: scheduled crawls with alerts when new critical issues appear.

**Tiers of capability:**

- **Defining core** — page-population discovery; SEO evaluation into per-page findings; the ranked, fix-guided issue report
- **Standard capabilities in mature products** — health score and trend tracking; crawl comparison; scheduled crawls with alerting; JavaScript rendering; a per-URL explorer over the crawled data; segmentation; exports and report generation; search-console/analytics/page-speed integrations; site-architecture visualizations
- **Optional / segment-dependent** — adjacent rule domains (accessibility, security headers, spelling and grammar, mobile usability); staging-vs-production comparison; white-label and PDF client reporting; team collaboration on shared crawl data; AI-era additions such as AI-crawler accessibility checks and AI-written explanations

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Audit overview / health dashboard

- purpose: judge the site's overall technical condition at a glance
- typical information: overall score (where the product offers one), issue counts by category, distributions (response codes, indexability, page speed, duplicates), trend charts across crawls
- primary actions: start or reschedule a crawl, open the issue report, compare with a previous crawl

### Issue report

The main working surface.

- purpose: turn thousands of crawled pages into a ranked, workable list of problems
- typical information: one entry per issue with its type, severity/priority, and the number of URLs affected; grouped by rule area
- primary actions: open an issue's detail, export, ignore, mark as fixed

### Issue detail

- purpose: explain and scope one finding
- typical information: why the issue matters, how to fix it, the full list of affected URLs
- primary actions: view/export the URL list, send to a developer or ticketing tool

### URL explorer / page detail

- purpose: go beyond predefined issues and inspect any crawled page
- typical information: the page's full record — status, redirect chain, title/meta/headings, links in and out, images, directives, structured data
- primary actions: search and filter the crawled population, inspect a page's record, compare raw and rendered versions where available

### Crawl configuration

- purpose: control what the audit covers and how it behaves
- typical information: scope, URL limits, crawl speed, user agent, rendering toggle, authentication, robots handling
- primary actions: set up a crawl, save segments, schedule recurring runs

### Exports and reports

- purpose: move findings out of the application
- typical information: spreadsheet/ZIP exports per issue or per crawl; client-facing PDF or white-label reports in some products
- primary actions: export, generate report, configure alerting

## Important Rules / Behaviors

- **Findings are advisory, not verdicts.** Severity and priority express estimated potential impact based on broadly accepted SEO practice; vendors document that these are not hard rules — a practitioner interprets them in the context of the specific site and business. The audit directs attention; it does not decide strategy.
- **The audit is only as complete as the crawl.** Only pages the application discovered are evaluated. Pages missed because of scope limits, robots blocks, authentication, or broken discovery are unknowns, not clean results. A page the crawler couldn't reach is itself often a finding.
- **Issues have a state and a lifecycle.** An issue exists until a recrawl shows otherwise: fixed issues disappear on re-verification, ignored issues stay out of the way, and new or recurring issues are tracked as such. Without the recrawl step, "fixed" is a claim, not a fact.
- **Scale is part of the finding.** Issues are reported with affected URL counts — sometimes as a percentage of the crawlable site — because three broken links and thirty thousand are different decisions.
- **Duplicate and similarity detection is heuristic.** Exact, near-duplicate, and similar-content judgments are algorithmic and product-specific; they are signals to investigate, not determinations.
- **Performance numbers vary by run and source.** Where speed metrics come from lab tests or field-data integrations, values differ between runs and between products; they should be compared within one tool.
- **Crawling has constraints.** Crawl speed, URL caps (tier-dependent in several products), and politeness toward the target server shape what an audit run can cover; authenticated and staging areas require explicit credentials.

## Variants

- **Desktop crawler specialist** — a standalone application that crawls from the user's machine; favors raw crawl depth, configurability, and one-off deep audits
- **Cloud suite module** — the audit as one tool inside a broader SEO platform; favors scheduled monitoring, scores, integrations, and handoffs; the dominant packaging in the market
- **Audit occasion** — one-shot deep audits (pre-launch, migration, redesign), recurring health monitoring, and client-deliverable audits with formal reports
- **Scale tier** — free/limited tiers with URL caps up to enterprise offerings crawling at million-page scale
- **Adjacent rule domains** — some products bundle accessibility, security-header, spelling/grammar, or mobile-usability checks into the same crawl
- **AI-era additions** — checks for AI-crawler accessibility and AI-assisted explanations; an emerging, still-product-specific layer

## Related Application Types

| Application Type | Distinction |
|---|---|
| SEO Platform | a multi-capability suite (keywords, backlinks, rank tracking, audits) whose objects are sites, pages, backlinks and rankings; the site audit is one module of most suites — remove the audit and the platform still stands; remove the platform's other tools and the audit still stands |
| Keyword Research Application | the object of record is the *search query* (demand, competition, attainability); the site audit's object is the site's *page population*. Research asks "which queries to pursue"; the audit asks "what is wrong with the pages we have" |
| Vulnerability / security scanner | the same crawl → evaluate → report shape, but the rule library targets security flaws and the audience is security teams; the SEO audit's rules target search visibility. The overlap (HTTPS, security headers) is one rule area, not the Type |
| Website monitoring / uptime tools | continuous live availability and performance signals with incident alerting, versus point-in-time semantic evaluation of page content and structure |
| Browser Compatibility Testing Platform | rendering correctness across browsers versus satisfaction of SEO rules; different rule libraries and audiences |
| Content Marketing Platform | manages the production of planned content; the site audit evaluates the existing site's technical and on-page condition. Content-quality checks touch at one issue category, nothing more |
| Log-file analysis | infers search-bot behavior from server logs; an adjacent or companion analysis (sometimes sold as a separate product), not the audit itself |

The most important boundary is with the SEO Platform, because the audit is so often sold as one of its modules. The test is the center of gravity: if the product's remaining value after removing keyword, backlink, and rank capabilities is exactly the crawl → evaluate → report loop, this Type is the product; if the audit is one tab among many, the platform is the product and this Type is a module inside it.

## Representative Products

- **Screaming Frog SEO Spider** — standalone desktop crawler specialist; the raw-crawl-data pole
- **Sitebulb** — standalone audit specialist (desktop and cloud); prioritization- and communication-led
- **Semrush Site Audit** — suite module; severity-ranked issues with health scoring
- **Ahrefs Site Audit** — suite module; data-first with explorers over the crawled population
- **Moz Pro Site Crawl** — accessible suite module; recurring monitoring with an explicit fix-verify loop

These span both packaging poles (standalone vs suite module), both delivery forms (desktop vs cloud), and several customer tiers; they were used to separate the defining core from vendor-specific implementation.

## Sources

Research date: **2026-09-07**

Official vendor documentation used:

- Screaming Frog — SEO Spider product overview — https://www.screamingfrog.co.uk/seo-spider/
- Screaming Frog — SEO Issues library (issue taxonomy and priority model) — https://www.screamingfrog.co.uk/seo-spider/issues/
- Sitebulb — product homepage — https://sitebulb.com/
- Sitebulb — Hints explanation library (issue metadata model) — https://sitebulb.com/hints/
- Ahrefs — Site Audit product page — https://ahrefs.com/site-audit
- Moz — Site Crawl product page — https://moz.com/products/pro/site-crawl
- Semrush — Site Audit features page — https://www.semrush.com/features/site-audit/

> Sourcing limitation: Semrush help-center (knowledge-base) articles were unreachable from the research environment on 2026-09-07; Semrush claims above rest on the vendor's own features page only, and no operational defaults or limits are stated for it. Moz evidence is at product-page level; its in-app issue list beyond the examples named on the page is not documented. Vendor-stated issue counts, URL caps, and crawl cadences were deliberately kept out of this document and recorded in the paired Research Notes.

Detailed observations, the cross-product comparison matrix, the historical/market-sample check, and vendor-specific findings are recorded in the paired Research Notes.
