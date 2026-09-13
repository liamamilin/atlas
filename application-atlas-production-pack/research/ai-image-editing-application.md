# Research Notes — AI Image Editing Application

Research date: 2026-09-06
Leaf: AI Image Editing Application (DIRECTORY §04.20 Generative Visual; siblings: AI Image Generator, AI Design Generator)
Slug: ai-image-editing-application

## Research Goal

Understand what an "AI Image Editing Application" actually is as an Application Type: what the user provides, what the system does to the image, how the edit loop works, and where the boundary lies against the sibling AI Image Generator and AI Design Generator, against the manual Photo Editor / Raster Image Editor Types, and against photo editors that merely bundle AI features.

## Initial Boundary (working hypothesis before research)

- Hypothesis: an application whose primary job is modifying an existing image supplied by the user, where the headline edit operations are performed by AI models (removal, background replacement, enhancement, generative add/replace, restyling) rather than by the user's own deterministic tool strokes.
- Nearest neighbors: AI Image Generator (creates from description, no source image), AI Design Generator (design compositions as deliverable), Photo Editor (manual photographic adjustments), Raster Image Editor (general pixel editing), Image Batch Processor / Conversion (non-interactive utilities), AI Video Editing (different medium).
- Unknowns at start: whether "generative" (content synthesis) is required or analytical AI ops (removal/enhancement) suffice; how manual tools coexist with AI ops; how instruction modality varies (one-tap vs brush+prompt vs conversational); metering and licensing postures; whether platform-native photo apps (Google Photos Magic Editor, Apple Photos Clean Up) fit.

## Research Questions

1. What does the user provide as input — always an existing image? From where?
2. What is the catalog of AI edit operations across products? Which are analytical (detect/remove/enhance) vs generative (synthesize new content)?
3. How does the user target the edit (whole image, brush, auto-detect) and instruct it (preset, prompt, conversation)?
4. What does the post-operation loop look like (review, retry, refine, continue with manual tools)?
5. How do manual editing tools coexist with AI operations, and which is the center of gravity?
6. What persistence, delivery, metering, licensing, privacy/provenance machinery exists?
7. Where is the boundary to AI Image Generator, AI Design Generator, Photo Editor, Raster Image Editor, and image utilities?
8. Do platform-native photo apps and single-purpose tools still fit the same definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy | Customer tier | Evidence level |
|---|---|---|---|
| Facetune (Lightricks) | mobile-first AI selfie/photo editor; conversational AI assistant; one-tap AI feature catalog | consumer / social creators | Tier-2 (official product + AI-photo-editor pages, feature-level) + Tier-1 help-center index |
| Photoleap (Lightricks) | mobile AI photo editor; brush+prompt generative editing (AI Transform) on a layer-based editor | consumer / creative | Tier-2 (official product + AI Replace pages) + Tier-1 help-center article index |
| BeFunky | web all-in-one editor (photo + collage + design) with a named AI feature set | consumer / SMB | Tier-2 (official homepage, feature-level) |
| remove.bg (Canva Austria) | single-purpose AI edit (background removal) with manual touch-up + API | individuals → e-commerce/enterprise | Tier-2 (official homepage) |
| Microsoft Designer | design generator whose "Edit with AI" surface performs AI image editing on uploaded photos | consumer (personal) | Tier-1 (official support article, full) |

Market anchors considered but unreachable on the research date (no claims made about their internals): Adobe Photoshop (Generative Fill/Expand), Canva (Magic Edit/Magic Eraser), Pixlr, Photoroom, Luminar Neo, Picsart, Fotor, Google Photos Magic Editor, Apple Photos Clean Up. Photopea (reachable) used as boundary evidence only — a manual raster editor with no documented AI editing surface.

## Sources

Fetched 2026-09-06 (reachable layer):

