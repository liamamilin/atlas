# Research Notes — Visual Note-taking Application

## Research Goal

Understand the Visual Note-taking Application as an Application Type: what the "board" is as a unit of record, what content lives on it, how spatial arrangement functions as organization, what mature products add, and where the boundary lies against the processed §03.02 siblings (note-taking-application, personal-knowledge-management-application, outliner) and against §03.05 (digital-whiteboard/collaborative-canvas, diagramming-application). This pass must discharge three pre-hung sibling flags (canvas/spatial-first vs text-first note-taking; vs link-network-first PKM; vs structure-first outliner) by center of gravity.

## Initial Boundary

- Hypothesis: a visual note-taking application is a personal knowledge tool whose primary working surface is a persistent free 2D board on which the user places authored content pieces and composes meaning through spatial arrangement.
- Closest confusions: (a) note-taking applications (list/library organization, text-first); (b) PKM applications (link network as the point); (c) outliners (indentation tree as the point); (d) digital whiteboards / collaborative canvases (multi-user co-marking team artifact); (e) diagramming applications (notation shapes + routed connectors); (f) mind-mapping products (structure-first auto-layout trees — no dedicated directory leaf exists); (g) presentation/slide tools (bounded ordered slides).
- Pre-hung flags to discharge: note-taking pass ("visual note-taking = canvas/sketch-first"); PKM pass ("canvas/spatial-first vs link-network-first; fix by center of gravity; Obsidian's Canvas is a PKM surface, not the Type center"); outliner pass (canvas-first vs structure-first).

## Research Questions

1. What is the unit of record — board, card, note, project? How do they relate?
2. Is spatial position user-controlled and meaningful, or computed from an underlying structure?
3. What content types are placed on boards, and who authors them?
4. How do connections (lines/arrows) and grouping containers work — auxiliary or semantic?
5. How do boards accumulate and organize (nesting, hierarchy, library)?
6. What is the capture-and-return loop (clipper, inbox, search)?
7. Personal vs shared: default posture, collaboration depth?
8. Where is the seam vs note-taking, PKM, outliner, whiteboard, diagramming, mind mapping?
9. What does the historical (paper-era) analog look like, and would it satisfy the definition?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Milanote | creative-project boards, template-driven, cloud | self-labels "visual note-taking app"; strong help center |
| Heptabase | learning/research cards on whiteboards | self-described "visual knowledge base"; YC labels it "the visual note-taking tool"; deep public wiki |
| Scapple | freeform connection web for writers, desktop one-time purchase | self-labels "freeform mind-mapping software" but freeform mechanics — bridge specimen |
| Curio | legacy-generation freeform project notebook, local-first | since-2002 lineage; richest feature surface; historical depth |
| MindNode | mind-map pole (boundary probe, not representative) | structure-first auto-layout tree + outline duality — tests the Type's edge |

## Sources

All fetched 2026-09-09 (layer A unless noted):

- Milanote — https://milanote.com/product/note-taking (product page, self-label "Free Visual Note-Taking App for Creatives"); https://milanote.com/guide (guide index); https://help.milanote.com/ (help center); https://help.milanote.com/en/collections/166826-adding-organizing-content (article list); https://help.milanote.com/en/articles/9860073-nesting-boards (full article)
- Heptabase — https://heptabase.com/ (product page); https://wiki.heptabase.com/ (public wiki index); https://wiki.heptabase.com/fundamental-elements (full article); https://www.ycombinator.com/companies/heptabase (title only, via wiki citation — "The visual note-taking tool for learning complex topics", layer B)
- Scapple — https://www.literatureandlatte.com/scapple (product page, full)
- Curio — https://zengobi.com/curio/ (product page + edition comparison, full)
- MindNode — https://www.mindnode.com/ (product page, boundary probe)

No numeric limits, plan gates, or default values were asserted from any source. MindNode evidence is positioning-level only (product page; support docs not fetched).

## Product Observations

### Milanote (layer A)

