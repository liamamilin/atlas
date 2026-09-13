# Source Code Hosting Platform

## Overview

A **Source Code Hosting Platform** is a networked service that holds a software project's source code as version-controlled repositories — the shared authoritative copy that a team or community works against — and provides the application surface for browsing that code, controlling who can access it, and collaborating on changes to it.

The defining structure is small:

```text
Hosted version-controlled repository (the system of record)
└── Networked multi-user access under access control
    └── Platform application surface (browse / manage / administer)
```

- **Hosted repositories as the system of record** — the platform holds each project's code as a persistent, identified, version-controlled repository: files plus their full revision history, kept as the one shared authoritative copy rather than on any individual's machine.
- **Networked multi-user access under access control** — authorized people reach the repository over the network to read it (clone, fetch, browse) and, where permitted, update it (push); the platform holds the accounts and decides who may read and write each repository.
- **The platform application surface** — a managed, web-first application over the repositories: browse code and history, create and manage repositories, administer people and permissions. This surface is what makes it a platform rather than a bare version-control server.

Everything else the market associates with these products — pull requests, issue trackers, wikis, CI pipelines, package registries, stars and social profiles — is collaboration machinery layered on that spine. Much of it is an embedded instance of a neighboring Application Type (code review, issue tracking, continuous integration, package registries) rather than part of what makes this Type what it is. The first-generation project forges and today's minimal self-hosted forges are fully recognizable instances of this Type without any of that machinery.

## Users & Context

Primary users:

- **developers** — clone repositories, keep local working copies, push commits, browse code and history on the web when they need context
- **contributors** — people outside the direct write access circle who propose changes (commonly through a fork and a proposed-change request, or a patch in older-generation products)
- **maintainers / project admins** — manage repositories, review and merge proposed changes, configure branches and settings, grant or revoke access

Secondary users:

- **organization administrators** — manage members, teams/groups, organization-wide policies and security
- **occasional readers** — people who only browse code, README pages, or download a release; in public-community products this population is large

Context: the platform is the daily home of a team's code. Work starts from it (clone, issue, branch) and returns to it (push, propose, review, merge). It serves both private enterprise settings (private repositories, controlled membership, compliance) and public open-source communities (public repositories, anonymous read access, self-serve contribution).

## Core Model

### The Defining Core

```text
Account / Group container (ownership)
└── Repository  ← the central object
    ├── Version-controlled content: files + full revision history
    │   (commits, branches, tags — the version-control substrate)
    ├── Visibility (public / private)
    └── Access control (who may read, who may write, who administers)
└── Platform application surface over all of the above
```

- **Repository** — the central object. A persistent, identified, version-controlled store of one project's source code and its complete revision history, addressable by a stable URL path. Every product in this space is organized around repositories; what differs is what sits above them.
- **Version-control substrate** — the repository's content model comes from a version-control system: commits form the history, branches are parallel lines of work, tags mark points of interest. The platform exposes and manages this substrate; it does not replace it. Git is the dominant substrate today; older and some current products also host other version-control systems.
- **Ownership container** — repositories are owned either by an individual account or by a group container (organization, group, workspace, project — naming varies). The container carries membership, team structure, and often default permissions.
- **Access control** — accounts, per-repository roles (read / write / administer), visibility levels, and branch-level restrictions together decide what each person can do. Visibility (public vs private) is a first-class property of the repository, not a plan detail: public repositories are readable by anyone, private ones only by explicitly authorized people.
- **Application surface** — the web application through which all of the above is seen and managed, plus the network endpoints (HTTPS/SSH) that version-control clients use.

### Collaboration Machinery Layered on the Spine

Mature products commonly add these. They are not what makes the product a hosting platform, and several are embedded instances of neighboring Application Types:

- **Proposed-change workflow (pull request / merge request)** — an embedded instance of the Code Review Type: a proposed set of changes held as a reviewable object with a diff, a line-anchored discussion, and a recorded merge decision.
- **Forking** — a new repository created as a copy of another, with its own settings and permissions but a live connection to the original, so changes can be proposed back. This is the community-scale collaboration shape; enterprise settings often work branch-first inside one repository instead.
- **Issue tracking** — an embedded instance of the Issue Tracker Type: work items, bug reports, and tasks attached to the project.
- **Wiki / project pages** — documentation held beside the code, with README files rendered as the repository's front page.
- **Built-in CI/CD** — an embedded instance of the Continuous Integration Type: automated runs triggered by changes to the repository.
- **Package registries** — an embedded instance of the Package Registry Type in several products.
- **Notifications, activity feeds, search, webhooks, API** — the connective tissue that makes the platform operable at team and ecosystem scale.