- Microsoft Designer — Welcome to Microsoft Designer (Tier-1 support article): https://support.microsoft.com/en-us/Designer/welcome-to-microsoft-designer
- Lightricks Help Center — Photoleap section index (Tier-1): https://lightricks.zendesk.com/hc/en-us/sections/28873600717330-Photoleap
- Lightricks Help Center — Facetune category index (Tier-1): https://lightricks.zendesk.com/hc/en-us/categories/360002911719-Facetune
- Facetune — product homepage (Tier-2): https://www.facetuneapp.com/
- Facetune — AI Photo Editor page (Tier-2): https://www.facetuneapp.com/features/ai-photo-editor
- Photoleap — product homepage (Tier-2): https://www.photoleapapp.com/
- Photoleap — AI Replace / AI Transform page (Tier-2): https://www.photoleapapp.com/features/ai-replace
- BeFunky — product homepage (Tier-2): https://www.befunky.com/
- remove.bg — product homepage (Tier-2): https://www.remove.bg/
- Photopea — Learn/Introduction (Tier-1, boundary evidence): https://www.photopea.com/learn/

Source-access limitations (recorded per evidence rules; no detail filled from model memory):

- helpx.adobe.com and adobe.com (Photoshop Generative Fill docs): timed out on 3 attempts → abandoned. Professional-suite-embedded AI editing under-evidenced.
- canva.com (Magic Studio / help): browser-sniffing wall on 2 attempts across passes → abandoned.
- photoroom.com: transport error ×2 → abandoned. E-commerce mobile segment under-evidenced.
- pixlr.com: timeout ×2 → abandoned.
- skylum.com (Luminar Neo): HTTP 403 → abandoned. AI-first desktop photo editor segment under-evidenced.
- picsart.com, fotor.com (×2), clipdrop.co, krea.ai: timeouts → abandoned.
- support.google.com (Photos Magic Editor): timeout → platform-native segment under-evidenced.
- support.befunky.com: transport error ×2 → BeFunky evidence stays at homepage feature level.
- Consequence: operational mechanics are asserted at the level the fetched pages support; no numeric limits, prices, or defaults from unreachable sources are asserted anywhere.

## Product Observations

### Facetune (evidence layer A — official product pages + help-center index)

