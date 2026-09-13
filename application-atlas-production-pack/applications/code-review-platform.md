# Code Review Platform

## Overview

A **Code Review Platform** is the system of record for the human review of proposed code changes. It holds each proposed change as a reviewable diff against a base revision, anchors discussion to the changed lines, and records explicit reviewer verdicts that determine whether — and how — the change progresses into the codebase.

Its purpose is to turn "someone other than the author looks at every change before it lands" into a structured, traceable workflow: every judgment is attached to the exact lines it concerns, every verdict is attributable to a named reviewer, and the full history of a change — what was proposed, what was said, who approved it, and what finally shipped — survives in one place.

The defining boundary: the **review workflow over proposed changes** is what the product is organized around. A code review platform may host repositories itself or attach to external ones; it may execute the merge or leave the push to the author; it may enforce verdicts or merely record them. When the primary object is automated analysis of code health rather than human review of changes, the product belongs to a different Type (code quality / static analysis). When the primary object is repository storage and browsing, it is a source-hosting platform that may embed review as a capability.

## Users & Context

Primary users:

- **Author (developer)** — proposes changes: pushes or uploads a diff, writes the change description, responds to review feedback, publishes revised versions, and ultimately lands the change (or abandons it).
- **Reviewer (peer or senior developer)** — reads the diff file by file, comments on specific lines, discusses trade-offs, and records a verdict: approve, request changes, or a graded judgment.
- **Required approver / code owner** — a reviewer whose verdict policy demands before the change may progress (maintainers, owners of the affected paths, security or database specialists).

Automated participants act on the change but do not replace the human verdict: CI pipelines report build and test status, analyzers and bots post findings as comments or checks, and increasingly AI reviewers draft comments or even push follow-up commits.

Administrators configure the rules that shape the workflow: who may approve, whose approval is required, which branches are protected, and how ownership maps to files.

Context: software teams of every size; open-source communities reviewing external contributions; enterprises with mandatory review gates for compliance. The platform sits between the developer's local work and the shared codebase — it is where private work becomes team-visible.

## Core Model

### The defining core

```text
Proposed Change  (a diff against a base revision, held as a versioned object)
└── Review Conversation  (comments anchored to diff lines + change-level discussion)
    └── Review Verdict  (recorded, attributable reviewer outcome)
        └── Progression  (incorporation into the target branch — or abandonment)
```

Four structures. If any one is removed, the product stops being a code review platform:

- **Proposed change** — the unit of review. A change to a version-controlled codebase, expressed as a diff of one or more file modifications against a base revision. It is a first-class object: it has an identity, a title and description, an author, a target branch, and a version history — successive revisions of the same change are linked so reviewers can see what was reworked. Realizations differ (a branch-based pull/merge request, a patch-set change, an uploaded diff), but the object itself is invariant.
- **Diff as the review surface** — the change is read as a line-level diff, not as whole files. Comments attach to specific lines or line ranges of that diff; change-level discussion (description, summary comments) surrounds them. The diff is what makes review precise: feedback lands exactly where the code changed.
- **Review conversation** — the discussion attached to the change: inline threads on lines, replies, resolution states (a thread or comment can be resolved, fixed, dropped, or re-opened), and reviewer-proposed replacement edits ("suggestions") the author can apply with one click. The conversation persists across revisions of the change.
- **Recorded verdict** — the explicit outcome a reviewer records: approve, request changes, a graded vote, or an approval marker. Verdicts are attributable (named reviewer, timestamped) and visible to the team. The workflow treats the verdict state as the gate for progression: a change with the required approvals may proceed; one with blocking feedback may not.

**Progression** — incorporation of the change into the target branch — is the intended outcome, but its execution varies by product (see How It Works): many platforms merge the change themselves; some leave the push to the author. The verdict, not the merge, is the defining gate.

### Standard capabilities

Mature products commonly add, around that core:

- **Change lifecycle states** — open/draft → under review → merged/submitted, or closed/abandoned/dropped; drafts let authors share work in progress without formally requesting review.
- **Reviewer routing** — manual review requests plus automatic rules: path-ownership files that auto-request owners of changed files, review groups, default-reviewer rules, and approval rules that specify how many approvals of which kind are needed.
- **Diff-viewing tooling** — unified or side-by-side layout, file tree and filtering, per-file "viewed" tracking with progress, whitespace control, and comparison between successive versions of the change (interdiffs / patch-set diffs).
- **Threaded, resolvable discussion** — comment threads with resolve/re-open states; unresolved threads can optionally block progression.
- **Suggestion mechanics** — reviewers propose concrete replacement lines; the author applies them as a commit.
- **Change metadata and links** — linked issues, milestones, projects, labels; closing an issue automatically when its change merges.
- **Automated checks on the change** — CI pipeline status, test results, analyzer findings, coverage and mergeability reports, surfaced as tabs, widgets, or status lines next to the diff.
- **Merge execution with strategies** — merge commit, squash, or fast-forward; auto-merge when checks pass; source-branch cleanup.
- **Notification and triage** — email and in-app notifications, to-do lists, dashboards of changes awaiting the user's action, search and filters over change lists.
- **Access control and extensibility** — permissions inherited from repository roles, protected branches, APIs and webhooks for automation.

### One structure, many implementations

```text
Concept:            Proposed change
Implementations:    branch-based pull/merge request · patch-set change · uploaded diff

Concept:            Review verdict
Implementations:    binary approve/request-changes · graded label votes · approval marker + per-comment issues

Concept:            Progression
Implementations:    platform-executed merge (with strategies) · author-executed push after approval

Concept:            Enforcement
Implementations:    advisory (recorded only) · optional · required (branch protection, label gates, approval rules)
```

A reader who has only seen branch-based pull requests should still be able to recognize patch-set review tools and advisory review layers from this model — and vice versa.

## How It Works

### Propose

```text
develop locally
→ create the change (push to a review ref / open a pull or merge request / post a diff)
→ write the description (what and why; link issues)
→ reviewers are assigned or auto-requested (owners, groups, rules)
```

The change now exists as a reviewable object. Many products support a draft state: share early, request review later.

### Review loop

```text
reviewer opens the change
→ reads the diff file by file (marks files viewed, tracks progress)
→ comments on lines or ranges; proposes suggestions; raises change-level points
→ marks blocking comments as issues / unresolved threads
→ submits a verdict: approve · request changes · comment / graded vote
```

The author responds:

```text
read feedback
→ apply suggestions or rework the code
→ publish a new revision of the same change (new commits / new patch set / new diff)
→ discussion continues on the updated diff; resolved points stay resolved
```

This propose→review→rework loop is the heart of the product. It may cycle several times; the change's version history and conversation accumulate the full record.

### Verdict and progression

When the required verdicts are in place, the change progresses:

- **Platform-executed**: the author or a maintainer merges the change into the target branch — choosing a merge strategy (merge commit, squash, fast-forward) or setting auto-merge so it lands when checks pass. The platform may clean up the source branch and retarget dependent changes.
- **Author-executed**: in review-first tools without merge machinery, approval is the signal for the author to push the change to the upstream repository themselves, then mark the review completed.

Either way, the change ends merged (or submitted) and archived with its full review history — or closed/abandoned with the record intact.

### Two workflow postures

- **Pre-merge / pre-commit review** (dominant modern posture): the change is reviewed *before* it lands; approval gates incorporation.
- **Post-commit review**: the change lands first and is reviewed after; findings become follow-up commits. Older and some current workflows use this deliberately; the review platform supports both — the difference is only whether the verdict precedes or follows the push.

### Enforcement wiring

Whether verdicts actually block anything is configuration, not essence:

- **Advisory** — verdicts are recorded and visible but nothing mechanically prevents progression.
- **Optional** — approvals are invited; merging without them is possible.
- **Required** — branch protection, label gates, or approval rules make specified verdicts a hard precondition (including "approval from the owner of the changed files").

