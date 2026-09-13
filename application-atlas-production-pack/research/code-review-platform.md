# Research Notes — Code Review Platform

## Research Goal

Understand the Code Review Platform as an Application Type: the core reviewable object, the review workflow and change lifecycle, the verdict model, enforcement wiring, reviewer routing, and the boundary against Source Code Hosting Platform, Code Quality Platform, Static Code Analysis Platform, and Issue Tracker.

## Initial Boundary

- Working hypothesis: the Type is organized around the **human review of proposed code changes**. The dominant modern delivery embeds review inside source-hosting platforms (pull request / merge request), but standalone review-first products exist (Gerrit, Review Board) and historically preceded the hosting-embedded form.
- Neighboring Types: Source Code Hosting Platform; Code Quality Platform (processed 2026-09-07 — its entry explicitly notes "bare analyzers belong to the analyzer layer"); Static Code Analysis Platform; Issue Tracker; Version Control System; Continuous Integration Platform; AI Coding Assistant / Agent.
- Overfitting risk: defining the Type by the GitHub-style branch-based, merge-executing pull request. The historical sample (Mondrian/Rietveld lineage, Review Board pre-commit/post-commit) must still fit.

## Research Questions

1. What is the core reviewable object, and how is it expressed (branch diff, patch series, uploaded diff)?
2. What is the change lifecycle from proposal to incorporation or abandonment?
3. How does the review conversation work (inline vs change-level, threads, resolution states)?
4. What verdict models exist (binary approve/request-changes, graded label votes, approval markers)? Who records them?
5. How are reviewers selected (manual request, automatic rules, code ownership, groups)?
6. Does the platform execute the merge itself, or hand the push back to the author?
7. How is enforcement wired (advisory vs optional vs required; branch protection; label gates)?
8. How do automated participants (CI, analyzers, AI reviewers) enter the review?
9. What roles and permissions matter (author, reviewer, approver, verifier, admin)?
10. Where are the seams to hosting, quality analysis, and issue tracking?

## Representative Products

Selected for market representation + different philosophies + different delivery shapes + historical spread:

| Product | Why selected | Delivery shape |
|---|---|---|
| Gerrit Code Review | canonical standalone review-first tool; patch/change-centric; used by very large projects; Mondrian→Rietveld descendant | self-hosted standalone (also acts as central repo) |
| GitHub | dominant market implementation; pull request embedded in hosting platform; SaaS; individual → enterprise | hosting-embedded |
| GitLab | merge request embedded in a DevOps platform; SaaS + self-managed; Free → Ultimate tier structure | hosting-embedded |
| Review Board | standalone, repository-agnostic (Git/Hg/SVN/Perforce/CVS/…), since 2006; documents both pre-commit and post-commit review; does NOT execute merges | standalone, attaches to external repos |

Historical/lineage anchors used for the market-sample check: Mondrian (Google, Perforce-based, pre-submission peer review), Rietveld (open-source, Subversion, strictly advisory) — documented on Gerrit's official history page.

## Sources

All fetched 2026-09-07. Tier 1 (official operational documentation) unless noted.

- Gerrit — "How Gerrit Works" (v3.14.2): https://gerrit-documentation.storage.googleapis.com/Documentation/3.14.2/intro-how-gerrit-works.html
- Gerrit — "Working with Gerrit: An example" (v3.14.2): https://gerrit-documentation.storage.googleapis.com/Documentation/3.14.2/intro-gerrit-walkthrough.html
- Gerrit — "Gerrit's History" (official site): https://www.gerritcodereview.com/about.md
- GitHub — "About pull requests": https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- GitHub — "Reviewing proposed changes in a pull request": https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request
- GitHub — "About code owners": https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- GitLab — "Merge requests": https://docs.gitlab.com/ee/user/project/merge_requests/
- GitLab — "Merge request approvals": https://docs.gitlab.com/ee/user/project/merge_requests/approvals/
- Review Board — "What is Code Review?": https://www.reviewboard.org/docs/manual/latest/users/getting-started/what-is-code-review/
- Review Board — "Review Board Workflows": https://www.reviewboard.org/docs/manual/latest/users/getting-started/workflow/
- Review Board — "Issue Tracking": https://www.reviewboard.org/docs/manual/latest/users/reviews/issue-tracking/
- Review Board — "Approving Changes (Ship It!)": https://www.reviewboard.org/docs/manual/latest/users/reviews/approving-changes/

