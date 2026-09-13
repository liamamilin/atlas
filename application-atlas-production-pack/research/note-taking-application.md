# Research Notes — Note-taking Application

Research date: 2026-09-08
Directory leaf: "Note-taking Application" (§03.02 Notes & Personal Knowledge)
Slug: note-taking-application

## Research Goal

Understand the Note-taking Application as an Application Type: what a "note" is as a unit of record, how capture works, how the collection is organized and retrieved, what mature products add on top, and where the boundary lies against neighboring Types (document editors, PKM/outliner/visual note-taking siblings, wikis/knowledge bases, bookmark/read-later, task apps, meeting-notes).

## Initial Boundary

Working hypothesis at start:

- Core: an individual captures information as discrete, persistent notes; the notes accumulate into a personal library; the library can be organized and searched so any note can be gotten back.
- Primary users: individuals (students, professionals, writers, anyone remembering things) — not organizations as governing bodies.
- Nearest confusions: Document Editor (single long-form artifact); Personal Knowledge Management Application (linked-network thinking); Outliner and Visual Note-taking Application (structure-first / canvas-first siblings); Wiki / Knowledge Base (organization-governed corpus); Bookmark Manager / Read-it-later (records pointing at external resources); To-do (tracked actions); Meeting Notes Application (meeting-anchored records).

Unknowns at start: whether "capture surfaces outside the main editor" and "retrieval" are definitional or merely common; whether platform-native memo/sticky apps pass a definition built from modern cloud note apps (historical check).

## Research Questions

1. What is a "note" in these products — content model, typical size, what it may embed?
2. How do notes get created? What capture surfaces exist beyond the main editor?
3. How is the collection organized — containers, tags, links, pins, ordering?
4. How does retrieval work — browse, search, filters, attachment search?
5. What is the note lifecycle — create, edit, pin, archive, delete, restore, version?
6. What non-text content do notes hold — images, files, audio, handwriting, scans?
7. What is the sync/device model — cloud vs local, offline behavior?
8. How do sharing and collaboration work, and how do they relate to personal ownership?
9. What privacy/security surfaces exist (locks, encryption posture)?
10. Where are the boundaries: vs document editors, PKM/outliner/visual siblings, wikis/KBs, bookmark/read-later, task apps?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer layers:

| Product | Philosophy / position | Customer layer | Evidence tier reached |
|---|---|---|---|
| Microsoft OneNote | suite-embedded freeform digital notebook (notebook/section/page) | consumer + education + enterprise | Tier 1 (operational docs) |
| Apple Notes | platform-native default notes app, OS-integrated | consumer (mass) | Tier 1 (official user guide) |
| Evernote | cloud "remember everything" capture-and-archive archetype | consumer + prosumer + enterprise tier | Tier 2 (product page; help-center how-tos "under construction") |
| Obsidian | local-first plain-text Markdown files, link/graph-centric | prosumer / power users | Tier 2 (product page; help site SPA unreachable) |
| Joplin | open-source, local data ownership, E2EE sync | prosumer / privacy-conscious | Tier 2 (product page) |

Google Keep (lightweight card-capture pole) was attempted twice and timed out; dropped from the sample rather than substituted from memory (see Sources — limitation).

## Sources

- Microsoft — OneNote help & learning: https://support.microsoft.com/en-us/onenote (fetched 2026-09-08)
- Microsoft — Basic tasks in OneNote on Windows: https://support.microsoft.com/en-us/onenote/onenote-help-and-learning/basic-tasks-in-onenote-on-windows (fetched 2026-09-08)
- Apple — Notes User Guide for Mac (TOC + section titles; macOS Tahoe 26): https://support.apple.com/guide/notes/welcome/mac (fetched 2026-09-08)
- Evernote — product site: https://evernote.com/ (fetched 2026-09-08); Evernote Help & Learning root: https://help.evernote.com/hc/en-us (fetched 2026-09-08; how-to guides section declared "under construction")
- Obsidian — product site: https://obsidian.md/ (fetched 2026-09-08)
- Joplin — product site: https://joplinapp.org/ (fetched 2026-09-08)
- Google Keep — https://support.google.com/keep/ (attempted twice 2026-09-08, request timed out both times)

