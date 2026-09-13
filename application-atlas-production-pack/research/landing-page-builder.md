# Research Notes — Landing Page Builder

## Research Goal

Understand what a Landing Page Builder is as an Application Type: what objects exist inside it, what users do with them, how the build→publish→capture loop works, and where its boundaries sit against Visual Website Builder, Landing Page Optimization Platform, Lead Capture Platform, and A/B Testing Platform.

## Initial Boundary

Hypothesis before research: a Landing Page Builder is a marketing-side tool for constructing single-purpose web pages tied to campaigns, visually and without code, then publishing them to a live URL. Nearest neighbors:

- Visual Website Builder (whole multi-page web presence vs single campaign page)
- Landing Page Optimization Platform (same page object; optimization loop as differentiator)
- Lead Capture Platform (form machinery vs page construction)
- A/B Testing Platform (experiment on external surface vs page-owned object)

Two pre-hung flags exist from prior passes:
1. **visual-website-builder pass (2026-09-09)**: seam hypothesis = unit of work (whole persistent web presence vs single conversion page) + organizing machinery (site assembly vs conversion machinery); Wix markets the two as separate product lines; Carrd noted as near the seam but unreachable in that pass.
2. **landing-page-optimization-platform pass (2026-09-07)**: the two leaves are adjacent poles of one product family (page object shared; optimization loop is the differentiator; a pure builder pole exists in the market); recommends this pass be written design-side (page construction as the job) with the loop as the stated boundary.

## Research Questions

1. What is the unit of record — the page? What does a "landing page" mean to the products themselves?
2. How is the page built (editor model, templates, AI)?
3. How does the page go live (hosting, domains, publishing)?
4. What conversion machinery is built in (forms, leads, popups, ecommerce)?
5. Is testing/optimization part of the core or an add-on?
6. Who uses it (marketer vs developer vs agency)?
7. Where is the line against website builders and against optimization platforms?

## Representative Products

Selected for market representation, documentation quality, and different philosophies/customer tiers:

| Product | Philosophy / tier |
|---|---|
| Unbounce | conversion-first incumbent; marketer self-serve + agency Clients structure |
| Leadpages | small-business pole; aggressive "build + optimize included" positioning |
| Instapage | enterprise ad-to-page pole; post-click optimization framing |
| Landingi | European full-stack builder; agency/enterprise scale features |

Carrd (minimal one-page pole) was targeted but unreachable (see Sources).

## Sources

- Unbounce product page: https://unbounce.com/landing-page-builder/ (fetched 2026-09-10)
- Unbounce Documentation (help center): https://documentation.unbounce.com/hc/en-us — incl. "Learning the Unbounce Platform", "Building Your First Landing Page" (fetched 2026-09-10)
- Leadpages landing page builder product page: https://www.leadpages.com/landing-page-builder (fetched 2026-09-10)
- Instapage Help Center: https://help.instapage.com/hc/en-us — incl. "Landing pages → Basics" article list (fetched 2026-09-10)
- Landingi Help Center: https://landingi.com/help/ — incl. "Platform walkthrough" (fetched 2026-09-10)
- Carrd: https://carrd.co/ and https://carrd.co/docs — request timed out twice; abandoned per network rule
- Prior-pass context: research/landing-page-optimization-platform.md, research/visual-website-builder.md (STATUS.md entries)

## Product Observations

### Unbounce (evidence layer A — official help center + product page)