- Positioning: "Your Everyday Editing Tool Companion"; help center: "Your everyday mobile editor for selfies, photos, and videos, powered by AI tools." Audience: influencers, creators, social-media users ("stand out on social media").
- AI feature catalog (each = named one-tap operation on the user's photo): AI Photo Enhancer, AI Hairstyle & Hair Color, AI Outfit Changer, AI Beauty Filters, AI Beard Filters, AI Color Analysis, AI Headshot Generator, AI Photo Reshape, AI Nail Simulator, Skin Tone Editor, Freckles Editor, AI Bangs Filter, AI Face Shape Detector, AI Wrinkle Remover, AI Smile Filter.
- Photo-editor tool catalog alongside AI: Remove Object From Photo ("Vanish"), Photo Retouch, Background Remover, Filters & Effects, Blur, Crop, Makeup, Flip, Eye Color Changer, Image Brightener, Teeth Whitening, AI Shadow Remover, Blemish Remover, Face Slimmer.
- Conversational instruction modality: "Transform your photos using our AI photo editor through simple prompts, where every edit is just a conversation away with Facetune's AI assistant. Want smoother skin? A vintage look? A stunning new hairstyle? Just ask!"
- One-tap transformation framing: "redefine aesthetics, styles, and vibes in just a tap"; "Turn your selfies into new AI visuals — it's the same you, with an all new vibe."
- Documented how-to loop: "1. Open the Facetune app on your phone and select a photo from your gallery. 2. Tap on your chosen AI feature and let Facetune's AI transform your photo. 3. Download your new AI photo and share it on your socials or to your phone."
- Multi-face support documented in help center ("Can I edit multiple faces in a photo/video"); edits reusable ("Can I save my edits for use in a future project"); own photos from device ("How do I use my own photos in Facetune?").
- Surfaces: mobile apps (App Store/Google Play) + web editor ("Facetune is now on the web").
- Monetization: freemium; some AI features free, others VIP subscription; 7-day free trial; watermark-free editing for VIP.
- Privacy/safety: help-center sections "Safety, Privacy and Monetization" incl. "Facetune Policy" and "Are my Images stored in the App?".
- Use-case packaging: profile picture maker, passport photo maker, LinkedIn headshot, dating profile, wedding, real estate photo editors.

### Photoleap (evidence layer A — official product pages + help-center article index)

- Positioning: "A photo editor for every vision… The AI photo editor app for quick edits to pro designs." Mobile app (homepage states iOS only; AI Transform FAQ states iOS and Android — conflicting, recorded as uncertainty).
- Generative targeted editing (AI Transform / "AI Replace"): "Pick the 'Custom' option to brush over an area in your photo and describe what you want it to become. Alternatively, select from our 'Props' collection for quick, fun changes. Watch in amazement as the AI instantly creates a new, AI-generated object in place of the old."
- Documented operation loop: open app → choose AI Transform → Custom (brush area + type prompt) or Props (pre-designed edits) → "Let AI work its magic."
- Refinement after AI ops: FAQ — "Can I personalize my design after using AI Transform? Yes, after using AI Transform, you can further personalize your image with Photoleap's range of editing tools, giving you full control over the final look."
- AI tool catalog: AI Replace, AI Background Generator, AI Image Extender (Uncrop), AI Colorize, AI Photo to Painting, Photo to Cartoon, AI Interior Design, AI Photo Enhancer, AI Image Upscaler, AI Style Transfer, AI Hairstyle Simulator, AI Headshot Generator, AI Image Generator (text-to-image), AI Yearbook, AI Gender Swap, AI Facemix, AI Face Swap, AI Tattoo Generator, AI Costume Generator, AI Character Generator, AI Portrait Generator, AI Image to Video.
- Manual editing tools: Remove Objects, Combine Photos, Remove Background, Crop, Borders, Collage, Blur, Filters & Effects, Animate, Text, Double Exposure.
- Layer system documented in help center ("What are Layers and how do I use them?" — "Photoleap uses a Layering system…"); Cutout tool article; Projects saved per device ("Can I continue editing a Project on a different device?" — currently per-device); project size change article.
- Help-center AI feature articles: Using AI Transform, AI Tattoos, AI Cars, AI Rooms, AI Scenes, AI Facemix.
- Monetization: freemium; Pro/VIP subscription; 7-day trial; listed pricing $3.99/mo or $47.99/yr (marketing page).
- Commercial use: "Photoleap Policy" article addresses monetization/commercial use of Projects.
- Bundled generation: text-to-image generator and image-to-video sit beside editing (suite bundling).

### BeFunky (evidence layer A for homepage — Tier-2 official, feature level)

- Positioning: "all-in-one online Creative Platform" — Photo Editor + Collage Maker + Graphic Designer; web app + mobile app.
- Dedicated "AI Features" nav group: Background Remover ("Our Artificial Intelligence powered Background Remover detects the main subject in your photo and removes the background – in a single click!"), Object Eraser, Photo Enhancer, Upscale, Sky Replacer, Deblur, Old Photo Restorer.
- Manual editor alongside: crop/resize/exposure, effects (Cartoonizer, Digital Art), Touch Up retouching, text, vector graphics, batch processing.
- Support center exists (support.befunky.com) but unreachable on research date (2 transport errors) — no help-article-level evidence.

### remove.bg (evidence layer A for homepage — Tier-2 official)

- Positioning: "Remove Image Background 100% Automatically and Free. One tool, endless uses." Single-operation AI editing.
- Output semantics: white background for e-commerce shots/car listings/headshots; transparent PNG for logos/graphics.
- Manual refinement of the AI result: "Magic Brush" (touch up the cutout).
- Audience segmentation: individuals, photographers, marketing, developers, e-commerce, media, car dealerships, enterprise.
- Delivery surfaces: web app, API + documentation, integrations/tools/apps, Photoshop extension, Windows/Mac/Linux desktop, Android app, design templates.
- Feedback loop: "Teach the Artificial Intelligence" — users contribute rejected results to improve future quality (Improvement Program).
- Ownership: "remove.bg, a Canva Austria GmbH brand."

### Microsoft Designer (evidence layer A — Tier-1 official support article)

- "Edit with AI" tab = AI image editing surface inside a design generator: "upload your own photo or choose from a gallery of images to begin editing. Use AI tools to restyle your image, remove or blur backgrounds, or fix individual elements with crop, rotate, and adjust features. Enhance your image even further with filters, design templates, and text options. When finished, you can download, copy, or share your edited image."
- Generative erase feature (from the Designer FAQ article, per ai-design-generator research): quick/brush select → erase object; Upscale (to 4K, age-gated); prompt abuse monitoring; C2PA content credentials on AI-generated/edited images.
- Shows the capability-embedding pattern: AI image editing as a tab inside a broader generative design product.

### Photopea (boundary evidence — Tier-1 official learn site)

- "An advanced image editor, which can work with both raster and vector graphics"; full manual toolchain (layers, masks, selections, adjustments, text, vector, automation); runs locally in browser.
- No AI editing features documented anywhere in the learn TOC — demonstrates that a full-featured image editor without AI-executed operations remains a Raster Image Editor, not this Type.

## Cross-product Comparison

| Dimension | Facetune | Photoleap | BeFunky | remove.bg | Microsoft Designer (Edit with AI) |
|---|---|---|---|---|---|
| Source image intake | photo from device gallery | own photos into a Project | upload to web editor | upload (web/app/API) | upload or pick from gallery |
| AI op families | remove object (Vanish), background remove/replace, enhance, reshape, wrinkle/blemish/shadow removal, style filters, try-on (hair/outfit/nails/makeup), headshot gen | remove objects, background remove/generate, generative add/replace (AI Transform), extend (Uncrop), colorize, paint/cartoon styles, enhance, upscale, interior/scene restyle | background remove, object erase, enhance, upscale, sky replace, deblur, old-photo restore | background removal only (+ Magic Brush touch-up) | restyle, remove/blur background, generative erase, upscale, crop/rotate/adjust, filters |
| Targeting | auto-detect (faces/subject), tap tools | brush over area (Custom) or preset Props | single-click auto-detect; tool-specific | auto-detect subject + Magic Brush manual refine | quick/brush select (erase) |
| Instruction modality | one-tap features + conversational AI assistant ("just ask") | brush + text prompt (Custom) or preset Props | one-tap named features | one-tap (no prompts) | one-tap tools + select-and-erase |
| Generative synthesis | yes (try-on, headshots, restyle) | yes (AI Transform generates new object in place) | yes (sky replace, restore) | no (analytical segmentation) | yes (erase fills, restyle) |
| Manual tools alongside | retouch/crop/blur/filters/text | layers, cutout, crop, text, filters, collage | full photo editor + design + collage | Magic Brush only | crop/rotate/adjust, filters, text, templates |
| Review/refine loop | tap feature → result → save/share; edits reusable | AI result → further personalize with editing tools | apply → continue editing | result → Magic Brush refine → download | pick result → download/copy/share or Edit |
| Persistence | save edits for future projects; images stored per policy | Projects saved (per device) | account Photos | — (single-shot tool) | auto-saved cloud projects |
| Delivery | download/share to socials | export/save project | download | download result (white/transparent) | download/copy/share |
| Metering | freemium + VIP subscription, watermark-free at VIP | freemium + Pro/VIP, trial | freemium (BeFunky Plus) | free tier + paid plans/API credits | free with M365 account; subscription for heavier use |
| Privacy/safety surface | Safety/Privacy/Monetization help section; image-storage policy | Photoleap Policy (commercial use) | not observed on fetched page | Improvement Program (user-image contribution, opt-in) | prompt-abuse monitoring; C2PA content credentials; age gating |
| Platform | mobile + web | mobile (iOS; Android per FAQ) | web + mobile | web/desktop/API/extension | web + M365 embedding |
| Domain focus | people/selfie/social | creative photo art + fun transforms | general consumer photos | subject cutout (e-commerce, IDs, cars) | everyday graphics in design context |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Four properties. Remove any one and the product stops being an AI Image Editing Application:

1. **Source image as the object of work** — the user brings an existing image (photo, product shot, graphic) into the application; the edit operates on that image. Remove → AI Image Generator (creation from description).
2. **System-executed edit operations** — the application's AI models interpret the image's content (subject, background, faces, regions) and produce the changed result; the user selects/targets/describes, the system computes. Remove (user performs all edits with deterministic tools) → Photo Editor / Raster Image Editor.
3. **Review-and-refine loop** — the user inspects the computed result, retries or adjusts it, and can continue editing (with further AI operations or manual tools). Remove (one-shot endpoint with no interactive surface) → model API / batch utility.
4. **Edited image as deliverable** — the result is saved/exported/shared as an image. Remove → not an editing application.

Notes:
- "AI-executed" is satisfied by both analytical operations (subject/background detection, removal, enhancement, restoration) and generative synthesis (fill, replace, expand, restyle). A product needs system-executed operations; it does not need every family.
- No requirement about: specific model technology, prompt interfaces, cloud delivery, subscription, mobile platform, or any specific operation catalog.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B unless noted):