Source-access limitations:
- gerrit-review.googlesource.com (canonical docs host) timed out twice → abandoned per network rule; the official storage.googleapis.com documentation mirror (version path discovered via gerritcodereview.com) was used instead. Content is the same official documentation.
- Bitbucket, Azure DevOps, Phabricator Differential, Atlassian Crucible were NOT fetched (budget; two of them discontinued). No product claims are made about them anywhere in this research or the final document.

## Product Observations

Evidence layers: **A** = directly observed in official docs of that product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

### Gerrit Code Review (Layer A)

- Self-description: "code review platform for Git-based development" (official site).
- Lineage (official history page): Google's Mondrian — Perforce-based, "peer-review of changes prior to submission to the central code repository"; Rietveld — open-source Mondrian descendant for Subversion, "strictly advisory and does not enforce peer-review prior to submission"; Gerrit — started as a Rietveld fork to serve the Android Open Source Project on Git.
- Core concept ("How Gerrit Works"): Gerrit becomes the central source repository and introduces a store of **Pending Changes**. All code changes are sent there for others to review and discuss. "When enough reviewers have approved a code change, you can submit the change to the code base." Gerrit captures notes and comments per change, providing "a history of each change (what was changed and why and who reviewed the change)". Fine-grained access-control model.
- Walkthrough (official example):
  - A **Change-Id** in the commit message links successive versions of the same change under review.
  - The author pushes to `refs/for/<branch>`; Gerrit creates a **change** (review object) with a web URL.
  - The review screen shows the **diff** (unified or side-by-side); reviewers add **inline comments** on lines and **summary comments** on the change; the author can add reviewers manually; reviewers can also find changes via search, an "Open" changes list, or email notifications.
  - **Label status** shows required checks. Default workflow has two: **Code-Review** (a person judges the code against project guidelines; default vote scale −2…+2: +2 "approved", +1 "someone else must approve", 0 no score, −1 "prefer not submitted as is", −2 "shall not be submitted"; values do **not** accumulate — two +1 ≠ +2; submit requires at least one +2 and no −2) and **Verified** (pass/fail ±1; typically an automated build server via e.g. the Jenkins Gerrit Trigger plugin; **separate permissions** so an automated process can verify without being able to code-review).
  - Rework loop: author amends the commit and pushes again → a new **patch set** on the same change; the UI can diff patch set 1 vs patch set 2; the author signals rework with a "Done" reply.
  - Manual verification is supported: each change is exposed as a Git branch that a reviewer with the Verified permission can fetch and check out.
  - **Submit** merges the change into the target branch — the change becomes part of the project.
- Interpretation: Gerrit is the purest form — review is the organizing spine; hosting is instrumental (the central repo exists to receive submitted changes).

### GitHub (Layer A)

