# Game Engine / Game Development Platform

## Overview

A **Game Engine / Game Development Platform** is software that both **authors** and **runs** interactive games: it provides a real-time runtime that executes a game as a live simulation, an authoring environment in which the game world is composed from reusable objects and assets with author-defined behavior, an edit↔play loop for testing the game in place, and a way to deliver the finished game to players.

The defining structure is small:

```text
Real-time interactive runtime (the game loop)
└── Authoring environment over that runtime
    └── Edit↔play iteration loop
        └── Delivery of a runnable game
```

Everything else the market associates with engines — rendering/physics/audio/animation depth, prefab-class template systems, asset marketplaces, analytics/ads/cloud services, visual scripting, real-time collaboration, AI assistance — is widespread in current products but is not part of the defining core. Older engines (a runtime codebase paired with separate editor tools), 2D-first no-code creators, and platform-pole products all fit this definition without any of those specifics.

When the product stops running the game itself — a code-only runtime library with no integrated editor, a linear-rendered animation tool, or a pure game store with no authoring environment — it has drifted into a different kind of software.

## Users & Context

The primary user is a game developer: someone building a game to be played by others. Inside that population the toolchain serves distinct roles that modern engines bring into one environment:

- **programmer** — defines behavior in code (or visual logic), works against the engine's runtime API
- **game / level designer** — composes scenes and worlds from objects, assets, and reusable templates
- **artist / animator** — produces the assets the project references; animation work happens partly inside the engine

In hobby projects and small teams these roles collapse into one person; in larger studios they are distinct people working in the same project.

The user population spans a wide range: beginners and educators (served by the no-code pole), indie and mobile/web teams, large studios at the high-fidelity pole, and creators who publish into a vendor-operated platform with its own built-in audience.

The work context is iterative authoring on a workstation: compose the world, define behavior, test in place, adjust, and finally deliver to desktop, mobile, web, or console targets — or publish onto the platform's own runtime. A secondary context is non-game real-time work (simulation, film/TV virtual production, architectural visualization, automotive, XR), where the same engines are used for their runtime rather than for games.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as a game engine:

- **Real-time interactive runtime** — the engine executes the game as a live simulation: player input is read, game state is updated, and the result is rendered, continuously, frame by frame (the game loop). Without this, the product is an asset or animation authoring tool with nothing live to run.
- **Authoring environment over that runtime** — an editor in which the game world is composed from reusable objects and assets, and in which behavior is defined by the author (scripting and/or visual/event logic), with the engine supplying the runtime subsystems (rendering, physics, audio, input) so authors do not rebuild them. Without this, the product is a game framework/library — code-only development in a general-purpose IDE.
- **Edit↔play iteration loop** — the authored game can be run for testing from within the same toolchain (play-in-editor / preview / playtest), with changes made during play treated as test-state, not saved content. Without this, development falls back to edit-compile-run cycles against a built game.
- **Delivery of a runnable game** — the authored game is packaged or published as a runnable product for players on target platforms — standalone builds per platform in the classic form; publication onto the vendor's own platform and audience in the platform-pole form. Without this, the product is an internal prototyping toy, not a game development tool.

The four are jointly held. A runtime alone is a library or tech demo; an editor without a runtime is a level editor for someone else's engine; a play button without authoring is a generic test harness; authoring plus testing without delivery never reaches players.

### Standard Capabilities

A typical modern engine carries most of these. They are not what makes it an engine, but they make game development practical:

- **Runtime subsystems** — rendering (2D/3D, cameras, lights, materials, post-processing), physics (bodies, colliders, collision events), audio (clips, sources, mixing), input (keyboard, mouse, touch, gamepad), animation (clips, state machines, sprite/skeletal), in-game UI. No single subsystem is definitional — text and puzzle games need no physics; 2D creators need no 3D.
- **Reusable object templates** — a saved, configured object that can be instanced throughout the game, with edits to the template flowing to instances. Realized very differently per product (prefab assets with variants and overrides, saved scenes instanced as building blocks, custom object types).
- **Scripting layer** — author-defined behavior in code and/or visual event logic, with a runtime API and a defined execution order within the game loop (per-frame callbacks, event handlers).
- **Asset pipeline** — importing, referencing, and managing the images, models, audio, and other resources the game uses.
- **Editor surfaces** — viewport (2D/3D), scene hierarchy/outliner, inspector/properties, asset browser, script editor, animation editor, console.
- **Debugging and profiling** — frame inspection, statistics overlays, profilers, gameplay tests.
- **Project container** — a persistent, versionable container of scenes, assets, and settings.
- **Multi-platform build targets** — desktop, mobile, web; consoles in mature engines.
- **Multiplayer/networking support.**
- **Asset/extension marketplace or library.**

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Specific products realize each concept differently:

```text
Concept:          World composition
Implementations:  object-plus-component scenes, node trees, placed object types, platform data models

Concept:          Author-defined behavior
Implementations:  scripts in general-purpose languages, engine-specific scripting languages, visual condition/action event systems

Concept:          Reusable templates
Implementations:  prefab assets with variants/overrides, saved scenes instanced as nodes, custom object types, shared model libraries

Concept:          Delivery
Implementations:  per-platform standalone builds, store/portal packages, publication onto the vendor's own runtime and audience
```

A reader who has only seen one implementation — say, a component-based 3D engine — should still be able to recognize a no-code 2D creator or a platform-pole creator tool from the Core Model.

## How It Works

### Create a project

```text
Create a project (from a 2D or 3D template, where offered)
→ the project becomes the persistent container of scenes, assets, scripts, and settings
```

### Compose the world

```text
Open or create a scene (a level, a room, a game screen)
→ place objects into it (characters, props, lights, cameras, UI)
→ configure each object's properties
→ attach reusable behaviors/capabilities
→ reference assets (images, models, sounds)
→ save well-configured objects as templates for reuse across scenes
```

### Define behavior

```text
Author behavior as code scripts and/or visual event logic
→ attach it to objects
→ the engine executes it at defined points in the game loop (per frame, on input, on collision)
```

### Test in place

```text
Press play / preview
→ the game runs inside the toolchain, as players will see it
→ observe, interact, debug, profile
→ stop; changes made during play are discarded as test-state
→ adjust the authored content; repeat
```

This loop is the characteristic rhythm of engine work: the distance between "editing the game" and "playing the game" is one button press, and the two states are kept separate.

### Deliver

```text
Choose target platform(s)
→ build/package the game (or publish it onto the platform's own runtime)
→ distribute to players (stores, portals, or the platform's own audience)
```

### Core vs standard vs optional

**Defining core** — without these, not a game engine:

- real-time interactive runtime (the game loop)
- authoring environment over that runtime
- edit↔play iteration loop
- delivery of a runnable game

**Standard capabilities** — present in most modern products:

- rendering/physics/audio/input/animation/UI subsystems
- reusable object templates
- scripting layer with a runtime API
- asset pipeline
- editor surfaces (viewport, hierarchy, inspector, asset browser, script editor)
- debugging/profiling
- project container
- multi-platform targets, multiplayer support, marketplace/library

**Variant / optional** — depends on segment, era, and business model:

- authoring paradigm: code-first, visual/no-code, or hybrid
- 2D-first, 3D-first, or unified 2D+3D
- platform services layer (analytics, ads, in-app purchase, cloud/multiplayer backends) — some engines bundle these, others deliberately ship without them
- creator economy: paid asset store, free library, or platform profit sharing
- licensing model: open source, subscription, royalty, revenue share
- real-time collaboration
- non-game real-time uses (simulation, virtual production, visualization, XR)
- AI assistance (era-current)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Scene editor / viewport

The primary authoring surface.

- purpose: compose and arrange the game world
- typical information: the current scene as viewed in 2D or 3D, with placed objects, grid, and manipulation gizmos
- primary actions: place, move, rotate, scale objects; set properties; parent objects; save scenes

### Scene hierarchy / object list

- purpose: show the structure of the current scene as a tree of objects
- typical information: the scene's objects and their nesting
- primary actions: select, reorder, parent/ungroup, add and remove objects

### Inspector / properties

- purpose: view and edit the selected object's configuration
- typical information: the object's property values and attached components/behaviors/scripts
- primary actions: edit values, add or remove attached capabilities

### Asset browser

- purpose: manage the project's files and resources
- typical information: the project's imported assets and their organization
- primary actions: import, organize, search, drag assets into scenes

### Script editor

- purpose: author behavior in code (and, in some products, visual logic)
- typical information: script files, the engine's API reference
- primary actions: write and edit scripts, look up API documentation, debug

### Play / preview surface

- purpose: run the authored game for testing inside the toolchain
- typical information: the game as players will see it, optionally with debug overlays
- primary actions: play, pause, step, interact with the running game, stop

### Build / publish surfaces

- purpose: configure and produce the deliverable
- typical information: target platforms, build configurations, scene lists
- primary actions: select targets, configure, build/export/publish

### Debug / profiling panels

- purpose: diagnose runtime behavior
- typical information: console output, frame statistics, profiler traces
- primary actions: inspect, filter, measure

## Important Rules / Behaviors

