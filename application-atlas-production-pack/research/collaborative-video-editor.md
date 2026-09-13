# Research Notes — Collaborative Video Editor

## Research Goal

Understand, from real products, what a **Collaborative Video Editor** is as an Application Type: what the shared unit of work is, how multiple users coordinate editing work on it (locking vs live merging), what roles and access rules exist, how review/comment/approval loops attach to the edit, how media and project state are shared across users and machines, and where the boundary lies against the single-user Video Editor / NLE, AI Video Editing Applications, media asset management, and the "video collaboration" review-platform category.

## Initial Boundary (working hypothesis before research)

- Hypothesis: a Collaborative Video Editor is a timeline-based video editing application whose defining addition is a **shared project that multiple identified users edit together**, with the system coordinating concurrent work so nothing is lost.
- Nearest neighbors: Video Editor / NLE (single-user, local-file project), AI Video Editing Application (system executes the edits), Media Asset Management / MAM (asset custody without editing), and video review & approval platforms (Frame.io-style — collaboration *around* editing, no editing execution).
- Potential confusions to resolve: (a) is real-time same-timeline co-editing definitional or just the cloud-native pole? (b) do review platforms belong here? (c) is collaboration a separate Type or just a capability of modern NLEs?

## Research Questions

1. What is the shared unit of work (project / project library / production / workspace), and where does it live (local file, shared storage, project server, cloud)?
2. How do multiple users edit at the same time — what is locked, at what granularity, and who releases locks?
3. What roles exist (editor, assistant, colorist, audio, producer/reviewer, admin) and how is access differentiated?
4. How are media/assets shared between users and machines (shared bins, media sync, proxies, relinking)?
5. How do changes made by one user surface to others (update prompts, compare tools, version stacks, merge)?
6. How do comments/markers/approvals attach to the edit, and do they round-trip into the timeline?
7. What review surfaces exist inside the editor vs outside (publish for review, presentations, chat)?
8. What are the boundary tests against Video Editor / NLE, AI Video Editing, MAM, and review platforms?
9. Does the leaf hold as an independent Type?

## Representative Products

| Product | Posture | Segment | Why selected |
|---|---|---|---|
| DaVinci Resolve (Blackmagic Design) | all-in-one post suite; cloud project libraries + private project server; multi-role simultaneous work | professional post-production (film/episodic) | the most explicit "collaboration" marketing pillar among pro suites; different philosophy: everyone on the same project at once |
| Avid Media Composer | dedicated editorial NLE; shared-storage project sharing | film/TV/news facilities (enterprise) | the decades-old classic multi-user editing environment; different philosophy: shared storage + bin locking |
| WeVideo | cloud-native browser editor | education (K-12/higher-ed) & business teams | different customer tier and substrate; cloud real-time co-editing pole |
| Frame.io | video collaboration platform: file management, review & approval, workflow | media/entertainment, agencies, brands | **boundary anchor** — the most famous "video collaboration" product that does not edit |

Market context only: Adobe Premiere Pro's team-workflow features (Productions) could not be verified — Adobe's help center was unreachable from the research environment (see Sources / Limitations). No claims are made about it.

## Sources

