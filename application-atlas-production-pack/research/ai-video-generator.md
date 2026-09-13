# Research Notes — AI Video Generator

Research date: 2026-09-06
Leaf: AI Video Generator (DIRECTORY §04.21 Generative Video)
Slug: ai-video-generator

---

## Research Goal

Understand, from real products, what an AI Video Generator is: what the user actually provides, what the system generates, what the generation unit and its parameters are, how the iterate-to-quality loop works, how outputs are organized and delivered, which rules (metering, moderation, provenance, ownership) govern the Type, and where the boundary lies against the sibling Types under Generative Video (AI Avatar Video Generator, AI Video Editing Application) and against AI Image Generator, Video Editor, and Motion Graphics.

## Initial Boundary

Initial hypothesis (to be tested): an application that produces novel video footage from user descriptions — a text prompt, optionally conditioned on images or other references — where the moving imagery did not exist before generation. The deliverable is a generated video clip; the core loop is describe → generate → review → refine/regenerate.

Most likely confusions:

- AI Avatar Video Generator (sibling, 04.21) — presenter performing authored speech vs imagined scenes
- AI Video Editing Application (sibling, 04.21) — transforming existing footage vs creating footage
- AI Image Generator (04.20) — still images vs moving footage
- Video Editor / NLE (04.06) — timeline manipulation of existing footage
- Motion Graphics Application (04.07) — user-animated designed graphics vs model-synthesized footage
- AI Music/Audio Generator (04.22) — audio-only deliverables

Known fuzziness going in: generation products increasingly bundle editing of generated output, image generation, audio generation, and assembly timelines; avatar products add generated scenes; editing products add generation. The boundary must be drawn on the center of gravity, not on feature presence.

## Research Questions

1. What is the input (text prompt, image, first/last frame, reference images, audio)? What is the canonical concept behind these input modes?
2. What is the generation unit (clip/shot/scene) and which parameters surround it (aspect ratio, resolution, duration, model)?
3. What does the iterate-to-quality loop look like (regenerate, variations, prompt refinement, upscale)?
4. How are outputs organized (sessions, projects, assets, libraries) and delivered (download, share, community, API)?
5. How is a "video" longer than one clip produced (extension, multi-shot assembly, storyboards)?
6. How is generation metered and priced (credits, model-dependent cost)?
7. Which rules matter (content moderation, provenance/watermarking, ownership/licensing, model governance)?
8. How do models themselves appear as objects (model catalogs, model switching, third-party model aggregation, open weights)?
9. Where is the boundary against AI Avatar Video Generator, AI Video Editing Application, AI Image Generator, Video Editor? Does the leaf hold as an independent Type?

## Representative Products

| Product | Why selected | Evidence actually obtained |
|---|---|---|
| Runway | Professional creative platform; mature help center; multi-model posture | Yes — help center root, Getting Started, Generative Video guide, Sessions, Text-to-Video Prompting Guide, Agent article, aspect-ratio/resolution FAQ, commercial-use FAQ (evidence layer A) |
| Google Veo | Platform-embedded model (Gemini app, Flow, Vids, API); filmmaker positioning | Yes — DeepMind Veo model page incl. capabilities, safety, limitations, production integrations (layer A, Tier 2 model/product page; developer docs hosts unreachable) |
| Kling AI (Kuaishou) | China-origin creator platform with international version; consumer + developer split | Yes — klingai.com product/dev site + official usage-guide table of contents (feature structure confirmed; article bodies JS-gated) |
| LTX (Lightricks) | Open-weights philosophy; developer + studio + local deployment | Yes — help center root incl. FAQ (access points, open-source licensing, positioning) (layer A) |
| Hailuo AI (MiniMax) | Consumer template-driven posture; regional (China) vendor with international site | Yes — product site (entry surfaces, Omni reference, template gallery, community feed) (layer A, Tier 2) |

