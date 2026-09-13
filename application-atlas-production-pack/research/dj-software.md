# Research Notes — DJ Software

Research date: 2026-09-07
Leaf: DJ Software (DIRECTORY 04.12 DJ & Performance)
Slug: dj-software

## Research Goal

Understand the Application Type **DJ Software** from real products: what its world consists of (library, decks, mixer, performance tools), what users do inside it, how the performance workflow runs, which rules constrain it, and where its boundaries sit against the sibling leaf **Live Music Performance Software** (04.12), the production family (04.09–04.10: DAW, Audio Editor, Beat-making, Loop-based Production), and consumption surfaces (Music Streaming Platform).

Note: the sibling leaf **Live Music Performance Software** (04.12) is unprocessed in STATUS.md. The DAW research pass (2026-09-07) flagged the DJ/Live-Performance seam: "DJ software performs finished tracks; live performance software centers the show." This pass holds that boundary from the DJ side and recommends a joint review when the sibling leaf is processed.

## Initial Boundary (hypothesis before research)

- Core use: performing a continuous music program in real time by mixing pre-existing finished recordings — selecting, tempo-aligning, and blending one track into the next.
- Primary users: DJs (club/mobile/radio/bedroom), from hobbyist to professional.
- Nearest neighbors: DAW (produces the tracks), Live Music Performance Software (performs musical material, not finished tracks), Audio Editor (edits recordings as files), Music Streaming Platform (consumption), Media Player (playback without mixing).
- Key unknowns going in: Is the library definitional or just common? Is tempo/pitch control definitional or sync-era baggage? Is headphone cueing definitional? Where exactly does "software performance" end and "hardware control utility" begin (rekordbox export workflow)? Is Auto DJ part of the definition or an automation add-on?

## Research Questions

1. What objects make up a DJ software's world? (deck, mixer/channel, crossfader, library/crate/playlist, waveform, cue points, loops, FX, sampler)
2. What is the end-to-end workflow? (prepare → set up audio → perform → record/broadcast → history)
3. What does "beatmatching" mean operationally, and what do sync features change?
4. What audio-routing rules matter? (master vs headphones/pre-listen, external mixer mode, gain staging)
5. How do products integrate hardware? (controllers, DVS timecode vinyl, club players/HID, MIDI learn)
6. What automation exists? (Auto DJ / Automix)
7. Where is the boundary vs DAW / Live Performance / Audio Editor / Media Player / Streaming?
8. Would older or non-software-era DJing (two turntables + mixer) still fit the abstracted definition?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / tier | Source type |
|---|---|---|---|
| Serato DJ Pro | Serato (NZ) | Pro club/turntablist standard; hardware-unlock licensing; expansion suite | Product page + FAQ (Tier 2) |
| rekordbox | AlphaTheta (Pioneer DJ) | Hardware-ecosystem software; library preparation + export to club players; cloud/mobile | Product site (Tier 2) |
| VirtualDJ | Atomix | Long-running broad-audience software; huge feature surface incl. video/karaoke | Official user manual (Tier 1) |
| djay | Algoriddim | Consumer/mobile-first, cross-platform, streaming-native, AI stem separation | Product pages (Tier 2) |
| Mixxx | Mixxx Development Team | Free open-source; full DJ feature set; best-in-class manual | Official user manual (Tier 1) |

Rationale: two pro poles (club-standard Serato, hardware-ecosystem rekordbox), one legacy-broad (VirtualDJ), one consumer/mobile (djay), one open-source baseline (Mixxx — also serves as the anti-vendor check: whatever Mixxx shares with the commercial products is likely Type structure, not marketing).

## Sources

