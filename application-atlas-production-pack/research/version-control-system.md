# Research Notes — Version Control System

Research date: 2026-09-09
Methodology: v1.1

## Research Goal

Understand what a Version Control System (VCS) actually is as an Application Type — its defining core, its user-facing machinery, and its boundary against the neighbors it is most often confused with (source-code hosting platforms, code review tools, backup/file-sync, document version history) — from official operational documentation of representative products across both major architectures (centralized and distributed).

## Initial Boundary (pre-research hypothesis)

- Core use: record successive versions of a set of files (usually source code) so that any recorded version can later be recalled, compared, and restored; enable parallel lines of development and reconciliation of concurrent changes.
- Users: software developers primarily; also designers/artists versioning binary assets.
- Nearest Types: Source Code Hosting Platform (sibling §12 leaf — a boundary FLAG from that pass awaits ratification here), Code Review Platform, Backup Management / File Sync / Personal Cloud Drive, Document Management (version history), Build Automation / CI, Package Registry, IDE-embedded VCS clients.
- Likely boundary: VCS = the versioning machinery itself (no accounts/venue/web application surface); hosting = the networked venue built around a VCS. Unknowns to resolve: is distributed architecture definitional? is multi-user sharing definitional? is branching/merging definitional? is the staging area definitional (Git habit)? is "source code" definitional?

## Research Questions

1. What is the irreducible object set (repository, revision, working copy, branch, diff, merge)?
2. What is the user's core loop (edit → record → inspect → restore)?
3. Is the distributed-vs-centralized architecture part of the definition or a variant?
4. How is concurrent change handled, and are lock-based and merge-based models both within the Type?
5. Is versioning of non-source files in scope?
6. Which features are common-but-not-definitional (tags, ignore rules, blame, staging, hooks, rename tracking)?
7. Where exactly is the seam vs Source Code Hosting Platform (ratify the sibling flag), vs backup/file-sync, vs document version history, vs code review?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophy, and different customer layers:

| Product | Philosophy | Customer layer | Docs used |
|---|---|---|---|
| Git | distributed; lightweight branching; content-addressed history | individual/OSS → enterprise (via hosting) | Pro Git 2nd ed. (official, git-scm.com) |
| Mercurial | distributed; simpler command model; extension-based | individual/OSS | official guide (mercurial-scm.org) |
| Apache Subversion (SVN) | centralized; copy-modify-merge with optional locking; copy-based branching | OSS → legacy enterprise | Version Control with Subversion (official book, svnbook.red-bean.com) |
| Perforce P4 (Helix Core) | centralized; locking-first; binary/asset-heavy enterprise scale | large enterprise (game dev, semiconductor, automotive, media) | product page (perforce.com); operational manual NOT reachable |

## Sources

Evidence layers: A = directly observed on official source for a specific product; B = cross-product commonality; C = canonical inference.

- Git — Pro Git 2nd ed., "About Version Control" — https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control — fetched 2026-09-09 (A)
- Git — Pro Git 2nd ed., "Recording Changes to the Repository" — https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository — fetched 2026-09-09 (A)
- Subversion — Version Control with Subversion (1.7), "Fundamental Concepts" TOC + "Version Control Basics" — https://svnbook.red-bean.com/en/1.7/svn.basic.html and https://svnbook.red-bean.com/en/1.7/svn.basic.version-control-basics.html — fetched 2026-09-09 (A)
- Mercurial — official Guide ("Learning Mercurial in Workflows") — https://www.mercurial-scm.org/guide — fetched 2026-09-09 (A)
- Perforce — P4 (Helix Core) product page — https://www.perforce.com/products/helix-core — fetched 2026-09-09 (A for positioning/architecture-level claims; Tier 2 only)
- Perforce — Helix Core user manual — https://www.perforce.com/manuals/helix-core-user/Content/helix-core-user/home.html — **404, not reachable** (1 attempt; abandoned per network rule)

Source-access limitation: Perforce operational documentation (workspaces, changelist mechanics, streams internals) could not be fetched; all Perforce claims in these notes are limited to what its product page directly states (file locking, streams as branching model, changelists, central server with proxy/edge replication, P4V/P4 Merge clients, separate P4 Code Review product). No precise Perforce operational details were filled in from memory.

## Product Observations

### Git (Pro Git, official book) — evidence A