Sample rationale: professional creative platform (Runway) + platform-embedded model (Veo) + regional creator platform (Kling) + open-weights challenger (LTX) + consumer template app (Hailuo). Different philosophies, customer tiers, and geographies.

Market-churn note: **OpenAI Sora was discontinued** — the Sora web and app experiences ended April 26, 2026, and the Sora API is scheduled to end September 24, 2026 (OpenAI Help Center, "What to know about the Sora discontinuation", accessed 2026-09-06). Sora therefore could not serve as a representative product; the discontinuation is recorded as evidence that product turnover in this category is high and that docs-based claims must be anchored to living products.

## Sources

All fetched 2026-09-06.

- Runway Help Center — https://help.runwayml.com/ ; key articles: Getting Started with Generative Video (/hc/en-us/articles/37425232841875), Generating with Sessions (/hc/en-us/articles/33545310653203), Text to Video Prompting Guide (/hc/en-us/articles/42460036199443), Creating with Runway Agent (/hc/en-us/articles/51601639579667), Changing the aspect ratio and resolution (/hc/en-us/articles/26113483666451), Can I use the content I made in Runway for commercial purposes (/hc/en-us/articles/21668707517587)
- Google DeepMind — Veo model page — https://deepmind.google/models/veo/ (capabilities: ingredients, style reference, character consistency, extend, camera controls, first/last frame; performance; safety incl. SynthID; limitations; Try-Veo surfaces; production integrations)
- Kling AI — https://klingai.com/ (creation tools nav, dev platform nav, Video 3.0 / 3.0 Omni announcement) + 可灵AI使用指南 (official usage guide) — https://docs.qingque.cn/d/home/eZQBGvsEtlGCz5-IhhQP3S-eM (table of contents only; article bodies require JS)
- LTX Help Center — https://support.ltx.studio/hc/en-us (FAQ: what is LTX, access points, open-source licensing, positioning)
- Hailuo AI (MiniMax) — https://hailuoai.video/ (entry surfaces, H3 announcement, Omni Reference, template gallery, community feed, AI-content notice)
- OpenAI Help Center — https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation (Sora sunset)

Access limitations:

- **OpenAI platform docs** (platform.openai.com/docs/guides/video-generation) — 403; Sora app discontinued anyway; abandoned.
- **Google developer docs** (ai.google.dev/gemini-api/docs/video — 2 timeouts; cloud.google.com Vertex video docs — timeout) — Veo evidence rests on the DeepMind model page; API-side operational details unverified.
- **Luma** (docs.lumalabs.ai transport error; lumalabs.ai timeout) — abandoned after 2 failures.
- **Pika** (pika.art timeout) — abandoned.
- **Kling usage-guide article bodies** — JS-gated; only the table of contents was readable. Feature existence confirmed; operational details (credits, limits) not obtained.
- **Adobe Firefly** (adobe.com timeout) — not pursued; enterprise-suite-embedded posture left as an unverified variant.

---

## Product A — Runway (help center, evidence layer A)