| Source | Type | Date |
|---|---|---|
| Blackmagic Design — "DaVinci Resolve – Collaboration" product page (https://www.blackmagicdesign.com/products/davinciresolve/collaboration) | Tier 2, operationally detailed | 2026-09-06 |
| Avid — "Media Composer" product page (https://www.avid.com/media-composer) | Tier 2, operationally detailed | 2026-09-06 |
| WeVideo — "Real-time video collaboration" page + operational FAQ (https://www.wevideo.com/business/collaboration) and homepage | Tier 2 | 2026-09-06 |
| Frame.io — product site (https://www.frame.io/) | Tier 2 | 2026-09-06 |

Research date: 2026-09-06. All four products' official product pages were fetched directly. Help centers / user manuals were not reachable or not attempted where product pages carried the needed operational detail (see Limitations).

### Limitations

- Adobe helpx.adobe.com timed out twice (Productions documentation). Premiere Pro is market context only; nothing is asserted about its collaboration model.
- Avid and WeVideo evidence comes from official product pages (marketing framing but with concrete operational claims: "real-time bin locking", "simultaneous editing"). Assertion strength calibrated accordingly; no numeric limits derived from them.
- DaVinci Resolve's user manual (PDF) was not fetched; collaboration mechanics rely on Blackmagic's own collaboration page, which describes mechanisms (bin/timeline locking, update acceptance, timeline compare) in operational terms.
- No precise numbers (collaborator counts, storage quotas, lock timeouts) are asserted in the final document.

## Product A — DaVinci Resolve (Blackmagic Design)

### Key observations (Layer A — vendor collaboration page)

- Positioning: "the world's only complete post production solution that lets everyone work together on the same project at the same time"; contrast with the traditional linear hand-off workflow ("each artist handing off to the next").
- **Blackmagic Cloud**: create a Cloud ID → log into the **DaVinci Resolve Project Server** → set up a **project library** for the project → "assign any number of collaborators to a project" → "Multiple people can work on the same timeline!"
- **Change acceptance model**: "When changes are made, you can see and accept them in the viewer, changes are only applied when you accept updates. A single click can relink files, update timelines, or view changes."
- **Timeline compare tools**: "let you merge changes into a master timeline or others can continue with edits"; visual diff shows "where footage has been added, deleted, moved or trimmed".
- **Bin and timeline locking**: "Automatic bin and timeline locking let multiple people work without overwriting each others work… Bins and timelines are 'read only' until unlocked by the current user." One user organizes footage in a bin while another works in a different bin.
- **Clip-level locking in grading**: "Individual clips are auto locked while they are being graded so they can't be overwritten, and each colorist knows who is grading which shot."
- **Role specialization by page**: editors, colorists, VFX artists, animators and sound engineers work "in their own dedicated page with the tools they need"; they "can review each other's changes without… re-conforming the timeline".
- **Shared markers**: private markers visible only to their author; shared markers visible to everyone working in the project — annotation with visibility classes.
- **Built-in chat** so team members "can talk about shots, review tasks and share creative ideas without leaving the software".
- **Live save**: "multiple users can constantly save small and incremental changes to the project's database while working in real time."
- **Individual monitoring and caching**: per-user cache/monitoring settings; collaborative projects can be opened "in read only mode to review cuts or copy items without affecting other users."
- **Media distribution**: media sync between computers so "everyone has a local copy… As new files are added they will automatically sync and appear in the project"; **Blackmagic Proxy Generator** auto-creates proxies from camera originals, "automatically linked… to the original media"; live camera sync uploads proxies so editors "will get the shots" while working.
- **Infrastructure options**: Blackmagic Cloud (cloud project libraries + storage), private **Project Server app** (free, for VPN/private-network workgroups), or network storage (Blackmagic Cloud Store / Cloud Pod / own storage).
- **Organizations** (for companies): groups/teams to share projects with a whole group, SSO, license management, project libraries on dedicated servers.
- **Review outside the editor**: "Presentations" — publish a timeline/clip, authorize viewer IDs; "Shared markers and comments are automatically and bidirectionally relinked with DaVinci Resolve" — frame-accurate feedback round-trips.

## Product B — Avid Media Composer

### Key observations (Layer A — vendor product page)

- Pricing tiers make **Shared Projects** a tier differentiator: Standard/Ultimate include "Shared Projects (Avid NEXIS)"; Enterprise adds "Shared Projects (Avid NEXIS + 3rd party storage)" and "Enterprise admin: manage settings and roles".
- **Production-Scale Deployments**: "Shared projects: Integrate seamlessly with Avid NEXIS and now with Third Party Shared Storage solutions to let multiple editors safely work inside the same project using **real-time bin locking** and **centralized shared media**."
- **"Conflict-free collaboration"**: "Patented bin-locking lets teams work in the same project at once. Assistants and editors can collaborate without overwriting any cuts."
- **Media management**: "robust database engine effortlessly tracks millions of assets… automated asset tracking and zero broken links"; "database-driven core tracks every asset's identity, keeping media linked even as you move projects across different drives and servers."
- **Proxy editing**: "editing with lightweight proxies… Automatically track and relink seamlessly back to camera originals for final conforming and delivery."
- **Role/segment ecosystem**: newsroom integration (MediaCentral — "cut footage against live rundowns… deliver packages to playback"), audio post handoff (Pro Tools round-trip), enterprise export/toolset restriction ("Leak-proof security: Control your environment by restricting user exports and toolsets").
- Editing grammar itself is the professional editorial toolset (trim mode, multicam, color/finish) — collaboration rides on top of a standard NLE core.

## Product C — WeVideo

### Key observations (Layer A — vendor collaboration page + FAQ)

- Cloud-native: "cloud-based team video editing software… no extra downloads or installs needed"; access "from any device" with an internet connection.
- **Simultaneous co-editing**: FAQ — "Can multiple users edit the same video simultaneously? Absolutely! Simultaneous editing is the bread and butter of real-time video collaboration." Homepage: "Share projects with others and collaborate in real-time."
- **Project-level collaboration setup**: "Simply open a new project, add users, customize permissions, then work together inside the editor."
- **Permissions**: "you decide who gets to view, edit, and share content each step of the way"; "Easy-to-manage user permissions help shape workflow and security."
- **Feedback machinery**: "Multiple people can edit video projects at once, give actionable feedback, and apply instantly"; "Built-in chat and comment features"; engagement analytics to "assess and measure progress."
- **Collaborator scale**: "no limit to the number of collaborators" on a project (vendor claim).
- **Segment machinery**: templates to "customize, brand, and assign"; "shareable content libraries across teams, departments, or districts"; LMS/video-host integrations (Google Classroom, Canvas, YouTube, Zoom, Vimeo…); admin features; interactive-video sibling (PlayPosit-style) and white-label API are separate platform pillars.
- No mention of a locking model — coordination is presented as live simultaneous editing inside the cloud editor.

## Product D — Frame.io (boundary anchor)

### Key observations (Layer A — vendor site)

- Self-description: "Upload creative files, manage projects, assign tasks, get precise feedback, and share your work." Feature pillars: Workflow Management, File Management, Share & Present, Review & Approvals, Camera to Cloud, Mounted Storage, Frame.io Drive, Integrations.
- **No editing execution anywhere**: no timeline, no trimming, no rendering in the product. Review is "precise feedback with advanced commenting capabilities" on uploaded files.
- The editor stays external: "Premiere integration — Give the editor frame-accurate notes right in their workspace." Notes flow *to* the editor; the edit happens elsewhere.
- Project/permission machinery (restricted projects/folders, internal vs client comments, share permissions, watermarks, SSO, team workspaces) is workflow/review machinery, not editing coordination.
- Conclusion: Frame.io is the canonical member of a *different* category — video review/collaboration platform — despite the marketing overlap. It fails the editing-execution test, hence not this Type (and the directory has no leaf for that category — see Boundary Issues).

## Cross-product Comparison

| Dimension | DaVinci Resolve | Media Composer | WeVideo | (Frame.io — anchor) |
|---|---|---|---|---|
| Shared unit of work | project inside a project library (cloud or private Project Server) | shared project on shared storage (NEXIS / 3rd-party) | cloud project in a workspace | project = file collections (no edit) |
| Multi-user editing model | same project simultaneously; bin & timeline locks; clips auto-lock during grading; update-accept; timeline compare/merge | same project at once; real-time bin locking ("without overwriting any cuts") | real-time simultaneous editing, permissions per user; no documented lock model | n/a — no editing |
| Roles | edit / color / VFX / audio by dedicated pages; org groups; SSO | editors & assistants; Enterprise admin manages settings and roles | view / edit / share permissions per user | reviewer/commenter/view-permission roles |
| Media sharing | media sync to local copies; proxy auto-generation + relink; live camera proxies into bins | centralized shared media; database asset tracking; proxy relink for conform | cloud-hosted media; host-platform integrations | file management + mounted storage (custody, not editing) |
| Change surfacing | see-and-accept updates in viewer; visual timeline diff (added/deleted/moved/trimmed); merge to master | shared project state; bin-level separation of work | real-time change/progress tracking; instant application | version stacks of uploaded files (upload-replace, not edit-merge) |
| Review in/around the edit | shared vs private markers; built-in chat; Presentations w/ bidirectionally relinked comments | streaming playback for remote review; newsroom/audio-post handoffs | comments, chat, engagement analytics | the entire product is review/approval |
| Substrate | cloud project server / private project server / shared network storage | shared storage (facility LAN) | pure cloud browser | cloud |
| Editing grammar | full NLE + color/VFX/audio pages | full NLE (trim/multicam/finish) | simplified multi-track timeline | none |

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

Smallest structure without which the product stops being recognizable as a Collaborative Video Editor:

1. **Video editing core** — timeline-based assembly and manipulation of footage into an edited video deliverable (project, media, timeline, clips, edit operations, export). Inherited from the Video Editor / NLE grammar; without it the product is a review platform or asset manager.
2. **Shared persistent project** — the editing project lives in infrastructure designed for team access (shared storage, project server, or cloud), with identified members admitted to it — not a private local file passed around.
3. **Coordinated multi-user editing** — multiple members can perform editing work inside the same shared project, and the system coordinates their concurrent or interleaved changes so that simultaneous work does not destroy other members' edits (mechanism varies: locking, update-acceptance, or live merge).

Remove (1) → video review/approval platform or MAM. Remove (2) or (3) → single-user Video Editor / NLE with file exchange.

### L1 — Common Mature Structure

- **Access roles / permissions** beyond mere membership (view vs edit vs manage; per-project and per-user; enterprise role administration).
- **Coordination granularity machinery**: locks on named containers (bins, timelines) and on individual items (clips), read-only-until-unlocked semantics, "who is working on what" visibility.
- **Change surfacing**: update prompts with explicit acceptance, visual timeline comparison/diff, merge into a master timeline.
- **Shared annotation**: markers/comments with shared vs private visibility; built-in chat/comment threads attached to the work.
- **Shared media layer**: centralized or synced media libraries, proxy generation with automatic relinking to camera originals, database-backed media identity ("zero broken links").
- **Project infrastructure**: a project library/server/cloud account that outlives any single machine; live save/incremental persistence to the project database; read-only review mode.
- **Review & delivery surfaces around the edit**: publish-for-review, frame-accurate feedback relinked into the timeline, export/conform/deliver pipeline.

### L2 — Variant / Optional Structure

- **Substrate philosophy**: facility LAN shared storage ↔ cloud project server ↔ fully browser-native cloud editing.
- **Coordination cadence**: lock-based sequential work with explicit change acceptance (pro post facilities) ↔ live simultaneous same-timeline co-editing (cloud-native products). Both observed; neither is definitional.
- **Role specialization depth**: single general editor surface ↔ dedicated discipline pages (edit/color/VFX/audio) with per-discipline toolsets.
- **Segment machinery**: education/classroom (assignments, templates, LMS integration, engagement analytics) ↔ enterprise broadcast/film (newsroom integration, audio-post round-trips, security restrictions, SSO/org administration).
- **Intake extensions**: camera-to-cloud proxy ingest; watched-folder proxy generation.
- **Presentation/review surfaces**: branded share/present pages; watermarking (review-platform domain when standalone).

### L3 — Vendor-specific Structure (Research Notes only)

- Blackmagic: Blackmagic Cloud IDs/libraries, Organizations app + rental licenses, Blackmagic Cloud Store/Cloud Pod, Blackmagic Proxy Generator watch folders, live camera sync from Blackmagic cameras, Presentations app, free Project Server app, "world's only" positioning.
- Avid: Avid NEXIS shared storage, patented bin-locking, MediaCentral newsroom integration, Pro Tools round-tripping, ScriptSync/PhraseFind AI, tier split Standard/Ultimate/Enterprise, Media Composer First (free tier).
- WeVideo: PlayPosit interactive-video pillar, white-label API, assignment ideas library, district-scale admin, compare-vs-competitor marketing pages.
- Frame.io: Camera to Cloud, Mounted Storage/Frame.io Drive, forensic watermarking, asset lifecycle retention — all review-platform machinery.

## Vendor-specific Findings

- "Everyone on the same project at the same time" as the headline promise (Blackmagic) vs "conflict-free collaboration" via locking (Avid) vs "simultaneous editing is the bread and butter" (WeVideo) — three framings of the same underlying requirement (coordinated multi-user editing) with different coordination cadences.
- The pattern that grading locks individual clips while editing locks bins/timelines (Blackmagic) is product-specific machinery demonstrating granularity as a design variable; Avid's documented granularity is bins; WeVideo documents none. Treat "lock granularity by work type" as a design space, not a canonical rule.
- Frame-accurate comment round-trip into the timeline is documented by Blackmagic (Presentations ↔ Resolve) and exists in the review-platform world (Frame.io → Premiere integration); not verified as in-editor functionality in all sample products.

## Rejected Findings

- **"Collaborative video editing requires the cloud."** Rejected: facility shared-storage collaboration (Media Composer/NEXIS; Resolve private Project Server) is a first-class, older form. Substrate is L2.
- **"Real-time simultaneous same-timeline editing is the definition."** Rejected: the dominant professional model is lock-then-accept; live co-editing is the cloud-native pole. The invariant is *coordination*, not *live typing*.
- **"Collaboration here includes review/approval workflows — so Frame.io belongs in this Type."** Rejected: Frame.io performs no editing operations; its collaboration is around files and feedback. Fails the editing-execution test.
- **"A Collaborative Video Editor is just a Video Editor plus a chat/comments feature."** Rejected: comments/chat are surface machinery; the structural difference is the shared project + coordination model (membership, permissions, locks/merges, shared media, shared annotations).
- **"Collaboration features make the editor itself collaborative regardless of packaging."** Held with nuance: several NLEs embed collaboration as capability; the Type claim rests on products *centered* on the team workflow (see Boundary Findings / taxonomy note).

## Boundary Findings

1. **vs Video Editor / NLE (04.06 siblings)** — sharpest seam. Both share the same editing grammar (project/media/timeline/clip/export). Difference: the unit of work and its infrastructure. Single-user editors own a local project file; collaborative editors run a shared project with membership, permissions, and change coordination. Test: *remove the shared-project membership and coordination machinery — what remains is a complete single-user editor → the product is a single-user editor with optional team features; what disappears is the product's organizing spine → it is a Collaborative Video Editor.*
2. **vs video review & approval platforms (Frame.io-like)** — the platform executes no edit operations; feedback notes flow *to* an external editor. Test: *remove review/comment — an editor keeps editing; a review platform becomes nothing.* The directory (04.06) has no leaf for this category; products like Frame.io are currently uncatalogued (nearest existing leaves: Media Asset Management / MAM in §27) — recorded as a boundary issue.
3. **vs Media Asset Management / MAM (§27)** — MAM is custody/metadata/lifecycle of media assets; a collaborative editor's media layer exists to serve editing. MAM products do not assemble timelines.
4. **vs AI Video Editing Application (§04.21)** — different axis entirely: locus of execution (system executes edits) vs locus of collaboration (who executes). A collaborative editor's users execute edits; AI editors' users direct system-executed edits. The sibling research already records this seam.
5. **vs Collaborative Design Platform (§04.01)** — multi-user shared canvas of design objects (vector/pages/design files, live cursors) vs shared footage timeline. Canva-style products offer video as one format inside a design platform — design canvas remains the spine.
6. **Taxonomy note (joint review)** — collaboration is delivered as a built-in capability of several NLE products rather than as separate SKU categories, so the boundary between "NLE with collaboration" and "Collaborative Video Editor" is a posture gradient. The leaf is held as a distinct Type on the market-cluster test (an identifiable cluster of products and workflows organized around team editing: post facilities, cloud team editors, classroom co-editing), but it should be re-checked when the Video Editor and NLE leaves are processed.

## Historical / Market-Sample Check

Would older, regional, or platform-different products still fit?

- The pre-cloud form (1990s–2010s facility workflow: shared storage, shared project, bin locking, assistant/editor roles) satisfies L0 fully — collaboration predates cloud. ✓
- Cloud-era team editors (WeVideo-style) satisfy L0 with live co-editing instead of locks. ✓
- A hypothetical regional browser editor with project sharing but no locking — still fits L0 via permission-based coordination. ✓ (No specific regional product verified in this pass; no claim made.)
- The check confirms the invariant is *shared project + coordinated multi-user editing*, not any particular substrate, cadence, or feature generation. Live same-timeline co-editing stays out of the definition.

## Uncertainties

- Exact coordination behavior of WeVideo at scale (conflict handling when two users touch the same timeline region) is not documented publicly — no claims made about its merge/lock internals.
- Whether lock granularity in Media Composer extends beyond bins to timelines/clips with the same automatic semantics is not verifiable from the product page alone (bin locking documented; rest unverified).
- Premiere Pro Productions (team workflow) unverified — potential fourth data point lost to source inaccessibility.
- The degree to which review/comment round-trips into timelines exist natively across the sample (verified for Resolve's Presentations; plausible elsewhere; not asserted).
- Whether the market will continue to treat "collaborative" as a separate category or dissolve it into standard NLE capability — taxonomy judgment deferred to joint review.

## Final Synthesis

A **Collaborative Video Editor** is a timeline-based video editing application organized around a **shared persistent editing project** with identified team membership: the project lives in team infrastructure (shared storage, project server, or cloud), members work inside it under differentiated permissions, and the system **coordinates their editing work** — through locks, change acceptance, visual comparison/merge, or live co-editing — so simultaneous contributions compose into one evolving edit rather than overwriting each other. Around that spine, mature products share: granular locking and work visibility, shared annotations (markers/comments, shared vs private) with chat, a shared media layer (centralized/synced media, proxies with automatic relinking), per-user review and caching, project persistence with live/incremental save, and publish-for-review surfaces that round-trip frame-accurate feedback into the timeline.

The defining core is deliberately substrate- and cadence-agnostic: facility shared-storage bin-locking (the classic form) and browser-native live co-editing (the cloud form) are both implementations of the same three-part invariant. Products without editing execution (review/approval platforms) and products without shared-project coordination (single-user editors) sit outside the Type, whichever marketing words they use.
