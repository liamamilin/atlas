# Research Notes — Loop-based Music Production Application

## Research Goal

Understand the Application Type **Loop-based Music Production Application** (DIRECTORY 04.10 Music Production) from real products: what its central artifact is (the loop), which objects and surfaces define it (loop library, loop browser, arrangement timeline, musical lock), how the typical workflow runs from empty project to finished track, which rules govern it (tempo/key conformance, repeat/extend, content licensing), and where its boundary sits against the sibling Types of 04.09/04.10 (Digital Audio Workstation, Beat-making Application, Music Production Application, Virtual Recording Studio, Audio Editor) and adjacent Types (DJ Software, Live Music Performance Software, AI Music Generator, sample/loop marketplaces).

This leaf carries a **joint-review obligation** recorded in STATUS.md by the beat-making-application pass (2026-09-06): "beat-making-application vs digital-audio-workstation-daw / loop-based-music-production-application / music-production-application … flagged for joint review when DAW and Loop-based Music Production Application leaves are processed." The DAW portion was discharged by the DAW pass (2026-09-07, Boundary Findings #2/#3) and the music-production portion by the music-production pass (2026-09-08, ALIAS CONFIRMED). The loop-based portion is discharged below (Boundary Findings #1/#2). The DAW pass's forward expectation for this leaf: "assembling pre-made loops as the primary compositional act vs the DAW's record/author material. Loop tools are commonly embedded in DAWs … expect the same center-of-gravity pattern as beat-making."

## Initial Boundary

Initial hypothesis: a loop-based music production application centers on assembling **pre-made loops** — ready-made musical phrases (drum grooves, basslines, melodic riffs, percussion) — into arrangements on a timeline, with the application keeping the assembled loops musically coherent (tempo, and commonly key). The compositional origin of the material is *before* the user's project, in contrast to the DAW (material recorded/authored in the project) and beat-making (patterns authored in the project from sound sources).

Nearest neighbors: DAW (broader container; loop tools embedded in all of them), Beat-making (authored patterns vs pre-made phrases — gradient), Music Production Application (resolved alias of DAW), DJ Software (performs finished tracks), sample/loop marketplaces (content sources, not production apps), AI Music Generator (model composes).

Key definitional risks identified up front:
1. Is this an independent Type at all, or a workflow/variant of the DAW? (Loop tools are embedded in every DAW; ACID Pro self-describes as both "loop-based music software" and "a full-featured DAW".)
2. Is tempo/key conformance definitional, or merely the category's signature capability?
3. Historical check: the category is claimed to originate in 1998 (ACID) — the L0 must fit the 1998 original without any modern addition.

## Research Questions

1. What is the central artifact — the loop? the arrangement? the project?
2. What are the core objects (loop library, loop browser, loop types, tracks, regions, families/packs) and how do they relate?
3. What is the canonical workflow from empty project to finished track?
4. Which surfaces are typical (loop browser, timeline, editors, mixer, export)?
5. What rules matter: tempo/key conformance, repeat/extend semantics, loop-type/track-type constraints, content licensing (royalty-free vs licensed beats)?
6. What separates this Type from DAW / Beat-making / DJ / marketplaces / AI generators — structural or center-of-gravity?
7. Historical check: would the 1998 ACID-generation products still fit the definition? Would cloud/mobile-era products fit?
8. Is "loop-based music production" a vendor-recognized market category?

## Representative Products

| Product | Vendor | Why sampled |
|---|---|---|
| ACID Pro 11 | MAGIX (originally Sonic Foundry, 1998) | The category's origin and heritage/professional pole; self-described "the original loop-based music software"; full official product page + official tutorial index + official community announcement |
| GarageBand 10.4.x | Apple | Platform-bundled free consumer pole; Apple Loops + Loop Browser documented in a full Tier-1 user guide; shows loop assembly embedded in a complete DAW |
| Soundtrap | Spotify | Cloud/web collaborative pole with a strong education segment; loop library as headline feature; official product pages |
| BandLab | BandLab (Caldecott Music Group) | Free cloud/mobile entry pole with a social platform; Sounds loop library + Beats marketplace documented in Tier-1 help center; different content economy (claims, licensing) |

Supplementary observations (not primary samples): MAGIX Music Maker (same vendor as ACID Pro — consumer loop pole, official functions page via search capture); ACID Music Studio 11 (entry sibling of ACID Pro, official copy via retailer); Ableton Live Session View and FL Studio Loop Starter (carried from the DAW and beat-making passes — loop tooling embedded in DAWs).

## Sources

Research date: **2026-09-10**. Evidence layers: **A** = directly observed on an official source; **B** = cross-product commonality; **C** = canonical inference.

1. Apple — GarageBand User Guide (macOS): Welcome page; "Apple Loops in GarageBand"; "Add Apple Loops to a project" — https://support.apple.com/guide/garageband/welcome/mac , …/apple-loops-in-garageband-gbnd84045a00/mac , …/add-apple-loops-to-a-project-gbndc1d3db81/mac (fetched 2026-09-10) — Tier 1 (A)
2. MAGIX — ACID Pro product page content — https://www.magix.com/us/music-editing/acid and https://www.magix.com/us/music-editing/acid/acid-pro (content captured via web search 2026-09-10; direct fetch of magix.com paths returned 404 or redirected to the MAGIX homepage — the site is JS-rendered; limitation recorded) — Tier 2 (A, via search capture)
3. MAGIX — official tutorial index for ACID Music Studio & ACID Pro — https://www.magix.com/int/support/know-how/tutorial-videos/acid-music-studio-pro (captured via web search 2026-09-10) — Tier 2 (A, via search capture)
4. MAGIX — official community announcement "ACID Pro 11 — YOUR CREATIVITY. ACIDIZED." (MAGIX_Redaktion, 2022) — https://www.magix.info/us/forum/acid-pro-11-your-creativity-acidized--1301291 (captured via web search 2026-09-10) — Tier 2 (A, via search capture)
5. Soundtrap — main site and "Sample Packs: Royalty-Free Loops, Samples & One-Shots" product page — https://www.soundtrap.com/ , https://www.soundtrap.com/content/product/audio-loops-sample-packs (fetched 2026-09-10) — Tier 2 (A)
6. BandLab Help Center — "BandLab Sounds" and "BandLab Beats" — https://help.bandlab.com/hc/en-us/articles/360018942593-BandLab-Sounds , …/54864777405977-BandLab-Beats (fetched 2026-09-10) — Tier 1 (A)
7. BandLab Help Center — Creation category index (fetched 2026-09-10) — Tier 1 (A, structure only)
8. Sound On Sound — "Magix ACID Pro Next" review (Robin Vincent, August 2019) — https://www.soundonsound.com/reviews/magix-acid-pro-next (captured via web search 2026-09-10) — Tier 3 (historical grounding)
9. Sweetwater — ACID Pro 9 product listing copy (captured via web search 2026-09-10) — Tier 3
10. Sibling research (boundary alignment and carried evidence): research/digital-audio-workstation-daw.md, research/beat-making-application.md, research/music-production-application.md (2026-09-05/06/07/08)

**Sourcing limitations:**
- MAGIX's site is JS-rendered; direct fetches of ACID Pro pages failed (404 / homepage redirect). ACID Pro evidence rests on official page content captured through a search engine (quoted verbatim), the official tutorial index, and the official community announcement — Tier 2 strength, not manual-level Tier 1. No precise ACID operational claims (loop counts, Beatmapper behavior, exact edition matrices) are promoted anywhere.
- Soundtrap's support center (support.soundtrap.com) returned transport errors on two attempts and was abandoned per the network rule; Soundtrap evidence is official marketing/product pages (Tier 2). No help-center-level operational claims are made for Soundtrap.
- BandLab numeric limits (weekly claims by tier, My Sounds storage/duration limits, Beats license term) are vendor-published and recorded here only; they are not promoted to the final document.
- Wikipedia and 1990s consumer loop software (eJay class) were not fetched; the historical check rests on ACID's own documented lineage plus independent press (Sound on Sound).

## Product A — ACID Pro 11 (MAGIX) — Layer A (Tier 2 via search capture)

- Positioning: "ACID Pro is the original loop-based music software, making it easy to create original songs and beats without any prior experience. Take complete creative control with high-quality loops, multitrack audio, MIDI recording, and live takes."
- "The original loop-based composer … combining loops, MIDI, and live takes in an intuitive drag-and-drop workflow. Turn your ideas into real tracks, no training required."
- Category breadth: "Loop-based composing — Produce any genre. Mix any style. From blues, rock, and jazz to metal, country, and classical."
- Content economy: "Endless inspiration with royalty-free loops"; "build pro-quality, royalty-free tracks that give your content a custom-made sound" (content-creator/soundtrack context: "Place, move, and adjust loops with precision to build a custom soundtrack that follows your visuals. ACID Pro keeps everything in time and on point.")
- Core workflow: "To create your own original composition, simply select a sound loop, drag it into your timeline, and play the results."
- **The musical lock, vendor-stated**: "ACID Pro matches the loops you choose to the tempo and the key of the music, so it sounds great, even if you don't know what 'tempo' and 'key' means."
- Self-description spanning both names: "ACID Pro is a full-featured digital audio workstation (DAW) that supports loop-based music production, multitrack audio, and MIDI workflows. You can create musical projects that include any one or any combination of all three workflows." And: "You can use it to record multiple tracks simultaneously, punch into a track to record another take, edit tracks, mix multiple tracks of audio, loop content, and MIDI-generated music, and deliver it all as a single mixed file."
- DAW furniture around the loop center: "Route tracks freely, group them through shared effects and controls, fold in submixes, and solo or mute with ease"; VSTi support ("Endless creativity with MIDI and VSTi support").
- Heritage (official community announcement): "ACID Pro 11 takes loop-based music production one step further - yet again. Since its historic invention of today's industry standard in 1998, ACID offers the most extensive options for arranging, editing and resampling audio." Ships with "ACIDized Loops (12 GB … or 16 GB with ACID Pro 11 Suite)" (vendor figures, research notes only).
- Official tutorial index (workflow vocabulary): "produce your own tracks using ACID sound loops, cut loops with the Chopper and play software instruments"; Chopper = "a creative tool which you can use to make your own loops and remixes … cut any kind of audio material into short loops and then insert these into your project"; "MIDI Playable Chopper … the Chopper can be used like a sampler and played using a MIDI keyboard"; "Tempo and pitch editing"; "Composing … create different sections of a song and then combine them into the finished product."
- Entry sibling: ACID Music Studio 11 — "Compose original music with the super easy loop-based production tool"; retailer copy of official positioning: "ACID Music Studio helps you get started in loop-based music production. Includes over 2,500 ACID loops, eight virtual instruments, and six effects" (figures research-notes-only).
- Independent press (Tier 3, historical grounding): Sound on Sound — "ACID Pro is the original loop-based remixing program … When it first appeared in the late '90s, ACID's extraordinary ability to manipulate the pitch and tempo of looped audio created a whole genre of computer-based loop sequencing that had previously been the realm of scratch DJs and hardware samplers. Loops in ACID contained tempo and key information that allowed them to be matched automatically when used in the same project. Armed with a sample CD of 'Acidized' loops, you could paint them onto a timeline and pull together arrangements at great speed." Sweetwater: "The original loop-based DAW … automatic pitch and tempo-matching, loop reviewing, unlimited tracks."

## Product B — GarageBand 10.4.x (Apple) — Layer A (Tier 1 user guide)

- Positioning: "GarageBand is a fully equipped music creation studio right inside your Mac … Record, use loops, add effects, then mix and share your music with the world."
- **Loop definition**: "Apple Loops are prerecorded musical phrases or riffs that you can use to easily add drum beats, rhythm parts, and other sounds to a project. These loops contain musical patterns that can be repeated over and over, and can be extended to fill any amount of time."
- **The musical lock, vendor-stated**: "When you add an Apple Loop to a project, a region is created for the loop. When the project plays, the region plays at the project's tempo and key. You can use several loops together, even if the loops were recorded at different speeds and in different keys." And on add: "The added Apple Loop always matches the project tempo."
- **Loop type system**: audio loops (blue, audio recordings, edited like audio regions), MIDI loops (green, editable like MIDI regions, instrument-swappable, viewable in Piano Roll/Score editors), Drummer loops (yellow, carry performance information); conversions by dragging a loop onto a different track type (MIDI→audio, Drummer→MIDI, Drummer→audio).
- **Loop Browser**: "find loops with the instrument, genre, and feel you want, play loops, and add loops to your project … create a selection of your favorite loops, create your own loops, and customize the Loop Browser." Third-party Apple Loops can be added to the browser; more sounds and loops via content packs.
- **Assembly**: drag a loop to an empty Tracks area → "A new track of the appropriate type (audio, MIDI, or Drummer) is created, and the loop is added to the new track"; drag onto existing tracks to place/conform.
- **Repeat/extend**: "Extend a loop so it repeats — drag the upper-right edge of the region for the desired number of repetitions" (or a keyboard shortcut); loops "can be extended to fill any amount of time."
- **Loop families**: "Many Apple Loops are part of a loop 'family.' Loops that are part of a family have the same name, but each has a unique number at the end … Loops in the same family work well together. After you add a loop to your project, you can easily replace it with any other loop in the same family."
- **Custom loops**: "Create custom Apple Loops" (user material can become loop content that re-enters the browser).
- Project musical grid: project properties include tempo, key and scale, time signature; Tempo track and Transposition track for changes over time.
- Full DAW furniture around the loop center: audio/software-instrument recording with takes, Audio/Piano Roll/Score/Drummer editors, mixing and automation, Smart Controls, Audio Units plug-ins, movie scoring, share/export (Music app, AirDrop, Mail, disk/iCloud, CD).

## Product C — Soundtrap (Spotify) — Layer A (Tier 2 official pages)

- Positioning: "Music Production, made simple. Create & record easily with powerful tools and sounds, all in one place." Collaborative studio: "Make music online anytime, with anyone, on any device"; real-time collaboration "through video and chat, directly in the studio"; comments; auto-save.
- **Loop library as headline**: "Thousands of loops and sample packs, one-shots, and sound effects"; "Soundtrap offers over 23 000 exclusive and royalty-free loops, instruments, sound FX, and samples — all available inside the Studio!" (figure research-notes-only). Bi-weekly exclusive "Soundtrap Originals" packs by genre (Phonk, Drill, Lo-Fi, K-Pop, …).
- **Loop nature**: "Loops are in either MIDI or wave form and can be layered and mixed together to create interesting rhythms and melodies."
- **Loop Library surface**: "open up a new project and click on the note icon … This opens up the Loop Library where you can browse through a variety of categories, like Hip Hop, Rock, Sound FX, Drums, Piano, MIDI, and Vocals. Or you can search for specific sounds based on instrument, style, genre, vibe, format, artist or song, etc."
- **Assembly**: "Preview any sound or loop before adding them and save the ones you want to keep for later. Once you've decided on a loop, add them to a new track and start building."
- **Fitting controls**: "Soundtrap's DAW lets you change the speed and pitch of a loop, as well as key and scale. You can also chop up samples and add effects to the sound." (Adjustment capability — automatic matching not claimed on this page; assertion kept at adjustment strength.)
- **Templates from loops**: "Every Soundtrap Original also includes a demo project built with loops and instruments from the Sound Packs … lets you use the demo project as a template to create your own song."
- **Licensing**: "Soundtrap Originals consist of sounds, loops, and samples that are 100% royalty-free. This means that you can commercially release any original song that you've created using sounds from the Soundtrap library."
- Plan gating on library access; adjacent tools: Patterns beatmaker, vocal tuning, automation, mixing/mastering ("auto-mixing to EQs, compressors"); Education segment (Soundtrap for Education); podcasting sibling.

## Product D — BandLab — Layer A (Tier 1 help center) + carried sibling evidence

- **BandLab Sounds** (help center): "a massive, world-class library of **royalty-free loops, samples, and one-shots** designed to make sure you never have to start a track from a blank screen." "thousands of royalty-free loops and sounds sorted by style, plus the ability to import your own loops and sounds."
- **Assembly workflow** (web): browse the Sounds site (Sidebar: "Browse, Packs, Loops or One Shots") → preview → "Open In Studio" → "Drag and drop the loop you desire into the Studio"; in-studio: "Double-click, or click, drag, and drop the sound you'd like to use from the Loop Pack browser straight into the Studio to create a track for it." Mobile: tap sample to preview → "+" to add to the Studio.
- **My Sounds**: personal cloud sample vault — upload own samples, organize into collections, tag for search; membership-gated uploads (vendor limits: 2 GB storage, 1-minute per sample — research notes only).
- **Claims economy**: downloads from the library consume weekly "claims" tiered by membership (Free 20 / Pro 100 / Max 500 samples — vendor figures, research notes only); claims do not roll over.
- **BandLab Beats** (help center): a marketplace of licensed instrumentals — "Pull tracks directly into the Studio to start recording instantly"; producers sell **non-exclusive licenses** (vendor-stated 10-year term) rather than ownership; purchased beats open in the Studio. This is the licensed whole-track pole adjacent to loop assembly.
- Carried from the beat-making pass (fetched 2026-09-06): the Studio is "a free, cloud-based Digital Audio Workstation (DAW) that lets you record, edit, and mix music in your browser or on your phone"; track types include Voice/Audio, Instrument, Drum Machine; projects cloud-saved with revision history; forking, publishing, and a social platform surround the studio; vendor-published limits (15-minute projects, 16 audio/MIDI tracks) research-notes-only.

## Supplementary observations

- **MAGIX Music Maker** (official functions page via search capture; same vendor as ACID Pro, therefore not a primary sample): "Easy music production with loops, virtual instruments and drag-and-drop"; "6 Soundpools from different genres"; Loop Browser ("Explore thousands of loops across all genres … pick your favorites"); genre filter; "up to 99 audio and MIDI tracks in the Arranger"; Beatbox Pro 3 for custom beats; VST support; export formats; FAQ: "Music Maker is easy-to-use music production software for beginners … create your own songs and beats, make music with virtual instruments and loops, add effects, and arrange tracks—all in one intuitive interface." Confirms the consumer loop pole and the "Soundpool" content economy.
- **Ableton Live Session View** (carried from research/digital-audio-workstation-daw.md): clips as "the basic musical building blocks … a piece of musical material: a melody, a drum pattern, a bassline or a complete song", launched in real time — the performance-facing edge of loop-based work, embedded in a general DAW.
- **FL Studio Loop Starter** (carried from research/beat-making-application.md): "instant, genre-based loop stacks" as idea-starters inside a pattern-first DAW.

## Cross-product Comparison

| Dimension | ACID Pro | GarageBand | Soundtrap | BandLab | Evidence |
|---|---|---|---|---|---|
| Pre-made loop library as headline material source | ✔ ("high-quality loops", ACIDized loops bundled) | ✔ (Apple Loops + content packs) | ✔ (loops/sample packs "all available inside the Studio") | ✔ (BandLab Sounds) | A×4 |
| Loop browser with filtering + preview + favorites | ✔ (loop workflow; genre breadth claims) | ✔ (instrument, genre, feel; play; favorites) | ✔ (instrument, style, genre, vibe, format; preview; save) | ✔ (Browse/Packs/Loops/One Shots; preview; favourites/collections) | A×4 |
| Drag loop into timeline → track created / assembly | ✔ ("select a sound loop, drag it into your timeline") | ✔ (drag → new track of appropriate type) | ✔ ("add them to a new track and start building") | ✔ ("drag … straight into the Studio to create a track for it") | A×4 |
| Tempo conformance of loops to the project | ✔ ("matches the loops you choose to the tempo") | ✔ ("always matches the project tempo") | ✔ (speed of a loop changeable; adjustment-level evidence) | not directly evidenced | A×2 strong + A×1 adjustment; degrade for BandLab |
| Key conformance / tonal fit | ✔ ("and the key") | ✔ ("plays at the project's tempo and key") | ✔ ("as well as key and scale" — adjustment-level) | not directly evidenced | A×2 strong + A×1 adjustment |
| Repeat/extend loops to fill time | ✔ (arranging/resampling options; paint onto timeline per press) | ✔ ("extended to fill any amount of time"; drag edge) | implied ("layered and mixed together") | implied (loopable regions — carried) | A×2 strong; degrade elsewhere |
| Loop types beyond audio (MIDI/instrument loops) | ✔ (loops + MIDI workflows; MIDI-playable chopper) | ✔ (audio/MIDI/Drummer loops + conversions) | ✔ ("either MIDI or wave form") | not evidenced (audio loops; patterns separate) | A×3 — common, not universal |
| Custom loop creation from own material | ✔ (Chopper: cut audio into loops) | ✔ (Create custom Apple Loops) | ✔ (chop up samples) | ✔ (import/upload own loops; My Sounds) | A×4 |
| Loop families / packs / variation swap | ✔ (ACIDized loop packs) | ✔ (loop families, swap within family) | ✔ (packs + demo-project templates) | ✔ (packs; Open In Studio) | A×4 (form varies) |
| Mixing/effects/automation around the loop center | ✔ (routing, groups, submixes, solo/mute) | ✔ (mix and automate) | ✔ (mixing/mastering tools, auto-mixing) | ✔ (FX, automation, mastering — carried) | A×4 |
| Recording alongside loop assembly | ✔ (multitrack audio, live takes, punch-in) | ✔ (audio + software instruments, takes) | ✔ (record vocals; plug-in mic/guitar) | ✔ (Voice/Audio tracks — carried) | A×4 |
| Rendered deliverable | ✔ ("deliver it all as a single mixed file") | ✔ (share/export songs) | ✔ (mix/master; release) | ✔ (export/publish — carried) | A×4 |
| Royalty-free content economy | ✔ ("royalty-free loops/tracks") | ✔ (bundled + packs) | ✔ ("100% royalty-free … commercially release") | ✔ (royalty-free Sounds; licensed Beats marketplace beside) | A×4 |
| Cloud/collaboration layer | — (desktop) | — (local; share/export) | ✔ (real-time collaboration, video/chat, auto-save) | ✔ (cloud projects, forking, publishing — carried) | A×2 — variant |
| Education positioning | — | — (learn-to-play lessons only) | ✔ (Soundtrap for Education) | — | A×1 — variant |
| Entry economics | paid + trial; entry sibling (Music Studio) | free with platform | free tier + plans | free tier + membership | A×4 — variant |

Reading: the first twelve rows are present in every sampled product (two rows with degraded strength on one product) — candidate defining core plus common mature structure. The last three rows vary — variant/optional structure.

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

```text
Loop library (pre-made, reusable musical phrases as the primary material source)
└── Loop assembly on a musical timeline (loops placed, repeated, and chained into an arrangement)
    └── Musical lock (loops conform to the project's tempo — and commonly its key —
        so separately sourced loops combine into one coherent piece)
        └── Rendered audio deliverable
```

Four properties. Remove any one and the product stops being recognizable as loop-based music production:

1. **Loop library** — the material is ready-made musical phrases (drum grooves, basslines, melodic riffs, percussion, vocal chops) held in a browsable library. Without it there is nothing to assemble; the product becomes a recorder or a general DAW.
2. **Loop assembly on a musical timeline** — the central compositional act is placing, repeating, and chaining loops into an arrangement. Without it the product is a loop player or a sample library, not a production tool.
3. **Musical lock** — loops conform to the project's musical grid (tempo; and commonly key/scale) so that loops from different sources and different original speeds/keys combine into one coherent piece. This is the property that makes assembly a *musical* production act rather than audio-file stacking; it is the category's founding capability (ACID, 1998) and is vendor-stated in the sampled products. Without it the product drifts toward media assembly or a fixed-audio sampler.
4. **Rendered audio deliverable** — the assembled track leaves the application as audio. Without it, not a production application.

Deliberately NOT in L0 (tested against the historical/market-sample check):
- **Key matching specifically** — tempo conformance is the strongly-evidenced universal; key conformance is vendor-stated in three of four sampled products but is phrased "commonly" in the canonical model. (Both ACID and GarageBand state key matching directly; Soundtrap states key/scale adjustment; BandLab not evidenced.)
- **MIDI/instrument loop types** — the original ACID was audio-loop-based; MIDI loops are L1.
- **Mixing depth, recording, plugin hosting** — inherited DAW furniture; L1 (present in all sampled products but the loop center stands without deep versions of them — entry products ship simplified versions).
- **Cloud, collaboration, education, social publishing, subscription/claims economies, AI features** — L2.
- **Vendor loop formats and branded tools** (ACIDized loops, Apple Loops, Soundpool, Sounds/Beats, Chopper, Loop Browser color system) — L3.

### L1 — Common Mature Structure

- **Loop browser/library surface** — filtering by instrument/genre/feel/vibe/mood, search, audition/preview, favorites/collections (A×4).
- **Drag-to-timeline assembly with automatic track creation** — dropping a loop creates or populates a track of the appropriate type (A×4).
- **Repeat/extend semantics** — a placed loop can be repeated/extended to fill any length of time (A×2 strong, implied elsewhere).
- **Loop type system** — audio loops vs MIDI/instrument loops, with conversion paths (A×3).
- **Custom loop creation** — chopping/slicing the user's own audio into loops; saving user material as loops; importing own loop libraries (A×4).
- **Loop families / packs / templates** — curated groups of mutually compatible loops; swap-within-family; demo/template projects built from packs (A×4, form varies).
- **Mixing, effects, automation** — per-track levels/pan/processing over the loop arrangement (A×4).
- **Recording alongside loops** — vocals/instruments recorded over loop foundations (A×4).
- **Export/share** — the finished mix leaves as audio; cloud variants add publishing (A×4).
- **Royalty-free content economy** — bundled + purchasable/subscription loop packs, commercially usable (A×4).

### L2 — Variant / Optional Structure

- **Delivery model**: desktop perpetual/paid (ACID Pro), platform-bundled free (GarageBand), cloud/web subscription with plan gating (Soundtrap), free cloud/mobile with membership economy (BandLab).
- **Collaboration depth**: solo desktop vs real-time cloud collaboration (video/chat, comments, auto-save) vs social publishing/forking community.
- **Education positioning** (one sampled product).
- **Depth of the surrounding DAW**: full multitrack recording/MIDI/plugin hosting (ACID Pro, GarageBand) vs simplified entry environments (Music Maker, ACID Music Studio, mobile BandLab).
- **Performance orientation**: real-time clip/loop launching as a surface (carried Live evidence) — the edge toward Live Music Performance Software.
- **Licensed-beat marketplace extension**: whole-instrumental licensing pulled into the studio (BandLab Beats) — adjacent commerce, not the assembly core.
- **AI-era features**: stem separation and similar (carried from sibling passes; not directly evidenced for this sample — not asserted).

### L3 — Vendor-specific (research notes only)

- ACID Pro: "the original loop-based music software" positioning; 1998 heritage claim; ACIDized loops (tempo+key metadata in the loop file); Chopper / MIDI Playable Chopper; Beatmapper; "loop-based + multitrack + MIDI workflows, any combination" framing; ACID Music Studio entry sibling; Producer Planet content store; VEGAS Pro Suite bundle.
- Apple: Apple Loops format; Loop Browser with blue/green/yellow type colors; Drummer loops; loop families with numbered variants; "Get more sounds and loops" packs; Transposition/Tempo tracks; GarageBand-as-free-DAW bundling.
- Soundtrap: Soundtrap Originals bi-weekly exclusive packs; demo-project templates per pack; plan-gated library access; 23,000+ loops figure; education programs; real-time video/chat collaboration.
- BandLab: Sounds vs Beats split; weekly claims economy by membership tier; My Sounds cloud vault (2 GB / 1-minute limits); "Open In Studio"; forking/publishing social layer; 15-minute/16-track project limits (carried).
- MAGIX Music Maker: Soundpools; Beatbox Pro 3; 99-track Arranger figure.

## Vendor-specific Findings

- "Loop-based music production" is a vendor-recognized category phrase: MAGIX uses it across two product lines (ACID Pro: "the original loop-based music software"; ACID Music Studio: "get started in loop-based music production"; Music Maker: "easy music production with loops"), and independent press uses it as a genre of software (Sound on Sound: ACID "created a whole genre of computer-based loop sequencing").
- The same vendors simultaneously describe their loop products as DAWs (ACID Pro: "a full-featured digital audio workstation (DAW) that supports loop-based music production"; BandLab Studio: "a free, cloud-based DAW"; Soundtrap: "Soundtrap's DAW"; GarageBand: "a fully equipped music creation studio") — the label blur is structural, not sloppy marketing: the loop center sits on the DAW substrate.
- ACID's own FAQ frames loop-based, multitrack-audio, and MIDI as three combinable workflows in one project — the vendor's own words show the shared substrate and distinct centers.
- Loop content licensing splits into two regimes in the sample: royalty-free loops (commercially usable, bundled or subscription-gated) vs licensed instrumentals (non-exclusive, term-limited, marketplace-purchased). Both feed the same studio.

## Rejected Findings

1. **"Loop-based production is a DAW variant/workflow, not a Type"** — rejected as grounds for collapsing the leaf: the category phrase is vendor-recognized across multiple vendors and 25+ years of products; the center of gravity (assemble pre-made phrases) is stable and distinct; the same center-of-gravity pattern was ratified for beat-making in joint review. The gradient vs DAW is documented instead (Boundary Findings #1).
2. **"Loops must be third-party content"** — refined: the defining property is that the material's compositional origin precedes the user's project (ready-made phrases); every sampled product also lets users create custom loops that re-enter the same assembly loop. The library is the primary material source, not necessarily exclusively third-party.
3. **"Requires MIDI loops / instrument loops"** — rejected: the 1998 original was audio-loop-based; MIDI loops are common mature structure.
4. **"Key matching is definitional"** — weakened: tempo conformance is the universal, strongly-evidenced property; key conformance is vendor-stated in three of four products and phrased "commonly" in the canonical model.
5. **"Loop-based = clip launching / live performance"** — rejected: real-time launching is the performance-facing variant edge (carried Live evidence); the Type's center is assembly into finished tracks.
6. **"Genre-specific (EDM/hip-hop)"** — rejected: the heritage vendor claims "any genre … blues, rock, jazz, metal, country, classical"; sampled packs span dozens of genres.
7. **"Cloud/collaboration is definitional"** — rejected: desktop products (ACID Pro, GarageBand) fit the core fully offline.
8. **"Free tier is definitional"** — rejected: entry economics vary (paid, platform-bundled free, freemium, subscription).

## Boundary Findings

1. **vs Digital Audio Workstation / DAW (04.09 — JOINT REVIEW DISCHARGED for this leaf)**: the strongest overlap, held as a center-of-gravity gradient exactly as the DAW pass predicted. The DAW's defining center is a general multitrack project filled with **user-created material** (recorded or authored in the project); the loop-based Type's defining center is **assembly of pre-made loops** whose musical content was fixed before the project. Loop tools are embedded in DAWs (Live's browser+clips, FL's Loop Starter, GarageBand's Apple Loops inside a full DAW), and loop products embed DAW furniture (ACID Pro self-describes as "a full-featured DAW that supports loop-based music production"; ACID's FAQ frames loop-based/multitrack/MIDI as combinable workflows). Directional tests: remove loop assembly from a loop product → a general DAW remains (recording/editing/mixing depth persists in ACID Pro, GarageBand); remove general recording/authoring depth → a loop-based tool remains (entry products ship simplified DAW furniture while keeping the loop center). Both leaves stand as independent Types; no taxonomy change; the gradient is documented on this side and matches the beat-making precedent.
2. **vs Beat-making Application (04.10 sibling — JOINT REVIEW DISCHARGED for this leaf)**: the discriminator is the **compositional origin of the rhythmic/musical material**. Beat-making authors patterns in the project from sound sources (kit + step grid + pads); loop-based assembles phrases whose composition happened before the project. Both place repeating material on a timeline and render audio — the overlap is real (loop tools host drum grids; beat tools arrange loops; Soundtrap ships both a loop library and a Patterns beatmaker), and the boundary is a gradient on the same test as the DAW seam: remove pattern authoring → a loop tool remains; remove pre-made phrase assembly → a beat maker remains. Consistent with research/beat-making-application.md Boundary Findings ("the differentiator is the compositional origin (authored pattern vs pre-made loop)").
3. **vs DJ Software (04.12, unprocessed)**: DJ software performs and beat-matches finished tracks in real time; loop-based production assembles new tracks from phrase material. Historical note from independent press: before ACID, loop sequencing "had previously been the realm of scratch DJs and hardware samplers" — this Type was created by moving that act into arrangement software. Gradient at the performance edge (clip launching).
4. **vs Sample/loop libraries and marketplaces (Loopcloud/Splice class; BandLab Beats; Producer Planet; Soundtrap Originals as a store)**: content sources without an arrangement/render core are not this Type; they feed the loop library. A marketplace embedded in a studio (BandLab Beats "pull tracks directly into the Studio") is an extension surface of the production app, not the Type itself.
5. **vs AI Music Generator (04.22, processed)**: the model composes from a specification; here humans made the loops and the user assembles them. Even where loop content is machine-assisted, the assembly act remains the user's. Consistent with the sibling's recorded boundary.
6. **vs Live Music Performance Software / looper hardware (04.12, unprocessed)**: real-time performance looping (triggering phrases live) vs production assembly into finished tracks. The clip-launching surface straddles the seam; the deliverable separates the Types.
7. **vs Audio Editor (04.09, processed)**: no loop library, no assembly, no musical lock; single-file waveform work. Clean boundary, consistent with the sibling pass.
8. **vs Music Production Application (04.10, processed as DAW alias)**: the umbrella name covers the DAW family; loop-based production is one of the narrower centers under it (with beat-making), now documented as its own Type. No conflict with the alias resolution.
9. **vs Virtual Recording Studio (04.10, unprocessed)**: different center — studio-hardware/recording-chain simulation vs loop assembly. No conflict expected; flagged for the sibling pass.

**"Remove what and it becomes another Type" criteria:**
- Remove the pre-made loop library (material must be recorded/authored in-app) → DAW territory.
- Remove assembly into arrangements (loops only browsed/previewed/triggered) → sample library / marketplace territory.
- Remove the musical lock (loops as fixed audio files stacked manually) → audio-editor / media-assembly territory.
- Remove production/arrangement (real-time triggering only) → DJ / live-performance territory.
- Remove human-made loops (a model composes from a specification) → AI music generator territory.

## Historical / Market-Sample Check

- **ACID (Sonic Foundry, 1998 → Sony → MAGIX)**: the category's documented origin. The vendor's own announcement claims the 1998 invention of "today's industry standard"; independent press confirms the founding behavior — loops carrying tempo and key metadata, matched automatically, "painted onto a timeline" to "pull together arrangements at great speed". The 1998 product satisfies the L0 fully with none of the modern additions (no cloud, no subscription economy, no AI, no collaboration).
- **Modern cloud/mobile poles (Soundtrap, BandLab)**: the same structure on a cloud substrate with plan/membership economies — fits without desktop installation.
- **Platform-bundled pole (GarageBand)**: the same structure embedded in a free general DAW — fits.
- Conclusion: the definition abstracts across eras and delivery models; no re-abstraction needed beyond keeping key-matching phrased as "commonly" and keeping MIDI loop types, mixing depth, and cloud out of the core.

## Uncertainties

1. ACID Pro evidence is Tier 2 (official page content captured via search; direct fetches failed on the JS-rendered site). No manual-level ACID operational detail (exact loop counts, Beatmapper behavior, edition matrices) is asserted anywhere.
2. Soundtrap's support center was unreachable (2 transport errors, abandoned); Soundtrap conformance evidence is adjustment-level ("change the speed and pitch of a loop, as well as key and scale"), not automatic-match level; the final document phrases it accordingly.
3. BandLab loop tempo/key conformance was not directly evidenced in fetched text and is not asserted; BandLab's loop assembly workflow (browse → preview → drag into Studio → track created) is Tier 1.
4. Vendor-published figures (23,000+ loops, 2,500 loops, 12/16 GB loop bundles, claims tiers, 2 GB/1-minute vault limits, 10-year license term, 99-track Arranger) are recorded here only and kept out of the final document.
5. eJay-class 1990s consumer loop software was not verified against a fetched source; the historical check rests on ACID's documented lineage plus independent press.
6. Ableton Live and FL Studio loop features are carried from sibling passes (fetched 2026-09-06/07), not re-fetched.

## Final Synthesis

A Loop-based Music Production Application is a music-production environment whose defining structure is: a **loop library** of pre-made, reusable musical phrases → **assembly of those loops on a musical timeline** (place, repeat, chain into an arrangement) under a **musical lock** (loops conform to the project's tempo, and commonly its key, so separately sourced phrases combine into one coherent piece) → a **rendered audio deliverable**. Around this core, mature products add the loop browser (filter/preview/favorites), drag-to-timeline assembly with automatic track creation, repeat/extend semantics, audio-vs-MIDI loop types with conversions, custom loop creation from the user's own material, loop families/packs/templates, mixing and recording (inherited DAW furniture), export, and a royalty-free content economy. Delivery model (desktop paid / platform-bundled / cloud subscription / free cloud-mobile), collaboration depth, education positioning, DAW depth, performance orientation, and licensed-beat marketplaces are variants. The Type stands as an independent leaf with center-of-gravity gradients against the DAW (user-created material vs pre-made phrases) and beat-making (authored patterns vs pre-made phrases) — the same pattern the sibling passes ratified — with the joint-review obligation discharged on this side.
