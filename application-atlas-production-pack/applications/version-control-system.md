# Version Control System

## Overview

A **Version Control System** is the machinery that records successive versions of a set of files over time, so that any recorded version can later be inspected, compared, and restored — and so that parallel lines of work can proceed independently and be reconciled.

The defining structure is small:

```text
Repository (the versioned store of record)
└── Working copy (editable checkout of the files)
    └── Deliberate recording of versions (commits / check-ins)
        └── Navigable history (what changed, who changed it, compare any versions)
            └── Branches and merges (parallel lines of development, reconciled)
```

Two boundaries matter immediately:

- A version control system is **not** the website where teams host, browse, and discuss that work. The hosting venue is a separate Application Type (Source Code Hosting Platform) that is built *on top of* version control machinery. The machinery itself — a repository, a working copy, recording, history, branching — functions completely without any account system, web surface, or venue.
- A version control system is **not** an automatic backup. Backup keeps copies of the current state; version control keeps versions the user deliberately authored, with attribution and description, and provides comparison and reconciliation machinery backup never has.

Although overwhelmingly used for software source code, the machinery is content-agnostic: the official documentation of the researched products explicitly extends it to any file collection, including images, layouts, audio, and 3D assets.

## Users & Context

The primary user is a **developer** working on a body of files — typically source code — who needs their work to be recoverable, reviewable, and combinable with other people's work.

Typical reasons to sit down in front of this machinery:

- record a completed unit of work so it can never be silently lost ("commit")
- look back at what changed between two points, and who made each change
- recover an earlier state of a file — or the whole project — after a mistake
- start an independent line of work (an experiment, a fix, a release) without disturbing the main line
- bring a long-running side line back into the main line, reconciling overlapping edits

Secondary users include **designers and artists** versioning binary assets (the enterprise-scale products in this Type are built around 3D art and design files), and **release/build engineers** who rely on recorded history as the stable input to builds.

The work environment is unusual for an Application Type: there is no single "app window". Users operate the machinery from a command line, from dedicated GUI clients, and from version-control panels embedded in code editors and IDEs — all surfaces onto the same core operations. A single developer can use it entirely alone on one machine; teams deploy a shared repository server; organizations connect it to hosted collaboration venues.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as a version control system:

- **The repository** — a persistent store that remembers every recorded version of the tracked files. It is the project's memory, held in one place (or replicated across peers in distributed products) rather than in any individual's working files. The official documentation of one centralized product makes the contrast itself: the repository "is a kind of file server" — what makes it different is that as files change, it "remembers each version". Remove the remembering → an ordinary file server.

- **The working copy and the recording loop** — the user does not edit history directly. They edit files in a *working copy* (a checkout of a recorded version), and when the work reaches a state worth keeping, they deliberately **record** it: a commit (also called check-in or submit) that captures the current state of tracked files, attributed to an author and described by a message. History exists only because of these deliberate acts. Remove the deliberate recording → automatic backup or file synchronization.

- **History navigation** — every recorded version stays retrievable. The user can read the history (what changed, when, by whom), compare any two recorded states file-by-file and line-by-line (a *diff*), and **restore** any recorded version into the working copy — a single file or the whole tree. Remove the comparison and recall → an append-only change log that nobody can work from.

- **Branching and merging** — development can fork into independent lines (branches): an experiment, a fix, or a release can proceed without disturbing the main line. A branch's changes can later be brought back together (**merge**); when both lines changed the same content, the system flags a **conflict** and the human decides how to combine the versions. Remove branching → versioned file history (the document-version-list shape), not development tooling.

### Capabilities Shared by Mature Products

Modern products almost always carry the following. They make version control practical, but they are not what makes it version control:

- **Tags** — named markers on recorded versions ("this one is release 2.1"), so significant points can be referenced without memorizing revision identifiers.
- **Sharing recorded work** — updating the working copy with other people's recorded work and publishing one's own (push / pull / update / submit); in distributed products, repositories themselves are synchronized between machines.
- **Two-level undo** — discarding uncommitted edits in the working copy; and reverting changes that were already recorded, by adding a new recorded state that undoes them.
- **Ignore rules** — per-project patterns listing generated files (build outputs, editor scratch files) that recording should always skip.
- **History annotation** — line- or file-level queries answering "who last changed this, when, and why" — the machinery's answer to "who introduced this problem".
- **Safety rails** — guards against losing unrecorded work (e.g., refusing to delete files whose content was never recorded, refusing a commit with an empty description).

### One Machinery, Many Implementations

The core is conceptual; real products realize each concept differently:

```text
Concept:          Identity of a recorded version
Implementations:  content checksum identifying the version (distributed products),
                  a sequential number for the whole repository,
                  a numbered change record assembled per submission

Concept:          Preparing a commit
Implementations:  a two-step stage-then-commit model (select content first),
                  committing selected files directly,
                  assembling a pending change record on the server

Concept:          A branch
Implementations:  a lightweight movable pointer to a recorded version,
                  a named line recorded in the repository,
                  a copied subtree of the repository,
                  a structured branch type with inherited workflow rules

Concept:          Concurrent change
Implementations:  edit in parallel and merge afterwards (merge-first),
                  lock a file before editing so only one person changes it at a time
                  (lock-first, common for unmergeable binary assets)
```

