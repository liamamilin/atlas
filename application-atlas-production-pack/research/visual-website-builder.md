# Research Notes — Visual Website Builder

Research date: 2026-09-09

## Research Goal

Understand what a "Visual Website Builder" actually is as an Application Type: what the unit of work is, what the building act consists of, how the artifact becomes a live website, which capabilities are definitional vs common-mature vs variant, and where the exact seams lie against the neighboring Types — especially the three §04.16 siblings (Landing Page Builder, Interactive Web Design Application), the commerce sibling (Online Store Builder), the domain-specialized sibling (Church Website Builder), CMS, and the no-code/code development Types.

## Initial Boundary

- Working hypothesis: a Visual Website Builder lets a non-developer assemble a complete website through visual manipulation and publish it as a live hosted site, without writing code as the primary act.
- Nearest neighbors suspected: Landing Page Builder (§04.16 sibling, unprocessed), Interactive Web Design Application (§04.16 sibling, processed — joint review recommended), Online Store Builder (§05.01, processed — joint review flag), Church Website Builder (§25, processed — joint review flag), AI Design Generator (§04.20, processed — split recorded), Template-based Design Platform (§04.01, processed — drift watch flag), CMS (§02.07), No-code Application Builder (§12, processed), Web Development IDE (§12), UI Design Application / UX Prototyping (§04.15, processed), Blogging Platform (§02.07), Link-in-Bio Platform (§27, processed).
- Biggest taxonomy risk: the leaf could collapse into a pole of Interactive Web Design Application (same tool space, shared flagship products) or into Online Store Builder (Wix/Squarespace straddle).

## Research Questions

1. What is the unit of work — page, section, site? What is the persistent artifact?
2. What exactly is the "building" act (drag-and-drop? section insertion? style-panel editing)? Which parts are definitional vs implementation?
3. How does the artifact become live (publish loop, hosting, domain)? Is vendor-operated hosting definitional?
4. What does the editor look like (canvas, panels, device views)?
5. Which capabilities are common mature structure (templates, responsive, SEO, media, roles, marketplaces, AI) and which are variants (commerce, blog, code posture, white label)?
6. Where are the exact seams vs the six flagged neighbors?
7. Would older / regional / platform-native / desktop products still fit the definition (historical check)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence obtained |
|---|---|---|
| Wix | mass-market all-in-one hosted builder; free-canvas element editing; consumer/SMB | Tier 1 (help center topic tree + Getting Started with the Wix Editor article) |
| Squarespace | design-led template builder; premium consumer/creative | Tier 1 (help center category tree + "Add content to your site with blocks" article) |
| Webflow | professional visual site development; designer/agency pole; sits on the interactive-design seam | Tier 1 (Help Center "Intro to Webflow") |
| Duda | agency/reseller white-label builder; multi-site client management | Tier 1 (Support category tree + "Editor Overview") |

Rejected / unreachable samples:
- GoDaddy Website Builder (registrar-distribution guided SMB pole) — help center timed out twice; positioning-level only, no operational claims.
- Carrd (minimal one-page pole) — docs timed out twice; positioning-level only, no operational claims.

## Sources

- Wix Help Center root: https://support.wix.com/en/ (fetched 2026-09-09)
- Wix "Creating a website" topic: https://support.wix.com/en/creating-a-website (fetched 2026-09-09)
- Wix "Wix Editor basics" listing: https://support.wix.com/en/wix-editor-basics (fetched 2026-09-09)
- Wix "Getting Started with the Wix Editor": https://support.wix.com/en/article/wix-editor-getting-started-with-the-wix-editor (fetched 2026-09-09)
- Squarespace Help Center root: https://support.squarespace.com/hc/en-us (fetched 2026-09-09)
- Squarespace "Add content to your site with blocks": https://support.squarespace.com/hc/en-us/articles/206543757 (fetched 2026-09-09)
- Webflow Help Center "Intro to Webflow": https://university.webflow.com/lesson/intro-to-webflow (fetched 2026-09-09)
- Duda Support root: https://support.duda.co/hc/en-us (fetched 2026-09-09)
- Duda "Editor Overview": https://support.duda.co/hc/en-us/articles/26519221644439-Editor-Overview (fetched 2026-09-09)
- GoDaddy help: https://www.godaddy.com/help/website-builder-6782 and https://www.godaddy.com/help — timed out ×2 (abandoned)
- Carrd docs: https://carrd.co/docs and https://carrd.co/docs/overview — timed out ×2 (abandoned)