- one-tap AI feature catalog: operations packaged as named, single-click features (A in Facetune/BeFunky/Photoleap/Designer; the dominant presentation across the sample)
- manual editing tools alongside AI operations (crop/adjust/filters/text; layers in Photoleap; retouch in Facetune/BeFunky) — the AI surface sits inside a broader editor in most products
- edit targeting: auto-detection (subject/face) and/or brush/selection of the region (A in Photoleap brush, Designer brush-select, remove.bg Magic Brush; auto-detect in Facetune/BeFunky/remove.bg)
- removal/background/enhance families recur in every sampled product (B)
- retry/variation: generative operations produce a computed result the user can rerun or pick among (A Photoleap "variety of AI-generated transformations", Designer "variety of design options")
- before/after comparison and progressive stacking of operations (implied by editor surfaces; B)
- persistence: projects/edits saved for later continuation (A Photoleap projects, Facetune saved edits, Designer cloud projects)
- delivery paths: download/save/share, plus integrations/API in some products (A remove.bg API/extension, Designer M365 embedding)
- freemium metering: free tier + subscription/credits gating the AI operations (all five)
- privacy/policy surface: image-storage policies, commercial-use policy, safety sections (A Facetune, Photoleap; Designer C2PA/provenance — product-specific so far)
- prompt-directed editing (brush+prompt, conversational assistant) — common in the current generation of generative-capable products (A Facetune assistant, Photoleap Custom, Designer erase) but absent in preset-only products (remove.bg, BeFunky as observed) → common, with preset-only as an existing variant

