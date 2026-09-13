# Research Notes — Virtual Recording Studio

## Research Goal

Understand the Application Type **Virtual Recording Studio** (DIRECTORY 04.10 Music Production) from real products: what software the market actually sells under the "virtual recording studio" / "virtual studio" / "recording studio" label, what its world consists of, what users do inside it, and — critically — how it relates to the already-processed sibling leaves **Digital Audio Workstation / DAW** (04.09, processed 2026-09-07), **Music Production Application** (04.10, processed 2026-09-08, resolved as alias of the DAW family), **Beat-making Application**, and **Loop-based Music Production Application**.

This pass discharges two standing joint-review flags:

- research/digital-audio-workstation-daw.md §Boundary Findings #5 — "vs Virtual Recording Studio (04.10, unprocessed): likely a marketing-positioned variant of the DAW (bundled instruments + recording aimed at home studios). Flagged for the sibling pass."
- research/music-production-application.md §Boundary Findings #4 — "vs Virtual Recording Studio (04.10, unprocessed) — expected marketing-positioned variant of the same family (bundled instruments + recording aimed at home studios). GarageBand's 'fully equipped music creation studio right inside your Mac' is the consumer pole of exactly this pattern. Flag stands for that pass."

## Initial Boundary

Working hypothesis at start (to be tested, not assumed):

- A "virtual recording studio" is likely software that provides what a physical recording studio provides — multitrack capture, processing, mixing, a deliverable — on a computer.
- The DAW pass and the music-production pass both predicted this leaf resolves to the DAW product family, either as an alias (like music-production-application) or as a positioning variant (home-studio bundles).
- Known disambiguation risks: (a) "Virtual Studio Technology" (VST) is a plugin standard, not an application; (b) "virtual studio" in broadcast television means virtual-set/AR studio systems — a different domain entirely; (c) "studio" appears in many product names (Studio One, n-Track Studio) without the leaf meaning anything separate.

## Research Questions

1. What products does the market actually sell/label as a "virtual recording studio" (or describe as "a studio on your computer")?
2. Do those products satisfy the DAW core (persistent multitrack project + user-created material + mixing + rendered deliverable)?
3. Do vendors use "studio" language and "DAW" language interchangeably for the same products (alias test)?
4. Is the "studio" framing restricted to a segment (home studios) or does it span the family (consumer → budget → professional → cloud)? This decides alias vs variant.
5. Is any part of the "studio" framing definitional (e.g., bundled instruments, recording, ease of use), or is it positioning?
6. Historical check: would the older "recording studio software" generation (1990s–2000s) fit the same definition?
7. Where are the boundaries: vs DAW, vs music-production-application, vs audio editor, vs beat-making, vs loop-based, vs podcast editing, vs the broadcast "virtual studio" name collision?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Pole in the sample | Why selected |
|---|---|---|---|
| GarageBand | Apple | free consumer entry, bundled "studio" | the exact product the sibling passes named as the consumer pole of this pattern; full official user guide available |
| Mixcraft | Acoustica | budget home-studio DAW, self-described "virtual studio" | the strongest vendor-side "virtual studio" self-label found; editions literally named Home Studio / Recording Studio / Pro Studio; full online manual |
| n-Track Studio | n-Track Software | cross-platform budget DAW, 30-year heritage | self-labels "Digital Audio Workstation"; press quote on its own page apposes "music studio" with "digital audio workstation" |
| Reason | Reason Studios | rack-simulation philosophy, professional | the "virtual studio rack" concept made literal; already sampled in the music-production pass; re-fetched fresh for this pass |
| Soundtrap | Spotify | cloud/browser collaborative studio | the online "studio" pole; its own site names the mixing toolset "online DAW features" |

## Sources

All fetched 2026-09-09 unless noted.

