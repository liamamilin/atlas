# Research Notes — Interactive Web Design Application

## Research Goal

Determine whether "Interactive Web Design Application" (DIRECTORY §04.16 Web Experience Design, third leaf alongside Visual Website Builder and Landing Page Builder) corresponds to a real, distinct Application Type in the current market; if yes, extract its defining core, standard structure, variants, and boundaries against neighboring Types.

## Initial Boundary

Working hypothesis before research:

- A designer-facing visual application for designing *interactive, motion-rich web experiences* — where behavior (animation, scroll response, hover/click states, transitions) is a first-class design material, composed on a visual canvas and published as a live web artifact.
- Nearest neighbors suspected: Visual Website Builder (§04.16 sibling), Landing Page Builder (§04.16 sibling), UX Prototyping Application / Interactive Prototype Builder (§04.15), Motion Graphics Application (§04.07), Graphic Design Application (§04.01), CMS (§02.07), 3D Modeling Application (§04.13), Web Development IDE / No-code Application Builder (§12).
- Biggest taxonomy risk: the leaf could be merely a *pole of Visual Website Builder* rather than a distinct Type.

## Research Questions

1. What is the authoring surface and object model? (canvas, pages/frames/scenes, elements/layers)
2. How is interactivity authored — what triggers exist, what responses are composed, and is this a core surface or an add-on?
3. What is the output model — is the artifact a live public web thing? Hosted site, embed, or both?
4. How is responsiveness handled, and is it definitional or common?
5. Who is the primary user, and what do they actually build?
6. How does content (CMS) relate to design?
7. Where are the exact seams vs Visual Website Builder, Landing Page Builder, UX Prototyping, Motion Graphics, CMS, 3D creation?
8. Historical check: would Flash-era interactive web design tools satisfy the definition?
9. Taxonomy verdict: distinct Type, variant, or alias?

## Representative Products

Selected for market representativeness, documentation access, differing product philosophy, and differing customer tiers:

| Product | Philosophy / pole | Tier |
|---|---|---|
| Framer | designer-first interactive *website* design, full hosted sites | freelancer → startup → agency |
| Webflow | professional visual web *development* with deep interactions (GSAP) | professional/agency → enterprise |
| Ceros | experiential *interactive content* embedded into existing corporate architecture | enterprise brand/marketing teams |
| Vev | visual editor for *interactive content* (microsites, reports, editorial) with publish-into-CMS | enterprise teams, publishers, agencies |
| Spline | 3D-first *interactive experiences* shipped to the web as embeds | brand designers, creative studios |

Secondary / boundary samples:

- Readymag — designer-craft web design tool ("the design tool for outstanding websites"); deep docs unreachable (JS-rendered), used with reduced evidence strength.
- Wix Studio — agency pole of a site builder; features page timed out, abandoned per retry discipline; not used in any claim.

## Sources

All fetched 2026-09-07:

- Framer — https://www.framer.com/features/ , https://www.framer.com/design/ (official product pages)
- Webflow — https://webflow.com/features , https://webflow.com/interactions-animations (official feature pages)
- Ceros — https://www.ceros.com/ , https://www.ceros.com/comparisons/framer-vs-ceros/ (official product + vendor comparison page)
- Vev — https://www.vev.design/ (official product page)
- Spline — https://spline.design/ (official product page)
- Readymag — https://readymag.com/ (title only), https://help.readymag.com/hc/en-us (Zendesk shell only)

Access limitations:

- Readymag: marketing and help pages are JS-rendered shells; only the site title and help-center shell were retrievable. All Readymag-specific claims are kept minimal; no Readymag observation supports any cross-product claim.
- Wix Studio: request timeout; abandoned after one retry attempt per source discipline. No claims based on it.
- Deep help-center articles (Framer help articles, Webflow University lessons, Ceros/Vev educate portals) were not individually fetched; evidence rests on official product/feature pages, which are Tier 1/Tier 2 official sources. Numeric limits, plan details, and default values were not researched and are not asserted anywhere.

## Product Observations

Evidence layer per observation: **A** = directly observed on that product's official pages; **B** = cross-product commonality (stated only in the comparison section).

### Framer

