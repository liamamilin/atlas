# Research Notes — AI Audio Generator

## Research Goal

Understand what an "AI Audio Generator" is as a distinct Application Type within 04.22 Generative Audio (siblings: AI Voice Generator, AI Music Generator): what its core object is, what users provide and receive, how the generation loop works, which rules matter (moderation, licensing, economics), and where its boundaries sit against the two sibling Types and against non-generative neighbors (sound-effects libraries, audio editors, DAWs).

## Initial Boundary (working hypothesis before research)

- Hypothesis: the leaf centers on generating **sound material that is neither speech nor musical composition** — sound effects, foley, ambience, one-shots, textures — by describing the desired sound, with the waveform synthesized by a model rather than retrieved from a recording library.
- Nearest neighbors: AI Voice Generator (speech), AI Music Generator (compositions), sound-effects/stock libraries (retrieval), Audio Editor (manipulation of existing recordings), DAW (production environment).
- Risk: "AI Audio Generator" could be an umbrella alias covering voice + music + SFX. The directory lists all three as separate leaves, so the research must establish whether a distinct non-speech/non-music center of gravity exists in the market.

## Research Questions

1. What is the central object (the generation? the clip? the prompt?)
2. What inputs does the user provide — text prompt only, or also reference audio / seed material?
3. What does the output look like — duration, formats, where does it go?
4. What is the standard workflow from idea to usable asset?
5. What controls exist (duration, prompt adherence, looping, variation strength)?
6. How are generations kept, compared, and reused (history, favorites, community surfaces)?
7. Which rules matter — content moderation, ownership/commercial terms, usage economics?
8. Where is the boundary vs AI Voice Generator, AI Music Generator, SFX libraries, audio editors?
9. What variants exist (SFX-only vs general audio; web app vs API vs DAW plugin vs open weights)?
10. Historical/market check: does the definition overfit the current text-prompt pattern?

## Representative Products

Selected for market representability, documentation quality, different product philosophies, and different customer tiers:

1. **ElevenLabs — Sound Effects** — SFX as one capability inside a commercial voice/audio platform; creator → enterprise tiers; web playground + API. (Tier 1: official docs, product guide, FAQ, API reference)
2. **Stable Audio (Stability AI)** — audio-first model family (SFX + music) with web app, DAW plugin, API, self-hosting, open weights; enterprise + free tiers. (Tier 1: official knowledge base — prompt guide, moderation article; Tier 2: product page)
3. **AudioGen / AudioCraft (Meta)** — open-source research lineage; text-to-sound library for developers. (Tier 1: official repository documentation)

Abandoned candidates (source-access limitation): OptimizerAI (dedicated AI-SFX startup; transport errors ×2), MyEdit/CyberLink (free consumer web tool; timeout ×2). These segments (dedicated SFX point products, free consumer tools) are therefore under-evidenced.

## Sources

Fetched 2026-09-06:

- ElevenLabs — Sound Effects overview (docs): https://elevenlabs.io/docs/capabilities/sound-effects
- ElevenLabs — Sound Effects product guide + FAQ (docs): https://elevenlabs.io/docs/eleven-creative/playground/sound-effects
- ElevenLabs — Sound Effects API reference: https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert
- ElevenLabs — Eleven Music overview (sibling-boundary evidence): https://elevenlabs.io/docs/capabilities/music
- Stability AI — Stable Audio product page: https://stability.ai/stable-audio
- Stability AI — Knowledge Base, Stable Audio section index: https://kb.stability.ai/knowledge-base/stable-audio
- Stability AI — Stable Audio 3 Prompt Guide: https://kb.stability.ai/knowledge-base/stable-audio-3-prompt-guide
- Stability AI — Content moderation article: https://kb.stability.ai/knowledge-base/why-was-my-prompt-flagged-understanding-content-moderation-in-stable-audio
- Meta — AudioCraft repository README: https://github.com/facebookresearch/audiocraft
- Meta — AudioGen model documentation: https://github.com/facebookresearch/audiocraft/blob/main/docs/AUDIOGEN.md

Unreachable (recorded per source-access limitation rules): optimizerai.ai (transport error ×2), www.myedit.online (timeout ×2), stableaudio.com (JS-rendered shell; substituted by stability.ai product page + KB).

## Product A — ElevenLabs (Sound Effects)

