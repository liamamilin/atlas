# Research Notes — AI Image Generator

Research date: 2026-09-06
Leaf: AI Image Generator (DIRECTORY §04.20 Generative Visual; siblings: AI Design Generator, AI Image Editing Application)
Slug: ai-image-generator

## Research Goal

Understand what an "AI Image Generator" actually is as an Application Type: what the user provides, what the system produces, how the request→generation→delivery loop works, where the boundary lies against the sibling AI Design Generator and AI Image Editing Application (both flagged this leaf for joint review in STATUS.md), against Model API / open-weights infrastructure, and against image retrieval.

## Initial Boundary (working hypothesis before research)

- Hypothesis: an application whose core is producing new images from user descriptions (primarily text prompts), returning generated image(s) the user reviews, keeps, and can regenerate or adjust.
- Nearest neighbors: AI Image Editing Application (existing image is the object of work), AI Design Generator (design composition with format/purpose semantics as deliverable), AI Video Generator (motion deliverable), Model API Platform / AI Model Hosting (developer-facing, no user application loop), Search Engine / stock imagery (retrieval, not creation), Photo/Raster Editor (deterministic user-driven tools).
- Unknowns at start: whether multiple candidates per request is definitional; how editing coexists with generation; how metering, retention, and safety machinery vary; whether assistant-embedded and search-embedded surfaces satisfy the same structure as standalone generators; whether open-weights/API delivery is in or out of the Type.

## Research Questions

1. What does the user provide as input? (text prompt; reference images; style presets; parameters such as aspect ratio)
2. What is the output — one image, a set of candidates? Is it a flat image or something more structured?
3. What does the post-generation loop look like (re-roll, variation, adjust prompt, edit, upscale)?
4. What surfaces carry the loop (standalone app, assistant conversation, search bar, enterprise platform, API)?
5. How are generations metered (free quotas, credits, subscriptions, rewards) and how are outputs persisted (library, history, retention, delete semantics)?
6. What safety/provenance/account machinery surrounds generation (prompt blocking, reporting, watermarks, content credentials, age/parental controls, regional restrictions)?
7. Where is the boundary to AI Image Editing Application, AI Design Generator, AI Video Generator, Model API Platform, and image retrieval?
8. Do embedded surfaces (assistant, search) and API/open-weights delivery satisfy the same definition as standalone generators?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy | Customer tier | Evidence level |
|---|---|---|---|
| ChatGPT Images (OpenAI) | generation embedded in a conversational assistant; create + edit + library in one surface | consumer, all tiers | Tier-1 (official help-center article, full) |
| Bing Image Creator (Microsoft) | free generator embedded in search/address bar; rewards-metered; heavy responsible-AI machinery | consumer (personal accounts) | Tier-1 (official feature page + FAQ, full) |
| Brand Studio (Stability AI) | enterprise creative-production platform: brand consistency, workflows, precision editing | enterprise/professional teams | Tier-1 (official knowledge base: getting-started + section index) |
| Stable Assistant (Stability AI) | consumer chatbot-style app over the same model family; credit-metered | consumer/creator | Tier-2 (official product page + FAQ) |
| Stable Diffusion 3.5 open weights + Platform API (Stability AI) | model-as-infrastructure: open weights, inference code, developer API | developers / self-hosters | Tier-1 (official GitHub README) + Tier-2 (product pages) |

Market anchors considered but unreachable on the research date (no claims made about their internals): Midjourney (docs transport errors ×2), Leonardo.Ai (timeouts ×2), Ideogram (timeouts ×2), NightCafe (timeout), Canva, Adobe Firefly, Google Gemini image generation, Meta AI.

## Sources

Fetched 2026-09-06:

- OpenAI — "Images in ChatGPT" (Tier-1 help-center article): https://help.openai.com/en/articles/11084440-images-in-chatgpt
- OpenAI — Help Center index / ChatGPT collection (Tier-1 navigation): https://help.openai.com/en/ , https://help.openai.com/en/collections/3742473-chatgpt
- Microsoft — "Bing Image Creator" feature page incl. FAQ (Tier-1): https://www.microsoft.com/en-us/bing/features/bing-image-creator
- Stability AI — "Getting Started with Brand Studio: From First Process to Final Image" (Tier-1 KB article): https://kb.stability.ai/knowledge-base/getting-started-with-brand-studio-from-first-process-to-final-image
- Stability AI — Knowledge Base, Brand Studio section index (Tier-1): https://kb.stability.ai/knowledge-base/brand-studio
- Stability AI — "Stable Image" product page (Tier-2): https://stability.ai/stable-image
- Stability AI — "Stable Assistant" product page incl. FAQ (Tier-2): https://stability.ai/stable-assistant
- Stability AI — homepage (Tier-2): https://stability.ai/
- Stability AI — Stable Diffusion 3.5 official inference repository README (Tier-1, open-weights): https://github.com/Stability-AI/sd3.5

Source-access limitations (recorded per evidence rules; no detail filled from model memory):

- docs.midjourney.com: transport errors on both URL forms → abandoned. The most culturally prominent pure-play generator is under-evidenced at documentation level; no claims about its mechanics.
- leonardo.ai and ideogram.ai: request timeouts ×2 each → abandoned. Production-platform and typography-specialist segments under-evidenced.
- creator.nightcafe.studio: timeout → abandoned. Community-creation segment under-evidenced.
- Bing Image Creator's edit/refine surface is not documented on the fetched page (creation, history, retention, and policy are) → no claims made about Bing-specific refinement mechanics.
- Candidate counts per request are not consistently documented in the reachable layer → no numeric variant-count claims anywhere.

## Product Observations

### ChatGPT Images / OpenAI (evidence layer A — Tier-1 official help article)

- Positioning: "ChatGPT Images lets you create new images and edit existing images in ChatGPT." Available on all tiers; web, iOS, Android; also generable from Codex.
- Creation: "describe the image you want ChatGPT to create" — either in conversation or via select More → Images. Generation "may take a few minutes, depending on the complexity"; user can keep using ChatGPT while it runs.
- Instruction-following inside the image: "can follow instructions to add text, add details within the image, or make the background transparent."
- Editing beside creation: upload an existing image and describe changes; two edit modes — selection tool + describe in chat, or describe the edit directly; an editor with Select (highlight area), Aspect ratio (regenerate at a different ratio), Undo/Redo, Cancel, Save; mobile variant with selection-size slider and Next → describe changes for highlighted areas.
- Vendor-stated limitation: "Highlights are not always precise, and edits may extend beyond the area you selected."
- Any aspect ratio via picker or in-prompt.
- Management: all created images auto-saved under Images; browse/revisit/reuse; image controls Copy / Save (download) / Share to another app; deletion works by deleting the conversation that produced the image.
- Capability embedding: GPTs with the Image Generation capability can use the model; DALL·E GPT retired (replaced by ChatGPT Images).
- Safety/account: content reporting path for policy-violating images; teen accounts have upload reminders and parental controls that can gate image creation/editing entirely.

### Bing Image Creator / Microsoft (evidence layer A — Tier-1 official feature page + FAQ)

- Positioning: "a free AI-powered tool that turns your descriptions into images. Explore different styles of artwork, or upload your own images to personalize what you make."
- Entry surfaces: bing.com/create; typing "create image of.. [idea]" directly in the address bar; a miniapp inside the Bing mobile app; embedded in Copilot Search / Bing Search (sign-in prompted before generating).
- Identity gating: requires a personal Microsoft Account; explicitly unavailable to work/school (Entra ID) accounts. Regional availability excluding Russia and China; 100+ languages supported.
- Prompt education as product surface: extended "Tips and Tricks" — be specific, use adjectives, include action, set the scene, indicate style/mood and lighting — with a worked example upgrading "astronaut" into a detailed prompt.
- Metering: a daily quota of free "fast" creations; beyond it, standard (slower) speed; Microsoft Rewards points can be spent to keep fast speed. (Exact counts on the page are treated as product-specific detail; not promoted.)
- Retention/deletion: creations stored for a bounded period (vendor states up to 90 days); deleting Bing search history deletes the Image Creator profile and history wholesale.
- Responsible AI machinery (detailed): automatic prompt blocking when a potentially harmful image is detected; per-image watermark in a corner; C2PA-based content credentials/provenance on each image; artists/celebrities/organizations can request name/brand restrictions via a Report a Concern form; repeated content-policy violations → temporary suspension → permanent restriction, with an appeal path.