### L2 — Variant / Optional Structure

- operation breadth: single-purpose tool (remove.bg) ↔ multi-tool editor (Facetune/Photoleap/BeFunky)
- domain focus: people/selfie/social (Facetune), creative photo-art (Photoleap), general consumer (BeFunky), e-commerce/product cutout (remove.bg, Photoroom as market anchor), design-suite embedded (Designer, Canva as market anchor)
- instruction modality: one-tap preset / brush+prompt / conversational assistant
- generative depth: analytical-only (detection/removal/enhancement) vs generative synthesis (fill/replace/expand/restyle)
- platform & packaging: mobile-first, web, desktop, API, embedded in a host editor or platform photo app (Google Photos Magic Editor / Apple Photos Clean Up as market anchors)
- adjacent bundled capabilities: video editing (Facetune), image-to-video (Photoleap), text-to-image generation (Photoleap/Facetune headshots), design templates (Designer/BeFunky)
- commercial-use licensing posture (Photoleap Policy article)
- provenance/moderation machinery (Designer C2PA + prompt monitoring — only direct observation so far)

### L3 — Vendor-specific (research notes only)

- Facetune: "Vanish" object remover; conversational AI assistant; Color Analysis / Face Shape Detector quizzes; watermark-free VIP; 295M+/400M+ download claims (inconsistent between pages); $13/mo or $40/quarter pricing.
- Photoleap: AI Transform with "Props" preset collection; named AI Rooms/Scenes/Cars/Facemix/Tattoos features; per-device projects; $3.99/mo or $47.99/yr pricing; iOS-only vs iOS+Android conflict between pages.
- BeFunky: named AI features (Sky Replacer, Deblur, Old Photo Restorer); all-in-one photo+collage+design packaging.
- remove.bg: Magic Brush; "Teach the AI" opt-in improvement program; Canva Austria ownership; Photoshop extension; white-background vs transparent-PNG output semantics.
- Microsoft Designer: DALL·E powering; C2PA content credentials; M365 app embedding; upscale to 4K; age gating; legacy-editor deprecation Oct 2025.

