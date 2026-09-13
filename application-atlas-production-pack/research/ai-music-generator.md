# Research Notes — AI Music Generator

## Research Goal

Understand what an "AI Music Generator" is as a distinct Application Type within 04.22 Generative Audio (siblings: AI Voice Generator, AI Audio Generator): what its core object is, what users provide and receive, how the generation→refinement loop works, which rules matter (moderation, ownership/licensing, economics), and where its boundaries sit against the two sibling Types, against the 04.10 human music-production family (DAW, beat-making, loop-based production), and against non-generative neighbors (royalty-free music libraries, streaming platforms).

## Initial Boundary (working hypothesis before research)

- Hypothesis: the leaf centers on generating **musical compositions** — arranged pieces with temporal structure (sections, progression, optionally vocals with lyrics) — from a user-supplied specification, with the piece composed by a model at request time rather than retrieved or human-arranged.
- Nearest neighbors: AI Audio Generator (sound material: SFX/foley/ambience), AI Voice Generator (speech performance), Music Production Application / DAW (human arrangement environment), Beat-making / Loop-based Music Production (assembly of pre-made material), royalty-free music libraries (retrieval), Music Streaming Platform (consumption).
- Known prior finding (from processed sibling `ai-audio-generator`): the three-way split inside 04.22 is confirmed by the market — ElevenLabs ships SFX/Music/Voice as separate capabilities, AudioCraft ships AudioGen/MusicGen as separate models, Stable Audio spans SFX+music via output-class tags. The boundary is the **deliverable class** (sound material vs composition vs speech), not product borders. This pass must confirm the music side of that split.

## Research Questions

1. What is the central object — the generation attempt, the track/song, the prompt?
2. What inputs exist — text description, lyrics (own or AI-generated), reference audio/melody, genre/mood pickers, style models?
3. What output forms exist — audio file, stems, MIDI/sheet, full song with vocals vs instrumental?
4. What is the standard workflow from idea to usable piece?
5. What post-generation refinement exists — extend, replace section, edit lyrics, trim/crop, remix, stems, mixer?
6. How are generations kept, compared, shared (library, community/discover surfaces)?
7. Which rules matter — moderation, ownership/commercial terms, training-data posture, usage economics?
8. Where is the boundary vs AI Audio Generator, AI Voice Generator, DAW/music production, beat-making, stock libraries?
9. What variants exist (song factory vs composer tool vs licensing catalog vs open weights vs API)?
10. Historical/market check: does the definition overfit the current text-prompt, full-song-with-vocals, web-app pattern?

## Representative Products

Selected for market representability, documentation quality, different product philosophies, and different customer tiers:

1. **Udio** — creator-focused song generation with vocals and lyrics; web app + iOS; free/paid tiers. (Tier 1: official help center — 5 articles fetched)
2. **AIVA** — composer-oriented assistant (operating since 2016); instrumental compositions, style models, MIDI/audio influence, MIDI/MP3/WAV export; individual/education/enterprise tiers. (Tier 2: official product page; help center unreachable)
3. **SOUNDRAW** — licensing-first royalty-free music generator for creators, artists, and companies; genre/mood → arrangement, in-app mixer, stems, API/enterprise. (Tier 2: official product page incl. FAQ)
4. **Stable Audio (Stability AI)** — audio model family spanning SFX and music via output-class tags; web app, DAW plugin, API, self-hosting, open weights. (Tier 1: knowledge base — evidence shared with the processed sibling research, fetched 2026-09-06)
5. **MusicGen / AudioCraft (Meta)** — open-weights text-to-music model; the research lineage of the Type and the developer-library form. (Tier 1: official repository documentation)

**Suno** — the largest consumer song-generation product — was selected as a candidate but its domain was unreachable from the research environment (help.suno.com and suno.com both timed out; 2 failures, abandoned per source-access rules). It is retained as a known market anchor but **no claims about Suno are made**; the vocals/lyrics side of the Type rests on Udio's documentation.

## Sources

Fetched 2026-09-06:

- Udio — Help Center home: https://help.udio.com/
- Udio — Create Your First Song: https://help.udio.com/en/articles/10715838-create-your-first-song
- Udio — Create a Song with Your Own Lyrics: https://help.udio.com/en/articles/10716221-create-a-song-with-your-own-lyrics
- Udio — Extend Your Song: https://help.udio.com/en/articles/10732568-extend-your-song
- Udio — Edit Your Song Music and Lyrics: https://help.udio.com/en/articles/10732667-edit-your-song-music-and-lyrics
- AIVA — product page (positioning, capabilities, licensing tiers): https://www.aiva.ai/
- SOUNDRAW — product page incl. FAQ (positioning, mixer, stems, plans, API): https://soundraw.io/
- Stability AI — Stable Audio product page + Knowledge Base (prompt guide, moderation, section index): https://stability.ai/stable-audio , https://kb.stability.ai/knowledge-base/stable-audio-3-prompt-guide , https://kb.stability.ai/knowledge-base/why-was-my-prompt-flagged-understanding-content-moderation-in-stable-audio , https://kb.stability.ai/knowledge-base/stable-audio (fetched for the sibling leaf `ai-audio-generator` on the same date; reused as music-side evidence)
- Meta — AudioCraft MusicGen documentation: https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md

Unreachable (recorded per source-access limitation rules): help.suno.com (timeout), suno.com (timeout) — 2 failures, abandoned; help.aiva.ai (transport error), aiva.ai/faq (SPA shell returning the product page) — 2 failures, abandoned; www.udio.com root (JS-rendered shell — substituted by the reachable help.udio.com).

## Product A — Udio

Evidence layer: **A (directly observed)** from the official help center.

### Key observations

- Positioning: AI music generation for creators; the help center is organized into Song Creation (12 articles), Editing (4), Discovering (2), Organizing (1), Community info & contributions (6), Subscriptions/credits/billing (7), Troubleshooting (3), Miscellaneous (10) — creation, refinement, and community are the product's own taxonomy.
- **Core creation flow** ("Create Your First Song"): on the Home page, type a short description (Prompt) of the style, mood, or theme ("Song about New York, jazz"; "Song about a rainy day, 80s pop"); choose a Clip Length (default 32 seconds "great for quick ideas", or 2 minutes; the product generates songs 32 s or 2 min 10 s in length); click Create. A dice icon offers a random idea.
- **Multi-take generation**: "Each prompt generates two songs; you can always tweak your description and try again. Your prompt stays in the text box."
- **Lyrics as a first-class input** ("Create a Song with Your Own Lyrics"): three modes — (1) describe the song's theme and Udio generates lyrics for you; (2) Extended Editor: Write Your Lyrics → Custom, with a "Write for me" button, "Regenerate Lyrics", version navigation (Go Back / Move Forward / View History), and manual editing in a Lyrics Editor; (3) paste your own lyrics for full control.
- **Extend** ("Extend Your Song"): add a new intro, extend a verse, or create a smooth outro. Extend Mode shows controls plus a preview of the original track; the original prompt is pre-filled for consistency but editable ("a mellow acoustic intro could build into a roaring guitar solo"). Placement options: Add Intro / Add Section (before) / Add Section (after) / Add Outro; Crop & Extend trims parts of the original; extensions stack "up to 10 sections total". Longer lyrics can be split into sections; leaving lyrics blank creates an instrumental break. Users can extend songs made by others to remix.
- **Edit** ("Edit Your Song Music and Lyrics", paid-subscriber feature): from the Library, open the editor and choose **Replace Section** (change mood, instruments, or style via a Replacement Prompt, with an "Include original prompt" option) or **Edit Lyrics** (adjust words, lines, or entire verses); highlight the target section with a selection tool; apply. "Small changes can subtly refine your track, while bold edits can create entirely new variations."
- Other observed surfaces: Trimming Your Song; Sessions ("Udio's timeline editing view"); Styles; Prompt Like a Master; Share Your Song; Audio Upload ("create or remix music with your own audio"); iOS app; credits and credit limits (subscription economics).
- Community: extending others' songs is an explicit remix path; Discovering and Community collections exist.

## Product B — AIVA

Evidence layer: **A (directly observed)** for the product page (Tier 2); operational details beyond the page were not verifiable (help center unreachable).

### Key observations

