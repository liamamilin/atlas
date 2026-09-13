# Research Notes — Career Site Platform

Research date: **2026-09-07**

## Research Goal

Understand what the software category "Career Site Platform" (employer career site / careers site software) actually is: its core objects, its candidate-facing and employer-facing surfaces, how job content flows onto the public site, how the apply seam works, and where it begins and ends relative to Job Board, ATS, Recruitment Marketing Platform, and generic CMS / Website Builder.

## Initial Boundary (working hypothesis before research)

- **What it probably is:** employer-side software for building and operating an organization's own public careers website — the employer's "storefront" for jobs and employer brand.
- **Primary users:** recruiting/talent-acquisition staff, employer-brand or recruitment-marketing staff, admins; candidates are the consuming audience, not operators.
- **Nearest neighbors:** Job Board (multi-employer aggregation), Applicant Tracking System (recruiter-side pipeline), Recruitment Marketing Platform (paid channels + CRM), CMS / Visual Website Builder (generic authoring).
- **Unknowns:** whether job data must originate in an ATS; how many apply-seam forms exist; multi-brand/multi-country structure; whether the category exists standalone or only as an ATS module.

## Research Questions

1. What are the core objects? (job/requisition, job page, site pages/blocks, application, lead, brand/design settings, boards)
2. Where does job data come from and how does it reach the public site?
3. What does the candidate see and do (browse, search, job detail, apply, lead capture)?
4. What does the employer manage, and with what roles/permissions?
5. What lifecycle/states govern publishing (jobs and pages)?
6. What realization forms exist (hosted builder vs embed vs API)?
7. What rules matter (approval, expiry, internal vs external, accessibility, SEO)?
8. Where is the boundary to Job Board / ATS / CMS / Recruitment Marketing?

## Representative Products

Chosen for market representativeness + documentation quality + different product philosophies + different customer tiers:

| Product | Posture in sample |
|---|---|
| **Phenom** (Career Site + Design Studio CMS) | Enterprise talent-experience suite; career site as a named product with its own CMS; personalization/AI-led |
| **Radancy** (Talent Acquisition Cloud, "Career Site & CMS" / BCX) | Enterprise recruitment-marketing suite; career site as a product area of the suite |
| **Teamtailor** | Mid-market ATS-first product with a first-class career site builder; employer-branding-led |
| **Greenhouse** | Enterprise/mid ATS; hosted "job board" surfaces + documented careers-page integration options |
| **Workable** | SMB/mid ATS; three documented careers-page delivery options (builder / widget / API) |

## Sources

**Teamtailor (Tier 1 — official support center, fetched 2026-09-07):**
- Support center index: https://support.teamtailor.com/ (collections: Career Site & Content [31 articles], Publish Jobs [19], Multi-Brand & Entity Solutions [6], Analytics & Insights)
- Building your career site: https://support.teamtailor.com/en/articles/128990
- Career site: Default pages: https://support.teamtailor.com/en/articles/9881375
- Career site: Lead pages: https://support.teamtailor.com/en/articles/2904179
- Job statuses: https://support.teamtailor.com/en/articles/2611060
- Publish Jobs collection: https://support.teamtailor.com/en/collections/33020
- Career Site & Content collection: https://support.teamtailor.com/en/collections/33106

**Greenhouse (Tier 1 — official support, fetched 2026-09-07):**
- External job board overview: https://support.greenhouse.io/hc/en-us/articles/21270826058907
- Customize your job board: https://support.greenhouse.io/hc/en-us/articles/18996861758363
- Getting started with careers page integration: https://support.greenhouse.io/hc/en-us/articles/11913197669019
- Job boards search: https://support.greenhouse.io/hc/en-us/search?query=job+board

