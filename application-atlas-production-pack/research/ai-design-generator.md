# Research Notes — AI Design Generator

Research date: 2026-09-06
Leaf: AI Design Generator (DIRECTORY §04.20 Generative Visual, siblings: AI Image Generator, AI Image Editing Application)
Slug: ai-design-generator

## Research Goal

Understand what an "AI Design Generator" actually is as an Application Type: what the user provides, what the system produces, how the generation→refinement→delivery loop works, and where the boundary lies against the sibling AI Image Generator and against Template-based Design Platforms / Graphic Design Applications that increasingly bundle generative AI.

## Initial Boundary (working hypothesis before research)

- Hypothesis: an application whose core is producing *design artifacts* (social posts, cards, invitations, banners, logos, UI mockups) from user-described intent using generative AI, where the output is an editable design composition rather than a final flat image.
- Nearest neighbors: AI Image Generator (flat image deliverable), Template-based Design Platform (human-browsed pre-made templates), Graphic Design Application (human-composed editing), UI Design Application (manual UI design), AI Website Builder (working site as deliverable).
- Unknowns: whether "editable structure" is universal; how template libraries and generation coexist; how brand/style machinery is implemented; licensing and metering postures.

## Research Questions

1. What does the user provide as input? (description, uploaded assets, event details, brand assets, screenshots?)
2. What is the generated output — an editable design composition or a flat image? How many candidates?
3. What does the post-generation refinement loop look like (direct editing vs AI-directed edits)?
4. What design conventions does the product automate (layout, color, typography, brand consistency, format/size)?
5. What deliverables and delivery paths exist (download, copy, share, embed in other apps, integrations)?
6. How is generation metered (free tier, subscription, credits) and licensed (personal vs commercial)?
7. What safety/moderation/provenance machinery exists?
8. Where is the boundary to AI Image Generator, Template-based Design Platform, Graphic Design Application, UI Design Application, and AI Website Builder?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy | Customer tier | Evidence level |
|---|---|---|---|
| Microsoft Designer | prompt→design variants for everyday personal graphics; embedded in M365 | consumer (personal, non-commercial) | Tier-1 (2 official support articles, full) |
| Recraft | professional-designer design platform with own models; vector-native output | professional designers/teams | Tier-2 (2 official product pages, feature-level) |
| Uizard | AI-first UI/product design generation (multi-screen prototypes) | product teams, PMs, founders, enterprise | Tier-2 (2 official product pages, feature-level) |
| Designs.ai | brief→specialist agents→multi-format on-brand assets | SMB / solo operators | Tier-2 (1 official product page, positioning-level) |

Market anchors considered but unreachable (no claims made): Canva (Magic Design), Adobe Express (Firefly), Looka (logo/brand generator), Galileo AI, Framer AI, Wix ADI.

## Sources

Fetched 2026-09-06:

- Microsoft Designer — Welcome to Microsoft Designer (Tier-1 support article): https://support.microsoft.com/en-us/Designer/welcome-to-microsoft-designer
- Microsoft Designer — Frequently asked questions (Tier-1 support article): https://support.microsoft.com/en-us/Designer/frequently-asked-questions-about-microsoft-designer
- Uizard — product homepage (Tier-2): https://uizard.io/
- Uizard — Autodesigner 2.0 page incl. FAQ (Tier-2): https://uizard.io/autodesigner/
- Recraft — product homepage (Tier-2): https://www.recraft.ai/
- Recraft — AI Vector Generator page (Tier-2): https://www.recraft.ai/vector-generator
- Designs.ai — product homepage (Tier-2): https://designs.ai/

Source-access limitations (recorded per evidence rules):

- Canva (canva.com/help, canva.com/magic-design): blocked by browser-sniffing wall on 2 attempts → abandoned. Template-platform-with-generation segment under-evidenced.
- Adobe (helpx.adobe.com/express ×2 timeouts; adobe.com/express ×2 timeouts) → abandoned. Professional-suite-embedded generation under-evidenced.
- Looka (looka.com): 403 on 1 attempt → abandoned. Logo/brand-generator segment under-evidenced.
- Microsoft Designer root (designer.microsoft.com) is a JS shell — no content; Tier-1 support articles used instead.
- No Tier-1 operational help-center docs were reachable for Uizard, Recraft, or Designs.ai; their evidence is product-page level. Operational mechanics for these products are asserted only at feature/positioning level; no numeric limits, defaults, or pricing asserted for them.