- A: Positioning: "Design websites with AI, then refine every detail… Design responsive websites on Framer's visual canvas… and publish without code." A freeform canvas on which sites (also icons, social assets) are composed; "every change the agent makes is fully editable. Move it, restyle it, tweak it by hand."
- A: Interactions named as a top-level design capability: "Clicks, hovers, and taps that make your site respond." Animations: "best-in-class web animations that are easy to set up and performant out of the box." Dictionary entries list Scroll effects, 3D transforms, SVG animations, sticky positioning, custom cursors, overlays, blend modes, masks, tickers, flow effect.
- A: Layout: "flexible layouts… auto-layout stacks and fully customizable grids"; responsive adaptation across breakpoints (agent prompt "Make this responsive for tablet and phone").
- A: Reusable interactive components: "Add variants, interactions, and properties so every instance works exactly as intended"; smart components.
- A: Publishing and platform: "Publish — go from design to live site in seconds"; hosting, performance, SEO, CMS ("structure content and publish dynamic pages"), localization, analytics, A/B testing, collaboration with branches, desktop app, plugins, community marketplace of templates/components.
- A: Market neighborhood from its own comparison list: Webflow, Figma, Wix, Squarespace, WordPress, Readymag, Ceros, Unbounce — i.e., the product positions itself simultaneously against site builders (Wix/Squarespace), design/prototyping tools (Figma), interactive content platforms (Ceros), and landing page tools (Unbounce).
- A: 2026 positioning is AI-agent-first ("AI design agent"; agents on canvas; external agents via Claude Code/Cursor/Codex); interaction/canvas/publish capabilities remain the product substance on /design/.
- A: Audience surfaces: designers, agencies, marketers, site teams, founders; use cases: portfolios, startup sites, landing pages, company blogs.

### Webflow

- A: Positioning: "Web design, CMS, & hosting"; "Webflow translates every design choice you make into clean, standards-compliant code. So you're not just designing or prototyping your website — you're building it." Interactions nav item: "Craft immersive experiences."
- A: Interactions capability (dedicated feature page): "Design unique, expressive interactions visually — with the full power of GSAP." Workflow described as Select → Animate → Perfect → Reuse: "Target any element and define how it responds with flexible triggers like scroll, hover, and click"; "a wide array of features, including GSAP favorites like SplitText, Staggers, and ScrollTrigger"; "fine-tune every detail on a horizontal timeline where you can scroll, scrub, zoom, and pan"; "reusing custom presets anywhere across your site."
- A: Interaction authoring details: choose precisely what to animate by targeting ids, classes, custom attributes, and custom query selectors; custom actions with control over duration, ease, and CSS property changes; trigger actions with custom events using custom code; tailor interactions to breakpoints; adapt designs for reduced motion (accessibility); preview animations on a visual timeline without publishing first (customer quote).
- A: Definition provided by vendor FAQ: "Website interactions are actions that occur in response to user behaviors like click, hover, or scroll."
- A: Design surface: visual CSS grid/flexbox, classes, Symbols→Components, variable fonts, responsive by default, custom code embeds, clean HTML/CSS export (plan-gated).
- A: Platform: CMS collections with template pages, hosting/CDN, backups/versioning, staging on webflow.io, localization, security, Analyze/Optimize (analytics + A/B/personalization), apps, Figma-to-Webflow import.
- A: Ecosystem integration for motion: import Lottie (After Effects), embed Spline 3D scenes, Rive animations; extend with GSAP code.
- A: FAQ examples of what can be built: hover effects revealing hidden content, click-triggered dropdowns, parallax scrolling sections, animated page transitions, staggered animations, mouse-movement tracking.

### Ceros