**Workable (Tier 1 — official help, fetched 2026-09-07):**
- Help index: https://help.workable.com/
- Comparing careers page options: https://help.workable.com/hc/en-us/articles/115012944968
- Careers page search: https://help.workable.com/hc/en-us/search?query=careers+page
- (support.workable.com redirects to Workable's own careers page; the live KB is help.workable.com)

**Phenom (Tier 2 — official product pages, fetched 2026-09-07):**
- Root: https://www.phenom.com/
- Career Site product page: https://www.phenom.com/career-site
- CMS / Design Studio product page: https://www.phenom.com/cms

**Radancy (Tier 2 — official pages; help centers login-gated, fetched 2026-09-07):**
- Root: https://www.radancy.com/ (Talent Acquisition Cloud; "Branded Candidate Experiences"; "Employer Brand & Experience")
- Support center index: https://support.radancy.net/hc/en-us (public taxonomy shows a "Career Site & CMS" product area and a "Branded Candidate Experience (BCX)" help center)
- Career Site & CMS help center: https://careersite.support.radancy.net/hc — **login-gated (SSO), articles not reachable**

**Source-access limitation:** Radancy's operational career-site documentation is behind SSO; all Radancy-based claims are limited to public marketing pages and the public support-center taxonomy. Phenom has no public operational help center; Phenom-based claims are Tier 2 product-page statements, used only where structurally corroborated by Tier 1 evidence from other products. No numeric limits, defaults, or timings are asserted in the final document beyond what Tier 1 sources state.

---

## Product Observations

### Teamtailor (Tier 1 — evidence layer A)

- Career site is a first-class editor area of the product ("Career site" in the top menu). Site = pages built from **content blocks**; **Design settings** hold fonts, logos, colors; custom HTML/CSS/JS can be applied.
- **Default pages are auto-generated from account data**: Home; **Jobs** (all published jobs findable; Jobs block supports layouts incl. an interactive map); **Departments** (overview + one customizable page per department, generated from Settings → Organization → Departments); **Locations** (overview + one page per location); **People** (employee profiles; an employee appears only with profile image and an admin-set "Show profile on career site" toggle; categorized by department/location); **Posts** (company updates archive with tags); Team Stories (add-on page).
- Additional page types: **Custom pages**, **Location pages**, **Lead pages** ("engage passive talent by encouraging an initial conversation instead of an application"; connected to a job; candidate submits email/phone → "automatically create a candidate profile and link them to the job", tagged *Lead* with source), **Campaign pages**.
- Publishing lifecycle: pages **preview before publishing** ("Save, collaborate, and preview your content updates before making them public"); lead pages move **Draft → Published**.
- **Job statuses** (observed table): Draft; **Published** ("active on your career site, available for all visitors"); **Pending publication** (created by a Hiring Manager, "awaiting approval from ... Recruitment Leads ... and Admins"); **Scheduled** (publishes at start date); **Unlisted** (public application closed; "anyone with access to the unlisted job ad link can still apply"; can be used to "test the full application flow ... without it appearing on your career site"); **Expired** (end date passed → "removed from the career site"); Archived (closed, moved to archived list); **Internal** ("published internally and will not be found on the career site"); Protected (from protected job template).
- Apply seam variants (observed articles): native **application form** with questions (incl. video questions) and conditional logic; **redirect to an external application form** (apply button goes to an external URL); **Mailbox** (email applications transferred into the job); candidate endorsements.
- Job-ads layer: job templates, SEO optimization for job ads, sharing images, **trackable share links** ("track the number of visits and applications generated"), **QR codes** for postings and career-site pages, transparent recruitment (connected candidates follow application progress), internal recruitment feature.
- Site infrastructure: **custom domain** ("connect your own domain"; "use your Teamtailor career site as your main website"), redirect to own site, **career sites in multiple languages**, SEO optimization article, **accessibility** article + accessibility statement, sharing images per page.
- Era-current: career sites "support key open standards designed for the emerging agentic web" — `llms.txt`, AI-friendly `robots.txt`, sitemaps, link headers, markdown content negotiation, content signals — "enabled automatically, no additional setup".
- Support-center taxonomy confirms adjacent modules: **Promote** (boost job ads), **Channel Integrations** (job boards/channels), Multi-Brand & Entity Solutions.

### Greenhouse (Tier 1 — evidence layer A)

- Hosted public surface is called the **(external) job board**: "a page created in Greenhouse Recruiting that links to your external job posts". A **job post** is "a page created in Greenhouse Recruiting that includes a description of the role you're hiring for, its location, and an application form".
- **Terminology definition (from official docs):** "**Careers page:** The page on your organization's website where you list open roles, often called 'Careers,' 'Jobs,' 'Opportunities,' or 'Work with us'."
- **Multiple external job boards** per organization (tier-gated); documented use cases: one board per candidate language, one board per business entity. Board status can be changed **to live**.
- **Internal job boards** exist as a separate surface (Greenhouse-hosted internal job board; post internal jobs; host outside); customization article covers both internal and external boards.
- **Board customization**: Design Studio ("preview your changes as you make them, then apply your design to as many boards as you'd like"); colors (preset theme or per-element); fonts (Google Fonts or up to 8 custom fonts; primary/secondary roles); buttons (shape; apply-button text up to 25 characters); form-field label position; banners/logos; board layout (post list stacked vs side-by-side; display or hide departments/hierarchies); **filters** ("Allow jobs to be filtered by..." Department, Office, up to 5 custom fields; dropdowns on the board); hiring-team display (hiring manager + recruiter names per post). Permissions: customization is a **Site Admin** action. Candidate self-schedule and availability pages inherit board styles.
- **Careers-page integration** ("Getting started with careers page integration"): integrate boards/posts "with the career page you already have on your organization's website. This is key to ensuring that candidates who apply through your career page will be brought into Greenhouse Recruiting." Names website builders/CMS (WordPress, Squarespace, HubSpot) as the counterpart systems. **Five documented integration options** with tradeoffs: minimal code changes; embed the job board; customize order/appearance or segment by office/department; keep applicants on your website with a (less customizable) application form; full creative control + tracking pixel + ADA AA compliance. "Options 1–4 are all compliant with ADA level A."
- **Off-site apply integrations**: Indeed Apply, LinkedIn Easy Apply — "candidates can apply directly from the Indeed or LinkedIn sites without needing to ... navigate to your company's careers page."

### Workable (Tier 1 — evidence layer A)

- Dedicated **Careers page** section in Recruiting settings; a careers-page **site builder** ("user-friendly builder - no coding required"), sections built like Header; **page editors** can be invited (e.g., marketers/designers) who "can add sections and images, change the styling, and publish the page" but not access the rest of the product.
- **"Comparing careers page options"** documents three delivery realizations of the same careers site:
  1. **Careers page site builder** — hosted at `apply.workable.com/[companyname]` or a custom domain (plan-gated); "on-brand careers site that can act as a single source of truth for candidates"; grouping & listing by location or department, further customizable with CSS; invite page editors.
  2. **Workable Widget** — auto-generated code pasted into the employer's own website, "inherits its formatting (font, color, etc.)".
  3. **Custom with API** — "maximum flexibility, can be built from scratch by your team"; "a full website team is needed, including front-end developers".
- **"All options will automatically update when you post new jobs or remove existing ones from your account."** — the job record set drives every delivery surface.
- Disabling the careers page removes jobs "from the careers page and job boards, and candidates will no longer be able to apply". Careers pages are mobile-optimized. API-based careers page is an explicitly supported pattern (API token, API docs). Related: GDPR automation features referenced in the same section.

### Phenom (Tier 2 — vendor product pages; structural claims corroborated elsewhere)

- Markets **"Career Site"** as a named product, self-described "AI-Powered Career Site Platform": "Engage job seekers with personalized experiences that reflect your employer brand ... best-fit job recommendations and content that match their skills, interests, and geographic location to help them apply faster."
- Documented capabilities (vendor-stated): dynamic content & personalization (two visitors see different jobs/content); **Talent Community** ("Capture passive candidate leads and build an engaged community ... nurture with email and SMS campaigns"; multiple communities by location/job category); conversational **Chatbot** on the career site (job discovery, Q&A, interview scheduling); **Intelligent Search** (semantic); **Digital Accessibility** built-in.
- **Design Studio / CMS** ("Design Studio for AI Career Sites"): no-code drag-and-drop editor; "create, edit, and publish pages from job descriptions to company overviews"; manage multilingual content across 115+ languages from one interface; "unlimited brand themes" (multi-brand: business units each get their own career-site identity); generative AI drafting of job descriptions/blogs/copy.
- **ATS/HCM integration**: "bi-directional sync"; "Job data, requisition status, candidate and location information stay current automatically. Recruiters do not need to manually update the career site when a role closes or a new one opens."
- Related products listed alongside: CMS, University Recruiting, Chatbot, Talent CRM, X+ Screening, Direct Sourcing — the career site sits inside a suite.

### Radancy (Tier 2 — public pages only; help centers gated)

- Suite positioning: "Radancy Talent Acquisition Cloud"; a public support-center taxonomy card named **"Career Site & CMS"** ("Login to explore features, best practices, and troubleshooting guides") confirms career site + CMS is a distinct product area of the suite; a separate help center exists for **"Branded Candidate Experience (BCX)"** ("managing your BCX").
- Root page capability claims: "Branded Candidate Experiences — ... build and activate employer brands across all candidate touchpoints – driving attraction, engagement and conversion"; employer brand & EVP research; personalized messaging; consistent brand experiences "deployed through the Radancy Talent Acquisition Cloud".
- No operational detail reachable; per source-access limitation, Radancy is used only as market-structure evidence (that a major enterprise vendor ships a dedicated career site + CMS product area), not for workflow claims.

---

## Cross-product Comparison

| Structure / capability | Teamtailor | Greenhouse | Workable | Phenom (T2) | Radancy (T2) |
|---|---|---|---|---|---|
| Employer-operated public careers web presence | ✔ hosted builder, custom domain | ✔ hosted boards + careers-page integration options | ✔ builder / widget / API | ✔ hosted career site | ✔ product area |
| Job pages driven by the org's own openings; publish state controls visibility | ✔ (job statuses; Jobs page) | ✔ (job posts; board links to posts; status to live) | ✔ ("automatically update when you post/remove") | ✔ (bi-directional sync claim) | ✔ (inferred, gated) |
| Auto-generated job/department/location structures | ✔ default pages | ✔ filters by department/office; multiple boards per entity/language | ✔ grouping & listing by location/department | — | — |
| No-code branding/design customization | ✔ design settings, blocks, custom code | ✔ Design Studio (colors/fonts/buttons/banners) | ✔ builder, page editors, CSS | ✔ Design Studio claim | ✔ (BCX, gated) |
| Employer-brand content pages (culture/people/testimonials) | ✔ blocks: Workplace & Culture, People, Testimonial; Posts | — (board-focused; customization only) | ✔ builder sections | ✔ company overviews claim | ✔ EVP claims |
| Candidate response path on the site | ✔ native form / external redirect / email (Mailbox) | ✔ application form on post / off-site apply (Indeed, LinkedIn) | ✔ apply on hosted page / widget / API-built | ✔ apply + chatbot claim | — |
| Passive-candidate capture surface | ✔ Lead pages → auto candidate record | — | — | ✔ Talent Community | — |
| Multiple boards / brands / languages | ✔ multi-language; Multi-Brand & Entity collection | ✔ multiple boards (language/entity use cases); internal boards | — (single hosted page; API for more) | ✔ unlimited brand themes; 115+ languages claim | ✔ global suite |
| Draft/preview/publish for site content | ✔ preview before publish; Draft→Published (lead pages) | ✔ Design Studio preview; board status live | ✔ publish in builder | ✔ create/edit/publish claim | — |
| Publishing approval gate on jobs | ✔ Pending publication (role-based) | — (tier/permission structure exists; approval flow not observed) | — | — | — |
| SEO / sharing / discoverability | ✔ SEO articles (site + job ads), sharing images, QR, trackable links; AI-agent standards (llms.txt etc.) | — (integration docs mention tracking pixels) | ✔ custom domain; iframe notes | — | — |
| Accessibility posture | ✔ accessibility article + statement | ✔ options 1–4 ADA level A; option 5 for AA | ✔ (mobile-optimized; not observed re WCAG) | ✔ digital accessibility claim | ✔ accessibility policy page |
| Site performance analytics | ✔ trackable links (visits/applications); Analytics collection | — | — | ✔ conversion claims | ✔ Insights area (gated) |
| Internal-only job surface | ✔ Internal status | ✔ internal job boards | — | — | — |

Legend: ✔ = directly observed (A) unless marked (T2) = vendor page claim; — = not observed in fetched sources (absence of observation, not absence of feature).

---

## Abstraction Levels

### L0 — Defining Invariant (minimal)

Four properties; removing any one stops the product from being a career site platform:

1. **Employer-operated public careers web presence** — a public web presence dedicated to one organization's employment opportunities, operated by that organization (hosted by the platform, embedded into the corporate site, or API-built by the employer on top of the platform's data — realization is variant; the employer-owned public presence is invariant).
2. **Job-content binding** — the presence's primary content is pages for the organization's own open positions, rendered from managed job records whose publication state controls public visibility (add/change/remove at the source is reflected on the site).
3. **Candidate response path** — every public listing carries a defined route for a candidate to respond or express interest (in-site application form, redirect to an external form, instructed contact channel, or off-site apply integration) that creates or hands off a candidate record/contact.
4. **Employer-side management machinery** — the employer (not an outside developer, as a rule) controls branding, page content, and the publication of job content through the platform — via a no-code editor, site settings with delegable editor roles, or a management API + auto-updating feed.

