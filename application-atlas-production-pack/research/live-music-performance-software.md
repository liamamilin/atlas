# Research Notes — Live Music Performance Software

Research date: **2026-09-08**
Directory leaf: `Live Music Performance Software` (§04.12 DJ & Performance)
Slug: `live-music-performance-software`
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what software of this Type is, from real products: what objects it holds, what the performer prepares before a show, what the performer does during the show, what the deliverable is, and where the Type ends against its two obvious neighbors — DJ Software (same Family, §04.12) and Digital Audio Workstation (§04.09). This pass also carries a joint-review obligation from the dj-software pass (STATUS.md Boundary Issues, 2026-09-07): ratify or reject the working-material seam, and give a recommendation on where Auto DJ/Automix-style automation surfaces and the hardware-ecosystem export posture belong.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this is software a musician operates **on stage**, live — as opposed to DJ software (mixing finished recorded tracks) and as opposed to a DAW (producing a recorded deliverable).
- Likely two product philosophies: (a) clip/scene launching environments where the material is clips and patterns triggered in real time; (b) live rig / plugin-host environments where the material is sound patches and song configurations recalled per song.
- Nearest neighbors: DJ Software (working material), DAW (deliverable), Music Production Application (umbrella), Audio Editor (different object), Worship Presentation Software (visually adjacent "performance" but not music-producing).
- Unknowns: whether a single canonical model covers both poles; whether hardware control mapping is definitional or common; where live looping and backing-track playback rigs sit; whether older/regional/hardware-era practice fits the definition.

## Research Questions

1. What is the working material of each product, and who authors it?
2. What exactly happens during the show — what does the performer trigger, recall, play, and control?
3. What is the deliverable of the software? Is there a persistent edited document, or is the show the output?
4. How is the show organized — scenes, songs, set lists, patches?
5. How does hardware control (keyboards, footswitches, pads) attach to the software?
6. How do the products handle tempo, sync, and real-time stability?
7. Where is the seam to DJ Software and to the DAW? Can one product instantiate both Types?
8. Historical check: would pre-software and non-clip-based live rigs still fit the definition?

## Representative Products

| Product | Pole | Why selected | Access |
|---|---|---|---|
| Ableton Live | clip-launch environment (dual-role with production DAW) | the canonical product of the category; Session View defines the clip-launch pattern | official manual (Live 12) — fetched |
| Bitwig Studio | clip-launch environment, different philosophy ("two sequencers") | second philosophy on the same pole; explicit live-performance framing | official user guide — fetched |
| Apple MainStage | live rig / patch host for instrumentalists | the mass-market rig pole; patch/setlist model; cheap prosumer tier | official user guide — fetched |
| Cantabile | live rig / plugin host, small independent vendor | second rig philosophy (songs/racks/states); shows the pole is a market, not one vendor | official guides — fetched |
| Gig Performer | live rig / wiring-style plugin host | intended fifth sample for cross-platform rig diversity | official docs unreachable (403/404 ×2) — abandoned per network rule; no observations recorded |

The sample deliberately spans: two product philosophies (grid vs rig), customer tiers (prosumer mass-market vs pro independent), and vendor sizes (major vendor, independent, one-person-company).

## Sources

Tier 1 (official operational documentation, fetched 2026-09-08):

- Ableton — *Live Reference Manual v12, §3 Live Concepts* — https://www.ableton.com/en/manual/live-concepts/
- Bitwig — *Bitwig Studio User Guide, §6 The Clip Launcher* — https://www.bitwig.com/userguide/latest/the_clip_launcher/ ; guide index — https://www.bitwig.com/userguide/latest/
- Apple — *MainStage User Guide* (4.3) — https://support.apple.com/guide/mainstage/welcome/mac
- Cantabile — *Guides: Song and Rack States* — https://www.cantabilesoftware.com/guides/states ; *Set Lists* — https://www.cantabilesoftware.com/guides/setLists ; guides index — https://www.cantabilesoftware.com/guides/