## Product Observations

### Wix (evidence layer A unless noted)

From the help center topic tree and the "Getting Started with the Wix Editor" article:

- Self-description (footer, every help page): "Wix is a website builder that lets any business or individual build their own professional website."
- "The Wix Editor is the platform you use to build and edit your website."
- Building act: "Adding and customizing elements" — an Add Elements panel with "hundreds of stunning, customizable elements… images, text, shapes, strips and more"; select an element → customization options appear.
- Design system: Site Design panel — site theme (colors and text styles used across the site), page background (color/image/video), page transitions.
- Mobile: a separate mobile editor; "adjust elements to ensure they are mobile-friendly… hide any elements that aren't necessary for mobile visitors"; mobile-only elements.
- Publish loop: Save / Preview / Publish buttons; "saved changes won't appear on your site until you click Publish"; "publish it to make it available on the internet"; Site History to "go back to a previous version"; Unpublish exists as a separate article.
- Live-site editing: "You can edit your site at any time from the Wix Editor, even after you have published it."
- Hosted-service shape: "The editor needs to be constantly connected to Wix's servers. Therefore it is not possible to edit your site while offline, or save pages from your site to your computer." Single-editor concurrency: "Avoid editing your site on more than one computer at a time."
- AI onboarding: "Wix offers an AI Website Builder that can automatically create a personalized website for you. By answering a few questions… the AI generates a custom design that you can further customize using the Wix Editor."
- Topic tree breadth: Editor basics / Editor tools / Your site's structure / Designing / Managing pages and menus / Adding and customizing elements / Files and media / Working with elements / Effects and animations / Sharing and promoting / Advanced elements / Building a mobile site; Managing your site (dashboard, roles & permissions); Managing media; Multilingual; Accessibility; Advanced features (CMS, Wix for Developers, Test Site); Wix Vibe; Wix Headless.
- Product-line split (footer nav): Website Builder, AI Website Builder, Website Templates, Web Hosting, Landing Page Builder, Online Store Builder, Wix Studio, Mobile App Builder — the vendor itself separates "website builder" from "landing page builder" and "online store builder" as product lines.
- Editor feature-request list (evidence of product boundaries): "Allowing Multiple People to Edit a Site at the Same Time" and "Storing a Backup of Your Site Outside of Wix" and "Responsive Sites" are *requests*, i.e. not generally available in the classic editor — single-editor-at-a-time and non-responsive classic canvas are real constraints of that editor generation.

### Squarespace (evidence layer A)

From the help center category tree and the "Add content to your site with blocks" article:

- Category tree: Getting started ("Everything you need to start and launch your site"), Pages and content ("build and edit your site with pages, sections, and blocks"), Templates and design ("customize fonts, colors, and other design features"), Domains ("registering, transferring, and connecting domains"), Commerce, Email Campaigns, Marketing, Analytics, Images and videos, Integrations and extensions, SEO and AI optimization, Privacy and security, Acuity Scheduling, Professional Email.
- Building act: "Blocks are drag-and-drop features that add content–like text, buttons, forms, and images–to your site. Think of them as the building blocks of your site."
- Flow: Pages panel → select page → Edit → hover section → Add Block → block menu (searchable) → block appears "with placeholder content" → click block → pencil icon to customize. Drag-and-drop placement with guidelines. Classic editor uses "+" icons instead.
- Block types (partial list from article): Archive, Audio, Button, Calendar, Chart, Code, Content link, Donation, Embed, Form, Flickr, plus text blocks, image blocks, product blocks, summary blocks, shape blocks.
- Structure constraints: blocks can be added to block sections, blog posts, event descriptions, footers, layout pages; NOT to auto layout sections, collection page sections, gallery sections, site headers (7.1) — the editor distinguishes block-editable areas from structured/collection areas.
- Fit/Fill for image/button blocks; transform effects (opacity, rotate, scale, offset, skew) in Fluid Engine.
- Version split: version 7.1 (Fluid Engine) vs version 7.0 (classic editor) — different editing models coexist in one product.
- App-based editing limitation: the Squarespace app "doesn't support adding or rearranging blocks on layout pages, only editing existing ones."
- Scale guidance: "no hard limit for the number of blocks… we recommend no more than 60 blocks per page" (product-specific guidance, kept out of the canonical document).
- Commerce as a sibling category (products, payment processor, discounts, taxes) — separate from site building.

### Webflow (evidence layer A)

From the Help Center "Intro to Webflow":

- "In Webflow, you can structure, build, and design your site across pages, branches, and locales… share your work, solicit feedback, and finally, publish your site to dedicated environments (i.e., staging and production)."
- Canvas: "The largest area in Webflow is the canvas… You can select elements, move them around, and edit content right on the page."
- WYSIWYG claim: "everything you do in Webflow directly affects the HTML and CSS of your site and reflects how your published site will look."
- Interface: top bar (Design/CMS/Insights tabs, context bar, site actions incl. Preview and Publish), canvas bar (undo/redo, breadcrumb element hierarchy, breakpoints), left toolbar (Add panel, Pages panel, Navigator, Components, Variables, Style selectors, Assets, Libraries, Apps, Site Activity log, Localize, Settings, Audit panel for accessibility/SEO, Quick find), right toolbar (Style panel — "adjust all CSS properties available for a selected element", Element settings, Interactions panel).
- CMS: "CMS tab — this tab opens the CMS panel, where you can create and manage Collections, Collection items, and Ecommerce products and categories."
- Roles: "site role (e.g., reviewer, content editor)".
- Responsive: breakpoints — "preview and edit how your site looks on different device sizes."
- Publish: "publish your site to push your site changes to a stage domain and/or your production domain."
- Code posture: main menu includes "Export code".
- Hosted-app rationale: "Webflow is an online/hosted app because we believe web design tools should let you design in the browser and immediately reflect the results… WYSIWYG."
- Collaboration: "Multiple teammates can collaborate on a site together… hand off design control… see where other people are working within your site in real-time."
- Insights: Analyze (site analytics) and Optimize ("run experiments on your site").

### Duda (evidence layer A)

From the Support category tree and "Editor Overview":

- Agency posture: dashboard tools are "Clients and Team", "White Label"; community is "dudaresellers"; row/column menus include "Lock for client editing"; "Account owners and staff members are able to create and save sections for customers to use, but customers cannot create and save their own sections."
- Editor interface: top navigation bar (pages dropdown, device icons/breakpoints, undo/redo, save indicator, site comments, share, preview changes, publish/republish), side panel (Add — "drag and drop Widgets, Media, and Site Text onto the canvas"; Pages; Layers; Theme — "default styles and settings for all text, colors, buttons, images, backgrounds, rows, columns, layout, width and spacing on your site"; CMS — "manage collections and content collected from clients"; SEO/AEO; More — Blog, Store, Bookings, Personalization, App Store, Settings), canvas, design panel.
- Site structure: "The Website Builder is built from a header, footer, rows, sections, and columns. Every widget you add is inserted into one of these sections."
- Rows/columns/inner rows; dragging a widget between rows creates a new row; column limits per device (product-specific detail, kept in notes).
- Designed Sections: "pre-built rows of elements which users can add… grouped into categories (Intro, Features, About, Team, Testimonials, and so on)"; "Save as Section" to reuse.
- AI: "Create a Flex Section with AI… the AI Assistant to generate content and design for flex sections" (plan-gated); separate "Duda Vibe" and "AI Tools" categories.
- Modules installable into the side panel: "after you install Blog, Bookings, or Store, they are added to your side panel."
- Publish: "Publish or Republish: use the publish or republish button to publish your site with the latest changes"; Preview Changes "including unpublished changes".
- Device handling: device icons switch breakpoints; "Hide On Device" per row/column; reverse column order for mobile.
- Snap to Align / Snap to Grid; entrance animations per row/column.
- Store as two categories: "Native Store" and "Third Party Store" — commerce is a module, not the organizing center.
- CMS: "Dynamic Pages and Collections" category; Personalization Rules; Custom Code; Popups.