This is deliberately realization-free: hosted builder (Teamtailor, Workable builder), embedded widget (Workable widget, Greenhouse embed options), API-built front-end (Workable API, Greenhouse option 5), enterprise CMS platform (Phenom, Radancy) all satisfy the four properties.

**§24 historical/market check:** a pre-SaaS employer "join us" page (static HTML listing + `jobs@company` email) satisfies properties 1–3 but not 4 — it is a hand-built page, not a platform; the Type is the software category that lets employers operate such a presence continuously. Conversely, older/regional/platform-native deployments (corporate-site job scripts, agency-hosted microsites, multi-country "recruit sites") satisfy all four once the employer manages them through tooling — so nothing in L0 may depend on modern SaaS specifics (AI, chatbots, personalization, cloud hosting, talent communities).

### L1 — Common Mature Structure

Present across most sampled products; expected by the market; not definitional:

- job search/browse surface: keyword search plus filters (department, location/office, custom fields) and grouping views (incl. map layouts in one product)
- employer-brand content pages: home/landing, culture & values, benefits, teams/departments, locations, people/testimonials, content posts
- generated structural pages derived from account data (departments, locations) rather than hand-maintained
- no-code design/branding layer (colors, fonts, logos, banners, buttons) with preview-before-publish and delegable page editors
- application-form machinery (configurable questions; conditional logic and rich question types in some products)
- integration seam to the recruiting backend: auto-reflection of job state, applications handed into the ATS/candidate pool, candidate auto-creation from lead capture
- SEO and sharing machinery (meta/sharing images, sitemaps, custom domains, shareable/trackable links)
- accessibility posture (documented at multiple products, from statements to compliance-level choices)
- multi-surface governance: multiple boards/brands/languages from one platform for larger employers
- site performance measurement (traffic/visits/applications by source; conversion)