- "About pull requests": a PR is "a proposal to merge code changes into a project"; GitHub's "key collaboration feature" for discussing and reviewing changes before merging. The PR page organizes review context into tabs: **Conversation** (description, timeline, comments, reviews), **Commits**, **Checks** (automated tests, builds, other validations), **Files changed** (the diff reviewers use), **Findings** (automated code review results such as code scanning alerts). A **merge status** in the header/merge box "highlights blockers, missing approvals, and other requirements before merging".
- **Draft pull requests**: cannot be merged; code owners are not auto-requested until marked ready for review; convertible back to draft.
- Development models: **fork and pull** (anyone with read access can fork; popular in open source) vs **shared repository** (collaborators push topic branches; "pull requests … start code review and general discussion about a set of changes before the changes are merged into the main development branch").
- Reviewing (official how-to): review file by file; mark files **Viewed** (collapses; unmarks if the file changes again); progress bar of viewed files; hover a line to comment; comment on a **range of lines**; **suggestion blocks** propose specific replacement lines the author can commit; file-level comments; pending comments are visible only to the reviewer until the review is submitted (can be edited or the review abandoned).
- **Submitting a review** — three verdicts: **Comment** (general feedback), **Approve** ("submit your feedback and approve merging the changes"), **Request changes** ("feedback that must be addressed before the pull request can be merged").
- Enforcement nuance (same page): "The Request changes option is purely informational and will not prevent merging unless a ruleset or classic branch protection rule is configured with the 'require a pull request' option." With required reviews + stale-review dismissal enabled, pushing new commits **dismisses existing approvals**; the PR must be re-approved. "Pull request authors cannot approve their own pull requests." Repository owners/admins can merge without approving review. Approvals from Copilot do not count toward merge requirements (AI participant, not an approver).
- **CODEOWNERS**: a file mapping path patterns to owners (users/teams with write access); owners are **automatically requested for review** when a PR modifies their paths; branch protection can "Require review from Code Owners" (an approval from *any* of the owners of a path suffices); per-branch CODEOWNERS; draft PRs do not auto-request owners.
- Interpretation: the PR is a branch-diff review object embedded in hosting; enforcement is optional wiring layered on top of an advisory-by-default verdict system.

### GitLab (Layer A)

- "Merge requests": "a central location for your team to review code, have discussions, and track code changes"; can be linked to issues (auto-close on merge). Viewing an MR shows: description; code changes and inline code reviews; CI/CD pipeline info; **mergeability reports**; comments; commit list.
- **Roles**: **Assignee** "owns the merge request and is responsible for its progress" (usually the author); **Reviewer** "reviews the changes and provides feedback… can request changes or, if eligible, approve". "Your project's approval rules and settings determine who can approve."
- **Approvals**: Free tier — all users with Developer+ role can approve; approvals are **optional and don't prevent merging**. Premium/Ultimate — **required approval rules**: number and type of required approvals; reviewer categories (backend/frontend/QA/database/documentation); **CODEOWNERS** file determines reviewers; coverage-check approval rules; security-team approval policies (Ultimate). Approval widget statuses: Approve / Approve additionally / Revoke. Per-reviewer status icons: awaiting review / review in progress / approved / reviewer commented / reviewer requested changes. `/approve` quick action. Merge can be blocked by: merge conflicts, open threads (setting "All threads must be resolved"), failed CI/CD pipeline. Setting: **Prevent approval by merge request creator**. Impossible-to-satisfy rules are marked "Auto approved" (unblocked) unless policy-created.
- **Threads**: single comments vs threads; open (unresolved) threads can block merge (project setting); threads auto-resolve when a push makes their diff section outdated (setting); open threads can be moved to issues.
- **Merge**: default merge permissions from project role + branch protection (default branch protected; Maintainers+ merge into it); **auto-merge** — a reviewer can set the MR to merge automatically when checks pass; close (preserves records); delete source branch; chained/stacked MRs are retargeted when their target branch merges; squash and merge; merge methods (merge commit / fast-forward).
- Documented developer workflow: branch → MR → feedback → code quality reports → unit test reports → approval from manager → auto-merge → deploy.
- Interpretation: same branch-diff review object as GitHub, with a stronger built-in approval-rule system (tier-gated) and explicit assignee/reviewer role separation.

### Review Board (Layer A)

