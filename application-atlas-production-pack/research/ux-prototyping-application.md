# Research Notes — UX Prototyping Application

Research date: 2026-09-10

## Research Goal

Understand what a UX Prototyping Application actually is, from real products that self-identify with the "UX prototyping" label: what the central working artifact is, what objects exist in its world (screens, interactions, flows, feedback), what the characteristic workflow is from idea to validated design, and — because this leaf sits in the 04.15 family alongside two processed siblings — where its boundary lies against UI Design Application, Interactive Prototype Builder, and the adjacent Types.

This pass carries four ratification duties left by earlier passes:

1. **interactive-prototype-builder** (processed 2026-09-07): discharge the heavy-overlap JOINT REVIEW flag — candidate outcomes were "keep-both with the fidelity/stage seam" or "one-Type-two-emphases presentation".
2. **ui-design-application** (processed 2026-09-09): ratify from this side the held hypothesis (UI Design centers the screen-design artifact; UX Prototyping centers the prototyping/validation process).
3. **collaborative-design-platform** (processed): resolve the probable-partial-overlap flag (04.15 siblings).
4. **ai-design-generator** (processed): resolve the Uizard-class boundary flag (generation of multi-screen editable prototypes).

## Initial Boundary

Working hypothesis before research:

- Core purpose: build interactive representations of a product interface — from wireframe-level screens to clickable simulations — so a design can be experienced, discussed, tested, and approved before engineering implementation.
- Likely users: UX/product designers, product managers, business analysts, founders, agencies; stakeholders and developers as consumers.
- Nearest neighbors: Interactive Prototype Builder and UI Design Application (same directory family 04.15), Collaborative Design Platform, Digital Whiteboard, Diagramming Application, No-code Application Builder, Visual Website Builder, AI Design Generator.
- Known tensions going in:
  - The interactive-prototype-builder pass found "no clean market split between 'UX prototyping' and 'interactive prototype building'" — the two labels are used for the same products.
  - The ui-design-application pass found Balsamiq (low-fi pole) self-labels as a UI design tool while positioning itself process-oriented ("the part of the process where you're still figuring out what to build").
  - Figma is the archetype of UI design, prototyping, and collaborative design at once — packaging straddles all three leaves.

## Research Questions

1. What do products self-labeled as UX prototyping tools actually center on — the simulation artifact, or the process around it?
2. What are the core objects (screens/pages, interactions, flows, iterations, comments, specs)?
3. How does the workflow run from idea to validated, approved design?
4. Is the wireframe→prototype fidelity ladder a definitional structure or a common one?
5. What logic depth exists (variables, conditions, expressions) and where does it sit?
6. How are prototypes shared, reviewed, tested, and approved?
7. Where exactly are the seams vs Interactive Prototype Builder, UI Design Application, Collaborative Design Platform, AI Design Generator, no-code builders, whiteboards/diagramming, and user-flow tools?
8. Do older / differently-positioned products still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers — deliberately avoiding re-sampling the sibling passes' products (Figma, Axure RP, ProtoPie, Marvel, Sketch, Penpot), whose evidence is reused as cross-pass context:

| Product | Philosophy / pole | Customer tier | Evidence tier |
|---|---|---|---|
| UXPin | realism/code-backed pole — "prototypes that feel like the real thing"; design-systems and enterprise posture | professional → enterprise | Tier 1 (official docs) |
| Justinmind | dedicated full-spectrum prototyping tool — wireframes → high-fi interactive prototypes, forms/data, requirements | professional / SMB → enterprise | Tier 1 (help center) |
| Moqups | early-stage all-in-one — wireframes + diagrams + prototypes + whiteboard in one browser app | individuals / SMB teams | Tier 2 (product pages; help center unreachable) |
| Balsamiq | intentionally low-fidelity wireframing-first pole; "product people, not designers" | individuals / small product teams | Tier 1 (help center) |
| Overflow | boundary probe — user-flow diagramming + design presentation; screens imported, not authored | design teams / agencies | Tier 2 (product pages) |

## Sources

All fetched 2026-09-10 unless noted.

