# Wiki Application

## Overview

A **Wiki Application** is a system for building and maintaining a corpus of interlinked pages that its users edit directly, where every change is recorded in durable, attributed version history that can be compared and restored.

It solves a specific problem: a body of knowledge that many people hold pieces of needs a shared home where any of them can improve it directly — without a publication bottleneck, and without fear that an edit destroys something. The wiki pattern answers with three commitments that reinforce each other:

- pages link to pages, so structure grows from use instead of being designed up front;
- the people reading the pages are the same people who can edit them — authorship is not gated behind a publication pipeline;
- every change is recorded and reversible, which is what makes open editing safe rather than reckless.

The boundary: a wiki application is defined by this pattern, not by who uses it or what the pages are about. The same core runs a public reference wiki, a fan-community wiki, a team's documentation wiki, or a personal wiki. When the corpus is scoped to an organization — entered through organizational identity and governed by layered access control — the product is the sibling Type **Enterprise Wiki**. When authorship is reserved to designated editors who curate and review a managed article set, it drifts toward a **Knowledge Base**.

## Users & Context

The population is the wiki's users, and most of them play more than one role:

- **Readers** — people looking for something the corpus holds: how something works, what happened, how to do a task. Reading dominates by volume.
- **Contributors** — the same people acting as authors: fixing an outdated step, adding a missing page, linking two related topics. The defining posture of the Type is that the product's users *can* edit directly — whether that means everyone, a community's members, a small author group, or (on a personal wiki) one person depends on the wiki's access model.
- **Maintainers / administrators** — people responsible for the wiki as a whole: access configuration, organization, templates, spam and abuse controls, backups, extensions.

Typical corpora: public reference and knowledge wikis, fan and game-community wikis, project and team documentation, community handbooks, personal notebooks kept in wiki form. Typical moments: "how do I do X?", capturing the outcome of a decision, updating a page after something changed, writing a link to a page that should exist and filling it in later.

Deployment contexts span self-hosted wiki engines (from lightweight flat-file engines to feature-rich platforms), hosted wiki farms where many communities run their wikis on shared infrastructure, wiki-at-the-core suites, and single-user personal wikis.

## Core Model

### The Defining Core

```text
Interlinked page corpus
├── Page  (the unit of knowledge)
│   └── Version history  (attributed, diffable, restorable)
├── Links between pages  (structure emerges from use)
└── Direct editing by the product's users  (the audience are the authors)
```

Three properties. If any one is removed, the product is no longer recognizable as a wiki:

- **Interlinked page corpus** — the unit of knowledge is the page. Pages reference each other through links; related topics connect directly; the corpus's structure is emergent, grown by contributors through links and light organization rather than fixed by a schema or a publication pipeline. Without the interlinked corpus, the product is an editable website, a document repository, or a blog.
- **Direct editing by the product's users** — the wiki's own users create and edit pages in place. There is no separate publication step between writing and reading: the "Edit" affordance lives on the page itself. How broad the editor population is — everyone, a community's members, a restricted group of authors, a single person — is set by the wiki's access model and varies by deployment; that editing is direct is the invariant. Without it, the product is a published website, a CMS, or a help center.
- **Durable version history with restore** — every change is recorded with who changed what and when; revisions can be compared and restored; deleted content is recoverable. This is the mechanism that makes open editing viable: mistakes are recoverable, accountability is visible, and no contributor needs special permission to be trusted with a page. Without it, open editing degrades into a shared notepad.

### Standard Capabilities

Mature wiki products add a consistent layer that makes the core practical. These are widespread expectations, not what makes the product a wiki:

- **Recent-changes stream** — what changed, where, by whom, with an edit comment; the corpus's pulse.
- **Search** — full-text search across the corpus.
- **Backlinks and orphan detection** — which pages reference a page; which pages nothing references.
- **Link-first page creation** — a link written to a page that does not exist yet renders as an invitation (marked distinctly — for example with a question mark) and opens the editor when followed; the corpus grows along the paths readers actually need.
- **Organization layer** — a light structure over the flat corpus: page groups, ordered page trees ("structures"), or path-based trees, plus free-form categories or labels for cross-cutting topics.
- **Templates** — reusable starting points for recurring page types.
- **Attachments and media** — files and images attached to or embedded in pages.
- **Watch / notification** — follow a page (or an area) and be notified of changes, usually by email.
- **Accounts and access control** — from none at all (fully open wikis) to password protection and user accounts with groups; permissions commonly granular enough to control reading, editing, and uploading per page, per area, or site-wide.
- **Sandbox** — a practice page for learning the editing rules safely, kept separate from real content.
- **Talk / comments** — discussion attached to a page (talk pages or threaded comments), separate from the page's content.
- **Page operations** — rename, move, copy, lock (prevent editing), delete (recoverable), undo, export.
- **Export, print, syndication** — printable views, page or corpus export, web feeds of changes.
- **Extension ecosystem** — plugins/recipes/modules that add markup, macros, embeds, and features.
- **Theming and multilingual support** — customizable appearance; multi-language content and interface.
- **Spam and abuse controls** — filtering, blocking, and restricted editing rights where the wiki accepts public contributions.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:            Page (unit of knowledge)
Implementations:    page, topic, entry

Concept:            Organization layer
Implementations:    page groups, ordered structures/trees, path-based trees

Concept:            Editing surface
Implementations:    wiki markup, Markdown, visual/WYSIWYG editor, plain HTML

Concept:            Version history
Implementations:    built-in revision store, git-backed history

Concept:            Identity / access
Implementations:    anonymous editing, password protection, user accounts + groups,
                    enterprise directory/SSO
```

A reader who has only seen a modern cloud-style wiki should still be able to recognize a classic self-hosted markup wiki — and vice versa — from this model.

## How It Works

### Establish the wiki and its access posture

```text
Deploy the engine (or create a space on a hosted platform)
→ choose who can read and who can edit
  (fully open · public-read/restricted-write · members-only · fully private)