- Self-label (product page): "Free Visual Note-Taking App for Creatives"; "The top visual notes app for organizing ideas and creativity"; "Organize your notes into flexible visual boards."
- The anti-list seam in the vendor's own words: "Traditional notes apps separate your notes into silos accessed by tags and search terms. But Milanote is different. You can arrange your notes side by side on an infinite canvas to start seeing patterns and connections." Also: "Linear word documents are great for your final output, but on day one you need a flexible space to explore your ideas. Milanote's flexible drag and drop interface lets you arrange things in whatever way makes sense for your project."
- "Use lines and colours to add another layer of meaning." — connections as an added layer, not the base structure.
- Content types (help center article list): images, links, lines, tables (with formulas), drawing, synced notes, files, videos, to-do lists, map cards, documents, columns, audio, comments, color swatches.
- Board hierarchy (nesting boards article, full text): "Just like folders on your computer, boards can be placed inside of one another"; create a board inside a board or drag a board into another; breadcrumb "board navigation… shows the list of boards you navigated through to get to your current board"; sharing a board grants access to nested sub-boards and permission changes cascade; "Your home board is like the desktop on your computer. It's private—just for you"; boards shared with you land in the "Unsorted" column on your home board via "Save to Home".
- Organizing content collection: "Unsorted notes" (capture inbox), labels, locking an item to the board, moving content between boards, nesting boards.
- Navigation: zoom in/out, search, board shortcuts. Templates: custom templates.
- Posture: "Milanote boards are private by default, but with a few clicks you can share your notes with your team to collaborate, get feedback or ask for input." Web Clipper saves "text, images, videos or links to your boards from any website". Cloud sync, mobile/iPad/desktop apps.
- Audience (guide index): creative directors, filmmakers, photographers, marketers, designers; techniques: moodboarding, brainstorming, storyboarding, creative writing; also markets itself for note-taking, mind-mapping, whiteboarding use cases.

### Heptabase (layer A)

- Self-label (product page): "an intelligent, visual knowledge base built for students, researchers, and lifelong learners"; "Use whiteboards and cards to clarify your thinking and stay in flow." Y Combinator's company line (cited on the public wiki): "The visual note-taking tool for learning complex topics."
- Fundamental Elements (public wiki, full text):
  - **Card**: "A card is your note, as well as a container for knowledge and ideas. All cards are stored in the Card Library App." Card types: Note Cards, Journal Cards, Highlight Cards, plus imported PDF/Video/Audio/Image Cards. Card editor: `/` inserts blocks (headings, lists, to-dos, toggles, tables, images, audio, videos, files, PDFs, code, math, dates); `@` mentions other cards; block-level backlinks visible in the card's Info section; "These interconnected cards together form a knowledge network that belongs to you."
  - **Whiteboard**: "A whiteboard is your space for thinking. Consider it as an unlimited desktop for placing cards to help you learn and research the topics you care about." Sub-whiteboards for subtopics. "**Whiteboards do not own cards**. All cards belong to the Card Library… you can import related cards from the Card Library and place them on the whiteboard." "The same card can be placed on multiple whiteboards at the same time… If you click on a whiteboard name, it will automatically open the whiteboard and focus on the location of the card, allowing you to easily recall the thinking context of the card."
  - Whiteboard objects (right-click on blank space): cards, text, mind maps, journals, sections ("to group whiteboard objects"), sub-whiteboards. Toolbar: Select, Note card, Upload files, Connect ("Draw arrows to connect cards and other objects"), Text, Section, Search, plus Journal/Calendar/Mindmap/sub-whiteboard tools. Multi-select by drag box; per-object operations (color, mindmap mode, export, edit history, tags, move to other whiteboards).
- Other product-page capabilities: block-based editor, bi-directional links, PDF annotation, daily journals, web clipper, Zotero/Readwise integration, offline access, real-time collaboration ("Invite your friends and teammates"), search "over 10,000 notes in less than a second" (vendor claim, not asserted), AI Chat & Actions (era-current).
- Wiki workflow pages: organize knowledge & projects; capture in journal; learn & research a topic; write essays; read PDFs.

### Scapple (layer A)

- Self-label (product page): "Scapple: Freeform Mind-Mapping Software for Writers"; "Get your thoughts, musings and 3am brainwaves onto the page. Then join them up in any way you like."
- Paper anchor in the vendor's own words: "Ever scribbled ideas on a piece of paper and drawn lines between related thoughts? Then you already know what Scapple does. It's a virtual sheet of paper that lets you make notes anywhere and connect them using lines or arrows."
- Freeform mechanics: "Scapple doesn't force you to make connections—every note is equal, so it's up to you which notes have connections and which don't. You have complete freedom to experiment with how your ideas fit together."
- Operations: "Creating notes is as easy as double-clicking anywhere on the page; making connections between ideas is as simple as dragging and dropping one note onto another. And unlike real paper, in Scapple you can move notes around and never run out of space."
- Feature screenshots: "Write notes anywhere", "Connect notes using drag and drop", "Completely freeform", "Stack notes in columns of related ideas", "Create background shapes to group notes", "Customise the appearance of notes".
- More features: "Move and arrange notes easily", full screen mode, "Export or print your ideas", "Drag notes into Scrivener".
- Desktop (macOS/Windows), one-time purchase, no collaboration, no cloud in the documented core.