## Product Observations

### Microsoft Designer (evidence layer A — Tier-1 official support docs)

Key observations:

- Positioning: "graphic design tool… uses the power of generative AI to create eye-catching images with your words, craft next-level designs… and edit photos"; "AI-powered visual designs"; for personal use with a Microsoft account; explicitly personal, non-commercial license.
- Three top-level creation modes: **Create with AI** (describe → generate → variety of design options → pick → download/copy/refine → Edit), **Edit with AI** (upload photo → restyle, remove/blur backgrounds, crop/rotate/adjust → filters, design templates, text → download/copy/share), **Design from scratch** (blank canvas → choose layout/size → add images, text, shapes, icons with AI tools → filters/fonts/color palettes/upload own media → download/copy/share).
- Template search coexists with generation: search bar for templates/inspiration by keyword ("invitation", "social media post"); choose templates or start from scratch.
- Feature catalog (each = described intent → generated result → download or edit in canvas): Banners (description + images + dimension), Brand kits (brand name/description → logo, palette, font, brand voice; apply to designs; one saved at a time), Collages (up to 10 uploaded images + description + style), Enhance prompt (AI rewrites prompt), Frame image (upload + elements + style → custom frame), Generate text (prompt → text options; rewrite existing text), Generative erase (quick/brush select → erase object), Greeting cards (description → animated digital card with image + message; edit text), Invitations (occasion details → 1–5 vertical invitation options), Social posts (description + images + platform size), Upscale (up to 4K; age-gated).
- Storage: designs auto-saved to cloud ("My projects"); uploads saved to OneDrive; files count toward Microsoft storage quota; no recycle bin (deletes unrecoverable).
- Delivery: download, copy, send to phone via QR; components supported in Teams, Outlook, Word for the Web, OneNote, PowerPoint; creation from Word/PowerPoint via Copilot (Copilot Pro subscription required).
- Access: web app, iOS/Android apps, embedded in M365 apps; requires Microsoft 365 Personal or Family (not enterprise); free to use, "a subscription may be required for those who want to create more frequently"; age requirements by region for generative-AI features.
- Responsible AI: prompt abuse monitoring; content credentials (C2PA provenance metadata) on AI-generated/edited images; controls against harmful uploads/generation.
- Known limitation stated by vendor: text inside generated images may not be in the requested language or may contain spelling errors.
- Product evolution note: legacy visual editor deprecated Oct 2025; brand kits and stock videos removed in migration to a new editor with improved image/text editing.

### Recraft (evidence layer A for product pages — Tier-2 official)

Key observations:

- Positioning: "AI for designers, creatives, sellers, and teams"; "top-ranked text-to-image model and design platform"; Recraft Studio = "creator's platform for generating and editing images, vectors, and mockups with Recraft's models and other top frontier models".
- Vector generation: text prompt → production-ready SVG (logos, icons, illustrations); "clean paths, editable layers, scalable to any size"; ready for Figma, Illustrator, production.
- Generate-and-iterate loop: "Pick from multiple generations. Adjust the palette, drop background elements, change level of detail — without leaving the canvas"; export at any size without quality loss; recolor whole palette in one click; reduce color count.
- Raster↔vector: upload raster → convert to SVG (vectorizer); generate raster then vectorize.
- Custom styles: drop in your images → reusable, editable style ("Style It Once, Every Image Matches" — V4 Styles).
- Multi-model studio: Recraft models plus third-party frontier models (image and video) in one design tool; API + MCP; integrations into Figma, Framer, Chrome, Google Docs/Slides.
- Use cases: ads, stock images, icons, logos, characters; professionals: graphic designers, print-on-demand sellers, visual artists; custom DPI and CMYK for print.
- Delivery surfaces: web studio, mobile apps, API, host-app integrations.

### Uizard (evidence layer A for product pages — Tier-2 official)

Key observations:

- Positioning: "UI design made easy, powered by AI"; "AI-first from day one" (founded 2018); audiences: product managers, designers/UX pros, marketers, startup founders, consultants/agencies, developers, enterprise.
- Autodesigner 2.0: "combines the conversational flow of ChatGPT with Uizard's generative design capabilities and drag-and-drop editor"; conversational modality to generate designs, add elements, modify components with text prompts; "idea to sharable, interactive prototype with plain english".
- Generation units: multi-screen editable prototypes from simple text; new screens for existing projects; new themes ("instantly change the style"); component-level modification ("Select any component, describe the changes you want").
- Brand kit: "Generate UIs that match your design system and brand guidelines".
- Import-as-input: Screenshot Scanner (screenshots → editable mockups); Wireframe Scanner (hand-drawn wireframes → digital designs).
- Real-time collaboration with the product team; templates library (mobile app, website, web app, tablet, wireframes).

### Designs.ai (evidence layer B for positioning — Tier-2 official, single page)

Key observations:

- Positioning: "AI-Powered Design Platform"; 2026 repositioning as "Your AI creative team, on demand": brief once → specialist agents (Brand, Image, Storyboard, Video, Slides, Audio) deliver assets.
- Brand consistency as system-level constraint: "Your brand becomes the system prompt. Enforced automatically across every design, video, slide, and campaign."
- Conversational intake: describe in plain words; agent asks clarifying questions; remembers brand/style/recent projects ("picks up where you left off").
- Skills library incl. Logo Design; chat-based helper (Designs Claw) creating images/video/audio inside a chat app; pay-for-production economics ("you only pay for what it produces").
- Target segments: café/F&B owners, property agents, insurance agents, online sellers, content creators, tuition teachers (SMB/solo operators).

## Cross-product Comparison

| Dimension | Microsoft Designer | Recraft | Uizard | Designs.ai |
|---|---|---|---|---|
| Primary input | text description (+ uploaded images, event details, brand info) | text prompt (+ example images for styles, raster uploads) | text prompts (conversational) (+ screenshots, hand-drawn wireframes) | plain-language brief (+ brand context) |
| Generated output | design variants for a named artifact type (post, card, invitation, banner, collage, frame) | raster images and editable SVG vectors (logos, icons, ads, illustrations) | multi-screen editable UI prototypes, screens, themes | multi-format assets (design/image/video/slides/audio) on brand |
| Multiple candidates | yes ("variety of design options"; 1–5 invitations) | yes ("pick from multiple generations") | multi-screen set (not framed as variants) | agent-produced asset sets |
| Refinement loop | Edit in canvas; AI edits (erase, restyle, background, upscale, text) | iterate on canvas (palette, detail, background); vector editing | modify any component by description; regenerate themes/screens | iterate via agent conversation |
| Style/brand machinery | brand kits (logo/palette/font/voice) applied to designs | custom styles from example images; palette control | brand kit matching design system; themes | brand enforced as system-level constraint |
| Format semantics | platform size selection (social posts), dimensions (banners), vertical (invitations) | scalable SVG, any export size, DPI/CMYK | device/screen formats | per-format agents |
| Templates / from-scratch | template search + design from scratch alongside generation | examples as prompt inspiration | templates library alongside generation | skills/examples |
| Storage | auto-saved cloud projects ("My projects") | studio projects | projects with screens | projects remembered by agent |
| Delivery | download/copy/QR-to-phone; embed in M365 apps | download SVG/any size; Figma/Illustrator-ready; API; host integrations | sharable interactive prototype | ready-to-ship assets; chat delivery |
| Audience | consumers, personal non-commercial | professional designers, sellers, teams | product teams, PMs, founders | SMB/solo operators |
| Metering | free + subscription for more frequent creation | pricing tiers + API pricing | free signup + pricing tiers | pay for what it produces |
| Safety/provenance | prompt abuse monitoring; C2PA content credentials; age gating | not observed on fetched pages | not observed on fetched pages | not observed on fetched pages |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three properties. Remove any one and the product stops being an AI Design Generator:

1. **Described design intent as the driving input** — the user conveys what they want (a description, optionally plus supplied assets/content/brand context); the system — not the user — composes the first-pass design. Remove → manual design application (Graphic Design Application).
2. **Machine-composed design output** — the system produces one or more candidate designs: arranged visual elements and text with styling, within a defined output format, for a design purpose (post, card, invitation, banner, screen, logo…). Remove the composition/format/design-purpose semantics (flat image only) → AI Image Generator.
3. **Workable generated design** — the output remains a workable design object: the user can refine it (direct editing and/or AI-directed modification) and deliver it as an artifact (download/copy/share/export). Remove → one-shot generation endpoint, drifting toward image generation / API-only.

