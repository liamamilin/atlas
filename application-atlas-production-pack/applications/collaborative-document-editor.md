# Collaborative Document Editor

## Overview

A **Collaborative Document Editor** is a hosted writing application in which the document itself is a shared object: several people can open the same document, edit it at the same time, and always see one merged current version.

The defining structure is small:

```text
Shared Persistent Document
└── Shared access — the document's audience is extended beyond its
    original author through the product's sharing mechanism
    └── Concurrent multi-user editing merged into a single live current version
```

Everything else commonly associated with modern products — rich text formatting, comment threads, review modes, version history, live cursors, workspaces, guest links — is standard or optional capability, not the definition. A minimal self-hosted collaborative editor with plain text, pseudonymous authors, and nothing else is still recognizably this Type; a powerful word processor used by one person with files passed around by email is not.

The Type sits in deliberate contrast with the single-user Document Editor. The single-editor world runs on a save–copy–pass-around loop with manual reconciliation; the collaborative world replaces that loop with a shared document and a system that keeps everyone's view consistent. The boundary between the two is visible inside the market itself: where a product also serves older local clients, those clients may fall back to the save-and-merge mode — the older behavior reappearing as a compatibility path.

## Users & Context

The primary users are people who compose documents together:

- **co-authors** drafting a proposal, report, specification, essay, or minutes — several people writing and revising the same text, sometimes simultaneously
- **reviewers** who read a draft and respond through comments or suggested edits rather than by rewriting
- **readers** who only consume the finished document

One participant is normally the **owner or originator**: the person who created the document, controls who else may enter, and can always do everything the others can. Beyond that, the same person may play different roles on different documents — editor on one, commenter on another, viewer on a third — because the role is a property of the person-document pair, not of the person.

Typical contexts: team and organizational work (the dominant market), education and group study, community and open projects, and privacy-sensitive environments. The work surface is predominantly the web browser; native desktop and mobile apps usually act as companions to the same hosted document rather than as separate file editors.

## Core Model

### The defining core

**The document.** A durable, addressable unit of composition — a text-bearing document that persists independent of any user's session or device. Someone can return next week and find the document as it was left, with its accumulated content. The document is the thing that is shared, edited, discussed, versioned, and delivered. (The document grammar is prose-shaped: paragraphs, headings, lists, images, tables. The same collaboration machinery applied to a grid produces the sibling Collaborative Spreadsheet type; applied to slides, the Collaborative Presentation Editor.)

**Shared access.** The document's audience is extended beyond its original author through the product's sharing mechanism — by inviting named people, by granting an organization or team, or by distributing a link. Whoever is inside that audience can open the document; whoever is outside normally cannot. Sharing is both a convenience surface and the access-control boundary of the Type.

**Concurrent editing, one current version.** Multiple people can edit at the same time, and the system integrates everyone's changes into a single current version that all participants see. There is no "whose copy wins" problem in normal flow: the merged document simply is the document. Editing is therefore continuous — changes are visible to co-editors as they happen, and the saved state advances as people type rather than only when someone remembers to save.

Remove shared access and the product collapses into a single-user Document Editor with a cloud copy. Remove concurrent-merged editing and it collapses into the save–copy–pass-around loop. Remove the persistent document and it becomes an ephemeral live surface rather than a writing tool.

### What mature products add

These capabilities appear across essentially all mature products. They are not what makes the product a collaborative editor, but they make it practical.