**Source-access limitations.** (1) Google Keep unreachable — the lightweight-capture card-style pole is under-evidenced in this sample; no claims rest on it. (2) Evernote's operational how-to documentation was not reachable in substance ("under construction"), so Evernote evidence is positioning-level (Tier 2) only. (3) Obsidian's help site (SPA) was not readable from this environment (same limitation recorded by the markdown-editor pass); Obsidian evidence is limited to its product-page claims, which are unusually explicit about storage and linking. Precise operational numbers (storage limits, note-size limits, plan caps) were not researched anywhere and are not asserted.

## Product Observations

Evidence layers: **A** = directly observed on that product's official documentation; **B** = cross-product commonality; **C** = canonical inference.

### Microsoft OneNote (evidence: A — Tier 1)

- Self-description: "a digital notebook that provides a single place for all of your notes and information — everything you need to remember and manage in your life at home, at work, or at school."
- Container hierarchy directly observed: **notebook → sections → pages → subpages**; sections "like the tabs in a typical five-subject paper notebook"; page titles show in the page list; section/page tabs can be rearranged.
- Freeform page model: "click wherever you want them to appear, and then start typing" — content lives in movable note containers on a page.
- **No Save button** — "OneNote automatically saves everything for you."
- Content: type or handwrite (ink; convert ink to text/shape/math); insert pictures, screen clippings, online video, scanned images, file attachments ("inserted files are just copies"), tables (convertible to Excel), date/time, math equations.
- Links: typed URLs auto-format; manual links "including links to text, pictures, and to other pages and sections of your notebooks" — internal note-to-note links observed.
- Tags: apply a tag to a note; search for tagged notes.
- Search: "search all your notes quickly so you can find notes even if you forget where you put them."
- Capture surfaces beyond the editor: Quick Notes, sticky notes, screen clipping, insert Outlook meeting details, audio/video notes, linked notes.
- Sync via OneDrive ("store your notebooks online and get to them on any of your devices"); sync troubleshooting is a documented concern class.
- Sharing: share a notebook, change permissions, stop sharing.
- Security: password-protect (sections).
- Lifecycle: recover deleted notes; export notes as PDF; print.
- OCR: copy text from pictures and file printouts.
- Era-current: Copilot summarize notes / create to-dos / project plans.
- Organization extras: templates; Outlook tasks from notes.

### Apple Notes (evidence: A — Tier 1, official user guide TOC/sections)

- Positioning: "Jot down a quick thought or take longer, detailed notes."
- **Accounts and folders** organize notes; folders can be added/removed; notes sorted and **pinned**.
- **Tags** and **Smart Folders** (rule-based folder views).
- Create and edit notes; format with lists, tables, highlight styles.
- Quick Note: a dedicated system-level capture surface for instant note creation.
- Content: drag-and-drop pictures, videos, PDFs and other files; scan documents; mark up attachments; record audio in a note with searchable live transcription; solve math inline; add links.
- Attachment browser ("View attachments"); customizable note appearance; widgets.
- Search your notes (dedicated guide section).
- Lock your notes with a password; change that password.
- Share notes **and folders**; collaborate with shared notes and folders; manage shared items.
- Delete a note; import, export, and print notes.
- Accounts: notes live in configurable accounts (iCloud and others) — "Add or remove notes accounts".
- Content intake from other apps: "add content to notes right from Safari, Maps, and many other apps."

### Evernote (evidence: positioning-level, Tier 2)

- Positioning: "Your second brain... Remember everything"; "Capture everything that is, was, or could be important and access it whenever and wherever."
- Capture breadth: "Save anything, in any form — Record, transcribe, scan, clip." Web Clipper ("Clip what you see online with a click"); document scanning.
- Organize: "Notebooks & Spaces — Organize ideas where they belong"; templates ("ready-made note structures").
- Recall: Search as a first-class marketed capability ("Find exactly what you're looking for in seconds"); "already synced across all your devices."
- Adjacent structure inside the product: Tasks ("integrated tasks"), Calendar ("Link events to notes"), collaboration (real-time editing, comments, task assignment), AI features (transcribe/rewrite/meeting note taker — era-current).
- Help center reachable but how-to guides "under construction" — operational details not verified.

### Obsidian (evidence: A on product-page claims, Tier 2)