The same product can span this gradient across projects; teams choose per branch or per repository.

## Interfaces

### Change list / dashboard

The triage surface: changes awaiting the user's review, changes the user authored, changes on their teams.

- typical information: title, author, target branch, status, review/verdict state, checks status, last activity
- primary actions: open a change, filter/search, create a change

### Change page

The workhorse surface, usually organized as tabs or sections:

- **Overview / conversation** — description, timeline, comments, reviews, verdict states
- **Commits / versions** — the revision history of the change; comparison between versions
- **Checks** — CI status, test results, analyzer findings, mergeability
- **Files changed** — the diff itself (see below)
- **Merge / submit box** — current blockers, missing approvals, merge strategy, the merge/submit action

### Diff viewer

Where review actually happens.

- typical information: changed files with line-level additions/removals, viewed-markers, per-file comment counts
- primary actions: comment on a line or range, propose a suggestion, mark file viewed, toggle unified/side-by-side, hide whitespace, navigate between files and versions

### Review composer

Where a reviewer assembles and submits their verdict: pending inline comments (visible only to the reviewer until submitted), a summary comment, and the verdict choice (approve / request changes / comment, or a graded vote).

### Administration / settings

Project- and branch-level configuration: approval rules, protected branches, ownership files, merge permissions, thread-blocking, templates.

## Important Rules / Behaviors

- **Verdicts are attributable and durable.** Every approval, rejection, or vote is recorded against a named reviewer with a timestamp; the change page is the audit trail of who judged what and when.
- **Authors do not approve their own changes.** Commonly prevented outright (as a default in some products, a setting in others) — the review exists precisely to bring a second judgment.
- **New revisions can invalidate old approvals.** Some products dismiss existing approvals when new commits arrive, forcing re-review of the changed code; others leave approvals standing. Teams that need the strict behavior enable it explicitly.
- **Unresolved discussion may block.** Whether open threads or unfixed review issues prevent progression is configurable — from purely informational to hard-blocking.
- **Enforcement is wiring, not essence.** The same verdict system can be advisory on one branch and mandatory on another; the recorded verdict is the invariant, its blocking power is configuration.
- **The change is versioned; the conversation survives updates.** Reviewers can diff successive versions; comments stay anchored to their lines (with explicit handling — auto-resolve or carry-over — when lines move).
- **Automated checks inform but do not replace the human verdict.** CI status, analyzer findings, and AI-generated review comments appear on the change; where documented, machine approvals explicitly do not count as the required human approval. Verification-style checks (build/tests) are often separated from code-review judgment with distinct permissions.
- **Review scope can exceed code.** Some platforms extend the same review machinery to images, documents, and other artifacts; the diff-anchored review of code changes remains the core.

## Variants