- **Positioning**: "a research organization that builds generative AI tools … bleeding-edge generative video products and tools." Four generation modes: **Tools** (traditional interface, precise control over inputs/settings), **Apps** (optimized per-use-case experiences, reducing manual prompting), **Agent** (AI creative partner producing complete multi-shot videos through conversation), **Workflows** (node-based editor for automated, customized, scalable creative pipelines).
- **Sessions**: organizational structure that keeps outputs organized as you generate; "exceptionally useful when iterating on a specific style, scene or shot"; auto-named from the first prompt; session list shows 30 most recent; full library under Dashboard → Sessions; rename; share with workspace/team (view generations and prompts); delete (assets survive, sessions unrecoverable). **Projects** add another layer: organize assets, sessions, and workflows per creative effort.
- **Models as objects**: Gen-4.5 (most advanced; Text to Video + Image to Video), Gen-4 / Gen-4 Turbo (older, faster, cheaper credits); model switcher in Tools mode. Agent FAQ: "Agent picks the best model for each task automatically — including Gen-4.5, Seedance 2.0, Kling, Veo, and others. Prefer a specific model? Just ask." Enterprise: only admin-enabled models. → **Runway aggregates third-party video models (Kling, Veo, Seedance) alongside its own.**
- **Prompting (Text to Video)**: prompts describe **what appears** (visual components: subject appearance, environment, lighting, composition/framing, style) and **how elements move** (motion components: subject action, environmental motion, camera motion, motion style & timing, direction & speed). Recommended structure: "[Camera] shot of [subject/object] [action] in [environment]. [supporting descriptions]". Natural language gives more control than keywords; no ideal length; order does not matter. **Timestamp prompting** sequences actions ("[00:02 through 00:03] rapidly crash zoom…"). Iteration is normal: "Iteration is a normal part of the process when working with generative media, much like the drafting phases of other creative processes." Reinforce missing components by iterating the prompt.
- **Image to Video**: upload an image + prompt describing **motion only** ("You do not need to describe the contents of the image"). T2V vs I2V guidance: T2V for B-roll/stock effects/background plates when consistency isn't the priority; I2V constrained to a starting scene; T2V handles complex motion better.
- **Generation parameters**: aspect ratio selectable on the generation canvas before generating (model-dependent); generative video outputs 720p, **upscaleable to 4K** via an Upscale option under the completed generation; no numeric pixel-size customization. Agent generates 480p/720p/1080p depending on model/quality; "iterate at 720p to save credits, then upscale your final version."
- **Iterate loop**: click **Generate** → processing → generations scrollable in the session; **Use** under a completed generation opens continuation options; or adjust the prompt and regenerate.
- **Agent** (chat-based collaborative agent): analyzes inputs (product, image, ad campaign, idea); plans, produces, scales entire creative projects; picks the best model per step. Generates images, video (T2V/I2V, single or multi-shot, with/without native audio per model), audio (SFX, ambience, foley, dialogue scenes), music, voiceover. Edits video (restyle, change environments/seasons/lighting, swap elements while preserving motion/framing), edits images, and assembles timelines. Creates reference sheets, storyboards, mood boards, character sheets, scripts; diagnoses failing prompts. **Generation mode**: ask-before-generating (shows plan: model, prompt, estimated credit cost) vs auto-generate. **Model-selection preference**: optimize for speed / cost / quality / custom natural-language instructions. Multi-shot videos auto-combine in the **Final Cut** tab (timeline editor: split, trim, track volume, add tracks, undo/redo). Generations tab grid with filters. Agent Skills: ready-made workflows ("/" triggers, e.g. Ad Campaign, Mood Board). No hard duration limit; clips longer than the model's limit generate separately and are auto-assembled. Voice input on mobile. Honest framing: "generating media is inherently variable — Agent's plan describes its intent, not a guaranteed outcome… results may require iteration."
- **Commercial/ops**: generations use credits; costs vary by model and output type. Ownership: "the content you create using Runway is yours to use without any non-commercial restrictions… you retain ownership and all your rights"; no attribution required. Community: share work with team or have it featured to the community. Dev portal, MCP, mobile apps.

## Product B — Google Veo (DeepMind model page, evidence layer A, Tier 2)

- **Positioning**: "Our leading video generation model… Generate cinematic video with audio… designed to empower filmmakers and storytellers." Veo 3.1: "Video, meet audio" — native audio generation (sound effects, ambient noise, dialogue) "generating all audio natively"; strengths in physics, realism, prompt adherence.
- **Capabilities**:
  - **Ingredients/reference images**: "giving Veo reference images of a scene, a character, or an object to guide its generation. Now includes audio."
  - **Style reference**: provide a style reference image; Veo generates videos with the same visual style ("from paintings to cinematic looks").
  - **Character consistency**: reference images of a character maintain appearance across scenes.
  - **Extend**: "Extend clips into longer, more dynamic videos. Use the last second of your first shot to continue the story — while maintaining visual and audio consistency" (multi-prompt continuation example: dancer → partner joins → more dancers → music continues).
  - **Camera controls**: "Precisely control the framing and exact movement of shots" (move back, zoom in, move up, move right).
  - **First and last frame**: transitions between images provided as first and last frame.