A reader who has only seen one product (say, a checksum-identified, merge-first, pointer-branch system) should still recognize the other members of the family from the core above.

## How It Works

### Start versioning a body of files

```text
Create a repository for the project (or copy an existing one, with its full history)
→ a working copy of the files appears
→ declare which files the machinery should track (or add them one by one)
```

Tracking is selective: generated files and scratch files are declared out of scope, so they never enter history.

### The recording loop

This is the rhythm all daily work follows:

```text
Edit files in the working copy
→ ask the machinery what changed (which files, and exactly which lines)
→ select the changes that belong together
→ record them as one version: attributed, described with a message
→ the repository now remembers this state, permanently
→ repeat
```

Each recorded version is a recoverable snapshot of the whole tracked file set. Recording one unit of work does not require recording unrelated in-progress edits — the working copy can hold several states at once: content already selected for recording, edits not yet selected, and files not tracked at all.

### Branch, merge, and resolve

```text
Create a branch → an independent line of development begins at the current state
→ work and record along that line without affecting the main line
→ when the line is ready, merge it back
→ the machinery combines the changes;
   where both lines changed the same content, it marks a conflict
→ a human reads both versions and resolves the conflict
→ the combined result is recorded as a version
```

Merge-capable content is the assumption behind merge-first products — which is why line-based text merges well. Files whose formats cannot be merged (artwork, sound, design files) take the other path: the file is locked while being edited, so only one person changes it at a time.

### Recall and restore

```text
Browse the history of a file or the whole project (what changed, when, by whom)
→ compare any two recorded versions, or compare the working copy against a recorded one
→ restore an earlier version into the working copy — one file, or everything
```

This is the machinery's core promise: recorded work is never silently lost, and any recorded state can be brought back.

### Share recorded work with others

In team deployments, recorded versions move between repositories: the working copy is updated with others' recorded work before recording one's own; conflicting parallel work is reconciled through the same merge-and-resolve path above. Distributed products replicate the entire repository — every copy holds the full history — so any copy can restore any other; centralized products keep the full history on the shared server, and working copies hold a checkout of one version.

### Capability tiers

```text
Defining core:
- repository remembering recorded versions
- working copy + deliberate, attributed, described recording
- history inspection, comparison, and restoration
- branching, merging, conflict resolution

Standard capabilities:
- tags for significant versions
- sharing/synchronizing recorded work between people and machines
- two-level undo (uncommitted edits; recorded revisions)
- ignore rules for generated files
- line-level history annotation ("who changed this")
- GUI clients and IDE-embedded panels

Common variants / optional:
- architecture generation (see Variants)
- lock-first vs merge-first concurrency
- structured branch types with inherited workflow rules
- large-binary and global-scale specializations
```

## Interfaces

### Command line

The historical and still-canonical surface: short verbs with arguments and flags (`init`, `clone`, `add`, `status`, `diff`, `commit`, `log`, `branch`, `merge`, `revert` — vocabulary varies slightly by product but the verb set maps one-to-one onto the core). Output is plain text: state listings, patches, history entries.

### Status view

Answers "where do I stand?" before recording: which tracked files were modified, which changes are selected for the next recording, which files are untracked, which branch is current. The single most-consulted view in daily use.

### Diff view

Side-by-side or inline comparison showing exactly which lines changed between the working copy and a recorded version, or between two recorded versions. Also the raw material for review and for resolving conflicts.

### History / log view

The recorded past as a list of versions — identifier, author, date, description — optionally filtered by file, author, or content, and rendered as a graph when branches fork and join.

### Conflict-resolution view

During a merge, the conflicting file is presented with both divergent versions marked; the user edits a combined result and marks the conflict resolved, which becomes part of the merge recording. Dedicated graphical merge tools are commonly attached here.

### GUI clients and IDE panels

The same verbs in visual form: file-state lists with checkboxes for selecting changes, one-click recording, clickable history graphs, drag-and-drop conflict resolution. Code editors embed these panels directly next to the text being edited.

### Repository server administration (variant surface)

Team deployments add server-side configuration: user access to repositories, repository creation and housekeeping, and (in enterprise products) granular per-path permissions and audit logs.

## Important Rules / Behaviors

### Nothing enters history until it is recorded

The working copy is not the record. Unrecorded edits can be discarded in one motion; only recorded versions are protected. This is why the machinery constantly surfaces the working copy's state — and why "did you commit?" is the first question after any accident.

### Recorded history is ordinarily permanent

Once recorded, a version is treated as part of the project's past, and new states are recorded on top of old ones rather than replacing them. Some products additionally offer careful tools for rewriting existing history; these are understood as exceptional and carry real risk when other people's work builds on the rewritten versions. The safe mental model: history is append-only.

### Conflicts are resolved by people

The machinery detects that two lines changed the same content and stops; it does not decide the outcome. The conflicting versions are presented together, and a human — usually after understanding why both changes exist — records the resolution. Automated tools can help compare; they cannot understand intent.

