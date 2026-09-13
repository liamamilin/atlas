# Previsualization Application

## Overview

A **Previsualization Application** is the shot-planning tool of film, television, animation, and commercial production. It lets a filmmaking team build a rough, watchable model of a scene before that scene is ever produced: the scene is staged in a representational space (drawn panels, a floor plan, or a three-dimensional set), broken into an ordered sequence of shots, each shot fixing a planned camera view; the sequence then plays back as a timed rough animation — an *animatic* — and the plan leaves the application as the documents the shoot and the edit consume: storyboards, shot lists, camera setup data, and edit-ready animatic sequences.

The defining core is small:

```text
Scene-to-be
└── ordered, revisable sequence of SHOTS
    └── each shot = a planned camera view of a STAGED scene
        └── staged in a representational space (panels / floor plan / 3D set)
            └── played back as a TIMED ROUGH ANIMATIC
                └── exported as PRODUCTION ARTIFACTS
                    (boards · shot lists · camera data · edit sequences)
```

What the application holds is a *plan*, not a product: nothing in it is finished footage, and its visual roughness is deliberate. When the center of the work shifts to producing the final moving image itself, the work has moved into other application types (animation, editing).

## Users & Context

The primary users are the people responsible for what the camera will do:

- **directors** — block the scene (where actors and cameras go), decide coverage (which shots will cover the action), and test pacing by watching the animatic
- **cinematographers / camera operators** — define camera positions, heights, framing, and commonly lens/format choices; some products extend into lighting placement
- **previs artists** — on larger productions, specialists who build the staged scenes and shot sequences for the director
- **storyboard artists** — in board-first workflows, draw the panels that carry the plan

Secondary consumers rather than operators: production staff, cast, and crews who receive printed or shared boards and shot lists; editors who receive the animatic sequence as a cutting reference. Educators and film students are a significant audience — several products are used in film programs precisely because they force students to plan coverage before shooting.

The working context is **pre-production** ("fix it in prep", as the market puts it): the tool is used from the first breakdown of the script through location scouts, blocking rehearsals, and pitch meetings, and its output continues to be consulted on set. Some teams also keep using it during the edit, when animatic timing is conformed against the real cut.

## Core Model

### The objects

**Scene / sequence.** The top-level container of planning is the scene — a contiguous unit of the story defined (directly or indirectly) by the script. Groups of scenes may be gathered into sequences. Scenes can be duplicated, reordered, and renumbered as the plan changes.

**Shot.** The central object. A shot is one planned camera view: a framing of a moment, with a duration in the sequence, and — depending on the product — camera data (position, height, angle, lens/format, movement) and a descriptive caption. Shots are created, inserted between existing shots, reordered, replaced, and deleted; the sequence of shots *is* the plan. Shots are typically numbered according to scene/shot conventions that survive into the exported shot lists and boards.

**Staging space.** The scene's content lives in a representational environment where the user places the things the camera will see:

```text
Concept:            Staging space
Realizations:       drawn panels with a camera frame
                    2D floor plan with camera/actor symbols
                    3D set with posed actors, props, walls, lights
```

The substrate is a product philosophy, not a definition. Board-first products stage scenes as drawn panels (with an optional 3D layer for depth and camera moves); blocking-first products stage them as overhead floor plans with movable camera and character symbols; previz-first products stage them as navigable 3D sets with mannequin actors, prop libraries, and lights. In every realization, the user is positioning subjects and defining where the camera stands — the fidelity stays symbolic.

**Camera viewpoint.** Each shot fixes a view of the staged scene. Minimally this is a framed image with the project's aspect ratio; mature products add camera realism — film/sensor formats, lens character, depth of field, camera supports and movement rigs — so that what the plan shows is achievable with real equipment. A recurring signature: some products pair the staging with a *viewfinder* function that records the exact lens/format a shot was composed for, turning the plan into equipment guidance.