- **Performance**: text-to-video, image-to-video, text-to-audio+video, realistic physics; "Professional grade resolution: 1080p and 4K."
- **Safety**: "videos made with Veo will be marked with SynthID, our advanced technology for watermarking and detecting content generated by AI. Additionally, Veo outputs will undergo safety evaluations and checks for memorized content to reduce potential issues related to privacy, copyright infringement, and bias." Harmful requests/results blocked; internal + external red-teaming.
- **Limitations** (vendor-stated): "creating videos with natural and consistent spoken audio, particularly for shorter speech segments, remains an area of active development."
- **Surfaces**: Try in Gemini (gemini.google.com/veo), Try in Google Flow ("An AI filmmaking tool built with and for creatives… create seamless cinematic clips, scenes, and stories"), Google Vids ("AI-powered video creation for work"), AI Studio (veo_studio app), Build with Veo (Gemini API). → one model, many delivery surfaces.
- **Production integrations**: Promise (MUSE platform — generative storyboarding/previsualization), Volley (game cinematics), OpusClip (Agent Opus — motion graphics/promotional videos); Primordial Soup partnership (integrating live-action footage with Veo-generated video; three short films).

## Product C — Kling AI (Kuaishou) (product site + usage-guide TOC, evidence layer A-)

- **Positioning** (klingai.com): "Next-Gen AI Video & Image Generator"; creation tools: 可灵 Omni, AI视频, AI图片, AI音效 (AI sound effects), 创意特效 (creative effects), 更多创意工具; separate 开发者平台 (developer platform: pricing, API docs center, usage guide).
- **Model series** (announcement): 可灵视频 3.0 and 3.0 Omni — "native multimodal instruction parsing and cross-task fusion"; long-video shot division (分镜); audio-visual sync ("视觉主体与听觉音色的双重绑定").
- **Usage-guide structure** (TOC): 如何更好地生成视频 — model guides (Video 3.0, 3.0 Omni, O1, 2.6 「音画同出」 audio-video co-generation); **基础功能**: 文生视频 (text-to-video), 图生视频 (image-to-video), 多图参考 (multi-image reference); **进阶功能**: 首尾帧能力 (first/last frame), 数字角色2.0 (digital character), 动作控制 (motion control), 对口型 (lip sync), 运镜控制 (camera movement control). Image side: text-to-image, character-feature/face reference, style transfer, generic reference, multi-image reference, image editing, virtual try-on.
- **Community**: creator exchange groups, official video channel for feature intros and "优质作品分享" (quality work sharing); GitHub (Kolors).
- Interpretation: same structural vocabulary as Western products (T2V/I2V/references/first-last-frame/camera control/lip sync) plus a strong creator-community layer and a separate developer platform. Article bodies JS-gated; operational details not obtained.

## Product D — LTX (Lightricks) (help center, evidence layer A)

- **What it is**: "LTX is Lightricks' AI video generation platform — built around LTX-2.3, an open-source foundation model for cinematic video generation. It supports text-to-video, image-to-video, audio-to-video, and more, at up to 4K resolution."
- **Access points** (explicitly enumerated): **open model weights** (self-hosted, custom, research deployments, "full control over how you run and extend the model"), **LTX API** (developers integrate generation into products/pipelines), **LTX Studio** (browser-based platform for filmmakers and creative teams — "Create, storyboard, and produce films, ads, and more in our full creative platform"), **LTX Desktop** (runs the full model locally, no cloud), **LTX Playground** (no-setup trial).
- **Open source**: weights, code, tooling on Hugging Face + GitHub; free for most purposes; **commercial license required if the company generates over $10M annual revenue**.
- **Positioning vs market**: "Most AI video tools are closed, cloud-only, and API-locked. LTX is different in three ways: the underlying model is open source; you can run it locally or on your own infrastructure; and it's designed for production workloads, not just demos. That makes it a practical choice for teams with strict data, compliance, or customization requirements."
- **LTX Trainer**: LoRA training (custom model adaptation). API Console for developers.

