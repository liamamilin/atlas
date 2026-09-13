# Research Notes — Virtual Beauty Try-on Application

Research date: 2026-09-09
Leaf: Virtual Beauty Try-on Application (§29 Home, Family, Personal & Local Services)
Slug: virtual-beauty-try-on-application

## Research Goal

Understand what a consumer-facing virtual beauty try-on application actually is and how it works: what the user captures, what the tryable options are, how the apply/preview loop operates, how it connects (or does not connect) to shopping, and where its boundary sits against photo editors, AI image tools, e-commerce surfaces, and the beauty-industry sibling Types already processed (beauty-service-marketplace, beauty-professional-business-app, personal-styling-platform).

## Initial Boundary (hypothesis before research)

- Guess: a consumer application that overlays makeup / hair / nail options on the user's own face or photo using AR.
- Neighbors suspected: Photo Editor (selfie retouch), AI Image Generator/Editor, E-commerce Platform (embedded try-on widgets), Beauty Service Marketplace (booking services), Personal Styling Platform (merchandise selection), generic "virtual try-on" in other retail domains (eyewear, watches, clothes).
- Sibling-pass forward flags to verify: personal-styling-platform flagged this leaf as "AR visualization only, no stylist/fulfillment/loop, seam expected clean"; beauty-service-marketplace and beauty-professional-business-app both recorded "consumer-facing AR surface over appearance; no provider population, no bookings, no money flow".

## Research Questions

1. What is the capture model — live camera, uploaded photo, or both? Is AR/face tracking required?
2. What exactly is tryable — which beauty categories, and are options anchored to real products/shades or generic presets?
3. What does the apply/preview loop look like — intensity, before/after, multi-option compare, save/share?
4. How does the shopping connection work — is purchase part of the Type or a hand-off?
5. What non-shopping uses exist (entertainment, exploration, tutorials)?
6. How is the experience deployed — standalone app, retailer app/site, brand site, in-store, API?
7. What are the accuracy/fidelity rules and user guidance (lighting, bare face)?
8. Where is the boundary against photo editing, AI generation, and other virtual try-on domains?
9. Historical check: do pre-AR "virtual makeover" products satisfy the same core?

## Representative Products

Selected for market representation + documentation access + different product philosophy + different deployment surface:

| Product | Pole | Why selected |
|---|---|---|
| YouCam Makeup (Perfect Corp) | standalone consumer app, tech vendor's own consumer product | broadest coverage (makeup + hair + nails + retouch), entertainment-led, freemium |
| Sephora Virtual Artist | retailer-embedded try-on inside the Sephora app | shopping-led, multi-brand assortment, shade matching |
| Ulta Beauty GLAMlab | retailer-embedded try-on (second retailer pole) | app feature framing, "before you shop" positioning |
| Maybelline Virtual Try-On (L'Oréal; ModiFace-powered) | brand-site embedded try-on | brand-owned assortment, official step-by-step usage docs reachable |

Technology-vendor layer (context, not consumer products): Perfect Corp (YouCam/YCE API, docs.perfectcorp.com), ModiFace (L'Oréal subsidiary, modiface.com).

## Sources

Tier 1 (directly fetched official pages):
- Maybelline New York (GCC site) — "Virtual Try On tool" page, fetched 2026-09-09: https://www.maybelline-me.com/en/virtual-beauty-studio/virtual-try-on — full 5-step usage instructions + tips.

Tier 2 (official page text obtained via search-engine cache after direct fetch was blocked):
- Sephora — "Sephora Virtual Artist" page (sephora.nz / sephora.hk / sephora.my, identical text): https://www.sephora.nz/pages/virtual-artist (direct fetch 403 ×2 → degraded to search-cache text)
- Ulta Beauty — GLAMlab pages: https://www.ulta.com/discover/glamlab , https://www.ulta.com/innovation/glamlab/ , https://www.ulta.com/company/app , https://www.ulta.com/discover/lifestyle/ulta-beauty-app-tips-tricks (direct fetch 403 → degraded to search-cache text)
- Maybelline US — https://www.maybelline.com/virtual-try-on-makeup-tools , https://www.maybelline.com/virtual-makeover-makeup-tools , https://www.maybelline.co.in/virtual-try-on (search-cache text)
- Perfect Corp consumer — https://yce.perfectcorp.com/features/ai-makeup-app , https://yce.perfectcorp.com/ai-makeup , https://www.perfectcorp.com/consumer/apps/ymk (search-cache text)
- Apple App Store / Google Play listings for YouCam Makeup (developer-authored listing text): https://apps.apple.com/us/app/youcam-makeup-face-editor/id863844475 , https://play.google.com/store/apps/details?id=com.cyberlink.youcammakeup

Tier 2 (official developer/technology documentation):
- Perfect Corp API docs — https://docs.perfectcorp.com/reference/makeup_vto/section/overview , https://yce.perfectcorp.com/ai-api/products/virtual-makeup-try-on-api , https://yce.perfectcorp.com/ai-api/contents/virtual-try-on-api , https://www.perfectcorp.com/business/showcase/foundation
- ModiFace — https://modiface.com/products-makeup.html

Tier 3 (historical / independent, for the historical check and market context):
- Los Angeles Times, 1997-10-30 — Cosmopolitan Virtual Makeover (SegaSoft/Hearst desktop software): https://www.latimes.com/archives/la-xpm-1997-oct-30-ls-48125-story.html
- The West Georgian (Georgia Historic Newspapers), 2001-02-07 — column reviewing virtual makeover websites (Makeoverstudio.com, Emakeover.com, clairol.com, makeover.women.com, iVillage "makeover-o-matic"): https://gahistoricnewspapers.galileo.usg.edu/lccn/sn11890897/2001-02-07/ed-1/seq-22/ocr/
- TechCrunch, 2009-08-23 — Daily Makeover "Makeover Studio" (face tracing, brand shades, licensed to 60+ brands; Taaz purchase comparison): https://techcrunch.com/2009/08/23/daily-makeover-tries-to-re-create-the-beauty-counter-online/
- NYT, 2009-09-30 — "Pixel Lipstick, Now Improved" (Makeover Studio features: before-after tab, 68-point face mapping): https://www.nytimes.com/2009/10/01/fashion/01SKIN-3.html
- Sephora press release via PRNewswire, 2017-06-07 — Virtual Artist cheek try-on / color match / looks update: https://www.prnewswire.com/news-releases/sephora-virtual-artist-debuts-new-cheek-product-try-on-expanded-looks-and-ai-powered-color-match-technology-in-latest-update-300470427.html
- hellobeautiful.com, 2020-08-19 — independent hands-on of Ulta GLAMlab (photo/stock-model/live modes, shade finder with undertone, cart with store pickup): https://hellobeautiful.com/3183005/tried-it-ulta-glamlab-virtual-makeup-try-on/
- Amazon Ads case study (Maybelline lipstick finder + VTO on Amazon.in): https://advertising.amazon.com/library/case-studies/maybelline-lipstick-finder-virtual-try-on

### Source-access Limitation

- sephora.nz and sephora.hk returned 403 on direct fetch (2 attempts); ulta.com returned 403 (1 attempt). Per the network rule these sources were abandoned for direct fetch. Their official page text was nevertheless captured verbatim in search-engine results and is used as Tier-2 evidence with reduced strength: claims drawn only from those pages are marked below.
- No precise numeric claims (shade counts, accuracy percentages, category counts) from vendor marketing are promoted into the final document; where a number is officially published (e.g. "compare up to 4" on Maybelline's own how-to) it is attributed to that product only.

## Product A — YouCam Makeup (Perfect Corp)

### Key observations (evidence layer A unless noted)

- Positioning: "selfie editor and beauty cam" app; "Live Makeup Virtual Try On: … instantly try the makeup looks on live camera or with a photo" (App Store / Google Play developer listings).
- Capture: live camera mode ("see the makeup move with you in real-time") or uploaded selfie from gallery (official how-to: "Upload Your Photo → Open the app and choose a clear, well-lit selfie from your gallery, or use the 'Live Cam' mode").
- Option catalog: "Makeup" tab with full "Looks" (pre-designed styles) or individual elements — eyeliner, lashes, blush, contour, lip, foundation, eye color, eyebrows (official feature pages).
- Adjust: intensity slider ("use the slider to adjust the intensity. Want a softer lip? Just slide left"); save creation and share.
- Brand integration: "Try on actual products from your favorite global beauty brands before you buy them" — present but the app is broader than shopping (entertainment/selfie-editing first).
- Hair: "Hairstyle Try On & Hair Color Changer" — 250+ preset hairstyles, hair color changer, custom hair try-on with reference photo (app listings).
- Makeup transfer: upload a reference/celebrity photo → AI extracts the look → applies to your face (official AI-makeup pages).
- Adjacent non-try-on capabilities bundled in the same app: face reshape, skin smoothing, teeth whitening, body tuner, AI image/video generation, AI wardrobe (outfit try-on). The try-on core coexists with a full photo editor.
- Online web editor exists (yce.perfectcorp.com/ai-makeup): upload photo → features detected → apply makeup features, free, no download.
- Technology layer (Perfect Corp B2B): Makeup VTO API — async task (image + effect parameters → task_id → poll result); effect schemas per category; shade/texture/finish matching ("7 textures including Matte, Gloss, Holographic, Metallic, Satin, Sheer, Shimmer"; foundation coverage and glow adjustments); 350+ curated looks via single API call; Camera Kit with guided capture and quality validation (lighting, pose, angle, distance) and detection modes incl. `makeup`, `shadefinder`, `nail`, `hairlength`; "Connect try-on experiences to product IDs, images, colors, shades, styles, pricing, and availability"; deployed across "websites, mobile apps, marketplaces, kiosks, consultation tools, and retail platforms"; "trusted by over 800+ brands".

## Product B — Sephora Virtual Artist

### Key observations (evidence layer A via search-cache official page text; reduced strength noted)

- Official page text: "The app scans your face, detects your eyes, lips, and cheeks for product placement, and lets you try on makeup virtually" — facial-recognition-based placement.
- Tryable options: "an infinite library of eyeshadows, lip colours, and even false lashes"; full looks; "compare hundreds of colour swatches instantly"; "compare colour swatches from a range of brands side-by-side on your virtual arm" (swatch-on-arm comparison surface).
- Tutorials: "virtual step-by-step tutorials customised to your own face … instructions that actually map out where to place the product on your face" — tutorial overlay on the user's face.
- Color match: point camera at any photo/object → AI detects color → returns matching shades available at Sephora → "Matches can be immediately tried on in Virtual Artist then purchased in app" (2017 official press release).
- Looks: curated one-click looks by Sephora artists, grouped by category (Daytime/Trend/Nighttime/Natural), overlaid on the user's face in 3D live view; select from skin tones (2017 press release).
- Capture: 3D live view "moves with the user like a mirror"; looks captured as photo/video and shared socially; emailed with product links.
- Shopping hand-off: products saved to "Loves" list or "instantly added to your basket for purchase"; "shop the curated list of products to recreate the look".
- Technology: powered by ModiFace (2017 press release); deployed inside the Sephora mobile app (community post confirms access via the Sephora app).
- Deployment note: page text identical across Sephora regional sites (NZ/HK/MY) — the try-on is a standard retailer feature, not a regional experiment.

## Product C — Ulta Beauty GLAMlab

### Key observations (evidence layer A via search-cache official text; reduced strength noted)

- Official framing: "GLAMlab® is our app's virtual try-on feature. You can test out makeup, lashes, nail color, you name it" (Ulta's own tips article); "Virtually try on thousands of beauty products just as they would look in real life–before you shop" (Ulta company app page).
- Category coverage: makeup, lashes, nail color (official text) — nails evidenced here at retailer pole.
- Independent hands-on (Tier 3, hellobeautiful 2020): three input modes — take/upload a photo, use Ulta's stock model photos matching your complexion, or live try-on; foundation shade finder that returns shade + undertone and was repeatable across lighting conditions; items added to cart with store-pickup or ship options.
- Shopping hand-off: add to cart inside the Ulta app; pickup/shipping (Tier 3).

## Product D — Maybelline Virtual Try-On (brand site, ModiFace-powered)

### Key observations (evidence layer A — page fetched directly)

- Official 5-step usage (fetched verbatim from maybelline-me.com):
  1. "use either the Live Camera or Upload Photo option to get started"
  2. "Browse the different categories of makeup products and select the products you want to try"
  3. "a slider so you can see a before and after in real time and even see half of your face bare-faced and half your face with makeup"
  4. "Use the Compare feature … to compare up to 4 makeup products or shades at once"
  5. "test products individually or give yourself a full face of virtual makeup"
- Official tips: "Find Good Lighting" (bright light washes out, dark room grainy and colors won't match); "Go Bare Face" (traces of foundation/concealer alter face-makeup result; "trying a nude lipstick … while you have a purple one on will not accurately reflect the colour of the nude lipstick") — i.e., options within a category replace each other; the tool renders one treatment per region at a time.
- Tool surface organized by product: the US try-on hub lists products with shade counts and "Buy now" links per product (search-cache official text).
- FAQ (maybelline.co.in, search-cache): "try on makeup products - from lips, eyes, to face - using your camera or uploaded photo, so you can see results before buying"; "mix and match shades and even compare up to 4 products or looks in one virtual makeover session".
- Adjacent brand tools in the same "Virtual Beauty Studio": foundation shade finder (Perfect Shade Foundation Match Finder), lip quiz.
- The same try-on capability is also embedded on retailer channels: Amazon Ads case study documents Maybelline lipstick VTO integrated on Amazon.in product detail pages and Brand Store (Tier 3 for the deployment fact).

## Cross-product Comparison

| Dimension | YouCam Makeup | Sephora Virtual Artist | Ulta GLAMlab | Maybelline VTO |
|---|---|---|---|---|
| Deployment | standalone app + web editor | inside retailer app | inside retailer app | brand website (+ retailer channels via API) |
| Capture | live cam or photo | live 3D view (camera) | photo / stock model / live (Tier 3) | live camera or upload photo |
| Face anchoring | AI face feature detection | facial recognition, eyes/lips/cheeks placement | face scan (Tier 3) | face detection (implied by placement) |
| Option catalog | generic looks + individual elements + brand products + hairstyles + hair color | multi-brand shades (lip/eye/cheek/lashes) + curated looks | "thousands of beauty products", makeup/lashes/nails | brand's own products by category with shade counts |
| Adjust | intensity slider | (not evidenced) | (not evidenced) | intensity slider, before/after, half-face |
| Compare | (not evidenced) | swatch compare, "virtual arm" | (not evidenced) | compare up to 4 |
| Save/share | save + share | save My Looks/Loves, photo/video capture, share | (not evidenced) | (not evidenced) |
| Shade/color matching | AI recommendations | color match from any photo | shade finder with undertone (Tier 3) | foundation shade finder (adjacent tool) |
| Tutorials | (not evidenced) | step-by-step tutorials mapped on face | (not evidenced) | (not evidenced) |
| Shopping hand-off | brand products "before you buy" (peripheral) | add to basket / Loves / product links | add to cart + pickup/ship | "Buy now" per product |
| Primary motivation | beauty exploration / selfie fun | purchase decision | purchase decision | purchase decision |

### Cross-product commonalities (evidence layer B)

- Capture is always the user's own appearance, via live camera or uploaded photo (all 4).
- Options are organized by beauty category (lips/eyes/face; plus nails at Ulta, hair at YouCam) (all 4).
- The rendered result is anchored to the user's captured appearance — placement computed on the user's face regions (all 4).
- An apply → adjust/compare → (save/share) loop is the interaction core (all 4; adjust/compare evidenced explicitly at YouCam + Maybelline, save/share at YouCam + Sephora).
- Shopping hand-off exists where the operator sells products (Sephora, Ulta, Maybelline); the standalone app keeps it peripheral (YouCam).
- Shade/color matching from a photo or live scan is a common entry path (Sephora color match, Ulta shade finder, Maybelline shade finder, ModiFace Live Scan/Color Match, Perfect Corp shadefinder mode).

### Technology-layer structure (from Perfect Corp / ModiFace docs, evidence layer A for the vendor layer)

- The try-on engine consumes: a capture (image or live feed) + configured product/shade records (SKU, shade name, rendering parameters set via sliders/CMS) → renders the treatment onto detected face regions with color/texture/finish/lighting matching.
- Delivery forms: SDK (custom UI), embeddable widget/miniprogram (no-code), API (async image processing), in-store virtual mirror, standalone consumer app.
- The operator supplies the assortment; the vendor supplies rendering. This explains why the same Type appears as brand-site widget, retailer feature, and standalone app.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The user's captured appearance as the try-on canvas.** The user's own face and face regions (eyes, lips, cheeks, brows), hair, or nails — captured through a live camera or an uploaded photo — is the surface onto which options are rendered. The visualization is anchored to this captured appearance (substituting a stock model photo is a variant, not the center). Remove → a product gallery / swatch viewer.
2. **The beauty-option catalog.** A browsable set of tryable beauty options organized by beauty category — lip, eye, face, nail, hair — each option being a defined visual treatment (a shade, a product, a preset look, a hairstyle) that can be rendered onto the canvas. Remove → a camera-filter app or a plain photo editor.
3. **The apply-preview-adjust loop.** Select option(s) → rendered in place on the captured appearance → adjust intensity/coverage, compare before/after or multiple options side-by-side → save/share the result. The loop exists to answer "how would this look on me" — a shade/style decision or open-ended exploration. Remove → a static lookbook or before/after gallery.

Jointly-held load-bearing:
- 1 alone = photo/gallery viewer
- 2 alone = product catalog / swatch list
- 3 without 1+2 = generic filter playground
- 1+2 without 3 = lookbook with no application
- 1+3 without 2 = generic beauty-filter camera
- 2+3 without 1 = look previews on models (lookbook), not "try on"

### L1 — Common Mature Structure

- live-camera AR rendering with face tracking (modern dominant implementation)
- intensity/coverage adjustment
- before/after and multi-option comparison
- saved looks / favorites; photo/video capture and sharing
- shade/color matching from a photo or live scan (shade finder)
- shopping hand-off (buy now / add to bag / product links) in retail- and brand-operated deployments
- preset full looks alongside individual products
- user guidance for capture quality (lighting, bare face)

### L2 — Variant / Optional Structure

- deployment surface: standalone app / retailer app feature / brand-site widget / in-store mirror / API-embedded in third-party commerce
- option anchoring: real SKU/shade catalog (retail/brand pole) vs generic preset looks and filters (standalone pole) — most products mix both
- category scope: makeup-centric vs multi-category (makeup+hair+nails) vs hair-only or nails-only single-category apps
- motivation: shopping-led vs entertainment/exploration-led
- tutorial overlay mapped on the user's face (Sephora pole)
- makeup transfer from a reference photo (extract a look, apply to own face)
- swatch comparison on a body-part image ("virtual arm")
- stock model photos as substitute canvas

### L3 — Vendor-specific (research notes only)

- Perfect Corp effect schema parameters (vto_type, finish_type; 7 lip textures; foundation glow levels); async task API shape; Camera Kit detection-mode list (ring/wrist/necklace/earring/teeth-whitening modes — non-beauty-face domains served by the same vendor platform)
- ModiFace miniprogram "two lines of code" embedding; per-SKU configuration service; Live Scan / Color Match naming
- Sephora "Loves" list, "My Looks", "virtual arm" naming; 2017-era "4 skin tones" selection
- Ulta GLAMlab brand name; store-pickup integration
- YouCam AI Agent / AI Wardrobe / body tuner / AI image-video generation bundling
- Maybelline "compare up to 4" (product-specific published limit); "Lip Quiz" (3 questions)

## Historical / Market-Sample Check (§24)

Pre-AR generation satisfies the L0 with none of the modern machinery:

- **1997 — Cosmopolitan Virtual Makeover** (SegaSoft/Hearst, desktop software): scanned head shot → test hairstyles, hair colors, eyebrow shapes, eye colors, blushes, eye shadows, lipsticks, including brand-name cosmetics. No AR, no live camera, no purchase integration. ✓ L0 holds.
- **2001 — web makeover sites** (Makeoverstudio.com, iVillage "makeover-o-matic", clairol.com hair color): upload a photo or choose a provided model → experiment with foundation/eye shadow/liner/cheek color/lipstick or hairstyles → save the look in a "Look Book" to reference before shopping in a store. Purchase not integrated. Model-photo substitution already present. ✓ L0 holds.
- **2009 — Daily Makeover Makeover Studio**: upload photo (or model) → face traced by facial recognition → brand-specific shades applied per region → compare brands (Dior vs Lancôme blush) → before-after tab → finishes (matte/satin/metallic…) → adjust placement/coverage → licensed to 60+ beauty brands. Purchase optional: Taaz allowed buying tried products, Daily Makeover did not — purchase is demonstrably not definitional. ✓ L0 holds.
- **2011 — InStyle Hollywood Hair Virtual Makeover**: photo + *manual* face outlining (no automatic tracking) + celebrity hairstyle overlay. Even face detection is not definitional. ✓ L0 holds.

Conclusion: the defining core (captured appearance + beauty-option catalog + apply-preview-adjust loop) predates AR, face tracking, and shopping integration. AR/live tracking, SKU anchoring, and purchase hand-off are era- and deployment-realizations, not invariants.

## Vendor-specific Findings

See L3 above. Notable: Perfect Corp's platform extends the same capture-render machinery to non-beauty domains (rings, wrists, necklaces, earrings, teeth) — evidence that "virtual try-on" is a generic retail visualization pattern and that the *beauty* leaf is defined by its domain binding (face/hair/nails beauty treatments), not by the try-on mechanism alone.

## Boundary Findings

| Neighbor Type | Relationship | Distinction / "remove what to become the other Type" |
|---|---|---|
| Photo Editor / selfie editor | adjacent, often bundled | Photo editing *modifies* the appearance itself (reshape, smooth, whiten); try-on *applies additive beauty treatments* (color/product/style) onto the appearance while preserving identity. Strip the option catalog and keep retouch tools → Photo Editor territory. YouCam Makeup bundles both halves in one app. |
| AI Image Editing / AI Image Generator | adjacent, increasingly bundled | Generative tools synthesize new imagery from prompts/references; try-on overlays *defined* options onto the user's preserved appearance. Makeup-transfer (extract look from reference) sits at the seam but stays anchored to the user's face. |
| E-commerce Platform / Product Discovery | host / hand-off | The try-on surface has no cart, checkout, catalog-of-record, or order flow of its own; purchase is a hand-off ("Buy now", "add to basket"). Remove the appearance anchoring and loop → product discovery/gallery. |
| Beauty Service Marketplace | sibling (§29), different world | No provider population, no bookings, no service fulfillment, no money flow. Confirms the sibling-pass flag. |
| Personal Styling Platform | sibling (§29) | No stylist relationship, no merchandise acquisition, no keep-or-return resolution loop — pure visualization. Confirms the sibling-pass flag ("seam expected clean" — confirmed clean). |
| Salon Management / beauty-professional business apps | sibling (§29), different world | Consumer-facing visualization vs operator-side business system of record (clients, appointments, ledger). |
| Generic virtual try-on (eyewear, watches, jewelry, clothes) | same mechanism, different domain | The mechanism (capture + option catalog + apply loop) is domain-generic (Perfect Corp serves ring/wrist/necklace/clothes with the same platform). This leaf is bound to beauty categories (face makeup, hair, nails). Eyewear try-on belongs to eyewear commerce territory; no directory leaf exists for a generic "virtual try-on platform" — noted as a taxonomy observation, not changed here. |
| Camera filter apps | adjacent | Filters are generic image effects without a browsable beauty-option catalog organized as tryable products/shades/styles; try-on's catalog + decision purpose is the seam. |

## Uncertainties

- Sephora Virtual Artist and Ulta GLAMlab official pages could not be fetched directly (403). Page text was captured via search cache; current live feature sets may differ from the cached text (Sephora text appears long-standing; the 2017 press release is historical). Claims from these two are held at moderate strength.
- Whether Sephora's tutorial-overlay and "virtual arm" features are still current was not verified.
- Ulta's photo/stock-model/live input triad and shade-finder-with-undertone detail rests on one independent hands-on review (Tier 3) — treated as product-specific observation.
- The exact current depth of YouCam Makeup's brand-product integration (vs its generic presets) was not verified inside the app; official listings confirm both exist.
- In-store virtual mirrors (ModiFace mentions) were not researched in depth — recorded as a deployment variant only.
- Regional availability differences (e.g., Maybelline VTO present on GCC/India sites, Amazon.in embedding) suggest deployment varies by market; not systematically mapped.

## Final Synthesis

A Virtual Beauty Try-on Application is a consumer-facing application whose defining core is three jointly-held structures: (1) the user's captured appearance — face/face regions, hair, or nails, via live camera or uploaded photo — as the canvas the visualization is anchored to; (2) a browsable beauty-option catalog organized by beauty category (shades, products, preset looks, hairstyles), each option a defined visual treatment; (3) the apply-preview-adjust loop — select, render in place, adjust intensity, compare before/after or side-by-side, save/share — serving a shade/style decision or exploration. Everything else commonly associated — AR face tracking, SKU anchoring, shade finders, tutorials, shopping hand-off, sharing — is common mature structure or variant, not definition. The historical check (1997 desktop makeover → 2001 web makeovers → 2009 face-traced brand try-ons → 2011 manual-outlining hair try-on) confirms the core without AR, without purchase, and even without automatic face detection. The Type is the consumer-visualization sibling of the §29 beauty-industry block: no providers, no bookings, no money flow of its own; where the operator sells beauty products the try-on ends in a hand-off to that operator's commerce, not in its own transaction.