Notes:
- "Design purpose" is generic: visual communication artifacts, brand identity artifacts, product/UI mockups.
- Text in the design is typical but not required as an invariant (some generated artifacts are text-free graphics); the composition+format+purpose semantics are the invariant.
- No requirement about: LLM/conversational interface (form-based prompt fields qualify), specific model technology, cloud-only delivery, subscription, brand kits, collaboration.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B unless noted):

- multiple candidate outputs per generation (A in Designer, Recraft; B overall)
- prompt aids: example/idea galleries that preload prompts; prompt enhancement/rewriting (A in Designer; B in Uizard conversational flow)
- a design canvas editor with direct manipulation (text, images, shapes) alongside generation (A Designer; A-level product pages Uizard/Recraft)
- AI-directed edit operations: restyle, background removal/blur, object erase, upscale, text generation/rewrite (A Designer; Recraft/Uizard equivalents at feature level)
- style/brand machinery: brand kits, themes, custom styles, brand-as-constraint (all four products, differently implemented)
- format/size selection tied to target platform/purpose (Designer, Recraft, Uizard; Designs.ai per-format)
- template library and/or from-scratch mode coexisting with generation (Designer, Uizard; Recraft examples-as-inspiration)
- persistent project storage with auto-save (A Designer; B Uizard/Recraft/Designs.ai)
- delivery paths: download/copy/share; embedding into other apps or integrations (A Designer M365 embedding; Recraft Figma/Framer/Docs/Slides integrations; Designs.ai chat delivery)
- metered usage economics: free tier + subscription/credits/pay-per-output (all four)
- import-as-input paths: uploaded images as design material (Designer collages/frames/social posts; Recraft vectorizer); screenshot/sketch scanning (Uizard — product-specific so far)

### L2 — Variant / Optional Structure

- domain specialization: social/marketing graphics (Designer), UI/product mockups (Uizard), logos/icons/ads/print (Recraft), multi-format campaigns (Designs.ai), logo/brand-only (Looka — unreachable, market anchor)
- deliverable class: raster images vs editable vectors vs multi-screen prototypes vs animated cards (Designer animated greeting cards)
- input modality: form-based prompt fields vs conversational agent; image upload; screenshot/wireframe scanning
- model posture: proprietary model (Designer/DALL·E, Recraft V4) vs multi-model routing (Recraft studio, Designs.ai) vs embedded in host suite (Designer-in-M365, Recraft-in-Figma)
- entry surface: web app, mobile apps, embedded in host apps, chat surfaces
- commercial license posture: personal non-commercial (Designer) vs commercial plans (Recraft, Designs.ai)
- collaboration: real-time multi-user (Uizard; Recraft teams)
- safety/provenance machinery: prompt moderation, content credentials (C2PA), age/region gating (A Designer only — treat as product-specific evidence of a conceptually common concern)
- print-production depth: DPI/CMYK control (Recraft)

### L3 — Vendor-specific (research notes only)

- Designer: DALL·E powering; C2PA content credentials; OneDrive storage/quota coupling; no recycle bin; one saved brand kit at a time; 1–5 invitation options; upscale to 4K; M365 Personal/Family gating (no enterprise); Copilot Pro embedding; legacy-editor deprecation (brand kits/stock videos removed Oct 2025).
- Uizard: Autodesigner 2.0 naming; Screenshot Scanner / Wireframe Scanner; GenUI framing; "AI-first since 2018" claim.
- Recraft: V4/V4.1 model naming; V4 Styles; named third-party model catalog; MCP server; custom DPI/CMYK feature.
- Designs.ai: AI Agent routing; Designs Claw chat helper; "brand as system prompt" framing; pay-for-production.

## Historical / Market-Sample Check (§24)

- The Type is gen-AI era (2022+), so the "older product" check has limited reach, but two older patterns were tested against the L0:
  - **Content-driven layout suggestion inside a host app** (e.g., automatic slide-layout suggestions in presentation apps): input is the user's content, not a described design intent; output is layout suggestions applied inside a document container. Fails L0 property 1 → capability of a Presentation Application, not this Type.
  - **Pre-genAI automatic site/logo builders** (Q&A-driven site generation; template-algorithm logo makers): site generators produce a functioning website (different deliverable container) → Visual Website Builder territory; template-algorithm logo makers that output a finished logo with customization steps can satisfy L0 (described intent → composed design → workable/customizable result) — the L0 deliberately does not require neural generation.