- Apple — GarageBand for Mac (official product page) — https://www.apple.com/mac/garageband/
- Apple — GarageBand User Guide (official manual, table of contents + welcome) — https://support.apple.com/guide/garageband/welcome/mac
- Acoustica — Mixcraft 10.6 product page — https://acoustica.com/mixcraft
- Acoustica — Mixcraft 10 User Guide, Getting Started (official manual) — https://acoustica.com/mixcraft-10-manual/getting-started
- n-Track — n-Track Studio home page — https://ntrack.com/
- n-Track — n-Track Studio features page — https://ntrack.com/features.php
- Reason Studios — What is Reason? (official product page) — https://www.reasonstudios.com/reason
- Soundtrap — Music Makers landing page — https://www.soundtrap.com/
- Carried from sibling passes (not re-fetched): DAW-pass evidence for Pro Tools / REAPER / BandLab / Ableton Live (research/digital-audio-workstation-daw.md, 2026-09-07); music-production-pass evidence for FL Studio / Logic Pro / Ableton Live (research/music-production-application.md, 2026-09-08).

## Product Observations

### GarageBand (Apple) — evidence layer A

- Self-description (product page and user guide, verbatim): "GarageBand is a fully equipped music creation studio right inside your Mac — with a complete sound library that includes instruments, presets for guitar and voice, and an incredible selection of session drummers and percussionists." User guide headline: "A complete music studio on your Mac."
- The user guide's table of contents is a complete DAW structure: projects (create/save/delete; tempo, key, time signature, project end point), tracks (audio / software instrument / Drummer tracks; record-enable, input monitoring, mute/solo, volume/pan), recording (record to audio track, multiple takes, multiple tracks, software-instrument takes, overdub, choose/delete takes), loops (Apple Loops, Loop Browser, custom loops), regions (cut/copy/paste/move/loop/resize/split/join), editors (Audio Editor, Piano Roll Editor, Score Editor, Drummer Editor), mixing (automation curves, master track, EQ, amps and pedals, Audio Units plug-ins), arrangement (arrangement markers, tempo track, transposition track), sharing (export to disk/iCloud, Music app, CD, AirDrop, Mail, GarageBand for iOS).
- Product page adds: "Create and mix up to 255 audio tracks"; multi-take regions ("Record as many takes as you like… GarageBand saves them all in a multi-take region"); Flex Time timing correction; Groove Track; Smart Controls; Learn to Play lessons; share to social/email/ringtone/Music app.
- The same page promotes the professional sibling in studio language: "Logic Pro for Mac — Turn your Mac into a full recording studio."
- Observation: the "studio" framing is Apple's own, applied to both the free consumer product (GarageBand) and the professional product (Logic Pro) — the framing is not segment-restricted.

### Mixcraft (Acoustica) — evidence layer A

- Self-labels, verbatim, from the product page: "Mixcraft is Acoustica's highly acclaimed DAW software for Windows"; "Mixcraft offers an all-in-one solution to all your audio and video editing needs in a single virtual studio package"; "Acoustica has enhanced the virtual studio with new features."
- Editions are named **Home Studio**, **Recording Studio**, **Pro Studio** — the vendor's own tier names use the studio vocabulary for the same product at three price points.
- User guide opening, verbatim: "Welcome to Mixcraft 10, a powerful recording DAW software offering the tools and performance power to create professional music and video projects... easily!"
- Manual structure is a complete DAW: projects (loading/saving), track types (audio, virtual instrument/MIDI, video, video text, send, submix, output bus, master, vocoder, multi-out instrument child tracks), clips (audio/MIDI, clip grid), MIDI editors (piano, step, score), sound editor, mixer tab with channel strips, library tab, performance panel (live clip launching), automation (clip + track, real-time recording, hardware controllers), mixing down to audio/video files, burning audio CDs, effects (per-edition lists), virtual instruments (per-edition lists), plug-in manager, ReWire, stem separation (Pro), hardware controllers, Melodyne integration (Pro).
- Product page features: unlimited audio and MIDI tracks, 7,500+ loops, 16 virtual instruments and 36 effects (more in Pro), vocoder tracks, envelopes, per-track EQ, performance panel, video editing, integrated store, AI stem separation (Pro), remote control app.
- Observation: the same vendor, on the same page, uses "DAW software", "recording DAW software", "virtual studio", and edition names "Recording Studio"/"Home Studio" — the strongest single-vendor interchange evidence in the sample.