### Curio (layer A)

- Self-label (product page): "Capture More Than Notes. Gather your notes, research, and documents in Curio's intuitive, freeform notebook environment."
- Model: "Create a Curio project to represent a real-world project. Next, fill it with *everything* related to that project, including text notes, markdown, images, PDFs, documents, web links, multimedia, and much, much more." "Place this information *anywhere* on Curio's freeform idea spaces. Use Curio's integrated mind maps, lists, tables, index cards, albums, pinboards, and Kanban boards to organize your data into powerful collections and compositions."
- "Everything related to your project lives in a single local project file… on your Mac, under your control." (local-first pole)
- Structure above the canvas: hierarchical Organizer sections; metadata (tags, dates, percent complete, priority, rating, custom cross-references); search/Quick Find with queries; smart filters; query-based collections (Pro).
- Collections inside idea spaces: mind maps (multiple arrangements), lists, albums, index cards, tables, pinboards ("freeform collections of text and images"), stacks, kanban boards, compositions ("flexible, dynamically-sized arrangements of contained figures").
- Figures: rich text, markdown (with equations, code blocks, callouts), embedded/aliased files, images, PDFs (spread across idea spaces for annotation), audio/video recordings, YouTube embeds, SVG; brush/pen sketching; flowcharting shapes + sticky lines ("with numerous arrowhead choices"); figure layers (Pro).
- Idea space templates + figure stencils; presentation mode; PDF mirror export; import/export (text, markdown, image, PDF, HTML, CSV, OPML, mind-map formats); Curiota companion menu-bar app for quick capture ("quickly jot down ideas, take notes, or collect files when inspiration strikes").
- Customer-profile vocabulary (vendor-published quotes): "visual planner and thinker", "whiteboard idea space format", "corkboard of index cards… constellation of ideas", "most flexible idea board".
- Editions: Free (5 idea spaces) / Standard / Professional; subscription (Mac App Store) or one-time license key. macOS only.

### MindNode (layer B — positioning only, boundary probe)

- "MindNode helps you capture, connect, and evolve ideas visually as **mind maps** and **outlines**."
- "Capture, link, and expand ideas on an open canvas where every thought belongs." / "Switch between mind map and outline as structure emerges. Group, reorder, and connect thoughts until clarity takes shape."
- Native Apple apps, iCloud sync, tasks, 18+ years of refinement. Support docs not fetched — no operational claims drawn.

## Cross-product Comparison

| Dimension | Milanote | Heptabase | Scapple | Curio | MindNode (probe) |
|---|---|---|---|---|---|
| Unit of record | board (nesting, breadcrumbs, home board) | whiteboard (sub-whiteboards) + card library | document = "virtual sheet of paper" | project → idea spaces | mind map document |
| Content placed | notes/cards, images, files, links, to-dos, tables, video, audio, drawings | cards (note/journal/highlight/PDF/video/audio/image), text, mind maps, journals | text notes | figures: text, markdown, images, PDFs, files, web, audio/video, shapes | nodes (short text) |
| Position control | user drag-and-drop, "arrange things in whatever way makes sense" | user placement on "unlimited desktop" | "notes anywhere", "move notes around" | "place this information *anywhere*" | auto-layout from tree structure |
| Connections | lines ("another layer of meaning") | Connect tool (arrows) | drag note onto note; optional, "every note is equal" | sticky lines, relationship lines, flowchart shapes | branches (structural) |
| Grouping | columns, labels, nested boards | sections, sub-whiteboards | background shapes, stacked columns | compositions, pinboards, collections, Organizer sections | parent-child branches |
| Organization above canvas | board nesting + search + unsorted inbox | card library + tags/properties + nested whiteboards + tab groups | file-per-document | Organizer (hierarchical sections) + tags + queries | document list |
| Capture | web clipper, unsorted notes | web clipper, journals, Zotero/Readwise | none documented | Curiota companion, drag-in shelf | quick entry |
| Personal vs shared | private by default; share on demand | personal knowledge base; optional real-time collaboration | single-user | single-user, local file | personal (iCloud private) |
| Substrate | cloud | cloud + offline | local file | local project file | iCloud |
| Sketching | drawing tool (article) | not emphasized in fetched docs | none | brush/pen scribbles | none |
| Mind-map objects | markets a mind-mapping use case | mindmap objects + mindmap mode | self-labels mind mapping, freeform mechanics | mind maps as collections | the product IS a mind map |
| Export | (share links; files) | export files | export/print, drag into Scrivener | PDF/markdown/OPML/image/CSV…, PDF mirror | (docs not fetched) |
| Business model | freemium subscription | subscription trial | one-time purchase | freemium + subscription or license | subscription/freemium |