- UXPin Docs (Tier 1): "Downloading and Using UXPin" (https://www.uxpin.com/docs) — positioning, product lines, Mirror apps, SSO; "Interface | Editor" (https://www.uxpin.com/docs/editor/interface/) — editor anatomy, pages/sitemap, layers, groups; "Interactions | Editor" (https://www.uxpin.com/docs/editor/interactions/) — triggers, actions, animations, conditional interactions, if-else; "What is Wire" (https://www.uxpin.com/docs/wire/what-is-wire/) — AI product line generating working React apps; "Preview and Share" (https://www.uxpin.com/docs/sharing/preview-and-share/) — preview modes (Simulate/Comment/Spec/Documentation), share modal, password, embed.
- Justinmind Help Center (Tier 1): root (https://www.justinmind.com/support/) — section map; "Create your first project" (https://www.justinmind.com/support/start-prototyping-web-and-mobile-apps/) — workspace, screens, events, simulate, share, device preview.
- Moqups (Tier 2 only): homepage/product pages (https://moqups.com/) — positioning, three pillars, feature list. Help center (https://help.moqups.com/hc/en-us) failed with a transport error (1 attempt, abandoned per the network rule) — Moqups claims are held at product-page strength.
- Balsamiq (Tier 1): "What is Balsamiq?" (https://balsamiq.com/support/getting-started/what-is-balsamiq/).
- Overflow (Tier 2): homepage (https://overflow.io/) — positioning, three views, sync integrations.
- Cross-pass context (not re-fetched): research/interactive-prototype-builder.md (Figma, Axure RP, ProtoPie, Marvel — Tier 1, 2026-09-07); research/ui-design-application.md (Figma, Sketch, Penpot, Balsamiq — Tier 1, 2026-09-09).

## Product Observations

### UXPin (evidence layer A — Tier 1 official docs)

- Positioning: "UXPin is a code-based design tool that merges design and engineering into one unified process. Thanks to conditional interactions, variables, state-based animations, and powerful expressions, you can build prototypes that feel like the real thing. In other words, anything that's on the web can be accurately prototyped in UXPin."
- Product lines: main editor; **Merge** (code-backed components — docs section); **Forge** (AI system); **Wire** ("fully interactive, code-backed product flows… add logic, navigation, form behavior, and responsive layouts – then share the result as a hosted link"); design systems; dashboard.
- Editor anatomy: Toolbar (quick tools: shapes, pen, form elements, text, media, icons, **hotspot**, comments, search), Properties panel, Top bar (Design/**Documentation** modes; prototype name + **iteration** list; new iteration; Share; Preview on Device; Preview), Canvas, Bottom bar. Pages & Layers panel; **Sitemap** for switching pages; pages nestable; per-page canvas size; hide pages from preview/exports.
- Layers: boxes, shapes, text, **forms (Input, Text area, Checkbox, Radio, Select, Multi-select, Button)**, images, icons, **hotspots**, groups, components, video/audio. Layer filtering by type; search/replace fonts and colors.
- Interactions: "Take your prototype from static to motion… Create simple click-through mockups or fully animated prototypes." Interactions attach to **elements or the canvas**. **Element triggers**: Click/Tap, Double Click, Right Click, While Hovering, Mouse Down/Up, Over/Leave, Swipe (4 directions), Press and Hold, Release Hold, Focus, Focus Lost, Value Change, Option Select, State Change. **Canvas triggers**: Key Press, Scroll (to defined height), Page Load, Window Resize, Variable Change. **Actions**: Go to Page, Hide, Show, Toggle, Set State, Set Variable, Scroll to, Open URL, Go Back, **API Request (GET/POST)**, Move to/by, Opacity, Size, Color, Rotate, Bring to Front/Back, Next/Previous State, Focus, Enable/Disable, Check/Uncheck, Set Content, Play/Pause/Stop video. Animations: easing (Linear/Ease In/Out/InOut) with curve types, duration, delay, loop/count. **Conditional interactions**: if-then conditions (equals, greater, contains, starts/ends with, matches regex with ready-made patterns like Email/URL/Strong password, is empty, is true/false…), any/all condition matching, **if-else** chains (ordering rule: primary interaction must sit above the secondary). **Draft interactions** (broken references) flagged; invalid interactions highlighted red; interaction indicators (thunderbolt icons) on canvas and layers panel.
- Preview and Share: Preview mode with Sitemap navigation, adaptive-version toggles, zoom, interaction highlighting, full screen. Four preview modes: **Simulate** ("go through your design without any distractions"), **Comment** ("leave your feedback or look through comments from stakeholders"), **Spec** ("lets developers explore the design in detail"), **Documentation** ("a more detailed description with notes from your team about the design"). Share modal: link, per-stakeholder access toggles (Sitemap/Comments/Spec/Documentation), auto-highlight interactions, **password protection** (paid plans; force-password account default), **embed code** (iframe, live-updating). Device frames auto-matched to canvas size; touch cursor on touch devices. UXPin **Mirror** apps (iOS/Android) update live as the editor changes.
- **Wire** (AI product line): "Wire generates a working React app from your components or a text description. You interact with the result in the **Playground** — a live preview where you can click through flows, test forms, and check logic in real time." Code Editor with direct access to generated code; export as Vite + React app for developer handoff; builds saved with **Variants**; Wire Dashboard with Collections. "Wire can do more than clickable prototypes… you can create fully working apps with real logic, state management, and navigation." Example builds include an internal ticket system and a CRM pipeline. Positioned for: working flows, stakeholder sharing, code handoff, concept proofing.
- Enterprise posture: SAML SSO (individually configured), desktop apps on paid plans, two-device login limit, offline editing in desktop app with sync on reconnect.

### Justinmind (evidence layer A — Tier 1 help center)

- Positioning: "Welcome to Justinmind, the most powerful prototyping and design tool." Help-center training: "Go from zero to prototyping hero"; getting-started covers "how to create UI designs, wireframes, and prototypes"; advanced interactions "to test and validate usability"; business logic "design and test advanced user flows and validations".
- Project creation: new project → choose device (website, mobile, tablet, other) → cloud or local storage → device dimensions.
- Workspace palettes: **Toolbar** (shapes, images, text; '+' for dropdowns, hotspots, input fields), **Screens** ("Screens are similar to Artboards or Frames in other applications. Each screen contains its own Canvas and an entire project can contain many different screens, which you can link together using events"), **Canvas**, **Alignment**, **Properties** (styling, position, "visibility during simulation"), **Events** ("create interactions and turn wireframes into high-fi projects"), **Layers**, **Libraries** ("pre-styled elements… if you're prototyping for an Android phone, you'll find Android components displayed here by default"; more libraries; custom libraries).
- Editing: drag elements/widgets; Pen tool for vector shapes; images; **interactive inputs** ("pre-made Input widgets are automatically interactive. You can type into Input Text Fields, select values from Dropdowns, tick Check Boxes, and much more without adding any events").
- Linking: three ways — drag an element onto a target screen in the Screens palette (auto-creates **On Click + Navigate To** event); right-click → Navigate To (with optional transition); Events palette → Choose Trigger (e.g. Mouse → On Click) → Action (Navigate To) → target screen; also link to previously viewed screen or external URL.
- Simulate: Play button / F5 → simulation viewer in browser; top bar to navigate manually and change canvas size.
- Share: invite editors/viewers by email from the Cloud tab ("Can view"), shareable link, notification email; viewers review on mobile app or mobile browser.
- Device preview: Justinmind mobile app (iOS/Android); projects with interactivity intact.
- Help-center section map (capability evidence): Events and interactions; **Dynamic Panels**; Adding conditions to interactions; **Variables**; Scrolling content; Parallax; Forms and inputs; **Data visualization / data lists / data grids**; **Responsive Prototyping** (breakpoints, liquid layouts, pinned elements, percentage height/width); Templates and Masters; UI widget libraries; Collaboration (shared projects, feedback); Integrations (Adobe, Sketch, JIRA, TFS); API-SDK.
- Product nav (positioning evidence): Interaction design; UI design; Forms and data; **User flows ("Diagram user flows")**; Collaboration; **Requirements module**; **Design systems**; **Specifications**; use cases span Wireframing, Prototyping, Mockup, Web design, Mobile app design, **VR & AR design**.

### Moqups (evidence layer B/Tier 2 — product pages; help center unreachable)

- Positioning: "Online Mockup, Wireframe & UI Prototyping Tool… Wireframe, Diagram & Whiteboard Online. A simple and powerful visual collaboration solution for your whole team."
- Three pillars: **Wireframes & Mockups** ("Drag and drop easy-to-configure elements to take your UI and UX mockups from low to high fidelity"); **Diagrams & Flowcharts** ("sitemaps, org charts, storyboards, user flows, mindmaps, and UML diagrams"); **Interactive Prototypes** ("Create functional web and app prototypes by adding interactivity to UX wireframes and mockups. Simulate the user experience, present to stakeholders, and get final approval before handing off to developers"); plus real-time collaboration ("live-editing and online whiteboards").
- Workflow framing: "Jump effortlessly between diagrams, wireframes, mockups and prototypes… moving seamlessly from low-fidelity to high-fidelity… Create diagrams, wireframes and prototypes, in both low-fi and hi-fi, within a single app."
- Features: stencil kits (iOS, Android, Bootstrap), icon sets (Font Awesome, Material Design, Hawcons), image import ("Upload ready-made designs, and quickly convert them into interactive prototypes"), fonts/typography, object editing (Outline Panel, bulk-edit, groups, grids/rulers/guides), **Page Management** (folders, reorder, hide, **Master Pages** "automatically apply any changes to all associated pages").
- Audience: "Product Managers, Business Analysts, System Architects, Designers and Developers"; client-facing framing: "Validate ideas and clarify assumptions early in the game… Prove your concept by showing clients interactive prototypes of your vision."
- Ecosystem: Slack/Google Drive/Dropbox integrations; **Balsamiq import**; **webpage-to-wireframe extension** ("Turn webpages and AI layouts into fully editable mockups").

### Balsamiq (evidence layer A — Tier 1 help center)

- Self-label: "Balsamiq is a user interface design tool for creating wireframes (sometimes called mockups or low-fidelity prototypes). You can use it to generate digital sketches of your idea or concept for an application or website, and to facilitate discussion and understanding **before any code is written**. The completed wireframes can be used for **user testing, clarifying your vision, getting feedback from stakeholders, or getting approval to start development**."
- Product nav: Features; **Prototypes** (dedicated product page); Balsamiq AI; Wireframes. Use cases: For PMs, founders, consultants, IT.
- (Deeper mechanics — container grammar, AI drafting, one-click prototype generation, handoff surfaces — were documented in the ui-design-application pass's Tier 1/2 fetches of 2026-09-09 and are reused as cross-pass context: Space → Project (.bmpr) → Board → Wireframe; drag from component library or AI/screenshot drafting; "Select your screens and generate a clickable prototype"; share links, comments/reactions, embed in Jira/Confluence/Notion, export PNG/PDF, MCP server to AI coding tools; positioning "built for the part of the process where you're still figuring out what to build".)

### Overflow (evidence layer B/Tier 2 — boundary probe)

- Self-label: "User flow diagramming tool for design teams… Create interactive user flows, stunning design presentations, and step-by-step walkthroughs to engage your audience in synchronous or asynchronous design critique."
- Screens are **imported**: "Sync your work from design tools" (Figma, Sketch, Adobe XD, Photoshop) — "All original layers or prototyping links stay the same."
- Three views: **Canvas** (bird's-eye user-flow diagram of the user journey), **Prototype** ("screen-by-screen view… Interact with the out-of-the-box rapid prototype with your mouse or navigate with your arrow keys"), **Story** ("interactive, self-guided design walkthroughs… at their own pace").
- Surrounding machinery: publication links, embeds, comments ("asynchronous design critique"), boards, version history, feedback filtering by version, team folders.
- No in-tool screen authoring at the center — the value is the flow/presentation/critique layer over screens made elsewhere.

## Cross-product Comparison

| Aspect | UXPin | Justinmind | Moqups | Balsamiq | Overflow (probe) |
|---|---|---|---|---|---|
| Self-label | code-based design tool; "prototypes that feel like the real thing" | "prototyping and design tool" | "Mockup, Wireframe & UI Prototyping Tool" | "user interface design tool for creating wireframes (…low-fidelity prototypes)" | "user flow diagramming tool" |
| Central artifact | interactive prototype (code-backed realism) | interactive prototype project | wireframes + diagrams + prototypes in one app | wireframe board (+ clickable prototype derivative) | user-flow diagram + presentation over imported screens |
| Screen unit | Page (nestable, sitemap) | Screen ("like Artboards or Frames") | Page (folders, Master Pages) | Wireframe on a Board | imported screen node |
| Screen origin | drawn in-tool; Forge AI; Wire components | drawn in-tool; widget libraries | drawn in-tool; stencils; image import; webpage extension; AI layouts | drawn in-tool; component library; AI; screenshots | imported from Figma/Sketch/XD/Photoshop |
| Interactions | element + canvas triggers → ~30 action types; conditions; if-else; variables; expressions; API requests | events (trigger → action, e.g. On Click → Navigate To); conditions; variables; dynamic panels | "adding interactivity to UX wireframes and mockups" (mechanics not fetched) | clickable prototype generated from screens (one-click) | out-of-the-box rapid prototype view; arrow-key navigation |
| Run mode | Preview (Simulate mode); Mirror apps; device frames; touch cursor | Simulate (F5) in browser; mobile app | (implied by "Simulate the user experience") | Play the prototype | Prototype view; Story view |
| Fidelity ladder | Wire line (wireframing) ↔ main editor (hi-fi, code-backed) | "turn wireframes into high-fi projects" | "from low to high fidelity" in one app | intentionally low-fi only | n/a (screens made elsewhere) |
| UI libraries | form elements, icons, components, design systems, Merge code-backed | device-specific widget libraries (Android default), custom libraries | stencil kits (iOS/Android/Bootstrap), icon sets | UI-control component library (sketchy) | none (imports) |
| Flows | sitemap (page navigation) | user-flow diagramming (product nav) | user flows, sitemaps, flowcharts | not surfaced | the center (canvas view) |
| Feedback/approval | Comment mode; share modal with access toggles; password; embed | invite viewers/editors; share links; email notifications | comments "right on your designs"; real-time | share links, comments/reactions, embed | comments, publication links, feedback by version |
| Handoff | Spec mode; Documentation mode; Wire exports React code | specifications; requirements module; API-SDK; Jira/TFS | "get final approval before handing off to developers" | "approval to start development"; MCP to code tools | presentations as the handoff artifact |
| Logic depth | first-class (variables, conditions, expressions, states, API) | conditions, variables, dynamic panels, data lists/grids | not surfaced | none surfaced | none |
| Responsive | adaptive versions; auto-set preview; responsive mode (Merge) | responsive prototyping (breakpoints, liquid layouts) | not surfaced | not surfaced | not surfaced |
| Collaboration | avatars in top bar; comments | shared projects; editors/viewers | real-time co-editing; whiteboard | real-time comments/reactions | team folders; document editors |
| AI | Forge; Wire (working React apps); AI Focus mode | (not surfaced in fetched pages) | webpage/AI-layout import extension | Balsamiq AI drafting | none surfaced |
| Beyond-UI scope | — | VR & AR design use case | diagrams, whiteboard, UML, graphs | — | — |

## Canonical Abstraction

### L0 — Defining Invariant

**The honest structural finding: this leaf shares its population core with Interactive Prototype Builder.** No sampled product labeled "UX prototyping" lacks the four properties the interactive-prototype-builder pass established, and no property unique to this leaf could be validated as definitional. The four jointly-held properties of the shared core:

1. **The screen set** — the prototype is composed of discrete UI surfaces (pages / screens / wireframes on a board) staging the simulated experience; drawn in-tool, composed from UI libraries, imported, or AI-drafted. (Remove → no prototype exists.)
2. **User-defined interactions** — the author binds triggers (click/tap, hover, swipe, key, load…) to responses (navigate to another screen, show/hide, state change). (Remove → static mockup/wireframe drawing.)
3. **Run mode** — a playback surface where the simulation responds to input without authoring tools (browser viewer, device app). (Remove → an interaction spec, not an experienceable prototype.)
4. **Pre-implementation design-artifact posture** — the simulation stands in for the product to explore, communicate, and validate the design; it is never the deployed working software. (Remove → no-code application builder.)

**The center of gravity that makes this leaf distinct is not an additional structure but the role the core plays**: the prototype is the instrument of the pre-implementation validation loop — express the idea as screens (often wireframe-first) → link them into flows → simulate → share → collect feedback and tests → iterate → approve → hand off. The sampled products stake their identity on this loop, in their own words: "facilitate discussion and understanding before any code is written… user testing… getting approval to start development" (Balsamiq); "Simulate the user experience, present to stakeholders, and get final approval before handing off to developers… Validate ideas and clarify assumptions early" (Moqups); "test and validate usability… design and test advanced user flows and validations" (Justinmind); preview organized into Simulate / Comment / Spec / Documentation modes (UXPin). Removal test for the center of gravity: strip the validation loop (sharing, feedback, approval, handoff surfaces) and what remains is a simulation builder with no process role — still the sibling Type's artifact, but no longer the UX-process instrument this leaf names.

Jointly-held load-bearing checks: (1) alone = drawing/mockup canvas; (2) without (1) = interaction spec; (3) without (1)+(2) = slide deck; (4) without (1)–(3) = a process checklist with nothing to validate; (1)–(4) without the validation-loop emphasis = the Interactive Prototype Builder center of gravity.

### L1 — Common Mature Structure

Present across the sample (directly observed unless noted) but not definitional:

- **UI element/stencil libraries** — device- and platform-specific kits (Justinmind's Android-default libraries; Moqups' iOS/Android/Bootstrap stencils; UXPin's form elements/icons/components; Balsamiq's UI-control library).
- **The fidelity ladder in one artifact space** — wireframe → mockup → interactive prototype without switching tools (Moqups explicit "from low to high fidelity"; Justinmind "turn wireframes into high-fi projects"; Balsamiq wireframe → one-click clickable prototype; UXPin splits it across the Wire line and the main editor). 3–4 of 5 sampled; common, not definitional (UXPin's main editor is hi-fi-first).
- **Transitions/animations** with easing, duration, delay (UXPin documented in detail; Justinmind transition effects on links; sibling-pass products likewise).
- **Overlays / show-hide / state changes** (UXPin Show/Hide/Toggle/Set State; Justinmind Dynamic Panels; sibling-pass overlays).
- **Reusable components / masters / templates** (Justinmind Templates and Masters; Moqups Master Pages; UXPin components and design systems).
- **Flows and multi-path navigation** (Justinmind user-flow diagramming; Moqups user flows/sitemaps; UXPin sitemap; sibling-pass flow starting points).
- **Sharing with roles and feedback** — links, viewer/editor roles, comments, password protection, embeds (UXPin share modal; Justinmind share dialog; Moqups comments; Overflow publications).
- **Device preview** — mobile companion apps (UXPin Mirror; Justinmind app), device frames, touch cursors.
- **Responsive/adaptive prototyping** (UXPin adaptive versions; Justinmind responsive section; 2–3 of 5 directly evidenced — common-mature at market level).
- **Forms/data simulation** (Justinmind forms, data lists/grids; UXPin form elements, Set Content, API requests).
- **Logic depth** — variables, conditions, expressions (first-class in UXPin; present in Justinmind; advanced-tier in sibling-pass Figma; absent in Balsamiq/Moqups surfaced docs). Depth is a differentiator, not the definition.
- **Developer handoff surfaces** — spec mode (UXPin), specifications/requirements (Justinmind), design specs (sibling-pass Marvel), inspect modes (sibling-pass Figma/Sketch/Penpot).
- **Documentation/annotations** (UXPin Documentation mode; sibling-pass Axure notes; Justinmind requirements).
- **Iterations/versioning** (UXPin iteration list; Overflow version history).
- **Real-time collaboration** (Moqups, UXPin, Justinmind shared projects; single-user eras existed).

### L2 — Variant / Optional Structure

- **Realism posture** — code-backed components and production-grade rendering (UXPin Merge) vs intentionally sketchy low-fi (Balsamiq). A spectrum, not the definition.
- **Scope posture** — prototype-only specialist (Justinmind) vs early-stage all-in-one bundling diagrams/whiteboards (Moqups) vs mode-inside-a-design-suite (sibling-pass Figma).
- **Screen origin** — drawn in-tool vs imported/synced from design tools (Overflow, sibling-pass Marvel/ProtoPie) vs AI-drafted (UXPin Forge/Wire, Balsamiq AI, Moqups extension).
- **Input breadth** — touch/mouse basics vs sensors/voice/multi-device/hardware (sibling-pass ProtoPie pole).
- **Audience** — UX professionals vs "product people, not designers" (Balsamiq) vs enterprise design-system teams (UXPin Merge/SSO).
- **Substrate/deployment** — desktop app vs browser vs both; local vs cloud projects (Justinmind); self-hosting (sibling-pass Penpot).
- **Beyond-UI scope** — VR/AR prototyping (Justinmind use case), diagram/whiteboard bundling (Moqups).
- **Working-app generation** — AI-era products that generate running code from prototype intent (UXPin Wire's React apps). A deliberate boundary-crossing variant (see Boundary Findings #5).

### L3 — Vendor-specific Structure (research notes only)

- UXPin: Merge code-backed components; Forge AI + AI Focus mode; Wire builds/variants/collections and Playground; preview's four named modes (Simulate/Comment/Spec/Documentation); thunderbolt interaction indicators; draft-interaction flagging; if-else ordering rule (primary above secondary); ready-made regex conditions (Email, URL, Strong password); Power Duplicate with data refresh; scrubbable inputs; embed codes; force-password account default; SAML SSO setup flow; two-device limit; Mirror apps.
- Justinmind: Dynamic Panels; data lists/grids; requirements module; specifications; API-SDK; VR & AR use case; Sketch/Photoshop/XD integrations; Jira/TFS; local-vs-cloud project choice; F5 simulate; drag-to-screen auto-event creation.
- Moqups: Master Pages; Outline Panel; webpage-to-wireframe extension; Balsamiq import; named stencil/icon kits; "2,000,000 people" marketing claim.
- Balsamiq: Space/Project/Board/Wireframe grammar with .bmpr files; intentionally sketchy rendering rationale ("the team debates the idea, not the pixels"); Confluence/Jira/Desktop editions; MCP server; "0 day learning curve" positioning.
- Overflow: Canvas/Prototype/Story views; sync plugins; boards; publication links; feedback filtering by version; PROTOIO parentage.

### Rejected Findings

- **"UX prototyping means low-fidelity only"** — rejected: UXPin builds code-backed high-fidelity prototypes; Justinmind "turn wireframes into high-fi projects"; Axure (sibling pass) is high-fidelity. Fidelity is a spectrum posture (L2), not the definition.
- **"UX prototyping requires code-backed components"** — rejected: UXPin-specific realism posture (Merge); absent from Balsamiq/Moqups/Justinmind surfaced docs.
- **"UX prototyping tools must include user-flow diagramming"** — rejected: Balsamiq has none surfaced; UXPin's sitemap is navigation, not diagramming; common (Justinmind, Moqups) but not definitional.
- **"UX prototyping requires user-testing session modules"** — rejected: test-session machinery is an attached module (sibling-pass Marvel/ProtoPie); the sampled UX-prototyping products deliver validation through sharing/comments/approval surfaces, not test-session management.
- **"The prototype must be authored from screens made in the same tool"** — rejected: Overflow and sibling-pass Marvel/ProtoPie import screens; screen origin is an implementation choice.
- **"UX Prototyping and Interactive Prototype Building are different markets"** — rejected at the population level: the same products, the same four-property core, the same vocabulary ("prototyping tool"). The seam is center of gravity, not market structure.

### Historical / Market-Sample Check

- **Paper prototyping (pre-digital)** — the validation loop without the tool: sketches linked by hand, walked through with stakeholders. Lineage of the process emphasis; not the digital Type.
- **HyperCard (1987)** — stacks of cards, buttons linking cards, user mode vs editing mode: satisfies the four shared properties. ✓ (market-structure strength; consistent with the sibling pass's check)
- **Early Axure (2003+)** — pages + widgets + event/case/action interactions + browser preview: satisfies the core; process-oriented positioning from the start. ✓
- **InVision (2011–2024, discontinued)** — uploaded screens + hotspots + transitions + comments + user testing: the archetypal "UX prototyping platform"; validation loop was its identity. ✓ (background knowledge of the shutdown not re-verified; used only as a historical sample note)
- **POP-class paper-photo apps** — photos of sketches as screens, hotspots, phone playback: satisfies the core; proves screens need not be natively drawn. ✓
- Conclusion: the four-property core holds across eras, substrates, and fidelity poles; the validation-loop emphasis is era-stable (InVision's feedback machinery, Balsamiq's "before any code is written"). Nothing era-specific (cloud, real-time collaboration, AI, code-backed components) is definitional.

## Boundary Findings

1. **vs Interactive Prototype Builder — JOINT REVIEW DISCHARGED; keep-both RATIFIED on center-of-gravity grounds.** The two leaves share one population and one four-property core (screens, interactions, run mode, design-artifact posture); no clean market split exists — confirmed from this side by the sampled self-labeled "UX prototyping" products being structurally identical to the sibling pass's sample. The ratified seam: **this leaf centers the prototyping/validation process** (the idea→validated-design loop; early-stage and wireframe-first emphasis; feedback/approval/handoff surfaces as first-class), **that leaf centers the interactive simulation artifact itself** (behavior depth, input realism, run-mode fidelity — including specialist simulation-depth tools like ProtoPie-class). Products straddle; flagship tools span both centers in one file (Figma). This is the "keep-both with the fidelity/stage seam" outcome, stated as center of gravity; the "one-Type-two-emphases" alternative was considered and is recorded as the fallback reading if the directory ever merges the leaves.
2. **vs UI Design Application — RATIFIED from this side.** The ui-design pass's held hypothesis is confirmed: that Type centers the screen-design artifact of record (at any fidelity); this leaf centers the prototyping/validation process. Evidence: Balsamiq self-labels a "user interface design tool" while positioning entirely process-oriented — the straddle is real and is capability-embedded packaging, exactly as both prior passes recorded for merged products. Removal tests agree: strip prototyping from a UI design tool → still a UI design tool; strip the design-of-record polish machinery from a UX prototyping tool → still a UX prototyping tool.
3. **vs Collaborative Design Platform — RATIFIED keep-both.** That Type is defined by its collaboration structure (shared multi-user design files, subject-agnostic); this leaf by the prototyping process/artifact. Moqups straddles by packaging (a "visual collaboration solution" carrying wireframes + diagrams + prototypes) — the collaboration is the container, the prototyping is the capability. Single-user UX prototyping (early Axure, desktop Justinmind projects) remains fully in-type here without any shared-multi-user file.
4. **vs AI Design Generator — keep-both.** Generation-first production of designs (Uizard-class) vs process-first prototyping tooling. UX prototyping tools absorb AI as accelerators inside the process (UXPin Forge/Wire, Balsamiq AI, Moqups webpage/AI-layout import) without changing Type; the overlap (editable multi-screen output) is capability convergence, consistent with the ai-design-generator pass's framing.
5. **vs No-code Application Builder / Visual Website Builder — design-artifact posture is the seam; one deliberate boundary-crosser recorded.** A prototype simulates intended behavior with fabricated data and is never the deployed product; a no-code builder produces working software. **UXPin Wire is documented as crossing this seam deliberately**: it "generates a working React app", runs "fully working apps with real logic, state management, and navigation", and exports a Vite + React codebase. Recorded as a boundary case for the no-code/website-builder passes — market evidence that the seam is real and crossed on purpose (the Framer pattern again), not evidence against this Type.
6. **vs Digital Whiteboard / Diagramming Application** — free-form ideation canvases and generic process diagrams vs UI-specific screens + interactions + run mode. Moqups straddles by packaging (whiteboard + wireframes + prototypes in one app); a whiteboard's "connect frames and present" mode is static presentation, not input-driven simulation.
7. **vs User-flow diagramming tools (Overflow-class)** — adjacent. The flow/presentation/critique layer over screens made elsewhere, with no in-tool screen authoring at the center; its "prototype view" is navigation over imported screens. Sits between this leaf and Diagramming; recorded as a boundary pole, not a member of the sampled population.
8. **vs Presentation Application** — linear slide advancement vs input-driven simulation (consistent with the sibling pass's conclusion); Overflow's "Story view" is the closest straddle (self-guided walkthrough), still navigational rather than behavior-simulating.

## Uncertainties

- Moqups help center was unreachable (transport error, 1 attempt, abandoned); Moqups evidence is Tier 2 product pages only. Its prototyping mechanics (hotspot model, transition settings, logic) are **not** directly documented here; Moqups claims are held at positioning level.
- Balsamiq's clickable-prototype mechanics were not re-fetched this pass (the ui-design pass recorded a 403 on the UI-library docs page); its prototype claims are held at "generate a clickable prototype" strength, reusing that pass's Tier 1 context.
- Justinmind's user-flow diagramming, requirements module, and specifications are evidenced at feature-navigation level, not per-feature documentation; mechanics asserted only at capability level.
- The relative market weight of the two labels ("UX prototyping" vs "interactive prototype building") is not measurable from documentation; no claim made.
- UXPin Wire's working-app generation is treated as a boundary case; whether it represents a lasting product category (prototype-to-working-app) or a marketing posture is unresolved.
- InVision's shutdown is background knowledge, not re-verified from a live source; used only as a historical sample note.

## Final Synthesis

A UX Prototyping Application is the pre-implementation validation instrument of product design. Its world is built from the same four load-bearing structures as every interactive prototyping tool — a set of screens staging the experience, user-defined interactions binding triggers to responses, a run mode where the simulation is experienced, and the never-deployed design-artifact posture — but this leaf's identity lies in the role those structures play: the prototype is the instrument of the loop that turns a product idea into an approved design. The characteristic workflow runs: express the idea as screens (often wireframe-first, drawn from UI stencil libraries) → link screens into flows with interactions → simulate in a run mode → share with stakeholders → collect comments, feedback, and tests → iterate (versions/iterations) → approve → hand off to development (specs, documentation, or code). Around this loop, mature products converge on a standard structure: UI stencil/component libraries, the wireframe→high-fidelity ladder in one artifact space, transitions and overlays, reusable components/masters, flows, sharing with roles and comments, device preview, responsive prototyping, forms/data simulation, logic depth (variables/conditions/expressions), developer-handoff and documentation surfaces, and versioning. Products differentiate along realism posture (code-backed ↔ intentionally sketchy), scope (specialist ↔ all-in-one with diagrams/whiteboards), screen origin (authored ↔ imported ↔ AI-drafted), logic depth, audience, and substrate. The Type shares its population and core with the Interactive Prototype Builder leaf — the ratified seam is center of gravity (process/validation emphasis vs the simulation artifact itself) — and holds distinct centers against UI Design (artifact of record), collaborative design platforms (collaboration structure), AI generators (generation-first), no-code builders (deployed software), and whiteboards/diagramming (free-form or generic-process surfaces). Historical check passes: paper prototyping, HyperCard, early Axure, and the InVision generation all satisfy the core with the same process emphasis.