## Product E — Hailuo AI / MiniMax (product site, evidence layer A, Tier 2)

- **Positioning**: "MiniMax H3 LIVE NOW. Top-Tier Quality, Versatile References"; "Native multimodal generation, precise multimodal editing, production-ready content creation."
- **Entry surfaces**: Create Video, Create Image, **Hailuo Agent**; generation panel with **Refs (0/1) Omni Reference** (reference-based conditioning).
- **Template gallery**: photo-to-video templates (dance videos, transformations, K-pop idol MVs, cinematic scenes, broadcast close-ups), AI ad generator, style transfer, ASMR generator, pet/baby/funny variants — consumer-oriented packaged generation.
- **Community feed**: Trending with public view counts; "The content is generated by AI. Please use this feature legally and in a friendly manner" (usage notice).
- Sibling products: MiniMax Audio, MiniMax Design — separate tools.

## Cross-product Comparison

| Dimension | Runway | Google Veo | Kling AI | LTX | Hailuo (MiniMax) | Reading |
|---|---|---|---|---|---|---|
| Central input | text prompt; image + motion prompt (I2V) | prompt; ingredients/style/character reference images; first/last frame | text; image; multi-image reference; first/last frame | text; image; audio-to-video | prompt; Omni Reference; photo templates | **described intent is universal; conditioning inputs vary and multiply** |
| Generation unit | generation (clip) inside a Session; multi-shot assembled in Final Cut | clip; extend from last second; scenes/stories in Flow | clip; 分镜 shot division in 3.0 | clip up to 4K; storyboard→film in Studio | clip; template packages | **clip is the unit; longer works are assembled from clips** |
| Model as object | model switcher (Gen-4.5/Gen-4/Turbo); Agent picks among Gen-4.5, Seedance, Kling, Veo | one model family (3.1) exposed via many surfaces | model series (3.0, 3.0 Omni, O1, 2.6) | LTX-2.3 open weights + Trainer (LoRA) | H3 | **model catalog with cost/quality/speed tradeoffs is structural; aggregation of third-party models emerging** |
| Iterate loop | regenerate; "Use" to continue; prompt reinforcement; iterate at 720p then upscale | regenerate; extend; camera-control adjustments | regenerate (implied by guides) | playground iteration | regenerate; template re-runs | **iteration as normal drafting, stated explicitly by Runway** |
| Parameters | aspect ratio (model-dependent), 720p→4K upscale | 1080p/4K; camera controls | camera movement control; motion control | up to 4K | (not detailed) | **aspect ratio/resolution/duration are generation parameters, model-dependent** |
| Audio | native audio per model; Agent generates SFX/ambience/dialogue/music/voiceover | native audio (dialogue/SFX/ambience); spoken-audio limitation stated | 2.6 音画同出 (audio-video co-generation); AI音效 tool; 对口型 lip sync | audio-to-video input | ASMR template | **native audio co-generation is a newer common capability, not yet universal** |
| Organization | Sessions → Projects → Assets | (Flow scenes/stories) | creator library | projects in Studio | Mine (library) | **persistent output libraries with grouping structures are common** |
| Metering | credits; cost varies by model/output; iterate-cheap-then-upscale guidance | (API pricing; not fetched) | dev pricing page | API console; open weights free/<$10M license | subscription (From $/mo) | **metered generation universal; unit economics product-specific** |
| Delivery | download; share to workspace; community featuring | Gemini/Flow/Vids/API surfaces | creator community; dev platform | download/API/self-host | download; public trending feed | **download + share universal; public showcase common in consumer products** |
| Safety/provenance | (terms; community guidelines) | SynthID watermarking; safety evaluations; memorized-content checks | usage notice (Hailuo analog) | license terms | "use legally and in a friendly manner" notice | **provenance marking and moderation are structural where evidenced; depth varies** |
| Agent/conversational | Agent (plan → generate → Final Cut) | (Flow as filmmaking tool) | — | — | Hailuo Agent | **conversational orchestration emerging across vendors** |
| Openness | closed cloud | closed cloud (multi-surface) | closed cloud + GitHub (Kolors image model) | **open weights + local + API** | closed cloud | **deployment openness is a variant axis, not the definition** |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Described Intent (prompt; optionally conditioned on images/references)
└── Model-Synthesized Footage
    (moving imagery generated by the system — did not exist before)
    └── Generated Video Clip as Deliverable
