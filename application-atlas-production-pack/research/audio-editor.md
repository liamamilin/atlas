# Research Notes — Audio Editor

Research date: 2026-09-06
Methodology: v1.1 (update-v1/WORKFLOW_v1.1.md, WRITING_GUIDE_v1.1.md)

---

## Research Goal

Understand the Application Type **Audio Editor** (DIRECTORY 04.09 Audio) from real products: what its world consists of, what users do with it, how editing work flows, which rules constrain it, and where it borders Digital Audio Workstation / DAW, Podcast Editing Application, and Audio Restoration Application (the other three leaves of 04.09).

## Initial Boundary

Temporary hypothesis before research:

- Core use: editing **recorded audio** (a file or a capture) — cutting, trimming, splicing, cleaning, processing — as opposed to composing music from instruments/loops.
- Users: podcasters, voice-over artists, musicians doing quick edits, radio/producers, archivists, general consumers.
- Nearest neighbors: DAW (music production), Podcast Editing Application, Audio Restoration Application, Music Production Application, AI Audio Generator (generative, 04.22).
- Likely boundary: the audio editor works on **audio material that already exists** and presents it as **waveform**; the DAW works on a **composition** (tracks + MIDI + instruments + mixing).
- Unknowns: is multitrack mixing part of this Type or drift toward DAW? Is recording part of the definition? Is spectral editing definitional? Is the project container definitional or just common?

## Research Questions

1. What is the central object — the audio file, a project, a recording?
2. What does "editing" concretely mean (operations, targets, model)?
3. Destructive vs non-destructive processing: how do products implement and expose it?
4. How do effects work (dialog+apply, realtime stack, preview, bypass, render/bounce)?
5. Is recording part of the Type's core?
6. Is multitrack arrangement part of the Type's core?
7. What interfaces does the user face (waveform pane, spectrogram, effect panels, export, batch)?
8. What lifecycle: acquire → edit → save → export? What are the states?
9. What rules/constraints matter (formats/codecs, sample rate/bit depth, project vs export, undo limits, long files)?
10. Where exactly does the boundary to DAW / Podcast Editing / Audio Restoration lie ("remove/add what to become the other Type")?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Philosophy / Tier | Documentation used |
|---|---|---|
| Audacity | free, open source, cross-platform; the archetypal general-purpose audio editor; hobbyist/prosumer | support.audacityteam.org (official support docs, GitBook, markdown-fetched) — Tier 1 |
| ocenaudio | free, lightweight "stays out of your way" editor for quick edit + analysis | ocenaudio.com (features + about pages) — Tier 2 |
| TwistedWave | paid, fast minimal editor; Mac/Windows/iOS/browser; pro-leaning single-file editor | twistedwave.com (product pages) — Tier 2 |
| WavePad (NCH) | freemium consumer/prosumer editor; Windows/Mac/mobile | nch.com.au/wavepad (product + features pages) — Tier 2 |

Considered and **excluded due to source inaccessibility** (WebFetch failed; per source-access rule, no memory-based claims used):

- Adobe Audition — helpx.adobe.com and adobe.com/products both timed out (2 attempts).
- Steinberg WaveLab — steinberg.net/wavelab is a JS-only page; steinberg.help 404 / JS app (2 attempts).

Consequence: professional-suite-tier (subscription creative-suite) and mastering-editor-tier claims are **not** evidence-backed in this pass. All assertions below rest on the four accessible samples.

## Sources

- Audacity Support (official): https://support.audacityteam.org/ — llms.txt index; pages fetched as .md:
  - /basics/audacity-editing.md (Editing audio)
  - /basics/saving-and-exporting-projects.md
  - /audio-editing/using-realtime-effects.md
  - /special-uses/expected-uses.md
- ocenaudio official site: https://www.ocenaudio.com/ (start page, /features, /whatis)
- TwistedWave official site: https://twistedwave.com/ (home/product page)
- WavePad official site: https://www.nch.com.au/wavepad/index.html
- (attempted, inaccessible) https://helpx.adobe.com/audition/user-guide.html ; https://www.adobe.com/products/audition.html ; https://www.steinberg.net/wavelab/ ; https://steinberg.help/wavelab/v13/en/

## Product Observations

### Audacity (Evidence layer A — official support docs)