- A: Positioning: "Ceros: Interactive Content Creation Platform for Teams"; flagship product Flex = "An unrivaled design studio with limitless creative control." "Ship stunning interactive content faster, always on brand, and with built-in analytics."
- A: Category self-definition from its own FAQ list: "What is an interactive content platform?", "How is Ceros different from a website builder or CMS?", "Is Ceros a content creation platform or a design tool?" — the vendor explicitly claims a category distinct from website builders.
- A: Comparison page vs Framer (vendor-authored): "Framer excels at building and hosting websites. Ceros is purpose-built for interactive content that embeds into any existing architecture — landing pages, reports, sales demos, and thought leadership — without touching your web infrastructure." And: "Framer, by contrast, hosts the site itself and isn't designed to drop interactive content components into an existing architecture."
- A: Interactivity claim: "No-code animation + interactivity — designers get absolute freeform layout control to create heavy-duty animations, interactive data visualizations, and branching content journeys without touch-typing code or setting up intricate responsive break-point conditions." Capability table: "Built-in interactivity engine — states, triggers, sequences, and microinteractions directly on the canvas."
- A: Publishing model: "Universal CMS embedding — Ceros experiences deploy seamlessly as interactive embeds inside your existing enterprise stack, keeping your current CMS, analytics, and infrastructure completely intact."
- A: Analytics: "Granular behavioral analytics — tracks clicks, dwell time, and engagement at the page and object level — then pushes that data to… Google Analytics, Adobe Analytics, HubSpot, and more."
- A: Enterprise readiness: SOC 2, ISO 27001, GDPR, SSO, audit logs; brand kit enforcement; role-based permissions and approval workflows.
- A: Named output types: landing pages, interactive reports, RFPs, demos, sales collateral, thought leadership, ebooks, infographics, interactive maps, interactive touchscreens, gated content, event sites.

### Vev

- A: Positioning: "Vev | No-code tool for interactive content"; "Vev is the AI-powered visual editor for enterprise teams. Build and publish interactive content that drives real engagement, not just impressions."
- A: Roles split: "Vev lets designers build without limits, use AI where it speeds up, and allows editors to update copy and publish it straight into the existing CMS." Features grouped: For designers (AI, Design & layout, Interactions); For marketers (SEO & accessibility, Collaboration); For developers (Integrations, Developer tools, Hosting).
- A: Canvas: "Design pixel-perfect, publish-ready content on a free-roaming canvas with real-time collaboration built in."
- A: Interactions: UI screenshot alt text shows an Interactions panel with event triggers "Animate, On click, On timer"; visible parallax settings UI ("scroll parallax settings: speed 100px slider, linear easing dropdown"); named effects: scrollytelling, mouse-move parallax, horizontal scroll, video scroll, load animations.
- A: Publishing: "Publish into any CMS — embed or publish via webhooks to any CMS — keeping your analytics and integrations intact."
- A: Reuse: "Build a library once, then let any team assemble, tweak, and launch from it independently"; brand-aware AI generating fully-editable on-brand layouts.
- A: Named use cases: interactive presentations, annual reports, sponsored content, microsites, quizzes, sports marketing, science communication, campaign landing pages; solutions for publishers, marketing, agencies.

### Spline

- A: Positioning: "Spline - 3D Design tool in the browser with real-time collaboration"; "A complete platform for real-time interactive design"; "Make anything 3D."
- A: Two relevant product lines: 3D Design ("a web-based, collaborative 3D design tool for production-ready, real-time interactive experiences") and Hana ("a canvas for interactive design… interactive interfaces and motion… Design interactive and animated experiences with states, events and transition actions").
- A: Interactivity & motion: "Add interactivity and animation with Spline's powerful event system": States & Events, Timeline Animation, Game controls, Physics & Particles; "Variables & Data — bring real-time data into your experiences with Variables, Webhooks, APIs and AI."
- A: Delivery: "Ship real-time experiences to the Web, iOS and Android"; embed code shown (`<spline-viewer>` web component with scene URL) with documented integration targets: Webflow, Framer, Wix Studio, HTML/JS, React, Next.js, Swift, Kotlin.
- A: Template/community categories include "Interactive Websites", "Gamified Experiences", "Brand & Marketing"; community remix platform, library, academy, docs.
- A: Audience quotes: brand designers at software companies; "designers can focus on crafting assets, and engineers don't have to rebuild them from scratch"; junior designers integrating 3D experiences into Webflow projects.

### Readymag (limited evidence)

- A (minimal): Site title: "Readymag – the design tool for outstanding websites." Help center exists (Zendesk shell) with links to Forum, Learn, Blog.
- Limitation: deeper pages JS-rendered and not retrievable; product-specific detail is deliberately not asserted. Included only as evidence that a designer-craft pole of this product family exists and is a recognized comparison target of Framer.

## Cross-product Comparison