```

Three properties, deliberately minimal:

1. **Described intent** — the user describes what the video should show (text prompt; optionally with conditioning inputs such as an image, reference images, or first/last frames). The description exists before the video and drives generation. Without it — if the user supplies footage to be transformed — the product is an editor, not a generator.
2. **Model-synthesized footage** — the application generates moving imagery that did not previously exist. This is the defining "generation" step: nothing was filmed or drawn by the user. Without it, the product is an editor or a player.
3. **Generated video clip as deliverable** — the output is a video clip (downloadable file or streamable result), short-form by nature; longer works are assembled from clips. Without it — if the output is a still image — the product is an image generator; if the output is a live session, it is a different surface.

Deliberately NOT in L0 (tested against the historical/market-sample check):

- **Review-and-regenerate loop** — the dominant workflow, but a one-shot API generation (prompt in, video out) still satisfies the definition; the loop is how the Type is used, not what it is. (Contrast: the AI Video Editing Application, where the review loop is definitional because editing without review is a batch converter.)
- Text-to-video specifically — image-to-video, multi-image reference, and audio-conditioned generation are all the same concept (described intent + conditioning) at different implementation points.
- Native audio, 4K, camera controls, credits, communities, agents — all modern common structure, none required.

Historical / market-sample check: early research-grade text-to-video tools, prompt-to-short-clip toys, and API-only render endpoints all satisfy the three properties while lacking sessions, credits, communities, agents, and audio. Regional products (Kling's China service) and open-weights deployments (LTX self-hosted) satisfy them without cloud services. Removing any property breaks the Type: remove described intent → editing/analytics; remove synthesis → editing; remove the video deliverable → image generation.

### L1 — Common Mature Structure

Present in most mature modern products; not required to recognize the Type:

- **Prompting craft as documented practice** — official prompting guides describing visual components (subject, environment, lighting, framing, style) and motion components (action, environmental motion, camera motion, timing); camera-terminology vocabularies; timestamp prompting for sequencing; guidance that iteration is a normal drafting phase.
- **Conditioning inputs** — image-to-video (animate a still), first/last-frame interpolation, reference images for characters/scenes/objects/style, multi-image reference.
- **Generation parameters** — aspect ratio, resolution (with post-hoc upscaling), duration; availability model-dependent.
- **Model catalog** — multiple generation models with cost/quality/speed tradeoffs; explicit model selection; third-party model aggregation in platform products; enterprise model governance.
- **Iterate-to-quality loop** — regenerate, refine the prompt, continue from an output ("Use"), iterate at low cost then upscale the final.
- **Continuation and assembly** — extend a clip from its final moment; multi-shot sequences auto-assembled into a cut; storyboard/scene-level organization for longer narratives.
- **Output management** — persistent libraries with grouping structures (sessions/projects/assets); sharing within teams.
- **Metered generation** — credits or subscription consumption; cost varies by model and output type.
- **Delivery** — download, share links, embeds; public community showcase/trending in consumer products.
- **API access** — programmatic generation (submit, poll/webhook, retrieve) for developer-oriented products.
- **Native audio co-generation** — dialogue, ambient sound, effects, music generated with the picture (newer models; not yet universal).
- **Safety and provenance machinery** — content moderation, AI-content notices, provenance watermarking (where evidenced), usage policies.
- **Conversational agent orchestration** — chat-based planning, multi-step generation, timeline assembly (emerging; present in 2 of 5 sampled products).

### L2 — Variant / Optional Structure

- **Product posture** — standalone creative platform vs platform-embedded model exposed through host apps vs consumer template app vs open-weights platform vs regional creator platform.
- **Audience packaging** — filmmakers/studios, marketers/social teams, consumers, developers.
- **Generation entry** — blank prompt canvas, image upload, template gallery, agent chat, workflow/node editor.
- **Composition depth** — single clip ↔ multi-shot scene assembly with a timeline editor.
- **Audio posture** — silent video ↔ native audio co-generation ↔ separate audio tools.
- **Openness** — closed cloud ↔ open weights/local deployment; license regimes for open weights.
- **Community** — public trending feeds and creator programs ↔ private workspace-only.
- **Regional deployment** — separate regional services/domains (China vs global).
- **Bundled siblings** — image generation, audio tools, editing of generated output.

### L3 — Vendor-specific (kept out of the final document)

- Runway: Sessions (30-recent list, auto-naming, unrecoverable deletion), Tools/Apps/Agent/Workflows four-mode split, Agent Skills ("/"), Final Cut tab, model-selection preferences (speed/cost/quality/custom), ask-before-generating mode, Seedance/Kling/Veo aggregation, 720p default + 4K upscale, Edit Studio aspect-ratio change, Gen-4.5/Gen-4 Turbo naming, MCP integration, voice input on mobile.
- Veo: SynthID, Ingredients (scene/character/object), style reference, extend-from-last-second, camera-control directions (move back/zoom/move up/move right), first/last frame, 1080p/4K, memorized-content checks, Flow/Vids/Gemini/AI Studio surfaces, Primordial Soup partnership, spoken-audio limitation statement.
- Kling: model series naming (Video 3.0 / 3.0 Omni / O1 / 2.6 音画同出), 数字角色2.0, 对口型, 运镜控制, 多图参考, Kolors GitHub, qingque usage guide, creator community groups.
- LTX: LTX-2.3 open weights, $10M-revenue commercial-license threshold, LTX Desktop, LTX Trainer (LoRA), Playground, API Console.
- Hailuo: H3, Omni Reference, template gallery (K-pop MV, BabyForm, PetPal, SnapMorph, CineScope, ASMR), Hailuo Agent, trending feed with view counts.

## Vendor-specific Findings

See L3 above. None promoted to the canonical document.

## Boundary Findings

1. **vs AI Avatar Video Generator (sibling, 04.21)** — resolves the flagged joint review. The center of gravity differs: avatar products derive a video from **authored spoken content delivered by a depicted presenter** (the speech content is the invariant; imagery is presenter + supporting graphics); generator products produce **imagined scenes from described intent** (the imagery itself is the deliverable; speech is optional and, where present, co-generated rather than authored-and-bound). Test: **remove the presenter + speech binding — if the core survives as prompt→imagery generation, it is AI Video Generator; if the core collapses, it is the avatar Type.** The boundary blurs in both directions and remains a gradient: Runway Agent generates dialogue scenes and voiceover (speech co-generated, not authored-and-bound to a managed presenter); avatar products add AI-generated scenes/B-roll. Both remain separate Types; the gradient is recorded, not resolved into a merger.
2. **vs AI Video Editing Application (sibling, 04.21)** — the material test holds: a generator's input is a description and its output is footage that did not exist; an editor's input is existing footage and its output is a transformed version of it. Blur directions: generation products now edit *their own generated output* (Hailuo H3 "precise multimodal editing"; Runway Agent restyle/change-environment on clips) — editing generated material is part of the generator's refine loop, not a Type collapse; editing products bundle generation entry points. Classify by the primary material: created-from-description vs supplied-by-user.
3. **vs AI Image Generator (04.20)** — deliverable medium: moving footage vs still image. Generation products commonly bundle image generation (Runway generates images; Kling has a full image side; Hailuo Create Image) because images serve as conditioning inputs and supporting assets; the video deliverable is the defining line.
4. **vs Video Editor / NLE (04.06)** — no timeline-first manipulation of imported footage as the core. Generators may add assembly timelines (Runway Agent Final Cut) as delivery machinery for generated clips; the material is still generated, not user footage.
5. **vs Motion Graphics Application (04.07)** — motion graphics animates designed graphic elements by user operation; generation synthesizes footage from description. Overlap appears in marketing use cases (Runway Agent lists motion graphics as a use case; OpusClip uses Veo for motion graphics) — the production method differs (described-and-generated vs designed-and-animated).
6. **vs AI Music/Audio Generator (04.22)** — medium: audio-only vs video. Video generators co-generate audio as a capability (Veo native audio; Kling 音画同出; Runway Agent audio/music/voiceover); the video deliverable defines this Type.
7. **Naming**: the leaf name matches market usage ("AI video generator", "text-to-video", "generative video"). Products self-describe as "AI video generation platform" (LTX), "video generation model" (Veo), "AI video & image generator" (Kling, Hailuo). No alias problem within the leaf.
8. **Market churn** (recorded as a Type-level observation): Sora — a defining early product — was discontinued in 2026 (app April, API September). The Type's structure is stable across vendors, but individual products turn over quickly; documentation-anchored claims must be re-verified more often than in mature categories.

## Uncertainties

- Pika and Luma could not be reached (timeouts/transport errors) — two consumer-first postures are under-evidenced; Hailuo partially covers the consumer/template posture. Claims about consumer products are calibrated accordingly.
- Kling usage-guide article bodies are JS-gated; feature existence is confirmed via the official TOC and product site, but operational details (credit costs, duration limits, resolution options) were not obtained.
- Veo evidence rests on the DeepMind model page (Tier 2); developer-side operational details (API parameters, pricing, quotas) unverified because ai.google.dev and cloud.google.com were unreachable.
- Adobe Firefly's enterprise-suite-embedded posture was not verified (adobe.com timeout); recorded as a plausible unverified variant.
- Whether conversational agent orchestration becomes definitional for the Type is a trend judgment; currently evidenced in 2 of 5 products and kept at L1.
- Exact durations, resolutions, and credit costs per model are product- and plan-specific; intentionally excluded from the final document.

## Final Synthesis

An AI Video Generator is defined by a three-part structure: **described intent** (a prompt, optionally conditioned on images, references, or first/last frames), **model-synthesized footage** (moving imagery generated by the system that did not exist before), and a **generated video clip as the deliverable** (longer works assembled from clips). Everything else commonly bundled today — prompting guides, conditioning inputs, model catalogs, iterate-and-upscale loops, sessions and libraries, credits, APIs, native audio, communities, agents, provenance watermarking — is common mature machinery layered on that core, with product posture (creative platform / platform-embedded model / consumer template app / open weights / regional creator platform) determining which machinery dominates. The Type is separated from the AI Avatar Video Generator by the center of gravity (imagined scenes vs authored speech delivered by a depicted presenter), from the AI Video Editing Application by the material test (created from description vs transformed from existing footage), and from the AI Image Generator by the deliverable medium. The market shows high product turnover (Sora's discontinuation) but a stable structural core.