- Self-describes as a "landing page builder" whose pages are "standalone page[s] used in marketing — it's where a visitor 'lands' when they click one of the ads from your campaign"; "do not usually link to your homepage; their purpose is to encourage visitors to complete the desired action… such as completing a form, clicking a button, or watching a video. This is known as a call to action." (help center, "Building Your First Landing Page")
- Platform structure: account → **Clients** (sub-folders to segment pages, agency pattern) → **Pages** list (All Pages screen with bulk publish/unpublish, filters, grouping by campaign/industry/purpose) → per-page **Page Overview** with tabs: Overview (page views, visitors, conversions), **Leads** (table of leads collected for this page), Integrations (send lead info to CRM/email/webhook), Reporting (Smart Traffic breakdowns).
- Builder: drag-and-drop elements, customizable templates (100+ "professionally-designed"), custom scripts; popups and sticky bars as separate object types with their own list and embed code.
- Publishing: product-hosted; custom domains via CNAME / WordPress plugin / free ubpages.com subdomain; SSL; page-level publish/unpublish.
- Testing machinery exists (A/B testing, Smart Traffic AI routing) but is presented as separate product features alongside the builder — the builder is the front door.
- Other: Script Manager (global custom scripts), IP filters to exclude internal traffic from conversion data, user roles/permissions, AI copywriting, MCP server for AI-assistant page building.

### Leadpages (evidence layer A — official product page; help center unreachable)

- Defines the Type explicitly: "A landing page builder is a tool for creating standalone pages with one job: converting a visitor into a lead or a customer. Unlike a website builder, which is designed for multi-page sites with navigation, a landing page builder is built around a single call to action, typically paired with an ad campaign, an email, or a lead magnet."
- Build: AI page generation from a plain-language prompt grounded in a brand kit; drag-and-drop editor with sections/layouts/widgets; device previews (desktop/tablet/mobile); template gallery.
- Publish: managed hosting, custom domains, custom URL slugs, SEO indexing on paid plans, or a product subdomain.
- Conversion machinery: forms and lead collection built in with email lead notifications and a leads dashboard (search/filter/export); conversion tracking; A/B testing and Smart Traffic (AI variant routing) as plan-tiered features; dynamic text replacement (headline matches the ad clicked); ecommerce checkout with payment gateways on paid plans.
- Also ships "Sites" (multi-page) as a separate product line — packaging drift, consistent with the LPO pass's observation.
- Explicit competitive framing: "Most platforms stop at publish… Leadpages keeps working" — the optimization loop is its differentiator vs pure builders.

### Instapage (evidence layer A — official help center structure)

- Help center top categories: **Landing pages** (Basics, Mobile design builder, Forms in depth, The slideout, Advanced), Websites, Contacts & Emails, **Optimize** (Experiments, Analytics, Dashboard), **Personalize** (Collections, AdMap, Ad-To-Page Personalization), Integrations, Domains and publishing, Account administration.
- Landing pages → Basics article list shows the editor's object vocabulary: page elements (shapes, images, videos, countdown timers, carousels, accordions), forms, page background, fonts/colors, inline CSS editor, custom HTML embed, keyboard shortcuts, page settings right-side menu, templates ("Fluid Block Editor", "Fluid Grid Blocks"), popups (on-page and external popups published on any website), sticky bars, page grouping/sorting/managing in the Landing Pages tab, downloading/uploading pages, migration to a render engine.
- Publishing: custom domain via CNAME, SSL on landing pages.
- Optimize (experiments/analytics) and Personalize (AdMap — ad-to-page mapping; Ad-To-Page Personalization) are separate top-level categories — optimization and personalization are product pillars adjacent to the builder, not the builder itself.
- "Websites" category exists — packaging drift again (full sites inside the same account).

### Landingi (evidence layer A — official help center, "Platform walkthrough")

- Sidebar structure: **Landing Pages** (list of all pages; create, manage, edit in Editor, per-page Dashboard, leads, A/B tests, page download), Smart Sections (reusable sections synced across pages), Lightboxes, Products (sell directly from landing pages), Pop-ups (with display rules), **Programmatic** (generate many pages at scale from a template + spreadsheet of dynamic content), **Leads** (account-level lead management with export), Orders (from on-page selling).
- Settings: domains, fonts, API tokens, payment gateways (PayPal/Stripe/PayU), user roles, subaccounts; Agency Hub (subaccounts per client, package limits, audit logs, shared AI credits).
- Creation: Visual Builder ("total design control"), 400+ templates, AI page generator (Lunar), multi-language pages.
- Optimize: A/B testing, EventTracker (click/intent tracking), Solis (AI insights).
- Publishing options include custom domains and reverse-proxy publishing.
- Explicit self-positioning vs the sibling Type: Landingi markets itself as adding "analytics and experimentation… that a standalone landing page builder does not cover" (recorded in the LPO pass).

