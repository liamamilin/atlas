# Research Notes — Game Engine / Game Development Platform

## Research Goal

Understand what a game engine (and the broader "game development platform" reading of the leaf) actually is as an Application Type: what objects exist inside it, what users do with them, how the authoring and running of a game work, and where the Type's boundaries lie against game frameworks/libraries, 3D DCC tools (animation/modeling), simulation software, and low-code/no-code application builders.

## Initial Boundary

- Leaf: `Game Engine / Game Development Platform` (§12 Software Development & Product Engineering).
- Working hypothesis: a game engine is software that both **authors** and **runs** interactive games — a real-time runtime (rendering, physics, audio, input) plus an authoring environment (editor) plus a way to deliver the finished game to players.
- Likely confusions:
  - Game frameworks/libraries (Phaser, MonoGame, LibGDX class) — runtime without an integrated editor. No directory leaf exists for them.
  - 3D Animation Application (processed 2026-09-06) — shares viewports, keyframes, rigs; delivers linear rendered output, not an interactive runtime.
  - 3D Modeling Application — asset authoring consumed by engines.
  - Simulation software (§16) — real-time-looking simulation but engineering-analysis purpose.
  - Low-code/No-code Application Builder (§12 siblings) — visual authoring but form/data-app semantics, no game loop.
  - The "platform" half of the leaf name — engines bundled with services, marketplaces, and (in the extreme pole) distribution to the vendor's own audience.

## Research Questions

1. What is the core object model? (project, scene/level, game object/entity, components/behaviors, assets, reusable templates)
2. What does the authoring environment look like, and what are its main surfaces?
3. How is behavior defined? (scripting languages, visual/event logic, reusable behaviors)
4. What exactly is the edit↔play iteration loop, and how do products treat changes made during play?
5. What does the runtime provide (rendering, physics, audio, input, animation, UI, networking), and is any subsystem definitional?
6. How does delivery work (build/export/publish), and what targets exist?
7. Are services (analytics, ads, multiplayer backend), asset marketplaces, and collaboration definitional or add-on layers?
8. Where is the boundary against game frameworks/libraries, 3D animation, modeling, simulation, and app builders?
9. Historical check: would older engines (id-era, RPG Maker-class, platform-native) still fit the definition?

## Representative Products

| Product | Why sampled | Evidence status |
|---|---|---|
| Unity | Dominant cross-platform engine; component-based authoring; indie-to-enterprise reach | Official Manual fetched (Unity 6.6) — rich |
| Godot | Open-source engine; node/scene philosophy; community-driven | Official docs fetched (4.7) — rich |
| GDevelop | No-code/visual, open-source, beginner/2D pole (substitute for GameMaker, which was geo-blocked) | Official wiki fetched — rich |
| Roblox Studio | The "game development platform" pole: authoring + engine + publishing to the vendor's own audience | Official Creator Hub docs fetched — rich |
| Unreal Engine | AAA/high-fidelity pole; C++/visual-scripting philosophy | **Official docs unreachable** (JS-rendered shell ×2; product site 403) — included on market position only; no operational claims drawn |

Selection notes: GameMaker was the preferred beginner/2D sample but its manual returned HTTP 451 (geo-block) — dropped after one attempt per network rules; GDevelop substitutes that pole. Unreal was kept in the sample for market representativeness despite unreachable documentation, with all claims about it withheld.

## Sources

- Unity Manual (Unity 6.6): https://docs.unity3d.com/Manual/index.html — landing; GameObjects (GameObjects.html); Scenes (CreatingScenes.html); Prefabs (Prefabs.html); Game view / Play mode (GameView.html); Build profiles (PublishingBuilds.html → BuildSettings.html); Programming in Unity (scripting.html); Unity Services (UnityServices.html). Fetched 2026-09-08.
- Godot Engine docs (4.7 stable): https://docs.godotengine.org/en/stable/about/introduction.html ; getting_started/introduction/key_concepts_overview.html ; getting_started/step_by_step/nodes_and_scenes.html ; getting_started/introduction/first_look_at_the_editor.html. Fetched 2026-09-08. Export tutorial pages 404 (three URL variants tried); export evidence taken from the official introduction page instead.
- GDevelop 5 documentation: https://wiki.gdevelop.io/gdevelop5/ (TOC: interface, objects, behaviors, events, core features, publishing, extensions) ; https://wiki.gdevelop.io/gdevelop5/getting_started/ . Fetched 2026-09-08.
- Roblox Creator Hub docs: https://create.roblox.com/docs (landing) ; https://create.roblox.com/docs/studio ; https://create.roblox.com/docs/get-started/how-is-roblox-different . Fetched 2026-09-08.
- Unreal Engine: dev.epicgames.com/documentation (JS-rendered, empty shell ×2); unrealengine.com/en-US/what-is-unreal-engine (403). **Not usable.**