### Brand Studio / Stability AI (evidence layer A — Tier-1 official KB)

- Positioning: "a professional platform for managing your creative work at scale… replaces the guesswork of traditional image generation with a structured way to build assets" around three pillars: Customization (match your brand), Scale (more content faster), Precision (fine-tune every detail).
- Value framing: reduce costs (lifestyle scenes without location shoots), localization (adapt one image across regions/seasons), consistency (own brand assets ensure "every image looks exactly how it should").
- Documented workflow (four stages):
  1. Define Your Aesthetic — Style Preset (e.g., Cinematic, Line Art) + Aspect Ratio matched to destination (9:16 mobile, 16:9 web) set in the sidebar before generating.
  2. Execute Your Process — enter a description of the subject; Personalization menu selects custom tools so specific product SKUs or mascots ("your unique visual DNA") appear in the result.
  3. Refine and Iterate — per-image tools: Re-Roll (different version of the same idea), Edit (adjust settings for specific changes), Variation (similar versions of an image you like).
  4. Finalize for Production — Inpainting to fix small issues at standard size first; Upscale for print/high-resolution; Export from the Library, which "keeps a record of all your settings so you can use them again later."
- Vendor-recommended craft practices: fix-then-upscale ordering; expand the canvas in small increments (~25–50% at a time) for consistent textures/perspective; "Rule of Three" — re-roll at least three times before changing the description to distinguish random glitches from systematic problems; draw masks slightly beyond the target object and feather them for seamless blends.
- Adjacent KB topics: precision editing, six ways to create, style/branding consistency, team collaboration (sharing and editing projects), subscription plans, credit billing.

### Stable Assistant / Stability AI (evidence layer A for product page + FAQ — Tier-2)

- Positioning: "an easy and powerful creation tool" carrying image, audio, and 3D generation and editing; image generation powered by Stable Image Ultra (Stable Diffusion 3.5 Large + advanced workflows), highlighting multi-subject prompts, image quality, and spelling capabilities.
- Generation-adjacent image services demonstrated on the page: Search and Replace, Erase, Inpaint, Remove Background, Replace Background, Search and Recolor, Zoom Out, Enhance, Upscale, Sketch to Image, "New Image with the Same Structure", "New Image with the Same Style", Image to 3D.
- Conversational surface: chat interface (text model alongside) generating images from conversational prompts; public gallery of outputs.
- Metering: credit deduction per usage (FAQ cites per-image and per-message credit costs); subscription with a cancel flow. (Exact credit numbers treated as product-specific detail; not promoted.)

### Stable Diffusion 3.5 open weights + Platform API / Stability AI (evidence layer A for the GitHub README; Tier-2 for product pages)

- Open-weights delivery: models downloadable from HuggingFace (SD3.5 Large / Large Turbo / Medium; SDXL line; SDXL Turbo); MIT-licensed inference-only reference code; text encoders and VAE documented; runs from a CLI: prompt (or prompt file), width/height, steps; images written to an outputs directory named by model/prompt/datetime.
- Conditioned generation: optional ControlNets (Blur, Canny, Depth) guiding structure from an input image.
- Model-family framing on the product page: Large (1-megapixel professional), Turbo (few-step fast), Medium (consumer hardware); "Versatile styles… Prompt Adherence… Diverse Outputs."
- Deployment postures marketed side by side: Self-Hosted License, Platform API ("integrate our models and editing tools into your custom-built applications"), cloud partners, and the web apps (Stable Assistant, Brand Studio).
- API-side image services catalogued on the product page: Edit (erase, inpaint, outpaint, remove background, search-and-recolor, search-and-replace, replace-background-and-relight), Upscale (creative/conservative/fast), Control (sketch, structure, style).
- Note: the model weights + inference code are infrastructure, not an application — no user-facing review loop, no library; this is the Type's outer boundary, evidenced by the vendor's own split into separate offerings.

