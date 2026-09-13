# Research Notes — Collaborative Document Editor

Research date: 2026-09-06
Directory leaf: Collaborative Document Editor (§03.01 Documents & Writing)
Slug: collaborative-document-editor

---

## Research Goal

Understand what a Collaborative Document Editor is as an Application Type: what the unit of work is, how simultaneous multi-user editing actually appears to users, how access to a document is granted and controlled, what collaboration scaffolds (comments, review modes, version history, presence) attach to the document, and where the boundary lies against the single-user Document Editor, Wiki, Knowledge Base, Team Workspace, and the sibling Collaborative Spreadsheet / Presentation types.

## Initial Boundary (hypothesis before research)

- Core guess: a hosted writing application in which the document itself is the shared object — multiple identified users can edit the same document at the same time, and the system keeps one merged current version.
- Most likely confusions:
  - Document Editor (single-user, local files, save/share/export loop)
  - Wiki Application (interlinked topic pages, structure/navigation-first)
  - Knowledge Base Application (published knowledge for retrieval)
  - Team Workspace Platform (multi-app organizational container)
  - Collaborative Spreadsheet / Collaborative Presentation Editor (same collaboration machinery, different document grammar)
- Unknown points at start: permission granularity across products; whether access control is definitional or just common; whether rich-text formatting is definitional ( Etherpad-style plain-text collaborative editing might falsify that); offline behavior; version-history semantics.

## Research Questions

1. What is the unit of work (document/page/pad) and where does it live (drive, folder, workspace tree, flat instance)?
2. How does concurrent editing manifest: presence indicators, live merging, what the user sees when two people type at once?
3. How is access granted: identity invites, links, guests; what role ladder (view / comment / edit / manage)?
4. What scaffolds attach to the document: comments, suggestions/tracked changes, version history/snapshots, mentions, notifications?
5. What document-composition capabilities are expected (rich text, tables, images, import/export)?
6. What happens in degraded/legacy modes (offline, older clients, save-based sync)?
7. What product philosophies exist: suite-first, cloud-native doc-first, workspace-first, minimal self-hosted, encrypted zero-knowledge?
8. Historical check: does a minimal 2008-era collaborative editor (Etherpad) still satisfy the definition without suites, accounts, or rich text?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence quality |
|---|---|---|
| Microsoft 365 Word (Word for the web co-authoring) | document-suite heritage moved to cloud; consumer + enterprise | Tier-1 official support docs, 3 articles fetched |
| Notion | workspace-first, block-based pages; teams + enterprise | Tier-1 official help doc fetched (sharing & permissions) |
| Etherpad | minimal real-time collaborative editor, self-hosted, open-source; sovereignty posture; 16-year historical depth | Tier-1 official site fetched |
| CryptPad | encrypted zero-knowledge collaboration suite; privacy posture | Tier-1 official docs (index/TOC) fetched |
| Google Docs | the market archetype of cloud real-time document editing | positioning anchor only — official docs unreachable (see Sources) |
| Zoho Writer | suite-alternative (SMB tier) | positioning only — help hub fetched, guide content unreachable |

## Sources

Fetched 2026-09-06:

- Microsoft Support — "Share and collaborate with Word for the web": https://support.microsoft.com/en-us/word/training/share-and-collaborate-with-word-for-the-web — fetched OK
- Microsoft Support — "Collaborate on Word documents with real-time co-authoring": https://support.microsoft.com/en-us/word/training/collaborate-on-word-documents-with-real-time-co-authoring — fetched OK
- Microsoft Support — "Track changes in Word": https://support.microsoft.com/en-us/word/training/track-changes-in-word — fetched OK
- Microsoft Support — Word help & learning hub: https://support.microsoft.com/en-us/word — fetched OK
- Notion Help — "Sharing & permissions settings": https://www.notion.com/help/sharing-and-permissions — fetched OK
- Etherpad — https://etherpad.org/ — fetched OK
- CryptPad Documentation — https://docs.cryptpad.org/en/ — fetched OK (index/TOC level; subpages not fetched)
- Zoho Writer Help Resources — https://www.zoho.com/writer/help/ — fetched OK (hub level only)
- Zoho Writer user guide overview — https://www.zoho.com/writer/help/overview.html — fetched empty
- Zoho KB — https://help.zoho.com/portal/en/kb/writer — fetched empty (source abandoned after 2 failures)
- Google Docs — https://support.google.com/docs/... — request timed out ×2; https://www.google.com/docs/about/ — timed out ×1 (source abandoned)
- CryptPad user_guide/apps.html — HTTP 500 ×1 (index fetched instead)