- Regional check: Designs.ai (Southeast-Asia-rooted, SMB segments) satisfies the L0 with no regional specifics. No region-bound feature entered the core.
- Platform check: web-first products dominate the sample, but mobile apps (Designer) and chat surfaces (Designs.ai) also satisfy the L0; surface kept out of the core.

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Boundary Findings

1. **vs AI Image Generator (04.20 sibling, not yet processed)** — gradient, not a wall. The discriminator is the deliverable class: a design composition serving a design purpose within a defined format (with workability) vs a flat image as the final artifact. Products straddle: Designer's engine generates images as material inside designs; Recraft sells image generation and a design studio in one product and its own nav lists "AI image generator" first. Structural test: remove design-purpose composition/format semantics → image generator remains; keep them → design generator. Flag for joint review when AI Image Generator is processed.
2. **vs Template-based Design Platform (04.01 sibling)** — the discriminator is the origin of the first-pass composition: generated from described intent vs pre-made and browsed. Products bundle both (Designer has template search; the unreachable Canva is the archetype of generation-inside-template-platform). Gradient; flag for joint review.
3. **vs Graphic Design Application (04.01 sibling)** — who composes the first pass: the system (generation-first) vs the user (editing-first). AI design generators include full editors, so the difference is the workflow center of gravity, not feature presence. Gradient.
4. **vs UI Design Application / UX Prototyping (04.15)** — Uizard generates UI mockups/prototypes; the UI-design Type centers manual UI design/prototyping tooling. UI generation is a domain variant of design generation, but the boundary needs a joint review when 04.15 leaves are processed.
5. **vs Visual Website Builder / AI site generation (04.16)** — deliverable container differs: a design artifact (image/vector/prototype) vs a functioning website (structure + content + hosting). AI site generators fail L0 property 2's "design artifact" semantics. Clean split at research depth.
6. **vs AI Video Generator (04.21)** — animated design artifacts exist (animated greeting cards), but motion-video generation from prompts is a different deliverable class; Designs.ai bundles video agents beside design agents (suite bundling, not Type merger).
7. **Capability-embedding pattern** — the generation loop appears both standalone (Designer web, Recraft studio, Uizard) and embedded as a capability inside broader products (Designer-in-M365 via Copilot, Recraft-in-Figma/Framer, generation features inside template platforms). Standalone vs embedded is packaging, not structure; the leaf should be defined intake-agnostic.
8. **Taxonomy note** — the market phrase "AI design tool/platform" is loose: some products marketed as "AI design" are primarily image generators (Recraft's own navigation leads with image generation). The leaf is defensible as the design-composition-centered Type within 04.20, but the sibling boundary (finding 1) is the load-bearing one.

## Uncertainties

- Canva, Adobe Express, Looka unreachable → the template-platform-with-generation, suite-embedded, and logo-generator segments are under-evidenced; no claims made about them. The L0/L1 were checked to be segment-agnostic, but their L1 details (e.g., how template platforms integrate generation) are unverified.
- Whether every market product keeps the output structurally editable (vs delivering image-only results with regenerate-only refinement) is unverified beyond the sample; the final document phrases workability to cover both direct editing and AI-directed modification.
- Exact variant counts, credit costs, storage limits, and moderation policies for Uizard/Recraft/Designs.ai unknown (no Tier-1 docs); no precise numbers asserted for them.
- Designs.ai evidence is single-page positioning-level; its operational mechanics (agent routing, delivery) not verified in depth.

## Final Synthesis

An AI Design Generator is an application in which the user describes a design intent and the system composes candidate designs — arranged visual elements and text with styling, within a defined output format, for a design purpose — which remain workable (directly editable and/or AI-directable) until the user delivers them as artifacts. The defining core is deliberately small: described intent, machine-composed design output, workable result. Everything else familiar in the market — multiple variants, prompt aids, canvas editors, AI edit operations, brand/style machinery, template libraries, project storage, integrations, metering — is common mature structure, and domain specialization (social graphics, UI mockups, logos, print, campaigns), deliverable class (raster/vector/prototype/animated), input modality, model posture, and packaging (standalone/embedded/suite) are variants. The load-bearing boundary is against the AI Image Generator (deliverable class) and the Template-based Design Platform (origin of the first-pass composition); both are gradients and flagged for joint review.
