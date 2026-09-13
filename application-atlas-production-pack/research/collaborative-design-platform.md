# Research Notes — Collaborative Design Platform

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)
Sibling context: research/collaborative-canvas.md (§03.05, processed 2026-09-06) — its Boundary Finding #3 defines the seam this pass must hold: "Design canvases produce production-grade design artifacts with layers, components, and precision vector tooling; FigJam explicitly has no layers panel and positions ideation, not production design. Removal test: add layers/components/production fidelity → design platform."

---

## Research Goal

Understand, from real products, what a Collaborative Design Platform actually is: what the central working artifact is, how multi-user collaboration is structured (containers, roles, real-time mechanics), what design capabilities are core vs optional, and where the boundary lies with neighboring Types (Graphic Design Application, Template-based Design Platform, UI Design Application, Vector Graphics Editor, Collaborative Canvas, UX Prototyping Application).

## Initial Boundary (hypothesis before research)

- Core use: teams create visual design work together in shared files (the Figma-style category).
- Users: designers plus non-designer collaborators (PMs, engineers, writers, stakeholders).
- Nearest neighbors: Graphic Design Application (single-user), Template-based Design Platform (Canva-class), UI Design Application (04.15 — same archetype product), Vector Graphics Editor (04.03), Collaborative Canvas (03.05), UX Prototyping Application (04.15).
- Known tension: the market's flagship product (Figma) is the archetype of both this leaf and UI Design Application. The directory places this leaf under "General Visual Design", suggesting the collaboration structure — not the design subject — is the defining axis. To be verified.
- Unknowns: is real-time co-editing definitional or merely the mature implementation? Is the team/workspace container layer definitional? Is prototyping part of the Type or an optional capability?

## Research Questions

1. What is the central persistent artifact (file/document)? What is its internal anatomy (pages, canvas, layers, objects)?
2. How does multi-user collaboration actually work (live co-editing mechanics, presence, conflict handling)?
3. What is the organizational container model (workspace/team/project/folder/drafts) and how do permissions attach to it?
4. What roles exist (edit/view/admin/owner; members/guests) and what can each do?
5. Which design capabilities are core (vector tools, text, images, frames/boards, layers) vs common (components, styles, libraries, prototyping, handoff) vs optional?
6. What lifecycle does a design file have (draft → shared → reviewed → versioned → handed off)?
7. What are the main interfaces (file browser/dashboard, editor, comment mode, inspect mode, share modal, admin)?
8. What rules matter (single live version, permission inheritance, request-access, offline behavior)?
9. Where is the boundary against single-user design tools, whiteboards, template platforms, and prototyping tools?

## Representative Products

| Product | Why selected | Philosophy / tier | Evidence tier |
|---|---|---|---|
| Figma | Category archetype; browser-native; free→enterprise | cloud-first, multiplayer-native, product-development-centered | Tier 1 (official help center, multiple articles fetched) |
| Sketch | Native-Mac design tool that added cloud collaboration; different substrate philosophy | native-app-first + web companion workspace; subscription vs perpetual license split | Tier 1 (official documentation, multiple pages fetched) |
| Penpot | Open-source, self-hostable collaborative design; different deployment + business model | open-source, web-based, self-host or cloud | Tier 1 (official user guide, multiple pages fetched) |
| Canva | Boundary-informing only (Template-based Design Platform sibling) | template-first, non-designer audience | positioning-level only (homepage browser-gated; 1 attempt, abandoned) |
| InVision | Historical anchor (category predecessor, discontinued end of 2024) | collaboration-around-static-screens | not fetched (docs offline post-shutdown); conceptual context only |

Sample rationale: three primary products cover browser-native vs native-app vs self-hosted-open-source, consumer→enterprise tiers, and three different business models. Per workflow stop conditions, the three products' documentation converged on the same core structure; further sampling would mostly repeat evidence.

## Sources