## Cross-product Comparison

| Structure | Unbounce | Leadpages | Instapage | Landingi | Reading |
|---|---|---|---|---|---|
| Standalone campaign page as unit of record | ✓ (Pages list, per-page overview) | ✓ ("standalone pages with one job") | ✓ (Landing Pages tab, page settings) | ✓ (Landing Pages list) | Core |
| Single conversion goal / CTA orientation | ✓ (CTA definition in docs) | ✓ (explicit) | ✓ (post-click framing) | ✓ (lead gen / conversion solutions) | Core (purpose-level) |
| Visual no-code construction (drag-and-drop / sections / templates) | ✓ | ✓ | ✓ | ✓ | Core |
| Product-operated hosting + custom domain publishing | ✓ (CNAME/plugin/subdomain, SSL) | ✓ (managed hosting, domains, slugs) | ✓ (CNAME, SSL) | ✓ (domains, reverse proxy) | Core |
| Template library | ✓ (100+) | ✓ (gallery) | ✓ | ✓ (400+) | Common |
| Form builder + lead capture & storage | ✓ (Leads tab per page) | ✓ (leads dashboard) | ✓ (Forms in depth) | ✓ (Leads, account-level) | Common |
| Conversion analytics (views/visitors/conversions) | ✓ | ✓ | ✓ (Analytics) | ✓ (Dashboard/EventTracker) | Common |
| Integrations to CRM/email/webhook | ✓ | ✓ | ✓ | ✓ | Common |
| Popups / sticky bars / lightboxes | ✓ | (popups in catalog) | ✓ | ✓ | Common |
| A/B testing | ✓ (separate product feature) | ✓ (plan-tiered) | ✓ (Optimize category) | ✓ | Common — but NOT definitional (see below) |
| AI page generation / AI copy | ✓ | ✓ | (era-current) | ✓ (Lunar) | Common (era-current) |
| Mobile/responsive handling | ✓ | ✓ (device previews) | ✓ (Mobile design builder) | ✓ | Common |
| Dynamic text replacement / ad-to-page personalization | ✓ | ✓ | ✓ (AdMap, Personalize) | ✓ (personalized pages) | Variant/optional |
| AI traffic routing (Smart Traffic class) | ✓ | ✓ | ✓ (AI experiments) | ✓ (Solis) | Variant/optional |
| On-page ecommerce checkout | — | ✓ | — | ✓ (Products, Orders, gateways) | Optional |
| Programmatic page generation at scale | — | — | — | ✓ | Optional (single-product in sample) |
| Agency subaccounts / client segmentation | ✓ (Clients) | ✓ (agency solutions) | (enterprise) | ✓ (Agency Hub) | Optional |
| Multi-language pages | — | — | — | ✓ | Optional |
| Full multi-page sites in same product | — | ✓ (Sites line) | ✓ (Websites category) | — | Packaging drift, not core |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **The standalone campaign page as the unit of record** — a persistent, individually managed single-purpose web page, built to receive traffic from a marketing campaign and drive one conversion goal (a call to action). It is not a fragment inside another system's pages, and not one page of a navigable multi-page site. Remove → generic web design tool or embedded-content territory.
2. **Visual no-code page construction** — the page is assembled by direct visual manipulation (drag-and-drop elements/sections, template starting points) by a marketer, with writing code not required as the primary building act. Remove → code-first web development / Web Development IDE territory.
3. **Publication to a live web address** — the built page becomes a functioning page reachable at a web address, via product-operated hosting or a provided publishing path, typically on the marketer's own domain or a product subdomain. Remove → unpublished design tool / prototype territory.