Source-access limitations:
- Google Docs official documentation could not be fetched. No operational claims about Google Docs are made from memory beyond its uncontroversial market-anchor status (cloud real-time collaborative document editing, free consumer tier + Workspace offering).
- Zoho Writer operational detail could not be fetched; only its published help-hub scope statement is used.
- CryptPad evidence is TOC-level (structure names), not full article text; claims about it are kept to what the TOC titles and index text directly state.
- Word version history / AutoSave specifics were not fetched and are not asserted.

---

## Product A — Microsoft 365 Word (Word for the web + co-authoring)

Evidence layer: A (directly observed in official support docs).

### Key observations

- **Share**: Select **Share** → set permissions → enter names or email addresses → optional message → **Send**; alternative **Copy Link** to share a link (also via Outlook email).
- **Co-edit**: after sharing, work with others "at the same time"; who is editing shows next to the Share button; **colored flags show exactly where each person is working**; real-time view of changes when working in Word for the web.
- **Real-time vs save-based**: if using an older Word version or not a Microsoft 365 subscriber, you can still edit the document at the same time as others, **but without real-time collaboration — you must save periodically to see others' changes**. This is direct official evidence that the same product family spans both the save-and-merge mode and the live-merged mode, and names the live mode ("coauthoring, or real-time collaboration") as the current standard.
- **Comments**: Review → New Comment (or right-click); reply; **@mention** someone in a comment; delete; Show Comments; navigate Previous/Next between comments.
- **Track Changes**: on/off; scope selector **For Everyone vs Just Mine**; markup views (Simple Markup margin line / All Markup with per-reviewer colors / No Markup / Original); balloons vs inline display; filter by reviewer or by edit type; navigate Next/Previous; **Accept / Reject per change, all shown, or all**; **Lock Tracking with a password** so others cannot turn it off; documents "shared for review" may prevent turning Track Changes off; Reviewing Pane summary of remaining changes; printing can include or exclude markup; "Comments are no longer part of the Track Changes function" (separate feature).
- **Macros (.docm)**: content editable collaboratively; macro code requires **check out / check in** (an explicit exclusive-lock island inside the shared flow).
- **Training hub structure**: Create a document / Format text / Pages & layouts / Tables, pictures & watermarks / Save & print / **Share & coauthor** (Share a document, real-time co-authoring, Track changes, Accept tracked changes). Confirms document composition (formatting, pages, tables, pictures) is a first-class part of the product alongside collaboration.

## Product B — Notion

Evidence layer: A (directly observed in official help doc).

### Key observations

- **The page is the shared object**: `Share` at the top of **any page** — invite people, see/change who has access and at what permission level, copy the page's link, Publish tab (web publishing / Notion Sites).
- **Audience model**: share with specific workspace members/groups; **guests** = people outside the workspace invited by email (need their own Notion account); teamspaces (team-level spaces with own members and permission defaults; "default" teamspaces accessible to everyone in the workspace).
- **General access ladder**: Only people invited / Everyone at {workspace} (with "hide in search") / **Anyone on the web with link** (with link expiry).
- **Permission levels**: **Full access / Can edit / Can edit content / Can create (database-specific) / Can comment / Can view** — a graded role ladder on a single page object.
- **Permission mechanics**: subpages inherit parent permissions; **broadest level of access wins** across grants; moving a shared page to Private removes others' access; request access / request edit access flows with owner approval via Inbox.
- **Presence**: profile photos in the top bar; faded = not currently on page; hovering shows name and last visit; **clicking an active avatar jumps to where that person is reading/typing; avatars move next to the blocks being edited**; "last edited by / when" recorded.
- **Deeper granularity**: database page-level access rules via person properties (business/enterprise).
- **Governance**: enterprise security settings (disable public links, disable export).
- **Container**: workspace → teamspaces → pages → subpages (nesting is core); Private / Shared sidebar sections.
- Note: Notion positions "Docs" as a named product line in its own navigation, showing workspace products actively claiming the document-editor market.