Figma (all fetched 2026-09-06):
- https://www.figma.com/ (product positioning)
- https://help.figma.com/hc/en-us (help center root)
- https://help.figma.com/hc/en-us/articles/1500005554982 (Guide to files and folders)
- https://help.figma.com/hc/en-us/articles/35361119554711 (File and folder permissions)
- https://help.figma.com/hc/categories/360002042553 (Figma Design category — full article tree)
- https://help.figma.com/hc/en-us/articles/15297425105303 (Explore design files)

Sketch (all fetched 2026-09-06):
- https://www.sketch.com/help/ (help center root)
- https://www.sketch.com/docs/ (documentation root)
- https://www.sketch.com/docs/sharing-and-collaborating/ (+ real-time-collaboration/, using-your-workspace/)

Penpot (all fetched 2026-09-06):
- https://help.penpot.app/ (help center root)
- https://help.penpot.app/user-guide/ (user guide root)
- https://help.penpot.app/user-guide/first-steps/the-interface/ (interface tour)
- https://help.penpot.app/user-guide/account-teams/teams/ (teams & roles)

Canva: https://www.canva.com/ — returned a browser-compatibility gate (1 attempt; abandoned per network rule). No operational claims made for Canva.

No source-access limitations for the three primary products; all claims below are Layer A unless marked.

---

## Product A — Figma

### Key observations (Layer A unless noted)

**Positioning**: "The collaborative canvas for design, code, and AI"; "One workspace for your entire product development process." Product family: Figma Design, FigJam (whiteboard), Slides, Sites, Buzz, Draw, Make, Dev Mode, Motion, Weave. Help-center use-case links span UI design, UX design, graphic design, wireframing, brainstorming — the design file is subject-agnostic.

**Unit of work — the file**: "In Figma, you work in files, which can be organized into folders." Multiple file types (Design files, FigJam boards, Slide decks…), each with its own tools and file format (.fig, .jam, .deck…). Every file has a unique URL (with per-layer node IDs). Files can be saved as local copies.

**Live multiplayer as the stated contrast**: "Figma files are live and always up-to-date, so people can work on the same file at the same time. Having one live file gets everyone on the same page without the need to save, download, or pass documents back and forward." (Explore design files)

**File anatomy** (Explore design files): five regions — navigation bar, left sidebar (layers/pages/assets), canvas ("the file's main workspace where you can create and manipulate designs"), right sidebar (design/prototype properties; share; presence; audio), toolbar (creation tools). Pages: "Each page is its own canvas"; used for milestones, components, scratchpads, archives; shareable per page via link.

**Layer/object model**: every object added to the canvas is a layer; layer types include frame, group, component, instance, text, shape, image, auto layout, section, GIF/video. X/Y coordinates + Z-index ordering; layer order determines overlap. Containers: groups (collections, no own properties), frames (own dimensions/properties; auto layout, constraints, layout grids; nestable; device presets), sections (labeled canvas regions). Parent/child/sibling relationships.

**Design capabilities**: vector tools (vector networks, shape builder, stroke-to-path); text + text styles; fills/gradients/patterns/blend modes; strokes, effects, corner radius; auto layout ("use auto layout with CSS Flexbox in mind"); pencil tool. Figma Draw = advanced illustration tools inside the platform.

**Design systems**: styles (color/text/effect/layout-guide); components (create, variants, slots, instances); variables (collections, modes); libraries (publish, enable per team, review-and-accept updates, swap components/instances).

**Prototyping**: connections between frames, triggers, flows, overlays, smart animate, variables in prototypes; present in presentation view, on mobile, offline.

**Collaboration surfaces**: comments (add/reply/resolve, on canvas and prototypes); multiplayer tools (viewer history, spotlight, cursor chat, audio calls with captions); branching and merging (guide, share branch, get updates from main, branch review) — branch capability is Figma-specific among the sample.

**Permissions** (File and folder permissions): files organized into folders; per-file and per-folder permissions — can edit / can view / owner. Share modal lists access from broadest to most specific: plan/workspace access → inherited permissions → individual users → user groups (Org/Enterprise). Folder permissions inherit from parent team/folder; nested folders inherit from parent; file-level grants can widen but "you can't restrict someone's access below what they already have through their folder or team permissions". Viewers can comment, view layer properties, copy/export (unless restricted), view version history, interact with prototypes. Seats (billing) are separate from permissions. "Ask to edit" request flow for viewers.