**Animatic (timed playback).** The shot sequence carries durations and can be played back as a moving picture. Depending on the product, playback includes movement *within* shots (animated cameras, moving characters, tweened objects), transitions between shots, and sound (temp dialogue, effects). This is the evaluation surface of the whole type: a blocking diagram or a stack of boards becomes decidable only when the team can watch the scene play.

**Planning artifacts.** The plan exists to leave the application. Exports fall into four families:

- **boards / storyboards** — the shots as printed or digital framed images (PDF, images, HTML)
- **shot lists and camera data** — per-shot tables of framing, lens, movement, and notes (documents, spreadsheets, auto-generated pages)
- **overhead plans** — the blocking diagram itself, for the crew
- **edit-ready sequences** — the animatic as a movie file or as an interchange sequence (EDL/AAF/XML-class formats) that places every shot, in order and in timing, into the editor's timeline

### What is definitional — and what is not

Four properties together make the type; remove any one and the product stops being a previsualization application:

1. the **shot sequence as the plan of record** (remove → a shot-list spreadsheet, no visualization);
2. a **staged, representational scene** the shots look at (remove → documents with nothing to look at);
3. **timed rough playback** — the animatic (remove → a static board/layout tool, which is the neighboring storyboard type's territory);
4. **production-facing artifacts** out of the plan (remove → a creative 3D or diagram toy with no production loop).

Everything else is layered on top. Camera realism, motion machinery, sound, script import, lighting tools, libraries, team sharing, and print/export polish are standard capabilities that mature products carry in varying combinations — a floor-plan product can ship without 3D or sound and still be fully this type, just as a board product can ship without lens catalogs.

## How It Works

### 1. From script to scenes

The plan usually begins with story material: scenes are created manually, or a screenplay import generates a scene/shot outline (some products read screenplay formats and auto-create the storyboard skeleton with slug lines and cast; others simply rely on the user's script and captions). Board-first workflows often start even rougher — thumbnail sketches that are later promoted into formal panels.

### 2. Stage the scene

The user builds or selects the environment — draws the location, assembles a floor plan from a prop/furniture library, or constructs a 3D set from walls, props, and posed characters — and places lights where the type supports it. Sets and layouts are commonly saved and reused across scenes. Some products additionally support capturing the real world into the staging space (for example, importing a scan of a real location or composing against a live camera view), so the plan is anchored to a place that actually exists.

### 3. Define the shots

The user works shot by shot: position a camera (on the plan, in the set, or by framing a panel), adjust height, angle, framing, and — where supported — lens/format and movement; pose actors; then *commit* the shot into the sequence. In blocking-style products the camera diagram and the shot list are two views of one model: editing either one updates the other, and moving a character can drag the cameras that watch it. In previz-style products, committing a shot captures the staged state so the shot can be reloaded later exactly as it was.

### 4. Sequence, time, and make it move

Shots are ordered into the scene, durations are set (sometimes by literally tapping along a performance), and movement is added: animated camera moves that stay within a panel or sweep across a scene, tweened motion of characters and props on the set or the plan, transitions between shots, and a temp sound track. The result is the animatic — the scene, watched.

### 5. Watch, judge, revise

The core interaction loop is playback-driven: watch the animatic, find what does not work (coverage missing, pacing slack, an impossible camera position), and revise the staging, the shots, or the timing. Revision behaviors matter here: staged scenes change while already-captured shots exist, so products provide discipline — some keep each shot as an immutable record that must be deliberately re-taken, with tools to propagate later set changes into older shots; others keep diagram and shot list continuously synchronized so nothing drifts out of date. Snapshot/restore features let teams fork experiments without losing the plan.

### 6. Ship the plan

The finished plan is exported for the people who will execute it: boards and overhead diagrams printed or shared for the crew, shot lists and camera data for the camera team, the animatic movie for screenings and pitches, and — in the deepest integration — an edit-ready sequence that carries every shot, its order, its duration, and its camera motion into the editing application, in some products with changes flowing back so storyboard timing and the actual cut can be reconciled.

## Interfaces

The surfaces below appear under different names per product; layouts vary.

### Staging surface

The working canvas of the scene — a drawing canvas (board-first), a floor-plan editor (blocking-first), or a 3D scene editor with object placement, posing, and lighting (previz-first).

- Typical information: environment, actors, props, lights, cameras
- Primary actions: place/move/pose subjects and props, add lights, position cameras, navigate the space

### Overhead / plan view

A top-down view of the staged scene (floor plan, blueprint).

- Typical information: room geometry, actor and camera positions, movement arrows
- Primary actions: block the scene, place/reposition cameras, read coverage at a glance

### Shot sequence strip

The ordered list of shots as frames — a storyboard grid, a filmstrip, or a shot-list table.

- Typical information: shot number, thumbnail, caption, duration, camera data
- Primary actions: insert/append/replace shots, reorder, edit captions and camera notes, jump into a shot

### Timeline (animatic)

The timing surface where the sequence becomes a moving picture.

- Typical information: shot durations, camera-move keyframes, sound tracks, transitions
- Primary actions: set timing, animate camera/layer motion, add sound, play back

### Playback / animatic view

The viewing surface — the scene played as a rough film, commonly with sound and with on-screen overlays (timestamps, subtitles, or similar overlays) on export.

- Primary actions: play, scrub, review against dialogue

### Camera / viewfinder controls

The per-shot camera panel.

- Typical information: format/aspect, lens, height, angle, movement type, depth of field (where supported)
- Primary actions: adjust camera properties, save setups, record the exact lens/format per shot

### Export / share

The handoff surface: PDF/image/HTML board builders, shot-list and spreadsheet generators, movie and interchange-sequence exporters, print, and protected online sharing.

## Important Rules / Behaviors

- **Roughness is structural, not a limitation.** The application's whole value is that a scene can be modeled and watched faster than it can be produced. Mannequins, symbols, and sketch panels are the intended medium; pushing toward finished visuals moves the work into animation or editing tools.
- **Shots behave like records.** Once committed, a shot captures the staged state (camera, actors, lighting). Later changes to the set do not silently rewrite old shots; products either require explicit re-shooting of the frame or offer explicit propagation of new elements into existing shots. Accidental replacement of a shot is a recognized failure mode with dedicated recovery.
- **Diagram and shot list are one plan.** In blocking-style products, the visual diagram and the tabular shot list are two synchronized views of the same underlying shot data; a plan is never maintained twice.
- **Timing is consequential.** Shot durations established in the animatic are the same timing that flows into exported sequences; where the edit round-trips, panel order, duration, camera motion, and sound changes can be reconciled between the plan and the cut.
- **The plan is consumed by others.** Every output (boards, shot lists, camera data, animatics) is authored by one or two people and consumed by a crew. Numbering, captions, and camera data are structured precisely so they survive the handoff.
- **The staging space is the shared reference.** Whether panels, plan, or 3D set, the staging surface is what the team argues over; its persistent, editable nature (saved sets, reusable layouts, templates) is what makes multi-session pre-production work possible.

## Variants

- **Board-first realization** — drawn panels as the staging medium, with the animatic as an extension of the boards; dominant in animation and television studio pipelines, where boards travel through a revision process.
- **Blocking-first realization** — the overhead floor plan as the staging medium, optimized for speed so a scene can be blocked while a team is standing around it, commonly used by directors and educators, on desktop and mobile.
- **3D previz-first realization** — navigable 3D sets with posed actors and camera realism; common in feature-film prep, increasingly fed by real-world captures (location scans) and extended with virtual-camera techniques.
- **Mobile / on-location posture** — plan carried to the scout or the set: phone/tablet authoring, live-camera framing, shared web links for the team.
- **Animation pre-production vs live-action prep** — the same machinery serves animated productions (boards → animatic → animation pipeline) and live-action shoots (blocking → coverage → shoot), with different downstream consumers.
- **Advertising / commercial animatics** — short-form, pitch-oriented use of the same shot-playback machinery.
- **Edit-integrated workflows** — teams that keep conforming the animatic against the developing cut, treating the plan as a living document across production and post.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Storyboard Application | the closest neighbor; shares panels, scenes, and increasingly the animatic. The seam is the center of gravity: the storyboard type centers on the drawn board (narrative panels, drawing craft, script context) with playback as an extension; the previsualization type centers on the blocked scene (staging, camera setups, coverage, sequencing) with boards as one output among several |
| 3D Animation Application | produces finished animated work with performant characters; a previs tool borrows 3D machinery (sets, posed actors, keyframed cameras) but its output is a rough plan plus planning documents. Using a 3D animation or game-engine tool for previs does not make it this type — the plan-of-record orientation does |
| Video Editor / Non-linear Editing System | works on captured or generated footage; its timeline units exist because they were shot. The previsualization application works on shots that do not exist yet, and its animatic flows *into* the editor as reference — the dependency runs one way |
| Film Production Management System | the production office's system of record: schedules, call sheets, breakdowns, budget. Previs feeds it (boards inform scheduling) but shot planning is creative work, not logistics; neither contains the other's core objects |
| Production Scheduling / Call Sheet Application | consumes the plan for the shoot day; holds no staging space, no camera model, no animatic |
| Shot-list tools (no directory leaf) | ordered shot lists with notes are *below* this type: without a staged visualization and playback there is nothing to previsualize. Blocking products make exactly this argument when explaining why a shot list alone is not enough |
| UX Prototyping Application | shares the "rough model before building" idea but stages interactive interfaces, not filmable scenes with cameras; no shared machinery |

## Representative Products

- Toon Boom Storyboard Pro — board-first professional standard: drawn panels, animatic timeline, camera moves, sound, edit conformance
- FrameForge Studio — 3D previz standard: virtual sets and actors, real camera semantics, shot records and shot lists
- Shot Designer (Hollywood Camera Work) — floor-plan blocking: fused camera diagram + shot list + viewfinder + animation
- Previs Pro — mobile/Apple-first 3D previs: script import, full timeline, NLE export, AR and location-scan staging

## Sources

Research date: **2026-09-08**

- Toon Boom — Storyboard Pro product page: https://www.toonboom.com/products/storyboard-pro
- Toon Boom — Storyboard Pro Knowledge Base (Help Centre): https://helpcentre.toonboom.com/hc/en-ca/categories/39971055086995 — including "About the 3D space in Storyboard Pro" and "What is the difference between an AAF/XML/EDL export and Conformation?"
- Toon Boom — Storyboard Pro Online Help (docs): https://docs.toonboom.com/help/storyboard-pro-27/storyboard/index.html — including "About the Camera"
- FrameForge — product page: https://frameforge.com/ ; Knowledge Base: https://support.frameforge.com/ — including "Difference between SETS, SHOTS and SCENES", "What are the differences between 'Physical,' 'Floating' and 'Prop' cameras?", "Shot Preview Area", "Exporting Images, Auto-generated HTML or Shot Lists"
- Hollywood Camera Work — Shot Designer product page: https://www.hollywoodcamerawork.com/shot-designer.html
- Previs Pro — product page: https://previspro.com/ ; Knowledge Base: https://support.previspro.com/

> Sourcing note: all product evidence comes from official vendor product pages and support/knowledge bases. One additional game-engine-based previs product was considered for the sample but its official documentation could not be reached on the research date; it was excluded from the evidence base rather than filled in from memory. Precise numeric limits, prices, and format lists are deliberately not stated in this document; detailed per-product observations are kept in the paired Research Notes.