## Product C — Etherpad

Evidence layer: A (directly observed on official site).

### Key observations

- **Self-definition**: "the editor for documents that matter… **Real-time collaborative editing** where authorship is the default, your server is the only server…"
- **Authorship is the product**: **every keystroke is attributed to its author; every revision is preserved; the timeslider lets you scrub through the document's entire history character by character; author colors make collaboration visible** — i.e., a minimal collaborative editor makes attribution and history the central features.
- **Sovereignty posture**: self-hosted, no telemetry, Apache 2.0, open data format, full data export built in; used by Wikimedia, EU public-sector institutions, schools where US cloud SaaS is not permitted, newsrooms.
- **Minimal core + plugin richness**: core ships small; ~290 plugins add **comments, images, tables, drawing, video chat, math, code highlighting, OAuth/LDAP/OpenID auth, AI plugins** — proving rich text, comments, and auth are NOT needed for the type to be recognizable (they are add-ons).
- **16 years old** (first-wave ~2009, still current v3.x): the historical/§24-style sample — pads on public instances are editable by anyone with the URL; identity is pseudonymous author colors.
- Also ships desktop/mobile apps, CLI client, terminal editor joining pads live.

## Product D — CryptPad

Evidence layer: A− (official docs index + TOC directly observed; article text not fetched).

### Key observations

- **Self-definition**: "a collaboration suite, **encrypted** and open-source"; zero-knowledge ("what our server can see" is a documented developer topic) — the server cannot read document content.
- **Rich Text app**: toolbar, view settings, headings/paragraphs editing, **comments**, import/export.
- **Per-document collaboration structures** (TOC): **Document history, Snapshots, Properties, Users and chat, Undo and collaboration modes** — same scaffold set, encrypted substrate.
- **Share/Access machinery** (TOC): **Access rights, sharing with contacts, sharing a link, embedding, shared folders, Access List, Owners** — owner concept + rights list even in an encrypted product.
- **Account types**: **Guest user** (anonymous editing), logged-in, premium — identity is optional.
- **CryptDrive**: folders, renaming, deleting, drive history, tags, templates, storage quota — a personal container for documents.
- **Teams**: team drive, members, invite, **roles and permissions**, administration.
- **Security variants**: passwords for documents and folders, self-destructing documents, remote disconnect.
- **Suite breadth**: rich text, document (OnlyOffice-based), presentation, spreadsheet, code/markdown, slides, form, kanban, diagram, whiteboard — the collaboration model repeats across document grammars.

## Product E — Zoho Writer (positioning only)

Evidence layer: A− (help hub text only).

- Published scope of its user guide: "creating, editing, **sharing and collaborating** on your documents" — collaboration named as core usage.
- Publishes comparison pages against MS Word and Google Docs ("alternative" positioning) — suite-tier document editor competing on the same structure.
- Has developer platform/APIs, integrations, KB, community — suite platform posture.
- No operational detail usable; no precise claims made.

## Product F — Google Docs (market anchor only)

Evidence layer: none beyond market position (official docs unreachable; 3 fetch failures).

- The archetype of the type: browser-native document editor built around sharing a document by identity or link with live co-editing.
- Because official documentation was unreachable, **no precise Google Docs claims** (edit windows, permission names, version-history mechanics, offline behavior) are recorded here or in the final document.

---

## Cross-product Comparison