- Storage claim, verbatim: "Obsidian stores your notes locally as plain text Markdown files"; "notes privately on your device... even offline. No one else can read them, not even us"; "open file formats, so you're never locked in."
- Notes-as-files model visible in product UI claims: a note is a Markdown text file with title, word/char counts, timestamp; tags inline (`#projects #travel`).
- **Links between notes are the headline capability**: "Link anything and everything... Invent your own personal Wikipedia"; backlinks shown per note ("1 backlink"); graph view visualizing relationships between notes; tags for organization.
- Canvas: infinite space for research/brainstorm (visual surface alongside notes).
- Plugins/themes ("thousands of plugins") — calendar/daily notes, kanban, tasks, dataview as community plugins.
- Sync as a paid add-on: E2EE, selective sync, version history (one year, per their claim), collaboration via shared vaults.
- Publish: "Turn your notes into an online wiki, knowledge base, documentation, or digital garden."
- Web Clipper; CLI; mobile apps.
- Positioning spans: "From personal notes to journaling, knowledge bases, and project management" — note app as base layer under multiple ambitions.

### Joplin (evidence: A on product-page claims, Tier 2)

- Self-description: "an open source note-taking app. Capture your thoughts and securely access them from any device."
- Multimedia notes: images, videos, PDFs, audio; math expressions and diagrams; photos from mobile into a note.
- Collaboration: share notes via Joplin Cloud; publish a note to the internet with a URL.
- Web clipper: save web pages or screenshots as notes.
- Customization: plugins, themes, choice of Rich Text or Markdown editor; extension API.
- Sync: Joplin Cloud, Dropbox, OneDrive; desktop/mobile/terminal apps.
- Data ownership: "your notes are saved to an open format"; E2EE ("Uses End-To-End Encryption (E2EE) to secure your notes").

## Cross-product Comparison

| Capability | OneNote | Apple Notes | Evernote | Obsidian | Joplin |
|---|---|---|---|---|---|
| Note as authored persistent record | A | A | A | A | A |
| Many notes forming one personal collection | A | A | A | A | A |
| Container organization (notebooks/sections/folders) | notebooks/sections/pages/subpages | accounts/folders | Notebooks & Spaces | folders (in a file vault) | (claimed notebooks; not detailed on page) |
| Tags | A (apply + search by tag) | A (tags + Smart Folders) | not evidenced | A (inline tags) | not evidenced |
| Pins / ordering / sorting | rearrange tabs | sort and pin | home personalization | not evidenced | not evidenced |
| Search across the library | A (explicit) | A (explicit) | A (explicit, marketed) | not evidenced on page | not evidenced on page |
| Rich content in notes (media/files/tables/audio) | A (broad) | A (broad, incl. scan + audio transcription) | A (record/transcribe/scan/clip) | A (embeds; canvas) | A (broad) |
| Handwriting/ink | A (full ink toolchain) | A (mark up attachments) | not evidenced | not evidenced (plugin territory) | not evidenced |
| Internal note-to-note links | A (explicit) | ambiguous (links section not read) | not evidenced | A (links + backlinks + graph, core) | not evidenced |
| Capture beyond the editor | Quick Notes, sticky notes, screen clipping | Quick Note, share from other apps | Web Clipper, scan | Web Clipper | Web Clipper (pages/screenshots) |
| Multi-device sync | A (OneDrive) | A (accounts, iCloud et al.) | A (marketed) | optional paid add-on (E2EE) | A (multiple targets) |
| Sharing / collaboration | share notebook + permissions | share notes + folders, collaborate | real-time editing, comments | Publish sites; shared vaults | share via Cloud; publish URL |
| Lock / encryption posture | password-protect sections | lock notes with password | not evidenced | local-only + E2EE sync (claimed) | E2EE (claimed) |
| Delete / recovery | recover deleted notes | delete note (guide section) | not evidenced | version history (1 year, claimed) | not evidenced |
| Export / print | export PDF, print | import/export/print | not evidenced | open formats | open format |
| Task adjacency | Outlook tasks in notes | lists/checklists | first-class Tasks + Calendar | community Tasks plugin | to-do (press quote only) |
| AI assist (era-current) | Copilot | transcription/math (not AI-labeled) | AI feature suite | none claimed | none claimed |
| Storage substrate | vendor cloud | user accounts (iCloud) | vendor cloud | local plain-text files | local + user-chosen sync targets |