## Product Observations

### Unity (evidence layer A — directly observed, official Manual)

- Positioning: "Unity 6.6 User Manual… the next generation of the Unity Engine… high-quality, high-performance experiences for all supported platforms." Manual sections: rendering/render pipelines, lighting, visual effects, animation, audio, physics, scripting, UI toolkits, 2D, XR, multiplayer, platform development, package management, Unity services, AI tools.
- **GameObject/Component model**: "The GameObject is the most important concept in the Unity Editor. Every object in your game is a GameObject, from characters and collectible items to lights, cameras and special effects." GameObjects "act as containers for Components, which implement the functionality." A GameObject always has a Transform component (position/orientation) that cannot be removed. Built-in component types exist; custom components are authored as scripts inheriting MonoBehaviour. A Light = GameObject + Light component; a cube = Mesh Filter + Mesh Renderer + Box Collider.
- **Scenes**: "Scenes are where you work with content in Unity. They are assets that contain all or part of a game or application… for a more complex game, you might use one scene per level." A project holds any number of scenes; a new project opens a sample scene containing only a Camera and a Light. Scene templates; multi-scene editing.
- **Prefabs**: "create, configure, and store a GameObject complete with all its components, property values, and child GameObjects as a reusable asset. The prefab asset acts as a template from which you can create new prefab instances in the Scene." Nested prefabs, prefab variants, instance overrides, runtime instantiation from code.
- **Play mode (edit↔play loop)**: "Use Play mode to run your project and test how it works as it would in a built application." Play / Pause / Step (one frame) buttons. "In Play mode, any changes you make are temporary and are reset when you exit Play mode." The Game view "displays how your final, built application looks" and "is rendered from the Cameras in your application." Simulator view previews the built application on a mobile device. Frame Debugger and a rendering-statistics overlay (Stats) support diagnosis in Play mode.
- **Build**: "Unity can build your application for different platforms with unique build configurations using build profiles in the Unity Editor" (Build Profiles window, formerly Build Settings); scene list managed per build; Platform Browser.
- **Scripting**: "Programming in Unity refers to authoring your project's functionality in code rather than through the Unity Editor UI." C#; docs cover "the order in which Unity executes your script components and the lifecycle callbacks within those scripts during the runtime application loop," time/frame-rate management, coroutines across frames, compilation and code reload, test framework, debugging.
- **Services (beyond the engine)**: "Unity is more than an engine. It also brings a growing range of integrated services to engage, retain and monetize audiences." Named: Unity Ads, Unity Analytics, Unity Build Automation, Unity Multiplayer, Unity Gaming Services.
- **Ecosystem**: Package manager ("use packages to add assets and extend the Unity Editor"); Asset Store (linked throughout).

### Godot (evidence layer A — directly observed, official docs)

- Positioning: "the free and open source community-driven 2D and 3D game engine… a feature-packed, cross-platform game engine to create 2D and 3D games from a unified interface. It provides a comprehensive set of common tools, so that users can focus on making games without having to reinvent the wheel. Games can be exported with one click to a number of platforms, including the major desktop platforms (Linux, macOS, Windows), mobile platforms (Android, iOS), as well as Web-based platforms and consoles." MIT license, "no royalties."
- **Core concepts**: "In Godot, a game is a tree of nodes that you group together into scenes. You can then wire these nodes so they can communicate using signals."
  - Nodes: "the fundamental building blocks of your game… dozens of kinds that can display an image, play a sound, represent a camera." Every node has a name, editable properties, per-frame callbacks, extensibility, and parent-child composition. A character = CharacterBody2D + Sprite2D + Camera2D + CollisionShape2D.
  - Scenes: reusable saved trees of nodes with one root; "Godot's scenes are flexible; they fill the role of both prefabs and scenes in some other game engines." Scenes can be nested/instanced; a project requires one **main scene** as the entry point.
  - Scene tree: all scenes together form the running game.
  - Signals: observer-pattern event wiring between nodes (button pressed, collision, area entered; custom signals allowed).