### One Spine, Many Shapes

The container hierarchy above the repository is a shape variant, not a difference in kind:

```text
Repository-first:   account / organization → repositories
Project-first:      group → project (which contains the repository)
Workspace-nested:   workspace → project → repositories
Forge-classic:      project → tools (repositories attached as one tool among several)
```

## How It Works

### Put a repository on the platform

```text
Create a repository (blank, from a template, or by importing/migrating an existing one)
→ or fork an existing repository into your own namespace
→ or push an existing local repository to the platform
```

The repository becomes addressable at a stable path and appears in the web application with its own settings, access list, and history.

### Get the code and make changes

```text
Clone the repository over HTTPS or SSH (or download a snapshot archive)
→ create a branch
→ commit changes locally (or edit files directly in the web application)
→ push the branch back to the platform
```

The hosted repository is the shared authoritative copy; local clones are working copies. Changes become part of the shared history only when pushed — and pushing is exactly where access control bites: read access does not imply write access.

### Propose and land changes

```text
Open a proposed-change request (pull request / merge request) from a branch or a fork
→ reviewers see the diff and discuss line by line
→ automated checks may run against the change
→ a maintainer merges it into the target branch (or declines it)
```

This loop is the dominant modern collaboration shape. It is an embedded review workflow: the hosting platform remains a hosting platform without it, and first-generation products coordinated changes through patches and direct grants instead.

### Control who can do what

```text
Set repository visibility (public / private)
→ grant access to individuals and/or teams-groups
→ assign roles (read / write / administer)
→ optionally protect branches: restrict who may push or merge into them
```

Organization-level containers let administrators manage many repositories and many people at once; repository-level settings refine the picture per repository.

### Live with repositories over time

```text
Rename or transfer a repository — old paths and remote URLs redirect, so existing clones and automation keep working
→ archive a repository that is no longer active
→ delete when truly done (a deliberate, permission-gated operation)
```

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Repository home / code browser

The primary surface for one repository.

- file tree of the selected branch, rendered file contents, README as front page
- primary actions: browse directories and files, switch branch/tag/revision, clone or download, open history

### History, branches, and comparison views

The revision-history surfaces.

- commit list with authors and messages, per-file blame, branch and tag lists, diff between any two revisions
- primary actions: inspect a commit, compare revisions, create a branch or tag

### Proposed-change surface (pull / merge request)

The review conversation around one proposed change.

- diff against the target branch, line-anchored comments, status of checks, merge controls
- primary actions: open a proposal, review and comment, approve or request changes, merge or decline

### Issue tracker surface

Work items attached to the project.

- issue list with labels, assignees, and states; per-issue discussion
- primary actions: open an issue, comment, link to commits and proposed changes, close

### Repository settings

The administration surface for one repository.

- visibility, collaborator/team access and roles, branch protection, webhooks, danger-zone operations (transfer, archive, delete)

### Organization / group administration

The container-level surface.

- members and teams, container-level permissions, organization-wide settings

### Transport endpoints and API

Not pages, but equally real surfaces: the HTTPS/SSH endpoints version-control clients talk to, the REST API, and webhooks that push events outward to other systems.

## Important Rules / Behaviors

- **The hosted repository is authoritative.** Local clones are working copies; the shared history lives on the platform. All coordination ultimately flows through push and merge against it.
- **Read and write are separately gated.** Anyone may read a public repository (often without an account); writing always requires explicit authorization. Roles decide who may push, who may merge, and who may administer.
- **Visibility is a structural property.** Public/private is chosen per repository and has direct security consequences; changing it later affects everything attached to the repository, including forks.
- **Forks are separate repositories, not branches.** A fork carries its own settings, permissions, and collaboration space, while staying connected to its upstream so changes can be proposed back. In fork-centric products the upstream and its forks form a connected network that shares underlying data; exactly how visibility and permissions propagate across that network varies by product.
- **Branches can be protected.** Protected branches restrict who may push or merge into them — the platform-level enforcement point for "changes to this line of code must be reviewed first".
- **History is durable and append-shaped.** Commits accumulate; rewriting or deleting history is possible but is a controlled, permission-gated operation precisely because other people's work depends on it.
- **Paths are stable and redirect.** Renames and transfers keep old URLs and remote addresses working through redirects, because external automation and existing clones depend on them.
- **Embedded objects cross-link.** Issues reference commits, proposed changes reference issues, checks attach to proposals — the repository's history and the project's work items form one linked record.