- **Standalone review-first vs hosting-embedded.** Standalone products organize everything around review and attach to external repositories (one well-known tool also serves as the central repository; another performs no hosting and no merge at all). Hosting-embedded products deliver review as the collaboration core of a source-hosting platform — the dominant modern delivery.
- **Change-centric vs branch-centric.** Patch/change-centric tools review a sequence of commits as versioned patch sets with explicit inter-version diffs; branch-centric tools review the cumulative diff between two branches.
- **Pre-merge vs post-commit posture.** Approval-before-landing vs land-then-review (see How It Works).
- **Enforcement posture.** Advisory → optional → required, per project and branch.
- **Verdict grammar.** Binary approve/request-changes; graded label votes (e.g. a −2…+2 scale where votes do not accumulate); approval markers combined with per-comment issue states.
- **Ownership routing depth.** From manual reviewer picks to path-ownership files, review groups, default reviewers, and category-based approval rules (backend / frontend / security / database).
- **AI participation.** AI reviewers that post findings, respond to comments, or push follow-up commits; AI assistance embedded in the review surface.
- **Beyond code.** Review of images, documents, and text artifacts on the same machinery.
- **Delivery.** SaaS vs self-hosted; enforcement features are frequently tier-gated in commercial offerings.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Source Code Hosting Platform | adjacent, heavily co-delivered | hosting centers repository storage, browsing, and permissions; review centers the change-review workflow. Remove the review workflow → a hosting platform remains; remove repository hosting → a standalone review platform remains. Modern hosting platforms embed review; standalone review tools attach to external repos |
| Code Quality Platform | adjacent, automation-side | system of record for *automated* analysis state (issues, metrics, thresholds, analyzer verdicts); the review platform is the system of record for the *human* review conversation and verdict. They meet where checks surface on the change and bots post review comments |
| Static Code Analysis Platform | upstream feeder | analyzers produce findings; the review platform is where findings land as checks/comments on a change and where humans respond |
| Issue Tracker | adjacent | managed object is a work item, not a proposed change; review threads can be exported to issues, but the change review is the core |
| Version Control System | substrate | branches, commits, and diffs are the raw material; the review platform organizes collaboration around a proposed change on top of them |
| Continuous Integration Platform | adjacent, check-provider | CI executes builds/tests and reports status onto the change; it does not host the review conversation or verdict |
| AI Coding Assistant / Agent | participant-side | assistants author code; the review platform judges changes. AI reviewers act inside the review loop, not as the Type |
| Peer Review Platform (academic) | same verb, different domain | reviews grant submissions/papers against criteria, not diffs of code changes against a base revision |

## Representative Products

- **Gerrit Code Review** — standalone, review-first; patch-set changes pushed to a review ref; graded label votes gate submission; used by very large open-source projects and enterprises.
- **GitHub** — pull requests embedded in a leading source-hosting platform; branch-diff review with approve/request-changes verdicts, code-owner routing, and optional branch protection.
- **GitLab** — merge requests embedded in a DevOps platform; explicit assignee/reviewer roles, tiered approval rules, thread-blocking and auto-merge.
- **Review Board** — standalone, repository-agnostic review layer since 2006; review requests with uploaded diffs, per-comment issue tracking, Ship It approvals; supports both pre-commit and post-commit workflows and performs no merge itself.

The definition was checked against older and differently-shaped products (the Mondrian/Rietveld lineage documented by Gerrit's official history, and Review Board's pre-/post-commit workflows) so that it does not over-fit the modern branch-based pull-request pattern.

## Sources

Research date: **2026-09-07**

- Gerrit — "How Gerrit Works" and "Working with Gerrit: An example" (official documentation, v3.14.2): https://gerrit-documentation.storage.googleapis.com/Documentation/3.14.2/intro-how-gerrit-works.html , https://gerrit-documentation.storage.googleapis.com/Documentation/3.14.2/intro-gerrit-walkthrough.html
- Gerrit — "Gerrit's History" (official site): https://www.gerritcodereview.com/about.md
- GitHub — "About pull requests", "Reviewing proposed changes in a pull request", "About code owners" (official docs): https://docs.github.com/en/pull-requests
- GitLab — "Merge requests", "Merge request approvals" (official docs): https://docs.gitlab.com/ee/user/project/merge_requests/ , https://docs.gitlab.com/ee/user/project/merge_requests/approvals/
- Review Board — "What is Code Review?", "Review Board Workflows", "Issue Tracking", "Approving Changes (Ship It!)" (official manual, latest): https://www.reviewboard.org/docs/manual/latest/

> Sourcing limitation: the canonical Gerrit documentation host was unreachable from the research environment (repeated timeouts); the official documentation mirror on storage.googleapis.com was used instead (same content, version 3.14.2). Bitbucket, Azure DevOps, and the discontinued standalone review tools (Phabricator Differential, Atlassian Crucible) were not directly researched; no claims about them are made in this document. Precise vendor-specific mechanics (label scales, tier gating, dismissal rules, size limits) are recorded in the paired Research Notes rather than asserted here.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