### Play-mode changes are test-state

Mature engines commonly treat changes made while the game is running as temporary test-state rather than saved content; several products state explicitly that such changes are discarded when play stops. Authoring changes are made outside play mode. This separation is a defining behavior of the edit↔play loop.

### The engine supplies the subsystems; the author supplies the game

Rendering, physics, audio, and input are provided by the engine. The author's job is composing objects and defining behavior, not rebuilding infrastructure. Custom behavior attaches to objects and executes at defined points in the game loop.

### Templates propagate

Reusable object templates act as sources for instances: edits to the template flow to its instances, while instances can carry their own overrides. Exact semantics vary by product.

### The project is the container

Scenes, assets, scripts, and settings live inside a project. The project — not individual files — is the unit a team works in and versions.

### Delivery targets constrain portability

What can be built for which platform varies by product and by licensing; console targets in particular are gated by platform-holder agreements. Publishing onto a vendor-operated platform ties the game to that platform's runtime and audience.

## Variants

- **code-first general-purpose engines** — full 2D/3D subsystems, scripting in general-purpose or engine-specific languages, per-platform builds (e.g. Unity, Godot)
- **visual/no-code creators** — event-based logic and attachable behaviors instead of required code; beginner- and education-friendly (e.g. GDevelop)
- **high-fidelity AAA engines** — cutting-edge rendering and large-team pipelines (e.g. Unreal Engine)
- **platform-pole creator tools** — authoring + engine + publication onto the vendor's own runtime and audience, with creator-economy features built in (e.g. Roblox Studio)
- **non-game real-time uses** — the same engines used for engineering simulation, film/TV virtual production, architectural visualization, automotive, and XR

A variant remains a **Variant**, not a separate Type, unless it changes users, core objects, workflow, or rules so much that the Core Model no longer applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Game framework / library (no directory leaf) | provides the runtime leg only; authoring happens as code in a general-purpose IDE, with no integrated editor and no play-in-tool loop. The sharpest boundary of this Type: remove the integrated authoring environment → framework/library |
| 3D Animation Application | shares viewports, keyframes, and rigs; delivers a linear rendered moving image from a virtual camera, not an interactive runtime. Remove interactivity → animation; remove linear delivery → engine |
| 3D Modeling Application | authors static geometry assets that engines consume and run; no game loop |
| Simulation software (engineering) | both "simulate"; simulation serves engineering analysis (solvers, accuracy, reports), the engine serves playable real-time experiences delivered to players |
| Low-code / No-code Application Builder | both can be visual; app builders center on forms, data, and workflows for business applications, engines on the real-time game loop |
| Mobile App Development Platform | engines build mobile apps too; the seam is the game loop vs the app lifecycle/UI-form world |
| Interactive Prototype Builder | UX prototypes center on flows and clickthroughs; engines center on real-time simulation |
| Digital Twin Platform | engines serve as the real-time 3D visualization substrate; twin platforms center on IoT data binding and operational state |
| Game store / distribution platform | distribution alone is NOT this Type; the platform pole always includes the authoring environment and the engine |

## Representative Products

- Unity
- Godot
- GDevelop
- Roblox Studio

Unreal Engine is retained as a market anchor for the high-fidelity pole; its official documentation could not be fetched during research, so no operational claims about it are made here.

The Core Model was checked against older engines (the separate-editor-tool era), 2D-first no-code creators, and the platform pole to avoid over-fitting to the modern integrated-editor pattern.

## Sources

Research date: **2026-09-08**

- Unity Manual (Unity 6.6) — https://docs.unity3d.com/Manual/index.html (GameObjects, Scenes, Prefabs, Game view / Play mode, Build profiles, scripting, Unity Services)
- Godot Engine documentation (4.7 stable) — https://docs.godotengine.org/en/stable/about/introduction.html and getting-started pages (key concepts, nodes and scenes, first look at the editor)
- GDevelop 5 documentation — https://wiki.gdevelop.io/gdevelop5/ (interface, objects, behaviors, events, publishing)
- Roblox Creator Hub documentation — https://create.roblox.com/docs (Studio; how Roblox is different)

> Sourcing limitation: Unreal Engine's official documentation was unreachable from the research environment (JS-rendered shell; product site 403), and GameMaker's manual was geo-blocked — the beginner/2D pole is covered by GDevelop instead. Precise operational details (numeric limits, licensing percentages, royalty thresholds, default settings) are intentionally not stated in this document; such details remain in the Research Notes. Historical engines were checked structurally rather than from primary sources, and historical claims are held at inference strength.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical / market-sample check are recorded in the paired Research Notes.