- "What is Code Review?" (official manual): distinguishes **peer/human code review** from **automated code review** (lint, static analysis, automated testing, CI — "best paired with peer/human code review"). Two workflow postures: **pre-commit review** ("code is developed locally, put up for review, and is only pushed to the repository after approved by reviewers") and **post-commit review** ("the code is committed to the repository first. Then, at some point later, the code is reviewed"). Review Board "has been helping companies achieve this since 2006".
- Workflows (official manual):
  - **Pre-commit**: make change locally → create a **review request** (web UI or `rbt post` CLI) → publish → reviewers see it on their **Dashboard** → reviewers discuss, **open issues**, or approve → if issues: update code, update the review request with the new diff, republish, loop → if approved ("Ship It!"): **the author pushes the change to the upstream repository** (Review Board does not push) → close the review request as Completed (auto-close possible if the repository is configured for it).
  - **Post-commit**: push first → create review request for the commit(s) → same review loop → fixes are new commits pushed upstream → close.
  - Note: some features (e.g. **interdiffs** — diffs between successive versions of a diff) are built with pre-commit review in mind.
- **Issue tracking** (official manual): "some comments are more critical than others… a critical issue that must be resolved before the change can be submitted." A comment can be filed as an **open issue** (default checkbox on). The review-request owner marks issues **Fixed** or **Drop** (with follow-up comment), issues can be **re-opened**; an **issue summary table** lists all issues with status filters (Open/Dropped/Resolved) and per-reviewer filters; **Issue Verification** — for critical issues, the owner cannot close the issue until the reviewer (or admin) approves the resolution.
- **Ship It!** (official manual): the approval marker. "By default, review requests are considered approved if there's at least one Ship It! and no open issues, but this can be customized by writing an extension that implements custom approval logic." Variants: Ship-It-only quick review; Ship It + comments; **"Fix It, then Ship It!"** (approve while filing remaining issues; transitions to full Ship It when the last issue resolves); **revoking** your own Ship It.
- Administration: **review groups**, **default reviewers** (rules that auto-add reviewers), permission groups, access control, per-repository configuration across many VCS/backing services (Git, SVN, Perforce, Mercurial, CVS, ClearCase, GitHub, GitLab, Bitbucket, Azure DevOps, …), webhooks, extensions, CI/chat integrations.
- Interpretation: a pure review layer with no hosting and no merge execution — proves that merge execution and repository hosting are NOT definitional. Verdict model is marker-based (Ship It) plus per-comment issue states, advisory by default with policy/extension-based enforcement.

## Cross-product Comparison

| Dimension | Gerrit | GitHub | GitLab | Review Board |
|---|---|---|---|---|
| Core reviewable object | Change (patch sets linked by Change-Id) | Pull request (branch diff) | Merge request (branch diff) | Review request (uploaded diff) |
| Diff expression | commit pushed to `refs/for/<branch>` | head branch vs base branch | source vs target branch | uploaded diff against repository state |
| Inline line comments | yes (unified / side-by-side) | yes (line or line-range) | yes (threads) | yes (diffs, images, file attachments) |
| Change-level discussion | summary comments / cover message | Conversation tab | MR description + comments | review-request description + general comments |
| Verdict model | graded label votes (Code-Review −2…+2 default; Verified ±1 pass/fail) | Comment / Approve / Request changes | Approve + per-reviewer status; required-approval counts | Ship It! marker + per-comment open issues |
| Verdict recorded per reviewer, attributable | yes (votes with names) | yes (reviews) | yes (approvals + status icons) | yes (reviews) |
| Author self-approval | not directly evidenced | blocked | blocked via setting | not directly evidenced |
| Reviewer routing | manual add; search; email notifications | manual request; CODEOWNERS auto-request | manual request; approval rules; CODEOWNERS; automatic reviewer assignment | manual; review groups; default reviewers |
| Versioning of the change | patch sets; inter-version diff | new commits on PR branch | new commits; MR versions | new diffs; interdiffs |
| Discussion resolution state | reply/vote flow | (resolve/conversation resolution not directly fetched) | resolve threads; threads can block merge | open issues: Fixed / Drop / Re-open; verification |
| Merge execution | yes — Submit merges into branch | yes — merge box | yes — merge + auto-merge | **no — author pushes externally** |
| Merge strategies | (not fetched) | (not fetched in detail) | merge commit / squash / fast-forward | n/a |
| Enforcement | labels gate submit (configurable per project) | advisory by default; required via rulesets/branch protection | optional (Free) vs required rules (Premium/Ultimate) | advisory by default; org policy / extension approval logic |
| Automated checks on the change | Verified label via CI plugin | Checks tab | pipelines + mergeability reports | Review Bot / CI integrations |
| Automated review comments | (not evidenced) | Copilot reviews & replies (does not count as approval) | Duo in MRs (nav-level evidence only) | Review Bot (automated reviews) |
| Non-code review surfaces | no | not primary | not primary | images, documents, screenshots, text/markdown files |
| Linked work items | (not fetched) | linked issues/discussions/projects/milestones | link issues; auto-close; move threads to issues | (issue tracking is comment-scoped) |
| Delivery | self-hosted standalone + acts as central repo | SaaS hosting-embedded | SaaS / self-managed hosting-embedded | self-hosted standalone, attaches to external repos |
| Heritage | 2008 (Rietveld fork for AOSP); lineage from Mondrian | PR era (2010s) | PR era | 2006 |