## Canonical Abstraction

### L0 — Defining Invariant (four jointly-held structures)

1. **The board as the unit of record** — a persistent, individually addressable free two-dimensional space (board / whiteboard / idea space / sheet) that the user keeps and returns to; boards accumulate as the user's working library and are commonly organized by nesting/containment. Remove → a list-of-notes application or a scratch surface with no memory.
2. **Authored content pieces placed freely on the board** — self-contained pieces of the user's own notes and materials (text notes/cards, images, files, links, sketches) placed at user-chosen positions; the content is authored/held by the user, not drawn from an application-supplied notation vocabulary. Remove → diagramming (notation shapes) or a bare drawing canvas.
3. **Spatial arrangement as the primary organization** — meaning is composed and read through placement: position, grouping containers (sections/background shapes/columns/compositions), and optional connecting lines carry the structure; the layout is the organization itself, not a rendering computed from an underlying list, tree, or database. Remove → note-taking (list organization) or structure-first mind mapping (tree-computed layout).
4. **Personal knowledge-notes posture** — the boards hold the individual's own accumulating notes and materials; private by default, with sharing/collaboration as a delegated capability rather than the co-creation default. Remove → digital-whiteboard / collaborative-canvas territory (multi-user co-marking team artifact).

Jointly-held is load-bearing: (1) alone = empty canvas; (2) without 1 = loose notes with no spatial home; (3) without 1+2 = a list-based note app; (4) without 1–3 = a shared team board; (1+2+3) without (4) = a whiteboard used alone.

### L1 — Common Mature Structure

- Content-type breadth on the board: images, files/PDFs, links/web content, to-do lists, tables, audio/video (Milanote article list; Curio figures; Heptabase card types).
- Connecting lines/arrows between pieces (Milanote Lines; Heptabase Connect; Scapple drag-to-connect; Curio sticky lines) — present in all four, always as an added layer over free placement.
- Grouping containers: sections, background shapes, columns, compositions, pinboards (all four).
- Board hierarchy: nesting boards / sub-whiteboards / Organizer sections (Milanote, Heptabase, Curio; Scapple = file-per-document instead).
- Capture surfaces: web clipper (Milanote, Heptabase), quick-capture inbox/companion (Milanote unsorted notes, Curio Curiota), journals (Heptabase).
- Library-level retrieval: search across boards/cards (Milanote, Heptabase, Curio), tags/labels/properties (Milanote labels, Heptabase tags, Curio tags/metadata).
- Templates (Milanote custom templates, Curio idea-space templates/stencils).
- Zoom/pan navigation with orientation aids (Milanote zoom + breadcrumbs, Curio navigator).
- Export/print/share outputs (Scapple export/print, Curio PDF/markdown/OPML, Milanote share links).
- Rich text / markdown editing inside pieces (all four).
- Multi-device sync (Milanote cloud, Heptabase offline+sync, MindNode iCloud) — Curio/Scapple local-first poles lack it → common, not definitional.

### L2 — Variant / Optional Structure

- Storage substrate: cloud service (Milanote, Heptabase) vs local file (Scapple document, Curio project file).
- Purpose polarity: creative project boards (Milanote) vs learning/research (Heptabase) vs writing/thinking (Scapple, Curio) vs personal productivity (MindNode probe).
- Collaboration depth: none (Scapple, Curio) → share-for-comment (Milanote) → real-time co-editing (Heptabase).
- Business model: freemium subscription (Milanote, Heptabase) vs one-time purchase (Scapple; Curio license-key option).
- Platform: web + apps (Milanote, Heptabase) vs desktop-native (Scapple, Curio).
- Structured organizers inside the canvas: mind-map objects/modes (Heptabase, Curio), kanban stacks/tables (Curio, Milanote columns/to-dos) — freeform canvas remains the primary surface.
- AI assistance (Heptabase AI Chat & Actions; Curio AI services/Sleuth) — era-current.
- Freehand sketching/drawing (Milanote drawing, Curio scribbles) — optional; absent from Scapple and not emphasized by Heptabase.