Evidence layer: **A (directly observed)** unless noted.

### Key observations

- Positioning: "turns text descriptions into high-quality audio effects with precise control over timing, style and complexity." Named use cases: cinematic sound design for films & trailers; custom SFX for games & interactive media; foley and ambient sounds for video content.
- Input: a text prompt. "The model understands both natural language and audio terminology." Prompt length capped (450 characters per FAQ).
- Controls (API + UI):
  - `duration_seconds` — optional; if unset the model "guesses the optimal duration using the prompt"; bounded range (0.5–30 s per API; docs cite 0.1–30 s).
  - `loop` — seamless looping "for sound effects longer than 30 seconds… perfect for atmospheric sounds, ambient textures, and background elements."
  - `prompt_influence` — how strictly the output follows the prompt (default 0.3; higher = more literal, less variable).
- Generation is **multi-variation**: "Each time you select Generate, the AI will generate full variations of the prompt" — four effects per generate in the playground.
- Prompting guide teaches prompt craft: simple effects ("Glass shattering on concrete"), complex sequences ("Footsteps on gravel, then a metallic door opens"), musical elements ("90s hip-hop drum loop, 90 BPM"), and a glossary of audio terminology (impact, whoosh, ambience, one-shot, loop, stem, braam, glitch, drone).
- Output: audio file; MP3 for all effects, WAV at 48 kHz for non-looping effects (docs); API supports multiple codec/sample-rate/bitrate formats, some gated by subscription tier.
- Post-generation handling: History tab; download MP3/WAV; star to favorites; adjust prompt/settings and regenerate. Explore tab: browse community-made sound effects.
- Workflow guidance: for complex multi-event sequences, "generate individual sound effects and then combining them in an audio editor of your choice" — i.e., the product positions itself as a material source, not a sequencing environment.
- Economics: credit-based; cost varies with settings (duration, number of variations); "cost is not influenced by the text input."
- **Sibling boundary (direct)**: SFX docs state "Musical elements: Drum loops, bass lines, and melodic samples can be generated; for full music production use the Music API." Music is a separate capability with separate docs, terms (music-terms page), and model line. Voice (TTS/voice cloning) is likewise a separate capability family; SFX documentation does not cover speech.

## Product B — Stable Audio (Stability AI)

Evidence layer: **A (directly observed)** unless noted.

### Key observations

- Positioning (product page): "Stable Audio 3.0 is a model family trained on fully licensed data" — models range "from SFX to musical compositions"; full tracks up to ~6 minutes; "Generation is the beginning of the process, not the end" (artist-first controllability).
- Model family: Large (enterprise-grade), Medium (full song composition, open weights), Small & **Small SFX** (mobile-optimized, open weights) — SFX exists as a named model variant.
- The prompt guide names **four generation modes**: music composition; **samples and sound effects**; audio-to-audio; inpainting and continuation.
- SFX prompting structure (KB): describe **the source** (what object/instrument/synth makes the sound), **the action** (how triggered, how long, decay), **the production/characteristics** (mic placement, room character, processing). Examples: distorted wooden-drawer slam; tape-stop sub-bass; fast-decay hi-hats.
- Tag syntax: optional labels steer output class — `TrackType: Music` (full track), `TrackType: Instrument` (stem), `TrackType: SFX` ("a sound effect or one-shot"), `Format: Duo`, `Genre: …`.
- Audio-to-audio: seed audio + optional prompt + `init_noise_level` (how far the output moves from the input; documented working range 0.3–0.9). Uses: timbre transfer (violin → electric guitar), style transfer.
- Inpainting: select a section, regenerate just that section with a prompt while preserving the rest; documented caveats (too-small sections ignore the prompt; context matters).
- Continuation: extend an existing clip to a target length (variable-length generation; up to ~6 minutes on Large).
- Non-determinism as a design property: "Stable Audio will not produce the same result every time. That variation can help you find unexpected ideas."
- Delivery surfaces: web app (with multitrack session view, track FX, tape/splice edits — reverse, stutter, freeze, cut, copy, paste — "without generating new audio"), **DAW plugin** (generate directly inside a DAW; treat output "like any other audio in the session"), Platform API, self-hosted enterprise license, open-weights download.
- **Voice boundary (direct)**: "Stable Audio 3.0 is designed primarily for instrumental work. It can sometimes create non-lexical vocal-like textures, but it is not intended to generate intelligible vocals."
- **Moderation rule (direct)**: prompt text is screened before generation; prompts naming real, identifiable individuals ("in the style of [artist]") may be flagged/blocked — protection against style cloning, misattribution, likeness issues. Guidance: describe qualities instead of naming people.
- Ownership/commercial terms (product page + KB): trained on fully licensed data; "You own your outputs, and can distribute and commercialize them freely"; legal indemnification under the Enterprise license.
- Economics: subscription plans and credits (KB section exists; details not fetched).