- Mixxx 2.4 User Manual — https://manual.mixxx.org/2.4/en/ (fetched 2026-09-07; chapters: introduction, DJing With Mixxx https://manual.mixxx.org/2.4/en/chapters/djing_with_mixxx)
- VirtualDJ User Manual — https://www.virtualdj.com/manuals/virtualdj.html (fetched 2026-09-07)
- Serato DJ Pro product page + FAQs — https://serato.com/dj/pro (fetched 2026-09-07)
- rekordbox product site — https://rekordbox.com/en/ (fetched 2026-09-07; feature overview, mobile, plans, USB Export support listing)
- Algoriddim djay product pages — https://www.algoriddim.com/djay and https://www.algoriddim.com/djay-ios (fetched 2026-09-07)

Source-access limitations: Serato's deep operational manuals and rekordbox's full manuals were not fetched (only product/FAQ surfaces); Algoriddim offers no equivalent public operational manual at the fetched locations. Claims relying only on those products are therefore kept at positioning/capability level, not precise operational detail. Per-source fetch count was kept to 1–2.

## Product Observations

### Mixxx (evidence layer A — official manual, directly observed)

- Positioning: "free DJ software for Windows, macOS and Linux"; perform with MIDI/HID controllers, CD players, vinyl turntables, or just keyboard and mouse.
- Interface structure: Decks; Mixer; Samplers; Effects; Microphones & Auxiliary Inputs; Preview Deck. (User Interface chapter TOC)
- Library chapter: import audio files, analyze library, tracks table, loading tracks, search, previewing tracks, metadata editing, **Auto DJ** (automated mixing), **Playlists** ("arranging tracks in a set order"), **Crates** ("organizing tracks into collections"), computer file browsing, Recordings, **History** ("keep track of your sessions"), Analyze, import libraries from other software, file formats, audio CDs.
- DJing chapter (workflow ground truth):
  - **Gain staging**: level meters, headroom, clipping warnings — signal-chain level discipline is taught as core skill.
  - **Beatmatching**: "adjusting the playback rate of a track so that it matches the tempo of another track" plus "adjusting the phase of the beats so they are aligned" — tempo + phase are named as "the two things a DJ must do"; manual method = rate sliders + temporary pitch bend; SYNC button does it automatically given accurate BPM + beat grid.
  - **Sync Lock**: linked decks share rate changes; handles integer tempo ratios (140 vs 70 BPM example); QUANTIZE aligns beats precisely.
  - **Harmonic mixing**: key detection + keylock (speed changes don't alter key).
  - **Recording**: records main output (or external mixer input) to audio files (default WAV), recordings browsable in library.
  - **Intro/Outro cues**: analyzer places intro/outro markers at first/last sound; DJs align outro of old track with intro of new track to time transitions; used by Auto DJ to choose crossfade length.
  - **Auto DJ**: automatically loads tracks into decks and mixes by taking control of the crossfader; queue from playlists/crates; mix modes (Full Intro+Outro, Fade At Outro Start, Full Track, Skip Silence); explicitly "not intended to be a replacement for a human DJ."
- Hardware chapter: controllers, audio interfaces, mixers, turntables, CDJs, headphones, splitter cables; **Vinyl Control (DVS)** via timecode vinyl/CDs; external mixer mode (software mixer bypassed).
- Live broadcasting chapter: stream mix to internet radio servers.
- Effects chapter: effect units, per-unit routing/mix modes, effects audible in headphones.
- 4 decks supported.

### VirtualDJ (evidence layer A — official manual TOC, directly observed)

- Positioning: "the #1 most popular DJ software for real working DJs."
- Interface structure: **Decks** (track info, basic controls; advanced: effects, loops, pads, custom buttons), **Mixer** (audio, **video**, scratch, master), **Browser** (folder list, file list; SideView: sidelist, remixes, sampler, **Automix**, **karaoke**, clone view), **Database** (search, analyze tracks, smart folders, online music/catalogs, playlists, **history/sets**, recommendation features, charts, **CDJ export**, stems, AI prompt).
- Editors: Automix editor, BPM editor, DNA scratch editor, pads/scratch bank editor, POI (points of interest) editor, lyrics editor, sample editor, tag editor, track cleaner, video editor — deep preparation layer over tracks (points, grids, tags).
- Audio setup options: master out, master & headphones, **external mixer**, controller, record loopback, microphone, line-in, **timecode** (DVS), ReWire.
- Broadcast (audio and video) and Record settings sections.
- VirtualDJ Remote (phone/tablet as controller surface).
- Stems 2.0 (real-time source separation).

### Serato DJ Pro (evidence layer A for listed features — official product page + FAQ; positioning only beyond that)

- Positioning: "industry-leading professional DJ software, renowned for its reliability"; pro club/turntablist artist roster.
- Directly observed features: dynamic waveforms (horizontal/vertical), **Practice Mode** ("continue using Serato DJ Pro without hardware connected"), Prepare/History/Browse panels, Sampler panel, **4-deck mode** (hardware-dependent), 20–50+ built-in FX, **Stems** (isolate vocals/melody/bass/drums, Stems Pad FX), streaming services (Apple Music, Beatport, SoundCloud, Spotify, Tidal), 100+ supported hardware, **DVS expansion** (control vinyl/CDs/tone), **HID mode** with CDJs, club-standard setups, Smart Sync, Key Analysis, Smart Crates/Crate Search, pad modes (Stems FX, Beat Jump, Slicer), MIDI mapping, live streaming guidance.
- FAQ rules observed:
  - Recording set: available with license/hardware unlock; **not available when playing from a streaming service**, in Practice mode, or on hardware without recording.
  - Licensing model: hardware unlock (connected compatible hardware unlocks the software) vs paid license/subscription; DVS and club-standard usage gated to Suite tier; Lite vs Pro feature split.
- Separately marketed music-production products (Studio, Sample) exist — good negative evidence that DJ software and production software are distinct product families inside one vendor.

### rekordbox (evidence layer A for listed features — official product site; plan-level detail only)

- Positioning: "All a DJ needs" — software for professional DJs in the (Pioneer/AlphaTheta) hardware ecosystem.
- Directly observed features: high-speed **track analysis** (BPM and KEY; cloud analysis), **Cloud Library Sync** (Dropbox-backed, multi-device), CloudDirectPlay (browse/play cloud library from compatible players), **stems** (isolate vocals/drums/bass/instrumental), mobile iOS/Android apps "with performance capabilities just like the PC/Mac version" plus track management (edit cue points and grid info on the move), connection to DJ gear (controller via USB/Bluetooth), **USB Export** support area (prepare on computer → play from USB on CDJ/XDJ multi players), mobile app used "like a USB drive to play tracks on CDJ and XDJ multi players."
- Plan structure: Free / Core / Creative / Professional; feature gating on DVS control, video output, recording, cloud sync device counts; "Hardware Unlock" eligible equipment.
- DJ testimonial themes (positioning, weak evidence): reliability in the club, library organization (5,000-song USB sorted by BPM/key), hot cues/loops enabling performance style, preparation before the show, "as close as you can get to the old days of carrying vinyl around."
- "2 Player mode to test track combos", "Edit mode", Export Loops function — preparation-and-simulation surfaces (weakly evidenced, listed for completeness).

### djay / Algoriddim (evidence layer A for listed features — official product pages; positioning only beyond that)

- Positioning: "#1 DJ app," Apple Design Award winner; "transforms your iPhone or iPad into a complete DJ system"; for beginners and professionals; free with PRO subscription tier.
- Cross-platform: iOS, Mac, Windows, Android, Apple Vision Pro, Meta Quest (spatial/VR DJing).
- Streaming-native: unified media library over Spotify, Apple Music, Tidal, SoundCloud, Beatport + local library; "start mixing right away."
- Interface: classic turntable + mixer setup, **Automix view**, 2-deck pro mode with high-resolution waveforms and library side by side, **four decks**, sampler.
- **Neural Mix**: real-time music source separation (isolate beats/instruments/vocals); **Crossfader Fusion** (morph tracks with filters/FX); **Fluid Beatgrid** (beat-matching engine "across diverse musical genres and tempos").
- Looper: record/sequence loops during the mix, auto-quantized and synced (up to 48 loops).
- Video mode: mix videos/live photos, audio-reactive visual loops, transitions, overlays, external display.
- Hardware: 50+ MIDI controllers plug-and-play (Pioneer DJ, Reloop, Numark, Denon DJ), MIDI Learn mapping, **Pre-Cueing** (split-output mode or external audio interface to cue in headphones independently of main mix), multi-channel USB audio interfaces.

## Cross-product Comparison

| Structure / capability | Mixxx | VirtualDJ | Serato DJ Pro | rekordbox | djay | Strength |
|---|---|---|---|---|---|---|
| Library of finished tracks with search/metadata | ✔ | ✔ | ✔ | ✔ | ✔ | 5/5 — defining-adjacent |
| Organization units (crates/playlists/smart lists) | ✔ (crates, playlists) | ✔ (folders, playlists, smart folders) | ✔ (crates, smart crates, prepare) | ✔ (playlists, smart playlists, tags) | ✔ (playlists, media library) | 5/5 |
| Playback decks (≥2), loadable, simultaneous | ✔ (4) | ✔ (multi) | ✔ (4-deck mode) | ✔ (players/2 Player mode) | ✔ (4) | 5/5 — defining |
| Mixer: level, EQ, crossfader per channel | ✔ | ✔ | ✔ | ✔ | ✔ | 5/5 — defining |
| Real-time tempo/pitch control per deck | ✔ (rate sliders) | ✔ | ✔ | ✔ | ✔ | 5/5 — defining |
| Beat/tempo alignment assistance (sync) | ✔ (Sync Lock, Quantize) | ✔ | ✔ (Smart Sync) | ✔ | ✔ (Fluid Beatgrid) | 5/5 |
| Track analysis: BPM/key/beatgrid | ✔ | ✔ (+BPM editor) | ✔ (Key Analysis) | ✔ (BPM/KEY, cloud) | ✔ (Fluid Beatgrid) | 5/5 |
| Waveform displays | ✔ | ✔ | ✔ (dynamic H/V) | ✔ | ✔ (high-res) | 5/5 |
| Cue/pre-listen separate from master | ✔ (Preview Deck, headphones) | ✔ (master & headphones) | ✔ | ✔ | ✔ (Pre-Cueing/split output) | 5/5 |
| Performance points: hot cues, loops | ✔ | ✔ (POI editor, loops) | ✔ (pad modes) | ✔ (hot cues/auto loops) | ✔ | 5/5 |
| FX | ✔ (units) | ✔ | ✔ (20–50+) | ✔ (RMX/DJM-type, plan-gated) | ✔ | 5/5 |
| Sampler | ✔ | ✔ | ✔ (sampler panel) | (not observed) | ✔ | 4/5 |
| Recording of the mix | ✔ (main output) | ✔ (record settings) | ✔ (license-gated; blocked for streaming) | ✔ (plan-gated) | (not observed) | 4/5 |
| Auto DJ / Automix | ✔ (modes, crossfader control) | ✔ (+Automix editor) | (not observed) | (not observed) | ✔ (Automix view) | 3/5 |
| Hardware: controllers | ✔ (MIDI/HID) | ✔ | ✔ (100+) | ✔ | ✔ (50+, MIDI Learn) | 5/5 |
| DVS (timecode vinyl/CD) | ✔ | ✔ (timecode) | ✔ (expansion) | ✔ (plan-gated) | (not observed) | 4/5 |
| Club players / HID / export-to-USB | ✔ (CDJs) | ✔ (CDJ export) | ✔ (HID/DVS club sets) | ✔ (USB Export, CloudDirectPlay) | (not observed) | 4/5 |
| Streaming service integration | (not observed) | ✔ (online catalogs) | ✔ (5 services) | ✔ (Apple Music, Spotify mobile) | ✔ (Spotify, Apple Music, Tidal…) | 4/5 |
| Stems / real-time source separation | (not observed in 2.4) | ✔ (Stems 2.0) | ✔ | ✔ | ✔ (Neural Mix) | 4/5 — era-typical |
| Key lock (speed ≠ pitch) | ✔ | ✔ | ✔ | ✔ | ✔ (implicitly via tempo engines) | 4/5+ |
| Microphone / aux input | ✔ (chapter) | ✔ (settings) | (not observed) | (not observed) | (not observed) | 2/5 — qualified |
| Video mixing | ✔ (not observed) | ✔ | ✔ (expansion) | ✔ (plan-gated) | ✔ (video mode) | 3–4/5 — optional |
| Broadcasting / live stream | ✔ (internet radio) | ✔ (audio/video) | ✔ (guidance) | (not observed) | (not observed) | 2/5 — optional |
| Karaoke surface | ✘ | ✔ | ✘ | ✘ | ✘ | 1/5 — product-specific |
| Practice without hardware | ✔ (computer only) | ✔ | ✔ (Practice Mode) | ✔ (mobile app free DJing) | ✔ (touch-first) | 5/5 — hardware optional |
| Cloud library sync | (import from other libraries) | ✔ (CloudDrive) | (not observed) | ✔ (Dropbox sync) | (cloud libraries of services) | 2–3/5 — optional |
| History of played tracks | ✔ | ✔ (sets) | ✔ (History panel) | (not observed) | (not observed) | 3/5 |
| Freemium / subscription / hardware-unlock licensing | ✘ (free) | ✔ (home free / paid) | ✔ (hardware unlock, Suite) | ✔ (plans, hardware unlock) | ✔ (free + PRO) | business-model variant |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant

Minimal structure without which the product is not recognizable as DJ software:

```text
Library of finished recorded tracks (browsed/organized; material pre-exists)
└── Two or more playback decks, loaded from the library, able to sound simultaneously
    └── Mixing surface blending the decks into one continuous program output
        (per-deck level/EQ, crossfader-style transition control)
    └── Real-time tempo/pitch control per deck to align tracks
        (manual rate control or sync-assisted — the invariant is the capability)
```

Four properties:

1. **Finished tracks as working material** — the user selects and performs recordings that already exist; the user does not author the music inside the application. Remove this and it becomes production software (DAW / beat-making).
2. **Multiple real-time playback decks** — at least two channels that can play simultaneously. Remove this and it becomes a media player.
3. **Real-time performance mixing** — the operator blends decks into a single program output, performing transitions between tracks as the defining act. Remove this and it becomes a playlist player or an editor.
4. **Real-time per-deck tempo/pitch control** — the operator can change a deck's playback speed to align it with the other (manual or sync-driven). Remove this and continuous beat-aligned mixing — the type's signature skill — is impossible.

Historical check (§24 applied): two turntables + a mixer — the pre-software DJ setup — maps exactly onto these four properties (two playback devices for finished recordings, pitch faders, a blending mixer). Mixxx's manual defines beatmatching in exactly these vinyl-inherited terms. Early DVS products (vinyl control) and 2000s-era laptop DJing all fit. The definition therefore does not overfit the sync/waveform/stems era.

Deliberately NOT in L0: headphone cueing, waveforms, analysis, sync buttons, hot cues/loops, FX, samplers, recording, hardware, streaming, Auto DJ, stems, video.

### L1 — Common Mature Structure (present across the sample; not definitional)

- Track analysis: BPM, musical key, beatgrid; displayed in library and decks; user-correctable (editors/grids).
- Waveform displays (scrolling + overview) as the visual working surface.
- Cue / pre-listen routing: audition a deck in headphones independently of the master output.
- Performance points: hot cues, loops (incl. auto-loops), beat-jump/slicer-style pad modes.
- Sync assistance and keylock (tempo alignment decoupled from pitch).
- Harmonic mixing support (key display/notation, key-compatible filtering).
- FX units assignable to decks; sampler with quantized triggering.
- Organization units: crates/playlists/smart lists; search; metadata/tag editing.
- Session history of played tracks; recording of the mix to file.
- Gain staging discipline (level meters, clipping indicators) as user-facing behavior.
- Hardware control: MIDI/HID controllers, plug-and-play mappings, MIDI learn.
- Microphone/aux input paths (observed directly in 2 products; qualified).
- Library portability (import libraries from other software; export to standalone players).

### L2 — Variant / Optional Structure

- Auto DJ / Automix (automated transitions; modes; explicitly not a replacement for a human DJ) — strong in 3/5, absent from the two club-pole products' observed surfaces.
- Streaming-service integration (catalogs mixed with local files; licensing constraints follow).
- Stems / real-time source separation (era-typical; 4/5 sampled).
- DVS timecode control; HID mode with club players; export-to-USB workflows (hardware-ecosystem pole).
- Video mixing, visualizers, external displays.
- Live broadcasting to internet radio.
- Karaoke surfaces (1/5 — product-specific-ish, borderline L3).
- Cloud library sync across devices; mobile companion apps; remote-control surfaces.
- VR/spatial DJing (1/5).
- Practice-mode / laptop-only operation (hardware optional — observed in all, but historically controller-centric products treat it as secondary).
- Business models: free open-source, free-for-home/paid-pro, hardware unlock, subscription tiers, plan-gated features.

### L3 — Vendor-specific Structure (kept out of the final document)

- Serato: Practice Mode naming, Stems Pad FX, Noisemap control tone, Serato Video, Lite/Pro/Suite tiering, DJ Expansion Play, hardware-unlock FAQ rules.
- rekordbox: CloudDirectPlay, Mix Point Link/playback reservation, Export Loops, 2 Player mode, Edit mode, plan device counts, Dropbox 5TB bundling, PRO DJ LINK.
- VirtualDJ: VDJScript, skin/plugin SDK, DNA Scratch Editor, GeniusDJ/Ask The DJ, Track Cleaner, karaoke SideView, DMC Championships community.
- Algoriddim: Neural Mix™, Crossfader Fusion™, Fluid Beatgrid™, Looper 48-loop count, Vision Pro/Quest builds, Content Packs.
- Mixxx: crates-vs-playlists semantics, Sync Leader/Follower soft-leader machinery, Auto DJ mix-mode names, skins (Tango/Deere/LateNight/Shade).

## Vendor-specific Findings

- rekordbox's identity is split between "performance software" and "library preparation + export tool for standalone club hardware" (USB Export; mobile-app-as-USB-drive). This is a product-family posture, not a Type requirement — the other four products perform from the software itself. Recorded as a Variant.
- Serato's recording rules (blocked for streaming sources, Practice mode) show licensing interleaving with audio sourcing — product-specific rule, useful as an example of "recording availability depends on plan/source," not a Type rule.
- VirtualDJ's karaoke and editor depth (lyrics, track cleaner) extends beyond the Type core into adjacent jobs — evidence that mature products bundle adjacent surfaces without changing the Type.

## Rejected Findings

- "DJ software = DVS/turntable control" — rejected: 1/5 sampled product lacks DVS; laptop/controller/mobile DJing exists everywhere. DVS is a common expansion, not the definition.
- "DJ software = controller hardware" — rejected: all sampled products run standalone (Practice/computer-only/mobile); hardware integration is common mature structure.
- "DJ software = streaming-native" — rejected: Mixxx (open-source baseline) has no streaming integration observed; streaming is an L2 modern variant.
- "Stems are part of the definition" — rejected: absent in the Mixxx 2.4 manual (the most operationally documented sample); era-typical L2.
- "Auto DJ is definitional" — rejected: absent from two pro-pole surfaces; it is an automation layer over the same deck/mixer core.
- "DJ software is defined by scratch/turntablist performance" — rejected: scratch tooling (DNA scratch editor, scratch mixer panel) is 1–2/5; the general case is track-to-track mixing.
- Overfitting guard: beatmatching vocabulary (BPM, phase, sync) appears in all five, but the invariant was abstracted one level up to "real-time tempo/pitch control per deck," because manual rate control (vinyl-era and early software) predates sync engines.

## Boundary Findings

| Boundary | Discriminating test | Notes |
|---|---|---|
| vs Digital Audio Workstation / DAW | Working material and deliverable: DAW builds a multitrack project and renders a new recording; DJ software performs existing finished recordings in real time, deliverable = the performance itself | Aligned with the DAW pass (2026-09-07), which holds the same seam from its side ("performs finished tracks rather than producing them"). Clip-launch DAWs blur from the DAW side only. |
| vs Live Music Performance Software (04.12 sibling) | What is performed: DJ software mixes finished recordings; live performance software performs musical material itself (clips/patterns/instruments) triggered live | Same Family (04.12) — real seam. Held from the DJ side here; **joint review recommended** when sibling is processed (recorded in Boundary Issues). |
| vs Audio Editor | Interaction model: editor makes persistent region-based edits to recording files; DJ software performs tracks without authoring a persistent edited artifact | Aligned with audio-editor pass (2026-09-06). DJ products' "editors" (BPM/POI/grid) tune metadata, not the audio artifact. |
| vs Music Streaming Platform | Consumer playback vs operator performance; no decks/mixer/tempo alignment on the streaming side | Streaming integration inside DJ software is a source of material, not the Type. |
| vs Media Player | Player = single-channel consumption with optional crossfade; DJ software = multi-deck mixing surface with per-deck tempo control and pre-listen | The mixing surface + tempo control is the wall. |
| vs Beat-making / Loop-based Production | Created patterns/loops as material vs performed finished tracks | DJ loopers/samplers are performance layers over tracks, not composition environments. |
| vs Radio Station Management / broadcast automation | Scheduled programmatic playout vs a human operator performing in real time | Broadcasting output exists in DJ software (2/5) as a feature, not the definition. |
| "去掉什么就变成另一个 Type" test | Remove authoring of new material → stays DJ; remove performance-of-finished-tracks (material becomes clips/patterns the user authors) → becomes Live Performance/DAW family; remove multi-deck real-time mixing → becomes media player | The load-bearing invariants are #1 (finished tracks) + #2/#3 (decks + real-time blend) + #4 (tempo control). |

## Uncertainties

- Serato and rekordbox operational manuals were not fetched; their precise workflow rules (e.g., exact analysis options, export-mode mechanics, plan feature boundaries beyond what's stated) are unverified. Claims from these two are kept at the capability level their product pages support.
- djay's recording capability was not observed on the fetched pages; recording is stated as common from the other four only.
- Whether headphone cueing should sit in L0: argued here as L1 (all five have it, but laptop-only practice and splitter-cable workarounds show the type survives without dedicated cue hardware; the IM-gold-standard style "minimal definition" bias favors exclusion). Flagged as a judgment call.
- Karaoke (VirtualDJ only) might indicate a separate adjacent Type in some vendors' catalogs; insufficient sample to decide — left as product-scope note.
- The exact split between "performance mode" and "export/preparation mode" in hardware-ecosystem products could not be verified beyond the observed support-page listings.

## Final Synthesis

DJ Software is a real-time performance application over a managed library of finished recorded tracks. Its defining core is small: a track library (the working material pre-exists), two or more playback decks loaded from it and able to sound simultaneously, a mixing surface that blends the decks into one continuous program output, and real-time per-deck tempo/pitch control that lets the operator align tracks (by hand or with sync assistance). Everything else the market associates with the category — waveform displays, BPM/key/beatgrid analysis, sync, hot cues and loops, FX, samplers, recording, controllers, DVS, club players, streaming catalogs, Auto DJ, stems, video — is standard, common, or optional structure layered on that core, and several of these (streaming, stems, video, cloud sync) are era-markers rather than definitional. The type's deepest anchor is pre-software: the two-turntables-and-a-mixer setup maps one-to-one onto the defining core, which is why the definition survives the historical check. The nearest live boundary is the 04.12 sibling Live Music Performance Software (performed material: finished recordings vs performable musical material) — flagged for joint review; the production-side boundaries (DAW, Audio Editor, Beat-making) are held consistently with the sibling passes already recorded in STATUS.md.