- **Graded access roles** — a ladder of capabilities assignable per person, group, or link, typically spanning: view only → comment only → edit content → manage sharing (full access). Exact names and number of levels vary; the graded principle is common.
- **Sharing machinery** — invitation by name/email, shareable links (sometimes with expiry or password), external guest access for people outside the organization, and request-access flows when someone lands on a document they cannot open.
- **Live presence** — visible indicators of who is currently in the document and where they are working (flags, avatars, or cursor marks positioned in the text).
- **Authorship attribution** — edits and comments carry the identity of their author, so readers can see who wrote or changed what. In some products this is a persistent visual style (per-author colors); in others it surfaces in review tools and metadata.
- **Comments** — anchored remarks on the document content, with replies, @mentions of specific people, and navigation across the set. Comments are the async half of collaboration: they let people who are not editing concurrently still coordinate on the same text.
- **Review mode** — a mode that records proposed changes separately from the text so they can be inspected (whose change, what change) and individually accepted or rejected. Products differ in whether and how deeply they provide this: the word-processor lineage documents full tracked-changes machinery, while lighter products rely on suggestion flows or comments alone.
- **Version history** — the document's past states, accumulated from live editing and/or explicit snapshots, with the ability to view and often restore an earlier state.
- **Rich text composition** — formatting, headings, lists, tables, images, page/print semantics, templates, and import/export with office and PDF formats. (The most basic members of the Type do without parts of this; mature products do not.)
- **A container with search** — documents live somewhere: a drive of files, folders, or a nested workspace of pages — with listing, organization, and search across the collection.
- **Notifications** — for mentions, replies, access requests, and changes relevant to the user.

### One structure, many implementations

The core model is conceptual. The Variants section below shows how specific products realize each concept; the key implementations:

```text
Concept:        The document
Implementations: word-processor document, workspace page, minimal shared pad

Concept:        Shared access mechanism
Implementations: named-identity invites, organization/team grants,
                 share links, guest accounts, link-possession (minimal editors)

Concept:        Participants' identity
Implementations: organization-directory accounts, consumer accounts,
                 external guests, pseudonymous authors, anonymous editors

Concept:        The container
Implementations: flat drive/folder storage, nested workspace hierarchy,
                 bare instance of pads

Concept:        Review of proposed edits
Implementations: full tracked-changes with accept/reject and locking,
                 lighter suggestion flows, comment-only collaboration
```

A reader who has only seen one implementation — say, an organization account opening a shared browser document — should still be able to recognize the minimal self-hosted editor with anonymous authors and no formatting as the same Type, and the single-user word processor sharing files by email as a different one.

## How It Works

### Create and place the document

```text
Create a new document (blank or from a template), or import an existing file
→ the document is created in the product's hosted space
  (a drive/folder, a location in a workspace tree, or a fresh pad on an instance)
→ the creator owns it by default
→ compose: write, format, insert images/tables
```

At this point the document behaves like any document editor. What makes the Type is the next step.

### Share it

```text
Open the document's share control
→ choose the audience: named people / team or organization / anyone with a link
→ assign each a role (view / comment / edit, and possibly manage-sharing)
→ recipients receive an invitation or link and open the same document
```

From this moment the document has an audience, and every subsequent edit happens inside that access boundary. Access can later be widened, narrowed, or revoked; people who request access are approved or denied by someone who holds the right to decide.

### Edit concurrently

```text
Two or more participants open the same document
→ each sees live presence of the others (who is here, where they are working)
→ each types, formats, inserts content
→ the system merges everyone's changes into the one current version
→ every participant's view converges on the same text
```

The editing loop is the defining interaction of the Type: there is no separate "publish your changes" or "pull their changes" step. The user experience of co-editing is dominated by presence — seeing colleagues' markers moving through the text — and by the guarantee that the text being read is the text everyone else is editing.

### Review and discuss

```text
Participants attach comments to the content
→ others reply, @mention specific people, resolve the discussion
→ in products with a review mode, an author's proposed changes are
  recorded as suggestions: visible, attributed, individually acceptable or rejectable
→ accepted suggestions become part of the text
```

Review and comments are where sequential (not simultaneous) collaboration happens: one person's edits and another person's responses interleave over hours or days on the same persistent document.

### Revisit history

```text
Open the document's history
→ view earlier states (and, in some products, scrub through them in detail)
→ restore an earlier state if needed
```

History exists because the document is continuously editable by many people; it is the safety net that makes broad edit access acceptable.

### Finish and deliver

```text
Export or print the document (office formats, PDF)
→ optionally publish to the web as a page (in products that offer it)
→ the shared document remains the living master; delivered copies are derivatives
```

Unlike the single-editor world, delivery is an export step, not the end of the document's life. The shared document usually continues to evolve after any given export.

### Core, common, and optional capabilities

**Defining core** — without these, not a Collaborative Document Editor:

- a persistent, addressable document as the unit of work
- shared access extending the audience beyond one author
- concurrent multi-user editing merged into a single live current version

**Standard capabilities of mature products:**

- graded access roles and owner/creator privileges
- sharing machinery (invites, links, guests, request access)
- live presence
- authorship attribution
- comments with replies and mentions
- version history / snapshots
- rich text composition, templates, import/export
- a container (drive/folders or workspace) with search
- notifications

**Common variants and optional capabilities** — depend on product philosophy and segment:

- full tracked-changes review machinery (vs comment-only or lighter suggestion flows)
- offline editing (present in some products; not verified in detail here)
- end-to-end encryption / zero-knowledge hosting
- publish-to-web surfaces, embedding
- chat inside the document, video collaboration
- AI assistance for drafting and editing
- database/kanban/forms expansion (workspace-style products), or suite integration with mail, sheets, and slides

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### Document editor canvas

The center of the product.

- the document text with formatting, images, tables
- presence indicators of current co-editors, positioned in the content
- toolbar/controls for formatting and insertion
- primary actions: type and format text, insert content, navigate, undo

### Share dialog

The access-control surface of the document.

- who currently has access and at what role
- primary actions: invite people, set or change roles, create/copy a share link, adjust link behavior (e.g. expiry), remove access

### Comment threads

The discussion surface anchored to the content.

- remarks attached to text, with author, time, replies, @mentions, resolution state
- primary actions: add comment, reply, mention, resolve/reopen, navigate between comments

### Review-mode controls

Where offered, usually grouped with the review tools.

- current mode (direct editing vs tracked/suggested changes), whose changes are visible, accept/reject per change or in bulk, in some products the ability to lock the mode

### Version history

The document's timeline.

- list or timeline of past states with authors and times
- primary actions: preview an earlier state, restore it, name or mark milestones (product-dependent)

### Document list / container

The entry surface above individual documents.

- the user's documents organized by drive/folders or workspace structure, with recent activity
- primary actions: create document, search, organize, open

### Settings / admin surfaces

Ownership, security, and organizational governance around the documents (sharing policies, guest rules, export controls) — proportionally larger in organization-focused products.

## Important Rules / Behaviors

### There is one current version

The system, not the users, reconciles concurrent edits. In normal flow users never merge conflicting copies; the merged text simply exists. Behavior in pathological conflict cases is an implementation matter and is not uniform across products.

### Access level caps what a participant can do

A viewer can read but not change; a commenter can remark but not edit; an editor can change the content; sharing rights are typically a separate, higher capability. Where a document lives inside a hierarchy, access rules commonly inherit downward, and some products resolve overlapping grants by giving the broadest applicable access — details vary and matter in organization-scale deployments.

### Sharing is the gate

Editing happens only inside the granted audience. People outside it hit a request-access flow rather than a failure. Revoking access removes the person's entry; what they saw while inside is a governance question products answer differently.

### Attribution is visible

Edits and comments carry their author. In review machinery, proposed changes are attributed per reviewer and can be filtered by person. In the most attribution-centric products, even every keystroke carries its author's color through the document's entire history. The degree varies; the principle is common.

### Review mode separates proposal from text

When a review mode is engaged, recorded changes are proposals: they display independently of the clean text, they can be accepted or rejected one at a time or in bulk, and acceptance is what changes the document. Some products let the document owner lock review mode on, or share a document in a review context where tracking cannot be turned off — review is then an enforced workflow, not a preference.

### The degraded mode marks the boundary

A product that also serves older desktop clients may support a mode where co-editors see each other's changes only after saving. In that mode the application is behaving as a plain single-user document editor over a shared copy — and at least one major product documents exactly this fallback, which illustrates what the Type adds: the live merge.

### History accumulates by itself

Because editing is continuous and multi-user, history is gathered as a background property of editing rather than as explicit user saves (with explicit snapshots additionally available in some products). Restoring history is itself a change to the shared document, made within the same access rules.

## Variants

Common shapes of the Type:

- **Cloud-native document editors** — browser-first, sharing-centric, built for both individuals and organizations; the archetypal form of the Type.
- **Suite word processors with co-authoring** — full-formatting document apps with office-suite heritage (desktop lineage, deep page/print semantics) that gained real-time collaboration by moving the document onto hosted storage.
- **Workspace-embedded document pages** — documents as pages inside a larger nested workspace (teamspaces, databases, linked pages); the document surface carries the Type's core, while the surrounding platform drifts toward Wiki and Team Workspace territory.
- **Minimal self-hosted collaborative editors** — a bare instance of shared pads: real-time merging and authorship attribution with little else; extended by plugins; chosen for sovereignty and data-control reasons (education, public sector, journalism).
- **Encrypted zero-knowledge editors** — the same core structure with end-to-end encryption, where the server cannot read content; typically add owner concepts, document passwords, and guest/link sharing that works within the encryption model.
- **Publication-oriented shapes** — the shared document doubling as a publishable web page or site.

A variant remains a **Variant** while the defining core — shared document, shared access, concurrent merged editing — still applies. Where the surrounding platform's chat, tasks, and databases become the point, the product has become a different Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Document Editor | unit of work is a single-author file; sharing by export/copy/pass-around with manual reconciliation; no shared live current version |
| Wiki Application | primary object is a body of interlinked topic pages navigated as structured knowledge; documents are maintained more than composed |
| Knowledge Base Application | publishes curated knowledge for retrieval; the composition loop is secondary |
| Collaborative Spreadsheet | same collaboration skeleton (shared file, roles, comments, versions, presence) applied to a grid grammar |
| Collaborative Presentation Editor | the same skeleton applied to slide grammar |
| Team Workspace Platform | organizational container over multiple object types (chat, tasks, files, docs); document editing is one surface among several |
| Markdown Editor | composition-first, typically single-user and local; the sharing substrate is not the core |
| Digital Whiteboard / Collaborative Canvas | shared spatial canvas rather than linear text document |
| Note-taking Application | personal capture first; multi-user editing incidental |

The boundary with the **Document Editor** is the most important one, and it is porous in one direction: every major single-user document editor has added collaboration, so the market center of gravity has moved here. The leaf remains structurally distinct because the defining machinery — the sharing model, the role ladder, presence, review modes, and the merged current version — is a different architecture with different users and behaviors, not merely a feature added to a file editor.

## Representative Products

- **Microsoft Word (Microsoft 365)** — suite word processor with co-authoring; consumer + enterprise
- **Google Docs** — the market archetype of cloud-native collaborative document editing
- **Notion** — workspace-embedded pages with a deep permission model
- **Etherpad** — minimal self-hosted collaborative editor; sovereignty posture; 16-year lineage
- **CryptPad** — encrypted zero-knowledge collaborative suite

The definition was checked against the minimal end of the market (Etherpad: no accounts, no rich-text core, no suite machinery — still unambiguously this Type) to avoid defining the Type by the current cloud-suite implementation.

## Sources

Research date: **2026-09-06**

- Microsoft Support — Word help & learning: https://support.microsoft.com/en-us/word
- Microsoft Support — "Share and collaborate with Word for the web": https://support.microsoft.com/en-us/word/training/share-and-collaborate-with-word-for-the-web
- Microsoft Support — "Collaborate on Word documents with real-time co-authoring": https://support.microsoft.com/en-us/word/training/collaborate-on-word-documents-with-real-time-co-authoring
- Microsoft Support — "Track changes in Word": https://support.microsoft.com/en-us/word/training/track-changes-in-word
- Notion Help — "Sharing & permissions settings": https://www.notion.com/help/sharing-and-permissions
- Etherpad — https://etherpad.org/
- CryptPad Documentation — https://docs.cryptpad.org/en/
- Zoho Writer — Help Resources: https://www.zoho.com/writer/help/
- Google Docs — https://docs.google.com/ (product surface; documentation not reachable from the research environment)

> Sourcing limitations: official documentation for Google Docs and the operational help content for Zoho Writer could not be fetched during this research pass; both are treated as market anchors only, and no precise operational claims about them are made here. Where a capability is described from a single product's documentation (notably the depth of review-mode machinery and the save-based fallback mode), the wording is kept qualified. No numeric limits, default values, or timing rules are asserted anywhere in this document.