### n-Track Studio (n-Track Software) — evidence layer A

- Page titles, verbatim: home page "n-Track Studio | Multitrack recording, editing & mixing software"; features page "Features - n-Track Studio Digital Audio Workstation & Audio Recording App". The vendor self-labels as a digital audio workstation.
- Press quotes displayed on the vendor's own page include (Setapp): "Get a fully-fledged music studio inside your computer — n-Track is a digital audio workstation that will equally appeal to beginner artists as well as professionals." — "music studio" and "digital audio workstation" in apposition in one sentence. Other quotes: "their DAW software" (Sound On Sound), "DAW n-Track Studio" (MusicRadar), "cross-platform DAW" (Synthtopia), "one of the most cross platform available DAWs" (Create Digital Music), "a major update to the pioneering digital audio workstation, first released over 21 years ago" (Pro Sound News).
- Features page structure: piano roll, step sequencer, VocalTune pitch correction, guitar/bass amp simulation, AI MixSplit stem separation, screen drumkit, built-in effects list, audio part widgets, DAWproject import/export ("share projects between different DAWs"), surround mixing (5.1/6.1/7.1), effects chains, 15GB+ royalty-free loops/samples, add-on manager, beat doctor transient tool, ReWire, tuner, sonograms, song browser.
- Recording & mixing section: "Records and plays back a virtually unlimited number of audio and MIDI tracks"; VST/VST3/CLAP/DirectX/AU/ReWire effects per channel; automation of volume/pan/aux/effects; live input processing.
- Deliverable, verbatim: "Once finished recording the whole song, you can mixdown all the tracks into a single wav file and to use it to record an audio CD track using a CD recorder or to distribute the song via internet using the built-in mp3 encoder."
- Cross-platform: Windows, macOS, Linux, Android, iOS; "Exchange recordings between desktop and mobile versions."
- Heritage: 30th-anniversary branding on the site; Pro Sound News dates first release "over 21 years ago" (article predates the anniversary) — the product spans the 1990s "recording studio software" generation to the present.

### Reason (Reason Studios) — evidence layer A

- Self-description, verbatim: "Reason is the Rack and the devices. Reason is a plugin and a DAW. Reason is the wires and the workflow. Reason is your musical ideas and your final result." And: "a complete daw — From your first beat to your next album, Reason is the music making software for capturing and exploring your ideas."
- The Rack: "If Reason was a song, the Rack would be the hook. Wire up instruments, effects, and Player MIDI effects to create the sound you're looking for." — the virtual rack of wired devices is Reason's realization of the studio metaphor (a physical studio's outboard rack, simulated in software).
- Devices "hand-crafted in Sweden since we started in 1994" — heritage from the 1990s.
- Sound bank "more than 30 000 patches, loops, and samples"; Reason+ subscription adds "mastering, distribution, and an ever-expanding collection of sounds and devices"; Reason Hub for releases/distribution.
- Observation: Reason is the sample's literal "virtual studio" — its rack-and-wires metaphor simulates hardware studio equipment — and the vendor itself names the product "a plugin and a DAW". The studio simulation is a philosophy inside the DAW family, not a separate Type.

### Soundtrap (Spotify) — evidence layer A