- Positioning: "AIVA is an AI music generation assistant that allows you to generate new songs in more than 250 different styles, in a matter of seconds. Whether a complete beginner or a seasoned professional in music making…" — composer-assistant framing rather than song-factory framing.
- Customizability: "Create your own style models. Upload an audio or MIDI influence. Edit your generated tracks. Download in any file format."
- Output formats: MP3 & MIDI on lower tiers; "ALL file formats" plus high-quality WAV on the top tier — **MIDI export makes the deliverable a composition, not only a recording**.
- Licensing tiers (directly observed, plan-structured):
  - Free: copyright owned by AIVA; no monetization; credit must be given; 3 downloads/month; track durations up to 3 minutes; MP3 & MIDI.
  - Standard: copyright owned by AIVA; limited monetization (YouTube/Twitch/TikTok/Instagram); 15 downloads/month; up to 5 minutes; MP3 & MIDI.
  - Pro: **copyright owned by YOU**; full monetization; 300 downloads/month; up to 5 min 30 s; all formats incl. WAV.
- Audiences: Individuals, Students & Schools, Enterprises (named enterprise users include media/tech brands).
- Longevity: copyright notice "2016–2026" — the oldest product in the sample; predates the 2023 text-to-song wave.
- "Songs created with AIVA — Listen to over 150 tracks generated by AIVA, and arranged by humans" — generated material flowing into human arrangement is an acknowledged pattern.

## Product C — SOUNDRAW

Evidence layer: **A (directly observed)** for the product page incl. FAQ (Tier 2).

### Key observations

- Positioning: "AI Music Generator – Royalty Free Beats"; "100% Copyright-Safe"; "trained only on music we create in-house… Every beat is legally yours to use, monetize, and share." Training-data posture is the core marketing claim (contrast with scraped-data concerns).
- Creation flow (FAQ): "Pick a genre (Hip-Hop, EDM, Lo-Fi, 30+ more), set the mood, and hit Generate. The AI builds the arrangement; you just use SOUNDRAW's in-app editor to refine length, energy, or instruments. No theory, no DAW, no problem."
- Genre blending: "Choose any genres—Hip-Hop + Orchestra, Trap + Lo-Fi—and our AI fuses them into royalty free, studio-ready tracks in seconds."
- **Post-generation editing without a DAW**: the Mixer — "toggle instruments, tweak intensity, set the perfect length… SOUNDRAW rebuilds your track on the spot"; bar-level editing (mute, solo, intensity); timeline customization of energy and length.
- Outputs: MP3; WAV; **STEMS** — "separate WAV files for drums, bass, melody, vocals (if any), and FX. Drop them into Ableton, Logic, FL Studio, or any DAW to tweak mix levels, add plugins, or record vocals on top."
- Discover surface: "AI-recommended song thumbnails" grid — browsing generated tracks.
- Audiences and plans: Creators (background music for videos/podcasts/apps/games; unlimited MP3 downloads); Artists (beats to write over; distribute on Spotify/Apple Music/TikTok; keep 100% of royalties; 10/20/unlimited downloads; stems on higher tiers); Enterprise (10+ employees; API access; unlimited downloads; stems).
- **API form**: "Generate and embed high-quality music instantly through our API" — third-party products (e.g., a video editor) embed generation for their users.
- Adjacent use: SpaceMusic AI — spatial background music for stores/cafés.
- Licensing: perpetual worldwide commercial license; "Anything you make while you're subscribed stays licensed for life, even if you cancel later."

## Product D — Stable Audio (Stability AI)

Evidence layer: **A (directly observed)** via the sibling research (same date); summarized here for the music side.

### Key observations

- Model family "trained on fully licensed data", ranging "from SFX to musical compositions"; full tracks up to ~6 minutes; "Generation is the beginning of the process, not the end" (artist-first controllability).
- Four generation modes: music composition; samples and sound effects; audio-to-audio; inpainting and continuation.
- Output-class steering via tags: `TrackType: Music` (full track), `TrackType: Instrument` (stem), `TrackType: SFX` — **one product implementing both sibling Types via output class**.
- **Voice boundary (direct)**: "designed primarily for instrumental work… not intended to generate intelligible vocals."
- **Moderation rule (direct)**: prompt screening; prompts naming real, identifiable individuals may be flagged/blocked (style-cloning/likeness protection).
- Ownership: "You own your outputs, and can distribute and commercialize them freely"; enterprise indemnification.
- Delivery surfaces: web app (multitrack session view, track FX, tape/splice edits), DAW plugin, Platform API, self-hosted enterprise license, open-weights download.
- Non-determinism documented as a design property.

