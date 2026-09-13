# Research Notes — Source Code Hosting Platform

## Research Goal

Understand what a Source Code Hosting Platform really is from real products: what the central object is, what the platform provides around it, how access and collaboration work, and where the Type's boundary sits against Version Control System, Code Review Platform, Issue Tracker, Package/Artifact Repository, Code Search Platform, and CI Platform.

## Initial Boundary

Working hypothesis before research:

- Core use: be the central shared home for a software project's source code — hosted version-controlled repositories that multiple contributors work against over the network.
- Primary users: software developers, contributors, maintainers, organization admins.
- Nearest neighbors: Version Control System (substrate vs venue), Code Review Platform (embedded PR/MR machinery — a recorded flag from that pass), Issue Tracker (embedded), Package Registry / Artifact Repository (built artifacts vs source), Code Search Platform (search-primary vs hosting-primary), CI Platform (embedded), cloud storage (no VCS semantics).
- Unknowns: is the web application surface definitional or just common? Is the fork/social layer definitional? Does the first-generation forge (SourceForge era) satisfy a minimal definition? Where exactly does "bare git server" fall out?

## Research Questions

1. What is the unit of record — repository, project, or something else — and how do the sampled products name and nest it?
2. What does the platform provide around the VCS substrate (browsing, history, branches, tags, diffs, blame)?
3. How does code get in and out (clone/push protocols, import, fork, download)?
4. How is access controlled (accounts, containers, roles, visibility, branch protection)?
5. Which collaboration surfaces are definitional vs embedded instances of other Types (PR/MR, issues, wiki, CI, packages)?
6. Is the fork/social-coding layer definitional or variant?
7. What delivery models exist (SaaS, self-hosted, open-core, suite member)?
8. Historical check: does the first-generation forge satisfy a minimal definition without PRs, social coding, or CI?
9. What is the remove-test boundary against a bare VCS server and against neighboring Types?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| GitHub | dominant SaaS social-coding platform | market representation; richest docs; fork+PR philosophy |
| GitLab | open-core, SaaS + self-managed, "single application" DevOps philosophy | different philosophy; excellent docs; self-hosted pole |
| Bitbucket | Atlassian enterprise-integration member | suite-member philosophy; enterprise tier |
| Gitea | lightweight self-hosted open-source forge | minimal-resource pole; proves the floor |
| SourceForge | first-generation project forge (1999 generation) | historical / market-sample check |

## Sources

All fetched 2026-09-09 (Tier 1 — official operational documentation):

- GitHub Docs — About repositories: https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
- GitHub Docs — About forks: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks
- GitLab Docs — Create a project: https://docs.gitlab.com/user/project/
- GitLab Docs — Repository: https://docs.gitlab.com/user/project/repository/
- Bitbucket Cloud support — Get started (documentation tree): https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/
- Gitea Docs — What is Gitea?: https://docs.gitea.com/
- SourceForge — Documentation home: https://sourceforge.net/p/forge/documentation/
- SourceForge — Git hosting: https://sourceforge.net/p/forge/documentation/Git/

Fetch notes: two Bitbucket deep-dive URLs and two Gitea sub-page URLs 404'd; the Bitbucket documentation tree (full TOC with section descriptions) and the Gitea docs root were reachable and are used as the evidence layer for those products. SourceForge's Complete User Guide URL 404'd; the documentation home and the Git hosting page were reachable. No source was retried beyond the 1–2 failure limit.

## Product A — GitHub

### Key observations (evidence layer A unless noted)