| Dimension | Framer | Webflow | Ceros | Vev | Spline |
|---|---|---|---|---|---|
| Primary artifact | full hosted website | full hosted website (+ code export) | interactive experiences embedded into existing site/CMS | interactive content; embed or publish via webhooks into any CMS | interactive scenes embedded into sites/apps |
| Authoring surface | freeform visual canvas | visual Designer (CSS-grade) | freeform design studio (Flex) | free-roaming canvas, pixel-perfect | 3D scene editor / canvas (Hana) |
| Interactivity authoring | clicks/hovers/taps → responses; scroll effects; component variants with interactions | triggers (scroll/hover/click/page load) → animation sequences on timeline; GSAP; presets; per-breakpoint | states, triggers, sequences, microinteractions on canvas; no code | interactions panel: Animate / On click / On timer; scroll parallax, scrollytelling, mouse parallax | event system: states & events, timeline animation, physics, game controls, variables |
| Timeline/presets | animations "easy to set up"; variants | horizontal timeline, scrub/zoom/pan, presets | sequences on canvas | parallax/scrollytelling effect settings | timeline animation |
| Responsiveness | breakpoints, stacks, responsive agent adaptation | responsive by default; interactions tailored per breakpoint | vendor-claims no breakpoint conditions needed (marketing claim — treat as variant posture) | pixel-perfect; scoping not deeply documented | platform scaling; per-platform delivery |
| Content layer | CMS | CMS collections | embed library; CMS integration positioning | publish into any CMS (webhooks/embeds); libraries | variables, webhooks, APIs |
| Publishing | built-in hosting, publish in seconds | built-in hosting; code export | embed into existing architecture | embed or webhooks into any CMS | embed via web component; runtimes for iOS/Android |
| Preview | agent/canvas editing | preview timeline without publishing | — (not observed) | live collaboration; publish flow | press-and-drag interactive demo on site |
| Users | designers, agencies, startups, site teams | designers/agencies/enterprise marketing | enterprise brand/marketing teams | designers + marketers + editors, publishers, agencies | brand designers, creative studios |
| Governance | branches, collaboration | roles, backups, staging | brand kits, roles/approvals, SOC 2/ISO/SSO | brand-aware AI + libraries; enterprise tier | community/enterprise tiers |
| Analytics | built-in analytics, A/B testing | Analyze + Optimize | page- and object-level engagement analytics | engagement positioning; integrations intact | not observed |

### B-layer commonalities observed across the sample

- Visual canvas authoring by the designer (all five).
- Behavior as an authored, first-class design layer with named triggers (click/hover/scroll/load/time) driving animated or state responses (all five, in different shapes).
- The output is a live web artifact: a hosted site (Framer, Webflow) or an embeddable interactive web experience (Ceros, Vev, Spline — and hosting exists on the site-pole too).
- Reusable design elements with behavior attached (components/variants/presets/libraries — all five in some form).
- Preview/iterate loop close to the canvas (observed in four; not observed for Ceros in fetched material).
- Motion/effects vocabulary around scroll (scroll effects, parallax, scrollytelling, ScrollTrigger) — four of five (not observed for Ceros in fetched material; its sequences/microinteractions serve the same role).
- AI assistance inside the canvas (current-market common; Framer agents, Vev brand-aware AI, Ceros Flex AI, Webflow AI, Spline agentic editing).
- Two delivery poles: the *full site* pole (Framer, Webflow) and the *interactive content/experience embedded elsewhere* pole (Ceros, Vev, Spline). Both poles publish live web artifacts; they differ in what the artifact is.

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product is no longer this Type. Three structures, held jointly:

1. **The visual canvas composing the web experience.** A designer-directed visual authoring surface on which the pages/screens of a web experience are composed from directly manipulated elements (text, image, shape, media, 3D objects). Remove → code-first web development IDE, or a template/section form-filler.
2. **Behavior authored as first-class design material.** The designer visually composes the *responses* of the experience — trigger → response pairs (click / hover / scroll / load / time → animated transitions, state changes, sequences) — as part of the design itself, not as a developer hand-off or a plugin. Remove → static design tool / visual website builder / graphic design application.
3. **The live web artifact as output.** The designed thing is published as a functioning web experience — a hosted site or an interactive experience embedded in a web page — reachable by an end user in a browser. The design IS the deliverable; there is no prototype-to-development hand-off stage. Remove → UX prototyping application (artifact is a mockup/prototype), or a motion graphics tool (artifact is a rendered video).