- Self-description: "easy-to-use, multi-track audio editor and recorder for Windows, macOS, GNU/Linux". The expected-uses page states: "**Audacity is an audio editor with limited DAW functionality**." (Direct vendor statement of the DAW boundary — high value.)
- Expected uses list: recording audio incl. digitizing analog media; applying effects; installing plugins; analyzing audio; producing podcasts, audio books, songs; saving projects to disk or cloud; exporting to various formats.
- Import: drag & drop or File > Import; proprietary formats (M4A, WMA) require installing FFmpeg (codec extension model).
- Waveform is the primary representation: amplitude blobs = loudness, spikes = clicks/transients; "use the waveform to quickly find your way around an audio file."
- Editing model: select a region by click-drag → Delete; **clips** = pieces of audio inside the project that can be moved independently (between tracks, into empty space to create a track); split tool; trim via handles; **trimming is non-destructive — un-trim available**; per-clip speed and pitch change (with "optimize for voice" formant option).
- Effects in two modes:
  - **Realtime effects**: applied to an entire track; "they won't change the source waveform"; effect stack with bypass per effect; master effects applied to the mixed output; stack auto-applied at export; "Mix and Render" bounces the stack into the waveform.
  - Offline/dialog effects applied destructively to selected audio (implied by manual structure; noise reduction, compressor/limiter pages).
- Plugin formats: Audio Units (macOS), VST3, VST, LV2, LADSPA.
- Noise reduction & removal section: "core to most audio cleanup operations"; repair pages: re-recording a section (punch-in), removing clicks & pops.
- Loudness normalization targeted at "podcast platforms, television/radio programmes and some websites" (use-case evidence).
- Macros (formerly Chains): chain multiple commands to automate repetitive tasks; applicable to the project **or a set of files** (batch).
- Spectral analysis: spectrogram view per track, Plot Spectrum.
- Project vs export: saved project (.aup3) "has the most information"; lets you change realtime effects later or un-trim clips; export produces MP3/WAV/OGG etc. (more via FFmpeg). Cloud saving to audio.com with backups/versioning and optional "mixdown" previews. Warning not to keep active projects on slow/network storage.
- Music-oriented extras: music view, beat/bars alignment, loops; splitting a long recording into separate tracks (LP/CD digitization); audiobook mastering suite for ACX compliance.
- Recording: mic recording with level setting; desktop/system audio recording; latency compensation.

### ocenaudio (Evidence layer A — official site)

- Self-description: "cross-platform, easy to use, fast and functional audio editor… for people who need to **edit and analyze audio files** without complications"; originated from a research group needing format support, spectral analysis, and signal generation.
- Waveform view plus "powerful and complete spectrogram view"; spectrogram settings apply in real time; views can be combined.
- VST plugin effects support; **real-time preview**: "you hear the processed signal while adjusting the controls"; effect window includes a miniature view of the selected signal.
- **Multi-selection**: several disjoint regions selected simultaneously; listen/edit/apply effects to all of them at once (e.g., normalize only interview speech segments).
- Large-file handling: "no limit to the length or quantity of audio files"; background processing keeps UI responsive; copy/cut/paste near-instant on multi-hour files.
- Cross-platform with uniform feature set (Windows/macOS/Linux).

### TwistedWave (Evidence layer A — official site)

- Self-description: "Record, edit, master, batch-process and convert audio on Mac, Windows, iPhone & iPad, and right in your browser." (browser-based edition = web surface variant).
- Workflow verbs: record (with drop markers on the fly "ideal for podcasts and voice-over"), master ("equalize, compress and limit with hundreds of Audio Unit and VST plugins in flexible effect stacks"), convert (read/write dozens of formats: wav, aiff, mp3, mp4, flac, ogg…), batch process (effects, fades, conversions "across thousands of files, or whole folder hierarchies").
- Quality positioning: "up to 32-bit / 192 kHz, multichannel editing, best-in-class ZTX time-stretch and pitch-shift" (product-specific DSP facts).
- **Speech recognition editing**: recognizes speech, syncs script with audio; select words → selects audio and vice versa ("edit by reading the words") for audiobooks/long recordings.
- **Video sync**: open a movie, picture plays along; cut/reverse/slow audio and frames follow; save movie with edited soundtrack.
- Performance positioning: instant zoom/scrub on multi-hour files; effects run in background.
- Multichannel waveform display shown in product imagery.

### WavePad (Evidence layer A — official product page; Tier 2)

