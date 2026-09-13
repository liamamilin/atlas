# Live Music Performance Software

## Overview

A **Live Music Performance Software** is a performance application that a musician operates **during a live show** to execute music in real time from material the musician prepared in the software beforehand.

Its defining core is a trio of properties:

```text
Material the performer authors/curates in the software before the show
└── Real-time execution during the show
    │   (triggering, recalling, playing, mixing the material live)
    └── The show itself is the deliverable
        (no edited document is produced as the goal)
```

Each property is load-bearing. Remove the first and the software is mixing ready-made recordings — a DJ product. Remove the second and the material simply plays itself — a player, not a performance instrument. Remove the third and the work becomes production — a DAW whose goal is a recorded output. What remains when all three hold is the performer's seat: the software is the instrument, the rig, and the set-list holder at the same time.

The category has two recognizably different product shapes — **clip-launching environments** (the material is loops, patterns and sequences triggered from a grid) and **live-rig environments** (the material is sounds and song configurations recalled per song) — but both realize the same core.

## Users & Context

The primary user is a **performer who is also (or works with) the person who prepared the material**:

- an electronic producer-performer who performs their own tracks and patterns live by launching and combining them
- a keyboard player, guitarist, or vocalist who plays an instrument or sings *through* the software — sounds, effects and song configurations prepared as patches and recalled per song
- a band member operating prepared stems, click tracks and sounds behind a live act

Secondary users exist around the edges: a bandmate or technician may trigger scenes from a controller for a touring act, and a studio-side collaborator may help prepare material. The defining context, though, is the stage: the person at the software is mid-performance, reacting to the room, the band, and the song as it happens — not editing a timeline.

Preparation happens elsewhere — at a desk, in rehearsal, often in the same product or in a production tool — and is aimed at making the live surface predictable: every launch, recall and switch maps to something the performer can hit without looking.

## Core Model

### The Defining Core

**Prepared performance material.** The software holds musical material the performer authors or curates in advance: sounds, instruments, effects chains, audio loops and samples, patterns and sequences, and configurations that bundle these into per-song or per-section settings. The material is the performer's own working material — even when it samples recordings, it has been prepared, edited and arranged for this show. This is the clearest line against DJ software, where the working material is finished recordings made by others.

**Real-time execution.** During the show the performer triggers, launches, recalls and plays the material in response to live decisions, and plays input into it (keys, pads, guitar, voice). The software combines the triggered material and the live input — mixing levels, applying effects, handling tempo — into one continuous program output. The performer is executing the show; nothing is being rendered or edited toward a file.

**The show as the deliverable.** The output of the software is the performance itself. Recording the show, where supported, is a byproduct for later reference — never the stated goal, and nothing in the workflow depends on producing a document. This is the line against production DAWs, whose endpoint is a rendered mix or stems.

### Standard Capabilities

Mature products across both shapes carry most of the following. They make the core practical; they do not define the Type.

- **Hardware control attachment** — knobs, pads, buttons, keyboards and footswitches mapped to launches, recalls and parameters. In live-rig products this is the documented primary interaction (footswitch patch switching); in grid-style products it liberates the performer from the mouse.
- **Show-order organization** — named, ordered containers for the show: scenes that group simultaneous material, sets of patches, set lists of songs, and named song parts (intro / verse / chorus). Tempo and time-signature changes can typically be attached to these containers.
- **Live input processing** — instruments and microphones played through the software's instruments and effects; keyboard layers and splits with key and velocity ranges; amp and pedal processing for guitars; feedback protection.
- **Tempo and clock handling** — on-the-fly tempo change, tap tempo, synchronization to external MIDI clock, and peer-to-peer tempo sharing between linked applications.
- **Effects and output mixing** — per-material effects, send/return processing, master/concert-level processing and level control toward the front of house.
- **Recording and capture** — capturing the show's output or improvisations into a document for later use; always a secondary capability.
- **Backing-track and media playback** — prepared stems, click tracks and media files played back under the performer's control alongside the live execution.
- **Stage-support surfaces** — a full-screen performance mode with large, readable controls; metronome/click; tuners; show notes and lyric display; suppression of save prompts and other interruptions.

### One Structure, Many Implementations

The core is written conceptually; the two product shapes implement each concept differently:

```text
Concept:            Prepared performance material
Grid-style shape:   clips (audio loops / MIDI patterns) with launch settings
Live-rig shape:     patches — channel strips of instruments and effects;
                    songs and racks with named recall states

Concept:            Real-time recall of the material
Grid-style shape:   play buttons on a grid; scenes trigger rows together
Live-rig shape:     patch/song/state selection from a list or grid,
                    via screen, keys or MIDI program changes

Concept:            Show order
Grid-style shape:   scenes ordered top-to-bottom, jumped across freely
Live-rig shape:     set lists and sets ordering songs and patches
```