| Structure | Word | Notion | Etherpad | CryptPad | Strength |
|---|---|---|---|---|---|
| Shared persistent document as unit of work | ✓ (document shared via link) | ✓ (page) | ✓ (pad) | ✓ (document/pad) | B — all four |
| Concurrent editing merged into one live current version | ✓ ("real-time collaboration") | ✓ (avatars move to blocks being edited) | ✓ (core promise) | ✓ (real-time suite) | B — all four |
| Save-based sync as explicit legacy/degraded mode | ✓ documented (older clients: save to see changes) | — | — | — | A, single product |
| Access roles on the document | ✓ (set permissions at share time) | ✓ (view/comment/edit/full ladder) | minimal (URL possession; auth via plugins) | ✓ (access rights, owners, access list) | B, with variation |
| Link-based sharing | ✓ (Copy Link) | ✓ (web-with-link + expiry) | ✓ (pad URL) | ✓ (share a link) | B — all four |
| External/guest participation | ✓ (names or email addresses) | ✓ (guests by email) | n/a (public pads) | ✓ (guest account type) | B |
| Live presence of co-editors | ✓ (who's editing; colored flags at position) | ✓ (avatar presence, position jump) | author colors (persistent attribution) | ✓ (users list; chat) | B |
| Authorship attribution | ✓ (track-changes colors per reviewer; comments by author) | ✓ (last edited by/when) | ✓ (keystroke-level, default) | partial (pseudonymous guests) | B |
| Comments on document content | ✓ (reply, @mention, navigate, delete) | implied ("Can comment" level; not fetched directly) | plugin | ✓ (rich text comments) | B |
| Review/suggestion mode | ✓ (Track Changes, accept/reject, lock) | not fetched | — | — | A, single product (treat as common-with-variation) |
| Version history / snapshots | not fetched | last-edited metadata | ✓ (revisions + timeslider) | ✓ (history + snapshots) | B |
| Rich text composition | ✓ (format/pages/tables/pictures training) | ✓ (blocks) | plugin (core is plain) | ✓ (headings/paragraphs) | B — but see L0 note |
| Container above the document | suite storage (drive-hosted) | workspace → teamspaces → nested pages | flat pads on an instance | CryptDrive folders / teams | B, wide variation |
| Notifications | not fetched | ✓ (inbox for requests/assignments) | — | ✓ (notification settings) | B− |
| Import/export | ✓ (edit a PDF; save/print) | export (security setting) | ✓ (data export built-in) | ✓ (per-app import/export) | B |
| Publish to web | — | ✓ (Publish tab / Notion Sites) | public pads (by nature) | embed | Optional |
| Chat inside the document surface | — | — | plugin (video chat) | ✓ (users and chat) | Optional |
| Offline editing | not fetched — no claim | not fetched — no claim | — (server-required) | — | unasserted |
| AI assistance | ✓ (Copilot surfaces in help) | ✓ (Notion AI) | plugin (choose-your-model posture) | — | Optional, differently positioned |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

```text
Shared Persistent Document
└── Shared access: the document's audience is extended beyond its
    original author through the product's sharing/access mechanism
    └── Concurrent multi-user editing merged into a single live
        current version
```

Three properties. Remove any one and the Type collapses into a neighbor:

- Remove **shared access** → a single-user Document Editor (even if the file is in the cloud).
- Remove **concurrent-merged editing** → the save/pass-around editing loop (exactly the degraded mode Word itself documents for older clients).
- Remove the **persistent document** (a durable, addressable text-bearing unit) → an ephemeral live surface, not a document editor.

Notes on what was deliberately kept OUT of L0:

- **Rich text formatting** — out. Etherpad's core is plain text with author colors and it is unambiguously this Type; rich text is the most common mature capability, not the definition.
- **Account identity** — out. CryptPad supports guest/anonymous editing; Etherpad authors are pseudonymous; Word/Notion are account-based. The invariant is sharing, not identification.
- **Specific role ladder** — out. Ladders vary (view/comment/edit/full in Notion; instance-admin/URL-possession in Etherpad; owner/access-list in CryptPad).
- **Comments / suggestions / version history / presence UI** — out. All are L1 scaffolds.
- **Workspace/teamspaces/drive** — out. Container shape varies (flat pads vs nested workspace vs suite drive).

§24 historical/market-sample check: Etherpad (2008-era design, current v3.x) satisfies the L0 with no accounts, no rich text core, no suite, no org workspace. A local-network collaborative text editor (SubEthaEdit-class) satisfies it conceptually (shared persistent doc over network + concurrent merged editing + invited access). The definition is not an artifact of the modern cloud-suite era.

### L1 — Common Mature Structure

Capabilities found across the sample (and expected by the market) that are not definitional:

- **Graded access roles** on the document (view → comment → edit → manage/share), with owner/creator as a special position
- **Sharing machinery**: invite by identity/email, shareable links (sometimes with expiry), guest/external access, request-access flows
- **Live presence**: who is in the document and where (flags/avatars/cursor positions)
- **Authorship attribution**: edits and comments attributed to authors (per-author colors in review tools or by default)
- **Comments/annotations** with replies and @mentions, navigable as a set
- **Review/suggestion mode** capturing proposed edits separately from the text (track-changes / suggesting analogs), with accept/reject decisions
- **Version history / snapshots** with the ability to revisit or restore earlier states
- **Rich text composition**: formatting, headings, lists, tables, images, page/print semantics
- **Organization container** above documents (drive/folders or workspace tree) with search
- **Import/export** (office formats, PDF) and **templates**
- **Notifications** for mentions, access requests, changes

### L2 — Variant / Optional Structure

- **Container philosophy**: flat drive of documents (suite/docs-first) vs nested workspace of pages (workspace-first) vs minimal instance of pads (self-hosted)
- **Identity posture**: org-directory accounts vs consumer accounts vs guests vs anonymous/link-possession
- **Review-mode depth**: full tracked-changes with accept/reject and locking vs comment-only collaboration
- **Encryption posture**: server-readable (standard SaaS) vs zero-knowledge/end-to-end encrypted
- **Deployment**: SaaS multi-tenant vs self-hosted sovereign instance
- **Surface strategy**: web-first; native app + web companion (suite heritage); terminal clients (minimal editors)
- **Publication**: publish-to-web sites, embedding, public pads
- **Offline editing** (claimed widely in the market but not verified here — no assertion)
- **Scope drift**: expansion into databases/kanban/forms (workspace platform), or chat/files/tasks containers (team workspace), or the same collaboration engine reused across spreadsheets/slides/whiteboards (suite)
- **AI assistance** embedded in authoring

### L3 — Vendor-specific Structure (research notes only)

- **Word**: Track Changes lock-with-password; review-mode sharing that prevents disabling tracking; For Everyone vs Just Mine scope; markup views (Simple/All/No/Original, balloons vs inline); Reviewing Pane counts; .docm macro check-out/check-in; Copilot integration
- **Notion**: teamspaces and "default" teamspaces; Full access/Can edit/Can edit content/Can create/Can comment/Can view ladder; database page-level access via person properties; broadest-access-wins override rule; link expiry; Notion Sites publishing; guest limits and allowed-email-domain member conversion; disable-export security setting
- **Etherpad**: timeslider character-level history scrubbing; author colors as the default attribution surface; ~290-plugin ecosystem (comments/images/tables/video chat/auth/AI); ueberDB storage abstraction; public instance scanner; CLI/terminal clients
- **CryptPad**: CryptDrive; zero-knowledge server (ChainPad real-time engine per developer docs TOC); document passwords; self-destructing documents; remote disconnect; owners/access lists on encrypted documents; OnlyOffice-based document app
- **Zoho**: comparison-marketing pages vs Word/Google Docs (positioning)
- **Google**: unverified — nothing recorded

## Vendor-specific Findings (summary)

See L3. None of these enter the final document except as neutral illustrations where the final document explicitly keeps them generic.

## Rejected Findings

- **"Rich text editor" as definitional** — rejected: Etherpad's plain-text core falsifies it; rich text is L1.
- **"Real-time cursors/avatars" as definitional** — rejected: Etherpad's persistent author colors are an attribution surface, not live presence; presence is L1.
- **"Workspace/teamspaces" as definitional** — rejected: suite products and Etherpad have no workspace concept in this sense; container shape is L2.
- **"Accounts and emails" as definitional** — rejected: guests/anonymous/link-possession models exist in two of four sampled products.
- **"Autosave/no-save-button" as definitional** — rejected: an implementation consequence of hosted single-version editing; Word for the web does not advertise a save button while legacy clients keep one; not researched deeply enough to generalize — kept qualitative.
- **"Offline editing" as definitional or even common** — rejected for this pass: not verified in any fetched source; left as uncertainty.
- **Treating Notion as a pure Collaborative Document Editor** — rejected for classification purposes: Notion's defining object is a nested page inside a workspace with databases and teamspaces; its page surface is one implementation of this Type's document model with strong drift toward Wiki / Team Workspace. It remains valuable as a boundary-informing sample.

## Boundary Findings

1. **vs Document Editor** — the sharpest boundary. A Document Editor's unit of work is a file owned by one author; sharing happens by export/copy/pass-around, and reconciliation is manual. The Collaborative Document Editor's unit of work is a shared, hosted document with one live merged current version. Microsoft's own documentation names this split: subscribers get "real-time collaboration"; older clients "can still edit the document at the same time… but you'll have to save the document from time to time" to see others' changes — the save-and-merge loop is precisely what the modern Type replaces. Remove concurrent-merged editing + shared access → Document Editor.
2. **vs Wiki Application** — a wiki's primary object is a body of interlinked topic pages navigated as structured knowledge; the document is usually short, topic-shaped, and maintained more than composed. A collaborative document editor's primary object is a freeform long-form document being composed. Notion straddles the seam (nested pages + wiki positioning) but its sharing/presence/co-editing machinery is document-editor machinery. Remove freeform composition and add topic-index navigation → Wiki.
3. **vs Knowledge Base Application** — KB is about publishing curated knowledge for retrieval; the collaboration loop (co-editing in progress) is secondary. Remove the composition workflow → KB.
4. **vs Collaborative Spreadsheet / Collaborative Presentation Editor** — same collaboration skeleton (shared file, roles, comments, versions, presence) but a different document grammar (grid / slides vs linear prose). They are siblings in the directory, not the same Type.
5. **vs Team Workspace Platform / Collaborative Workspace** — a workspace platform is a container over multiple object types (chat, tasks, files, docs). A collaborative document editor is a document-centric type; workspace expansion is L2 drift. Add multi-app containers with chat/tasks as primary → Team Workspace.
6. **vs Markdown Editor / Distraction-free Writing Application** — those are composition-first, typically single-user local tools without a sharing substrate as the core. Remove the shared-access + concurrent-editing core → Markdown editor.
7. **vs Digital Whiteboard / Collaborative Canvas** — spatial canvas object vs linear text document.
8. **Directory-adjacency note**: this leaf sits next to Document Editor, Markdown Editor, and Distraction-free Writing Application under 03.01. The research supports keeping it separate: the concurrent-merged-editing + shared-access core is a genuine structural difference, not just an audience variant. The seam with Document Editor is porous in one direction — every major single-user document editor has added collaboration; the leaf remains useful because the collaboration machinery (sharing model, roles, presence, review modes) is the defining structure of a large, distinct market segment.

## Uncertainties

- Google Docs: official docs unreachable; treated as market anchor only. All Google-specific behavior excluded.
- Zoho Writer: operational detail unfetched; used only for market-structure evidence (suite-alternative tier).
- Offline editing behavior, real-time latency/limits, concurrent-editor caps, edit windows, autosave intervals: not verified anywhere — no claims made.
- Notion comments: not directly documented in the fetched page; presence of comment-capable access level is the only evidence.
- Word version history: not fetched; excluded from claims.
- CryptPad: TOC-level evidence only; article-level mechanics (e.g., how "undo and collaboration modes" differ) not recorded.

## Final Synthesis

A Collaborative Document Editor is a hosted writing application whose defining core is: a shared persistent document, access to it extended to multiple people through the product's sharing mechanism, and concurrent multi-user editing that the system merges into a single live current version. Around that core, mature products add a stable standard structure: graded access roles, share links and guests, live presence, authorship attribution, comments with mentions, a review/suggestion mode, version history, rich text composition, a container (drive or workspace) with search, import/export, and notifications. Products vary by container philosophy (drive vs workspace tree vs flat pads), identity posture (accounts vs guests vs links), review-mode depth, encryption posture, and deployment (SaaS vs self-hosted). The type is not defined by the modern cloud-suite era: a minimal self-hosted pad editor with keystroke attribution satisfies the core with none of the suite machinery. The sharpest boundary is against the single-user Document Editor — exactly the save-and-pass-around mode that collaboration-era products document as their own legacy behavior.
