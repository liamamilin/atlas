# Video Compositing Application

## Overview

A **Video Compositing Application** combines multiple live video sources into a single continuously-produced program picture, in real time and under the operator's control, and delivers that program concurrently to one or more outputs — a live stream, a recording, an external monitor or hardware output, or a virtual camera that other applications consume.

The defining structure is small:

```text
Video sources (cameras, captures, files, screens, calls, graphics)
└── The real-time mix
    │   (select and transition between sources · combine them in the frame:
    │    layering, positioning, split screens, overlays, keying)
    └── The program — one continuous composite, produced live
        └── Concurrent outputs (stream · recording · external output · virtual camera)
```

Two properties of this definition matter for recognizing the Type:

- **The composite is produced live.** The sources run, the operator directs them into one picture while everything moves, and the result is continuous. This is what separates the Type from offline compositing — the timeline-based layering inside video editors and the shot-by-shot work of visual-effects compositing — where the composite is rendered after the fact.
- **The deliverable is one running program sent to concurrent destinations.** The application does not publish a catalog or host an audience; it produces the feed that streaming platforms distribute and recordings preserve.

Everything else commonly associated with the category — streaming to multiple platforms, scene/preset systems, stinger transitions, remote guests, virtual sets, instant replay, control surfaces — is standard equipment of mature products but not part of the definition. The Type's direct ancestry is the hardware vision mixer with its keyers: sources in, an operator mixing and keying them into one program, program out. A software product that does the same thing is this Type, whether or not it streams anywhere.

## Users & Context

The primary user is a **live video operator**: someone responsible for what a running video program looks like at every moment.

Typical roles and contexts:

- **broadcast and streaming producers** — assembling multi-camera programs for television-style production and for live streams on external platforms
- **event and venue AV teams** — concerts, conferences, sports, church services: switching cameras, overlaying graphics and lyrics, feeding screens and streams
- **creators and podcasters** — producing shows from a webcam, a screen capture, remote guests, and branded overlays
- **marketers and communications teams** — browser-based studios for interviews, webinars, and company broadcasts, operated without specialist training

