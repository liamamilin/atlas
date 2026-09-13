# Research Notes — AI Avatar Video Generator

## Research Goal

Understand, from real products, what an AI Avatar Video Generator is: its defining structure, the objects users manipulate, the creation workflow, the generation/delivery model, the rules that govern synthetic presenters (consent, moderation, credits), and where the boundary lies against neighboring Types (AI Video Generator, AI Voice Generator, AI Video Editing Application, Video Editor, real-time conversational avatar products).

## Initial Boundary

Initial hypothesis (to be tested): an application that turns authored spoken content (a script, or user-supplied audio) into a video in which a synthetic on-screen presenter delivers that content, with system-generated speech and lip synchronization.

Most likely confusions:

- AI Video Generator (text-to-video scene generation) — sibling under 04.21
- AI Voice Generator — audio-only sibling under 04.22
- Video Editor / AI Video Editing Application — editing existing footage vs synthesizing new performance
- Real-time conversational avatar products (agents with a face) — live interaction vs rendered video

## Research Questions

1. What are the core objects (presenter/avatar, script, voice, scene, generated video)?
2. What is the end-to-end creation workflow in each product?
3. Where do avatars come from (stock library, photo, recorded video, builder) and what lifecycle/permissions do they have?
4. How does speech work (stock TTS voices, voice cloning, user audio upload)? Is text the only input?
5. What composition/editing capability surrounds the presenter (scenes, backgrounds, text, media, layouts, templates, timeline)?
6. How does generation work economically and operationally (credits, preview vs generate, async processing, status, webhooks)?
7. How are finished videos managed and delivered (library, share links, embeds, download, SCORM, analytics)?
8. Which rules matter (consent for likeness/voice, content moderation, plan gating, avatar retirement)?
9. Where is the boundary against AI Video Generator / Voice Generator / Video Editor / real-time avatar products? Does the directory leaf hold up as an independent Type?

## Representative Products

| Product | Why selected | Evidence actually obtained |
|---|---|---|
| Synthesia | Enterprise-first market leader; training/L&D positioning; mature help center | Yes — help center collections + article listings (evidence layer A) |
| D-ID | Different philosophy: API-first, photo-driven "talking head"; also ships a real-time agent line | Yes — developer docs incl. API reference (evidence layer A) |
| DeepBrain AI (AI Studios) | Regional (Korea-based) vendor that separates an async video studio (AI Studios) from a real-time avatar line (AI Human); JSON-project API | Yes — AI Studios V3 docs (evidence layer A) |
| HeyGen | Major prosumer/marketing player | No — help.heygen.com and docs.heygen.com timed out repeatedly; no claims based on it |
| Colossyan | L&D scenario-training player | No — help.colossyan.com transport errors; no claims based on it |

Sample rationale: enterprise SaaS leader (Synthesia) + API/photo-driven challenger (D-ID) + regional vendor with an explicit product-line split (DeepBrain). Two additional major products could not be accessed; assertions are calibrated accordingly (no market-wide numeric claims).

## Sources

- Synthesia Knowledge Base — https://help.synthesia.io/ (collections: Build Videos; Use Avatars & Voice; Translate & Localize; Ensure Trust & Safety; Publish & Scale) — accessed 2026-09-06
- D-ID Documentation — https://docs.d-id.com/ (Quickstart; V2 Photo Avatar quickstart; Create a clip API reference; llms.txt index) — accessed 2026-09-06
- DeepBrain AI DOCS — https://docs.deepbrain.io/ (AI Studios V3 Get started with API) — accessed 2026-09-06
- HeyGen — https://help.heygen.com/ , https://docs.heygen.com/ — **unreachable** (timeouts) — no evidence obtained
- Colossyan — https://help.colossyan.com/ — **unreachable** (transport errors) — no evidence obtained

## Product A — Synthesia (help center, evidence layer A)

Observed from Knowledge Base structure and article titles/summaries:

- Creation workflow collections: "Build Videos" (script → scenes → preview → generate → share/download), "Improve Video Quality", "Publish & Scale", "Translate & Localize", "Measure Performance".
- **Video structure**: scenes are the unit ("manage scenes ... to structure your video's beginning, middle, and end"); chapters for navigation; aspect-ratio selection (landscape/portrait/square); three authoring views — Canvas, Storyboard, Timeline ("sync visuals with narration, organize layers"); PowerPoint import turns an existing deck into an editable video; templates can be created from scratch or from existing videos.
- **Script**: per-scene script creation/editing, pauses, pronunciation control ("ensure words, acronyms, and brand names sound right"); audio file upload to a scene as an alternative to text ("upload your own audio file to a video scene").
- **Avatars**: stock avatars ("What stock avatars are available...", "which avatar type is right for me — stock and custom avatars"); custom avatars: Personal Avatar from a video recording, Personal Avatar from a single photo, Studio Express-1 avatar (film, submit), Avatar Builder (lifelike or stylized), personal avatar requests inviting non-users (e.g. a colleague) to record on the workspace's behalf; avatar outfits and backgrounds; expressive avatars whose delivery follows script wording; avatar B-roll clips (prebuilt presets or text prompts); Dialogue feature (multiple avatars with unique voices in one scene); Swap Shot (camera angle/zoom switches mid-script).
- **Avatar governance**: "Avatar Policy Foundation — covering consent, ownership, sharing, access, and avatar lifecycle"; custom avatar/voice access control and workspace sharing; deletion requests with defined time frames; avatar/voice "retirement" and what happens to existing videos; plan-gated avatar availability ("check which Avatars are available on my plan"); generation error "you don't have permissions for avatars".
- **Voices**: stock voices and languages; language selection per scene (multiple languages within a single scene); voice change, speed; voiceover-only video by hiding the avatar; voice options taxonomy — stock voices, custom voice clones, personal voices; voice cloning by recording or uploading a sample; ElevenLabs Professional Voice Clone transfer; preview voices and download audio clips.
- **Generation economics**: preview before generating "without using credits"; generating consumes credits; errors for insufficient credits and for avatar/voice permissions; autosave of edits.
- **Delivery**: share via public link, embed code, SCORM package, password protection; download; GIF thumbnail; "YouTube codes" to avoid content claims; video analytics/Insights and workspace-level reporting.
- **Localization**: translation into 140+ languages, AI Dubbing, Translation Glossary ("turn one video into many — without re-recording").
- **Adjacent surfaces**: Roleplay Sessions (interactive practice with learners — 16 articles); "Work with AI" (AI Assistant, Generate with AI); Trust & Safety collection (35 articles) covering content policies and moderation standards.

## Product B — D-ID (developer docs, evidence layer A)

Observed from docs.d-id.com (API reference is precise; Studio is the web app wrapping the same capabilities):