### L2 — Variant / Optional Structure

- **Delivery realization:** hosted site builder vs embeddable widget vs API-built front-end (one product documents all three as options); level of creative control traded against setup complexity
- **Packaging:** standalone enterprise suite product (career site + CMS as named products) vs ATS-embedded module (mid-market/SMB default) vs recruitment-marketing suite member
- **Job data source:** native job records vs ATS/HRIS sync (one-way or bi-directional) vs API-fed
- **Scale structures:** multi-board (per language, per business entity), multi-brand themes, multi-country site networks, consolidation of many sites into fewer
- **Passive-talent capture depth:** lead pages / talent communities with nurture linkage (email/SMS campaigns) — absent in board-style implementations
- **AI posture:** personalized recommendations, semantic search, chatbots, generative content — era-current, product-dependent, none definitional
- **Internal-only surfaces:** internal job boards / internal job statuses excluded from the public site
- **Niche tuning:** university/early-careers sites, high-volume hiring, per-industry brand content
- **Off-site apply integration** (apply happening on external job boards) as a companion rather than on-site behavior

### L3 — Vendor-specific (research notes only)

- Phenom: X+ platform framing, Design Studio naming, Fit Scores, "115+ languages", "200 career sites → 22 across 28 languages" (DHL claim), chatbot/interview-scheduling linkage, University Recruiting product
- Radancy: BCX naming, "Career Site & CMS" help-center brand, media/exchange machinery (belonging to recruitment-marketing Type)
- Greenhouse: "Design Studio" naming, exact tier gates (Core/Plus/Pro; internal boards Plus/Pro), 1,500+ Google Fonts / up to 8 custom fonts, 25-character apply-button limit, up to 5 custom-field filters, up to 3 hiring-team names displayed, ADA-level claims per integration option
- Teamtailor: Co-pilot suggested-candidates status, Team Stories add-on, Career button widget, job symbols/IDs, specific status color system
- Workable: widget naming, `apply.workable.com/[companyname]` URL pattern, plan-gated custom domain, page-editor role scope