Secondary users include **title/graphic operators** (updating names, scores, and tickers while the program runs), **audio operators** (mixing the program's sound alongside the video mix), and **remote guests**, who appear inside the composite as sources they do not control.

The work environment is defined by the live condition: the program is on air (or being recorded) while it is being assembled. Operators work from a control surface — a keyboard, a hardware pad, a touch screen, or the application window itself — and the cost of a mistake is visible immediately. This is why the interface is organized around *preparing the next state* and *committing it to the program*, rather than around editing history.

## Core Model

### The Defining Core

**Sources.** The material of the Type is a set of simultaneously available video sources — the application's inputs. Recurring source kinds: cameras and capture cards; video files and playlists; screen and window capture; network streams; remote video calls and guests; still images; solid colors and bars; and graphics (titles, tickers, lower thirds). A source is live in the sense that it keeps producing frames while the show runs — a camera keeps filming, a file keeps playing, a guest keeps talking.

**The mix.** The application's central act is producing one picture from several sources, continuously, while the sources run. Two complementary operations make up the mix:

- **Selection and transition** — choosing which source (or saved composite) fills the program at a given moment, and moving between them with cuts, fades, wipes, zoom-style moves, or animated stinger transitions.
- **Combination within the frame** — placing sources on top of or beside each other in the same picture: layered positioning, split screens, picture-in-picture, overlay channels carrying graphics with transparency, and keying (chroma key, luma key) which extracts transparency from a source — a presenter in front of a green screen, a graphic with an alpha channel — so it can sit over another source.

The mix is operator-directed and real-time: the operator decides, moment by moment, what the program picture contains.

**Saved composites.** Because live operation leaves no time to build arrangements from scratch, mature products let the operator prepare named composites in advance — scenes, presets, layouts, branded show frames — and recall them with one action during the program. A saved composite is a snapshot of an arrangement: which sources appear, where they sit, which graphics are shown.

**The program.** The output of the mix is the program: a single, continuous, live-produced video. The program is the Type's central object — everything else exists to change what it contains from moment to moment.

**Concurrent outputs.** The program leaves the application simultaneously through one or more destinations: a live stream to an external platform, a recording, an output to a display or professional video card, or a virtual camera that makes the program look like a webcam to conferencing software. The same running composite feeds all of them.

**The audio mix.** A parallel mix runs alongside the video: each source's audio is levelled, filtered, and combined into the program's sound. Audio and video are mixed in the same application but controlled somewhat independently — a source can be heard and not seen, or seen and not heard.

### Standard Capabilities of Mature Products

These are widespread in current products and make the Type practical; they are not what makes a product a video compositing application:

- **Preview before program** — a private monitor where the next state (scene, source, overlay) is prepared and checked before being committed to the live program; in some products an explicit preview/program mode, in others a multiview of all sources for cueing.
- **Transitions library** — cut, fade, wipe, slide, zoom-class moves, and animated "stinger" transitions built from video files with alpha.
- **Per-source processing** — colour correction, crop, zoom and pan, deinterlacing, LUTs, applied to a source in real time before it enters the mix.
- **Keying** — chroma key (green/blue screen) and luma key, with virtual sets as a mature extension: keying a presenter over a generated 3D environment.
- **Graphics machinery** — title templates, lower thirds, scoreboards, tickers, countdowns; some products include a dedicated title editor, others accept graphics from external design tools over network video protocols.
- **Remote guest ingestion** — guests join from a browser or a meeting service and are composited into the program as sources, with their audio mixed into the show.
- **Recording for post-production** — recording the program, and in mature products recording sources *separately* (isolated tracks), so the live output can be re-edited later.
- **Multistreaming** — sending the program to several streaming platforms at once.
- **Network video I/O** — ingesting and outputting sources across a local network (NDI-class protocols) or over the internet (SRT-class), which is how graphics systems, other machines, and remote cameras join the mix.
- **Control surfaces** — hotkeys, MIDI/controller surfaces, stream-deck-class pads, web/touch remotes, and tally lights, because the operator's hands are busy while the show runs.
- **Monitoring** — multiviewers, audio meters, and in professional products waveform/vectorscope scopes.
- **Camera and playback control** — PTZ camera control, instant replay, and automated playlists in production-oriented products.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   saved composite
Realized:  scenes (scene-based products) · presets (production software) ·
           show layouts and brand kits (browser studios)

Concept:   combination within the frame
Realized:  layer/overlay channels · sources stacked inside a scene ·
           predefined layout templates

Concept:   program output
Realized:  streaming encoder · file recorder · hardware card output ·
           virtual camera · network video output

Concept:   graphics in the program
Realized:  built-in title editors · imported graphic sources ·
           network-fed graphics systems
```

A reader who has only seen one implementation — say, a browser studio with layout buttons — should still be able to recognize a professional multi-camera production switcher or an open-source streaming compositor as the same Application Type.

## How It Works

### Set up the production

```text
Create a production (a saved setup)
→ add sources: cameras, captures, files, calls, graphics
→ build saved composites (scenes / layouts) for the show's states
→ position sources, add overlays and keys, assign audio
→ configure outputs: stream destination(s), recording, external output
→ rehearse: check every composite in preview
```

There is no timeline to fill and nothing to render in advance. The setup produces *states* the operator will enter live, not a finished sequence.

### Run the live loop

```text
Take the show live (start streaming / recording / output)
→ select the next state; adjust it in preview
→ commit it to the program (transition / take / cut)
→ update what runs inside the current state
   (roll a video, change a title, move a guest on screen)
→ overlay and remove elements as the show demands
→ keep the program continuous throughout
```

This loop is the working heart of the Type. The program never stops while it is being changed; the operator's skill is making the changes invisible or deliberate.

### Deliver concurrently

```text
The single program picture feeds, at the same time:
→ the live stream (one or more platforms)
→ the recording (program; often also isolated source tracks)
→ the external output (screens, projectors, hardware)
→ the virtual camera (the program appears as a camera to other apps)
```

### Hand off to post-production

```text
Stop the show
→ recordings (program + isolated tracks) become editor material
→ the live production's output is re-cut, graded, republished offline
```

The Type's output is deliberately the *input* of the editing Types: live production first, offline refinement second.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Source / input grid

The inventory of everything that can appear in the program.

- lists all sources with thumbnails and live states
- primary actions: add a source, preview it, send it to the program, open its settings

### Saved-composite list (scenes / layouts / presets)

The show's prepared states.

- lists named composites, often grouped (e.g., by show segment)
- primary actions: create/edit a composite, recall it in preview, take it to program

### Preview and program monitors

The two pictures the operator watches.

- preview: the next state, freely adjustable with no consequence
- program: what is being delivered right now — the authoritative picture
- primary actions: adjust the preview state, commit it to program

### Transition and overlay controls

The commit mechanism and the in-frame combination controls.

- transition buttons (cut / fade / effects) and overlay channel toggles
- primary actions: execute a transition, show/hide an overlay, choose a transition style

### Source settings (position / key / colour)

Per-source composition controls.

- position, scale, crop, rotation; chroma/luma key controls; colour correction
- primary actions: place the source in the frame, key out a background, correct the image

### Audio mixer

The parallel sound mix.

- per-source faders and meters, mute/solo, filters, bus routing in mature products
- primary actions: balance levels, mute a source, apply a filter, route audio to outputs

### Output and stream settings

Where the program goes.

- stream destinations and quality, recording format and location, external output and virtual camera configuration
- primary actions: start/stop streaming, start/stop recording, enable outputs

### Control surface / multiview

The operator's remote hands and overview.

- hardware pads, MIDI surfaces, web/touch remotes mapped to show actions; multiview grids of all sources for cueing
- primary actions: trigger transitions and composites, cue sources, monitor everything at once

## Important Rules / Behaviors

### The program never stops

The defining behavioral constraint: the program is continuous while it is being changed. Everything about the interface exists to serve this — preview/program separation, one-action recall of prepared composites, transitions that smooth the change. An operator cannot "pause and think" on air; preparation happens before commitment.

### Combination requires transparency

A source can only sit *over* another source if it carries transparency — either natively (graphics with an alpha channel) or extracted by keying (chroma/luma). Keying quality depends on the source's shooting conditions; this is why green-screen practice is part of the Type's craft, and why keying controls are per-source settings rather than global switches.

### Audio is mixed, not attached

Sources bring audio, but the program's sound is its own mix: levels, filtering, and routing are decided per source and per output. Seeing and hearing are independently controllable — a common live-production necessity (e.g., a video playing silently under a voice-over).

### Outputs are independent of each other

Streaming, recording, and external output are separately started, stopped, and configured. A show can be recorded without streaming, streamed without recording, or both; isolated-track recording can run alongside the program output. The destinations consume the same program picture but are controlled as separate delivery decisions.

### Real-time performance is a structural budget

Every source, effect, key, and output consumes processing in real time. Products are explicit about this budget: hardware requirements, hardware-accelerated encoding, and small input-to-output latency figures are part of the professional conversation. The Type's feasibility — how many sources, at what resolution, with how many effects — is a performance question, not just a feature question.

### Live state is fragile and protected

Because the program cannot be undone on air, products protect the live state: undo of the *last* action, fault-tolerant recording, and the discipline of preparing changes in preview. Mistakes are managed by preparation and by quick reversal, not by re-editing.

## Variants

Common forms of the Type:

- **professional production software** — deep mixing/keying/replay/PTZ feature sets, hardware I/O, multi-destination output; operated by trained operators (e.g., broadcast, sports, large events)
- **open-source streaming compositors** — scene/source model, extensible through plugins and scripts; the creator/streamer standard
- **platform-native creator studios** — polished single-platform products (e.g., Mac-native) with switcher, scenes, guests, and branding for individual creators and podcasters
- **browser-based studios** — no installation; guests and operators join from a browser; branding and layouts over raw control; the non-technical tier
- **hardware-lineage systems** — the same structure realized as integrated hardware-software production switchers in fixed installations

A variant remains a variant while the defining core — live sources mixed in real time into one continuously-delivered program — is intact. Where the center of gravity shifts to *authoring* animated graphics, or to *sequencing recorded clips* on a timeline, or to *hosting the audience*, a different Application Type begins.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Visual Effects Compositing Application | sibling | offline, shot-based compositing in a film/TV pipeline (node graphs, roto/tracking/cleanup, rendered shots); here the composite is produced live as a continuous program |
| Motion Graphics Application | sibling | authors animated graphic material and delivers rendered moving images; here graphics appear as elements *inside* the live program, composited with everything else |
| Video Editor / NLE | adjacent | sequences recorded clips on a timeline and renders a finished file; here sources run and the program is assembled live; the compositor's recordings are the editor's material |
| Video Streaming Platform | downstream | the distribution venue (audience, catalog, player); this Type produces the feed the platform distributes |
| Social Live Streaming Platform | downstream | the creator-broadcast economy on a platform (audience, chat, monetization); this Type is the production layer beneath it |
| Video Calling / Conferencing Application | source-side | mediates conversation between participants; here calls are ingested as sources/guests of the program |
| Broadcast Management System | adjacent | station-wide scheduling, traffic, and automation across a broadcast day; this Type produces one program at a time |
| AI Video Generator | adjacent | generates footage from prompts; here existing running sources are combined — no generative authoring in the core |

The boundary with **Visual Effects Compositing** is the most important one, because both are "compositing" and share primitives (keying, layering, alpha). The structural difference is the operating mode and the job: this Type produces a continuous program in real time for live delivery; VFX compositing produces finished shots offline within a production pipeline. The boundary with **Video Editor** is the temporal one: timeline sequencing of recorded material vs live mixing of running material.

## Representative Products

- **vMix** — commercial Windows live production software; the fullest documented feature set of the Type (mixing effects, layers and overlays, keying, virtual sets, replay, multi-destination output)
- **OBS Studio** — free open-source scene/source compositor for recording and streaming; the creator standard and the extensible pole
- **Ecamm Live** — Mac-native studio with camera switcher, saved scenes, green screen, guests, and isolated-track recording; the platform-native creator pole
- **StreamYard** — browser-based studio with branding, layouts, guests, and multistreaming; the non-technical SaaS pole

The defining core was checked against the Type's hardware ancestry (broadcast vision mixers/switchers with keyers) to avoid over-fitting the definition to the current streaming era. Nuke-class offline compositors and timeline editors were examined as boundary anchors, not representatives: they realize compositing *offline*, which places them in the neighboring Types.

## Sources

Research date: **2026-09-09**

Primary vendor surfaces:

- vMix — homepage, features page, and User Guide (Introduction and Features): https://www.vmix.com/ , https://www.vmix.com/software/features.aspx , https://www.vmix.com/help/
- OBS Studio — homepage and Knowledge Base (Quick Start Guide): https://obsproject.com/ , https://obsproject.com/kb , https://obsproject.com/kb/quick-start-guide
- Ecamm Live — product page: https://www.ecamm.com/mac/ecammlive/
- StreamYard — homepage: https://streamyard.com/

Boundary anchors:

- Nuke Family (Foundry) — product page (offline VFX compositing pole): https://www.foundry.com/products/nuke-family
- VSDC Free Video Editor — product page (offline editor with compositing capabilities): https://www.videosoftdev.com/free-video-editor

> Sourcing limitations: Wirecast (Telestream) and HitFilm (FXhome) documentation was unreachable from the research environment (repeated request failures) and no claims are made about them. Ecamm Live and StreamYard evidence is product-page level rather than help-center level, so their operational specifics are stated only in general terms. Precise vendor figures (overlay-channel counts, input limits, latency figures, edition gating) are recorded in the paired Research Notes and deliberately not asserted as Type-level facts.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis (including the joint-review record for the sibling compositing Types) are in the paired Research Notes.