## Canonical Abstraction

### L0 — Defining Invariant

Three properties, deliberately minimal:

1. **Proposed change as the review unit** — a change to a version-controlled codebase expressed as a **diff against a base revision**, held as a first-class object with identity, description, and version history (branch-PR, patch-set change, and uploaded-diff realizations all satisfy this).
2. **Line-anchored review conversation** — discussion attached to specific lines/regions of the diff, plus change-level discussion; the conversation persists with the change.
3. **Recorded review verdict** — an explicit, attributable reviewer outcome (approve / request-changes / graded vote / approval marker) that the workflow treats as the gate for the change's progression.

Remove-test:
- Remove the diff/change object → the product becomes a discussion forum or issue tracker.
- Remove the human conversation → the product becomes an automated analysis tool (Code Quality / Static Analysis territory).
- Remove the recorded verdict → the product becomes a diff viewer with comments, not a review workflow.

§24 historical/market-sample check: Mondrian (2006, Perforce, pre-submission review), Rietveld (advisory, Subversion), Review Board (2006, multi-VCS, no merge execution, pre- AND post-commit), Gerrit (2008, Git, patch-set model), GitHub/GitLab (branch-PR era) — all satisfy L0 without branch-based workflows, merge execution, CI checks, code owners, or tiered plans. L0 holds across eras, VCS generations, and delivery shapes.

### L1 — Common Mature Structure

Present across the sample; expected in mature products; not definitional:

- change lifecycle states (open/draft → under review → merged/submitted, or closed/abandoned/dropped)
- reviewer routing: manual requests + automatic rules (ownership files, review groups, default reviewers, approval rules)
- diff-viewing tooling: unified/side-by-side, file tree/filtering, viewed-marking, whitespace control, inter-version comparison (interdiffs / patch-set diffs)
- threaded, resolvable discussion (resolve/done states; open-issue states; optionally merge-blocking)
- suggestion mechanics (reviewer-proposed replacement edits the author can apply)
- change metadata and links (description, linked issues, labels/milestones/projects)
- notification machinery (email, to-do lists, dashboards of changes awaiting the user)
- automated checks surfaced on the change (CI status, analyzers, coverage)
- merge/submit execution with strategies (merge commit, squash, fast-forward; auto-merge on green checks)
- search/filter over change lists; access control inherited from repository permissions; APIs/webhooks

### L2 — Variant / Optional Structure