---

## Vendor-specific Findings

See L3. The only cross-cutting caution: enterprise vendors (Phenom, Radancy) sell the career site inside suites where the same surface is also marketed under recruitment-marketing language ("branded candidate experiences", "employer brand activation"). The surface is shared vocabulary between Types; the software's career-site component is what this Type describes.

## Boundary Findings

- **vs Job Board:** the deciding test is whose jobs the public surface lists. A career site presents **one organization's own openings** on the organization's own presence; a Job Board aggregates postings from **many** employers (marketplace posture, cross-employer search, employer-neutral rules). Naming collision to record: Greenhouse officially calls its hosted single-employer surface a "(external) job board" — the label is product vocabulary, not the Type. The Job Board Type remains distinct; this leaf documents the employer-owned surface.
- **vs Applicant Tracking System:** ATS is the recruiter-side pipeline (requisitions, candidates, stages, outcomes). The career site is the candidate-facing public storefront. Greenhouse's own docs formalize the seam: applications through the careers page are "brought into Greenhouse Recruiting". In mid-market products the two are modules of one platform; the surfaces and audiences still differ.
- **vs Recruitment Marketing Platform:** recruitment marketing spans owned surfaces + paid channels + candidate CRM + attribution; the career site is the owned surface itself. The career-site leaf is the surface-owner Type; distribution to external boards, programmatic spend, and CRM campaigns belong to the recruitment-marketing leaf (already processed jointly with this vocabulary).
- **vs CMS / Visual Website Builder:** generic authoring tools have no job-content binding, no generated job/department/location structures, and no apply machinery. Greenhouse's integration docs treat the corporate CMS (WordPress, Squarespace, HubSpot) as the *counterpart system* the career site connects to — strong evidence they are different Types even when the employer renders its careers page inside the CMS.
- **vs internal-facing Types (Employee Portal, Career Development Platform, Internal Talent Marketplace):** internal surfaces serve existing employees; the career site is external and pre-application. Products enforce this boundary explicitly (internal statuses "will not be found on the career site"; separate internal job boards). An internal board feature in a career-site product is a variant surface, not a second Type.