- **Editor**: "The Godot editor essentially is a scene editor." Project Manager (manage/create projects; Asset Library tab, offline by default). Five main screens: **2D, 3D, Script, Game, Asset Library**. Docks: FileSystem (project files: scripts, images, audio), Scene (active scene's nodes), Inspector (selected node's properties). Bottom panels: debug console, animation editor, audio mixer. Playtest buttons; Movie Maker Mode toggle.
- **Edit↔play loop**: "Run Current Scene" (F6) and "Run Project" (F5) buttons; the **Game screen** "is where your project will appear when running it from the editor. You can go through your project to test it, and pause it and adjust it in real time. Note that this is for testing how adjustments would work, any changes made here are not saved when the game stops running." Game embedding (game window inside editor) documented.
- **Script screen**: "a complete code editor with a debugger, rich auto-completion, and built-in code reference." Integrated class reference (F1 search) over the full API.
- **Project**: settings in a `project.godot` file; `res://` project-root file system; scenes saved as `.tscn`.

### GDevelop (evidence layer A — directly observed, official wiki)

- Positioning: "GDevelop is a full-featured, no-code and AI-powered, open-source game engine."
- **Getting started**: download for desktop (Windows/macOS/Linux), mobile (iOS/Android), or browser; "choose a game template that can be customized in a few minutes… or start from scratch"; "A **Preview** button is available in the toolbar. This button launches a preview of your game in a new window."
- **Interface**: Games dashboard (game analytics, player feedback, leaderboard administration, marketing); Project manager (game icons/thumbnail, properties, resources); **Scene editor** (external layouts, global objects, layers and cameras, layer effects); **Events editor** (external events); Preview; Debugger (with profiling); Gameplay tests (including command line).
- **Objects** (the placed building blocks): Sprite (with collision mask, edit points), Tiled Sprite, Panel Sprite (9-patch), Tilemap, Light, Text, 3D Box, 3D Model, 3D Light, Button, Particles emitter, Spine, Video, Text input, Slider, Multitouch joystick, Shape painter, **Custom Objects ("Prefabs")** with variants.
- **Behaviors** (reusable attachable capabilities): Anchor, Destroy outside screen, Draggable, Grid-based/Navmesh pathfinding, 2D Physics, 3D Physics, Platform(er), Top-Down Movement, Tween, and **custom behaviors** authored from events.
- **Events** (the no-code logic model): conditions/actions with else/repeat/while/for-each structures, expressions, JavaScript code escape hatch, custom functions, asynchronous events.
- **Variables**: global, scene, object/instance, local; structures and arrays.
- **Engine features**: audio (sounds/music, spatial sound), camera/layers, collisions, gamepad, keyboard, mouse/touch, timers, inventories, dialogue tree, save state, leaderboards, multiplayer, player authentication, network/P2P/Firebase, effects, lights, particles, tweening, window/resolution management.
- **Publishing**: Android (Play Store), iOS (App Store), desktop (Windows/macOS/Linux), web (gd.games — the vendor's own portal), Steam, Amazon App Store, Facebook Instant Games, CrazyGames, Poki, itch.io, Game Jolt, Microsoft Store, Kongregate; manual exports (HTML5 to local folder, Cordova for mobile, Electron for desktop); "Marketing your game" section.
- **Extensions**: installable extensions with tiers; AdMob ads; mobile in-app purchase; platform SDKs (Poki, CrazyGames, Discord, Steamworks experimental, Shopify).

### Roblox Studio (evidence layer A — directly observed, official Creator Hub)

- Positioning: "Roblox Studio is free to use and has everything you need to start publishing creations to hundreds of millions of Roblox users on consoles, desktops, and mobile devices." "Build, script, test, and publish… directly in Studio."
- **Authoring**: "Easy 3D world building — drag and drop objects into your workspace, move and rotate… texture and polish your world"; "An intelligent script editor — syntax highlighting, code completion, and inline documentation"; "Device emulation and playtesting — emulate a wide range of screen sizes and form factors… before sharing your game with the world."
- **Engine**: "Roblox Studio comes bundled with the powerful Roblox engine that runs anywhere with endless customization." "A standard and flexible data model — data models tell the engine how to render and simulate your games. Studio can manipulate data models at both edit and runtime, allowing you to create and iterate freely." "Out-of-the-box primitives and services — construct 3D worlds… with out-of-the-box primitives like simple 3D objects, physical constraints, and services for lighting, sound, and more. Choose what Roblox provides by default or customize behavior with property overrides and scripting."
- **AI assistance**: Assistant can "update the data model directly… add objects in bulk, modify scripts in place, optimize code"; material/texture generators; avatar rigging/caging tools.
- **Collaboration & economy**: real-time team creation; group-based access ("control how multiple team members work on the same games, use the same assets, and share profits"); Creator Store ("create and access millions of freely available models, meshes, images, sounds, and videos").
- **Platform difference (official)**: cloud-based ("join new games in seconds, without having to download massive files"), automatic matchmaking, cross-platform publishing; UGC community ("many devs are also often community members"); "develop and publish updates quickly"; creator ecosystem beyond the platform.

### Unreal Engine (evidence layer: none — source inaccessible)

- Included for market representativeness (AAA/high-fidelity pole). Official documentation could not be fetched (JS-rendered application shell; product site 403). **No operational claims about Unreal are made in this pass.** Its inclusion in Representative Products rests on market position, not on observed evidence.

## Cross-product Comparison

| Structure | Unity | Godot | GDevelop | Roblox Studio | Verdict |
|---|---|---|---|---|---|
| Real-time interactive runtime (game loop) | yes ("runtime application loop", lifecycle callbacks) | yes (per-frame node callbacks; scene tree) | yes (preview runs the game; events/behaviors execute) | yes ("data models tell the engine how to render and simulate") | **Core (all 4)** |
| Authoring editor composing a world from objects | yes (Scene view, GameObjects) | yes ("the editor essentially is a scene editor") | yes (Scene editor + objects) | yes (3D world building, drag/drop) | **Core (all 4)** |
| Behavior defined by the author (code and/or visual) | yes (C# scripts as components) | yes (GDScript/C#, signals) | yes (events; JS escape hatch) | yes (scripts; property overrides) | **Core (all 4); mechanism varies** |
| Reusable object templates | Prefabs (variants, overrides, nesting) | scenes-as-nodes ("fill the role of both prefabs and scenes") | Custom Objects ("Prefabs") with variants | prefabs-class reuse via Creator Store assets/models | **Core-adjacent (all 4; L1 — template semantics vary)** |
| Assets referenced by the project | yes (Project window, packages) | yes (FileSystem dock, res://) | yes (resources in project manager) | yes (Creator Store + own assets) | **Core (all 4)** |
| Engine-provided subsystems: rendering, physics, audio, input | yes (manual sections) | yes (node types; audio mixer) | yes (behaviors + features) | yes ("primitives and services… lighting, sound") | **Core-adjacent (all 4; individual subsystems not each definitional)** |
| Play-in-editor with temporary-change semantics | yes ("changes… are temporary and are reset") | yes ("changes made here are not saved when the game stops") | yes (Preview launches the game) | yes (playtesting modes; "manipulate data models at both edit and runtime") | **Core (all 4; explicit temporary-change semantics in 2/4)** |
| Delivery of a runnable game | yes (build profiles per platform) | yes ("exported with one click… desktop, mobile, web, consoles") | yes (publish to stores/portals; manual exports) | yes (publish to the Roblox platform itself) | **Core (all 4; platform pole realizes it as publish-to-platform)** |
| Debug/profiling tooling | yes (Frame Debugger, Stats) | yes (debugger, bottom panels) | yes (Debugger, profiling, gameplay tests) | yes (testing modes; output) | Common (all 4) |
| Multiplayer/networking support | yes (multiplayer packages/services) | yes (documented networking) | yes (multiplayer, P2P, Firebase) | yes (servers/matchmaking built into platform) | Common (all 4) |
| Asset/extension marketplace | yes (Asset Store, packages) | yes (Asset Library, offline by default) | yes (extensions with tiers) | yes (Creator Store) | Common (all 4) — but historical engines predate marketplaces; not definitional |
| Platform services (analytics/ads/IAP/cloud) | yes ("Unity is more than an engine") | no (community engine; third-party by design) | yes (dashboard, AdMob, IAP) | yes (built into platform) | **Variant (3/4; Godot counter-sample)** |
| Real-time collaboration | via source control (documented elsewhere) | via source control | not observed | yes (real-time team creation) | Variant |
| AI assistance | yes (Unity AI) | not observed | yes ("AI-powered") | yes (Assistant) | Variant (era-current) |
| 2D vs 3D | both | both ("2D and 3D… unified interface") | 2D-first with 3D objects | 3D | Variant |
| Publishing to the vendor's own audience/runtime | no | no | partial (gd.games portal) | yes (the defining platform move) | Variant (platform pole) |

## Canonical Model (L0 — Defining Invariant)

Four jointly-held structures. The abstraction is deliberately written at concept level so that older engines (separate editor tools), 2D-first creators, and platform-pole products all satisfy it.

1. **The real-time interactive runtime** — the engine executes the game as a live simulation: player input is read, the game state is updated, and the result is rendered, continuously, per frame (the game loop). Remove → asset/animation authoring tools with no live game (3D animation delivers linear rendered output; a modeling tool has no runtime).
2. **The authoring environment over that runtime** — an editor in which the game world is composed from reusable objects and assets, and in which behavior is defined by the author (scripting and/or visual/event logic), with the engine supplying the runtime subsystems (rendering, physics, audio, input) so authors do not rebuild them. Remove → a game framework/library (code-only, no integrated editor) or a DCC tool.
3. **The edit↔play iteration loop** — the authored game can be run for testing from within the same toolchain (play-in-editor / preview / playtest), with changes made during play treated as test-state, not saved content. Remove → framework-style edit-compile-run development, or a sandbox that cannot be tested in place.
4. **Delivery of a runnable game** — the authored game is packaged or published as a runnable product for players on target platforms (standalone builds per platform in the classic form; publish-to-platform in the platform-pole form). Remove → an internal prototyping toy; the product stops being a game development tool.

Jointly-held is load-bearing:

- 1 alone = a real-time rendering/simulation library or tech demo (no authoring) — the framework/library edge.
- 2 without 1 = a level/world editor for someone else's runtime (mod-tool territory), not an engine product.
- 3 without 1+2 = a generic run/test harness.
- 1+3 without 2 = the game framework/library class (runtime + code-only authoring) — the honest market edge this Type is distinguished from.
- 2+3 without 1 = a scene editor with an exporter and nothing to run — no such product class exists.
- 1+2 without 3 = an engine that cannot be tested or shipped — no market product.

## L1 — Common Mature Structure

Present across the sampled products; expected by the market; not part of the definition:

- rendering subsystem (2D/3D, cameras, lights, materials/shaders, post-processing; render pipelines in larger engines)
- physics simulation (bodies, colliders, collision events)
- audio subsystem (clips, sources/listeners, mixing)
- input handling (keyboard, mouse, touch, gamepad)
- animation system (clips, state machines, sprite/skeletal animation)
- in-game UI system
- asset pipeline (import, reference, resource management)
- reusable object templates (prefab/instancing semantics — realized very differently per product)
- scripting layer with a runtime API and defined execution order within the game loop
- editor surfaces: viewport (2D/3D), scene hierarchy/outliner, inspector/properties, asset browser, script editor, animation editor, console
- debugging/profiling tooling (frame debugger, statistics, profiler, gameplay tests)
- project as a persistent, versionable container of scenes/assets/settings
- multi-platform build targets (desktop/mobile/web; consoles in mature engines)
- multiplayer/networking support
- asset/extension marketplace or library

## L2 — Variant / Optional Structure

- authoring paradigm: code-first (Unity C#, Godot GDScript/C#) vs visual/no-code-first (GDevelop events) vs hybrid (visual scripting layers on code engines)
- dimensionality: 2D-first, 3D-first, unified 2D+3D
- services layer: analytics, ads, IAP, cloud/multiplayer backends (Unity "more than an engine"; GDevelop dashboard; Roblox built-in; Godot deliberately without)
- marketplace/creator economy: paid store vs free library vs platform Creator Store with profit sharing
- licensing/business model: open source (MIT, no royalties), subscription, royalty-based, platform revenue share — vendor-specific in detail; the *existence* of varied models is the variant
- distribution posture: standalone builds to external stores vs publish-to-the-vendor's-own-platform (Roblox; gd.games partially)
- collaboration: real-time co-editing (Roblox Studio) vs source-control-based workflows
- non-game real-time uses: simulation, film/TV virtual production, architectural visualization, automotive, XR — engines used beyond games
- AI assistance (era-current): code/asset generation, data-model manipulation
- education positioning: templates, in-app tutorials, classroom use

## L3 — Vendor-specific (research notes only)

- Unity: GameObject/Component/MonoBehaviour; Transform always attached; Prefabs with variants/overrides/nesting; Build Profiles (formerly Build Settings); Device Simulator view; Frame Debugger; Unity Gaming Services (Ads, Analytics, Build Automation, Multiplayer); Cinemachine/ProBuilder/UI Toolkit; DOTS; package manager.
- Godot: Node/Scene/SceneTree; signals (observer pattern); GDScript + C#; `project.godot` + `res://`; main-scene concept; five main screens (2D/3D/Script/Game/Asset Library); Movie Maker Mode; game embedding; MIT/no-royalty positioning; Asset Library offline by default.
- GDevelop: events (conditions/actions) as the primary logic model; behaviors as attachable capabilities; object taxonomy (Sprite/Tiled/Panel/Tilemap/3D Box…); Custom Objects ("Prefabs") with variants; gd.games portal; extension tiers; publishing target list (Steam, itch.io, Poki, CrazyGames, Facebook Instant Games, Kongregate…); Cordova/Electron manual exports.
- Roblox: Studio + bundled engine; the data model (Instances) manipulated at edit and runtime; Luau scripting (named in docs as "script editor" — language name not claimed here); Creator Store; groups with profit sharing; experiences published to the Roblox client; matchmaking/cloud delivery.

## Rejected Findings (not promoted to core)

- "Physics defines the Type" — rejected: text/card/puzzle games need no physics; physics is an engine-provided subsystem (L1).
- "3D defines the Type" — rejected: 2D-first engines are engines (GDevelop sampled; GameMaker class); dimensionality is a variant.
- "A specific scripting language defines the Type" — rejected: C#, GDScript, events-model, and platform scripts all realize the same concept (author-defined behavior); mechanism varies.
- "The asset marketplace defines the Type" — rejected: present in all 4 sampled products but absent from historical engines; Godot's library is optional and offline by default. L1/L2.
- "Multiplayer defines the Type" — rejected: single-player games are fully served; networking is L1.
- "Visual/no-code authoring defines the Type" — rejected: code-first engines dominate the market; paradigm is a variant.
- "Platform services (analytics/ads/cloud) define the Type" — rejected: Unity's own wording ("Unity is more than an engine") frames services as an add-on layer; Godot counter-sample. L2.
- "A single-window integrated application defines the Type" — rejected: historical engines paired a runtime codebase with separate editor tools; the integrated editor is the modern consolidation, not the invariant. The invariant is the authoring environment + runtime + iteration + delivery, however packaged.
- "Real-time viewport playback defines the Type" — rejected: 3D animation applications also have real-time viewports; the difference is what the delivery is (linear render vs interactive runtime).

## Boundary Findings

- **vs Game framework/library (Phaser, MonoGame, LibGDX class — no directory leaf)**: the sharpest boundary. A framework provides the runtime leg only; authoring is code in a general-purpose IDE; there is no integrated editor, no scene-composition surface, no play-in-tool loop. Test: remove the integrated authoring environment → framework/library. Taxonomy observation: the directory has no leaf for game frameworks/libraries; they fall outside this Type by the editor leg. Recorded for the taxonomy owner; no directory change made.
- **vs 3D Animation Application (processed 2026-09-06)**: confirmed from this side. Animation centers on linear rendered delivery from a virtual camera; the engine centers on the live interactive runtime. Overlap: real-time viewports, keyframes, rigs, game-asset export. Test: remove interactivity/runtime → animation; remove linear delivery → engine. (The animation pass recorded the mirror image of this finding.)
- **vs 3D Modeling Application**: modeling authors static geometry assets; the engine consumes them and runs them. Test: remove the runtime/game loop → modeling/DCC territory.
- **vs Simulation software (§16 CAE / System Simulation)**: both "simulate," but simulation software serves engineering analysis (accuracy, solvers, reports) while the engine serves playable real-time experiences (frame-rate interactivity, input, delivery to players). Engines are increasingly *used for* simulation/visualization — held as a non-game-use variant, not a boundary dissolution.
- **vs Low-code Application Platform / No-code Application Builder (§12 siblings)**: both can be visual, but the app-builder world is forms/data/workflows for business applications; the engine world is the real-time game loop (input → update → render), collisions, physics, sprites. GDevelop is no-code yet unambiguously engine-shaped (objects/behaviors/events/collisions/publishing). Test: remove the game loop → app builder.
- **vs Mobile App Development Platform (§12 sibling)**: engines build mobile apps too; the seam is the game loop vs the app lifecycle/UI-form world.
- **vs Interactive Prototype Builder (§04.15)**: UX prototypes center on flows/clickthroughs; engines center on real-time simulation. Prototypes may be built in engines; the Types' centers differ.
- **vs Digital Twin Platform**: engines serve as the real-time 3D visualization substrate for twins; twin platforms center on IoT data binding and operational state. Substrate relationship.
- **Platform pole internal boundary**: Roblox Studio = authoring + engine + publishing to the vendor's own audience. A pure game store/distribution platform (no authoring environment) is NOT this Type. The "Game Development Platform" half of the leaf name is realized as: engine + integrated services + (in the pole) distribution — never as distribution alone.

## Historical / Market-Sample Check

- **id-era engines (Doom/Quake class, 1990s)** — structural reasoning, not direct observation this pass: runtime engine + level editors (separate tools) + game build. Satisfies legs 1, 2, 4; the edit↔play loop existed as editor→run-game iteration, coarser than today's integrated play mode. Confirms that the integrated single-window editor must NOT be definitional.
- **RPG Maker class (1990s+, Japan-origin) and GameMaker (1999)** — structural reasoning: map/room editors + event/behavior systems + playtest + game export for non-programmers. Satisfies all four legs with zero code and zero modern features. Confirms the no-code pole is old, not new.
- **Platform-native/UGC pole (Roblox, 2006-origin)** — directly observed today: satisfies all four legs with publish-to-platform as the delivery realization.
- Conclusion: the four-leg core holds across eras and poles. Nothing modern (marketplaces, services, visual scripting, AI, cloud, real-time collaboration) is in the core. Historical check **passed**, with the caveat that the historical products were reasoned about structurally rather than fetched from primary sources.

## Uncertainties

- Unreal Engine official documentation was unreachable (JS-rendered shell ×2; product site 403). Unreal is retained as a representative product on market position; no operational claims about it appear anywhere in this pass. Its well-known Blueprints/royalty details are deliberately NOT documented from memory.
- GameMaker manual geo-blocked (HTTP 451); the beginner/2D pole is covered by GDevelop instead. GameMaker-specific claims: none.
- Godot export tutorial pages 404 (three URL variants); export evidence for Godot comes from the official introduction page ("exported with one click… desktop, mobile, web, consoles") — adequate for the delivery leg, but per-target export mechanics are not documented here.
- Exact numeric facts (limits, defaults, licensing percentages, royalty thresholds) were deliberately not stated anywhere — fetched evidence does not support that precision.
- Historical engines were reasoned about structurally (well-known market history), not fetched from primary sources; historical claims are kept at inference strength.
- The directory has no leaf for game frameworks/libraries; this pass records the seam but cannot cross-check a counterparty pass.

## Final Synthesis

A game engine is defined by four jointly-held structures: a real-time interactive runtime executing the game loop; an authoring environment that composes the game world from reusable objects/assets with author-defined behavior while the engine supplies the runtime subsystems; the edit↔play iteration loop with test-state semantics; and delivery of the authored game as a runnable product for target platforms (or, in the platform pole, publication onto the vendor's own runtime and audience). Everything else the market associates with engines — rendering/physics/audio/animation depth, prefabs, marketplaces, services, visual scripting, collaboration, AI — is common mature structure or variant structure, not the definition. The Type's sharpest boundary is against game frameworks/libraries (runtime without authoring environment); its most important processed-neighbor boundary is against 3D animation (linear delivery vs interactive runtime); and the "platform" half of the leaf name is realized as services/marketplace layers and, at the extreme, publish-to-platform distribution — never as distribution alone.