## Product C — AudioGen / AudioCraft (Meta)

Evidence layer: **A (directly observed)** for the repository documentation; the underlying models are research artifacts, so this product is used as lineage/market-structure evidence rather than a commercial product sample.

### Key observations

- AudioGen is defined as "a textually-guided audio generation model that performs text-to-sound generation" — sibling to MusicGen ("controllable text-to-music model") inside the same library. **The library itself separates text-to-sound from text-to-music as different models.**
- Example descriptions: 'dog barking', 'sirene of an emergency vehicle', 'footsteps in a corridor' — environmental/everyday sounds.
- API shape: load model → `set_generation_params(duration=5)` → pass a **list of descriptions** → batch of generated samples → written to WAV files with loudness normalization (−14 dB LUFS).
- Controls: duration; sampling parameters (temperature, top-K, top-P); batch size; audio continuation from a prompt (conditioning on existing audio).
- Technical substrate (L3): 16 kHz EnCodec tokenizer, autoregressive Transformer over discrete tokens; medium model ~1.5B parameters; GPU requirement documented.
- License: code MIT; **model weights CC-BY-NC 4.0 (non-commercial)** — an example of how licensing posture varies across the Type.
- No user-facing app surface in this sample: the "interface" is a Python API/notebook. Confirms that the Type can exist as a developer-facing library without a GUI.

## Cross-product Comparison

| Dimension | ElevenLabs SFX | Stable Audio | AudioGen (AudioCraft) |
|---|---|---|---|
| Type center | text → sound effects | text → SFX **and** music (tagged modes) | text → environmental sound |
| Input | text prompt (NL + audio terminology) | text prompt (+ optional TrackType tags); seed audio for audio-to-audio | text descriptions |
| Output | short clips (≤30 s), MP3/WAV | one-shots → full tracks (~6 min), variable length | short clips (e.g., 5 s), WAV, loudness-normalized |
| Controls | duration (auto/set), looping, prompt influence | duration, tags, noise level, inpainting, continuation | duration, sampling params, batch |
| Variations | multiple per generate (4 in playground) | non-determinism documented as a feature | batch of descriptions |
| History/library | History + favorites + Explore (community) | web-app workspace/sessions | none (files) |
| Post-generation editing | none built in (external editor recommended) | built-in tape/splice edits, multitrack mix, FX | none |
| Delivery surfaces | web playground + API | web app + DAW plugin + API + self-host + open weights | Python library |
| Moderation | not fetched (not claimed) | prompt screening; real-person naming blocked | not applicable (open weights) |
| Ownership terms | plan-dependent commercial terms | outputs owned; commercial use free; enterprise indemnification | weights CC-BY-NC (non-commercial) |
| Sibling separation | SFX vs Music vs Voice = separate capabilities | SFX vs Music = tag-level modes in one family; vocals explicitly out of scope | AudioGen vs MusicGen = separate models |

**Stable commonalities (Layer B — cross-product):**