- "A repository is the most basic element of GitHub. It's a place where you can store your code, your files, and each file's revision history." Repositories "can have multiple collaborators and can be either public or private."
- Repository terminology documented: Branch, Clone ("download a full copy of a repository's data from GitHub.com"), Fork ("a new repository that shares code and visibility settings with the original 'upstream' repository"), Merge, Pull request ("a request to merge changes from one branch into another"), Remote ("a repository stored on GitHub, not on your computer"), Upstream.
- Ownership: "You can own repositories individually, or you can share ownership of repositories with other people in an organization. In either case, access to repositories is managed by permissions." Permission levels for personal-account repos; repository roles for organizations.
- Visibility: public ("accessible to everyone on the internet") / private ("only accessible to you, people you explicitly share access with…") / internal (Enterprise Cloud, enterprise accounts). Organization owners always have access to every repository in the org.
- Collaboration surfaces listed inside the repository: issues, Discussions, pull requests, Projects.
- Forks (separate doc): "Forks are repositories that start as copies of another repository… A fork has its own settings and permissions but stays connected to the upstream repository." A fork can have its own branches, members and discussions, issues and pull requests, Actions and projects, tags, labels, wikis. "A branch is part of one repository. A fork is a separate repository with its own settings and collaboration space."
- Repository network: upstream + forks + forks-of-forks share visibility; deleting a public repo promotes an active fork to upstream; private-repo forks are deleted when access is removed; private forks inherit team permissions.
- Plans gate advanced tooling for private repositories; public repos unlimited collaborators on free tier.

## Product B — GitLab

### Key observations

