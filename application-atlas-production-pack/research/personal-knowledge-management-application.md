# Research Notes — Personal Knowledge Management Application

Research date: 2026-09-08
Directory leaf: "Personal Knowledge Management Application" (§03.02 Notes & Personal Knowledge)
Slug: personal-knowledge-management-application

Incoming obligations: (1) note-taking-application pass left the PKM boundary for joint treatment — proposed discriminator: note-taking's promise = capture + retrieve individual notes; PKM's promise = grow a connected network of notes (links/backlinks/graph as the point). (2) outliner pass left a NEW JOINT REVIEW RECOMMENDED — PKM's center = growing connected note network vs outliner's tree-as-the-point; Roam and Logseq straddle both; seam to be fixed by center of gravity. Both are discharged in this pass (see Boundary Findings and STATUS.md).

## Research Goal

Understand the Personal Knowledge Management Application as an Application Type, distinct from the already-documented Note-taking Application: what the "knowledge unit" is, how links between units work, whether the network itself is a first-class object, what the user's development loop looks like, what mature products add, and where the boundaries lie against note-taking, outliner, visual note-taking, wikis/knowledge bases, mind mapping, bookmark/read-later, reference managers, and workspace products.

## Initial Boundary

Working hypothesis at start:

- Core: an individual deliberately builds a network of connected notes; links between notes are created while writing; the accumulated link structure is navigable and inspectable (follow links, see backlinks/connections/graph); the point is knowledge that compounds over time — the network is the asset, not the shelf of notes.
- Primary users: individuals whose work is thinking/writing/learning — knowledge workers, researchers, students, writers, consultants; a team/enterprise pole exists in at least one product.
- Nearest confusions: Note-taking Application (closest sibling — capture/retrieve loop, links optional), Outliner (tree-as-the-point), Visual Note-taking Application (canvas-first), Wiki/Knowledge Base (org-governed corpus), Diagramming/Whiteboard (drawn diagrams vs emergent note network), Bookmark Manager/Read-it-later (external resources), Reference Manager (citation-centric), Team Workspace (org containers), Knowledge Graph Explorer (enterprise data systems).
- Unknowns at start: whether backlinks/graph views are definitional or modern UI over an older network concept; whether the historical personal-wiki family (pre-backlink-pane era) satisfies a modern definition; whether block-level references or typed links are structural (suspected: no).

## Research Questions

1. What is the unit of record — note/tiddler/thought — and how does it relate to the note-taking note?
2. How are connections made: link syntax, while-writing autocomplete, CamelCase, typed links?
3. Is the connection structure inspectable and navigable: backlinks, graph/network views, orphans?
4. What is the development loop: capture → link → revisit → refine → reuse → publish?
5. What organization exists beside links (tags, folders) and what role do containers play vs note-taking?
6. What is the storage/ownership philosophy (local files vs cloud vs self-contained file)?
7. What reuse machinery exists (transclusion, embedding, canvas placement, publishing)?
8. How do AI features enter (era-current)?
9. Historical check: do personal wikis / single-file web notebooks / long-lived associative-network products satisfy the definition without modern UI?
10. Boundary fixes: vs note-taking (discharge), vs outliner (discharge), and forward notes for visual note-taking and other neighbors.

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer layers:

| Product | Philosophy / position | Customer layer | Evidence tier reached |
|---|---|---|---|
| Obsidian | local-first plain-text Markdown files; links/graph as headline; plugin ecosystem | individual prosumer (enterprise offering exists) | Tier 2 (rich product page; help site SPA unreachable) |
| TheBrain | associative "visual knowledge network" (28+ years self-claimed); cloud app; personal → teams | individual → enterprise (TeamBrain) | Tier 2 (rich product page + support page; user-guide PDF >5MB unreachable) |
| TiddlyWiki | self-contained single-file "non-linear personal web notebook"; wiki-text linking; own-your-file | individual / self-hosters | Tier 1 (official static docs pages) |
| Roam Research | cloud outliner-flavored "note taking tool for networked thought" | individual prosumer | positioning only (site JS-locked; title/tagline fetched) |
| Logseq | open-source, privacy-first "knowledge base"; outliner + journals | individual (open-source community) | positioning only (site JS-locked; docs oversized ×3 across passes) |