## Product E — MusicGen / AudioCraft (Meta)

Evidence layer: **A (directly observed)** for the repository documentation; research artifact used as lineage/market-structure evidence.

### Key observations

- "MusicGen: Simple and Controllable Music Generation" — single-stage autoregressive Transformer over a 32 kHz EnCodec tokenizer (4 codebooks); sibling to AudioGen (text-to-sound) in the same library — **the library itself separates text-to-music from text-to-sound**.
- Trained on 20K hours of licensed music (internal 10K tracks + Shutterstock + Pond5).
- Model range: small (300M), medium (1.5B), large (3.3B); melody variants (text+melody → music via chromagram conditioning); stereo fine-tunes.
- API shape: `set_generation_params(duration=8)`; `generate_unconditional(4)`; `generate(descriptions)` with descriptions like 'happy rock', 'energetic EDM', 'sad jazz'; `generate_with_chroma` for melody conditioning from an audio file; audio continuation from a prompt; sampling controls (temperature, top-K, top-P, classifier-free guidance); batch generation; output written to WAV with loudness normalization (−14 dB LUFS).
- Fine-tuning/training pipelines provided; weights non-commercial (per model card, consistent with sibling research).
- No GUI in the library form — the Type can exist as a developer-facing API without any app surface.

## Cross-product Comparison

| Dimension | Udio | AIVA | SOUNDRAW | Stable Audio | MusicGen |
|---|---|---|---|---|---|
| Type center | text/lyrics → song with vocals | style spec → instrumental composition | genre/mood → arranged track (beats/BGM) | prompt/tags → full track or stem | text (±melody) → instrumental music |
| Vocals/lyrics | central (own, AI-generated, or edited) | not the focus (instrumental) | incidental ("vocals (if any)" in stems) | explicitly excluded (instrumental) | not present in observed examples |
| Input | description; lyrics editor; audio upload | style models; audio/MIDI influence | genre + mood pickers; genre blending | prompt + TrackType tags; seed audio | text descriptions; melody/chroma conditioning |
| Output | song (32 s / 2 min 10 s clips, extendable) | MP3/MIDI/WAV; durations capped by plan | MP3/WAV/stems | one-shots → full tracks (~6 min) | WAV clips (e.g., 8 s), loudness-normalized |
| Multi-take | 2 songs per prompt | not observed on page | generate + discover grid | non-determinism documented | batch generation |
| Refinement | extend (intro/sections/outro, ≤10 sections), replace section, edit lyrics, trim, Sessions timeline | edit generated tracks | mixer: instrument toggles, intensity, bar-level mute/solo, length | inpainting, continuation, tape/splice edits | continuation (API) |
| History/library | Library page | not observed on page | discover grid | web-app workspace | files |
| Surfaces | web + iOS | web + download | web + API + enterprise | web + DAW plugin + API + self-host + open weights | Python library / HF demo |
| Moderation | not fetched | not fetched | not fetched | prompt screening; real-person naming blocked | n/a (open weights) |
| Ownership terms | plan-dependent (paid features) | vendor-retained copyright on low tiers; user copyright on Pro | perpetual worldwide commercial license; 100% royalties | user owns outputs; enterprise indemnification | weights CC-BY-NC (non-commercial) |
| Training-data posture | not fetched | not stated on page | in-house-produced catalog only | fully licensed data | licensed data (internal + Shutterstock/Pond5) |

**Stable commonalities (Layer B — cross-product):**