Reading of the table: the first two rows hold across all five products without exception (B-level, universal in sample). Search is explicitly evidenced in three products; the other two simply don't state it on the surfaces fetched (absence of evidence, not evidence of absence — search is treated as common, not universal). Everything from "Tags" down varies in presence and depth — none of it is definitional.

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The note as the unit of record.** A persistent, individually addressable, user-authored content record — text-centric, optionally embedding media and files. The user creates and edits notes; the note, not the document or the resource, is what the system stores and manages. (Remove → a text editor / word processor with no discrete notes.)
2. **The personal note library.** Many notes accumulate, over time, into one collection that belongs to the individual user — held durably, private by default; any sharing is a delegation of specific notes or containers, not a change of ownership. (Remove the personal ownership → wiki / knowledge base territory. Remove the accumulation → a transient scratchpad.)
3. **The capture-and-return loop.** Low-friction creation of new notes (in the editor and, where present, through capture surfaces outside it) and reliable return to any earlier note through browsing and/or search. (Remove the return leg → a write-only journal, not a library. Remove the capture-first orientation → a document editor.)

Jointly-held is load-bearing:

- 1 alone = single-document text editor / word processor
- 2 without 1 (records that point at external resources rather than hold authored content) = bookmark manager / read-it-later
- 1+2 without 3 = write-only journal with an unusable archive
- 1+3 without 2 = sticky/scratch surface with no library ambition
- 2+3 without 1 = a pile of documents with a search box (document repository)

### Historical / market-sample check (per §24 reasoning)

Would older, regional, platform-native, or differently positioned products still fit?

- **Platform-native memo/sticky apps** (list of small text notes, browse-only, no sync, no tags, no media): satisfy all three legs — note as unit, personal accumulation, browse-to-return. Fits.
- **Plain-text flat-list cloud notes** (e.g. the Simplenote lineage — flat list, tags, search, no containers): fits; container structure is not definitional.
- **Paper analogy** (a notebook with an index): capture + accumulated collection + retrieval via index — the Type's thin ancestor. Fits at the analog level; no electronic capability is in the core.
- **OneNote 2003-era** (before cloud sync): fits — notebooks, freeform pages, local storage.
- **Modern AI-era apps**: fit with the AI layer as era-current addition.

Conclusion: the L0 holds across eras and platforms. No cloud, no sync, no tags, no media, no markdown, no AI belongs in the definition.

### L1 — Common Mature Structure (standard in modern products, not definitional)

- **Organization structures** — containers (notebooks/sections/folders), tags, pins, sorting, reordering. Multiple alternative indexing schemes over the same library.
- **Search across the library** — explicitly evidenced in OneNote, Apple Notes, Evernote; attachment-content search (OCR) in some.
- **Rich content in notes** — images, file attachments (as copies), tables, lists/checklists, audio/video, handwriting/markup in some.
- **Multi-device sync** — via vendor cloud, user accounts, or user-chosen sync targets.
- **Sharing and collaboration** — share a note or a container, permissions, real-time co-editing in some products; always a delegation from the personal default.
- **Lifecycle machinery** — delete with recovery, version history in some, archive/trash.
- **Capture surfaces beyond the editor** — quick note, web clipper, document scan, share-sheet intake.
- **Export / print.**
- **Note locking** (password protection) in several products.

### L2 — Variant / Optional Structure

- **Storage substrate**: local open-format plain-text files vs vendor cloud service.
- **Note format philosophy**: rich text vs Markdown source vs freeform canvas page.
- **Organization philosophy**: strict container hierarchy vs flat list + tags vs link-centric (links/backlinks/graph).
- **Platform posture**: platform-native preinstalled app vs cross-platform independent product.
- **Privacy posture**: local-only/offline-first vs cloud; optional E2EE.
- **Collaboration depth**: none → read-only share → co-editing.
- **Capture breadth**: clipper, scanning/OCR, audio transcription.
- **Adjacent structure embedded**: tasks/checklists, calendar linkage.
- **Handwriting-first** (stylus platforms) vs text-first.
- **Journaling / daily-note** usage patterns as a variant, not a separate Type.
- **AI assistance** (era-current; present in some current products).

### L3 — Vendor-specific Structure (research notes only)

- OneNote: notebook/section/page/subpage with movable note containers; sticky notes; Outlook tasks/meeting details insertion; Ink Replay; convert table to Excel; "no Save button" auto-save framing; SharePoint notebooks.
- Apple Notes: Smart Folders; system-level Quick Note; in-note audio transcription; inline math solving; lock with per-account password; iCloud account binding.
- Evernote: "second brain" positioning; Spaces; Home personalization; Tasks/Calendar linkage; AI feature suite naming.
- Obsidian: vault (folder of Markdown files); graph view; Canvas; community plugin ecosystem; paid Sync (E2EE, selective, version history) and Publish products; CLI.
- Joplin: choice of Rich Text or Markdown editor; multiple third-party sync targets (Dropbox, OneDrive); terminal app; Joplin Cloud as EU-hosted paid option.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model. The Evernote Tasks/Calendar embedding and the Obsidian plugin ecosystem are the clearest cases of suite/extension drift that must not be read back into the Type definition (same pattern as the Toast payroll/marketing caution in the workflow example).