- Self-description, verbatim: "Music Production, made simple. Create & record easily with powerful tools and sounds, all in one place."
- "Collaborative studio — Make music online anytime, with anyone, on any device." Real-time collaboration "through video and chat, directly in the studio", comments on shared projects, auto-save.
- The site's own link for its mixing/mastering toolset is "/content/product/**online-daw-features**" — the vendor's own URL vocabulary names the toolset DAW features.
- Features: vocal & mixing tools (reverb, distortion, EQ, delay, compressor), virtual instruments (beatmaker, sampler, software synths, drum kits, 808s), online MIDI editor / piano roll, patterns beatmaker, automation, vocal tuning (Antares Auto-Tune branding), royalty-free loops (up to 24,000+ loops), plug-and-play microphone/guitar/instrument connection, song templates, "Open in studio" fork links for demo projects.
- Plans gate features ("Access to Vocal tuning and Automation available on the Sound Starter, Music Production, and Production & Vocals plans"); separate Education and Podcasters lines exist.
- Observation: the cloud "studio" is the same production structure (record → instruments/loops → arrange → mix → deliver) delivered in a browser with real-time collaboration; the vendor's own vocabulary bridges "studio" and "DAW".

## Cross-product Comparison

| Dimension | GarageBand | Mixcraft | n-Track | Reason | Soundtrap |
|---|---|---|---|---|---|
| "Studio" self-language | "fully equipped music creation studio right inside your Mac"; "A complete music studio on your Mac" | "a single virtual studio package"; editions Home/Recording/Pro Studio | press on own page: "fully-fledged music studio inside your computer" | the Rack = virtual studio hardware; "your musical ideas and your final result" | "Collaborative studio"; "Open in studio" |
| "DAW" self-language | (family sibling Logic Pro is the DAW; GarageBand is its entry tier) | "DAW software"; "recording DAW software" (manual) | "Digital Audio Workstation & Audio Recording App" (page title) | "Reason is a plugin and a DAW"; "a complete daw" | own URL slug "online-daw-features" |
| Persistent project | projects: create/save/delete, tempo/key/meter | loading/saving projects | songs saved/reloaded (Song Browser); DAWproject exchange | projects in the DAW; Reason+ ecosystem | cloud projects, auto-save, shared/forked |
| Tracks carrying user-created material | audio tracks + software-instrument tracks + Drummer | audio + virtual instrument/MIDI + vocoder tracks | unlimited audio and MIDI tracks | recorded audio + notes played by rack devices | audio recording + virtual instruments + beatmaker patterns |
| Mixing | track volume/pan, automation, master track, EQ | mixer tab, channel strips, send/submix/output-bus/master tracks | volume/pan/aux automation, effects per channel | mixer in the DAW; rack wiring | mixing tools, auto-mixing, EQ/compressor |
| Rendered deliverable | export to disk/iCloud, Music app, CD, share | mixdown to audio/video files, burn CDs | "mixdown all the tracks into a single wav file", mp3 encoder | final result; Reason+ mastering/distribution | chart-ready mix/master, export |
| Bundled sound layer | complete sound library, Drummer session players, Apple Loops | 7,500+ loops, 16–24 instruments, 36–50+ effects | 15GB+ loops/samples, built-in instruments/effects | 30,000+ patches/loops/samples, rack devices | 24,000+ loops, presets, sound packs every 2 weeks |
| Distinctive emphasis | learning content (lessons), consumer simplicity | value bundles, video editing + scoring in the same package | cross-platform breadth (5 OSes), budget price | rack-and-wires device simulation | browser + real-time collaboration + education line |
| Customer tier | free consumer | budget home studio ($79–$149 one-time, rent-to-own) | budget cross-platform, one-time/subscription | professional, subscription (Reason+) | freemium cloud, education licensing |

**Cross-product commonalities (evidence layer B):**