1. **Specification-driven composition**: every product takes a user-supplied specification of the desired music — a natural-language description (Udio, Stable Audio, MusicGen), genre/mood selections (SOUNDRAW), or style models plus audio/MIDI influence (AIVA). Every product publishes prompting/creation guidance.
2. **On-demand model composition**: the piece is composed by a model at request time; none of the sampled products retrieves finished tracks from a fixed catalog as the primary mechanism (SOUNDRAW's Discover grid is secondary to generation; its catalog claim concerns training data, not retrieval).
3. **Bounded musical work as deliverable**: every product returns a discrete, playable piece — a track/song — exportable in standard formats (MP3/WAV; stems in some; MIDI in AIVA).
4. **Composition scope**: the deliverable is a musical piece with arrangement/temporal structure — distinct from sound material (AudioGen vs MusicGen as separate models; ElevenLabs SFX vs Music as separate capabilities; Stable Audio's TrackType tags) and from standalone speech performance.
5. **Multi-attempt iteration**: multiple takes per attempt (Udio: two songs; MusicGen: batch; Stable Audio: documented non-determinism); generate → audition → regenerate is the expected loop.
6. **Post-generation refinement inside the product**: extend/continuation (Udio, Stable Audio, MusicGen), section replacement/inpainting (Udio, Stable Audio), lyric editing (Udio), instrument/intensity mixing (SOUNDRAW), trimming (Udio). Refinement is generation-adjacent, not a full DAW.
7. **Downstream handoff**: pieces travel into video, games, podcasts, releases, or DAW sessions (stems explicitly for DAW import in SOUNDRAW; MIDI in AIVA; plugin form in Stable Audio).
8. **Usage economics and plan-bound rights**: credits/subscriptions are standard; commercial rights vary meaningfully — vendor-retained copyright with attribution (AIVA Free) → limited monetization (AIVA Standard) → full user copyright (AIVA Pro) → perpetual commercial license (SOUNDRAW) → user-owned outputs (Stable Audio) → non-commercial weights (MusicGen).
9. **Multiple delivery surfaces**: web app is dominant but not definitional — iOS app (Udio), API (SOUNDRAW, Stable Audio, MusicGen), DAW plugin (Stable Audio), open weights (Stable Audio, MusicGen).
10. **Training-data posture as a product feature**: in-house catalog (SOUNDRAW), fully licensed data (Stable Audio, MusicGen) — provenance is marketed, implying it matters to buyers.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

```text
User-supplied specification of desired music
  → on-demand model composition of a musical piece
    → bounded musical work as the deliverable (playable, exportable)
      → composition scope: arranged music with temporal structure —
        as distinct from sound material (AI Audio Generator)
        and standalone speech performance (AI Voice Generator)
```

Four properties. Remove any one and the Type stops being recognizable:

- **Specification-driven** — the user states what music they want (description, lyrics, references, style/genre choices) rather than performing, programming, or assembling it themselves. Without a specification step it is a production environment (DAW) or a library.
- **On-demand model composition** — the arrangement is generated by a model at request time. Remove this and the product is a royalty-free/stock music library (search + download of pre-existing recordings).
- **Bounded musical work as deliverable** — a discrete piece with defined extent that can be auditioned, compared across attempts, and exported. Remove this and it is a generative ambient stream or radio surface.
- **Composition scope** — the output is a musical piece (arrangement, sections, progression; optionally vocals with lyrics). Remove this restriction and the leaf collapses into its siblings: sound material → AI Audio Generator; spoken/sung verbal performance as such → AI Voice Generator.

### L1 — Common Mature Structure

Present in most mature commercial products; not required for the definition:

- specification controls: genre/style selection, mood/theme description, instrumental toggle, clip length/duration
- lyrics handling: own lyrics, AI-generated lyrics, lyric editing (in vocal-song products)
- reference inputs: audio upload, melody conditioning, MIDI influence, custom style models
- multi-take generation per attempt; non-determinism as an intended property
- generation history/library with comparison and download
- post-generation refinement: extend (intro/sections/outro), replace section (inpainting), edit lyrics, trim/crop, instrument/intensity mixing, stems
- prompting/creation guidance as product content
- multiple delivery surfaces: web app, mobile app, API, DAW plugin
- standard download formats (MP3/WAV; stems; MIDI in composer-oriented products)
- prompt/content moderation in hosted commercial products
- credit/subscription economics; commercial-use rights bound to plan or license
- community/discovery surfaces (browse, share, remix others' pieces)

### L2 — Variant / Optional Structure

- vocal songs with lyrics (song-factory pole) vs instrumental-only (composer/BGM pole)
- output forms beyond stereo audio: stems, MIDI (composition-level deliverable)
- editing depth: none → trim → section replace → bar-level mixer → timeline session view
- input modality breadth: text only vs multimodal (audio upload, melody conditioning, MIDI influence)
- business model: consumer subscription; licensing-first catalog posture; API/enterprise embedding; open weights/self-host
- training-data posture as a marketed feature (in-house vs licensed corpora)
- custom style models / fine-tuning on customer material
- adjacent uses: background music for physical spaces; generation embedded in third-party editors via API

### L3 — Vendor-specific (Research Notes only)

- Udio: 32 s default / 2 min 10 s clip lengths; two songs per prompt; extend up to 10 sections; Edit feature paid-only; Sessions timeline view; dice random idea; "Write for me" lyrics; iOS app; credits system.
- AIVA: 250+ styles; plan download quotas (3/15/300 per month); plan duration caps (3 min / 5 min / 5 min 30 s); copyright ownership per plan; MP3+MIDI vs all-formats+WAV; "arranged by humans" showcase.
- SOUNDRAW: bar-level mixer (mute/solo/intensity); stems = drums/bass/melody/vocals(if any)/FX; plan download caps (10/20/unlimited); SpaceMusic AI; enterprise API; in-house training-data claim; aiformusic supporter.
- Stable Audio: `TrackType:`/`Format:`/`Genre:` tag syntax; ~6-minute maximum on Large; `init_noise_level` 0.3–0.9; tape ops (reverse/stutter/freeze); model tiers Large/Medium/Small/Small SFX.
- MusicGen: model sizes 300M/1.5B/3.3B; 32 kHz EnCodec, 4 codebooks at 50 Hz; −14 dB LUFS normalization; chroma/melody conditioning; top-K/top-P/temperature; CC-BY-NC weights; 20K hours licensed training data.

## Vendor-specific Findings

- Udio's section-placement extend model (Add Intro / Add Section before/after / Add Outro, ≤10 sections) is a product-specific refinement grammar — evidence that structured section-level refinement exists in the Type, not a canonical structure.
- SOUNDRAW's bar-level mixer (mute/solo/intensity with on-the-spot rebuild) is a product-specific editing depth.
- AIVA's MIDI export and plan-bound copyright ownership are product-specific; MIDI as an output form is a variant signal, not a requirement.
- Stable Audio's tag syntax is a vendor-specific prompting convention (shared finding with the sibling research).
- SOUNDRAW's "trained only on in-house music" posture is a vendor-specific training-data claim.

## Boundary Findings

1. **vs AI Audio Generator (sibling)**: same generation loop, different deliverable class. Test: if the primary deliverable is a musical composition (arrangement, sections, full track, possibly vocals), it is this Type; if it is sound material (one-shots, foley, ambience, stems as material), it is the audio sibling. Market evidence: AudioCraft ships AudioGen and MusicGen as separate models; ElevenLabs ships SFX and Music as separate capabilities with separate terms; Stable Audio spans both via output-class tags — one product can implement both Types, which is bundling, not merger. Musical-element samples (drum loops, stabs) sit on the audio side; a full arrangement sits here.
2. **vs AI Voice Generator (sibling)**: sung vocals inside a generated song are part of the composition deliverable; the voice Type delivers spoken/verbal performance of given text as such. Test: is the deliverable "a song" or "a voice performance"? (ai-voice-generator leaf not yet processed; this boundary is recorded for the joint review flagged in STATUS.)
3. **vs Music Production Application / DAW (04.10)**: the DAW is a human arrangement/production environment (record, program, arrange, mix in a timeline); this Type composes from a specification. Products blur at the edges: SOUNDRAW's mixer ("no DAW needed"), Udio's Sessions timeline view, Stable Audio's DAW plugin. Test: remove the model → a DAW remains a DAW; remove the arrangement environment → the generator remains a generator. The generator's editing serves the generation loop; the DAW's generation (if any) serves the production.
4. **vs Beat-making / Loop-based Music Production (04.10)**: those Types assemble user-selected loops/samples into tracks; this Type composes the material itself. SOUNDRAW overlaps in market (beats) but generates the arrangement rather than assembling pre-made loops.
5. **vs royalty-free/stock music library (no dedicated leaf)**: retrieval vs synthesis. A library delivers pre-existing recordings found by search; a generator has no recording until the model composes one. SOUNDRAW is instructive: its marketing leans on license safety (library-like promise) while the mechanism remains on-demand generation.
6. **vs Music Streaming Platform (27)**: consumption of recorded catalogs vs creation of new pieces. Some products add public discover/share surfaces, but the primary object remains the user's own generation.
7. **vs algorithmic/auto-accompaniment composition tools (historical, no leaf)**: rule-based generation from user-supplied harmony is a functional ancestor; the modern Type is model-based composition from natural-language/multimodal specification. Recorded as a lineage observation, not a Type claim.

## Historical / Market-Sample Check

The Type is young (AIVA since 2016; the commercial text-to-song wave from ~2023; research models 2023). There is no long pre-AI product generation, so the check is applied in the overfitting direction:

- Do not define the Type by **text-prompt-only input** — AIVA uses style models plus audio/MIDI influence; MusicGen conditions on melody/chroma; Udio accepts audio uploads.
- Do not define the Type by **full-song-with-vocals output** — four of five sampled products are instrumental-focused; vocals/lyrics are a variant pole (Udio), not the definition.
- Do not define the Type by the **web-app surface** — API (SOUNDRAW, Stable Audio, MusicGen), DAW plugin (Stable Audio), mobile app (Udio), and open-weights library forms all exist.
- Do not define the Type by **pop-song form** — AIVA's center of gravity is cinematic/classical-style instrumental composition; SOUNDRAW's is beats/BGM.
- Do not define the Type by a specific **model technique** — autoregressive LM (MusicGen) and diffusion-family (Stable Audio) both present; the defining property is model composition from a specification, technique-agnostic.
- Do not define the Type by **stereo-audio-only deliverables** — MIDI (AIVA) and stems (SOUNDRAW, Stable Audio) exist as output forms.

Reverse check: a DAW or synth generates sound but from human performance/programming, not from a specification of desired music — excluded by the specification invariant. A stock library delivers music but retrieves rather than composes — excluded by the on-demand invariant.

## Uncertainties

- **Suno under-evidenced**: the largest consumer song-generation product was unreachable (2 timeouts, abandoned). Claims about it — and about the consumer song-factory segment generally beyond Udio — are not made. The vocals/lyrics pole rests on Udio's documentation alone (single-product evidence for that pole; marked accordingly).
- **Moderation coverage**: directly observed only in Stable Audio's KB (real-person naming blocked). Udio's and SOUNDRAW's moderation behavior was not fetched — no claims made for them.
- **Provenance/watermarking of outputs**: not verified for any sampled music product — no claim made.
- **AIVA operational depth**: "edit your generated tracks" and style-model creation are observed on the product page, but the editing model's details (chord/track-level editing) were not verifiable (help center unreachable) — kept generic.
- **Udio Sessions timeline view**: existence observed (article title); behavior not fetched — treated as an editing-depth variant signal only.
- **Pricing specifics**: plan structures observed for AIVA and SOUNDRAW on their pages; Udio credit mechanics not fetched — kept generic in the final document.
- **Vocal quality/limits, genre coverage claims**: marketing-level only; not asserted.

## Final Synthesis

The AI Music Generator is a **composition-source application**: the user specifies the music they want — a description of style/mood/theme, optionally lyrics, reference audio or melody, genre/style choices — a model composes a musical piece on demand, and the deliverable is a bounded musical work returned as audio (and, in some products, stems or MIDI), refined through a generate → audition → refine loop (extend, replace section, edit lyrics, trim, mix) and exported into downstream work (video, games, podcasts, releases, DAW sessions). Its identity is defined by four invariants — specification-driven input, on-demand model composition, bounded musical-work deliverable, composition scope — and everything else (lyrics handling, reference inputs, multi-take batches, refinement tooling, libraries, moderation, plan-bound rights, APIs, plugins, open weights) is mature structure or variant. The market confirms the three-way split inside Generative Audio from the music side: the same vendors that operate sound-effect and voice generation keep music composition as a distinct capability, model, or output class. The strongest structural boundary is twofold: against the royalty-free library (retrieval vs on-demand composition) and against the human music-production family (who composes — a model from a specification, or a person in an arrangement environment).