## Cross-product Comparison

| Aspect | Wix | Squarespace | Webflow | Duda | Reading |
|---|---|---|---|---|---|
| Unit of work | site (pages + elements) | site (pages + sections + blocks) | site (pages, branches, locales) | site (pages + rows/columns + widgets) | the site is the persistent artifact in all four |
| Building act | add/customize elements on canvas | drag-and-drop blocks into sections | select/move elements; style panel | drag-and-drop widgets into rows/columns | visual direct manipulation; drag-drop is one implementation |
| Starting point | template or AI-generated site | template | template or blank | template / Designed Sections / AI | templates common, not universal (blank pole exists) |
| Design system | Site Design panel (theme, background, transitions) | site styles (fonts, colors) | style panel + classes/variables | Theme panel (site-wide defaults) | site-wide style layer common |
| Mobile/responsive | separate mobile editor | structure-driven; version split | breakpoint editing | device views + hide-on-device | a device-handling surface is common; its form varies |
| Publish | Save/Preview/Publish; unpublish; Site History | launch + connect domain | publish to staging/production domains | publish/republish; preview changes | publish loop + product-operated hosting in all four |
| Domain | purchase/connect/transfer | register/connect/transfer | connect domain + site plan | Publishing and Domains category | domain connection common |
| Content structure | CMS (advanced feature) | collections (implied by category tree) | CMS Collections + items | CMS collections + dynamic pages | CMS common as module/advanced layer |
| Commerce | separate Online Store Builder product line | Commerce category | Ecommerce in CMS panel | Native Store + Third Party Store (installable) | commerce is a module/product line, not the center |
| Extensions | App Market | integrations/extensions | Apps panel + Libraries | App Store + Zapier + Connectors | marketplace common |
| Roles | roles & permissions | site contributors | site roles (reviewer, content editor) | clients & team, lock for client editing, white label | multi-actor surfaces common; depth varies |
| AI | AI Website Builder (Q&A → site) | SEO and AI optimization category | AI learning assistant | AI Assistant (sections), Duda Vibe | AI as onboarding/assist layer, era-current |
| Analytics | business analytics | Analytics category | Insights (Analyze/Optimize) | Site Performance | analytics common add-on |

Layer B (cross-product commonality, all four sampled products): site as persistent re-editable artifact; visual editor with canvas + element/block/widget palette; site-wide design/theme layer; device-handling surface; save→preview→publish loop with the product operating the live site; domain connection; media management; SEO surface; roles/contributors; optional modules (commerce, blog, forms, bookings); extension marketplace; AI assist/generation.

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **The site as a persistent visually-assembled artifact** — a complete website (one or more pages composed of arranged sections/elements carrying content) built and continuously re-edited by direct visual manipulation in a purpose-built editor, with writing code not required as the primary building act. Remove → code-first web development (Web Development IDE / framework) territory.
2. **The whole website as the unit of work** — the artifact is a whole web presence (a site), not a single campaign page and not a fragment embedded in pages owned by other systems. Remove → Landing Page Builder (single conversion page) or interactive-content/embed territory.
3. **The published live website as the deliverable** — the assembled artifact becomes a functioning website reachable at a web address; the product provides the path to publication (operating the hosting itself, or providing publishing machinery to hosting). Remove → design tool / prototyping territory (unpublished artifact).