## Variants

- **Social-coding community platform** — public repositories at the center, anonymous read access, fork-and-propose contribution, stars/follows/explore discovery, self-serve open-source communities at scale.
- **Enterprise private instance** — private repositories, organization/team permission structures, compliance machinery (managed authentication, audit, IP controls); delivered as SaaS or self-managed.
- **Open-core dual delivery** — the same product line offered as a hosted service and as a self-managed instance.
- **Suite member** — code hosting as one module of a wider software-delivery suite, with the deepest value in integration with the suite's planning and build tools.
- **Lightweight self-hosted forge** — a single deployable service for individuals and small teams, minimal resource footprint, the collaboration machinery present but lean.
- **First-generation project forge** — the project (not the repository) as the container, multiple version-control systems side by side, file-release downloads as the primary distribution channel to users, patch-based contribution; historically the founding shape of the Type.
- **Multi-VCS hosting** — hosting more than one version-control system (Git alongside Subversion/Mercurial) rather than Git alone.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Version Control System | substrate | the VCS is the versioning machinery (commits, branches, diffs) and runs entirely locally with no accounts or venue; the hosting platform is the centralized networked venue built around a VCS, adding accounts, access control, and the application surface |
| Code Review Platform | embedded instance + standalone sibling | the review platform's organizing spine is the change-review workflow; hosting platforms embed that workflow as pull/merge requests, but remain repository-centered. Standalone review products attach to repositories hosted elsewhere |
| Issue Tracker | embedded instance + standalone sibling | work items vs version-controlled source as the unit of record; hosting platforms embed trackers, standalone trackers attach to code hosted elsewhere |
| Package Registry | embedded instance + standalone sibling | built, consumable artifacts vs source of record; several hosting platforms embed registries |
| Artifact Repository | adjacent | custody of built artifacts under stable coordinates; no version-controlled source spine |
| Continuous Integration Platform | embedded instance + standalone sibling | change-bound automated runs; embedded in most modern hosting platforms but a distinct Type |
| Code Search Platform | adjacent | search-primary over a managed code corpus; indexes repositories without hosting them |
| Cloud Storage / File Sync | adjacent | holds files but with no version-control semantics — no commits, branches, or diffs, and no change collaboration around revisions |
| Web Hosting | adjacent | serves websites to end users; some hosting platforms add static-site publishing as an optional capability |

The most important boundary is with the **Version Control System**: the two are routinely conflated because hosting products embed a VCS. The test is the venue — a version-control system works with no server, no accounts, and no web surface at all; a hosting platform is precisely the shared, access-controlled, application-wrapped venue around one.

## Representative Products

- GitHub
- GitLab
- Bitbucket
- Gitea
- SourceForge

The defining core was checked against the first-generation forge (SourceForge generation: project containers, multi-VCS hosting, file releases, patch-based contribution) and the minimal self-hosted forge (Gitea) to avoid over-fitting the Type to the modern social-SaaS pattern.

## Sources

Research date: **2026-09-09**

- GitHub Docs — About repositories: https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
- GitHub Docs — About forks: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
- GitLab Docs — Create a project: https://docs.gitlab.com/user/project/
- GitLab Docs — Repository: https://docs.gitlab.com/user/project/repository/
- Bitbucket Cloud support — Get started with Bitbucket Cloud (documentation tree): https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/
- Gitea Docs — What is Gitea?: https://docs.gitea.com/
- SourceForge — Documentation home: https://sourceforge.net/p/forge/documentation/
- SourceForge — Git hosting: https://sourceforge.net/p/forge/documentation/Git/

> Sourcing limitation: several deep documentation pages (Bitbucket topic pages, Gitea sub-pages, the SourceForge complete user guide) were not reachable from the research environment; the reachable documentation trees and root pages were used instead. Precise operational details (permission-role names, size limits, rate behavior) are intentionally not asserted in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
