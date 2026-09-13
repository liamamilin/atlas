# Research Notes — Template-based Design Platform

## Research Goal

Understand what a Template-based Design Platform is as an Application Type: its defining core, its standard mature structure, its variants, and its boundaries against the neighboring creation Types — especially the two 04.01 siblings (Graphic Design Application, Collaborative Design Platform) and AI Design Generator (04.20).

This leaf sits in DIRECTORY section 04.01 "General Visual Design". Three prior passes recorded boundary flags against this leaf, all awaiting ratification from this side:

- **graphic-design-application** (§Taxonomy Issues #4, #5): ratified the 04.01 three-way partition (editing-first freeform / template-first / collaboration-first) and asked this pass to ratify from its side; also recorded the consumer/browser drift watch — a sampled vendor's beginner web app positions itself against "template-based alternatives" on vector-editing depth, evidence that the editing-first/template-first seam (origin of the first pass + freeform composition depth), not surface or audience, is the load-bearing 04.01 discriminator.
- **ai-design-generator** (§Boundary Findings #2): "the discriminator is the origin of the first-pass composition: generated from described intent vs pre-made and browsed. Products bundle both… Gradient; flag for joint review."
- **collaborative-design-platform** (§Boundary Findings #3): "Template-first platforms start from a browsed library of pre-made compositions and constrain editing for non-designers; this Type starts from blank/shared design files with freeform object editing for designers (while offering templates as optional starters). Canva unreachable in this pass — boundary drawn conceptually; flag for joint review."

Additionally, the presentation-application pass noted a Canva straddle (template platforms carrying presentation formats), and the resume-builder pass recorded "vs template-based-design-platform (career semantics)".

## Initial Boundary (hypothesis before research)

- What: a design application whose organizing structure is a maintained library of pre-made, professionally designed, editable compositions (templates) that users browse, select, and personalize to produce finished designs — rather than composing freeform from a blank canvas.
- Users: non-designers who need designed-looking output (small businesses, marketers, communicators, educators, individuals), plus teams and brand administrators at the upper tiers.
- Nearest neighbors: Graphic Design Application (04.01), Collaborative Design Platform (04.01), AI Design Generator (04.20), Visual Website Builder (04.16), Presentation Application (03.04), Desktop Publishing Application (04.17), Resume Builder, template/asset marketplaces.
- Sharpest expected seams: the three 04.01/04.20 flags above.
- Unknowns: whether the "platform" (hosted, account-based) is definitional or era machinery; whether the non-designer audience is a structural leg or a posture; how far AI-generated first passes erode the template-first center; whether blank-canvas composition is universal.

## Research Questions

1. What is the unit of work, and what exactly is a "template" in these systems (catalog entry vs user design)?
2. What is the canonical workflow from arrival to delivered artifact?
3. What does the editor expose, and how deep does freeform composition go relative to customization?
4. Which capabilities are universal in the sample vs plan/segment-dependent (brand kit, resize, print, collaboration, AI)?
5. Where are the boundaries vs the three flagged sibling Types, website builders, presentation applications, DTP, resume builders, and template marketplaces?
6. Historical check: do pre-web template-driven design products (desktop print-studio/greeting-card generation, template-gallery DTP) satisfy the definition without cloud/subscription/AI?

## Representative Products

Selection principles: market representation + documentation accessibility + different product philosophies + different customer tiers.

| Product | Role in sample | Directly researched? |
|---|---|---|
| Piktochart | focused template platform (infographics/reports/presentations-first); communications/education/HR departments; freemium | YES — Tier-1 help center (5 articles/categories) + Tier-2 homepage |
| VistaCreate | SMB-marketing template platform (Vistaprint family); social/print/ads formats; freemium | YES — Tier-2 homepage + full nav (help center unreachable) |
| Desygner | all-in-one template platform with PDF/enterprise/brand-governance emphasis; SMB→enterprise | YES — Tier-2 homepage + design-online FAQ (help center 500) |
| Canva | the archetype generalist template platform; consumer→enterprise | NO — browser gate (3rd consecutive pass); market anchor only |
| Adobe Express | creative-software incumbent's template-first product | NO — timeouts ×2 this pass (helpx timeouts in prior passes); market anchor only |

Rejected candidates: Marq/Lucidpress (brand-template management pole — closer to brand-governance territory), Venngage/Visme (same infographic pole as Piktochart, redundant), Microsoft Designer (AI-generation-first — belongs to the ai-design-generator gradient), PosterMyWall (video/poster marketing pole, thin docs).

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Piktochart Knowledge Base — https://support.piktochart.com/ (Help Scout KB)
  - "Getting Started with Piktochart" — https://support.piktochart.com/article/583-create-a-visual-in-4-steps
  - "Piktochart New Editor" — https://support.piktochart.com/article/584-piktochart-new-editor
  - "How to Download or Export Your Visual" — https://support.piktochart.com/article/418-downloading-visual
  - "Team: Collaboration" — https://support.piktochart.com/article/125-collaboration
  - "Download, Publish & Share" category — https://support.piktochart.com/category/613-download-publish-share
- Piktochart homepage — https://piktochart.com/
- VistaCreate homepage + navigation — https://create.vista.com/
- Desygner homepage — https://www.desygner.com/ ; "Design Online" FAQ — https://www.desygner.com/design-online/

Unreachable (recorded per source-access limitation; abandoned after 1–2 failures each):

- canva.com (incl. /help/): "unsupported browser" gate — same gate as the two prior passes; abandoned after 1 attempt this pass
- adobe.com/express/ and helpx.adobe.com/express/help.html: timeout ×2 (helpx also timed out ×2 in the graphic-design pass)
- create.vista.com/support/, /help-center/, /faq/: 404; support.vistacreate.com: soft-redirects to homepage
- support.desygner.com: HTTP 500; help.desygner.com: empty shell; desygner.com/tutorials/: JS-rendered shell

Evidence layers used below: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality; **C** = canonical inference.

## Product Observations

### Piktochart — evidence layer A (Tier-1 help center + Tier-2 homepage)

Positioning (homepage): "Meet the next generation of infographics… create stunning infographics, reports, and presentations… No design experience required." Products: Piktochart Visual, Video Editor, AI Design Generator. Claimed scale: 34M+ users, 220M+ visuals created. Solutions by department: communications, education, eLearning, financial services, healthcare, HR, marketing, nonprofits. Plans: Free / Pro / Enterprise / Education / Nonprofit.

Canonical workflow (Tier-1 "Getting Started with Piktochart", last updated 2026-06):

```text
Create account
→ land on the Visual Dashboard
→ choose what to create (formats: infographics, presentations, posters, reports, flyers —
   "set to the optimal dimensions for each visual format")
→ browse template categories or search keywords (e.g. "Technology", "Annual reports")
→ premium templates marked and plan-gated ("you'll need to upgrade your subscription to access and edit it")
→ click "Edit Template" on the chosen template
   (alternative documented in the same step: "Start from Blank")
→ edit in the editor: double-click text boxes; add graphics (icons, photos, maps, charts);
   change colors, resize, rotate; change fonts/colors/sizes; adjust layouts
→ optionally use AI ("generate designs from text prompts; turn documents into presentations
   or infographics; create or edit images")
→ Download (PNG, PDF, PPT) / Publish (share as an online presentation) / Share (social media)
```

Support posture (Tier-1 FAQ): "We don't offer custom design services. Piktochart is built to be easy for anyone to use, even without design skills."

Editor structure (Tier-1 "Piktochart New Editor"): left panel menu (graphics, photos, uploads under "My Files", colors, charts, tables, "More"); top panel with Download; pages/blocks add/delete/rearrange; one-click image replacement; crop/mask tool; color dropper; color schemes ("built-in designer color schemes or create your own… saved and reused across other visuals"); chart settings (data format, data colors, data labels, tooltips); "My Library" for paying users to save/reuse assets; presentation-format resize between 4:3 and 16:9; one-way Classic→New editor conversion ("visuals cannot be reverted").

Delivery (Tier-1 "How to Download or Export Your Visual"): Download button in the top panel → file type (PNG / PDF / PPT; explicitly no JPEG, no DOCX) → quality (Normal / Medium / High — Medium/High scale the design 2×/3× for print crispness) → "Download as Pages/Blocks" toggle (paginated PDF vs one continuous long-form design) → plan gating (free users: 2 non-renewable download credits, PNG only; Pro: unlimited PNG; Business: unlimited PNG/PDF/PPT). Related Tier-1 articles: transparent-background download, A-series print sizes (A0–A10), Presentation Mode, social-media publishing, email sharing, citation.

Collaboration (Tier-1 "Team: Collaboration"): workspace model; "By default, only you can edit your work, and only from within your own workspace"; invite team members; share visuals with the team or specific members; **no live co-editing** — "only one person can edit a visual at a time. If a second person tries to enter the editor, they will see an alert that the original person editing will be removed from the editor in order to let the second person in"; others view via the visual's comments page; no cross-workspace visual transfer; seats unlimited via sales. (Note: the homepage markets collaboration "just like in Google Docs" — the Tier-1 doc contradicts the live-co-editing reading; Tier-1 wins.)

Brand (homepage): Brand Assets hub (fonts, colors, logos); Branded Templates — "transforming all Piktochart templates into thousands of stylish, on-brand templates."

AI (homepage + Tier-1): Pikto AI — generate a visual from a text prompt by format ("Choose a format… Enter your topic or prompt… Click Generate Visual… personalize it by adding text, or change the layout"); image generator/modifier/upscaler/restorer, background/object/text remover, icon generator; AI video generation (Sora/Veo models named — vendor-specific).

### VistaCreate — evidence layer A on Tier-2 surfaces (homepage + navigation; help center unreachable)

Positioning (homepage): "VistaCreate is a free graphic design tool with thousands of free templates and powerful AI tools… **Pick a template you love, enhance it with custom visuals, refine your text with built-in features, and post or print.**"

Template library: "200K+ professionally-designed templates… Our online library is frequently updated with new templates for social media, web, and print formats" (100K+ free on the Starter plan). Format catalog in navigation: social media (Instagram posts/stories/reels, Facebook posts/covers, YouTube thumbnails/banners/intros, TikTok videos), print (business cards, flyers, posters, brochures, postcards, eBooks, invitations, letterheads), web (animations, newsletters, portfolios, moodboards, presentations, certificates, logos, planners), ads (Facebook/Instagram/display). Template tags: birthday, wedding, food, AI, business, spring.

Editor: "All-in-one Design Editor" with sidebars for templates, AI tools, and photos.

AI: AI Image Generator, AI Writer, AI Object Remover, Background Remover — "Generate commercially safe visuals, remove objects, and write or refine copy directly in your layout."

Assets: "170M+ photos, videos, and vectors" (Pro; 1M+ free).

Brand: "Brand Kit and Styles features — Upload your brand colors, fonts, and logos… Use the Styles tool to pull colors from templates and apply them to your own. Easily mix and match colors and font pairings to any template you choose."

Delivery: "Post, schedule, print — Make your own designs and post or schedule them for socials. If you're working with select print formats, send them for print through VistaPrint! Doorstep delivery included." One-click Resizer (Pro): "no need to recreate designs for different formats… resize your ready project for different social media and print formats in a click." HD download (Pro). Version history (Pro).

Collaboration: "Design together with your team… invite up to 10 people to join you and work on projects at the same time."

Plans: Starter ($0: 100K+ templates, 1M+ assets, 1 Brand Kit, 10 GB storage, design objects/fonts/music, social scheduling) / Pro (200K+ templates, 170M+ assets, infinite Brand Kits, generative AI image+text, Sticker Maker, one-click resizer, unlimited storage, version history, HD download).

### Desygner — evidence layer A on Tier-2 surfaces (homepage + design-online FAQ; help center 500)

Positioning (homepage): "One Platform. Replaces Everything. Design, documents, presentations, PDFs, social posts, video, whiteboards, spreadsheets — all free. 50 million people already made the switch."

Design Online page: "The all-in-one online design platform for marketing materials, social media content, presentations, documents, and more. No download needed. Free to start."

FAQ (design-online): free plan = "create designs using templates, images, and basic editing tools"; Pro+/Business = "AI tools, unlimited storage, and team features"; browser-based on desktop/tablet/phone plus iOS/Android apps; Brand Kit — "Upload your logo, fonts, and brand colors to create a Brand Kit that automatically applies across all your designs"; differentiation vs Canva — "PDF editing, Design Automation for creating materials at scale, Open Access for branded web pages, and enterprise-grade Brand Governance."

Template catalog (navigation): free templates by category — social media, business cards, flyers, posters, invitations, brochures, logos, greeting cards, certificates, documents, banner ads, book covers, menus & price lists. Design-tool "makers": logo, presentation, banner, flyer, brochure, poster, card, certificate, infographic, collage, meme, resume; photo editor, background remover, resize. Print Hub: print business cards, flyers, posters, invitations, menus. Compare pages: vs Canva, vs Adobe, vs Figma, vs Affinity.

### Canva — NO direct evidence; market anchor

Browser-gated for the third consecutive pass (this pass: 1 attempt at /help/, same gate). Widely-attested structural facts only, no operational claims: the archetype generalist template-first design platform — very large multi-format template library, drag-and-drop editor, brand kit, print offering, freemium model, consumer→enterprise span. The two sibling passes (collaborative-design-platform, ai-design-generator) also failed to fetch it.

### Adobe Express — NO direct evidence; market anchor

Timeouts ×2 this pass (adobe.com/express/, helpx.adobe.com/express/help.html); helpx.adobe.com also timed out ×2 in the graphic-design pass. Widely-attested structural facts only: Adobe's template-first quick-create product with templates, stock/font integration, and quick actions. No operational claims.

## Cross-product Comparison

| Dimension | Piktochart | VistaCreate | Desygner | (Anchors: Canva, Adobe Express) |
|---|---|---|---|---|
| Self-label | visual/infographics platform, "no design experience required" | "free graphic design tool" with templates | "all-in-one online design platform" / "One Platform. Replaces Everything." | template-first design platforms (market-attested) |
| Template library | format-organized catalog (infographic/presentation/poster/report/flyer), premium-marked | 200K+ templates, "frequently updated", social/web/print | free templates by 13+ categories | very large multi-format libraries (market-attested) |
| Starting point | "Edit Template"; "Start from Blank" documented as the alternative | "Pick a template you love" | "create designs using templates" | same posture (market-attested) |
| Format-correct canvases | "set to the optimal dimensions for each visual format" | format catalog = pre-sized formats | format-specific makers/templates | same |
| Editor | panel-based: graphics/photos/uploads/colors/charts/tables; pages/blocks; crop/mask; color schemes | all-in-one editor, sidebars (templates/AI/photos) | browser editor + mobile apps | drag-and-drop editors (market-attested) |
| Assets | stock graphics/photos/maps/charts + uploads + My Library | 170M+ photos/videos/vectors | royalty-free images | stock libraries (market-attested) |
| Brand layer | Brand Assets + Branded Templates | Brand Kit + Styles (pull colors from templates) | Brand Kit auto-applied | brand kit (market-attested) |
| Resize/reformat | presentation 4:3↔16:9; A-series download sizes | one-click resizer to other formats | resize tool | magic-resize class (market-attested) |
| Export | PNG/PDF/PPT (no JPEG/DOCX); quality tiers; paginated-vs-continuous; transparent bg; plan-gated credits | HD download (Pro) | PDF emphasis | standard formats (market-attested) |
| Publish/share | online presentation link, social, email, citation | post/schedule to socials | Open Access branded web pages | sharing/scheduling (market-attested) |
| Print | print-quality guidance (A-series, fit-to-page) | VistaPrint fulfillment, doorstep delivery | Print Hub | Canva Print (market-attested) |
| Collaboration | workspace; private-by-default; share/comment; **one-editor-at-a-time** | up to 10 members "at the same time" | team features (Pro+/Business) | multi-user (market-attested) |
| AI | Pikto AI: prompt→visual by format; image tools; docs→visuals | AI image gen, AI writer, object remover | AI-powered design (Pro+) | AI suites (market-attested) |
| Plans | Free/Pro/Business/Enterprise/Education/Nonprofit; download credits | Starter/Pro freemium | Free/Pro+/Business | freemium (market-attested) |
| Focus | infographics/reports/data-visuals first; department solutions | SMB marketing/social; print commerce tie-in | breadth + PDF + enterprise governance | generalist |

### Cross-product commonalities (layer B)

1. **The template library is the organizing catalog.** Every sampled product leads with a browsable, searchable, operator-maintained catalog of pre-made designs organized by format and use case; the homepage pitch is the library ("Pick a template you love"; "create designs using templates"; format-organized dashboard).
2. **Design-by-customization is the default loop.** Select template → personalize content (text, images, colors, elements) in the product's own editor. Blank-canvas composition exists (documented as the alternative option in the one Tier-1 workflow doc) but is not the organizing path.
3. **Finished-design delivery is built in.** Download/export in standard formats, publish/share online, social posting/scheduling; print fulfillment at 2/3 sampled (VistaCreate→VistaPrint, Desygner Print Hub) and print-quality export guidance at the third.
4. **Format-correct canvases.** Templates are pre-set to the target format's standard dimensions; resize machinery converts a finished design to other formats.
5. **Stock asset libraries + user uploads** feed the customization.
6. **Brand layer** (brand kit; branded/locked templates at the team pole) — 3/3 sampled.
7. **Freemium gating shapes the library and delivery** — premium-marked templates, asset-count tiers, export-format/credit limits (all 3 sampled).
8. **AI embedded as capabilities** — prompt-to-visual generation, image generation/editing, background removal, copywriting (all 3 sampled); the AI path lands in the same editor beside the template path.
9. **Cloud-stored projects in a personal/team workspace** with version history (where documented).
10. **Collaboration is a share/review layer** whose depth varies; the only Tier-1-collaboration doc in the sample explicitly documents one-editor-at-a-time (no live co-editing).

## Abstraction Levels

### L0 — Defining Invariant (deliberately small; three jointly-held structures)

1. **The template library as the operator-maintained catalog of starting points** — a curated, organized, searchable collection of pre-made, professionally designed, editable compositions spanning multiple design formats/use cases, maintained by the platform operator and offered to every user. Remove → blank-canvas design application (templates as optional starters) or a single-template tool.
2. **Design-by-customization in the platform's editor** — the user starts from a selected template and personalizes its content (text, images, colors, graphical elements); the template carries the designed structure (layout, typography, color, graphics) so the output is designed-looking without the user composing from scratch. Freeform composition is available but secondary. Remove → Graphic Design Application (editing-first freeform).
3. **Finished-design delivery** — the customized design is completed and rendered out as a usable artifact: downloaded/exported (image/PDF/video), published/shared online, scheduled to social channels, or sent to print. Remove → template gallery/marketplace (files for other software) or a preview site.

Jointly-held load-bearing:

```text
1 alone                = template marketplace / gallery (Envato-class: files, no in-product editing)
2 without 1            = blank-canvas design application (Graphic Design Application)
3 without 1+2          = export utility
1+2 without 3          = template browsing with no usable output
1+3 without 2          = download store
2+3 without 1          = single-template tool / generic editor
```

Historical check (§24): the desktop template-driven design generation — print-studio/greeting-card software and template-gallery DTP products of the late 1980s–1990s — satisfies all three legs with the library shipped on disk (operator-maintained catalog of pre-made editable compositions), customization in the product's own editor, and print output, with no web/cloud/subscription/AI. Conceptual lineage (layer C; no fetched sources for that generation — no precise product claims made). The L0 therefore contains none of the modern platform machinery: hosted delivery, accounts, cloud storage, freemium, AI, and the web surface are all era/market machinery. Word processors with template galleries do NOT satisfy leg 2 as the center (text documents, not visual compositions) — correctly excluded.

### L1 — Common Mature Structure (cross-product, layer B)

- format catalog organized by use case (social posts/stories, presentations, posters, flyers, business cards, logos, documents, ads…) with format-correct dimensions
- template browse/search (categories, keywords, tags) with premium markers
- drag-and-drop editor: text editing, image replacement, element add/remove/rearrange, color/font application, crop/mask
- stock asset library (photos, videos, vectors, icons, fonts) + user uploads + saved/reusable asset library
- brand kit (colors, fonts, logos) applied across designs; branded templates at the team pole
- one-click resize/reformat to other formats
- cloud-stored design projects ("my designs") with version history
- export in standard formats (PNG/JPG-class, PDF, PPT-class, video), quality options, transparent background
- publish/share surfaces (link, online view/presentation, social posting/scheduling, email)
- team collaboration (workspace, sharing, comments, team assets)
- AI assistance (prompt-to-visual, image generation/editing, background removal, copywriting)
- freemium plan gating over templates/assets/features/export

### L2 — Variant / Optional Structure

- format breadth: generalist multi-format vs focused (infographics-first, resume-first)
- audience/segment: consumer-personal (invitations, cards) vs SMB marketing vs enterprise brand governance
- brand-governance depth: brand kit → branded templates → locked templates / design automation at scale / brand governance (enterprise pole)
- print fulfillment: integrated print ordering vs print-quality export only
- content types: static graphics vs video/animation vs documents vs presentations vs web pages (web publishing drifts toward Visual Website Builder)
- delivery: web app + mobile apps (current norm) vs desktop heritage (historical pole)
- AI posture: assistive tools beside templates vs AI-generation-first entry
- collaboration depth: share/comment vs simultaneous multi-user editing (product-dependent)
- licensing: freemium subscription dominant; plan ladders vary

### L3 — Vendor-specific (research notes only)

- Piktochart: Pikto AI naming; Classic→New editor one-way conversion; My Files/My Library; built-in designer color schemes; chart settings (data format/colors/labels/tooltips); 4:3↔16:9 presentation resize; download credits (free = 2 non-renewable, PNG-only; Pro = unlimited PNG; Business = PNG/PDF/PPT); "Download as Pages/Blocks"; A-series sizes; citation tool; no JPEG/DOCX export; one-editor-at-a-time collaboration; department solutions; 34M users/220M visuals claims; Sora/Veo video models
- VistaCreate: VistaPrint print integration ("doorstep delivery"); Styles tool (pull colors from templates); Sticker Maker; 200K+/100K+ template counts; 170M+/1M+ asset counts; 10-seat Pro collaboration; specific pricing; 10 GB vs unlimited storage
- Desygner: "One Platform. Replaces Everything." positioning; Design Automation (materials at scale); Open Access (branded web pages); enterprise Brand Governance; PDF-editing emphasis; Print Hub; vs-Canva/vs-Adobe/vs-Figma comparison pages; 50M users claim
- Canva / Adobe Express: no operational claims (unreachable); market-attested posture only

## Rejected Findings

- **"Template-based design platform = Canva / = web app"** — rejected. The desktop template-driven generation satisfies the L0 with the library on disk; hosted delivery is era machinery. The Type is delivery-agnostic.
- **"Non-designer audience is the definition"** — rejected as a structural leg. The audience is the Type's posture and the reason the template carries design quality, but the structural discriminator is template-first origin + customization depth (professionals also use these products; the graphic-design pass's drift watch confirms the seam is structural, not audience-based).
- **"AI generation is defining"** — rejected. AI is embedded as a capability/entry path in all sampled products; the template library remains the organizing catalog and the same editor serves both paths. Gradient with AI Design Generator recorded, not merged.
- **"Multi-format breadth is defining"** — rejected. Focused platforms (infographics-first) satisfy the L0; breadth is a variant axis.
- **"Brand kit is defining"** — rejected. Common mature structure (3/3 sampled) but absent from the historical generation.
- **"Collaboration is defining"** — rejected. Share/review is the common layer; the only Tier-1 collaboration doc documents one-editor-at-a-time. The shared-live-multi-user-file model is the Collaborative Design Platform's defining structure.
- **"Print fulfillment is defining"** — rejected. 2/3 sampled integrate print ordering; the third documents print-quality export only; the historical generation printed on local printers.
- **"The library must be huge (200K+)"** — rejected. Scale is variant; the catalog-ness is the invariant.

## Boundary Findings

| Neighboring Type | Judgment | "Remove what → becomes the other" |
|---|---|---|
| Graphic Design Application (04.01) | **Ratifies the sibling's partition from this side.** The seam is the origin of the first pass + freeform composition depth: this Type organizes the work around browsed pre-made compositions (customize-first, blank secondary); the graphic design application organizes around user-composed freeform designs (templates optional starters). Consistent with the sibling's drift-watch evidence (a beginner web app differentiating from "template-based alternatives" on editing depth). | Make freeform composition the organizing structure and templates optional starters → Graphic Design Application |
| Collaborative Design Platform (04.01) | **Discharges the sibling's flag from this side.** Confirmed: template-first platforms organize around the template library + individual customized designs; collaboration is a share/review layer (Tier-1: one-editor-at-a-time, second editor displaces the first). The collaborative platform's defining structure — one live shared multi-user design file — is absent. | Make the shared live multi-user design file the unit of work → Collaborative Design Platform |
| AI Design Generator (04.20) | **Discharges the sibling's flag from this side.** The origin-of-first-pass discriminator holds: browsed pre-made vs machine-generated from described intent. The gradient is real — sampled products embed prompt-to-visual generation (one product's AI generates the first pass from a prompt by format) — but the template library remains the organizing catalog, the generated result lands in the same editor, and templates remain the fallback/browsing center. Keep-both; products bundle both. | Make described-intent machine composition the primary organizing loop and drop the template-catalog center → AI Design Generator |
| Visual Website Builder (04.16) | Adjacent with a drift watch. The deliverable here is a design artifact (image/PDF/video/print); a functioning website (structure + content + hosting) is the website builder's deliverable. One sampled product's "branded web pages" feature (Open Access) touches the seam — flagged, not merged. | Make the deliverable a hosted functioning website → Visual Website Builder |
| Presentation Application (03.04) | Adjacent straddle. Template platforms carry presentation formats (presentation templates, slide-like pages, PPT download, online presentation publishing), but the deck-delivery grammar (presenter-paced playback as the composing purpose) is not the center; the presentation pass independently recorded the Canva straddle. | Center the deck grammar + delivery → Presentation Application |
| Desktop Publishing Application (04.17) | Adjacent. Template platforms produce print-like layouts (flyers, brochures, menus) but center quick customization of pre-made compositions, not long-document text flow/publication assembly. Historical template-gallery DTP products are the shared ancestor. | Center long-document text flow and publication assembly → DTP |
| Resume Builder | Adjacent. Template platforms include resume templates/makers (2/3 sampled), but resume builders center career-document semantics (section vocabulary, ATS-aware rendering, application tailoring). | Constrain the artifact to the career document with career semantics → Resume Builder |
| Word processor / document editor with templates | Distinct. Built-in templates there are starters for text documents; here the visual design composition across formats is the center. | Center prose documents → document editor |
| Template/asset marketplace (Envato-class) | Clean split at leg 3. Marketplaces sell template files for use in other software; this Type edits and delivers in-product. | Remove in-product editing/delivery, sell files → marketplace |
| Brand Asset / Guideline Platform | Adjacent at the enterprise pole. Brand-governance features (locked branded templates, automation at scale) manage approved expression; the working design loop remains this Type's center. | Hold approved masters and guidelines, not the working customization loop → brand asset platform |

## Taxonomy Issues (for STATUS.md Boundary Issues)

1. **Ratifies the 04.01 three-way partition from this side** (discharges graphic-design-application's flag #4): editing-first freeform / template-first / collaboration-first is a coherent partition; the editing-first/template-first seam (origin of the first pass + freeform composition depth) is confirmed as the load-bearing discriminator from the template side.
2. **Discharges ai-design-generator's flag #2**: origin-of-first-pass discriminator holds; gradient confirmed (prompt-to-visual generation embedded in all 3 sampled products, one product marketing AI-generated first passes prominently) — but the template catalog remains the organizing structure and the editor is shared; keep-both.
3. **Discharges collaborative-design-platform's flag #3**: template-first vs blank/shared-freeform confirmed with Tier-1 collaboration evidence (one-editor-at-a-time; share/comment layer) — the shared live multi-user file is absent from this Type's sample; keep-both.
4. **New drift watch for visual-website-builder (04.16, unprocessed)**: template platforms adding web publishing (Desygner "Open Access — branded web pages") — seam = design artifact vs hosted functioning website; flag for that pass.
5. **Presentation straddle confirmed from this side** (presentation formats, PPT download, online presentation publishing in the sample) — capability, not Type merger; consistent with the presentation-application pass's Canva straddle note.

## Uncertainties

- **Canva and Adobe Express are anchors only** — the two most prominent template platforms could not be fetched (browser gate; timeouts). The generalist consumer pole is under-evidenced first-hand; no operational claims are made about either. The L0/L1 rest on the three directly-researched products.
- **VistaCreate and Desygner help centers were unreachable** — their observations are product-page strength (Tier 2). Step-level editor claims in the final document are calibrated to Piktochart's Tier-1 docs plus cross-product marketing consistency; no step-level claims are attributed to VistaCreate/Desygner beyond their own page text.
- **Blank-canvas universality** — verified as an option in one product's Tier-1 workflow doc; whether every template platform offers a blank start is unverified. The final document phrases blank as "commonly available secondary path", not universal.
- **Historical generation evidence is conceptual** (no fetched sources for print-studio/greeting-card software); the L0 is deliberately era-agnostic and no precise historical product claims are made.
- **Desygner's enterprise depth** (Design Automation, Brand Governance) is positioning-level only (help center 500); held at variant strength.
- **Simultaneous co-editing** — one sampled product documents it (marketing page, "up to 10 people… at the same time"), another explicitly documents its absence (Tier-1). Held as product-dependent; not generalized.

## Final Synthesis

A Template-based Design Platform is a design application whose organizing structure is an operator-maintained library of pre-made, professionally designed, editable compositions — templates — spanning multiple design formats. The user's work is a customization loop: browse/search the library, select a template pre-set to the target format's dimensions, personalize its content (text, images, colors, elements) in the platform's editor, and deliver the finished design (download/export, publish/share, schedule, or print). The template carries the design quality — layout, typography, color, graphics — so users without design training produce designed-looking output; freeform blank-canvas composition exists as a secondary path, and AI-generated first passes increasingly enter the same editor without displacing the template catalog as the organizing center.

The defining core is three jointly-held structures: template library + design-by-customization + finished-design delivery. Everything else commonly associated — format breadth, stock assets, brand kits, resize machinery, cloud projects, collaboration, AI, freemium, print fulfillment, web/mobile delivery — is standard mature structure or variant capability, not definition.

The 04.01 partition is ratified from this side: editing-first freeform (Graphic Design Application) / template-first (this leaf) / collaboration-first (Collaborative Design Platform), with the origin-of-the-first-pass + freeform-depth seam against the graphic design application, the shared-live-file seam against the collaborative platform, and the origin-of-first-pass gradient against the AI Design Generator.