- Definition given by the book: "Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later." Source code is the book's example, but "in reality you can do this with nearly any type of file on a computer"; a graphic/web designer keeping versions of images/layouts is given as a legitimate use.
- The book's own taxonomy of the lineage: local VCS (RCS — "keeps patch sets… can re-create what any file looked like at any point in time") → centralized VCS (CVS, Subversion, Perforce — "a single server that contains all the versioned files, and a number of clients that check out files from that central place") → distributed VCS (Git, Mercurial, Darcs — clients "fully mirror the repository, including its full history"; "Every clone is really a full backup").
- Value claims for a VCS: "revert selected files back to a previous state, revert the entire project back to a previous state, compare changes over time, see who last modified something that might be causing a problem, who introduced an issue and when… if you screw things up or lose files, you can easily recover."
- Working copy: repository on local machine plus a "checkout or working copy of all of its files".
- Recording loop: edit files → selectively stage → `git commit` records a snapshot; "Every time you perform a commit, you're recording a snapshot of your project that you can revert to or compare to later." Commit output includes branch, SHA-1 checksum, files changed, line statistics. Commit message entered via editor or `-m`.
- File states: tracked vs untracked; tracked files unmodified/modified/staged. `git status` shows branch and state. `git diff` shows exact lines added/removed (unstaged); `git diff --staged` shows what will be committed.
- Staging area (index): Git-specific two-step model ("add precisely this content to the next commit"); can be skipped with `commit -a` for tracked files. — This is an implementation choice, not shared by the other sampled systems.
- Ignore rules: `.gitignore` pattern files to keep generated files (build outputs, editor temp files) out of history; nested ignore files possible.
- Removal: `git rm` stages deletion; safety feature prevents removing data not yet recorded in a snapshot.
- Rename: "Unlike many other VCSs, Git doesn't explicitly track file movement" — rename detected implicitly after the fact; `git mv` is a convenience.
- Default branch: Git itself defaults to `master`; the note records that hosting providers changed default to `main` and the name is configurable — i.e., default branch naming is not part of the machinery.
- Book structure confirms the canonical chapter set: getting a repository (init/clone), recording changes, viewing commit history, undoing things, working with remotes, tagging, branching and merging, remote branches, rebasing, rewriting history, hooks, configuration.

### Apache Subversion (Version Control with Subversion, official book) — evidence A

- Definition: "A version control system (or revision control system) is a system that tracks incremental versions (or revisions) of files and, in some cases, directories over time." Usefulness: "allows you to explore the changes which resulted in each of those versions and facilitates the arbitrary recall of the same."
- Scope: "Subversion can manage any sort of file collection—it's not limited to helping computer programmers."
- Repository: "the central store of that system's data… usually stores information in the form of a filesystem tree"; clients read/write; "as the files in the repository are changed, the repository remembers each version"; a client "can request previous states of the filesystem" and ask historical questions ("What did this directory contain last Wednesday?", "Who was the last person to change this file, and what changes did he make?"). The book explicitly contrasts: the repository "is a kind of file server", and what makes it special is remembering each version.
- Working copy: "a local copy of a particular version of a user's VCS-managed data upon which that user is free to work"; appears to other software as an ordinary directory; the VCS client manages communication between working copy and repository.
- Versioning models (concurrency): the fundamental problem — "allow users to share information, but prevent them from accidentally stepping on each other's feet".
  - lock-modify-unlock: only one person may change a file at a time; the book catalogs its costs (admin problems, serialization, false security).
  - copy-modify-merge: users work simultaneously in private working copies; changes merged; the system "often assists with the merging, but ultimately, a human being is responsible"; overlapping changes produce a *conflict* state where the user "can see both sets of conflicting changes and manually choose"; "software can't automatically resolve conflicts."
  - Both models coexist in Subversion: it "is primarily a copy-modify-merge system" but "still recognizes the need to lock an occasional file" (binary formats where merging is impossible).