**"Remove one thing" tests:**
- remove the single-employer ownership → many-employer aggregation → Job Board
- remove the public candidate-facing site (keep pipeline) → ATS
- remove the job-content binding and apply path → generic CMS/website builder
- remove the employer-side management machinery → a hand-built static careers page, not a platform

## Uncertainties

1. **Radancy operational mechanics** — help articles SSO-gated; no workflow claims made from Radancy. Its suite posture (career site + CMS as product area) is the only use.
2. **Phenom operational depth** — no public operational help center; personalization/chatbot/AI claims are vendor-stated and were admitted only as variant/optional structure, not core.
3. **Job-alert subscriptions** — market-familiar capability, but not directly observed in fetched sources; deliberately excluded from the final document rather than asserted.
4. **Structured-data / Google-for-Jobs SEO specifics** — not directly observed; SEO support written generically from observed article existence (site SEO, job-ad SEO, sharing images).
5. **AI-agent discoverability standards** (`llms.txt`, content signals) — observed at one product (2026-era); kept product-qualified as an optional, emerging pattern.
6. **Approval gates on job publication** — observed at one product (role-based pending-publication); written as "some products" behavior, not universal.
7. Whether a meaningful standalone (non-ATS, non-suite) career-site-builder market exists below the enterprise tier: the sampled mid-market/SMB delivery is ATS-embedded; enterprise delivery is suite/product. If such a standalone SMB market is significant, it fits the same L0 with native job records; no boundary impact.

## Final Synthesis

A **Career Site Platform** is employer-side software for building and operating an organization's own public careers web presence. Its defining structure: the organization's openings, held as managed job records, are published as public job pages whose visibility follows their publication state; the site carries the employer's brand content around those openings; every opening offers a candidate response path that captures or hands off the candidate; and the employer — typically recruiting, employer-brand, or marketing staff rather than developers — controls design, pages, and publishing through the platform, in whatever realization the organization chooses (hosted builder, embeddable surface inside the corporate site, or an API-built front-end over the platform's data).

Everything else the market ships — search and filters, generated department/location pages, testimonials and culture content, lead capture and talent communities, personalization and chatbots, multi-brand/multi-language networks, accessibility and SEO machinery, analytics — is mature common structure or segment-dependent variant, not definition. The Type's identity comes from the four invariants; the product landscape varies mainly in where the job data lives (native vs synced vs API-fed), which delivery realization is used, and how much of the recruiting backend ships in the same box.