A reader who has only seen one shape should be able to recognize the other from the core.

## How It Works

### Prepare (before the show)

```text
Build or curate the material
  (record/import audio, program patterns, design sounds and effects chains,
   bundle them into per-song or per-section configurations)
→ organize the show order
  (scenes, sets, set lists, song parts; attach tempo/time changes)
→ attach hardware
  (map pads/keys/pedals to launches, recalls and parameters)
→ rehearse and save the performance state
  (some products pre-load everything so switching is instant on stage)
```

Preparation is the majority of the work. The live surface is the product's promise: what was built here must be triggerable there, by hand or foot, without a mouse and without delay.

### Perform — grid-launching shape (during the show)

```text
Open the performance surface (a grid of clip slots across tracks)
→ launch a clip or a whole scene (a row of clips starts together,
   usually snapped to the musical grid)
→ layer, stop, and re-trigger material across tracks as the song evolves
→ play input into the running material (keys, pads, FX control)
→ step through scenes — or jump freely when improvising
```

The material is time-bearing: loops and patterns play when launched and stop when replaced. The performer mixes the launched material with live input and controls, shaping arrangement and dynamics in real time.

### Perform — live-rig shape (during the show)

```text
Open the full-screen performance surface
→ recall the current song's patch or state (sounds, splits, effects load)
→ play the instrument or sing through it
→ between songs (or inside them), switch to the next patch/song part
  (via screen, keyboard command, or a footswitch sending a program change)
→ the previous sound is silenced or faded as the next takes over
```

The material is configuration-bearing: recalling a patch changes what the performer's playing sounds like, and the live act is playing through it. Tempo can change when a song is selected, either preset or tapped.

### Both shapes end where they began

At the end of the show nothing needs exporting. If the product captured the performance, the capture is reference material; the document the performer walks away with is the *next* show's prepared state.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- prepared, self-authored performance material held in the software
- real-time triggering/recall/playing of that material during the show
- the show itself as the deliverable

**Common mature structure** — present in most current products:

- hardware control mapping
- show-order containers (scenes / sets / set lists / song parts)
- live input processing (including layers/splits, amp/pedal processing)
- tempo/clock handling with per-section changes
- effects and output mixing
- recording/capture as a secondary capability
- backing-track/media playback
- stage-support surfaces (full-screen mode, click, tuner, notes)

**Common variants / optional** — depends on product class and performance style:

- dual-role packaging: the same product also being a full production DAW
- dedicated rig packaging: no timeline authoring at all
- live looping (capturing and layering loops live as a performance style)
- playback-rig use (prepared stems/click behind a touring act)
- follow-action/auto-advance automation of scene progression
- deployment breadth: single-platform vs cross-platform, desktop vs companion/standalone hardware

## Interfaces

### The performance surface

The surface the performer faces on stage.

- Grid-launching shape: a grid of clip slots arranged in tracks and scenes, each slot a large play button; scene triggers; stop controls per track and globally; transport, tempo, and a crossfader-style transition control in some products.
- Live-rig shape: a full-screen control panel of large screen controls (knobs, buttons, meters) mirroring the performer's hardware; the current patch/song name; patch/song selectors.
- Purpose: launch, recall, switch, and control — readable at arm's length, operable without fine mouse work.

### The preparation / editing surfaces

Where the material is built and the show organized.

- Grid-launching shape: clip editors (pattern and audio editing), device/effects views, mixing views, and the timeline view of the same tracks (in dual-role products the timeline is the production half).
- Live-rig shape: patch editors (channel strips, plugin slots, routing), layer/split editors, and mode switches between designing, editing, and performing.
- Purpose: make the material and the show order; primary actions are building, naming, ordering, and mapping.

### The show-order surface

The scene list, set list, or song list: ordered, named entries, typically with tempo/time-signature attachments, notes, and — in rig products — program numbers so hardware can address them. Primary actions: reorder, jump to an entry, organize into groups (sets, breaks).

### The hardware-attachment surface

The mapping view where physical controls are assigned: select a control, move a knob or press a pedal, and the assignment binds. In rig products this extends to designing the on-screen control layout itself and transforming/filtering incoming MIDI.

### Stage-support surfaces

Click/metronome controls, tuner, show notes or lyric displays, and settings that keep the machine quiet and stable mid-show (suppressing save prompts, pre-loading songs, audio-buffer and performance tuning).

## Important Rules / Behaviors

### The show must not stop

Performance software is built around the assumption that the output cannot interrupt itself. This shapes real behavior in the sampled rig products: features like defer-on-switch (finish the current sound before changing), instant silencing of the previous patch, pre-loading of songs so switching is instant, and suppression of save prompts mid-show — the exact combination varies by product. Stability and latency tuning is a documented concern in the category, not an implementation detail.