Jointly-held load-bearing analysis:

- 1 alone = visual design tool (design artifact, no site semantics)
- 2 without 1 = code-first site development
- 3 without 1+2 = hosting service
- 1+2 without 3 = unpublished site design / prototype
- 1+3 without 2 = single-page or fragment builder
- 2+3 without 1 = code-based site + hosting platform

### Level 1 — Common Mature Structure

Present across the sampled population (Layer B), expected in the market, not definitional:

- template/theme library as the standard starting point (blank start exists at the professional pole)
- element/block/widget palette with drag-and-drop placement and placeholder content
- page management (add/duplicate/reorder pages, navigation menus, headers/footers)
- site-wide design system (theme: colors, fonts, buttons, spacing defaults)
- media/asset library
- device-handling surface (separate mobile editor, breakpoint editing, or device views)
- save → preview → publish loop with version history/rollback and unpublish
- custom domain connection (purchase/connect/transfer)
- SEO settings surface
- contact forms
- roles/contributors with permission tiers
- extension/app marketplace
- AI generation/assistance as an onboarding or in-editor layer (era-current)

### Level 2 — Variant / Optional Structure

- editing model: free-canvas absolute positioning ↔ section/block structured ↔ flex/grid professional (variant axis; Wix classic vs Squarespace Fluid Engine vs Duda flex vs Webflow style-panel)
- audience/posture: consumer-personal, SMB business, designer/agency professional, agency white-label multi-site management (Duda pole)
- commerce depth: none → buy buttons → native store module → full store admin (module, not center)
- content depth: static pages → blog → CMS collections/dynamic pages
- code posture: none → embeds/custom-code blocks → dev platform/scripting → code export
- hosting posture: hosted service (dominant) vs publish-to-host machinery (desktop/export lineage)
- AI posture: none → section-level AI → full prompt-to-site generation
- scope: one-page minimal sites ↔ multi-page sites ↔ multi-site/agency management
- domain-specialized siblings (church builders etc.): same substrate + domain-shaped content objects

### Level 3 — Vendor-specific Structure

- Wix: classic Editor vs Harmony Editor generations; Velo dev platform; Wix Vibe; Wix Headless; Wix Studio; App Market; single-editor concurrency constraint; editor requires constant connection to Wix servers
- Squarespace: version 7.0 vs 7.1 split; Fluid Engine; classic editor "+" flow; 60-blocks-per-page guidance; Acuity/Email Campaigns bundling
- Webflow: branches and locales; staging vs production publish targets; Style panel exposing CSS properties; code export; Optimize experiments; Site Activity log (Enterprise)
- Duda: white label; lock-for-client-editing; Designed Sections library; personalization rules; native vs third-party store duality; client-content collection ("content collected from clients")

## Vendor-specific Findings

- Wix's classic editor is non-responsive by construction (responsive sites exist as a feature *request*); its mobile story is a separate mobile editor. This is an implementation generation, not a Type property — Webflow/Duda handle devices via breakpoints/device views.
- Squarespace's block system has explicit non-block areas (auto layouts, collection pages, gallery sections) — structured content areas resist free block placement. Product-specific structural rule.
- Webflow self-describes its artifact in code terms ("directly affects the HTML and CSS") and offers code export — the professional pole leans closest to development while remaining visually driven.
- Duda's editor carries agency machinery inside the building surface (lock for client editing, client-scoped sections, white label) — the multi-client posture realized as editor features.
- Wix's own product-line nav separates Website Builder / Landing Page Builder / Online Store Builder / Mobile App Builder — vendor-side confirmation that the market treats these as distinct products despite shared machinery.

## Boundary Findings