### L3 — Vendor-specific (research notes only)

- Heptabase's Card Library ownership model: whiteboards do not own cards; the same card can be placed on multiple whiteboards simultaneously; clicking a whiteboard name in a card's Info focuses the card's position ("recall the thinking context").
- Milanote's home board ("like the desktop on your computer… private—just for you") with an "Unsorted" column and "Save to Home" for boards shared with you; synced notes (one note instance synced across boards); map cards.
- Curio's Organizer/figures/stencils/Sleuth research window/queries/smart kanban/PDF mirror/Curiota companion; edition ladder (Free = 5 idea spaces).
- Scapple's Scrivener drag-in (sibling-product handoff within the same vendor).
- MindNode's mind-map↔outline duality and Apple-native/iCloud posture.

### Rejected Findings (anti-overfit)

- **Freehand sketching is NOT definitional.** The sibling passes' "canvas/sketch-first" framing is only half right: Scapple (a core sample) has no drawing at all, and Heptabase's fetched docs do not emphasize freehand. The invariant is *arrangement*; sketching is a common-optional content type.
- **"Infinite/zoomable canvas" is a common realization, not the invariant.** All four sampled products have unbounded/zoomable surfaces, but a bounded freeform page (scrapbook/mood-board page) would still satisfy the core; unboundedness is the dominant realization of free placement, not the definition. (Contrast: the digital-whiteboard pass likewise held "literal infinite canvas" as not definitional.)
- **Connections are NOT the defining structure.** Lines/arrows exist in all four products but are consistently documented as an added layer ("another layer of meaning" — Milanote; "doesn't force you to make connections" — Scapple). Making the link network the point is PKM's center, not this Type's.
- **Auto-layout mind mapping is NOT this Type's center.** MindNode's layout is computed from the tree structure and switches to a plain outline — structure-first, not arrangement-first. Held boundary-adjacent (see Boundary Findings).
- **Collaboration is NOT definitional.** Two of four sampled products have none; the personal posture is the constant.
- **Cloud sync, AI, templates, clippers, tags** — all standard-or-optional, none definitional (Scapple/Curio poles satisfy the core without them).

### Historical / Market-Sample Check

Passed. The paper-era analogs satisfy all four legs at analog level: a writer's corkboard of index cards (persistent boards, authored pieces, arrangement as organization, personal), a mood board or scrapbook page, sticky notes on a wall, a hand-drawn mind map or concept sketch on paper. Scapple's own copy anchors the lineage ("Ever scribbled ideas on a piece of paper and drawn lines between related thoughts? Then you already know what Scapple does. It's a virtual sheet of paper…"), and a vendor-published Curio customer quote uses the corkboard metaphor ("A corkboard of index cards is a nice way to build a constellation of ideas"). Curio itself documents a since-2002 lineage (customer quotes from 2005–2011 on the current product page). No cloud, AI, templates, clippers, or infinite-canvas machinery is required by the definition.

## Boundary Findings