1. Description-driven input: every product takes a natural-language description of the desired sound; every product publishes prompting guidance (prompting guides, tag syntax, terminology glossaries) — prompt craft is a first-class skill of the Type.
2. On-demand model synthesis: the waveform is generated at request time; none of the sampled products retrieves from a fixed recording library as the primary mechanism (ElevenLabs' Explore community surface is secondary to generation).
3. Bounded audio clip as deliverable: every product returns discrete audio files (MP3/WAV) that can be auditioned, compared, and exported.
4. Duration as a first-class control: every product exposes duration (set or auto); looping/extension exists where long ambience is needed.
5. Multi-attempt iteration: every product generates variations/batches and expects a generate → audition → regenerate loop; non-determinism is documented, not hidden.
6. Non-speech scope: no sampled product generates intelligible speech in this mode; the one that spans music+SFX explicitly excludes intelligible vocals; the platform vendor keeps voice, music, and SFX as separate capabilities.
7. Downstream handoff: outputs are meant to be used inside other contexts (video, games, podcasts, DAW sessions); one product ships a DAW plugin, another recommends combining clips in an external editor.
8. Usage economics: credit/plan-based generation is common in commercial products; licensing posture varies (commercial-friendly vs non-commercial weights).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

```text
Description of a desired sound (user-supplied specification)
  → on-demand model synthesis of the audio
    → bounded audio clip as the deliverable (auditionable, exportable)
      → output scope: sound material — effects, foley, ambience, one-shots, textures —
        as distinct from intelligible speech (AI Voice Generator)
        and musical composition (AI Music Generator)
```

Four properties. Remove any one and the Type stops being recognizable:

- **Description-driven specification** — the user states what they want to hear in words (dominant implementation) or by reference material; without a specification step it is not this Type (it would be a synth preset engine or a library).
- **On-demand synthesis** — the audio is generated by a model at request time. Remove this and the product is a sound-effects library (search + download of pre-existing recordings).
- **Bounded audio clip as deliverable** — a discrete, self-contained audio asset the user can keep, compare across attempts, and export. Remove this and it is a live processing effect or a streaming surface.
- **Sound-material scope** — the output is neither intelligible speech nor a musical composition. Remove this restriction and the leaf collapses into its two siblings.

### L1 — Common Mature Structure

Present in most mature commercial products; not required for the definition:

- generation controls: duration (set or auto), prompt-adherence/influence, seamless looping for ambience
- multi-variation generation per attempt (batch of alternatives)
- generation history / library with save/favorite; community exploration surface in some products
- prompting guidance as product content (guides, terminology glossaries, tag syntax)
- multiple delivery surfaces: web app, API, (in some products) DAW plugin
- standard download formats (MP3/WAV)
- prompt-level content moderation in hosted commercial products
- credit/subscription economics; commercial-use terms tied to plan or license

### L2 — Variant / Optional Structure

- audio-to-audio (seed audio + variation-strength control; timbre/style transfer)
- inpainting (regenerate a selected section, preserve the rest) and continuation (extend length)
- built-in post-generation editing/mixing workspace (multitrack, tape/splice edits, FX)
- DAW plugin form (generation inside a production session)
- self-hosted / open-weights form
- custom model fine-tuning on the customer's own audio library
- reference-audio conditioning (style guidance from an uploaded track)
- community sharing/exploration surfaces
- musical-element generation inside an SFX product (drum loops, stems, stabs) — a sample/loop class of output that stops short of composition

### L3 — Vendor-specific (Research Notes only)

- ElevenLabs: 450-character prompt cap; 4 variations per generate; `prompt_influence` default 0.3; duration 0.5–30 s (API) / 0.1–30 s (docs); 40 credits per second when duration is specified; tier-gated output formats; `eleven_text_to_sound_v2` model id; Explore community tab; regional API endpoints.
- Stable Audio: `TrackType:` / `Format:` / `Genre:` tag syntax; `init_noise_level` documented working range 0.3–0.9; ~6-minute maximum on Large; tape ops (reverse/stutter/freeze); Ableton Live plugin setup guide; Brand Studio; model tiers Large/Medium/Small/Small SFX.
- AudioGen: 16 kHz EnCodec tokenizer with 4 codebooks at 50 Hz; −14 dB LUFS loudness normalization; `facebook/audiogen-medium` (1.5B); CC-BY-NC weights; dora training grids.

## Vendor-specific Findings

- Stable Audio's tag syntax (`TrackType: SFX`) is a vendor-specific prompting convention — evidence that output-class steering exists in the Type, but the syntax itself is not canonical.
- ElevenLabs' Explore community tab and Stable Audio's Brand Studio are product-specific surfaces.
- AudioGen's loudness normalization default is a library-specific implementation detail.

## Boundary Findings

1. **vs AI Music Generator (sibling)**: same generation loop, different output class. Test: if the primary deliverable is a musical composition (arrangement, sections, vocals, full track), it is the music Type; if it is sound material (one-shots, foley, ambience, stems as material), it is this Type. Market evidence: ElevenLabs ships SFX and Music as separate capabilities with separate terms and its SFX docs redirect full music production to the Music API; AudioCraft ships AudioGen and MusicGen as separate models; Stable Audio spans both via output-class tags — i.e., one product can implement both Types, which is bundling, not merger.
2. **vs AI Voice Generator (sibling)**: intelligible speech is out of scope here. Test: if the deliverable is spoken/sung verbal content, it is the voice Type. Evidence: Stable Audio explicitly states it is "not intended to generate intelligible vocals"; ElevenLabs operates voice as a separate capability family; AudioGen's examples are environmental sounds.
3. **vs sound-effects/stock library (non-generative)**: retrieval vs synthesis. Test: remove the model — a library still delivers audio via search over pre-existing recordings; a generator cannot. Hybrid products may add community/explore libraries beside generation, but the defining capability is on-demand synthesis.
4. **vs Audio Editor (04.09)**: editors manipulate existing recordings; this Type creates material from descriptions. Stable Audio's web app bundles editing around generation (tape/splice edits "without generating new audio"), but the editing serves the generation workflow. Test: remove generation → an editor remains; remove editing → the generator remains.
5. **vs DAW / music production (04.10)**: the DAW plugin form injects generation into production sessions, but the generator is a material source inside the session, not the arrangement/production environment. ElevenLabs likewise recommends combining generated clips "in an audio editor of your choice."
6. **vs AI Video Generator workflows**: some generative-audio research generates audio *from* video; in the sampled commercial products, video is a use context (foley for video content), not an input modality. Video-to-audio would be an input-variant if it reaches product maturity — recorded as an observation, not a claim.

## Historical / Market-Sample Check

The Type is young (research models 2022–2023; commercial products from ~2023). There is no pre-AI product generation to test against, so the check is applied in the overfitting direction:

- Do not define the Type by **text-prompt-only** input (audio-to-audio and reference conditioning exist).
- Do not define it by **short-clip-only** output (variable-length generation and continuation exist).
- Do not define it by the **web-app** surface (API, plugin, and library forms exist).
- Do not define it by **SFX-only** scope in a way that would forbid musical-element samples (drum loops/stabs are sound material, not compositions).
- Do not define it by a specific model technique (diffusion vs autoregressive LM — both present in the sample; the defining property is model synthesis from a description, technique-agnostic).

Reverse check: a synthesizer or preset engine generates sound but from parameter manipulation, not from a description of a desired sound/event — excluded by the description-driven invariant.

## Uncertainties

- **Dedicated-SFX startups and free consumer tools under-evidenced**: OptimizerAI and MyEdit were unreachable (2 failures each, abandoned). Claims about the low-end market (free tools, per-generation limits, watermarking) are therefore not made.
- **Moderation coverage**: directly observed only in Stable Audio's KB. ElevenLabs operates safety programs (its docs reference safety surfaces) but the SFX-specific moderation behavior was not fetched — no claim made for it.
- **Voice boundary strength**: rests on Stable Audio's explicit exclusion + ElevenLabs' capability separation + AudioGen's environmental-sound scope. No sampled product generates speech in this mode, so the boundary is consistent but the "non-speech" invariant is inferred from scope statements rather than from a failed attempt to generate speech.
- **Pricing specifics**: credit mechanics observed (ElevenLabs per-second credits; Stable Audio plans/credits section exists) but exact plan structures not fetched — kept generic.
- **Watermarking/provenance**: AudioCraft ships a watermarking model (AudioSeal) in the same library; whether hosted products watermark SFX outputs was not verified — no claim made.

## Final Synthesis

The AI Audio Generator is a **material-source application**: the user describes a sound, a model synthesizes it on demand, and the result is a bounded audio clip delivered as a standard audio file for use in downstream work (video, games, podcasts, music production). Its identity is defined by four invariants — description-driven specification, on-demand synthesis, bounded clip deliverable, sound-material scope (neither speech nor composition) — and everything else (controls, variations, history, moderation, economics, editing surfaces, plugins, open weights) is mature structure or variant. The market itself confirms the three-way split inside Generative Audio: the same vendors that operate voice and music generation keep sound-effect generation as a distinct capability, model, or output class. The strongest structural boundary is against the sound-effects library: retrieval of pre-existing recordings vs on-demand synthesis is the line that makes this a distinct Type rather than a new front-end on stock libraries.