1. **vs Interactive Web Design Application (§04.16, processed) — JOINT REVIEW DISCHARGED.** The interactive pass ratified the discriminator: center of gravity (site-assembly-first with interactions as one feature vs behavior-first design on a freeform canvas). From this side's sample: every builder's documented front door is site assembly (templates/sections/pages/content → publish); interactions/animations appear as capabilities (Wix "effects and animations" category, Duda entrance animations, Squarespace transform effects, Webflow Interactions panel) — present, but never the organizing center; no sampled builder documents behavior authoring as the design act. Webflow sits on the seam (its own docs lead with canvas + style + publish; interactions are one right-toolbar panel). **Verdict: keep-both RATIFIED from this side** — the two Types share a tool space and flagship products, and the center-of-gravity seam holds.
2. **vs Landing Page Builder (§04.16, unprocessed) — seam hypothesis recorded, flag for that pass.** Working seam: the unit of work (whole persistent web presence vs single conversion page) + the organizing machinery (site assembly vs conversion machinery — forms/A-B/lead capture as the structure). Supporting observation: Wix markets "Website Builder" and "Landing Page Builder" as separate product lines; Squarespace's own help center documents "Creating a landing page" as a *use of* the site builder, not a separate product. Carrd (one-page pole) sits near this seam; unreachable this pass, so no claim is made about it. Final ratification belongs to the landing-page-builder pass.
3. **vs Online Store Builder (§05.01, processed) — JOINT REVIEW DISCHARGED.** The store pass's seam: the buying-and-ordering machinery of record (catalog → cart → checkout → orders operated by the product) + dedicated store-admin surfaces mark the store-first organizing purpose. From this side: commerce appears in the builder population as installable/sellable modules (Duda installs Store into the side panel; Wix sells Online Store Builder as a separate product line; Squarespace Commerce is a separate help category; Webflow keeps Ecommerce inside the CMS panel) — the site-building core stands without it, and the store pass itself documented Wix/Squarespace as straddle-by-marketing but store-first in structure. **Verdict: keep-both RATIFIED from this side** on the machinery-of-record seam.
4. **vs Church Website Builder (§25, processed) — JOINT REVIEW DISCHARGED.** The church pass's distinguishing structure: church-shaped content objects as first-class building blocks + church-operations integration (giving/ChMS/app) + non-technical church-operator framing. From this side: the generic substrate documented here (hosted site, templates, visual editing, domain, SEO, publish) contains no church-shaped objects in any sampled product; the church pass itself documented that removing the church-shaped objects yields a generic Visual Website Builder. **Verdict: keep-both RATIFIED from this side** — audience/domain-specialized sibling; a church using a generic builder performs the same job without the Type's product shape.
5. **vs AI Design Generator (§04.20, processed) — split RATIFIED from this side.** Deliverable container differs: design artifact vs functioning website with structure/content/hosting. Observed from this side: AI site generation lands *inside* builders as an onboarding path (Wix AI Website Builder generates a site "you can further customize using the Wix Editor"; Duda AI Assistant generates flex sections) — the generated result is a functioning editable site, not a design artifact. Clean split holds.
6. **vs Template-based Design Platform (§04.01, processed) — drift watch DISCHARGED.** Seam = design artifact vs hosted functioning website. Template platforms' web publishing produces design-artifact pages; builders produce the functioning site with structure/content/hosting. Keep-both; the drift watch is closed with the seam confirmed from this side.
7. **vs CMS (§02.07)** — center-of-gravity seam: assembly-first (the user composes the site's structure and appearance directly; content lives in the composed pages) vs content-first (the site is a container for ongoing content production through a content model; presentation comes from themes). Convergence is real and documented from both sides: builders ship CMS as an advanced/module layer (Wix CMS under Advanced features; Duda CMS collections; Webflow CMS tab), and the headless-CMS pass recorded the reverse drift boundary (block/page composition becoming the primary surface + platform owning rendering/hosting → Visual Website Builder territory). Complementary seam; keep-both.
8. **vs No-code Application Builder (§12, processed)** — ratified from this side on the no-code pass's own seam: builders center a published content/presentation site for web audiences; no-code builders center a data+logic application with user accounts and record-level permissions. Remove data+logic+users → website builder.
9. **vs Web Development IDE / Web Application Builder (§12)** — code-first vs visual no-code building act. Webflow's code export and CSS-level style panel mark the near edge; the building act remains visual manipulation.
10. **vs UI Design Application / UX Prototyping (§04.15, processed)** — design-artifact posture: the UI design is an inert specification implemented elsewhere; the builder's artifact is the working site (consistent with the ui-design pass's removal test).
11. **vs Blogging Platform (§02.07)** — content-stream-first vs site-assembly-first; blog appears in builders as an installable module (Duda) or product line (Wix), not the center.
12. **vs Link-in-Bio Platform (§27, processed)** — minimal single-purpose profile page vs whole web presence; the link-in-bio pass expected this seam; held here as adjacent.