### Triggers align to the music

In grid-launching products, launches and recordings are commonly quantized to the musical grid so that a late button-press still lands in time. Tempo changes can be attached to scenes, songs or patches, so recalling a section moves the whole machine to that section's tempo.

### One material-holder at a time (per channel)

Grid-style products typically allow one clip per track at a time; launching a new clip replaces the playing one on that track while others continue. Rig-style products recall whole configurations, replacing the active sound set. Both embody the same rule: the performer's action takes over the channel it is aimed at, instantly.

### Material changes are performance choices

During the show, edits to material are live musical decisions (layering, muting, swapping), not document revisions; some products can log the improvisation back into an editable document afterwards, but that is capture, not the goal.

### The working material is the performer's own

The software performs material prepared in it — even audio sampled from recordings has been edited, looped and arranged by the performer for this show. This is the rule that keeps the Type distinct from mixing finished recordings.

### Recording is a byproduct

Capturing the show is supported (documented across the sampled products) but sits outside the performing loop: nothing about the live workflow depends on it.

## Variants

- **Dual-role production + performance environments** — a full production DAW whose launcher view is the live half (the sampled clip-pole products all have this shape). Same installation, two centers of gravity.
- **Dedicated live-rig hosts** — no timeline authoring; the whole product is the stage rig (both sampled rig products). Typically cheaper, single-purpose, and built around patch recall.
- **Instrumentalist rigs** — keyboard players, guitarists and vocalists playing through prepared sounds; layers/splits and footswitch patch changes are the daily workflow.
- **Electronic clip-launch sets** — producer-performers launching their own patterns, loops and stems; improvisation across scenes is the daily workflow.
- **Live looping** — capturing input into loops live and layering them as the performance itself; supported both as a dedicated capability (loop plugins) and as a launch-grid workflow.
- **Playback rigs** — prepared stems, click and cues played from the software behind a live band; still self-prepared material executed in real time, so the core holds.
- **Niche adjacent practice** — live-coding environments perform by writing the music-generating code during the show itself, inverting the prepared-before/during split; treated here as an adjacent practice rather than a variant of the Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| DJ Software | same Family, opposite working material: DJ software mixes **finished recorded tracks** the user does not author; this Type performs **material the user authors/prepares**. DJ products' loopers/samplers and this Type's DJ-style crossfaders blur the edge; the removal test separates them |
| Digital Audio Workstation | production is the center of gravity: the deliverable is a recorded, edited document rendered from a timeline; here the deliverable is the show. Dual-role products straddle deliberately — the same product is a DAW when arranging/rendering and this Type when performing |
| Music Production Application | umbrella packaging over production-oriented music tools; performance surfaces in them are capabilities, not the Type's seat |
| Audio Editor | edits existing recordings into files; no live execution, no show |
| Worship Presentation Software | also "performed live" in front of an audience, but its objects are lyrics/slides/media presentation, not music produced in real time |

The boundary against DJ Software is the most important one, because both are real-time music performance over a library of prepared audio-adjacent material. The structural difference is **who made the working material and in what**: a library of finished recordings (DJ) versus sounds, patterns and configurations authored for the show (this Type).

## Representative Products

- Ableton Live — clip-launch environment (Session View) inside a dual-role production product
- Bitwig Studio — clip-launch environment with an explicit "two sequencers" philosophy
- Apple MainStage — live-rig product for instrumentalists (concerts, sets, patches)
- Cantabile — live-rig product from an independent vendor (songs, racks, states, set lists)

Other products populate both shapes of this market (for example dedicated rig hosts in the Gig Performer mold, and performance modes inside major production DAWs). The model above was checked against both product shapes — the clip-launch pole and the patch-recall pole — rather than generalized from one of them.

## Sources

Research date: **2026-09-08**

- Ableton — *Live Reference Manual 12, "Live Concepts"* — https://www.ableton.com/en/manual/live-concepts/
- Bitwig — *Bitwig Studio User Guide, "The Clip Launcher"* — https://www.bitwig.com/userguide/latest/the_clip_launcher/
- Apple — *MainStage User Guide* — https://support.apple.com/guide/mainstage/welcome/mac
- Cantabile — *Guides: "Song and Rack States", "Set Lists"* — https://www.cantabilesoftware.com/guides/states , https://www.cantabilesoftware.com/guides/setLists

> Sourcing limitation: one intended fifth sample (a cross-platform rig host) had unreachable official documentation and was dropped rather than substituted from memory. Claims about the dedicated live-rig shape therefore rest on two directly documented products (one major-vendor, one independent); no numeric or default-value details are asserted anywhere in this document. Product-by-product observations and cross-product comparison are recorded in the paired Research Notes.