- Mergeability assumption: copy-modify-merge "is based on the assumption that files are contextually mergeable—that is, that the majority of the files in the repository are line-based text files"; for binary files (artwork, sound) "it really is necessary for users to take strict turns."
- Book structure confirms: The Repository, The Working Copy, Versioning Models, Revisions, Addressing the Repository, working-copy interactions, mixed-revision working copies.
- Note: the book deliberately limits discussion to "modern version control systems" that "can operate across wide-area networks" — networked sharing is framed as the modern baseline, not (per the Git book's taxonomy) the only VCS category.

### Mercurial (official guide, mercurial-scm.org) — evidence A

- Positioning: "With Mercurial you can use a multitude of different workflows… intended to make it easy for beginners of version tracking to get going instantly." Guide's first workflow: "log keeping — you want to use Mercurial to be able to look back when you did which changes."
- Setup: user configures identity in `~/.hgrc` (`[ui] username = …`).
- Loop: `hg init project` → create files → `hg add` (track) → `hg commit` (message editor opens; "Leave message empty to abort commit"; commit template shows user, branch, added files) → `hg log` shows changesets (identifier hash, user, date, summary).
- Tracking is selective: "you can add only specific files… Mercurial will then track only these files and won't know about the others."
- A note in the guide says Subversion users "will likely feel at home quite quickly" — cross-VCS conceptual continuity acknowledged by the vendor itself.
- Deeper concept references: official Tutorial, "Mercurial: The Definitive Guide" (book.mercurial-scm.org, including "behind the scenes" design chapter), "UnderstandingMercurial" concepts page.

### Perforce P4 / Helix Core (product page only — Tier 2) — evidence A for positioning claims, degraded depth

- Positioning: "Version Control That Handles What Others Can't… tracks everything—from source code to 3D assets"; "scalable source control foundation and single source of truth"; industries: game development, animation/VFX, semiconductor, automotive.
- Concurrency: "built-in file locking that prevents overwrite disasters"; "Prevent merge conflicts with Exclusive File Locking" — locking-first posture (the mirror image of Git/Mercurial's merge-first default).
- Architecture: central server, optionally "proxy and edge servers" for global teams; "intelligent Delta Transfers" for sync/submit performance.
- Versioning idioms on the page: "makes it easy to restore your previous versions"; sync and submit as the sync verbs; audit logs and "full traceability".
- Branching: "Go beyond basic branching and structure your workflows for scale with Streams" — streams as Perforce's branch/workflow model.
- Permissions: "granular permissions controls" server-side (let users "only see the files they need").
- Clients: P4 Visual Client (P4V), P4 Merge (merge/diff tool), CLI; IDE integrations (Visual Studio plugin, Unity, Unreal).
- Boundary evidence: **P4 Code Review is a separate product** (web-based code review tool with pre-commit/post-commit models); P4 DAM (asset management) and P4 Plan (agile planning) are also separate; P4 Git Connector bridges to Git/GitHub/GitLab/Bitbucket. The vendor itself draws the VCS / review / DAM / planning seams.
- Free tier framing: "up to 5 users and 20 workspaces" — "users" and "workspaces" as the unit structure (workspace = Perforce's working-copy construct).

## Cross-product Comparison

| Structure | Git | Mercurial | Subversion | Perforce P4 | Strength |
|---|---|---|---|---|---|
| Repository as versioned store that "remembers each version" | ✓ (local repo, full history) | ✓ | ✓ (central store; filesystem tree) | ✓ (central server; "single source of truth") | B (4/4) |
| Working copy (editable checkout) | ✓ | ✓ | ✓ (named concept) | ✓ ("workspaces") | B (4/4) |
| User-invoked recording of a version with author + description | ✓ commit (SHA-1, message) | ✓ commit (changeset; username, message) | ✓ commit | ✓ submit (changelists) | B (4/4) |
| History navigation: view log, compare versions (diff), see who changed what | ✓ log/diff | ✓ log | ✓ (historical questions: what/who/when) | ✓ (audit logs, traceability) | B (4/4) |
| Retrieve / restore any recorded version | ✓ (revert/restore/checkout) | ✓ | ✓ ("arbitrary recall") | ✓ ("restore your previous versions") | B (4/4) |
| Branching (parallel lines of development) | ✓ (lightweight) | ✓ (named branches) | ✓ (copy-based per book structure) | ✓ (streams) | B (4/4) |
| Merging with conflict handling | ✓ | ✓ | ✓ (conflict state; human resolves) | ✓ (P4 Merge tool; locking prevents conflicts instead) | B (4/4) |
| Concurrency model | merge-first | merge-first | merge-first + optional locking | locking-first | L2 variant |
| Architecture | distributed (full mirror per clone) | distributed | centralized client/server | centralized (+proxy/edge) | L2 variant |
| Non-source files in scope | "nearly any type of file" | any files | "any sort of file collection" | source code → 3D assets (binaries first-class) | B (4/4) |
| Two-step staging before commit | ✓ (index; skip via -a) | ✗ | ✗ | ✗ (server-side changelists) | L3 (Git-specific) |
| Revision identity | SHA-1 checksum | changeset hash + local rev number | repository revision number | changelist number | L2/L3 variant |
| Rename tracking | implicit (similarity detection; book says "unlike many other VCSs") | explicit (not fetched in detail) | explicit (book structure) | explicit (not verified at operational depth) | L2 variant |
| Identity model | local config (user.name/email) | local config (hgrc username) | server-side (not fetched at depth) | server-side users/workspaces | L2 variant |
| Selective tracking of new files | ✓ (git add; untracked state) | ✓ (hg add of specific files) | ✓ (not fetched at depth) | — (not verified) | B (3/4 verified) |

Reading: every candidate defining structure is present in all four sampled products; every architecture- or implementation-level property varies. This cleanly separates L0 from L1/L2/L3.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Version Control System is the versioning machinery for a body of files. Four jointly-held structures; remove any one and the product stops being a VCS:

1. **The repository as the versioned store of record** — a persistent store holding successive recorded versions (revisions) of a set of tracked files; the store, not any one machine, is the memory of the project. Remove → plain file storage / a backup bucket.
2. **The working-copy recording loop** — the user works on files in a working copy (checkout) and deliberately records the current state as a revision (commit/check-in/submit), each recording attributed (author) and described (message); history accumulates only from these deliberate acts. Remove → automatic backup or file-sync (systemic, not user-authored versions).
3. **Version history navigation** — the user can inspect the recorded history (what changed, when, by whom), compare any recorded versions against each other (diff), and retrieve/restore any recorded version into the working copy. Remove → an append-only audit journal (no recall) or a snapshot store (no comparison).
4. **Parallel lines of development, reconcilable** — development can fork into independent branches and the lines' changes can be brought back together (merge), with conflict handling when the same content has diverged on the two lines. Remove → versioned document/backup history (e.g., per-file version lists), not development tooling.

Jointly-held load-bearing tests:

- 1 alone = a file server that archives (SVN book's own contrast: "a kind of file server" — the remembering is what makes it more).
- 2 without 3 = blind recording; useless as memory.
- 3 without 2 = a log with no user-authored record points.
- 4 without 1+2+3 = divergent directory copies.
- 1+2+3 without 4 = versioned backup / document-version-history territory (the boundary vs backup and document management).

Anti-overfitting on L0 (verified against sample):

- **Architecture is NOT definitional** — distributed (Git/Mercurial), centralized (SVN/P4), and the local single-machine generation (RCS, cited in Pro Git as a local VCS) all satisfy the core. Pro Git's own taxonomy treats local/centralized/distributed as three generations of the same Type.
- **Content-addressed hashing / SHA-named commits NOT definitional** — SVN uses repository revision numbers, P4 uses changelist numbers, Mercurial exposes local rev numbers beside hashes.
- **Staging area NOT definitional** — the index is Git's implementation (skippable even in Git via `-a`); SVN commits paths directly; Mercurial commits selected files; P4 stages server-side via changelists.
- **Atomic multi-file commits NOT definitional as a modern-only property** — the local-VCS generation recorded per-file (RCS patch sets); atomicity is a maturity achievement, not the invariant. (Kept at "common in modern systems" strength.)
- **Merge-first concurrency NOT definitional** — P4 is locking-first by design; SVN supports both models in one product (book-documented).
- **Multi-user sharing NOT definitional** — a solo developer's local Git/Mercurial repo is fully a VCS; multi-user synchronization is the universal deployment shape but not the machinery's definition. (The SVN book frames networked collaboration as the modern baseline — recorded, but the Git book's local-VCS category and Mercurial's solo "log keeping" workflow are counterweights.)
- **Source-code specificity NOT definitional** — all four sampled sources state or demonstrate general files; P4 is built around 3D assets; Pro Git names graphic/web designers.
- **Rename/move tracking style NOT definitional** — Git detects implicitly, SVN copies track explicitly, and the Git book explicitly says Git differs from "many other VCSs" here.
- **Default branch names, exact diff formats, exact identity config** — not definitional; vary per product and even per hosting deployment (Git book notes master→main is a hosting-level change).

### L1 — Common Mature Structure (very common, not definitional)

- Tagging: named markers on recorded versions for release/reference points (Git book dedicates a chapter; family-wide).
- Multi-user synchronization: updating the working copy from others' recorded work and publishing one's own (update/push/pull/fetch/submit; remotes in DVCS).
- Two-level undo: discard uncommitted working-copy changes; revert/roll back recorded revisions (Git "Undoing Things" chapter; family-wide idiom).
- Ignore rules: per-project exclusion patterns keeping generated files out of history (Git `.gitignore` directly evidenced; Mercurial/SVN carry equivalent mechanisms — common strength).
- History annotation: line/file-level "who last modified / who introduced this" queries (Git book names it among the core reasons VCS exists).
- Safety rails around destructive actions (Git's rm safety; empty-message aborts commit in Mercurial).
- GUI clients and IDE embedding as alternative surfaces (Git GUIs; P4V; IDE plugins).

### L2 — Variant / Optional Structure

- Architecture generation: local-only → centralized client/server → distributed full-clone.
- Concurrency model: copy-modify-merge (Git, Mercurial, SVN default) vs lock-modify-unlock (P4 default exclusive locking; SVN optional locking for unmergeable binaries).
- Branch implementation: lightweight mutable pointers (Git), named branches/bookmarks (Mercurial), repository-tree copies (SVN), streams with workflow structure (P4).
- Binary/large-asset strategy: merge-first systems bolt on locking + separate large-file handling; P4 makes binaries first-class.
- Identity substrate: locally configured user strings (Git/Mercurial) vs server-managed users/workspaces (P4; SVN server).
- Deployment posture: no server (solo), self-hosted repository server (bare repo, svnserve, P4 server), hosted platform (→ Source Code Hosting Platform territory), managed cloud (P4 Cloud).
- Scale specializations: global replication (P4 proxy/edge), delta transfer performance, asset-focused integrations (Unity/Unreal).

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Git: the index/staging area and its two-state model; SHA-1 (now optionally SHA-256) object checksums; reflog; interactive staging; stash; submodules; rerere; aliases; the `.git` directory layout; plumbing/porcelain command split.
- Mercurial: changesets with integer local rev + hash; revsets query language; extension system (mq, largefiles, evolve); phases.
- Subversion: repository-wide sequential revision numbering; properties (svn:mergeinfo mechanism per book structure); externals; mixed-revision working copies;Apache project governance.
- Perforce: changelists (numbered, server-side); workspaces with depot mapping; streams; Helix platform suite branding (P4 Code Review, P4 DAM, P4 Plan, P4 Git Connector, Helix IPLM); ISO 26262 certification claim; free-tier sizing (5 users / 20 workspaces).

## Rejected Findings (proposed-then-rejected definitional claims)

- "A VCS is distributed" — rejected: SVN and P4 are centralized members; Pro Git itself frames DVCS as one of three generations.
- "A VCS stores snapshots" — rejected as definitional: RCS stores patch deltas; SVN stores incremental revisions; the invariant is recorded *recoverable versions*, not the storage technique.
- "A VCS requires a central server" — rejected: local/distributed generations satisfy the core without one.
- "A VCS requires multi-user accounts and permissions" — rejected: solo local use is fully functional; accounts exist in server deployments but serve repository access, not an application venue (refinement of the hosting seam).
- "Staging is part of committing" — rejected: Git-only implementation (skippable in Git itself).
- "A VCS is for source code" — rejected by all four products' own scope statements.
- "Locking is legacy/wrong" — rejected as definitional stance: P4 is locking-first and prominent; SVN book treats locking as sometimes necessary (binaries).
- "Branches must be cheap/lightweight" — rejected: copy-based (SVN) and stream-structured (P4) branches are first-class members.

## Historical / Market-Sample Check (§24)

- Earliest documented generation: local VCS — Pro Git cites RCS keeping patch sets and re-creating any file state at any point in time: repository + deliberate record + recall/compare all present, with no network, no accounts, no hosting. Fits L0 items 1–3 (and the branch/merge leg exists across the documented lineage: CVS, Subversion, Perforce, Git, Mercurial all directly evidenced; RCS-era branch/merge machinery was not re-verified in this pass and is not load-bearing for the check, because the earliest generation already satisfies the Type via items 1–3 as a single-line VCS).
- Regional/regionalized and platform-native analogs: document-editor "version history" and OS file-history features deliberately do NOT fit L0 (no working-copy recording loop, no branch/merge machinery, no arbitrary-version diff as the working idiom) — the negative case that confirms the boundary.
- Creative-industry deployments (P4 with 3D assets, artists in workspaces) fit without modification — "source code" is already excluded from the core.
- Conclusion: the definition is not over-fitted to the modern distributed-branch-workflow era.

## Boundary Findings

| Neighbor Type | Seam | Remove-test |
|---|---|---|
| **Source Code Hosting Platform** (sibling flag ratified) | VCS = the versioning machinery (repository, commit loop, history, branch/merge). Hosting platform = the centralized networked *venue* built around a VCS: accounts + access control as managed platform properties, networked multi-user read/write of hosted repositories, and a web-first application surface (browse/manage/admin). Hosting embeds a VCS as substrate; a VCS does not imply hosting. Refinement ratified from this side: "runs locally with no accounts" holds strictly for the local/distributed generations; centralized members (SVN, P4) run a repository server with repository-level authentication — but that auth serves repository sync, not an account/venue/platform layer, and there is no application surface (web UI, profiles, venue). Perforce ships its code review as a separate product; Git's GitWeb appears in Pro Git as a minimal add-on viewer, not part of the machinery. | Remove the venue → the VCS remains fully functional (git init/hg init/svnserve/P4 server). Remove the VCS → file hosting / cloud-drive territory, not this Type. |
| Code Review Platform | Review is a workflow *about* recorded changes, not the recording machinery. Commit messages and diffs are inputs to review; no review states, approvals, or discussion objects exist in the bare VCS. Perforce separating P4 Code Review from P4 is vendor-drawn confirmation. | Remove review workflow → VCS intact. Remove VCS → review platform with nothing to review. |
| Backup Management / File Sync / Personal Cloud Drive | Backup/sync is automatic and systemic; VCS recording is deliberate and user-authored. No branches, no merge with conflict handling, no working-copy discipline; sync propagates current state. SVN book: "merely tracking the various versions… isn't very interesting in itself" — the explore-and-recall idiom is what distinguishes. | Remove deliberate recording + branch/merge + diff-and-recall idiom → backup/sync tool. |
| Document Management / document-editor version history | Per-document, tool-managed version lists inside a management system or editor; no repository-level identity, no working-copy loop across a file set, no branch/merge. | Same as backup: loses L0 items 2 and 4 → document version history, not a VCS. |
| Build Automation / CI | CI *consumes* VCS state (checks out recorded revisions) and produces builds; the VCS neither builds nor tests. | Adjacent downstream; no overlap in core structure. |
| Package Registry / Artifact Repository | Versions *published artifacts* for consumption by version number; no working-copy editing loop, no branch/merge of source. | Publishing/consumption spine vs development-recording spine. |
| Code Editor / IDE | IDEs embed VCS clients (panels for status/diff/stage/commit) — an interface embedding, not a separate or merged Type. | The embedded client exercises the same L0 machinery; remove it and both remain. |

**"去掉什么就变成另一个 Type" 判据**: remove the venue/application surface → still a VCS (this is what separates VCS from hosting). Remove the deliberate recording loop or the branch/merge machinery → backup/sync/document-version-history territory (no longer a VCS). Remove the versioned store itself → an editor with an undo stack (no longer any version management).

## Uncertainties

- Perforce operational depth (workspace mapping, changelist lifecycle, stream merge semantics) unverified — manual unreachable; all P4 claims limited to product-page strength. The final document avoids precise P4 operational claims.
- Mercurial observed only through its getting-started guide; deeper mechanics (phases, revsets) appear in references not fetched. Low risk: observed portions align with the family core.
- SVN's modern feature surface (1.14-era) beyond the 1.7-book fundamentals (e.g., current move/rename semantics, svn:mergeinfo details) not fetched. Book evidence is official and sufficient for L0/L1 claims.
- RCS-era branch/merge specifics not re-verified in this pass; the historical check was deliberately written to not depend on them.
- Whether some niche product could satisfy L0 items 1–3 while genuinely lacking item 4 (branch/merge) — none found in sample or lineage; if one exists, it would sit at the backup-history boundary. (Recorded as a boundary-shape question, not a blocker.)

## Final Synthesis

The VCS Type is best modeled as **the versioning machinery for a body of files**: a repository that remembers successive user-recorded versions of tracked files, a working copy in which the user edits and from which deliberate recordings (commits/check-ins) are made, history that can be inspected (what/who/when), compared (diff), and recalled (restore), and branching that lets development fork into parallel lines reconciled by merging with human conflict resolution. Distributed vs centralized, merge-first vs lock-first, hash-named vs numbered revisions, staged vs direct commits, lightweight vs copy-based branches — all are implementation generations and variants, not the definition. The shared venue where teams browse, discuss, and gate these versions is a different Type (Source Code Hosting Platform); the review workflow about recorded changes is another (Code Review Platform); automatic systemic version keeping without the deliberate record-and-reconcile machinery is yet another (backup/file-sync/document version history). Flag from the source-code-hosting-platform pass **RATIFIED** with the refinement above.