- Self-description: "full-featured professional audio and music editor for Windows and Mac"; "cut, copy and paste parts of recordings, and then add effects like echo, amplification and noise reduction"; "WAV or MP3 editor" plus VOX, GSM, WMA, real audio, M4A, AU, AIF, FLAC, OGG and more.
- Editing tools: cut, copy, paste, delete, insert, silence, auto-trim, compression, pitch shifting.
- Effects: amplify, normalize, equalizer, envelope, reverb, echo, reverse; restoration: noise reduction wizard, click/pop removal, dereverb, echo removal.
- VST and DirectX plugin support; effect chain tool.
- Batch processing: "apply effects and/or convert thousands of files as a single function".
- Navigation for long files: scrub, search, **bookmarks and regions** "to easily find, recall and assemble segments of long audio files".
- Advanced tools: spectral analysis (FFT), TFFT, beat detection, peak finder; voice tools (vocal isolation/removal, voice change, text-to-speech; AI-powered noise removal/enhancement).
- Formats/quality: "sample rates from 6 to 192kHz, stereo or mono, 8, 16, 24 or 32 bits".
- Video-related: "Edit the audio from your video files"; export audio to video with waveform/FFT visualization.
- History: "Automatic backup and version history to easily undo changes and restore previous edits"; markets "non-destructive audio editing".
- Ecosystem: integrates with MixPad "Multi-Track Audio Mixer" (multitrack mixing sold as a separate NCH product — boundary evidence: the editor stays file-centric; multitrack mixing is the sibling product).
- Business model: free for non-commercial use; Master's edition upgrade.
- Typical applications listed: trim sound bites, reduce vocals, cut together radio/podcast audio, ringtones, voiceovers, restore audio, normalize.

## Cross-product Comparison

| Structure / capability | Audacity | ocenaudio | TwistedWave | WavePad | Assessment |
|---|---|---|---|---|---|
| Audio file/recording as central object | ✔ (import/record) | ✔ (edit audio files) | ✔ (record/edit) | ✔ (open/record) | **Defining** — all four |
| Waveform as primary working view | ✔ | ✔ (+spectrogram) | ✔ (multichannel) | ✔ | **Defining** — all four |
| Direct region-based edit ops (select/cut/split/trim/move/silence) | ✔ | ✔ (multi-selection) | ✔ | ✔ | **Defining** — all four |
| Save/export as audio file; format choice | ✔ (+project) | ✔ | ✔ (dozens) | ✔ (50+) | **Defining** — all four |
| Effects processing incl. level tools | ✔ | ✔ (VST) | ✔ (AU/VST stacks) | ✔ (+DirectX) | Common (none without; but a pure trimmer would still be an editor) |
| Real-time effect preview / realtime stack vs destructive apply | ✔ (realtime track stack + Mix and Render) | ✔ (real-time preview) | ✔ (background effects) | ✔ (non-destructive claim) | Common; both processing models coexist |
| Plugin extension (VST/AU/LV2/DirectX) | ✔ | ✔ | ✔ | ✔ | Common |
| Recording input | ✔ | (not emphasized) | ✔ | ✔ | Common (not defining: ocenaudio still fully an editor) |
| Noise reduction / repair (clicks, hum, reverb) | ✔ | (analysis emphasis) | (mastering emphasis) | ✔ (wizard) | Common |
| Spectrogram / spectral analysis | ✔ | ✔ | (display only implied) | ✔ (FFT/TFFT) | Common |
| Time/pitch manipulation | ✔ (per-clip + optimize for voice) | — | ✔ (ZTX; product-specific engine) | ✔ | Common |
| Project container vs flat file editing | ✔ (.aup3/cloud) | — | — | — (backup/version history instead) | Common-to-optional; not defining |
| Multitrack arrangement of clips | ✔ (clips between tracks; "limited DAW") | — | (multichannel, not multitrack-mixing-first) | — (sibling product MixPad) | **Common-to-optional; varies; not defining** |
| Batch processing / macros | ✔ | — | ✔ | ✔ | Common |
| Markers / bookmarks / regions | ✔ (labels; markers during recording in TW) | — | ✔ (drop markers) | ✔ | Common |
| Long-file performance positioning | ✔ (projects need fast storage) | ✔ (hours-long, background) | ✔ (multi-hour scrub) | ✔ (bookmarks/regions) | Common concern |
| Text/transcript-based editing | — | — | ✔ (product-specific) | (TTS adjacent) | Product-specific (single source) |
| Video-linked audio editing | — | — | ✔ (video sync) | ✔ (edit audio from video) | Optional (2/4) |
| Cloud projects / sharing | ✔ (audio.com) | — | — | — | Product-specific/optional |
| Browser edition | — | — | ✔ | — | Surface variant |
| Mobile editions | — | — | ✔ (iOS) | ✔ (iOS/Android/Kindle) | Surface variant |
| Business model | free/OSS | free | paid | freemium | Variant |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant

Four properties. Removing any one stops the product from being recognizable as an Audio Editor:

1. **Recorded audio as the working material** — the object being edited is an existing sound recording (an imported audio file, a captured recording, or the audio track of a video). The editor does not generate the material from composition data (MIDI/instruments); it edits sound that has been captured or delivered as audio.
2. **Waveform-based visual working surface** — the audio is presented as amplitude-over-time (waveform), the canonical way users "see" sound; spectral views complement but do not replace it.
3. **Direct edit operations on the sound content** — the user selects regions of the audio and applies operations (cut, split, trim, move, splice, silence, process) that change the sound itself.
4. **Persistent audio output** — the result is saved/exported as an audio file (optionally alongside a project container preserving the editable state).

Notes:
- Multitrack arrangement, effects, recording, restoration, batch, analysis are all common but not required to recognize the Type (ocenaudio without recording emphasis, single-file editors like WavePad/TwistedWave editions remain paradigm editors).
- Historical check (older / platform-native / regional products): the four properties hold for classic desktop editors and for minimal platform-native forms (e.g., a phone voice-memo trimmer: waveform + trim + save). Phone/app-store distribution, plugin ecosystems, multitrack views are modern accretions, not part of the definition.

### L1 — Common Mature Structure

Present in most mature modern editors; expected by users but not definitional:

- Effects processing: level tools (amplify/normalize/fade), equalizers, dynamics (compressor/limiter), reverb/echo, reverse; effect chains/stacks; bypass.
- Two processing models coexisting: **destructive/offline apply** (bakes into audio; undo-able) and **realtime/non-destructive** (previewed, doesn't change source waveform; rendered on export or explicit bounce/mix-and-render).
- Plugin extensibility (VST is the common denominator; AU/LV2/LADSPA/DirectX vary by platform/vendor).
- Recording input (microphone, system/desktop audio) with level control.
- Audio repair/cleanup: noise reduction, click/pop removal, de-reverb.
- Spectral view / spectral analysis (spectrogram, FFT-based analysis).
- Time/pitch manipulation (speed change, time-stretch, pitch shift, voice/formant optimization).
- Broad format import/export; codec-extension mechanism when proprietary formats are involved (FFmpeg pattern).
- Navigation of long recordings: zoom/scrub, markers, bookmarks, regions, labels.
- Undo/history; some products add automatic backup/version history.
- Batch processing across many files (batch panel or macro/command chains).
- Some form of multitrack arrangement view (clips across tracks) — present in several, absent or shallow in others; vendors may sell a separate mixer product instead.
- Performance posture for multi-hour files (background processing, efficient memory).

### L2 — Variant / Optional Structure

Depends on segment, platform, business model, era:

- Surface: desktop native (Win/mac/Linux), mobile (iOS/Android), browser edition.
- Business model: free/OSS, freemium (free non-commercial + paid edition), one-time purchase, subscription suite member.
- Text/transcript-based editing (speech recognition synced to waveform) — emerging, single-source in sample.
- Video-linked editing (audio edits reflected in picture; export movie with edited soundtrack).
- Cloud projects / online sharing / collaboration hooks.
- Domain packs: audiobook mastering compliance, loudness targets for broadcast/podcast platforms, LP/tape digitization workflows, loop/music views, ringtone creation.
- AI-assisted features (AI noise removal, TTS, voice changing) — emerging.
- Destructive-vs-nondestructive default posture and depth of un-trim/recoverability.
- Multitrack mixing depth (from clip arrangement up to "limited DAW" behavior).

### L3 — Vendor-specific (kept out of the final document)

- Audacity: .aup3 project format; audio.com cloud + mixdown previews; Macros/Chains; ACX audiobook mastering suite; Muse Hub; FFmpeg-on-demand; fixed latency-compensation default; OpenVINO AI models; "Mix and Render" naming.
- ocenaudio: Ocen Framework; miniature in-effect selection view; uniform cross-platform feature parity claim.
- TwistedWave: ZTX time-stretch/pitch-shift engine; speech-script sync editing; per-platform complete editors incl. iOS.
- WavePad: Master's edition; SFX library; MixPad sibling integration; DirectX plugin support; TFFT tooling; voice-changing tools.

## Boundary Findings

**vs Digital Audio Workstation / DAW** (same directory family):
- DAW's world: composition-centric — multitrack recording of many sources, MIDI sequencing, virtual instruments, loop construction, mixing console, plugin instruments, tempo maps. Audio editor's world: material-centric — existing recordings edited on a waveform.
- Vendor-confirmed: Audacity calls itself "an audio editor with limited DAW functionality" and its multitrack features (clips, mixing, master effects) are exactly the "limited DAW" side. NCH sells WavePad (editor) and MixPad (multitrack mixer) as separate products.
- Test: add MIDI/virtual instruments/loop-based composition as the primary object → becomes a DAW. Remove recorded-audio-file editing → not an audio editor. Multitrack alone does NOT flip the type; instruments/composition do.

**vs Podcast Editing Application** (same family):
- Every sampled editor names podcasts/radio/voice-over as typical uses; none is podcast-first. A podcast-first product restructures around the podcast pipeline (episodes as units, text/transcript surfaces, music beds, chapters, publication) — that is a domain variant built on this Type's core. Whether it deserves independent-Type status is a taxonomy question (see STATUS Boundary Issues note); the audio-editing core remains the substrate.

**vs Audio Restoration Application** (same family):
- Restoration tools (noise reduction, click removal, de-reverb) are standard capabilities inside every sampled editor. A restoration-first product inverts the emphasis (diagnosis/repair as the whole world, measurement-first). The shared core is identical; the difference is emphasis and depth. Recorded as sibling leaf.

**vs Music Production Application / Virtual Recording Studio (04.10) / Beat-making (04.10)**:
- Those center on composing/arranging music (instruments, loops, recording of music sessions). The audio editor consumes finished recordings. Loop/music views inside editors (Audacity) are optional drift toward 04.10.

**vs AI Audio Generator (04.22)**:
- Generator: description → synthesized clip (creation of material). Editor: existing material → modified material. TwistedWave/WavePad's AI *cleanup* features are editing-side; generation is a different Type.

**vs Audio conversion utilities**:
- Format conversion is a side capability inside editors (TwistedWave "convert", WavePad batch convert). A converter without editing (no waveform edit operations) is a utility, not this Type.

**"去掉什么就变成另一个 Type" 判据**:
- 去 waveform/direct-edit、留 composition+instruments → DAW。
- 加 episode/publishing/text-first structure → Podcast Editing。
- 把 repair 从 capability 升为全部世界 → Audio Restoration。
- 把 material 从"已录好的"换成"模型生成的" → AI Audio Generator。

## Uncertainties

- Professional-suite-tier editors (Adobe Audition) and mastering-focused editors (Steinberg WaveLab) could not be fetched this pass. Their structural fit is assumed from the four accessible samples only; assertions about the high-end tier (multitrack depth, spectral repair, mastering meters) are not evidence-backed here and were kept out of the final document.
- Whether "project container" is definitional: sample suggests no (two of four editors are file-centric without a proprietary project format). Kept out of L0.
- Emerging text-based (transcript) editing may push the Type's surface; single-source in sample — watch for future re-research.
- Exact numeric limits (sample-rate ceilings, file-size limits, undo depths) are vendor facts; intentionally excluded from the final document.

## Final Synthesis

The Audio Editor is a **material-centric editing application**: it takes a sound recording that already exists, shows it as a waveform over time, lets the user select and directly operate on regions of that sound (cut/split/trim/move/silence), process it (level, EQ, dynamics, repair, time/pitch), and persist the result as audio files. A project container for unfinished work is common. Realtime effects, recording, repair, spectral analysis, batch processing, markers, and multitrack clip arrangement are the standard capability set of mature products. The Type's edge is against the DAW (composition + instruments vs recorded material), against Podcast Editing (domain pipeline vs generic material editing), and against Audio Restoration (emphasis inversion of a shared core).