## Cross-product Comparison

| Dimension | ChatGPT Images | Bing Image Creator | Brand Studio | Stable Assistant | SD3.5 open weights / API |
|---|---|---|---|---|---|
| Driving input | text description in conversation (or Images field) | text description (address bar or site); optional uploaded image to personalize | description of subject + Style Preset + Aspect Ratio + Personalization assets | conversational prompt (chat) | prompt / prompt file (+ ControlNet condition images) |
| Output | generated image(s) in the conversation | generated image(s) per creation | generated images into a project Library | generated images in chat/gallery | image files written to disk / API response |
| Repeat/iterate | regenerate; aspect-ratio regeneration; editor with select+describe, undo/redo | repeat creations (quota-metered); refine surface not documented at fetched layer | Re-Roll / Edit / Variation per image; fix-then-upscale pipeline | regenerate via chat; service-based edits (inpaint, erase, upscale…) | re-run with adjusted prompt/parameters |
| Editing beside generation | yes (first-class editor + conversational edits) | not documented on fetched page | yes (inpainting, masks, precision editing) | yes (broad service catalog) | via API endpoints only |
| Library/persistence | auto-saved Images library; delete via conversation | history with bounded retention; deletion via search-history clearing | Library keeping settings record | gallery + account | local files |
| Delivery | copy / save / share | (retention documented; download not on fetched page) | export/download for production | gallery/download | files / API bytes |
| Metering | tier-based availability | free quota + rewards points for speed | subscription plans + credits | credits per generation/message | license / API pricing |
| Identity/account | personal account; teen parental controls | personal Microsoft Account only (no work accounts) | account login (team collaboration) | account login | HuggingFace download / API keys |
| Safety/provenance | reporting path; parental controls | auto prompt-block; watermark; C2PA credentials; takedown/restriction requests; suspension | (not observed on fetched pages) | (not observed on fetched pages) | (model-level licenses/policies) |
| Surface philosophy | embedded in assistant | embedded in search | standalone enterprise platform | standalone consumer chat app | infrastructure (weights/API) |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three properties. Remove any one and the product stops being an AI Image Generator:

1. **Described visual intent as the driving input** — the user conveys what the picture should show (in words or equivalent description inputs, optionally with supporting images/parameters); the description — not existing artwork being reworked — is the starting point. Remove → AI Image Editing Application (existing image is the object) or an image utility.
2. **Machine-synthesized image as the deliverable** — the system produces new image content that did not previously exist; the output is a picture, not a composition to be further assembled. Remove → image retrieval/search (existing pictures) or deterministic image utilities.
3. **Interactive request-and-review loop** — a user-facing surface where the user requests a generation, inspects the returned image(s), and can request more or adjusted ones (re-run, vary, tweak the description) until they keep one. Remove → model API / open-weights inference (developer infrastructure with no user loop) or a one-shot demo.

Notes:
- "Machine-synthesized" is about structure (system creates content from the description), not about a specific model technology. Neural networks are the current implementation; the definition does not require them by name.
- The image (not a design composition) is the deliverable — this is the load-bearing difference from the AI Design Generator sibling.
- No requirement about: cloud delivery, natural-language-only input, candidate counts, editing tools, style presets, subscriptions, or any specific safety mechanism.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B unless noted):