- Unit is the **project**: "Your repository is a component of your GitLab project… Each repository is part of a GitLab project, and cannot exist without a GitLab project. Your project provides the configuration options for your repository." (Evidence layer A; the project-with-repository nesting is a container-shape variant vs GitHub's repo-first model.)
- Offerings: GitLab.com (SaaS), GitLab Self-Managed, GitLab Dedicated — open-core dual delivery.
- Project creation: blank, from built-in/custom templates, or "create a project with `git push`". Visibility Level selected at creation; "Initialize repository with a README… create a default branch, and enable cloning."
- Repository capabilities documented: add files via web editor/UI/command line; commit to branches; clone via SSH/HTTPS or open in Xcode/VS Code/IntelliJ; download source as zip/tar archives; view repository at any Git revision (SHA/branch/tag); repository languages detection; contributor analytics; repository history graph ("visual history of the repository network, including branches and merges"); path changes with redirects ("Git remote URLs… redirect… Automation scripts or Git clients continue to work after a rename").
- Docs tree around the repository: protect your repository, branches, compare revisions, commits, forks (forking workflow), file management, file tree browser, repository size, tags, Code Owners, mirroring, changelogs, snippets, push rules, signed commits, monorepos, merge requests, remote development.
- Groups as containers above projects; project visibility levels documented under "Project visibility".

## Product C — Bitbucket

### Key observations (from the official documentation tree — deep pages not fetched)

- Containers: **workspace** ("What is a workspace?", join/create, grant access, organize members into groups, access tokens) and **project** within the workspace (create, add repositories to a project, project permissions, project branching model, project merge strategy).
- Repositories: create, import (including "Import a repository from GitHub or GitLab"), clone, push/pull, add unversioned code, split a repository, transfer ownership, delete, reduce size, maintain.
- VCS substrate: Git (docs include "DVCS workflows", "Install and set up Git", "Git and Mercurial commands" legacy page — Mercurial heritage visible in doc structure).
- Branches and forks: branch a repository, fork a repository, list branches, check out, manage unmerged branches; "Set repository privacy and forking options".
- Commits: add/edit/commit from the web, tags, GPG/SSH signed commits, username aliases.
- Pull requests explicitly framed as code review: "Use pull requests for code review" — create, review code, check build status, merge, resolve conflicts, decline, draft PRs, merge queues.
- Governance: branch permissions, "Suggest or require checks before a merge", code owners, require signed commits, custom merge checks, repository/project/workspace access tokens.
- Embedded instances of other Types: work items ("Create a work item in Bitbucket Cloud"), wiki, Pipelines (CI/CD with runners, deployments, artifacts), packages (npm/Maven/PyPI/NuGet/container registries), Snippets, Code Insights, webhooks, REST API, Jira/Compass integration, static website publishing.
- Smart Mirroring (read-replica mirrors for distributed teams).

## Product D — Gitea

### Key observations

- Self-description: "Gitea is a painless, self-hosted, all-in-one software development service. It includes Git hosting, code review, team collaboration, package registry, and CI/CD. It is similar to GitHub, Bitbucket and GitLab." Goal: "the easiest, fastest, and most painless way of setting up a self-hosted Git service."
- Code hosting feature list: "creating and managing repositories, browsing commit history and code files, reviewing and merging code submissions, managing collaborators, handling branches… tags, cherry-picking, hooks, integrated collaboration tools."
- Code review: "supports both the Pull Request workflow and AGit workflow. Reviewers can browse code online and provide review comments…"
- CI/CD: Gitea Actions, "compatible with GitHub Actions" workflows.
- Project management: "tracks project requirements, features, and bugs through columns and issues. Issues support… branches, tags, milestones, assignments, time tracking, due dates, dependencies."
- Packages: "over 20 different types of public or private software package management" (Cargo, Chef, Composer, Conan, Conda, Container, Helm, Maven, npm, NuGet, PyPI, RubyGems, Vagrant, …).
- Access control docs: permissions, blocking a user, protected branches, protected tags; MFA.
- Repository docs: Markdown rendering, blame view, push, clone filters, Code Owners, webhooks, migration (from other forges), profile READMEs, template repositories, mirror repositories, incoming email.
- Deployment: single self-hosted service; "A Raspberry Pi 3 is powerful enough to run Gitea for small workloads"; Git 2.0.0+ required; runs on Linux/macOS/Windows. Gitea Cloud (hosted offering) exists as a commercial variant. MIT-licensed open source.

## Product E — SourceForge

### Key observations (first-generation forge; historical check)

- Unit is the **project**: documentation organized as "Hosting Your Project on SF.net" — create projects, then attach tools.
- VCS hosting offered per project: Git, Subversion, Mercurial (three SCMs side by side — multi-VCS variant). Git doc: "Git is a Source Code Management (SCM) tool… which supports collaborative development of software within a team, and the tracking of changes to software source code over time."
- Access model: "Developer (read/write) access is provided via ssh"; "anonymous (read-only) access is provided via git's daemon protocol"; "Repository access may be granted or revoked from a developer using the Project Admin interface." Read/write "uses your ssh password or ssh key to authorize your access. To perform write operations, your project administrator must have granted you write access."
- Web surface: code browser ("you will be able to browse your newly-committed content via the web"), viewable-files configuration, refresh repository, permissions, rename, delete; multiple repositories per project; import via git push; webhooks; default-branch change; backups (rsync guidance).
- The non-developer path: "Software users generally do not need Git; typically they will download official file releases made available by the project instead." File Manager (file releases/downloads), Tickets, Wiki, Discussion as sibling project tools; directory/search for finding software.
- No pull requests, no social layer, no built-in CI, no built-in package registries in the documented toolset — contribution historically patch/merge-request-by-hand shaped. (Evidence layer A for absence in current docs; historical absence consistent with the generation.)

## Cross-product Comparison

| Dimension | GitHub | GitLab | Bitbucket | Gitea | SourceForge |
|---|---|---|---|---|---|
| Unit of record | repository (org optional) | project (contains exactly one repository; group above) | repository (workspace + project containers) | repository (user/org) | project (repos attached as tools) |
| VCS substrate | Git | Git | Git (Mercurial heritage) | Git (required) | Git + SVN + Mercurial |
| Network read | clone HTTPS/SSH; anonymous read on public repos | clone SSH/HTTPS; archive download | clone HTTPS/SSH; anonymous read on public repos | clone HTTPS/SSH; anonymous read on public repos | SSH/HTTPS read-write; anonymous git:// read-only |
| Network write | push by authorized collaborators | push by authorized members | push by authorized users | push by authorized collaborators | push by developers granted write by project admin |
| Web code surface | file tree, history, blame, diffs | file tree browser, history graph, blame, compare revisions | source browsing, diffs, blame | code browser, blame, history | code browser, viewable-files config |
| Repo management | create/fork/rename/transfer/archive/delete; visibility | create (blank/template/push)/fork/mirror/transfer; redirects on rename | create/import/fork/transfer/delete; privacy & forking options | create/migrate/mirror/template; rename/delete | add tool (repo), import via push, rename, delete |
| Access containers | personal account + organization (roles) | personal namespace + groups (roles) | workspace + project + groups | user + organization (teams) | project admin grants per-developer access |
| Visibility | public/private/internal (enterprise) | public/private/internal | public/private (+ forking options) | public/private | public projects; anonymous read on repos |
| Change collaboration | fork + pull request | branch + merge request (fork workflow documented) | branch + pull request (framed as code review); merge checks | pull request + AGit workflow | none documented (patch-era generation) |
| Issue tracking | Issues (+ Projects boards) | issues in projects | work items | issues (milestones, assignments, dependencies) | Tickets tool |
| Wiki | wiki per repo | wiki in projects | wiki | wiki | Wiki tool |
| Built-in CI | Actions | CI/CD pipelines | Pipelines | Gitea Actions | none |
| Built-in package registry | (GitHub Packages — not fetched this pass) | container/other registries | npm/Maven/PyPI/NuGet/container | 20+ registry types | none (file releases instead) |
| Release/download surface | Releases | releases | Downloads (deploy artifacts) | releases/attachments | File Manager file releases — the primary distribution channel of its generation |
| Social layer | stars, follows, explore, contribution graph | topics, badges (lighter) | minimal | minimal | directory ranking/download counts |
| Delivery model | SaaS (+ enterprise server offerings) | SaaS + self-managed + dedicated (open-core) | SaaS (+ Data Center line) | self-hosted open source (+ hosted cloud variant) | hosted service (community/business directories) |
| Extensibility | webhooks, REST/GraphQL API, Marketplace | webhooks, API, integrations | webhooks, REST API, Marketplace apps | webhooks, API, OAuth2 | webhooks, API |

Evidence layer B (cross-product commonality): hosted version-controlled repositories; networked read with anonymous read on public repos; authorized write; web code browsing; repo management incl. import/mirror/rename; access containers with roles; visibility levels; issues; wiki; webhooks/API. Present in all five sampled products (issues/wiki/webhooks present in all five; CI in four of five; package registries in four of five; social layer strong in one, light in three, absent in one).

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The hosted repository as the system of record** — a persistent, identified, version-controlled store of a software project's source code (files plus full revision history), held by the platform as the shared authoritative copy rather than on any individual's machine. Remove → local VCS working copies with no shared home, or plain file storage.
2. **Networked multi-user access under access control** — authorized users reach the repository over the network to read it (clone/fetch/browse) and, where permitted, update it (push); the platform holds accounts and decides who may read and write each repository. Remove read → write-only drop box; remove write → read-only code mirror/browse site (Code Search Platform territory); remove access control → unauthenticated file server, below the platform bar.
3. **The platform application surface over the repositories** — a managed application (web-first) through which people browse code and history, manage repositories, and administer access — the shared venue that makes the hosted repository a place others work with, not just a server endpoint. Remove → bare VCS server (infrastructure, not a platform).

Jointly-held load-bearing:

- 1 alone = file server / storage bucket
- 2 without 3 = bare git server / git daemon — hosting without a platform
- 3 without 1+2 = a web application with nothing to host
- 1+2 without 3 = SSH-only VCS server — still not a hosting *platform*
- 1+3 without 2 = static code archive / read-only mirror — not hosting, browsing territory
- 2+3 without 1 = file-sharing application (no version-control semantics)

### L1 — Common Mature Structure

Present across the sampled products; expected in any mature offering but not required to recognize the Type:

- web code browsing: file tree, rendered file view, commit history, blame, branch/tag views, revision comparison/diffs
- repository management: create (blank/template/import), rename/transfer (with redirects), archive, delete, default branch, mirroring
- accounts + grouping containers (organizations / groups / workspaces / projects) with member management and repo-level roles (read/write/admin)
- visibility as a first-class property (public/private, internal in enterprise tiers)
- Git transport over HTTPS and SSH; archive downloads
- change collaboration: pull/merge request flow and forking (embedded instance of the Code Review Type)
- issue tracking (embedded instance of the Issue Tracker Type)
- wiki / project pages / README rendering
- notifications, activity feeds, watching
- search over code and repositories
- webhooks and REST API
- code owners, signed commits, large-file support

### L2 — Variant / Optional Structure

- social-coding layer: stars, follows, explore/trending, public profiles, contribution graphs (strong in the SaaS community pole; light or absent elsewhere)
- built-in CI/CD (embedded instance of the CI Type): present in four of five sampled products, absent in the first-generation forge
- built-in package registries (embedded instance of the Package Registry Type)
- release/download management: file releases were the primary distribution channel of the first generation; modern products offer tagged releases as a secondary surface
- VCS substrate breadth: Git-dominant today; SVN/Mercurial co-hosting in the first-generation forge; Mercurial heritage in one enterprise product
- delivery model: SaaS-only / self-hosted-only / open-core dual / suite member
- collaboration shape: fork-centric (community) vs branch-centric (enterprise) vs patch-based (first generation)
- container shapes: repo-first with optional orgs vs project-first (project contains the repository) vs workspace/project nesting
- enterprise compliance machinery: SAML/LDAP, audit, IP allowlists, managed users
- static site hosting from a repository (Pages-style features)

### L3 — Vendor-specific Structure (research notes only)

- GitHub: Copilot, Marketplace, Sponsors, Gists, Codespaces, Dependabot, repository rulesets/push rulesets, Enterprise Managed Users, Discussions as a distinct surface
- GitLab: Duo AI, epics, value-stream analytics, Dedicated offering, repository languages via linguist, SHA-256 repository experiment
- Bitbucket: Jira/Compass integration depth, Smart Commits, Sourcetree, Snippets, Agentic Pipelines/Rovo Dev, Smart Mirroring
- Gitea: AGit workflow, single-binary Raspberry-Pi-scale deployment, Gitea Cloud hosted variant
- SourceForge: download mirror network, business-software directory, Allura base, project-of-the-month promotion

## Vendor-specific Findings

- Fork semantics differ in depth: the SaaS community pole documents a full "repository network" model (fork visibility tied to upstream, permission inheritance for private forks, upstream promotion on deletion); the enterprise pole treats forking as an option to enable per repository; the lightweight forge supports forking without the network machinery; the first-generation forge has none.
- The first-generation forge's access model is coarser: per-developer grant/revoke by the project admin, explicitly noting that fine-grained path-level permissions are not supported.
- One product's unit of record is a project that *contains* the repository ("cannot exist without a GitLab project"); the others treat the repository as the primary unit with containers above it. Container shape is a variant axis, not a Type split.

## Boundary Findings

- **vs Version Control System (sibling leaf, unprocessed)**: the VCS is the versioning machinery (Git/SVN/Mercurial — runs entirely locally, no accounts, no venue, no web surface); the hosting platform is the centralized networked venue built around a VCS, adding accounts, access control, and the application surface. A hosting platform embeds a VCS as substrate; a VCS does not imply hosting. Remove-test: remove the hosting venue → the VCS remains fully functional (local repositories); remove the VCS → file hosting/cloud-drive territory, not this Type. Flag recorded for the version-control-system pass to confirm the seam from its side.
- **vs Code Review Platform (processed; recorded co-delivery flag — DISCHARGED from this side)**: the spine test holds. The hosting platform's organizing spine is repository storage/browsing/permissions; the review platform's spine is the change-review workflow. Pull-request/merge-request machinery inside hosting products is an embedded instance of the Code Review Type, not part of this Type's definition. Remove-test both ways: remove the review workflow → the hosting platform remains a hosting platform; remove repository hosting → a standalone review platform remains (Review Board proves the no-hosting pole; Gerrit straddles by also serving as a central repository). Keep-both ratified.
- **vs Issue Tracker**: the managed object differs — work items vs version-controlled repositories. Hosting products embed issue trackers as sibling tools; standalone trackers (Jira-class) attach to code hosted elsewhere. Remove issues → hosting platform unchanged; remove repositories → it is an issue tracker.
- **vs Package Registry / Artifact Repository**: built, consumable artifacts vs source of record. Hosting products embed package registries (four of five sampled) but the Type's defining record is version-controlled source. Remove registries → hosting platform unchanged.
- **vs Code Search Platform**: search-primary over a managed corpus vs hosting-primary. Code search indexes repositories without hosting them; hosting products include search as a capability, not as the spine.
- **vs Continuous Integration Platform**: change-bound automated runs. Embedded in four of five sampled hosting products; the first-generation forge proves hosting without CI. Remove CI → hosting platform unchanged.
- **vs Cloud Storage / File Sync**: no version-control semantics (no commits/branches/diffs), no VCS substrate, no change collaboration around revisions. The VCS binding is what keeps this Type distinct.
- **vs Web Hosting / static site hosting**: serves websites to end users vs serves code development. Pages-style features are optional capabilities of hosting platforms.
- **vs "DevOps platform" market drift**: one sampled product self-labels as a DevOps platform and another as an "all-in-one software development service" — market positioning has drifted suite-ward, but the hosting spine (repositories + networked access + application surface) is what makes both instances of this Type. Recorded as market-position note, not a taxonomy split.
- **Remove-tests for the Type itself**: remove version control → file hosting; remove networked multi-user access → local VCS; remove the application surface → bare VCS server (infrastructure); remove authorized write → read-only code mirror (browse/search territory); remove the repository as unit → generic project workspace.

## Historical / Market-Sample Check

The first-generation forge (SourceForge generation, 1999-era: CVS/SVN hosting, project containers, file releases, tickets/wiki/discussion, patch-based contribution) satisfies all three L0 structures with none of the modern machinery — no pull requests, no social layer, no built-in CI, no package registries. The lightweight self-hosted forge satisfies L0 at Raspberry-Pi scale with a single binary. Enterprise suite members satisfy L0 with private instances and compliance machinery. Conclusion: the L0 does not over-fit to the modern social-SaaS pattern; the social layer, PRs, CI, and registries are correctly held at L1/L2.

## Uncertainties

- Azure DevOps Repos was not directly researched this pass (enterprise-suite pole covered by Bitbucket's documentation tree instead); its TFVC+Git dual substrate is known market position, not directly observed here.
- Exact permission-role names, repository size limits, and API rate behavior vary by product and plan; no precise numbers are asserted.
- "Internal" visibility (enterprise tier of one sampled product) is a single-product observation; not generalized.
- Current breadth of non-Git VCS support among the large SaaS products was not verified beyond the first-generation forge (which documents Git+SVN+Mercurial) and one product's Mercurial heritage in doc structure.
- GitHub Packages was not fetched this pass; package-registry embedding is evidenced by GitLab/Bitbucket/Gitea documentation.

## Final Synthesis

A Source Code Hosting Platform is the networked system of record for software source code: it holds a project's source as version-controlled repositories, lets authorized people reach those repositories over the network to read and (where permitted) update them, and wraps them in a managed application surface for browsing, administration, and collaboration. Its defining core is exactly those three jointly-held structures. Everything the market associates with modern forges — pull requests, issues, wikis, CI, package registries, stars and follows — is collaboration machinery layered on that spine, much of it embedded instances of neighboring Application Types (Code Review, Issue Tracker, CI, Package Registry). The first-generation forges and the minimal self-hosted forges prove the core stands without any of that machinery.