- **Enforcement posture** — the strongest variant axis: advisory (Rietveld; Review Board default; GitHub request-changes without protection) → optional (GitLab Free) → required (Gerrit label gates; GitLab Premium/Ultimate rules; GitHub branch protection/rulesets).
- **Workflow posture** — pre-commit/pre-merge (change must be approved before landing) vs post-commit (land first, review after). Review Board documents both as first-class.
- **Delivery shape** — standalone review-first (Gerrit, Review Board) vs hosting-embedded (GitHub, GitLab). Gerrit straddles: standalone review product that also serves as the central repository.
- **Verdict grammar** — binary (approve/request-changes), graded label votes (−2…+2, non-cumulative), marker-based (Ship It) + per-comment issue states.
- **Code-ownership routing depth** — path-pattern ownership files, review groups, default-reviewer rules, category-based approval rules.
- **Merge queues / stacked or dependent changes** — stacked MRs documented (GitLab); Gerrit's dependent-changes model is implicit in its patch-series design (not directly fetched as a named feature).
- **AI participation** — AI reviewers posting comments and even pushing commits (GitHub Copilot — direct evidence); AI assistance surfaces in MRs (GitLab — nav-level evidence). AI approvals explicitly do not count as human approval where documented.
- **Non-code review surfaces** — images, documents, screenshots, text/markdown files (Review Board — direct evidence).
- **Review-process analytics** (cycle time, reviewer load) — not directly evidenced in the fetched sample; unverified, do not assert.
- **Self-hosted vs SaaS; tier-gating of enforcement features** (GitLab Free vs Premium/Ultimate).

### L3 — Vendor-specific Structure (research notes only)

- **Gerrit**: Change-Id commit-message hook; `refs/for/<branch>` magic branch; patch sets; default Code-Review label −2…+2 non-cumulative with +2-required/no-−2 submit rule; Verified label with separate permission; per-change Git branch for manual verification; Submit button; NoteDb (metadata stored in Git); Jenkins Gerrit Trigger plugin.
- **GitHub**: PR tab set incl. Findings (code scanning alerts); temporary PR refs incl. simulated merge result; draft PRs suppress code-owner auto-requests; rulesets vs classic branch protection; stale-review dismissal; Copilot cloud agent responding to review comments and pushing commits; CODEOWNERS per-branch resolution order and 3 MB size limit; fork-and-pull vs shared-repository models.
- **GitLab**: assignee vs reviewer role split; `/approve` quick action; auto-merge (formerly "merge when pipeline succeeds"); "All threads must be resolved" merge check; auto-resolve outdated threads; move-thread-to-issue; chained-MR retargeting (up to four); squash and merge; merge methods; invalid approval rules auto-approved; prevent-approval-by-creator setting; tier gating (Free vs Premium/Ultimate); review apps; CSV export; activity filtering.
- **Review Board**: `rbt post` / RBTools; interdiffs; Ship It! / "Fix It, then Ship It!" / revocation; issue open/fixed/dropped/re-open states; issue verification; review groups & default reviewers; Power Pack; RBCommons hosted service; Review Bot; RB Gateway; broad VCS adapter list.
- **Lineage**: Mondrian (Google, Perforce) → Rietveld (App Engine, Subversion, advisory) → Gerrit (Git, enforcing). Review Board independent since 2006.

## Vendor-specific Findings