## Historical / Market-Sample Check (§24)

- The Type is gen-AI era (background-removal tools ~2018+, generative editing ~2022+), so the "older product" check has limited reach, but three older/adjacent patterns were tested against the L0:
  - **Pre-AI automatic fixes** (auto-levels, one-click enhance in classic photo editors): parameterized adjustments executed by deterministic algorithms the user configures; they do not interpret content to decide *what* to change. They remain Photo Editor structure — the L0's "system interprets content and produces the change" is what separates this Type. (Borderline historical precursor: content-aware fill-style operations that synthesize missing content already exhibit the L0's system-executed property; the Type's market emergence post-dates them, but the definition does not depend on neural networks specifically.)
  - **Platform-native photo apps** (Google Photos Magic Editor, Apple Photos Clean Up — market anchors, unreachable): conceptually satisfy the L0 (existing photo + system-executed edit + review + save). No region/platform-bound feature entered the core.
  - **Batch/automation utilities**: no interactive review loop → fail L0 property 3 → Image Batch Processor territory.
- Regional check: remove.bg (European-rooted, global e-commerce audience) and the sample's US/Israel-rooted products satisfy the L0 identically; no region-bound feature entered the core.
- Platform check: mobile-first, web, desktop, and API surfaces all satisfy the L0; surface kept out of the core.

## Vendor-specific Findings

See L3. None promoted to the canonical model. The conversational-assistant modality (Facetune) and the C2PA provenance machinery (Designer) are single-product observations and stay product-specific.

## Rejected Findings

- **"Generative synthesis is definitional"** — rejected: remove.bg satisfies the Type with a purely analytical operation (subject segmentation + removal), and BeFunky's observed set is largely analytical. The invariant is *system-executed* operations, not content synthesis. Generative depth is a variant.
- **"A prompt interface is definitional"** — rejected: remove.bg and BeFunky (as observed) offer no prompt surface; one-tap presets and auto-detection suffice. Prompt/conversational instruction is common in the current generation but a variant modality.
- **"Background removal is the defining operation"** — rejected: it is one family among many; products lead with different families (person retouch, generative replace, restoration). Only the existence of system-executed operations is invariant.
- **"Mobile-first is definitional"** — rejected: web (BeFunky, Designer), desktop/API (remove.bg), and platform-native photo apps satisfy the Type; surface is a variant.
- **"Person/face intelligence is definitional"** — rejected: it is segment-specific (people-photo products); product-shot and general-graphics products lack it and remain in the Type.
- **"Any photo editor with an AI feature belongs to this Type"** — rejected as a boundary claim: the Type follows the product's center of gravity. BeFunky is evidence of the gradient (a conventional editor with a named AI set), not proof that the boundary is meaningless; the structural test (remove AI ops → photo editor remains) is documented in Boundary Findings.
- **"Manual tools disqualify a product from this Type"** — rejected: every sampled multi-tool product keeps a manual toolchain; the discriminator is who executes the *headline* edits, not the absence of manual tools.

## Boundary Findings