1. All five products satisfy the DAW core completely: persistent multitrack project; tracks carrying user-created material (recorded audio and/or authored notes/patterns); mixing into a unified output; rendered audio deliverable.
2. All five products are described by their vendors (or the press the vendors display) in "studio" vocabulary — the studio framing is universal across consumer, budget, professional, rack-simulation, and cloud poles.
3. Where both vocabularies appear on one page, they refer to the same product (Mixcraft: "DAW software" = "virtual studio package"; n-Track/Setapp: "music studio" = "digital audio workstation"; Soundtrap: "studio" = "online DAW features"; Reason: "the Rack" = "a plugin and a DAW").
4. The bundled sound layer (instruments, effects, loops) is present in all five — but in every product it is an addition to the record/author/mix/render core, not the core itself (the DAW pass already established, via FL Studio's edition gating, that even recording is not definitional; bundled content is weaker still).
5. None of the five is organized around anything other than the music-production project. There is no session-booking, no hardware-emulation-only product, no service marketplace in the sample.

## Abstraction

### L0 — Defining Invariant

The leaf resolves to the DAW product family; its defining core is the family's core, held from the studio framing:

```text
Persistent multitrack music project (survives save/open)
└── Tracks carrying user-created musical material
    (recorded audio and/or authored notes/patterns — at least one authoring path)
    └── Mixing (per-track level/pan/processing combined into a unified output)
        └── Rendered deliverable (the finished track leaves as audio)
```

Four properties, jointly held. Remove persistence → jam tool; remove user-created material → player/editor of existing recordings; remove mixing → recorder; remove the deliverable → practice toy. This is exactly the DAW core established by the sibling pass — which is the finding, not a copy: the "virtual recording studio" label adds no defining structure of its own.

### L1 — Common Mature Structure

Same as the DAW family's standard capability set, observed across all five sampled products:

- virtual instruments + MIDI sequencing (piano roll / step editor / score editor)
- audio recording machinery (record-enable, takes, multi-take regions, overdub)
- third-party plugin hosting (VST/AU family; n-Track adds CLAP/DirectX; GarageBand: Audio Units)
- non-destructive clip/region editing (split/trim/move/fade/loop)
- time/pitch manipulation (Flex Time, VocalTune, Melodyne integration in Mixcraft Pro)
- automation (clip and track envelopes, real-time recording, hardware control)
- routing (sends, submix/bus tracks, master track; ReWire in Mixcraft and n-Track)
- bundled sound library / browser (loops, samples, presets, instruments)
- export breadth (full mix, stems, MIDI, video; CD burning in two products)
- tempo/meter map, metronome, undo, project asset management

### L2 — Variant / Optional Structure

- **Bundled-completeness emphasis** — the home-studio pole ships instruments + effects + loops so a beginner can produce "in the box" (GarageBand, Mixcraft, n-Track, Soundtrap all advertise the bundled layer prominently). This is the sibling passes' predicted "bundled instruments + recording aimed at home studios" — confirmed as a *positioning emphasis*, not a defining structure: professional products (Logic Pro, Pro Tools, REAPER) carry the same core with less emphasis on bundles, and Apple applies the same "recording studio" language to Logic Pro.
- **Cloud/browser delivery + real-time collaboration** — Soundtrap (video/chat collaboration, shared projects, forking); n-Track's Songtree community (asynchronous collab).
- **Rack-simulation philosophy** — Reason's virtual rack and cables; a UI philosophy inside the family.
- **Video editing/scoring in the same package** — Mixcraft (video tracks, rendering videos); GarageBand (movie track, soundtracks); n-Track (video playback window).
- **Live performance surfaces** — Mixcraft Performance Panel (clip launching, Launchpad integration).
- **Learning content** — GarageBand Learn to Play lessons with feedback; Soundtrap song templates and education line.
- **Mobile companions / cross-platform spread** — GarageBand iOS + Logic Remote; Mixcraft Remote; n-Track on 5 OSes.
- **AI-era features** — stem separation (Mixcraft Pro, n-Track AI MixSplit); vocal tuning (Soundtrap/Antares).
- **Surround mixing** — n-Track (5.1/6.1/7.1).
- **Edition/tier gating** — Mixcraft three editions; Soundtrap plan gating; n-Track editions.
- **Ecosystem add-ons** — stores, subscription sound libraries, mastering/distribution services (Mixcraft Store, Reason+ Hub, Soundtrap Originals).

### L3 — Vendor-specific Structure (research notes only)

- Mixcraft: edition names Home Studio / Recording Studio / Pro Studio; Mixcraft Store + loyalty credits; Mixcraft Remote app; bundled Melodyne 5 Essential (Pro); Freesound.org integration in the library.
- GarageBand: Drummer session players (28 drummers / 3 percussionists per marketing), Smart Controls, Transform Pad, Logic Remote, ringtone export, iCloud continuity with iOS.
- n-Track: Songtree collaboration platform; DAWproject file format for cross-DAW exchange; Screen Drumkit; Beat Doctor; 2D/3D sonograms; 30th-anniversary positioning.
- Reason: the Rack metaphor and virtual cables; Player MIDI effects; Reason+ subscription; Reason Hub (mastering/distribution); ReCycle companion product.
- Soundtrap: Originals sound-pack drops "every 2 weeks"; fork links ("Open in studio"); Antares Auto-Tune branding; Spotify ownership; Education/Podcasters sister lines.

## Vendor-specific Findings

- "Studio" as product/tier vocabulary: Mixcraft's edition names, n-Track's product name, Soundtrap's "studio" surface, Reason's rack — the word is positioning, not structure.
- The Setapp quote displayed on n-Track's own page is the sample's cleanest apposition: "Get a fully-fledged music studio inside your computer — n-Track is a digital audio workstation…"
- Apple's studio language spans tiers: GarageBand ("music creation studio") and Logic Pro ("full recording studio") — the framing is not home-studio-restricted.
- Track-count figures (GarageBand "up to 255 audio tracks"; n-Track "virtually unlimited") are product-specific claims, not Type facts.

## Boundary Findings

1. **vs Digital Audio Workstation / DAW (04.09 — JOINT REVIEW FLAG DISCHARGED).** The two prior passes predicted a "marketing-positioned variant (bundled instruments + recording aimed at home studios)". The fresh evidence refines that prediction: the "studio" framing is **not** segment-restricted. Apple applies it to the professional Logic Pro ("Turn your Mac into a full recording studio") as well as to free GarageBand; Soundtrap applies it to a cloud DAW; Reason's rack simulation is a professional product. Every product marketed in studio vocabulary satisfies the DAW core, and where both vocabularies appear together they denote the same product (Mixcraft, n-Track/Setapp, Soundtrap URL, Reason). Substitution test: replace "virtual recording studio" with "DAW" in any sampled self-description and every claim holds; replace "DAW" with "a virtual recording studio" and the claims still hold. **Resolution: the leaf is a positioning-framed alias of the DAW product family — the family described from the "a recording studio on your computer" angle rather than the workstation angle. It is not an independent Type, and it is not a home-studio-segment variant (the framing spans the whole family). DAW remains the canonical name per the prior joint reviews; merge-vs-keep-both remains a taxonomy-owner decision.**
2. **vs Music Production Application (04.10, processed as alias).** Sibling alias of the same family. The two alias names differ in framing: "music production" frames the *activity* (producing music); "virtual recording studio" frames the *venue/environment* (the studio the computer becomes). Both carry the identical DAW core. No boundary to draw between them beyond framing; both documents point to the DAW document as canonical.
3. **vs Audio Editor (04.09 — aligned with sibling passes).** The discriminator is the working material: an audio editor works on a recording that already exists; the studio/DAW family builds a composition from recorded and authored material across tracks. Remove the multitrack project + authoring → an editor remains.
4. **vs Beat-making Application (04.10 — aligned).** Rhythm-anchored pattern composition is a narrower center on the same substrate; the beat-making core is one workflow inside the studio/DAW world (Soundtrap's "patterns beatmaker" and n-Track's step sequencer are embedded examples).
5. **vs Loop-based Music Production Application (04.10 — aligned).** Assembling pre-made loops as the primary compositional act is a narrower center; every sampled product embeds loop machinery (Apple Loops, Mixcraft's 7,500-loop library, Soundtrap's loop packs) as a starting aid, not the center.
6. **vs Podcast Editing Application (04.09 — aligned).** Same editing substrate, different center (episode/publication pipeline). Soundtrap ships a separate Podcasters line — the vendor itself splits the domains.
7. **vs DJ Software / Live Music Performance Software (04.12 — aligned).** Performing finished tracks vs producing new material. Mixcraft's Performance Panel is a live surface inside a production product — gradient, not boundary crossing.
8. **Name-collision disambiguations (not Application Type boundaries):**
   - **Broadcast "virtual studio"** — in television production, "virtual studio" means virtual-set/AR studio systems (rendered sets composited with camera feeds). Same words, entirely different domain; not a music product population and not part of this leaf.
   - **Virtual Studio Technology (VST)** — Steinberg's plugin interface standard. A format, not an application; the studio/DAW family *hosts* VST plugins.
   - **"Studio" in product names** (Studio One, n-Track Studio, Soundtrap Studio) — naming, not a separate category.

## Historical / Market-Sample Check

- The sampled products span three decades of the family: Reason's devices "since we started in 1994"; n-Track's 30th-anniversary branding and press dating its first release to the 1990s ("a pioneering digital audio workstation, first released over 21 years ago"); Mixcraft "since its initial release in 2004". The 1990s–2000s "recording studio software" generation — multitrack recording + mixing + effects on a home PC, marketed as "turn your computer into a recording studio" — satisfies the same four-property core with no cloud, no bundled-loop economy, no AI, and no edition gating in the core.
- The definition survives the check precisely because it names no era machinery: no bundled instruments (professional poles ship lean), no recording requirement (the DAW pass's FL Studio Fruity Edition counter-example: a MIDI-only edition is still the same Type), no desktop requirement (Soundtrap is browser-native), no beginner orientation (Apple applies the same framing to Logic Pro).
- The "virtual recording studio" phrase itself is the historical consumer description of what the industry later standardized as the "DAW" — the alias reading is the historically natural one.

## Uncertainties

- Whether market roundups use "virtual recording studio" as a standalone category heading was not directly verified (no roundup page fetched in this pass). The alias resolution rests on vendor-side interchange evidence, which is direct and multi-product; a roundup check would only corroborate.
- Pro Tools / Avid "studio" language was not re-fetched in this pass (carried structurally from the DAW pass); no claim in this document depends on it.
- Steinberg Cubase remains unfetchable (JS-rendered site, per the DAW pass); the heritage-MIDI-sequencer pole is covered by Reason/FL Studio evidence from the sibling passes.
- The broadcast "virtual studio" domain was not fetched (out of scope); the disambiguation rests on general domain knowledge and is recorded as a naming collision only, not as a researched boundary.

## Final Synthesis

The Virtual Recording Studio leaf resolves to the **Digital Audio Workstation product family**. Every product the market describes as a "virtual recording studio" — a complete music studio on your Mac, a single virtual studio package, a fully-fledged music studio inside your computer, a collaborative online studio, a virtual rack — satisfies the DAW core (persistent multitrack project; tracks of user-created recorded and/or authored material; mixing; rendered deliverable), and vendors use "studio" and "DAW" vocabulary interchangeably for the same products, sometimes in the same sentence. The framing is not restricted to home studios: it spans the free consumer pole (GarageBand), budget home-studio bundles (Mixcraft, n-Track), the professional tier (Logic Pro, Reason), and the cloud (Soundtrap). What the sibling passes predicted as a "bundled instruments + recording" variant is real but is a *positioning emphasis* (the bundled sound layer that lets a beginner produce in the box), not a defining structure. The leaf is therefore documented as the family's venue-framed alias: the studio the computer becomes. The canonical name remains DAW per the prior joint reviews; the taxonomy question (merge the three alias leaves vs keep both alias documents) is recorded for the taxonomy owner.