The conjunction is load-bearing: 1+2 without 3 = prototyping/design tooling; 1+3 without 2 = static visual website builder; 2+3 without 1 = code/framework territory, not a designer-facing application.

### L1 — Common Mature Structure

Present in most mature modern products; not definitional:

- responsive layout systems (breakpoints, stacks/grids, per-breakpoint interaction scoping)
- CMS or content bindings letting non-designers update content separately from design
- reusable components/presets/libraries carrying behavior (variants, states)
- animation timeline with easing/duration control and preview before publish
- scroll-driven effects vocabulary (scroll effects, parallax, scrollytelling)
- media/effects layer: masks, blends, 3D transforms, custom cursors, video
- hosting/domains (site pole) or embed-delivery machinery (content pole)
- custom-code escape hatch (code embeds, custom events, code export)
- collaboration (real-time co-editing, branches, roles/approvals at enterprise tier)
- analytics (page-level everywhere in the sample; object-level in one product)
- SEO/performance tooling (site pole; accessibility claims in both poles)

### L2 — Variant / Optional Structure

- artifact scope: full multi-page sites ↔ self-contained interactive content/experiences ↔ 3D scene embeds
- audience pole: designer-craft (portfolios, expressive brand sites) vs marketing/brand teams (campaign content, reports, RFPs) vs agencies serving clients
- governance posture: enterprise compliance (SOC 2/ISO/SSO claims), brand kits, approval workflows — one product leads here
- code posture: strictly no-code claims vs code-hybrid (custom code, GSAP code, HTML/CSS export)
- AI posture: agent-on-canvas editing, brand-aware generation, external-agent connectivity (all current-market, fast-moving)
- 3D/WebGL/physics/game-control depth
- platform destinations beyond the browser (iOS/Android runtimes — one product)

### L3 — Vendor-specific (kept out of the final document)

- Framer: agents/external agents (Claude Code, Cursor, Codex), CMS agent, branches workflow, dictionary-branded effects
- Webflow: GSAP-powered interaction engine (SplitText/Staggers/ScrollTrigger), Editor mode, DevLink, webflow.io staging, Lottie/Spline/Rive import paths
- Ceros: Flex AI four modes (Inspire/Plan/Build/Review), object-level analytics claims, MarkUp companion
- Vev: webhook publishing into arbitrary CMSs, Page AI beta
- Spline: `spline-viewer` web component, physics & particles, game controls, Spline Mirror

## Rejected Findings

- "Responsive breakpoints are defining" — rejected: Flash-era tools had no responsive layer; one product even markets freedom from breakpoint conditions. Common, not invariant.
- "A built-in CMS is defining" — rejected: the embedded-content pole reaches live web delivery without the platform hosting or owning content structure.
- "Full websites are the artifact" — rejected: half the sample ships interactive experiences embedded into pages owned by other systems.
- "Interactions require a timeline UI" — rejected: state/event panels and sequence editors satisfy the same role; the timeline is an implementation shape.
- "No-code (zero code ever) is defining" — rejected: code-hybrid escape hatches are common; pure no-code is a marketing posture. The invariant is *visually authored behavior*, not *absence of code*.
- "AI assistance is part of the Type" — rejected: current-market commonality only.

## Historical / Market-Sample Check

Flash-era interactive web design (late 1990s–2010s): Macromedia/Adobe Flash Professional authored web experiences on a stage canvas with timeline animation and interactivity (scripted or component behavior) published as live web artifacts (.swf); Adobe Director/Shockwave served the same role earlier. These products satisfy all three L0 structures — visual canvas, behavior as first-class authored design material, live web artifact — while lacking responsive breakpoints, CMS, components-as-design-systems, and AI. Conclusion: the definition is not over-fitted to the 2026 no-code generation; the historically older realization passes. Conversely, the modern sample's specific features (GSAP engine, webhook publishing, spline-viewer) are correctly excluded from the definition.

## Boundary Findings