## Boundary Findings

| Neighbor Type | Boundary judgment | "Remove what → becomes the other Type" |
|---|---|---|
| Document Editor / Collaborative Document Editor | unit is the document (long-form, formal, export-as-artifact) vs the note (many, small, retrievable fragments) | remove the multi-note library + retrieval loop and orient on producing formal documents → document editor |
| Distraction-free Writing Application | writing surface for producing text; no library organization/retrieval ambition | remove the library → writing surface |
| Markdown Editor | markdown files as substrate is shared; central promise differs — editing/rendering markdown documents vs holding/retrieving a personal note library | if the promise is the document (edit + render), it's a markdown editor; if the promise is the library, it's note-taking. Confirmed from this side (discharges the markdown-editor pass's seam). Obsidian straddles — held boundary-adjacent |
| Personal Knowledge Management Application (unprocessed) | closest sibling. Proposed discriminator: note-taking's promise = capture + retrieve individual notes; PKM's promise = grow a connected network of notes (links/backlinks/graph as the point). Needs joint treatment when PKM pass runs | remove the network-of-knowledge ambition → pure note-taking; add it as the product's point → PKM |
| Outliner (unprocessed) | structure-first (hierarchical items, folding) vs text-first freeform note | to be fixed in the outliner pass |
| Visual Note-taking Application (unprocessed) | canvas/sketch-first personal capture vs text-first note | to be fixed in that pass (consistent with digital-whiteboard/collaborative-canvas passes: "note-taking centers on personal capture and organization") |
| Meeting Notes Application (processed) | record anchored to a specific identified meeting occurrence with meeting anatomy | remove the meeting anchor → note-taking. Confirmed as recorded by that pass |
| Wiki Application / Knowledge Base Application | corpus governed by an organization; shared article lifecycle; reader/contributor separation | remove the org-governed shared corpus; make the collection personal → note-taking |
| Bookmark Manager / Read-it-later Application | records point at (or store captured) external resources; note records hold authored content | remove the address/resource anchor and hold authored content → note-taking. Consistent with the bookmark-manager pass |
| To-do List / Task Management Application | notes = information to remember; tasks = actions with state to complete | remove the action/state machinery → checklist inside a note (common), not a task app |
| Team Workspace / Notion-class products | org containers + databases + docs; note is one primitive among many | straddle case — flagged, not sampled in this pass |
| Text editor (Notepad-class) | single-document surface; no library/retrieval | remove everything except one editing surface → text editor |

## Uncertainties

1. Google Keep unreachable — the ultra-lightweight capture-only pole is unverified in this sample; claims about that pole are avoided.
2. Evernote operational documentation not reachable in substance — Evernote-specific workflow claims kept at positioning level.
3. Obsidian search not evidenced on reachable surfaces — search treated as common on the strength of three products, not five.
4. Apple Notes "Add links" section content not read — no claim that Apple Notes supports note-to-note linking; internal linking rests on OneNote (explicit) and Obsidian (explicit, core).
5. Whether platform sticky-notes apps should be a Variant or a separate Type: held as a thin Variant here (they pass L0); flagged for the Personal Organization neighborhood if a dedicated leaf ever appears.
6. Notion-class workspace products (note primitive inside databases/workspaces) not sampled; boundary to Team Workspace Platform is asserted structurally, not from product evidence.
7. No precise numeric limits anywhere (note size, storage, plan caps) — deliberately unclaimed; none were researched.

## Final Synthesis

A Note-taking Application is an individual's capture-and-retrieval instrument for information: the user creates persistent authored records (notes), the notes accumulate into a personal library held over time, and the application guarantees both low-friction capture and reliable return (browse and/or search). Everything else — containers, tags, links, media, sync, sharing, locks, clippers, AI — is mature-market structure layered on that loop, varying by product philosophy (suite-embedded freeform canvas; platform-native default; cloud archive; local markdown library; open-source data ownership). The Type's identity survives removing every one of those layers; it does not survive removing the note, the personal library, or the capture-and-return loop.