1. **vs note-taking-application (§03.02, processed) — keep-both RATIFIED, flag discharged.** Note-taking organizes a personal library of note records through containers/tags/search, with the note as a document-like record in a list; visual note-taking makes the spatial arrangement itself the primary organization. The sharpest evidence is the vendor's own contrast (Milanote: "Traditional notes apps separate your notes into silos accessed by tags and search terms. But Milanote is different. You can arrange your notes side by side on an infinite canvas…"). Removal tests: remove spatial-arrangement-as-organization → note-taking; make arrangement the point → visual note-taking. Straddle zone: note apps whose pages are freeform canvases (OneNote-class; the note-taking pass itself listed "freeform canvas" as one note-format variant) — resolved by center of gravity: if the product's promise is the personal note library retrieved by browse/search, it is note-taking; if the promise is composing meaning by arranging pieces in a shared visual space, it is visual note-taking.
2. **vs personal-knowledge-management-application (§03.02, processed) — keep-both RATIFIED, flag discharged.** PKM's defining structure is the user-built cross-note link network (connections as the point, network growth over time); this Type's defining structure is the spatial arrangement (placement/grouping as the point). Heptabase straddles by marketing (bi-directional links + whiteboards; "knowledge network" copy), but its own operational docs make the whiteboard the thinking space and the card library the store, with links a card-level capability — center of gravity: visual note-taking (corroborated by YC's "visual note-taking tool" label). Obsidian's Canvas is consistent with the PKM pass's ruling: canvas placement there is a PKM surface, not a Type center — a canvas feature inside a link-network product does not move the product into this Type.
3. **vs outliner (§03.02, processed) — keep-both, flag discharged.** The outliner's point is the indentation tree operated on directly (subtree operations); this Type's point is 2D placement of free pieces. Mind-map-mode products that switch between tree and map (MindNode) straddle the two — held boundary-adjacent, not variants of either Type.
4. **vs digital-whiteboard / collaborative-canvas (§03.05, processed) — keep-both.** The whiteboard's defining core is multi-user co-marking converging into one auto-preserved team artifact; this Type is personal knowledge notes, private by default, with sharing delegated. Milanote's own copy polices the seam ("Milanote boards are private by default, but with a few clicks you can share your notes with your team"). Surface mechanics overlap (free placement, stickies, lines); the unit-of-work and posture differ (team session/board vs personal accumulating library).
5. **vs diagramming-application (§03.05, processed) — consistent with that pass's own boundary.** Diagramming's artifact is the shape+connector graph with notation semantics and routed connectors; here the artifact is authored heterogeneous content pieces with connections auxiliary. Heptabase/Curio ship mind-map/flowchart objects inside the canvas as structured organizers — packaging, not identity.
6. **Mind mapping — taxonomy observation, flagged for directory review.** Mind-map-first products (MindNode/XMind class) form a distinct product population: structure-first (tree with auto-layout, outline duality). The directory has no mind-mapping leaf; this pass holds that population boundary-adjacent (between this Type, outliner, and diagramming) rather than claiming it as a variant, because the defining mechanics (computed layout from tree structure) contradict leg 3. Freeform-canvas products with mind-map vocabulary (Scapple self-labels "freeform mind-mapping software") ARE in-type — the vocabulary is inherited, the mechanics are arrangement-first.
7. **vs wiki-application / knowledge-base-application (§02.06, processed)** — consistent with the PKM pass's note: org-governed shared article corpus vs personal self-governed boards; no seam pressure observed.
8. **vs bookmark-manager / read-it-later (§02.13, processed)** — external-resource records vs authored units; the web clipper is the hinge (clippers bring external material INTO boards as content pieces, per Milanote/Heptabase).
9. **Notion-class workspace** — straddle consistent with the note-taking pass's flag; not sampled; no claims drawn.
10. **Handwriting/ink note apps (GoodNotes/Notability class)** — not sampled; provisionally held as ink-substrate note-taking (page/notebook organization), not this Type, because the point is handwriting on pages rather than spatial arrangement of pieces. Recorded as an uncertainty, not a claim.

## Uncertainties

- MindNode operational docs not fetched — mind-map pole characterized at positioning level only; no behavioral claims drawn.
- Kinopio and other indie spatial tools not sampled (small population; not needed for stop conditions).
- Handwriting-first apps unexamined (see Boundary Finding 10).
- Milanote "synced notes" (one note instance synced across boards) read only from the help-center article title — not characterized.
- Exact numeric limits (board sizes, item counts, plan gates) deliberately not asserted from any source.
- Heptabase's drawing/ink support not confirmed from fetched docs — recorded as unknown rather than claimed.

## Final Synthesis

The Visual Note-taking Application is defined by four jointly-held structures: a persistent free 2D board as the unit of record; the user's own authored content pieces placed freely on it; spatial arrangement (position, grouping, optional connecting lines) as the primary organization rather than a rendering of an underlying list or tree; and a personal knowledge-notes posture (private by default, sharing delegated). Everything else modern products carry — content-type breadth, clippers, search, templates, nesting, sync, collaboration, AI, sketching, infinite zoom — is standard or optional structure. The Type's center of gravity is composing and reading meaning through arrangement; remove arrangement-as-organization and it collapses into note-taking; make connections the point and it becomes PKM; make the tree the point and it becomes an outliner/mind mapper; make co-marking the point and it becomes a digital whiteboard; make notation shapes the point and it becomes diagramming.