### Mergeability depends on content

The merge-first model rests on files being line-based text. For binary formats (images, 3D assets, audio), parallel editing cannot be reconciled automatically, so products either support per-file locking (one editor at a time) or expect teams to serialize work on such files. Asset-heavy projects therefore run a hybrid: merge for code, locks for art.

### Ignore rules are load-bearing

Build outputs and editor scratch files are generated constantly; without ignore rules they would flood the record. Mature projects configure them before the first recording.

### Renaming is handled inconsistently across the family

Some products record file moves as explicit first-class changes; others store no rename metadata and detect moves by recognizing similar content after the fact. Users moving between products should not assume one behavior.

## Variants

- **Architecture generation** — the family's deepest split. *Local* generation: single machine, no server (the founding generation, still shipped with many systems). *Centralized*: one shared repository server; working copies check out and submit against it. *Distributed*: every copy is a full repository with complete history; copies synchronize as peers; a shared server is a convention, not a requirement. All three are the same Type.
- **Concurrency model** — merge-first (edit in parallel, reconcile on recording) is the default in most products; lock-first (exclusive editing rights per file) is the norm for unmergeable binaries and the enterprise-scale design center for some products. One centralized product supports both in the same repository.
- **Branch model** — from zero-cost pointers to repository-tree copies to structured "stream" types that carry workflow rules (what merges where and when) with them.
- **Deployment posture** — solo local use; self-hosted repository server; vendor-hosted platform service. Hosted platforms are the adjacent Source Code Hosting Type; the machinery underneath is identical.
- **Asset-heavy and regulated deployments** — enterprises in game development, semiconductor, automotive, and media run this Type at very large scale with binary-first design (global replication servers, exclusive locking, audit traceability), while the same Type also serves a two-person open-source project on one laptop.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Source Code Hosting Platform | adjacent venue, built on top of this Type | hosting adds the networked venue: user accounts, access control over hosted repositories, and a web-first application surface for browsing and managing them. Remove the venue → the machinery runs fully alone; remove the machinery → ordinary file hosting |
| Code Review Platform | adjacent, consumes this Type's output | review is a workflow *about* recorded changes (discussion, approvals, gating); the machinery itself has no review states — vendors ship review as a separate product even when they sell both |
| Backup Management / File Sync Application | commonly confused | backup/sync is automatic and keeps the *current* state; version control records versions the user deliberately authors, with history comparison, restoration, and branch/merge machinery backup never has |
| Personal Cloud Drive | commonly confused | file storage and state propagation without a recording loop, without branches, and without conflict-resolving merge |
| Document Management / Enterprise Records Management | weaker overlap | per-document version lists inside a management system; no working-copy loop across a file set, no branching, no repository-level identity |
| Build Automation / Continuous Integration | downstream consumer | CI checks out recorded versions and builds them; the machinery neither builds nor tests |
| Package Registry / Artifact Repository | adjacent publishing spine | versions *published artifacts* for consumption; no working-copy editing or merge of source |
| Code Editor / IDE | embedding host | editors embed version-control panels; the embedding is an interface convenience, not a different or merged Type |

The hosting seam is the most important one: the two Types share the vocabulary (repository, commit, branch) because hosting platforms embed this machinery, and the fastest test is the venue test — accounts, access management, and an application surface are hosting; recording, history, and merge machinery are this Type.

## Representative Products

- **Git** — the dominant distributed system; content-checksum-identified history, lightweight pointer branches, two-step staging model.
- **Mercurial** — distributed system with a deliberately simple command model and an extension architecture.
- **Apache Subversion** — centralized open-source system; repository-wide revision numbering, copy-based branches, merge-first with optional locking.
- **Perforce P4 (Helix Core)** — centralized enterprise system built for very large repositories and binary assets (game development, semiconductor, automotive); lock-first concurrency, structured branch "streams", global replication.

These four span the architecture generations, both concurrency models, and both open-source and enterprise customer layers; the defining core above was checked against all four, and the historical generations (local-only systems) against the core's solo/local shape.

## Sources

Research date: **2026-09-09**

- Git — Pro Git (2nd Edition), official book at git-scm.com: "About Version Control"; "Recording Changes to the Repository" — https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control , https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
- Apache Subversion — *Version Control with Subversion* (official book): "Fundamental Concepts", "Version Control Basics" — https://svnbook.red-bean.com/en/1.7/svn.basic.html , https://svnbook.red-bean.com/en/1.7/svn.basic.version-control-basics.html
- Mercurial — official Guide ("Learning Mercurial in Workflows") — https://www.mercurial-scm.org/guide
- Perforce — P4 (Helix Core) product page — https://www.perforce.com/products/helix-core

> Sourcing limitation: Perforce's operational user manual was not reachable from the research environment on 2026-09-09 (the documentation URL returned an error and was not retried). Perforce-related claims are therefore held to what its official product page directly states (central server with edge/proxy replication, exclusive file locking, streams, changelists, restore of previous versions, separate code-review product) and are not stated at operational depth. The defining-core analysis does not depend on any Perforce operational detail.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