- **Two product lines, explicitly separated**: "Realtime" (interactive agents: avatar + LLM + knowledge + tools, streamed via WebRTC) vs "Videos" ("create AI-generated videos from images, text, and audio ... produce talking avatars").
- **Talks endpoint** (one-shot): POST with `source_url` (an image) + `script` → response has `id` and `status: created` → poll GET until `status: done` → `result_url` to an mp4. "The Talks endpoint transforms any photo into a speaking avatar."
- **Script object**: either `type: text` (with TTS provider selection — Microsoft default, ElevenLabs, Amazon Polly, Google, Azure OpenAI; voice_id; voice_config rate/pitch/style; SSML flag; pronunciation dictionary_id; subtitles flag) or `type: audio` (audio_url; file-size and duration limits documented). So **text is not the only input; user-supplied audio is a first-class alternative**.
- **Clips endpoint** (Premium/presenters): `presenter_id` + `driver_id` + script + config (result_format mp4/mov/webm incl. transparent webm; output_resolution; logo overlay) + background (solid color or image) + crop. Managed "presenters" are listable/deletable records; "drivers" are gesture/performance sources from a drivers bank.
- **Avatar creation variants**: V4 Expressive Avatars (emotional states/sentiments), V3 Pro (Full-HD premium presenters with natural body movements), V3 Instant (custom avatar from the user's own video footage), V2 Photo Avatars (talking head from a photo + text), plus "Create a Premium+ Avatar" (training endpoint).
- **Moderation, hard-coded in the API**: HTTP 451 responses distinguish `ImageModerationError`, `CelebrityRecognizedError`, `TextModerationError`, `AudioModerationError` ("Automatic content moderation — contact support ... for manual review").
- **Consent machinery as API objects**: create/list/get/delete **consents**; "Upload video for consent" — consent is a first-class resource tied to avatar creation.
- **Voice cloning**: "Clone Voice — add a new voice to your collection of voices. Upload audio or video file ... at least 30 seconds of diverse high-quality audio samples" (recommendation documented on the endpoint); voices are listable/deletable records.
- **Economics/ops**: credits endpoint (remaining/total **with time expiration**); HTTP 402 InsufficientCreditsError; HTTP 403 PermissionError; temp uploads (image/audio) expire in 24–48h; result URLs expire (24h documented on talks quickstart); webhooks and `user_data` passthrough.
- **Video Translate**: translate any video to new languages with automatic lip-sync and voice cloning — operates on existing footage (dubbing capability).
- **Real-time line**: agents with knowledge bases, tools, memories, chat sessions, embeds; session telemetry — a separate interactive surface, not the async video product.

## Product C — DeepBrain AI / AI Studios V3 (developer docs, evidence layer A)

- **Project JSON model**: a project has `orientation` (landscape etc.) and `scenes[]`; each scene has `background` (image/color source), and `clips[]`; a clip of `type: "aiModel"` carries `layer`, position (`top`/`left`), size, a `script` (HTML content: `"Hello, this is test video using Api."`), `effects` (e.g. `head-only`), and a `model` object (`ai_name` id, `emotion`, `language`, source imagery, head-geometry editor values). The avatar is therefore a **positioned, layerable clip inside a scene**, with per-model emotion and language.
- **Async generation**: "video synthesis requires ... conversion time"; progress endpoint; "It takes about 1 to 10 minutes to produce a video depending on the size of the video, the server status, and the waiting users ahead of your requests"; status becomes Complete; **webhook** notification on completion.
- **API posture**: API on Pro plan and above; appid + user key auth; separate **China service domain** (app.aistudios.cn) vs global — regional deployment is explicit.
- **Template-based automation**: exporting a JSON-based template, exporting an existing project to video, multiple chroma-key export (transparency use cases).
- **Other modules**: Avatars → custom avatar; **Interactive Avatar** (client flow) as a separate API module; a separate "AI Human" product line ("virtual employees ... Brand Ambassadors, Bankers, Retail Assistants, Tutors, News Anchors") with SDKs for Web/Windows/Unity/Android/iOS — the vendor itself separates the async video studio from the real-time avatar product.
- Voice generator exists as a "Tools" API module.

## Cross-product Comparison

| Dimension | Synthesia | D-ID | DeepBrain AI Studios | Reading |
|---|---|---|---|---|
| Central input | per-scene script (text), audio upload alternative | script object: text (TTS) **or** audio URL | per-clip `script` (HTML text) | text script standard; **audio input also supported** in 2 of 3 (D-ID, Synthesia) → script-as-concept, TTS optional |
| Presenter | stock + custom (video/photo/builder) avatars; outfits/backgrounds | photo → talking head (talks); managed presenters/drivers (clips); avatars from own video | stock `aiModel` clips; custom avatar module; per-model emotion | presenter object is universal; **provenance varies** (stock/photo/video/builder) |
| Speech | stock voices + clones + personal voices; language per scene | TTS provider marketplace (MS/ElevenLabs/Polly/Google/OpenAI) + cloned voices | voice generator tool; per-model language | voice selection + cloning common; **provider model varies** |
| Composition | scenes, chapters, aspect ratio, Canvas/Storyboard/Timeline, templates, PPT import | single-result clips (background, crop, logo, resolution) — minimal composition on API | scenes → clips (layered, positioned), background, effects, orientation | **composition depth varies widely**; multi-scene editing common in app-first products, thin in API-first |
| Generation | preview (free) vs generate (credits); async | poll → done; 402 credits; result URL expiry | poll progress 1–10 min; webhook; Complete | **async render + credit economics + status lifecycle universal** |
| Rules | avatar policy (consent/ownership/lifecycle), plan gating, permissions errors, moderation collection | consent API objects; 451 moderation/celebrity errors; 402/403 | plan gating (Pro+ for API); regional domains | **consent + moderation + plan-gated access are structural, not marketing** |
| Delivery | share link/embed/SCORM/password, download, analytics | result_url download/stream, webhooks | project → video export, chroma key | download/stream universal; L&D-oriented packaging (SCORM) product-specific tier |
| Localization | 140+ languages, dubbing, glossary | Video Translate (lip-sync + voice clone) | per-model language | translation/dubbing common in mature products |
| Real-time line | Roleplay Sessions (adjacent collection) | Realtime agents (separate line) | AI Human (separate product) | **every vendor separates async video from real-time interactive avatars** |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Depicted Presenter (avatar)
└── Authored Spoken Content (script text or supplied audio)
    └── System-Generated Speaking Performance
        (synthesized movement — lip sync — synchronized to the speech)
        └── Rendered Video Deliverable
```

Four properties, deliberately minimal:

1. **Depicted presenter** — a visual person-figure that appears on screen as the speaker. Provenance is NOT defined here (stock synthetic human, user photo, recorded video, stylized character all qualify).
2. **Authored spoken content** — the user supplies what is said, as text or audio. The content exists before the video does; the video is derived from it.
3. **System-generated speaking performance** — the application synthesizes the presenter's speech delivery (at minimum lip movement synchronized to the spoken content). The user does not film the performance; without this synthesis step the product is not this Type.
4. **Rendered video deliverable** — the output is a video (file or streamable result), not merely audio and not a live-only session.

Historical / market-sample check: early photo-animation tools (a single photo + audio → short talking clip), regional "make my photo talk" apps, stock-presenter-only enterprise tools, and API-only render services all satisfy these four properties while lacking libraries, scene editors, templates, TTS, credits, and teams. Conversely, removing any property breaks the Type: remove the presenter → AI Voice Generator / audio dubbing; remove authored content (prompt-only imagery) → AI Video Generator; remove the generation step (arranging existing footage) → Video Editor; remove the rendered deliverable (live-only) → real-time conversational avatar product.

### L1 — Common Mature Structure

Present in most mature modern products; not required to recognize the Type:

- **Avatar library** — stock avatars as reusable records; custom avatars created from a recorded video, a single photo, or a builder; outfit/background/styling variants; avatar sharing, access control, retirement and deletion lifecycle.
- **Voice layer** — stock TTS voices across languages, selectable per scene; voice cloning from recorded samples; download/preview of voice audio.
- **Script machinery** — per-scene scripts, pauses, pronunciation control/dictionaries; alternative audio input.
- **Scene composition** — multiple scenes, backgrounds, text/media overlays, aspect ratio, timeline/layered views, reusable templates; document import (e.g., slides) as a starting point.
- **Generation economics & lifecycle** — credit/minute accounting with plan gating; free preview vs paid generation; asynchronous rendering with status (queued/processing/complete/error) and completion notifications (webhooks on APIs); regeneration after edits.
- **Delivery surface** — persistent video library; share links, embeds, downloads; access controls (passwords); basic analytics in team-oriented products.
- **Consent & moderation enforcement** — consent capture for a real person's likeness/voice before custom avatar/clone creation; automated content moderation on images/text/audio; celebrity/personality recognition; avatar usage policies.
- **AI assistance** — script drafting/rewriting from prompts or documents; AI-generated B-roll/imagery; one-video-to-many translation/dubbing with re-synced lip movement.

### L2 — Variant / Optional Structure

- **Presenter substrate** — stock synthetic humans vs photo-derived vs video-trained vs stylized builder characters; head-and-shoulders vs full-body with gestures.
- **Speech source** — built-in TTS only vs multi-provider TTS marketplace vs BYO API key; SSML support.
- **Composition depth** — single-shot render (API/photo tools) vs multi-scene editor with timeline and templates (studio products).
- **Delivery packaging** — plain download vs L&D packaging (SCORM, quizzes/interactivity) vs analytics/insights.
- **Product posture** — web studio-first vs API-first vs studio+API; regional deployment domains.
- **Adjacent real-time surfaces** — interactive/roleplay sessions, conversational agents with a live avatar — usually sold as a separate product line or module.
- **Enterprise workspace** — workspaces/teams, roles/permissions, brand kits, SSO.
- **Dubbing direction** — translate/dub existing third-party footage (operates on user video, not on a managed presenter).

### L3 — Vendor-specific (kept out of the final document)

- Synthesia: Express-1 studio avatars, Avatar Builder, Swap Shot, Dialogue (up to 20 avatars), ElevenLabs PVC transfer, YouTube codes, Translation Glossary, Insights, Roleplay Sessions, SCORM.
- D-ID: Talks vs Clips vs Presenters vs Drivers object split; 451 error taxonomy (image/text/audio moderation, celebrity); credits with expiration; 24–48h temp-upload storage; transparent webm; SSML; pronunciation dictionaries.
- DeepBrain: `odin/v3` project JSON schema, `aiModel` clip with head-geometry editor values, per-model `emotion`, `head-only` effect, multi-chroma-key export, appid/userkey auth, dedicated China domain.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical document.

## Boundary Findings

1. **vs AI Video Generator (sibling, 04.21)** — the cleanest boundary in the sample. AI Video Generator products produce novel moving imagery from prompts/images; the deliverable is generated *footage*. Avatar video products derive a video from *authored spoken content delivered by a depicted presenter*; the imagery is largely the presenter plus supporting graphics, and editing is text-editing (change the script, regenerate). Test: **remove the presenter + spoken-content binding — if the product's core survives as prompt→video imagery generation, it is AI Video Generator; if the core collapses, it is this Type.** The boundary blurs in both directions (avatar products add AI-generated scenes/B-roll; text-to-video products add talking avatars), which suggests center-of-gravity, not a wall.
2. **vs AI Voice Generator (04.22)** — deliverable medium: video with a visible speaker vs audio alone. Adding TTS to this Type does not make it a voice generator; hiding the avatar for a scene (voiceover-only) is a scene-level option, not a Type drift.
3. **vs Video Editor / AI Video Editing Application (04.06 / 04.21)** — editors manipulate pre-existing footage; avatar generators synthesize a performance that did not exist. Studio-style avatar products include real editing surfaces (timeline, layers, scenes) — the editing is L1 machinery around the synthesis core. Test: **remove the script/presenter and what remains is a video editor → editing is the product's center; what remains is nothing editable → synthesis is the center.**
4. **vs real-time conversational avatar products** (D-ID Realtime agents; DeepBrain AI Human; Synthesia Roleplay Sessions) — same presenter + sync technology, but the deliverable is a live interactive session, not a rendered video. All three researched vendors **ship these as separate product lines/modules**, which is strong evidence that the market itself treats async video generation and live avatar interaction as different products. This leaf covers the async, rendered-video Type. (No dedicated directory leaf exists for real-time conversational avatars; nearest neighbors are Agent Development Platform / conversational agent leaves in §13. Recorded below.)
5. **vs Presentation Application** — slide import and slide-like scenes exist (L1 convenience), but the defining object is the speaking presenter video, not a navigable slide deck.
6. **Naming**: the leaf says "Generator"; market names include "AI avatar video" / "talking-head video" / "digital human video" / "AI presenter". D-ID's API names the objects talks/clips/presenters; DeepBrain names them aiModel clips; Synthesia centers on avatars + scenes. Object naming varies; the underlying structure is shared — no alias problem within the leaf.

## Uncertainties

- HeyGen and Colossyan could not be reached; all cross-product claims rest on three products. Claims that might differ in other products (e.g., whether audio input, consent flows, or SCORM exist) are calibrated to "common in the researched sample" where only 2/3 support them.
- Exact credit pricing, minute-to-credit conversion, generation durations per plan: deliberately not stated (plan-specific, and only loosely evidenced: DeepBrain's "1 to 10 minutes" is plan/server-dependent and quoted as vendor guidance).
- Consent mechanics in Synthesia are evidenced at help-center level (article titles confirm consent/ownership/lifecycle topics); the operational details of verification were not fetched article-by-article — assertions kept at "consent is a governance topic with its own policy machinery," not the exact verification steps.
- Whether stylized (non-human) presenters are a major market segment or a minority option: evidenced only as an option in one product's builder; kept out of the definition and mentioned only as a provenance variant.
- Studio (GUI) side of D-ID and DeepBrain was evidenced through API docs; GUI composition depth for those two is inferred to be thinner or comparable, and is marked as uncertain rather than asserted.

## Final Synthesis

An AI Avatar Video Generator is defined by a four-part structure: a **depicted presenter**, **authored spoken content** (script text or supplied audio), a **system-generated synchronized speaking performance** (the defining "generation" step), and a **rendered video deliverable**. Everything else commonly bundled today — avatar libraries, voice cloning, scene editors, templates, credits, teams, translation, analytics, LMS packaging — is common mature machinery layered on that core, with provenance (stock/photo/video/builder) and composition depth varying by product posture (studio-first vs API-first). Consent for real-person likeness/voice and automated content moderation are structural rules of the Type, hard-coded into sampled products' APIs and policies. The market separates this Type cleanly from prompt-driven video generation and from audio-only voice generation, and vendors themselves split off real-time interactive avatars as different product lines.