1. **vs AI Image Generator (04.20 sibling, not yet processed)** — the discriminator is the object of work: an existing image supplied by the user vs a description from which an image is created. Products bundle both (Photoleap ships a text-to-image generator beside its editor; Facetune ships an AI Headshot Generator). Structural test: remove the source-image requirement → image generator remains. Gradient; flag for joint review when AI Image Generator is processed.
2. **vs Photo Editor (04.04) / Raster Image Editor (04.02)** — the discriminator is who executes the edit: the system's models interpret content and produce the change vs the user driving deterministic tools. Products merge both (BeFunky is a photo editor with a named AI set; Facetune/Photoleap keep manual toolchains; raster-editor research already classifies "AI generative editing" as an L2 drift for that Type). Structural test: remove AI-executed operations → photo/raster editor remains; remove manual tools → AI editor remains. Gradient; flag for joint review when Photo Editor is processed.
3. **vs AI Design Generator (04.20 sibling)** — deliverable class: an edited image vs a design composition (arranged elements + text + format-for-purpose semantics). Microsoft Designer straddles: its "Edit with AI" tab is image editing inside a design generator. Structural test: remove design-composition/format semantics → image editing remains. (Consistent with ai-design-generator research finding 1.)
4. **vs AI Video Editing Application (04.21)** — medium: Facetune and Photoleap bundle video editing and image-to-video; the image is this Type's object. Suite bundling, not Type merger.
5. **vs Image Batch Processor / Image Conversion (04.05)** — no interactive per-image review loop, no content-semantic operations → utility Types. remove.bg's API sits at this edge but its app surface keeps the review loop.
6. **Capability-embedding pattern** — AI image editing appears standalone (Facetune, Photoleap, BeFunky), embedded in photo editors (BeFunky), embedded in design platforms (Designer; Canva as market anchor), embedded in platform photo apps (Google/Apple as market anchors), and exposed as APIs (remove.bg). Standalone vs embedded is packaging, not structure; the leaf is defined intake- and packaging-agnostic.
7. **Taxonomy note** — the market phrase "AI photo editor" covers both AI-first editors (Facetune, Photoleap) and photo editors with AI features (BeFunky, Luminar Neo as market anchor). The leaf is defensible as the source-image-centered Type within 04.20 whose headline surface is AI-executed operations; the load-bearing boundaries are findings 1 and 2, both gradients.

## Uncertainties

- Photoshop (Generative Fill/Expand), Canva Magic Studio, Pixlr, Photoroom, Luminar Neo, Picsart, Fotor, Google Photos Magic Editor, Apple Photos Clean Up were unreachable on the research date → the professional-suite, template-platform, web-tool, AI-first-desktop, and platform-native segments are under-evidenced; no claims made about their internals. The L0/L1 were phrased to be segment-agnostic.
- Whether every market product keeps a manual-tool layer beside AI ops is unverified beyond the sample (remove.bg has only Magic Brush); the final document phrases manual tools as common, not required.
- Photoleap platform support conflicts between its own pages (homepage: iOS only; AI Transform FAQ: iOS and Android) — recorded, not resolved; no platform claim made in the final document.
- Facetune download counts differ between its own pages (295M+ vs 400M+) — marketing figures, excluded from the final document.
- Exact credit costs, variant counts, storage limits, and moderation policies for the sampled products are mostly not documented at the fetched layer; no precise numbers asserted.
- The precise historical boundary between "advanced deterministic photo tools" and "AI-executed operations" is inherently fuzzy for pre-2020 products; the L0 is phrased by structure (who interprets and produces the change), not by technology brand.

## Final Synthesis

An AI Image Editing Application is an application in which the user brings an existing image, the application's AI models execute edit operations on it — interpreting content (subject, background, faces, regions) to remove, replace, enhance, restore, restyle, extend, or synthesize parts — and the user reviews each computed result, retries or refines it (with further AI operations or manual tools), and delivers the edited image. The defining core is deliberately small: source image, system-executed edit operations, review-and-refine loop, edited image as deliverable. Everything else familiar in the market — one-tap feature catalogs, brush/prompt/conversational instruction, manual toolchains, layers, projects, before/after comparison, freemium metering, privacy policies, integrations and APIs — is common mature structure; operation breadth, domain focus, generative depth, platform, packaging, and adjacent capabilities (video, generation, design) are variants. The load-bearing boundaries are against the AI Image Generator (object of work: existing image vs description) and the Photo/Raster Editor (who executes the edit); both are gradients and flagged for joint review.