## Historical / Market-Sample Check

- **Hosted page-builder ancestry (GeoCities/Tripod era)**: template + visual assembly + hosted publish, no code — satisfies all three legs. Fits.
- **Desktop WYSIWYG site builders (FrontPage-era; Mac desktop site builders)**: visual assembly of complete sites with publish-to-host machinery (FTP) instead of vendor-operated hosting — satisfies leg 3 via the publishing-path reading. This is why **vendor-operated hosting is NOT in the defining core**; "the product provides the path to publication" is.
- **Flash-era site builders (mid-2000s)**: visual canvas + hosted publish — fits.
- **WordPress + page-builder plugins**: visual assembly inside a CMS — straddles the CMS seam; center-of-gravity question; recorded as boundary, not evidence against the definition.
- **Church/association builders**: domain-specialized variants satisfying the same substrate — fits as variants/siblings.
- Conclusion: the three-leg definition survives the historical check; the dominant hosted-service shape is an implementation, not the invariant.

## Uncertainties

- GoDaddy Website Builder and Carrd could not be fetched (timeouts ×2 each). Their inclusion would have strengthened the guided-SMB and minimal-one-page poles. No operational claims about either product are made in this pass; Carrd's position relative to the Landing Page Builder seam is left to that pass.
- The exact seam vs Landing Page Builder remains a hypothesis until that leaf is processed (its earlier run failed); the flag is recorded for joint review.
- WordPress.com's current builder posture (marketing "website builder" language over a CMS core) was not fetched this pass; the CMS seam is held on center-of-gravity reasoning plus the headless-CMS pass's recorded drift boundary, not on a fresh WordPress sample.
- Whether any mainstream builder ships without any publish machinery (pure file export) was not verified; the publishing-path reading of leg 3 is chosen to be robust to that case.

## Final Synthesis

A Visual Website Builder is a no-code site-creation application whose defining core is exactly three jointly-held structures: the site as a persistent visually-assembled artifact (complete website — one or more pages of arranged sections/elements carrying content — built and re-edited by direct visual manipulation without code as the primary act), the whole website as the unit of work (a whole web presence, not a single campaign page or embedded fragment), and the published live website as the deliverable (the artifact becomes a functioning website at a web address, via product-operated hosting or a provided publishing path). Templates, drag-and-drop as a specific gesture, responsive machinery, AI generation, commerce, blogging, CMS, marketplaces, roles, and analytics are common mature structure or variants, not definitions. The Type shares a tool space with Interactive Web Design Application (center-of-gravity seam, ratified keep-both), borders Landing Page Builder (unit-of-work + conversion-machinery seam, hypothesis flagged), Online Store Builder (machinery-of-record seam, ratified keep-both), Church Website Builder (domain-specialized sibling, ratified keep-both), CMS (assembly-first vs content-first), and the no-code/code development Types (website vs application; visual vs code-first). Historical check passes against hosted page-builder ancestry, desktop publish-to-host builders, and Flash-era builders.