**Containers**: drafts (personal space, private unless invited; Starter-plan drafts don't support co-editing) → folders/projects within teams; teams within plans; organizations/enterprise workspaces above teams. Connected folders: "two separate teams or organizations—like an agency and a client—work together in a shared folder."

**Version history**: "Every file has its own version history, where you can track the evolution of your designs. Explore previous iterations, or create new versions to capture milestones."

**Plan mechanics (L3)**: Starter plan limits (3 files per folder; unlimited drafts); unlimited files/folders on paid plans; folders nest up to 10 levels; projects→folders transition announced for Aug 2026.

## Product B — Sketch

### Key observations (Layer A)

**Positioning**: Mac-native design tool; product pages: Design ("Create with precision"), Collaboration ("Work better, together"), Prototyping, Developer Handoff, AI, MCP Server. Docs sections: Getting started, Interface and settings, Designing, Symbols and Styles, Libraries, Prototyping, Sharing and collaborating, Developer handoff.

**Collaboration requires the Workspace**: "With real-time collaboration, you can work together on the same document, see everyone's changes instantly, and never have to wonder about whether you're editing the right version of a document again." Requirements: a subscription (which "automatically includes all real-time collaboration features, along with a shared Workspace"); a Mac-only license includes only the Mac app (no collaboration). A document in the shared Workspace. A compatible Mac app version.

**Editor substrate**: real-time co-editing happens in the Mac app only. FAQ: "Can I use just my browser to collaborate? No. Real-time collaboration is a feature of the Mac app. You can still use the web app in your browser to view documents, comment, inspect, and share — but you can't co-edit a document in real time using only a browser." Web app = view/comment/inspect/share surface.

**Containers**: Workspace (subscription-only; "keeps all your documents together, in sync and available anywhere"); Members manage members, invite Guests; My Drafts (personal); projects in the Workspace; multiple Workspaces per account; Command Bar navigation; inbox/notifications; Discover.

**Real-time mechanics**: avatars of active collaborators in the toolbar; colored cursors matched to avatar colors; see which layer a collaborator is working on; "you'll only see their edits after they complete an action by clicking out of a layer… you won't see edits happen pixel-by-pixel"; "To keep the work of all collaborators safe, you'll only be able to undo your own actions"; same-layer simultaneous editing possible but undo/redo can override others — "it's best to avoid editing the same layer at the same time". Follow mode (view matches the followed person; can be disabled per user).

**Versions**: every change syncs in real time; closing the app "combines all your latest updates into a new version of the file, and saves it to your Workspace automatically"; manual File > Create Version; versions listed in the web app's Version tab; star versions as milestones; viewers can view/comment/inspect versions for handoff.

**Sharing/permissions**: save to Workspace → everyone in the Workspace sees the document; invite outsiders as Guests by email or share a link "Everyone can view"; set permissions to Edit for co-editing; document permissions docs section exists; embed fonts when sharing so all editors have them.

**Offline/local**: download a Workspace document, work locally, upload to create a new update ("might overwrite edits from other collaborators"); "If someone is working on the same document as you in your Workspace, you won't be able to push changes until they're gone"; offline changes sync on reconnect; deleted-object edits can't be applied.

**Comments**: comment pins dropped anywhere on the canvas; write, reply, resolve.

**Design capabilities (from docs tree)**: Designing (vector tools, stacks/layout), Symbols and Styles (symbols = reusable components; styling/effects), Libraries (shared symbol libraries), Prototyping, Developer handoff (inspect), MCP server (AI clients), iOS View & Mirror app.

## Product C — Penpot

### Key observations (Layer A)

**Positioning**: "Full-Stack Design"; open source (Kaleidos); product pages: Design, Code, Collaboration, Integrations & API, Self-host. Help center: User Guide, Technical Guide (installation/configuration/architecture), Plugins, MCP Server, FAQs, GitHub.

**Deployment**: "Cloud or Self-host" — the same collaborative design application delivered as SaaS or self-hosted. Migration guide exists for moving design systems from Figma.

**Interface — three main areas**: Dashboard, Workspace, View mode.
- Workspace: "infinite canvas where you can design without limits"; toolbar creates layer types: board, rectangle, ellipse, text, graphic, path, free drawing; pages ("A file can contain as many pages as you need. Each page has its own viewport… and its own layers"); layers panel; rulers + guides; color palette; typography palette; design properties sidebar (size/position always; stroke/shadow/blur optional); prototype mode (connect boards); inspect mode ("measurements, properties, and production-ready code… safer, view-only mode"); view mode; share/invite; history panel (undo/redo walk, per-change detail); comments mode; zoom; users indicator ("See how many users currently have the file open"); assets (file library + shared libraries: components, colors, text styles); design tokens; file status (saving state).
- Dashboard: teams, projects ("group design files… pretty much like a folder in a file system"), drafts ("design files that are not inside any project"), shared libraries, custom fonts, pinned projects, file cards (preview, rename/duplicate/move/download/delete), libraries & templates module.
- View mode: present boards, play interactions, comment, inspect (CSS/HTML/SVG code snippets), share prototype links "regardless of being at your team or even logged at Penpot".

**Teams & roles**: "A team is a group of members who collaborate on a collection of projects. Team members are allowed to work with any project or file within the team… depending on their permissions." Roles: Viewer (view, comment, inspect; no edit), Editor (create/import/edit/manage files and libraries), Admin (editor + change roles, invite, team settings), Owner (one per team; all admin + transfer ownership, delete team). "Your Penpot" = personal space where no members can be invited. Invitations by email with role; invitation links copyable ("specially useful for self-hosted installations, where sometimes SMTP email is not configured"); pending/expired states. No team size limits.

**Design systems**: components, variants, design tokens ("building blocks of UI elements, expressed in a format usable across design, tools, and code"), libraries (file library per file + shared libraries across team).

**Dev tools**: inspect design → production-ready code.

---

## Cross-product Comparison

| Dimension | Figma | Sketch | Penpot | Evidence |
|---|---|---|---|---|
| Unit of work | file (multiple file types; .fig) | document (in Workspace; .sketch lineage) | file | A×3 |
| Canvas | infinite canvas per page | Canvas in Mac app | infinite canvas per page ("design without limits") | A×3 |
| Objects | layers: frame/group/component/instance/text/shape/image/auto layout/section | layers, symbols, artboards, shapes, text | layers: board/rectangle/ellipse/text/graphic/path | A×3 |
| Layer ordering & nesting | Z-index; parent/child containers | layer list ordering | layers panel; boards as export units | A×3 |
| Real-time co-editing | yes, browser-native, "live" files | yes, Mac app only; edits land per completed action | yes (users indicator; multi-user) | A×3 |
| Presence | avatars, named cursors, follow (spotlight), audio | avatars, colored cursors, follow mode | users-open indicator | A×3 (depth varies) |
| Comments | pinned comments, resolve, on prototypes | comment pins, resolve | comments mode, notifications | A×3 |
| Version history | per-file version history | auto-version on close + manual versions + starred | history panel (change-level) | A×3 |
| Containers | drafts → folders/projects → teams → org/enterprise workspaces | My Drafts → projects → Workspace | drafts → projects → teams ("Your Penpot" personal) | A×3 |
| Roles | can edit / can view / owner; seats separate | Edit / view; Members / Guests | Viewer / Editor / Admin / Owner | A×3 |
| Permission inheritance | folder→file inheritance; widen at file level, can't restrict below inherited | workspace membership + per-document share settings | team-level membership governs projects/files | A×3 |
| Guests / external | guests; connected folders for agency–client | Guests by email; everyone-link | share links for prototypes (outside team) | A×3 |
| Components/styles/libraries | components, variants, styles, variables, published libraries | symbols, styles, shared libraries | components, variants, styles, design tokens, shared libraries | A×3 |
| Prototyping | connections, flows, triggers, smart animate | prototyping module | prototype mode connecting boards | A×3 |
| Inspect / dev handoff | Dev Mode (separate surface) | Developer handoff + web inspect | Inspect mode + code snippets | A×3 |
| Drafts (personal space) | yes | My Drafts | yes | A×3 |
| Import/export | import Sketch files; export static/animations; local copies | upload/download documents; local work + sync | export/import; migration guide from Figma | A×3 |
| Editor substrate | browser (all major platforms) | Mac app edits; web app views/comments/inspects | browser (self-host or cloud) | A×3 — variant, not defining |
| Branching/merging | yes | not observed | not observed | A×1 → product-specific/optional |
| Whiteboard sibling | FigJam (separate file type) | not observed | not observed | A×1 |
| AI assistance | AI features section; Figma agent in files | AI/MCP server page | MCP server | A×3 (depth varies) |
| Open source / self-host | no | no | yes (core identity) | A×1 — variant |
| Enterprise governance | org/enterprise workspaces, SSO section, user groups, billing groups | workspace admins, members/guests | team admins/owner; self-host | A×3 |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

A Collaborative Design Platform is a multi-user design application whose unit of work is a **shared, persistent design file** — a canvas of **editable design objects** (vector-first: shapes, text, images, frames/boards, organized as ordered, nested layers) — that **multiple people can open and work in together**, with the platform maintaining **one live, current version** rather than copies passed between users.

Three properties. Remove any one and the Type collapses into a neighbor:

1. **Shared persistent design file as the unit of work** — the design document lives in the platform (workspace/team/project containers), not on one person's disk. Remove → single-user design application with file exchange (Graphic Design Application / Vector Graphics Editor).
2. **Multi-user work on the same file** — several people access and change the same design document; mature implementations do this concurrently in real time with live presence. Remove → design tool with file sharing, or a review/annotation surface around static images.
3. **Editable design-object canvas** — content is structured, individually addressable design objects in ordered/nested layers (not freeform strokes/notes, not flattened images). Remove → Collaborative Canvas/whiteboard (freeform ideation) or raster painting (pixel substrate).

Not in L0 despite being near-universal today: browser delivery, cloud SaaS, real-time cursors, teams/workspaces hierarchy, comments, version history, components/libraries, prototyping, dev handoff, roles beyond "someone can edit".

### L1 — Common Mature Structure (present in all sampled products)

- Container hierarchy: personal drafts → projects/folders → team/workspace; file browser/dashboard with previews, search, pinning
- Graded participation: edit vs view roles; viewers can comment/inspect/export; guests and share links; request-access flow
- Real-time presence: named cursors/avatars, follow mode (depth varies)
- Comments pinned to the canvas with reply/resolve; notifications
- Version history: automatic preservation + named/starred versions
- Reusable design-system assets: components/symbols + styles + shared libraries across files
- Prototyping: interactive connections between frames/boards with a presentation/play surface
- Developer handoff: inspect mode with measurements, properties, code snippets, asset export
- Import/export and interchange with other tools; local copies
- Auto layout / flexible-layout systems for responsive structure
- Plugin/extension ecosystem; AI assistance (emerging)

### L2 — Variant / Optional Structure

- Editor substrate: browser-native (Figma, Penpot) vs native desktop app with web companion (Sketch — co-editing Mac-only)
- Deployment: multi-tenant SaaS vs open-source self-hosted (Penpot; invitation links usable without SMTP)
- Scope posture: general visual design vs product-development-centered; suite expansion into whiteboard (FigJam), slides, sites, motion, AI codegen
- Prototyping depth: simple connections → advanced logic/variables/expressions
- Design-token/variable systems (native in Penpot; variables in Figma)
- Branching/merging of design files (observed in one product — treat as optional, product-leaning)
- Enterprise governance depth: org hierarchy, workspaces, user groups, SSO, seat/billing models
- Audience posture: in-house product teams vs agency–client collaboration (connected folders/guests)
- Business model: freemium SaaS, subscription-with-workspace vs perpetual-license-without-collaboration (Sketch's split proves collaboration is the subscription's core), free open-source

### L3 — Vendor-specific (research notes only)

- Figma: Dev Mode as separate product surface; Figma Slides/Sites/Buzz/Make/Weave/Motion/Draw; branching & merging with branch review; cursor chat; audio calls with captions; spotlight; seat types (e.g., Collab seat gating product access); .fig/.jam/.deck formats; node-id URLs; frame presets; vector networks; slots; variables collections/modes; Starter plan file-count limits; 10-level folder nesting; projects→folders transition (Aug 2026); "Ask to edit"; viewer history.
- Sketch: Mac-app-only co-editing with web view/comment/inspect; Workspace subscription vs Mac-only license split; My Drafts; Command Bar; View & Mirror iOS app; edits land per completed action (not pixel-by-pixel); undo scoped to own actions; push blocked while another editor has the document open; starred versions; font embedding on share; "Active" collaborator status.
- Penpot: "Your Penpot" personal team; boards as page/export units; native design tokens; file status (saving state) indicator; history panel with per-change expansion; copyable invitation links for SMTP-less self-host; no team size limits; migration guide from Figma.

## Rejected Findings (considered and not promoted)

- **"Browser-based" is defining** — rejected: Sketch co-edits in a native Mac app; Penpot self-hosts. Substrate is L2.
- **"Real-time pixel-parallel editing" is defining** — rejected as stated: even Sketch deliberately lands edits per completed action; concurrency granularity is an implementation choice. The invariant is multi-user work on one live file, not a specific sync mechanism.
- **"UI design is the subject"** — rejected: the Type's own documentation positions design files for graphic design, social posts, presentations, wireframes, illustrations, and "anyone who wants to create or communicate visually". Subject-agnostic; UI-centered products are a variant emphasis (see Boundary Findings #2).
- **"Teams/workspaces are defining"** — rejected: a collaborative design tool with a single shared space and no org hierarchy is still the Type; hierarchy depth scales with customer tier (L1/L2).
- **"Components/design systems are defining"** — rejected: all sampled products have them, but a collaborative design platform without component reuse is still recognizable as the Type (early-era products); L1.
- **"Prototyping is defining"** — rejected: present in all three but a capability, not the structure that makes the Type; a collaborative design platform without prototyping remains one. L1/L2.
- **"Version history is defining"** — rejected: L1; persistence of the current file is the invariant, not the version machinery.
- **"Template-first content creation belongs here"** — rejected for this leaf: template-first platforms (Canva-class) start from browsed pre-made compositions for non-designer audiences; this Type starts from blank/shared files and freeform object editing. Boundary, not variant (see #3).

## Boundary Findings

1. **vs Graphic Design Application (04.01 sibling, unprocessed).** The graphic design application centers a single professional designer working in local files (desktop, print/illustration-oriented); the collaborative design platform centers a team working in shared platform-hosted files. Removal test: remove multi-user shared files → graphic design application. Gradient note: modern single-user tools add cloud sync and sharing; the seam is whether the shared multi-user file is the unit of work or a distribution convenience. Flag for joint review when that leaf is processed.
2. **vs UI Design Application / UX Prototyping Application (04.15 siblings, unprocessed) — taxonomy tension.** The market's flagship collaborative design platform is simultaneously the archetype UI design tool and prototyping tool. Working distinction adopted: this Type is defined by its collaboration structure (shared multi-user design files) and is subject-agnostic; UI Design Application is defined by its target artifact (user interfaces); UX Prototyping Application by its artifact (interactive prototype). Products straddle. **Flag for joint review when 04.15 leaves are processed; probable partial overlap.**
3. **vs Template-based Design Platform (04.01 sibling, unprocessed).** Template-first platforms start from a browsed library of pre-made compositions and constrain editing for non-designers; this Type starts from blank/shared design files with freeform object editing for designers (while offering templates as optional starters). Canva unreachable in this pass (browser gate) — boundary drawn conceptually; flag for joint review.
4. **vs Vector Graphics Editor (04.03, unprocessed).** Vector editors center precision illustration craft in single-user files; this Type centers shared production design. Vector tooling overlaps heavily (this Type embeds vector tools; one sampled product ships a dedicated illustration mode). Removal test: remove collaboration/shared files → vector graphics editor.
5. **vs Collaborative Canvas / Digital Whiteboard (03.05, processed).** Held per the sibling's own finding: design platforms produce production-grade artifacts with layers, components, precision vector tooling; canvases position ideation (no layers panel in the sibling's flagship evidence). Removal test: strip layers/components/production fidelity → collaborative canvas. The same vendor family ships both as separate file types (design file vs board), which is itself market evidence that they are different artifacts.
6. **vs UX Prototyping / design-handoff surfaces (historical anchor).** A collaboration surface built around static exported screens (comment/inspect/prototype on images, authoring elsewhere) does not satisfy L0 property 3 — the design file is not the editable working object. The category's discontinued predecessor (InVision-class) sits here: adjacent (prototyping/handoff), not this Type. Conceptual only; product docs offline post-shutdown.
7. **vs DAM / brand platforms (processed siblings).** Design platforms hold working design files in progress; brand-asset/DAM platforms hold approved, published expression masters. Different artifact states, different users. Consistent with brand-asset-guideline-platform's own boundary language.

## Historical / Market-Sample Check (§24)

- Would older, regional, platform-native products fit? The pre-collaboration baseline (single-user desktop design files exchanged by save/download/pass-around) is documented in the sample's own words — Figma's help center explicitly contrasts the live file with "the need to save, download, or pass documents back and forward". The Type is defined against that baseline; the L0 deliberately excludes everything that distinguishes the 2010s wave (browser, cloud, cursors) so that a hypothetical earlier shared-canvas design system, a self-hosted regional product, or a native-app product (Sketch) all satisfy it.
- Sketch's license split (Mac-only license = no collaboration; subscription = collaboration + workspace) is market evidence that "collaborative" is the load-bearing word in the Type name, not "design" (the design editor exists in both halves).
- Penpot (open-source, self-host, regional/EU-rooted) satisfies the L0 with none of the SaaS posture — definition is not delivery-bound.
- The discontinued predecessor generation (collaboration around static screens) fails L0 property 3 — correctly excluded as a different Type (prototyping/handoff), which keeps the definition from over-fitting to "anything design teams used together".

## Uncertainties

- Canva (Template-based Design Platform sibling) could not be fetched (browser gate, 1 attempt). The template-vs-freeform boundary is drawn conceptually and flagged for joint review; no operational claims made about Canva.
- InVision-class historical anchor not directly evidenced (product discontinued; docs offline). The exclusion argument rests on the L0 property test, not on fetched evidence.
- Real-time concurrency mechanics vary (Figma: continuous live; Sketch: per-completed-action). The final document states the invariant (one live shared file, multi-user) and describes co-editing qualitatively without asserting a uniform sync model.
- Whether the directory intends UI Design Application and Collaborative Design Platform as distinct Types is unresolved; flagged for joint review.
- Penpot's exact file-level permission granularity (beyond team roles) was not fetched in depth; role claims are limited to the documented team roles.

## Final Synthesis

The Collaborative Design Platform is the team-scale general visual design application: its defining structure is a shared, persistent design file — a canvas of editable, layered design objects — that multiple people open and change together while the platform keeps one live current version. Around that core, mature products converge on a standard structure: container hierarchies (drafts → projects/folders → teams/workspaces) with graded edit/view participation, guests and share links; live presence and follow modes; canvas-pinned comments with resolution; version history with named milestones; reusable components/symbols, styles, and shared libraries; prototyping connections with a presentation surface; inspect/handoff surfaces for developers; import/export interchange; and plugin/AI ecosystems. Products differentiate by editor substrate (browser vs native app), deployment (SaaS vs self-hosted open source), scope posture (general design vs product-development-centered, with suite expansions into whiteboarding/slides/sites), governance depth (free teams → enterprise orgs), and audience (in-house teams vs agency–client). The boundaries are sharp against single-user design applications (no shared multi-user file), whiteboards/canvases (no layered production objects), template platforms (browsed pre-made compositions vs blank freeform files), and prototyping/handoff surfaces (static screens vs editable design files). The soft boundary is UI Design Application — same flagship products, different defining axis (subject vs collaboration structure) — flagged for joint review.