Binding purpose: the page exists to convert campaign traffic (lead capture, signup, purchase, click-through). Without the campaign-conversion purpose the artifact is just a web page — the purpose is what makes the Type marketing-side rather than design-side.

### L1 — Common Mature Structure

- template library of conversion-oriented page designs
- form builder + lead capture with stored lead records and notifications
- conversion analytics (views, visitors, conversions) per page
- integrations handing leads to CRM / email / webhook destinations
- popups, sticky bars, lightboxes as companion conversion surfaces
- custom domains + SSL; mobile preview / responsive handling
- A/B testing of page variants (present in all four sampled products, but as a plan-tiered or separately-positioned feature — see anti-overfitting)
- AI page generation / AI copywriting (era-current)

### L2 — Variant / Optional Structure

- dynamic text replacement / ad-to-page personalization
- AI traffic routing between variants (Smart Traffic class)
- on-page ecommerce checkout and order management
- programmatic page generation from data at scale
- agency subaccounts / client segmentation / audit logs
- multi-language pages, reusable synced sections
- heatmaps, visitor intelligence, SEO indexing posture
- full multi-page sites shipped inside the same product (packaging drift)

### L3 — Vendor-specific (Research Notes only)

- Unbounce: Clients sub-folders, Script Manager, IP filters, ubpages.com subdomains, MCP server, Smart Traffic
- Leadpages: Ad Studio, Optimization Score, Visitor Intelligence, brand-kit-grounded AI, HTML Pub
- Instapage: AdMap, Thor render engine, Fluid Grid Blocks, slideout, external popups on any website
- Landingi: Lunar, Solis, EventTracker, Smart Sections, Programmatic, Agency Hub, Orbit MCP

### Anti-overfitting Rule applied

- **A/B testing is NOT definitional.** All four sampled products carry it, but every one positions it as a separate feature/plan tier/category distinct from the builder, and the LPO pass documented a pure builder pole in the market (template-and-publish products with no testing machinery). The LPO pass's own removal test confirms: remove the variant/routing machinery → a Landing Page Builder survives. Testing belongs in L1 as common-mature, not in the defining core.
- **AI generation is NOT definitional** — era-current onboarding path; the pre-AI generation of these products (and the historical check below) satisfies the core without it.
- **Forms/lead storage are NOT definitional** — a click-through landing page (button to another destination) is still a landing page; the CTA is the invariant, the form is its most common realization.
- **Traffic metering / plan limits are commercial packaging**, not structure.

### Historical / Market-Sample Check (§24)

Would older or differently-positioned products still fit? Yes:

- Pre-SaaS practice: marketers hand-built ad destination pages (static HTML, WordPress page templates) — single campaign page + manual construction + publish to own hosting satisfies all three legs; visual no-code construction is satisfied by the page-template lineage (choose a layout, fill in content) even before drag-and-drop canvases.
- Early dedicated products (Unbounce 2009, Leadpages early 2010s) shipped template + editor + hosted publish with no AI, no smart traffic, minimal analytics — clearly the same Type.
- The minimal one-page pole (Carrd class) sits near the visual-website-builder seam; unreachable this pass, treated as an uncertainty rather than asserted.
- The check confirms the core must not require AI, built-in testing, traffic metering, or any specific editor implementation (free canvas vs sections vs grid are variant axes).

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Boundary Findings

### vs Visual Website Builder (§04.16 sibling — flag DISCHARGED this pass)

The prior pass's seam hypothesis is **CONFIRMED** on both proposed discriminators:

- **Unit of work**: the website builder's unit is the whole persistent web presence (pages, navigation, an address); the landing page builder's unit is the single campaign page. Leadpages states the contrast explicitly ("Unlike a website builder, which is designed for multi-page sites with navigation, a landing page builder is built around a single call to action"); Unbounce's docs define the landing page as standalone and not usually linked from the homepage.
- **Organizing machinery**: site assembly (pages/navigation/content structure) vs conversion machinery oriented to one CTA and its campaign.
- Supporting: Wix markets Website Builder and Landing Page Builder as separate product lines (per prior pass); Leadpages ships "Sites" as a separate line; Instapage keeps "Websites" as a separate help category; Squarespace documents landing pages as a use of its site builder (per prior pass).
- **Position**: keep-both. The market itself maintains the split; packaging drift (sites inside landing-page products, landing pages inside site builders) is real but does not collapse the centers of gravity.

### vs Landing Page Optimization Platform (§06 sibling — flag from that pass, addressed)

Same page object; the differentiator is the optimization loop as the organizing center. This pass is written **design-side** (page construction as the job), as that pass recommended. The LPO pass's removal test stands: remove the optimization machinery → Landing Page Builder; remove page building/hosting → A/B testing platform. Keep-both ratified from this side. Note the market straddles: all four sampled builder products embed some testing/analytics, and the LPO-side products embed building — the leaves are adjacent poles of one product family, distinguished by center of gravity, not by feature presence.

### vs Lead Capture Platform / Marketing Automation Platform

Leads are captured on the page and **handed off** (CRM/email/webhook integrations in all four products). Nurture, scoring, and lifecycle management happen elsewhere. The seam is the handoff. A lead-capture platform without page construction is a different Type.

### vs A/B Testing Platform

Consistent with the LPO pass: the A/B-testing core applies experiments to surfaces it does not build or host; the landing page builder owns the page. Testing inside a landing page builder is an embedded capability (L1), not the organizing object.

### vs No-code Application Builder / Web Application Builder

The landing page is content/presentation with a form or checkout; it carries no user-facing data+logic application state. Remove the application logic from a no-code app builder and you approach this Type; add it and you leave it.

### vs Online Store Builder

A landing page may take a single product order (Leadpages, Landingi evidence), but there is no store machinery of record (catalog, cart, order management as first-class persistent structures). On-page selling is an optional capability, not the Type.

### "去掉什么就变成另一个 Type" 判据

- Remove the single-page campaign scope (allow multi-page navigable sites) → Visual Website Builder.
- Remove visual no-code construction → code-first web development.
- Remove publication/hosting → design/prototype tool.
- Add the optimization loop as the organizing center → Landing Page Optimization Platform.
- Remove the page and keep the form machinery → Lead Capture Platform.

## Uncertainties

- Carrd (minimal one-page pole) unreachable — its exact position on the visual-website-builder/landing-page-builder seam remains unverified; recorded rather than asserted.
- Help-center article bodies for Leadpages were not reachable (product-page level only); Leadpages operational claims rest on its official product page.
- Exact plan-tier gating of testing features varies by product and changes over time; no precise tier/price claims are carried into the final document beyond what sampled pages state.
- The pre-SaaS historical lineage is inferred from the structure of the core (template + manual assembly + publish), not from archived documentation of specific early products.

## Final Synthesis

A Landing Page Builder is the marketer-side page-construction application whose defining core is exactly three jointly-held structures: the standalone campaign page as unit of record (a persistent single-purpose web page built to receive campaign traffic and drive one conversion goal; remove → generic web design tool) + visual no-code page construction (assembled by direct visual manipulation from templates/elements/sections, code not required as the primary act; remove → code-first web development) + publication to a live web address (product-operated hosting or a provided publishing path, custom domain or product subdomain; remove → unpublished design tool). The campaign-conversion purpose binds the three: the page exists to convert.

Everything else — templates, forms/lead storage, analytics, integrations, popups, A/B testing, AI generation, personalization, ecommerce, agency tooling — is common-mature or variant structure. The two pre-hung flags are discharged: keep-both vs Visual Website Builder (unit of work + organizing machinery) and keep-both vs Landing Page Optimization Platform (center of gravity: construction vs optimization loop), with this leaf written design-side.