Source-access limitation: Gig Performer's documentation returned 403 (docs) and 404 (user-guide path) on 2026-09-08; per the network rule the source was abandoned after two failures. No claims in these notes rely on Gig Performer specifics. The rig-pole findings therefore rest on MainStage + Cantabile direct observation; the cross-platform third rig vendor remains unverified. Assertion strength for rig-pole claims is kept at "both sampled rig products" rather than generalized to the whole market.

---

## Product Observations

### Ableton Live (manual v12, §3 "Live Concepts") — evidence layer A

- The document is a **Live Set** (inside a **Live Project** folder). A Set is saved, reopened, exported.
- The basic musical building block is the **clip** — "a piece of musical material: a melody, a drum pattern, a bassline or a complete song." Audio clips reference samples (with real-time warping to match the Set's tempo); MIDI clips contain notes/controllers.
- Two views over the same tracks: the **Arrangement** (clips laid out on a linear timeline) and the **Session** — explicitly described as "a real-time-oriented 'launching base' for clips. Every Session clip has its own play button that allows launching the clip at any time and in any order."
- **Scenes**: "one usually places clips that should play alternatively in the same Session View column, and spreads out clips that should play together across tracks in rows, or what we call scenes." Scene tempo/time signature values exist.
- A track can play only one clip at a time; launching a Session clip takes over the track ("Session clips take precedence"); a *Back to Arrangement* button returns tracks to timeline playback.
- Clips have per-clip **launch settings** and **follow actions** (auto-advance behavior).
- **Launch quantization**: session launching and recording are "subject to real-time launch quantization" — triggers snap to the musical grid.
- **Crossfader**: "can create smooth transitions between clips playing on different tracks… like a typical DJ mixer crossfader," assignable to any number of tracks.
- **MIDI/Key Map Mode**: "To liberate the musician from the mouse, most of Live's controls can be remote-controlled via an external MIDI controller." Session clips can be mapped to keys or key ranges for chromatic playing. Mapped messages are filtered out of recording.
- Tempo is adjustable on the fly; Tempo Follower and Link exist for synchronization (control-bar section).
- Session recording: clips can be recorded into slots "on the fly… very useful for the jamming musician"; improvisation can be logged into the Arrangement for refinement.
- The manual states Live is used to create "songs, scores, remixes, **DJ sets or stage shows**" — the vendor itself places stage shows alongside production uses.
- Export Audio/Video exists (production-oriented deliverable), alongside saving Sets.

### Bitwig Studio (user guide §6 "The Clip Launcher") — evidence layer A

- The product is framed as "create, compose, polish, and **perform** your music."
- The guide posits **two sequencers** in one DAW: the Arranger Timeline ("the fixed 'story' of a song") and the **Clip Launcher** ("allows you to freely improvise with your clips"; "the logical Arranger's artistic brother").
- Purpose of Launcher clips: "Arranger clips are played back precisely at the designated time. But Launcher clips must be available whenever you want them, either for section-based composition (verse, chorus, bridge), **or as pieces for a live performance**, or however else you might use them."
- Structure: **slots** on each track hold clips; a vertical column of clips is a **scene**, triggered together; **Stop Clips** button per track; **Global Stop Clips**; **Switch Playback to Arranger** per track and globally (restores the timeline as the active sequencer).
- Play menu performance settings: Automation Write, Overdub, Record as Comping Takes, **Record on scene launch** (a scene launch triggers recording into empty armed slots).
- Scenes can be named, colored, commented; the Project Panel has a **Sections tab** for scene management.
- The guide explicitly invokes performing electronic music "from the stage" as a design concern.

### Apple MainStage (User Guide 4.3) — evidence layer A

- Positioning: "The ultimate live rig. MainStage brings your music to the stage with a full-screen interface optimized for live performance, flexible hardware control, and a massive collection of plug-ins and sounds."
- Object model: **Concert** (top container) → **Sets** (folders of patches) → **Patches** (per-song sound configurations) → **Channel strips** (software instruments + effects + external instruments).
- Three working modes: **Layout mode** (design the on-screen control surface and assign hardware: knobs, buttons, foot pedals), **Edit mode** (build patches/channel strips), **Perform mode** (full-screen live surface).
- **Assignments and mappings**: hardware controls → screen controls → parameters; mappings can exist at patch, set, and concert levels; controller transforms; blocking/filtering of MIDI messages.
- **Patch switching in performance** is a first-class documented workflow: via keyboard shortcuts, by typing, via actions, via MIDI **program change messages**; settings include *defer patch changes*, *instantly silence the previous patch*, program change/bank numbers per patch.
- Patch/set/concert levels each carry settings: tempo (with "change the tempo when you select a patch"), time signature, transposition, tuning, key ranges.
- **Layers and splits**: keyboard layers/splits with key ranges, floating split points, velocity ranges — the instrumentalist's rig semantics.
- Live input: connect microphones and electric instruments; amps/pedals (Amp Designer, Pedalboard, stompboxes), **feedback protection**, tuner, articulation switching.
- Tempo sources: **tap tempo, external MIDI clock, Ableton Link**; metronome; the MainStage clock.
- Concert-level machinery: overall volume, concert-wide effects, auxes, concert-level channel strips, mute audio output, silence MIDI notes.
- **Recording the audio output of a concert** and a Playback plug-in (backing tracks in performance) are documented as supporting capabilities — recording is secondary to performing.

### Cantabile (guides: states, set lists, index) — evidence layer A

- Tagline: "Software for Performing Musicians."
- Object model: **Songs** (files: routes, plugins, metronome, media players) and **Racks** (reusable containers of plugins slotted into songs); **States** = named snapshots of a song or rack configuration, recalled to switch configurations.
- States semantics: "The main purpose of states is to provide a fast mechanism for switching between the required sounds and settings for different songs or song parts." Rack states ≈ presets (one sound each); song states ≈ **"Song Parts"** (intro/verse/chorus). Song parts and rack states are "functionally identical."
- Switching mechanisms: clicking, keys (T / Shift+T for next/previous state), menu commands, and **Bindings** (generic MIDI/control-surface → action mapping).
- States control routes, plugin presets/parameters, metronome tempo/time signature, gain/mix; states *cannot* change which objects exist ("all states have the same set of plugins, routes").
- **Locked states** (explicit control over when state is saved; faster switching), **linked states** (verse 2 = clone of verse 1), **state behaviors** and exported settings (rack ↔ song interplay).
- **Set Lists**: "a saved list of song files that can be quickly switched between. You'll typically use a set list to pre-configure the a set of songs in the correct order for a gig." Entries carry optional **program numbers** loadable via Bindings; breaks organize the list; **pre-loading** all songs/racks to improve song-switch times (RAM trade-off documented); a full-screen **set list grid** for the stage.
- Performance-management surfaces: Live Mode, Show Notes, Ticker Bar (lyrics/prompt display), Set List Verification and Printing, **Preventing Prompts to Save** (avoiding interruptions mid-show).
- Stability posture documented as a concern: "Tuning for Reliable Glitch Free Performance," Performance Profiler, prevent-memory-paging options.
- Supporting: Media Players (backing tracks), Metronome, MIDI Clock Synchronization, Loopback Ports, Stream Deck integration.

### Gig Performer — no observations (source unreachable)

Named as a market member of the rig pole (cross-platform plugin host) but its documentation was not reachable; nothing below may cite it.

---

## Cross-product Comparison

| Dimension | Ableton Live | Bitwig Studio | MainStage | Cantabile |
|---|---|---|---|---|
| Working material | clips (audio/MIDI) with launch settings | clips in launcher slots | patches (channel strips of instruments/effects) | songs + racks with states |
| Unit of show order | scenes (rows of clips) | scenes (columns) | sets → patches | set list → songs → song parts (states) |
| Live act | launching clips/scenes, playing into them, mixing, FX | launching clips/scenes | selecting patches, playing instruments, switching with feet/hands | recalling states/songs, playing, switching |
| Authoring before show | building Sets in Session (and Arrangement) | building Launcher clips | building concert (Layout/Edit modes) | building songs/racks/states |
| Hardware control | MIDI/Key Map Mode, clip→key mapping | MIDI controllers chapter (guide §15) | Layout mode: hardware→screen control assignments, foot pedals | Bindings, Controller Bar |
| Live input processing | audio tracks w/ monitoring, FX | audio tracks w/ FX | core use case (mics, guitars, layers/splits, feedback protection) | routes/plugins process live input |
| Tempo/sync | on-the-fly tempo, Tempo Follower, Link | transport, scene launch | tap tempo, MIDI clock, Link | MIDI clock sync, metronome |
| Deliverable | the show; recording/export secondary (production role) | the show; record-to-Arranger for later | the show; concert output recording documented as support | the show; recording is a feature, not the purpose |
| Stability posture | CPU meter, resource settings documented | — (guide tone) | full-screen Perform mode | Live Mode, no-prompts, glitch-free tuning guides |

Observed commonalities (evidence layer B, cross-product):

1. Material is **prepared in the software before the show** in all four products (clips built/curated; patches constructed; songs/states configured).
2. The show is executed by **recalling/launching/switching prepared configurations in real time**, plus playing input into the software.
3. The show is organized as an **ordered, named sequence of configurations** (scenes / sets+patches / set lists+song parts) the performer steps through or jumps across.
4. **Hardware control attachment** (MIDI mapping / assignments / bindings) is universal in the sample — in the rig pole it is the documented primary interaction (footswitch patch switching); in the clip pole it liberates from the mouse.
5. **Live input processing** (instruments/mics through software FX/instruments) is present in all four; central in the rig pole, optional in the clip pole.
6. **Tempo/clock handling** exists everywhere (tap/clock-sync/Link), with per-song/per-scene/per-patch tempo changes documented in both poles.
7. **Recording the show** is a supported secondary capability in every product — never the stated purpose.
8. **Stage-support surfaces** (full-screen perform mode, show notes/lyrics, tuner, metronome/click) appear across poles.

Product-pole differences (kept out of the definition):

- The clip pole's material is **time-bearing** (loops/patterns that play) and the live act is *launching/combining*; the rig pole's material is **configuration-bearing** (sounds/recall states) and the live act is *playing/recalling*.
- The clip pole ships inside dual-role DAWs (Session/Arranger duality is explicit in both products' guides); the rig pole ships as dedicated hosts.
- Rig pole documents foot-pedal switching, patch-defer/silence semantics, key-range splits/layers; clip pole documents launch quantization, follow actions, crossfader transitions.

## L0 — Defining Invariant

**Live Music Performance Software** = software whose defining core is three jointly-held structures:

1. **The prepared performance material** — musical material (sounds, instruments, clips, patterns, patches, song configurations) that the performer authors or curates *in the software before the show*. This is the working-material discriminator: the performer's own material, not finished recorded tracks made by others.
   *Remove → the performer mixes ready-made recordings → DJ Software.*
2. **Real-time performance execution** — during the show, the performer triggers/launches/recalls the material and plays/controls it in response to live musical decisions; the software combines the material (and live input) into one continuous program output.
   *Remove → the material plays itself with no live execution → a playlist player / jukebox; or the work becomes editing rather than performing.*
3. **The show as the deliverable** — the output is the live performance itself; no persistent edited document is produced as the goal. Recording the show, where offered, is a byproduct.
   *Remove → the goal becomes a recorded/edited document → DAW production (Arrangement timeline becomes the center of gravity).*

Jointly-held is load-bearing:
- 2+3 without 1 = DJ Software (mixing finished recordings)
- 1+2 without 3 = DAW production with a session/launcher surface
- 1+3 without 2 = an automated playback device, not performance software

## L1 — Common Mature Structure

Very common in mature products, not definitional:

- **Hardware control attachment** — MIDI learn / controller assignments / bindings mapping knobs, pads, buttons, footswitches to launches and parameters. Universal in the sample; in the rig pole it is documented as the primary performance interaction (footswitch patch changes), in the clip pole as liberation from the mouse. Screen-only performance is possible in the clip pole, so mapping stays common-mature rather than definitional.
- **Show-order organization** — named, ordered containers for the show (scenes, sets, set lists), often with per-container tempo/time-signature and program-number addressing.
- **Live input processing** — instruments/microphones played through the software's instruments and effects; keyboard layers/splits and velocity/key ranges in the rig pole.
- **Tempo & clock machinery** — tap tempo, external MIDI clock sync, peer-to-peer link sync, per-section tempo changes.
- **Effects & mixing toward the program output** — per-material FX, master/concert-level processing, level control.
- **Recording/capturing the performance** — documented in all four sampled products as a secondary capability.
- **Backing-track/media playback** — Playback plug-in (MainStage), Media Players (Cantabile), clips-as-stems (clip pole).
- **Stage-support surfaces** — full-screen perform mode, metronome/click, tuner, show notes / lyric display.

## L2 — Variant / Optional Structure

- **Product class**: dual-role DAWs with launchers (production + performance in one product) vs dedicated live rig hosts (no timeline authoring) vs standalone/performance-edition packaging.
- **Performance style**: electronic clip-launching sets; instrumentalist rigs (keyboard/guitar/vocal processing); live looping (record→layer→overdub loops live; a Loopback plug-in and session-looping workflows are documented in the sample); playback rigs (prepared stems/click for touring acts — the material is still self-prepared, so the core holds).
- **Identity of the performer's seat**: producer-performer (authors and performs the same material) vs performing musician (plays an instrument into patches prepared by/for them).
- **Deployment**: Mac-only vs cross-platform; host-of-plugins vs self-contained device set; companion hardware surfaces.
- **Automation of the show**: follow actions / auto-advance (optional; the performer can hand over sequencing to the software without becoming a DJ product).
- **Niche drift pole**: live-coding environments perform by authoring code *during* the show, collapsing the prepared-before/during split — best treated as an adjacent practice, not part of this Type's definition (not directly researched this pass; recorded as uncertainty).

## L3 — Vendor-specific Structure (Research Notes only)

- Ableton: Session/Arrangement duality over shared tracks; Live Set/Project file model; Back to Arrangement button semantics; launch quantization; follow actions; Tempo Follower; Ableton Link (also licensed into others); Push/Move hardware.
- Bitwig: Launcher as a panel loadable inside other panels; per-track "Switch Playback to Arranger"; Sections tab; record-on-scene-launch; The Grid modular devices.
- MainStage: Concert/Set/Patch/channel-strip hierarchy; Layout mode with screen controls and hardware assignment; defer patch changes; instantly-silence-previous-patch; program-change patch addressing; feedback protection; concert-level auxes; Apple Creator Studio subscription tie-in.
- Cantabile: Song/Rack/State/Binding vocabulary; song parts vs rack states duality; linked/locked states; exported settings; set-list pre-loading; Ticker Bar; prevent-prompts-to-save; Stream Deck plugin; "rebranding" white-label option.

## Rejected Findings (considered and not promoted)

- "Hardware control mapping is definitional" — rejected: screen-only operation is a real clip-pole posture; kept at L1 with the rig-pole nuance documented.
- "Scenes/clips grid is the Type's defining structure" — rejected: the entire rig pole (MainStage, Cantabile) has no clip grid; the grid is a pole implementation of real-time recall.
- "Set lists/song order is definitional" — rejected: free-improvisation launching (explicit in both clip products' guides) satisfies the Type without a pre-ordered list; show order is a common organizer, not the invariant.
- "Sync/tempo machinery is definitional" — rejected: a solo instrumentalist rig at fixed tempo satisfies the core without any sync feature.
- "Backing-track playback makes it a playback utility" — rejected: playback of *self-prepared* material alongside live execution is a variant of the core, not a separate Type; the boundary would only move if the material were finished recordings owned by others (→ DJ Software / player).

## Boundary Findings

### vs DJ Software (§04.12 sibling) — joint review DISCHARGED from this side

The dj-software pass (2026-09-07) held the seam: DJ = "library of finished recorded tracks… the working material pre-exists and the user does not author the music"; this pass confirms the complementary side from direct observation of both poles — the performance material here is self-authored/curated (clips built in the software; patches constructed; song states configured), even when the material contains audio sampled from recordings. The two Types also differ in the live act (blending/transitioning between tracks vs triggering/playing/recalling self-prepared configurations).

**Keep-both RATIFIED** with the working-material seam as the discriminator. Blur acknowledged in both directions and held as variant-level: DJ products ship loopers/samplers; clip-launch products ship crossfaders and DJ-style transitions (documented verbatim in the Ableton manual). Removal test: remove self-authored material → the product is DJ Software; remove finished-track mixing → it remains this Type.

**Sub-decision recorded per the dj-software pass's request**: Auto DJ/Automix surfaces and the hardware-ecosystem export posture (prepare library on computer, perform from standalone club players via USB/cloud) are automation/workflow variants *of DJ mixing over finished tracks* — they involve no self-authored performance material. Recommendation: document them inside DJ Software as variants, not as separately named Types. No product population was found that would justify a third Type.

### vs Digital Audio Workstation (§04.09)

The deliverable seam held by the DAW pass ("the finished mix leaves as audio") is the same seam from the other side: here the deliverable is the show itself, and no edited document is the goal. Two of the four sampled products are **dual-Role products**: the same Ableton Live or Bitwig Studio installation is a DAW when the Arrangement/render workflow is the center of gravity and this Type when the launcher/performance workflow is. The center-of-gravity framing follows the beat-making/DAW precedent (STATUS 2026-09-07). Both Types stand; the documents cross-reference the seam. Music Production Application (§04.10 umbrella) inherits the same alias risk already flagged by the DAW pass — recorded, not resolved here.

### vs Worship Presentation Software (§25 sibling family)

Visually adjacent ("performed live, in front of an audience") but the object class differs: lyric/slide/media presentation vs music production in real time. A worship band's MainStage rig is this Type; the lyric projection system is the other Type. No overlap in core model.

### vs Audio Editor (§04.09)

Different object entirely (existing recordings edited into files). No seam confusion observed.

### vs consumer backing-track/lyric display apps

Set-list/lyric display without real-time music assembly lacks L0 legs 2–3 as defined here (no self-authored material being executed); these are stage-support utilities, not this Type.

## Historical / Market-Sample Check (§24)

- **Pre-software era**: a 1980s/90s keyboard player's MIDI rig — rack synthesizers with program-change-switched patches (foot controller) plus a hardware sequencer/sampler triggering self-programmed sequences — maps 1:1 onto the three legs: self-authored material (sequences/patches), real-time recall/playing, show-as-deliverable. Similarly, a live electronic act triggering prepared material from hardware samplers fits. **Passes** — no clip grid, scenes, set-list files, touchscreens, or cloud in the core.
- **Regional/smaller-market practice**: the rig pole's semantics (songs, parts, footswitch patch changes, set lists) are exactly the working musician's practice in regional gigging scenes; nothing in the core assumes a specific genre, market, or venue scale.
- **Era check against the sample**: the definition does not depend on DAW dual-role (MainStage/Cantabile are dedicated), on any sync technology, or on hardware surfaces.

## Uncertainties

1. **Gig Performer and the third-party rig market**: official docs unreachable; the rig-pole sample is two products (one major-vendor, one one-person-company). A wiring-paradigm rig product might contribute a third rig philosophy (explicit signal-graph editing) that could stress the L1 list (not the L0). Assertion strength kept calibrated accordingly.
2. **Live-coding environments**: adjacent practice identified but not researched from sources this pass; treated as a drift pole in Research Notes only.
3. **FL Studio Performance Mode**: known market member of the clip pole; not fetched (sample sufficient per stop conditions). No claims about it.
4. **Mobile/standalone performance surfaces** (tablet editions, standalone hardware running the same software): the Bitwig guide has a tablet chapter and Ableton ships standalone hardware, but this pass did not verify how deployment variants affect the core — expected to hold, recorded as uncertainty.
5. **Market size/positioning of the rig pole** beyond the two sampled vendors was not measured; the "pole, not one vendor" claim rests on two independent vendors + the known existence of others (unverified).

## Final Synthesis

Live Music Performance Software is the performer's seat: software operated during a live show to execute music in real time from material the performer prepared in the software beforehand. Its canonical core is the trio **prepared self-authored material + real-time execution/recall during the show + the show itself as the deliverable**. Everything else commonly shipped — controller mapping, scenes/set lists, live input processing, sync, recording, stage surfaces — is standard capability, not definition. The Type is bounded on one side by DJ Software (working material = finished recordings) and on the other by the DAW (deliverable = a recorded document); dual-role products straddle deliberately and are documented as such.