See L3. Additional cross-level notes:
- The verdict grammar is genuinely heterogeneous (labels vs binary vs marker+issues) — no single model can be canonized; only "recorded, attributable verdict" is invariant.
- Enforcement strength varies even within one product by configuration (GitHub: advisory unless protected; GitLab: tier-dependent; Gerrit: per-project label configuration; Review Board: default advisory, extensible).
- Automated participants are converging (CI checks everywhere; AI reviewers emerging) but every documented case keeps the human verdict distinct from machine checks (GitHub: Copilot approvals don't count; Gerrit: Verified is a separate label/permission from Code-Review).

## Boundary Findings

- **vs Source Code Hosting Platform**: hosting centers repository storage, browsing, and permissions; review centers the change-review workflow. The dominant modern delivery embeds review inside hosting (GitHub PR, GitLab MR; Bitbucket/Azure DevOps by market position, not directly researched). Standalone review platforms attach to external repositories (Review Board) or host the repo as an instrument of review (Gerrit). Remove-test: remove the review workflow → a hosting platform remains; remove repository hosting → a standalone review platform remains (Review Board proves the pole). The Types are distinct but heavily co-delivered; the hosting-platform pass should treat PR/MR machinery as an embedded instance of this Type.
- **vs Code Quality Platform** (processed 2026-09-07): the quality platform's system of record is automated analysis state (issues, metrics, thresholds, pass/fail from analyzers); the review platform's system of record is the human review conversation and verdict on a proposed change. They meet where checks are surfaced on the change and where automated tools post review comments (Review Bot; Copilot) — automation participates in the review conversation, but the human-review loop defines this Type. The quality-platform entry's own note ("bare analyzers belong to the analyzer layer") is consistent: this Type is the human layer above the analyzer layer.
- **vs Static Code Analysis Platform**: analyzers produce findings; the review platform is where findings land as checks/comments on a change and where humans respond.
- **vs Issue Tracker**: the managed object differs — work items vs proposed changes. Review threads can be exported to issues (GitLab move-thread-to-issue); Review Board's "issue tracking" is comment-scoped review state, not a work-item system.
- **vs Version Control System**: VCS is the substrate (branches, commits, diffs); the review platform organizes collaboration around a proposed change on top of it. A review platform can be VCS-agnostic (Review Board's adapter list).
- **vs AI Coding Assistant / Agent**: assistants author code; the review platform judges changes. AI reviewers act as participants inside the review loop, not as the Type.
- **Remove-tests (what turns it into another Type)**: remove the diff/change object → forum/issue tracker; remove human conversation → quality/analysis platform; remove recorded verdict → diff viewer with comments; generalize review targets beyond code changes → document review tool (Review Board does exactly this as an extension surface, while keeping code review as its core).

## Uncertainties

- Bitbucket, Azure DevOps, Phabricator Differential, Atlassian Crucible not directly researched (fetch budget; two discontinued). No claims made about them; they are plausible additional samples only.
- Merge queues: not directly evidenced in the fetched sample (GitLab stacked MRs documented; GitHub merge queue page not fetched) — kept generic in the final document.
- Review-process analytics (review turnaround, reviewer load): not researched; marked unverified; not asserted.
- Gerrit submit types (merge-if-necessary etc.) and custom label configuration: not fetched beyond the default workflow; not asserted.
- GitLab Duo in merge requests: evidenced only at documentation-navigation level; AI-participation claims in the final document rest on GitHub Copilot (direct) and are phrased as product examples.
- Whether Gerrit blocks author self-approval by default: not directly evidenced; not claimed.
- GitHub conversation-resolution state (resolve/unresolve) was not directly fetched; resolution semantics in the final document are anchored on GitLab (threads) and Review Board (issues), phrased generically.

## Final Synthesis

A Code Review Platform is the **system of record for the human review of proposed code changes**. Its defining core is small and stable across two decades of products: a proposed change held as a reviewable diff against a base revision; a review conversation anchored to the diff's lines; and a recorded, attributable reviewer verdict that gates the change's progression. Around that core, mature products add lifecycle states, reviewer routing, diff tooling, resolvable discussion, suggestions, linked metadata, automated checks, and — in most modern products — merge execution with enforcement wiring whose strength varies from advisory to required. The Type is delivered both standalone (review-first tools attached to external repositories, with or without hosting) and embedded in source-hosting platforms; the review workflow, not the hosting, is what defines it. The sharpest seams are: hosting (storage vs review spine), code quality (automated analysis state vs human review conversation), and issue tracking (work items vs proposed changes).