Roam and Logseq were attempted again in this pass (per the outliner pass's shared limitation) and remain unreachable beyond their taglines. No operational claims are drawn from either; they are used as market-positioning witnesses only.

## Sources

- Obsidian — product site: https://obsidian.md/ (fetched 2026-09-08; rich: links/graph/canvas/plugins/sync/publish, note UI showing backlink count)
- Obsidian — help site: https://help.obsidian.md/ and https://help.obsidian.md/Linking+notes+and+files/Internal+links (both fetched 2026-09-08; title only — SPA, content not readable)
- TheBrain — product site: https://www.thebrain.com/ (fetched 2026-09-08; rich: visual knowledge network positioning, capture/connect/find/AI, views, personal→teams)
- TheBrain — support: https://www.thebrain.com/support (fetched 2026-09-08; knowledgebase is a JS app; TheBrain 14 User Guide PDF https://assets.thebrain.com/documents/TheBrain14/TheBrain14-User-Guide-v01.pdf exceeds fetch size limit)
- TiddlyWiki — https://tiddlywiki.com/ (exceeds fetch size limit — the product IS a single self-contained HTML file) ; static representation fetched 2026-09-08: GettingStarted (https://tiddlywiki.com/static/GettingStarted.html), Tiddlers (https://tiddlywiki.com/static/Tiddlers.html), WikiText (https://tiddlywiki.com/static/WikiText.html), Tags (https://tiddlywiki.com/static/Tags.html), Linking in WikiText (https://tiddlywiki.com/static/Linking%2520in%2520WikiText.html) — official docs, Tier 1
- Roam Research — https://roamresearch.com/ (fetched 2026-09-08; title/tagline only: "A note taking tool for networked thought.")
- Logseq — https://logseq.com/ (fetched 2026-09-08; title only: "A privacy-first, open-source knowledge base") ; https://docs.logseq.com/ (exceeds fetch size limit; consistent with the outliner pass's oversized ×2 record — now ×3)

**Source-access limitations.** (1) Roam and Logseq operational documentation unreachable — no feature or workflow claims rest on them; they witness market positioning only. (2) Obsidian help site not readable (SPA) — Obsidian evidence is product-page claims, which are unusually explicit about linking, graph, backlink display, storage, and publishing. (3) TheBrain user-guide PDF exceeds fetch limits — TheBrain evidence is product-page claims; its internal link semantics (link types etc.) are NOT asserted. (4) TiddlyWiki's main site exceeds fetch limits by design (single-file product); its official static documentation pages are fully readable and serve as the Tier-1 evidence for the personal-wiki pole. (5) No precise numeric limits, plan details, or pricing were researched anywhere and are not asserted (one marketing-figure exception noted in observations below, kept in Research Notes only).

## Product Observations

Evidence layers: **A** = directly observed on that product's official documentation/surfaces; **B** = cross-product commonality; **C** = canonical inference.

### Obsidian (evidence: A on product-page claims)

- Positioning: "Sharpen your thinking. The free and flexible app for your private thoughts." Demo vault graph shows notes such as "Evergreen notes", "Writing is telepathy", "Daily", "Ideas", "References".
- **Links as headline**: "Links — Create connections between your notes. Link anything and everything — ideas, people, places, books, and beyond. Invent your own personal Wikipedia." Demo shows inline autocomplete while typing `[[thin` surfacing candidate note titles ("I think therefore I am", "Thinking, Fast and Slow", "The Thing").
- **Backlinks surfaced in the note UI**: demo note shows "1 backlink 206 words 1139 char" — connection visibility is rendered on the note itself.
- **Graph view**: "Visualize the relationships between your notes. Find hidden patterns in your thinking through a visually engaging and interactive graph."
- **Canvas**: "An infinite space to research, brainstorm, diagram, and lay out your ideas" — visual surface alongside notes (demo: philosophy topic with embedded note content and images).
- Tags in demo (`#evergreen`, `#projects #travel`); "Daily" node in demo graph (daily notes); community plugins include "Calendar — view of your daily notes", Outliner, Kanban, Tasks, Dataview.
- Storage/ownership: "Obsidian stores notes privately on your device… No one else can read them, not even us." "Obsidian uses open file formats, so you're never locked in." (Storage as local plain-text Markdown files is stated on the page and was also recorded by the note-taking pass.)
- Sync (paid add-on): E2EE, selective sync, shared vaults (invite by email, roles), version history (one year — marketing figure, Research Notes only).
- Publish (paid add-on): "Turn your notes into an online wiki, knowledge base, documentation, or digital garden… make it easy for readers to explore your web of ideas."
- Web Clipper offered (nav + "Get Obsidian Web Clipper" surface).
- Extensibility: "thousands of plugins and themes… shape Obsidian to fit your way of thinking"; open API for plugins.

### TheBrain (evidence: A on product-page claims)

- Positioning: "Stop filing your ideas. Start connecting them." "TheBrain brings notes, files, links, projects, and AI into one visual knowledge network — so you can see relationships, find anything, and think with full context."
- Anti-filing thesis stated verbatim: "Most apps force your knowledge into folders, pages, or isolated notes… The same idea belongs to a project, person, file, and future decision. TheBrain lets every idea live in every context where it matters — without duplication, silos, or folder compromise."
- Connect: "Link thoughts across projects, topics, people, timelines, and outcomes so your knowledge gains meaning."
- Find: "Search your Brain and return to the complete context: notes, files, links, people, and connected ideas."
- Capture: "Notes, files, links, web pages, research, meetings, ideas, and plans all live in one visual workspace."
- Views: Card View, Mind Map, and Tree View — "explore your knowledge from every angle."
- AI (era-current): Cerebro — "summarize, create, search, suggest links, and build with your own knowledge"; "surface related ideas, suggest links".
- Customer span: "From personal thinking to enterprise knowledge" — Personal Knowledge / Projects / Research / Teams (TeamBrain, shared knowledge networks); enterprise customers displayed (logo wall); self-claimed longevity "28+ years evolving, 10M+ downloads, 180 countries".
- Free desktop tier claim ("Now completely free on your desktop") — marketing figure, Research Notes only.

### TiddlyWiki (evidence: A — Tier 1 official static docs)

- Self-description (site title on every docs page): "TiddlyWiki v5.4.1 — a non-linear personal web notebook."
- **Unit of record**: "Tiddlers are the fundamental units of information in TiddlyWiki. Tiddlers work best when they are as small as possible so that they can be reused by weaving them together in different ways." "Other systems have analogous concepts with generic names like 'items', 'entries', 'entities', 'nodes' or 'records'." Internally "a list of uniquely named values called fields"; the only required field is `title`.
- **Linking is core**: "A key capability of WikiText is the ability to make links to other tiddlers or to external websites." Manual `[[Tiddler Title]]` links; CamelCase titles auto-link while typing; editor toolbar "link" button with search-and-select; external links; anchor links within tiddlers. WikiText self-described as "designed to be familiar for users of Markdown but with more of a focus on linking and the interactive features."
- **Reuse machinery**: Transclusion ("Transclusion in WikiText" is core WikiText) — embedding tiddler content into other tiddlers.
- Tags: "Tags are used to organise tiddlers into categories."
- Delivery/ownership: one self-contained HTML file you download and save ("Download an empty copy"; saving methods listed per platform/browser, e.g. Tiddlyhost community hosting); explicit warning not to use the browser File/Save menu.
- Getting started page documents the save-method ecosystem (Tiddlyhost account, per-platform saving options).

### Roam Research (evidence: positioning only)

- Tagline fetched: "A note taking tool for networked thought." Site is JS-locked; no operational docs readable. Used only as a market-positioning witness for the networked-thought category (consistent with the outliner pass's limitation record).

### Logseq (evidence: positioning only)

- Title fetched: "A privacy-first, open-source knowledge base." Site JS-locked; docs oversized across three attempts (two in the outliner pass, one here). Used only as a market-positioning witness (open-source, privacy-first knowledge-base framing).

## Cross-product Comparison

| Capability | Obsidian | TheBrain | TiddlyWiki | Roam | Logseq |
|---|---|---|---|---|---|
| Knowledge unit as persistent individually-addressable record | A (notes, local md) | A (thoughts + notes) | A (tiddlers, required title field) | positioning only | positioning only |
| User-created links between units | A (headline; `[[` autocomplete) | A ("link thoughts"; visual network) | A (core WikiText; `[[title]]`, CamelCase) | positioning only ("networked thought") | positioning only |
| Connection visibility / network inspection | A (backlink count in note UI; graph view) | A (visual knowledge network; "see relationships") | partial (links + navigation evidenced; backlink pane not evidenced) | not reachable | not reachable |
| Link-while-writing (authoring and linking are one act) | A (`[[` autocomplete demo) | not explicit on page (connect is a primary verb) | A (CamelCase auto-link while typing; toolbar link with search) | not reachable | not reachable |
| Tags/categories | A (#tags in demo) | not explicit on page | A (Tags doc) | not reachable | not reachable |
| Search across the library | implied (not explicit on page) | A ("Search your Brain… return to the complete context") | not evidenced on fetched pages | not reachable | not reachable |
| Graph/network visualization | A (graph view) | A (visual network; mind-map view) | not evidenced | not reachable | not reachable |
| Visual/canvas surface | A (Canvas) | A (mind-map/tree/card views) | not evidenced | not reachable | not reachable |
| Transclusion / embedding reuse | partial (canvas embeds demo) | partial (files/notes in one workspace) | A (transclusion core) | not reachable | not reachable |
| Daily-note / journaling pattern | A ("Daily" node; calendar community plugin) | not explicit on page (personal knowledge includes daily notes listed as use case) | not evidenced | not reachable | positioning only |
| Capture surfaces (clipper) | A (Web Clipper) | A (capture anything: files, web pages…) | not evidenced on fetched pages | not reachable | not reachable |
| Multi-device / sync | A (Sync add-on, E2EE) | A (cloud app, mobile) | A (saving methods incl. Tiddlyhost) | not reachable | positioning only |
| Sharing / collaboration / publishing | A (shared vaults; Publish → wiki/KB/digital garden) | A (TeamBrain shared networks) | A (Tiddlyhost hosting; publish by hosting the file) | not reachable | positioning only |
| AI layer (era-current) | not claimed on page | A (Cerebro: suggest links, summarize) | not claimed | not reachable | not reachable |
| Storage/ownership posture | local open-format files (A) | cloud/proprietary app (A) | single self-owned HTML file (A) | unknown | open-source claim (positioning) |
| Extensibility | A (plugins, open API) | not claimed on page | A (WikiText macros/widgets core) | unknown | open-source claim |

Reading of the table: the first three rows are the stable core across every product with readable evidence — knowledge units, user-built links, and (where UI evidence exists) connection visibility. Everything else varies. Note the deliberate asymmetry: TiddlyWiki proves the core WITHOUT graph views and backlink panes (the wiki's link-following navigation is the connection surface); Obsidian and TheBrain prove connection visibility as modern UI. The core therefore cannot require a specific backlink UI.

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures, plus the center of gravity that separates this Type from note-taking:

1. **Knowledge notes as the unit of record.** Persistent, individually addressable, user-authored units of content (notes / tiddlers / thoughts) — text-centric, optionally embedding media and files. (Remove → no PKM; without units there is nothing to connect.)
2. **The user-built link network.** The user connects notes to notes by creating links between them while authoring; the links persist and accumulate across the library into a web of connections that is a structure of its own — the network is not merely a navigation aid but the product's principal organization. (Remove → a note-taking application with an unconnected library.)
3. **The network is navigable and inspectable.** The user can move through the library by following links from note to note, and can see a note's place in the web — its connections. Implementations range from backlink displays and interactive graph views (modern) to link-following navigation and category/tag weaving (older wiki form). (Remove → links as inert inline text; the product is then a note app with hyperlinks, not a knowledge network.)

Center of gravity (the discriminator that separates PKM from note-taking, which shares structure 1): the point of the product is **growing the web as a personal knowledge asset** — connecting, revisiting, and refining ideas so knowledge compounds over time — rather than capturing and retrieving individual notes.

Jointly-held is load-bearing:

- 1 alone = note-taking (capture-and-return loop over a personal library)
- 2 without 1 = concept/mind-mapping territory (nodes with labels, no persistent authored content)
- 1+2 without 3 = a note application with inline hyperlinks (the straddle zone several products occupy on the way in; without connection visibility the network is never an object)
- 2+3 without 1 = an empty graph — a diagram, not knowledge

### Historical / market-sample check

Would older, regional, platform-native, or differently positioned products still fit?

- **TiddlyWiki (single-file personal web notebook, mid-2000s lineage, still current)**: satisfies all three legs with zero modern UI — tiddlers (small reusable units, uniquely titled), core wiki-text linking between tiddlers while writing, navigation by following links ("non-linear" is the product's own self-description). No backlink pane, no graph view, no cloud sync required. Fits.
- **TheBrain's 28-year lineage (self-claimed)**: an associative visual knowledge network predating the modern Markdown-linking wave; the filing-vs-connecting thesis is the product's own founding frame. Fits.
- **Paper Zettelkasten (conceptual ancestor, analog)**: numbered slips with explicit cross-references written on each slip, navigated by following references — notes + user-built links + connection visibility (references readable on the slip), with the explicit purpose of compounding knowledge. Fits at the analog level; cited as reasoning, not product evidence.
- **Personal wiki family generally (self-hosted personal wikis)**: fits the wiki-link core; not separately sampled in this pass (TiddlyWiki is its clearest self-described member: "personal web notebook").
- **Modern cloud/AI-era products**: fit with sync, publishing, and AI as era-current layers.

Conclusion: the L0 holds across eras and storage models. No graph view, no backlink pane, no Markdown, no bidirectional-link UI, no daily notes, no cloud, no AI belongs in the definition. The one modern-implementation pattern deliberately EXCLUDED from L0: the backlink pane (it is the current dominant implementation of "connection visibility", not the invariant — the wiki form achieves visibility through link-following navigation and the analog form through written cross-references).

### L1 — Common Mature Structure (standard in modern products, not definitional)

- **Link-while-writing ergonomics** — autocompletion of link targets as the user types, editor-toolbar link insertion with search over existing titles; creating a note and linking it are one act (A: Obsidian `[[` autocomplete; TiddlyWiki toolbar link + CamelCase).
- **Tags/categories** as a second organization dimension alongside links (A: Obsidian, TiddlyWiki).
- **Search across the library** returning notes with their context (A: TheBrain; Obsidian implied on page).
- **Backlinks and graph/network views** as the modern connection-visibility surface (A: Obsidian backlink count + graph; TheBrain visual network).
- **Visual surfaces** — canvas spaces and mind-map views where notes and their content are arranged spatially (A: Obsidian Canvas; TheBrain views).
- **Reuse machinery** — transclusion/embedding of one unit's content inside another (A: TiddlyWiki core; Obsidian canvas embeds).
- **Capture surfaces** — web clippers, quick capture, daily notes / journaling rhythm (A: Obsidian clipper + daily node + calendar plugin; TheBrain capture list).
- **Multi-device sync** — cloud, add-on, or self-hosted saving methods (A: all three evidenced products).
- **Publishing/sharing** — turning the personal web into a public wiki/knowledge base/digital garden, hosting services, shared team networks (A: Obsidian Publish, Tiddlyhost, TeamBrain).
- **Version history / recovery** in some products (A: Obsidian sync add-on claims version history).
- **Extensibility** — plugins, macros/widgets, open APIs (A: Obsidian, TiddlyWiki).
- **AI assistance** (era-current) — summarize, suggest links, surface related ideas (A: TheBrain Cerebro).

### L2 — Variant / Optional Structure

- **Storage/ownership substrate**: local open-format files (data-ownership pole) vs cloud-native app vs single self-owned file. A philosophy axis, not the invariant.
- **Authoring surface**: freeform document notes vs outliner bullets vs associative graph nodes — the outliner-hybrid is a recognized pole (Roam and Logseq position in it; positioning-level evidence only).
- **Network surface**: backlink panes + force-directed graph vs long-lived visual network map vs link-following wiki navigation.
- **Filing posture**: network-first (filing explicitly rejected — TheBrain's stated thesis) vs hybrid (links + folders/tags coexist — Obsidian demo shows folders).
- **Privacy/ownership posture**: local-first/E2EE vs cloud.
- **Collaboration depth**: none → shared vault → team/enterprise shared networks.
- **Publishing posture**: private tool → public digital garden/wiki output.
- **AI-native vs AI-added** (era-current).
- **Purpose emphasis**: thinking/writing vs research vs project/personal-organization adjacency (products differ in what they hang off the network).

### L3 — Vendor-specific Structure (research notes only)

- Obsidian: vault of local Markdown files; community plugin catalog (Calendar, Kanban, Dataview, Outliner, Tasks by name); paid Sync (E2EE, selective, shared vaults, one-year version history) and Publish products; Canvas; Web Clipper; "Invent your own personal Wikipedia" framing.
- TheBrain: "Brain" as the container noun; Cerebro AI (agentic, RAG over the user's knowledge); Card/Mind Map/Tree views; TeamBrain enterprise tier; 28+ years / 10M+ downloads marketing figures; free-desktop claim.
- TiddlyWiki: "tiddler" naming ("better to be confusingly distinctive than confusingly generic" — vendor's own words); tiddler fields model (required `title`); WikiText with CamelCase auto-linking and transclusion; single-HTML-file delivery; saving-method ecosystem (Tiddlyhost etc.); v5.4.1.
- Roam Research: "networked thought" tagline; (further specifics unreachable in this pass — none asserted).
- Logseq: "privacy-first, open-source knowledge base" positioning; (further specifics unreachable — none asserted).

## Vendor-specific Findings

See L3. None promoted to the canonical model. Two anti-overfitting cautions recorded:

1. **Backlink pane / graph view** are the currently dominant connection-visibility implementations (2 of 3 evidenced products), but TiddlyWiki satisfies the core without them — so they are L1, not L0 (same structure as the phone-number caution in the instant-messaging precedent).
2. **Local-first/open-format data ownership** is this sample's loudest philosophy (2 of 3 evidenced products) but TheBrain is a cloud/proprietary product — substrate stays L2.

## Boundary Findings

| Neighbor Type | Boundary judgment | "Remove what → becomes the other Type" |
|---|---|---|
| Note-taking Application (processed; JOINT REVIEW DISCHARGED) | ratified seam: note-taking = capture-and-return loop over a personal library (links optional, at most one convenience dimension); PKM = the user-built link network as the defining structure, with connection visibility/navigation and network-growth as the point. Removal tests both directions recorded (remove the network → note-taking; add the network as the point → PKM). Obsidian straddles by marketing (sampled by the note pass as a note product and here as a PKM product) — one product spanning two Types by center of gravity; the market splits OneNote/Apple-Notes/Evernote-class products (linking secondary) from network-first products | remove the link network → note-taking |
| Markdown Editor (processed; markdown-editor pass's substrate seam CONFIRMED from this side) | markdown files are the storage substrate of the local-first pole; the central promise discriminates: editing and rendering markdown documents → markdown editor; a growing link network of notes → this Type. Same seam the note-taking pass confirmed; Obsidian remains the recorded straddler (markdown at the storage/editing layer, PKM by promise) | remove the network, keep editing-and-rendering documents → markdown editor |
| Outliner (processed; JOINT REVIEW DISCHARGED) | ratified center-of-gravity seam as requested: outliner's point = the indentation tree as the content's own organization (subtree operations on items); PKM's point = the cross-note link network. Roam and Logseq straddle (outliner editing core + knowledge-network promise) and cannot be excluded from either side on editing grounds — held as outliner-hybrid variants inside PKM and networked-hybrid variants inside the outliner's record | remove the link network, keep the tree → outliner |
| Visual Note-taking Application (§03.02 sibling, unprocessed) | forward flag: canvas-first products (and Obsidian's Canvas as one surface) put spatial arrangement and sketching first; PKM puts the link network first. Canvas placement of notes is a PKM surface (A: Obsidian), not the Type's center — that pass should fix the seam by whether spatial arrangement or connection structure is the point | spatial-first → visual note-taking |
| Wiki Application / Knowledge Base Application | org-governed shared corpus with reader/contributor separation vs personal self-governed web. Obsidian Publish ("turn your notes into an online wiki") shows publishing the personal web OUT is an output surface, not a Type change | org-governed shared corpus → wiki/KB |
| Diagramming Application / Digital Whiteboard | drawn diagrams (nodes are shapes) vs accumulated authored knowledge units (nodes are notes; the graph is emergent from links, not drawn) | draw the relationships as shapes → diagramming |
| Bookmark Manager / Read-it-later | records pointing at external resources vs authored knowledge units; clippers feed captured web content INTO the network as notes | records address external resources → bookmark manager |
| Reference Manager (§23, unprocessed) | citation/bibliography-centric academic workflow vs general knowledge network; a PKM may cite sources but citation machinery is not its center | citation-centric → reference manager |
| Knowledge Graph Explorer / Knowledge Graph Platform (§13) | enterprise data systems over governed datasets vs an individual's thinking tool; "graph" vocabulary shared, world different | — |
| Team Workspace / Notion-class products | org containers + databases + shared pages; notes one primitive among many; straddle case, consistent with the note-taking pass's flag | org-managed shared workspace → team workspace |
| Concept/mind-mapping tools | node-and-arrow authoring of a single diagram vs persistent accumulating note network; L0 test "2 without 1 = concept mapper" records the seam | nodes without authored content → concept mapper |

## Uncertainties

1. Roam and Logseq operational docs unreachable (three passes' attempts combined) — their internal structures (outliner granularity, references machinery, journals) are NOT asserted anywhere; they witness positioning only.
2. Obsidian help site unreadable (SPA) — no operational mechanism claims (e.g., link-update-on-rename behavior) are made; the product page's own claims are the evidence ceiling.
3. TheBrain's link semantics (link types/directionality) live in an unreachable user guide — its model asserted only at product-page strength ("visual knowledge network", "link thoughts").
4. TiddlyWiki backlink display not evidenced on fetched pages — "connection visibility" for the wiki pole is held at link-following navigation strength, not backlink-pane strength.
5. Block-level references, typed links, and unlinked-mention conversion were not researched to evidence on any reachable surface and are deliberately NOT claimed (frequent marketing associations of this Type).
6. Whether platform-native personal wikis (Zim/Tomboy class) constitute a separate variant or mere members of the wiki-pole: held as members; not sampled.
7. No numeric limits, pricing, or plan details anywhere — deliberately unclaimed.

## Final Synthesis

A Personal Knowledge Management Application is an individual's instrument for growing a personal web of knowledge: the user authors persistent knowledge notes, connects them with links while writing, and navigates and inspects the accumulating network — following links, seeing a note's connections, watching patterns surface — so that knowledge compounds over time instead of piling up in folders. The link network is the product's organizing structure (that is what separates it from note-taking's capture-and-retrieve loop and from the outliner's indentation tree); the network's visibility and navigability make it an object the user can think with (that is what separates it from a note app with inline hyperlinks); and the notes themselves carry authored knowledge (that is what separates it from concept mapping). Everything else — backlink panes, graph views, tags, daily notes, canvases, transclusion, sync, publishing, plugins, AI — is mature-market structure layered on that core, varying from the self-contained single-file wiki through local-first Markdown graphs to cloud associative networks and outliner hybrids.