| Neighboring Type | Relationship | Removal test / distinction |
|---|---|---|
| Visual Website Builder (§04.16) | sharpest seam, same tool space | Site builders center on assembling whole sites — content, navigation, commerce, templates/sections; interactions are a feature. This Type centers on *authored behavior* as the design act on a freeform canvas. Remove first-class behavior authoring → becomes a Visual Website Builder. The embed pole (Ceros/Vev/Spline) is clearly outside site building; the site pole (Framer/Webflow) sits on the seam with behavior-first as center of gravity. Webflow self-describes as web development; Ceros explicitly differentiates itself "from a website builder or CMS." |
| Landing Page Builder (§04.16) | adjacent pole overlap | Landing builders optimize conversion of a single page (forms, A/B, lead capture) with template-driven assembly; here the center is the designed experience itself. Both poles of this Type can produce campaign pages (Vev use-case list; Framer landing-page solution) — the seam is purpose and center of gravity, not artifact. |
| UX Prototyping Application / Interactive Prototype Builder (§04.15) | closest capability neighbor | Prototypes *simulate* the final product and are handed to developers; here the design is published as the production artifact. Remove live web publication → prototyping. Framer's own market history (prototyping tool → live-site design tool) is market evidence that the seam is real and crossed deliberately. |
| Motion Graphics Application (§04.07) | adjacent | Motion graphics outputs rendered video/animation files; here the output is a live interactive web experience responding to its viewer. Remove interactivity → motion graphics. |
| Graphic Design Application (§04.01) | upstream | Graphic design produces static artwork; no live behavior. Remove behavior + web publication → graphic design. |
| Content Management System / CMS (§02.07) | complementary | CMSs are content-structure systems with templated presentation; this Type is design-behavior systems that often bind to or publish into CMSs (Vev/Ceros positioning literally "fills the gap" of the CMS). Both vendors state the distinction from a CMS. |
| 3D Modeling Application (§04.13) | crossover | Spline spans both; its 3D authoring side belongs to 3D creation, its interactive web delivery side to this Type. Center-of-gravity test applies. |
| Web Development IDE / No-code Application Builder (§12) | adjacent | Code-first development vs designer-canvas-first experience design; Webflow's "visual development" self-description is the extreme member of this Type leaning toward that boundary. |
| Template-based Design Platform (§04.01) | adjacent | Template-first assembly of static visual deliverables vs canvas-first authoring of behavior-bearing live web artifacts. |

## Uncertainties

- Readymag's exact capability set unverified (source limitation); used only as evidence of a designer-craft pole existing.
- Wix Studio (agency pole of a site builder with advanced-interaction claims from general market knowledge) not verified; excluded from all claims. If a future pass documents it, the Visual Website Builder seam analysis may need revisiting.
- The site pole vs content pole was established from vendor self-descriptions (Framer/Ceros comparison, Ceros FAQ, Vev positioning); no neutral third-party taxonomy was consulted. The center-of-gravity framing is a canonical inference (C-layer), not a directly observed industry standard.
- Deep operational details (interaction model limits, plan gates, performance behavior) were not researched and are not asserted.
- The directory's leaf name ("Interactive Web Design Application") is not a common vendor category label; the market vocabulary splits between "interactive content platform" (Ceros, Vev) and "web design tool with interactions" (Framer, Webflow). This is a naming consideration for the directory, not an obstacle to the Type.

## Final Synthesis

Interactive Web Design Application is a distinct designer-facing Application Type: a visual authoring application for web experiences in which the designer composes pages/screens on a canvas AND authors their behavior (trigger → animated/state response) as part of the design, and the output is a live web artifact — a hosted site or an interactive experience embedded into a web page. The defining core is exactly three jointly-held structures (canvas composition + first-class authored behavior + live web artifact); responsive systems, CMS, components, hosting/embed machinery, collaboration, analytics, and AI assistance are standard but not definitional; scope (full site vs embedded experience), audience (designer-craft vs marketing/brand vs agency), governance, and code posture are variants. The Type holds a real center-of-gravity seam against Visual Website Builder (site-assembly-first), Landing Page Builder (conversion-first), UX Prototyping (non-published artifact), and Motion Graphics (rendered video), and a complementary seam against CMS. Historical check passes against Flash-era tools.

**Taxonomy verdict: ratified as a distinct Type** — with two caveats recorded as Boundary Issues: (1) the seam with Visual Website Builder is a center-of-gravity split within one shared tool space and both leaves will attract the same flagship products (Webflow, Framer); joint review of the two documents is recommended once Visual Website Builder is processed; (2) the leaf name is not market-standard vocabulary.