→ configure identity: none, passwords, accounts + groups, or directory/SSO
→ seed the starting pages (home page, sandbox)
```

A wiki starts nearly empty on purpose: its value is accumulated by its users, not pre-loaded by a documentation team.

### The read → edit loop

```text
Open a page
→ choose Edit
→ modify the content (markup or visual editor), often with preview
→ save — the change is recorded as a new revision (who, what, when)
→ readers see the updated page; watchers (if any) are notified
→ anyone can compare revisions and restore an earlier state
```

This loop is the Type's heartbeat. There is no assignment, no approval queue, no publish step between the edit and the reader (except where a wiki deliberately adds revision approval — see Variants).

### Link and grow

```text
While writing, link to a page that does not exist yet
→ the link renders as an invitation (marked distinctly — for example with a question mark)
→ following it opens the editor for that new page
→ save — the page exists; the referencing page's link turns ordinary
→ backlinks accumulate; pages nothing links to surface as orphans
```

Linking is the organizing act. The corpus grows along the paths its readers actually need, and backlinks expose how a page is really used.

### Organize and discover

```text
Place pages into groups / structures / categories (or leave them linked-only)
→ users find content via search, the organization layer, backlinks, and listings
→ users follow activity via the recent-changes stream and watches
```

Structure is maintained, not designed: the organization layer gives coarse order, links carry the rest, and orphan detection shows what has fallen out of the graph.

### Maintain over time

```text
Content ages or errors → any editor fixes it; history preserves every prior state
→ pages are renamed, locked, or deleted (recoverable)
→ open wikis attract abuse → spam filters, blocking, and restore answer it
→ quality-controlled wikis may hold revisions for approval before they display
```

Maintenance is the chronic weakness of the pattern — open editing produces content easily, but nothing automatically keeps it current. Products answer with attribution (every revision names its author), recent-changes streams, watches, and restore; communities answer with editing norms.

### Core vs common vs optional

**Defining core** — without these, not a wiki:

- interlinked page corpus
- direct editing by the product's users
- durable, attributed, restorable version history

**Standard capabilities** — present in most mature products:

- recent changes, search, backlinks/orphans, link-first creation
- organization layer, categories, templates, attachments
- watches/notifications, accounts + access control, sandbox
- talk/comments, page operations (rename/lock/recoverable delete)
- export/print/feeds, extensions, theming, multilingual
- spam/abuse controls (where the wiki is open)

**Variant / optional** — depends on scope, era, deployment:

- corpus scope: public / community / group / personal / organizational
- identity: anonymous editing, passwords, accounts, enterprise SSO
- storage: flat files, database, git-backed
- markup: wiki syntax, Markdown, WYSIWYG, HTML
- packaging: standalone engine, hosted farm, suite-embedded, personal single-file
- revision-approval workflows for quality-controlled public wikis
- edit-conflict handling and save-as-draft (product-dependent)
- structured data in pages (forms, trackers) — the "application wiki" drift

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Page view

The primary reading surface.

- page title, content, attachments, metadata (last edited by whom/when)
- primary actions: edit, view history, watch, talk/comment, print/export, rename/move/lock/delete (where permitted)

### Editor

The primary writing surface — visual rich-text in modern products, lightweight markup in classic ones, often both.

- formatting, links (with completion over existing pages), images, tables, embeds
- primary actions: save (creating a revision), preview, cancel; sometimes save-as-draft

### Page history

The accountability surface.

- list of revisions with author and time; side-by-side or inline comparison; restore/revert to a prior version; undo of the latest edit

### Recent changes

- stream of what changed across the corpus: page, author, time, edit comment
- primary actions: open the page, open its history, diff a revision

### Search

- full-text search across the corpus, sometimes scoped to an area
- primary actions: open results, filter

### Backlinks / orphans / listings

- which pages reference this page; pages nothing references; page listings with per-page metadata (versions, links, last edit)
- primary actions: navigate, create missing pages, prune orphans

### Organization browse

- groups / structures / categories as entry points into the corpus

### Sandbox

- a practice page for trying out editing safely, kept separate from real content

### Administration

- access configuration (identity, groups, permissions), templates, extensions, spam controls, backups/export

## Important Rules / Behaviors

### The access model defines the editor population

A wiki's access settings decide who the "users who edit directly" are: everyone (fully open wikis, where editing may not even require an account), a community's registered members, a restricted group of authors, or a single person. The breadth varies deliberately; what does not vary is that editing is direct — the reader's surface and the author's surface are the same pages.

### Every edit is attributed and reversible

Each save creates a revision recording who changed what and when. Revisions can be compared and restored; deletion is normally recoverable. This is not an audit nicety — it is the mechanism that makes open editing safe, and it is why wikis commonly serve as records of decisions and processes.

### Links are the structure

Writing a link to a missing page is how new pages are invited into existence; backlinks show how a page is referenced; renaming a page carries its inbound links with it (where the product supports link-following rename); pages nothing references surface as orphans. The corpus's shape is an emergent property of its links, and the product's machinery treats links as first-class structure.

### Open editing attracts abuse — and the pattern answers it

Wikis that accept contributions from the public face spam and vandalism. The standard answers are structural, not social only: spam filtering and blocking, restricted editing rights, and — above all — fast restore of defaced content from history. The pattern's own description treats "restore what was destroyed" as a built-in expectation, not an add-on.

### No publication gate

Editing and publishing are the same act. This is the structural contrast with CMS- and knowledge-base-style systems, where a designated author publishes through a review pipeline and readers never touch the record copy. Some public wikis add revision approval as a deliberate exception; the default posture remains direct.

### Concurrency is expected

Multiple people edit the same corpus, sometimes the same page. Mature products handle simultaneous edits (the mechanism varies by product); some also let editors work on drafts before saving.

## Variants

- **Public reference wiki** — large, open, quality-governed corpora built by distributed contributor communities; the most famous encyclopedia is this variant realized on wiki software. Quality machinery (norms, and in some products revision approval) is heaviest here.
- **Community / fan wiki** — a community's shared knowledge base about a game, show, hobby, or world; open to the community's contributors.
- **Group / project / documentation wiki** — a team or project's documentation home; same pattern as the enterprise flavor but without organization-wide identity and governance; often the on-ramp to the sibling Type.
- **Personal wiki** — the pattern with an editor population of one: interlinked pages and history for personal notes and notebooks; overlaps Personal Knowledge Management territory (see Related Types).
- **Wiki farm / hosted platform** — many wikis operated on one installation or service; the operator's unit is the individual wiki, each with its own corpus, access model, and appearance.
- **Suite-embedded wiki** — the wiki as the page-and-linking core of a broader product that also carries forums, blogs, file galleries, trackers, and calendars; the wiki machinery stays recognizable inside the suite.
- **Classic markup engine vs modern engine** — lightweight markup editing, flat-file or simple storage, password/group protection vs rich editors, database or git-backed storage, granular permissions and enterprise identity. The defining core is identical across the two generations.

A variant remains a **Variant** unless it changes the core: adding organizational identity and layered governance produces the sibling Type Enterprise Wiki; replacing open editing with curated, owned, review-managed authorship produces a Knowledge Base.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Enterprise Wiki | the same wiki pattern plus organization-scoped identity, layered access governance, and an internal audience; this leaf holds the pattern without that scope |
| Knowledge Base Application | curated, owned, review-managed article set answering questions; readers react but never edit the record copy; the wiki's corpus is emergent and maintained by its users — the seam is the organizing principle, not the audience |
| Help Center | customer-facing published support publication; the reader-facing site is the product's center; a wiki's center is the user-authored corpus |
| Online Encyclopedia | a reader-facing reference product defined by its encyclopedic content; a wiki application is defined by the editing pattern and is indifferent to content genre — the largest encyclopedia happens to be built on wiki software, which is the overlap seat, not an identity |
| Content Management System / Website Builder | publisher-governed design and publication of a site; the wiki's users edit the corpus directly with no publication pipeline |
| Collaborative Workspace | a governed team container holding heterogeneous content (docs, data, files) under membership; the wiki's world is the emergent interlinked page graph with open editing |
| Collaborative Document Editor | freeform long-form document composition; the wiki's unit is the short, topic-shaped, interlinked, continuously maintained page |
| Online Forum / Q&A Community | discussion organized as threads around topics or questions; the wiki is organized as a page corpus; page comments/talk are an adjacent capability, not a forum |
| Personal Knowledge Management / Note-taking Application | the individual's link-network of notes is the point; a personal wiki is the degenerate single-user case of the wiki pattern and drifts toward this territory |
| Blogging Platform | a reverse-chronological stream of dated posts; wiki pages are topic-shaped and maintained in place rather than accumulated as a feed |

The boundary with **Enterprise Wiki** is the most important one: the wiki pattern is shared, and organizational scope is what the sibling leaf adds. The boundary with the **Knowledge Base Application** is the most blurred in market language — products self-label across it — but the organizing principles differ: emergent member-maintained corpus vs curated owned review-managed answers.

## Representative Products

- MediaWiki — the open-source engine behind Wikipedia and other large public wikis; extension ecosystem; the scale anchor
- PmWiki — classic lightweight engine; collaborative-authoring philosophy; flat-file storage; password- or account-based access
- Tiki Wiki CMS Groupware — the wiki pattern at the core of a full CMS/groupware suite
- Wiki.js — modern engine; Markdown/WYSIWYG editing; git-backed storage; module system
- DokuWiki — file-based open-source wiki engine (official documentation site unreachable during research; listed as a representative of the engine pole without operational claims)

The definition was checked against the pattern's origin generation (open editing, anyone-can-edit, restore mechanisms, recent changes — none of the modern machinery) to avoid over-fitting to the modern engine pattern.

## Sources

Research date: **2026-09-09**

- PmWiki — official site and documentation (home; Features; Philosophy; WikiWikiWeb concept page) — https://www.pmwiki.org/wiki/
- Tiki Wiki CMS Groupware — official documentation (Documentation home; Using Wiki Pages; keywords index) — https://doc.tiki.org/
- Wiki.js — official website (feature pages) — https://js.wiki/ ; official repository README — https://github.com/Requarks/wiki
- MediaWiki — official repository README — https://github.com/wikimedia/mediawiki
- DokuWiki — official repository — https://github.com/dokuwiki/dokuwiki

> Sourcing limitation: the official documentation sites for MediaWiki (mediawiki.org), DokuWiki (dokuwiki.org), Fandom, Wikipedia, and TiddlyWiki could not be fetched from the research environment (timeouts/oversized responses) and were abandoned after repeated attempts. MediaWiki is therefore evidenced at official-repository positioning level only, and no MediaWiki-specific operational claims are made. The hosted-farm and personal-wiki poles are evidenced indirectly (farm concept via PmWiki and Tiki documentation; personal pole via the paired Research Notes' cross-reference to the Personal Knowledge Management research). Precise vendor figures (language counts, extension counts, version specifics) are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the joint review with the Enterprise Wiki research) are recorded in the paired Research Notes.