- repeat generation as the core loop refinement: re-roll, variations, regenerate at a different aspect ratio (A in Brand Studio Re-Roll/Variation, ChatGPT aspect-ratio regeneration; Bing's quota-metered repeated creations; Stable Assistant per-credit generations)
- generation parameters surfaced to the user: aspect ratio (A ChatGPT, Brand Studio; A GitHub width/height), style presets (A Brand Studio; Bing "explore different styles of artwork")
- prompt education/aids: tips, worked prompt examples (A Bing; A Brand Studio workflow guidance)
- image input as a generation ingredient: upload to personalize what you make (A Bing); reference images for structure/style/sketch (A Stability services and ControlNets)
- post-generation editing beside generation: conversational or selection-based edits, inpainting, erase, upscale, background operations (A ChatGPT editor, Brand Studio pipeline, Stable Assistant services) — common in the current generation but not required (Bing's documented surface is creation-centric)
- persistent creations: auto-saved libraries/history with revisit/reuse (A ChatGPT, Brand Studio, Stable Assistant gallery, Bing history)
- delivery paths: download/save/copy/share/export (A ChatGPT, Brand Studio, Stable Assistant)
- metered economics: free allowances, quotas, credits, subscriptions (A Bing, Stable Assistant, Brand Studio; tier gating A ChatGPT)
- account/identity gating with population restrictions (A Bing consumer-account-only; A ChatGPT teen controls)
- safety and provenance machinery: prompt blocking, reporting, watermarks, content credentials, restriction requests, suspension (A Bing; reporting/parental A ChatGPT) — direction consistent across the sample, implementation depth varies (B)
- production-quality workflow advice from the vendor itself: fix-then-upscale, incremental expansion, multi-reroll before prompt changes (A Brand Studio)
- text-in-image as a claimed capability, with quality varying (A ChatGPT "add text"; A Stable Image Ultra "spelling capabilities"; sibling research documents vendor warnings that in-image text may be misspelled) — common capability, calibrated expectation

### L2 — Variant / Optional Structure

- delivery surface: standalone site/app, embedded in an assistant conversation, embedded in search/address bar, chatbot app, enterprise platform, developer API, open-weights self-host
- model posture: proprietary hosted model, open weights, multi-model catalogs
- input modality: free-text prompt, conversational turn-taking, structured fields (style preset + ratio + personalization assets), image-conditioned generation (sketch/structure/style)
- candidates per request: single image vs small sets — varies by product; not definitional
- editing depth beside generation: creation-only surfaces vs full edit pipelines (inpaint/outpaint/upscale/background ops)
- personalization machinery: brand assets, product SKUs, mascots injected into generations
- retention/delete semantics: bounded retention vs conversation-linked persistence vs project libraries with settings records
- metering mechanics: daily quotas, points economies, credits, subscriptions, enterprise contracts
- regional/account restrictions and language coverage
- adjacent bundled modalities: audio, 3D, video (suite bundling, not Type merger)

### L3 — Vendor-specific (research notes only)

- Bing Image Creator: 15 free fast creations/day with Rewards-points continuation; 90-day storage; address-bar invocation phrase; unavailability to Entra ID accounts and in Russia/China; corner watermark + C2PA per image; Report-a-Concern restriction requests for artists/celebrities/brands; content-policy suspension ladder; coupling with Bing Video Creator settings.
- ChatGPT Images: "Images 2.0" naming; "Images with thinking" tier gating (Plus/Pro/Business, Enterprise/Edu pending); delete-image-by-deleting-conversation semantics; GPT capability toggle for image generation; DALL·E GPT retirement; Codex integration; teen upload reminders.
- Brand Studio: named Style Presets (Cinematic, Line Art); Personalization menu (Atom icon) for SKUs/mascots; "Rule of Three"; 25–50% incremental expansion guidance; mask feathering recommendation; Library settings-record reuse; six-ways/precision-editing KB series.
- Stable Assistant: 6.5 credits per successful image / 0.1 per message (FAQ); Stable Image Ultra branding; Image-to-3D; Stable LM 2 12B chat companion.
- SD3.5 repo: MIT code license; CLIP-L/OpenCLIP bigG/T5-XXL text encoders; MM-DiT architecture; blur/canny/depth ControlNets; outputs/<MODEL>/<PROMPT>_<DATETIME>_<POSTFIX> naming; --skip_layer_cfg option.

## Historical / Market-Sample Check

- The Type is young in its current form (diffusion-era, ~2022+), so the "older product" check has limited reach, but three older/adjacent patterns were tested against the L0:
  - **Random/curiosity image demos** (single-purpose "a face that does not exist" sites): no described user intent — the user requests nothing specific; fails L0 property 1 → a demo, not this Type.
  - **Pre-neural procedural/art generators** (parameter-driven scene or pattern makers): user conveys intent through structured parameters rather than prose; satisfies L0 properties 2–3 if the system synthesizes pictures the user reviews and keeps. The L0 deliberately requires described intent, not natural language specifically — these edge cases are recorded as observations, not core-shapers.
  - **Image search / stock libraries**: the user wants a picture but retrieval returns existing images; fails L0 property 2 → Search/retrieval Types. Bing's own docs explicitly distinguish creation from "searching for an image or video on Bing."
- Regional/platform check: a search-embedded consumer tool (global minus two markets), an assistant-embedded product, an enterprise platform, and self-hosted open weights all satisfy the L0; no region- or platform-bound feature entered the core.
- Model-technology check: the core is phrased by structure (described intent → synthesis → review loop), not by diffusion/transformer specifics, so future or alternative synthesis methods remain inside the Type.

## Rejected Findings

- **"Multiple candidates per request is definitional"** — rejected: ChatGPT's documented behavior is one image per prompt; Brand Studio documents per-image tools. Repeat/re-roll is the universal loop element; per-request batch size is a product choice (variant).
- **"A standalone prompt page is definitional"** — rejected: two of the sampled products embed generation in other surfaces (a conversation, a search/address bar); the loop survives embedding intact.
- **"Post-generation editing is definitional"** — rejected as an invariant: the strongest documented creation-centric surface (Bing, at the fetched layer) documents no editor. Editing is common mature structure, and heavy editing is the sibling Type's core.
- **"Style presets/aspect ratio pickers are definitional"** — rejected: they are common parameter surfaces; a bare text prompt satisfies the Type (GitHub CLI evidence).
- **"Free tier is definitional"** — rejected: enterprise platforms and API/credit products monetize every generation; what is common is metered economics, not free access.
- **"Natural-language prompts are definitional"** — rejected: prompt files and structured parameter inputs satisfy the described-intent property; prose is the dominant implementation, not the requirement.
- **"Open-weights delivery means the model, not the application, is the Type"** — rejected as a boundary claim against the leaf: the Type is the application surface; weights/API are the infrastructure edge. The vendor itself ships the same model family as an API, two applications, and open weights — three different products, one of which (the app surfaces) is this Type.

## Boundary Findings

1. **vs AI Image Editing Application (04.20 sibling)** — the discriminator is the object of work: a description from which an image is created vs an existing image that is changed. In the researched sample the two loops cohabit freely: ChatGPT Images does both under one roof (create + upload-and-describe-edits); Stability splits them across services (generation on one side; erase/inpaint/background ops catalogued as "editing"); Bing supports upload-to-personalize within a creation-centric surface. Structural test: remove the described-intent starting point → editing application remains; remove the source-image requirement → generator remains. Both siblings' pending flags are hereby addressed from this side: the boundary is the object of the first operation, a gradient with heavy bundling, not a wall (resolves research/ai-design-generator.md finding 1 and research/ai-image-editing-application.md finding 1 as seen from this leaf).
2. **vs AI Design Generator (04.20 sibling)** — deliverable class: the picture itself is the final artifact vs a design composition (arranged elements + text + format-for-purpose semantics) that stays workable as a design. The researched generators deliver images into libraries/galleries; none documents composition semantics (text boxes, layout, purpose-formats) — Brand Studio, despite brand/consistency machinery, still delivers images (with presets/ratios as generation parameters, not design formats). Structural test: remove design-composition/format-for-purpose semantics → image generator remains; keep them → design generator. Gradient; consistent with the design-generator research's finding 1.
3. **vs Model API Platform / AI Model Hosting (§13)** — a user-facing request-and-review loop vs developer-facing inference endpoints. Stability ships both as separate offerings (Platform API vs Stable Assistant/Brand Studio), and the open-weights repo is explicitly a reference implementation for partner organizations. Clean split at the user-surface level; the API and weights are the Type's outer boundary, not the Type.
4. **vs image retrieval (Search Engine / stock libraries)** — synthesis vs retrieval. Conceptually clean; packaged adjacently (Bing embeds creation inside search and contrasts it with image search in its own docs).
5. **vs AI Video Generator (04.21)** — static image vs motion deliverable. Same vendor evidence: Bing maintains Image Creator and Video Creator as separate features with separate settings; Stable Assistant bundles image-to-3D and audio beside images (suite bundling, not Type merger).
6. **vs Photo Editor / Raster Image Editor (04.04/04.02)** — who produces the change: the system synthesizing from description vs the user driving deterministic tools; consistent with the ai-image-editing-application research's finding 2.
7. **Capability-embedding pattern** — the generation loop appears standalone (Brand Studio, Stable Assistant), embedded in an assistant (ChatGPT), embedded in search (Bing), behind an API (Stability Platform), and as open weights for others to wrap (GitHub). Standalone vs embedded is packaging, not structure; the leaf is defined surface-agnostic.
8. **Taxonomy note** — the market phrase "AI image generator" names both the model capability and the application surface; product homepages routinely mix creation, editing, and gallery features under one name. The leaf is defensible as the creation-loop-centered application Type within 04.20; the load-bearing boundaries are findings 1 and 2, both gradients.

## Uncertainties

- Midjourney, Leonardo.Ai, Ideogram, NightCafe (and, from sibling passes, Canva, Adobe Firefly, Google Gemini) were unreachable → the pure-play consumer/creator segment — culturally the most prominent — is under-evidenced at documentation level. No claims are made about their mechanics. The L0/L1 were phrased to be segment-agnostic (e.g., community features, parameter controls, and Discord-style surfaces are not required by the core).
- Bing Image Creator's refine/edit capabilities are not documented at the fetched layer; editing is asserted as common from the other three application surfaces, and no Bing-specific editing claims are made.
- Candidate counts per request, credit costs, quotas, and retention windows are product-specific and change over time; the reachable-layer numbers live in the L3/vendor-specific notes only.
- Whether every market product pairs a library/history with the loop is unverified beyond the sample; persistence is documented in four of five sampled surfaces and is treated as common, not definitional.
- The precise line between "generation with reference images" and "editing" (image-conditioned synthesis vs changing an existing image) is inherently fuzzy at the product level; the structural test in Boundary Finding 1 is the working discriminator.

## Final Synthesis

An AI Image Generator is an application in which the user describes the picture they want, the system synthesizes new image content from that description, and the user reviews the result and continues — re-rolling, varying, adjusting the description, editing, or accepting — until an image is kept and delivered. The defining core is deliberately small: described visual intent, machine-synthesized image as deliverable, interactive request-and-review loop. Everything else familiar in the market — repeat/re-roll, aspect ratios and style presets, prompt education, reference-image conditioning, post-generation editing, libraries and history, delivery paths, metered economics, account gating, safety and provenance machinery — is common mature structure; delivery surface (standalone, assistant-embedded, search-embedded, enterprise platform), model posture (proprietary, open weights), input modality, candidate counts, metering mechanics, retention semantics, and adjacent modalities are variants. The load-bearing boundaries are against the AI Image Editing Application (object of work: description vs existing image) and the AI Design Generator (deliverable class: the picture itself vs a workable design composition); both are gradients with heavy real-world bundling, and both pending sibling flags are resolved from this side. Against Model API/open-weights infrastructure the boundary is clean: no user-facing request-and-review loop, no Type.
