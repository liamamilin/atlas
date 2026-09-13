# Package Registry

## Overview

A **Package Registry** is the server-side venue of a package-manager ecosystem: the place where the ecosystem's packages live as a persistent catalog, where maintainers publish new packages and versions into that catalog, and where the ecosystem's package-manager clients resolve and fetch packages from.

Every package ecosystem is split into two sides. On the developer's machine sits the **client** — the package manager and dependency tooling that declares, selects, and installs dependencies. On the network sits the **registry** — the shared catalog that the client talks to. The registry is not the tool and the tool is not the registry; they are the two halves of one ecosystem's package flow, connected by the ecosystem's own registry protocol.

The problem it exists to solve is sharing at ecosystem scale: thousands of independently developed packages, published by independent maintainers, consumed by thousands of other projects. Someone must hold the authoritative catalog of what packages exist under what names, at what versions — and hand them out on demand. The registry is that holder. It defines the ecosystem's shared namespace (who owns which package name), preserves the packages once published, and serves them to every client that asks.

The defining structure is small:

```text
Package-manager ecosystem
├── client side: package manager / dependency tooling (not part of this Type)
└── server side: THE REGISTRY
    ├── Package Catalog (name → versions, under the ecosystem's name vocabulary)
    ├── Publication path (maintainers add packages/versions; name-ownership rules apply)
    └── Resolution path (ecosystem clients resolve and fetch by name + version)
```

Everything commonly associated with modern registries — web search and download statistics, two-factor authentication, signing and provenance, organization billing, upstream proxying — is standard or optional capability layered on this core, not what makes the venue a package registry. Registries from the earliest ecosystem era already had the three-part core.

When the center of gravity shifts from *serving a package-manager ecosystem* to *custody of an organization's build outputs across formats*, the product is drifting toward a different Application Type (Artifact Repository).

## Users & Context

Three participant roles interact with a registry, and their relationships are the context of everything the registry does:

- **Package maintainers (publishers)** — authors and teams who release their software into the catalog. They register accounts, claim or create package names, authenticate, and publish versions. Their permission to publish a given package is governed by the registry's name-ownership model.
- **Consumers (developers, builds, deployments)** — everyone who installs packages. They usually never create a registry account: their package-manager client is pointed at the registry (directly or through a configured source) and resolves packages anonymously or with a read credential.
- **Registry operators (venue side)** — the party running the venue: a company, a foundation, a platform vendor, or an organization running a private registry. On public venues they govern the namespace (disputes, typosquatting, malware moderation); on private venues they manage organizations, teams, access, and billing.

On **public venues**, the same individual is typically both roles at different times — a developer publishes their own packages by day and consumes thousands of others' packages by the same account. On **private venues**, the venue is an organizational capability: a team hosts its internal packages and grants read access to employees and build systems.

Typical context: publish happens from a maintainer's machine or, increasingly, from CI automation on the maintainer's behalf; consumption happens everywhere — developer machines, CI pipelines, deployment environments.

## Core Model

### The Defining Core

Three structures, held jointly. Remove any one and the venue stops being recognizable as a package registry:

- **The package catalog of record** — a persistent catalog of the ecosystem's packages, each identified by a name in the ecosystem's name vocabulary, organized as name → versions. Each package record carries the ecosystem's package semantics: version numbers, metadata (description, license, authors), and — critically — the dependency declarations that the packages themselves state. The catalog *defines the ecosystem's shared namespace*: it is the authoritative answer to "does this package name exist, and whose is it?" Without the catalog there is no venue — only a stream of uploads with no memory.
- **The publication path** — maintainers add new packages and new versions to the catalog through the registry's protocol, authenticated and subject to name-ownership and permission rules. Publishing is what makes the venue a living catalog rather than a mirror: a mirror copies what exists elsewhere; a registry is where new packages *enter the ecosystem*. Without it, the venue is a mirror.
- **The resolution path for the ecosystem's clients** — the ecosystem's package-manager clients treat the registry as a configured package source: they ask it for a package's available versions, receive the metadata, and fetch the package's distribution files by name + version. This is what makes the venue *the* registry of its ecosystem rather than a disconnected archive: the ecosystem's install commands resolve against it. Without it, the venue is a publication archive that nothing in the ecosystem actually consumes.

What binds all three together is the **ecosystem protocol**: catalog organization, publication, and resolution all speak the vocabulary of one package-manager ecosystem — its name rules, its version grammar, its metadata format, its client behavior. A venue that hosts files but speaks no package-manager protocol is generic file hosting; a venue that speaks several protocols serves several ecosystems at once (each getting its own catalog surface and endpoints).

### Standard Capabilities

Mature products commonly provide, on top of the core:

- **Package pages and discovery** — a rendered page per package (description, readme, metadata, version history, dependency list), search over the catalog, and commonly download statistics.
- **Ownership and permission model** — at least a two-level maintainer model (owners who control the package and its collaborator list, maintainers who can publish but not administer), extended on organization-oriented venues with teams, roles, and organization-scoped namespaces.
- **Publish authentication** — API tokens (often scope-limited), two-factor authentication, and first-class support for publishing from CI automation, including delegation mechanisms that let a CI service publish without holding a long-lived credential.
- **A version-immutability posture** — a published version is a *stable resolution target*: the same name + version keeps resolving to the same content. Public venues commonly forbid overwriting a published version or reusing a distribution filename, so that lockfiles and cached installs stay valid.
- **Soft-removal affordances** — ways to stop recommending or stop serving a version *without* pretending it never existed: deprecation notices, yanking (existing consumers keep working; new resolutions no longer pick it), archiving, or policy-gated unpublish. Hard deletion, where offered at all, is heavily constrained and commonly irreversible.
- **Programmatic access beyond the client protocol** — web APIs, feeds, webhooks, and audit events for automation and governance.
- **Hosting the distribution files themselves** — the venue stores the artifacts its catalog lists (the strongest observed posture across the researched sample; a metadata view that hosts no files is explicitly *not* the registry).
- **Private-venue machinery** — organization accounts, access control for consumption, storage metering, and integration hooks for the surrounding development platform and CI.

### One Structure, Many Implementations

The core is written conceptually; the researched products realize each structure differently, and a reader who has only met one realization should still recognize the others:

```text
Concept:            The catalog
Implementations:    public venue per ecosystem (npm registry, PyPI, crates.io);
                    per-ecosystem registries under one platform product
                    (GitHub Packages); one commercial account serving many
                    ecosystem protocols (Gemfury)

Concept:            Publication path
Implementations:    direct client commands (npm publish, twine upload,
                    cargo publish); web/dashboard upload; CLI and HTTP
                    upload endpoints; CI delegation (trusted publishing,
                    workflow tokens); git-push with server-side packaging

Concept:            Identity substrate
Implementations:    ecosystem-native accounts (npm, PyPI); platform
                    accounts (GitHub); federated login (crates.io via
                    an external developer-platform account)

Concept:            Resolution path
Implementations:    index protocols (git-based index, sparse HTTP index
                    documented as a registry-server protocol); per-format
                    client configuration (registry URL in the package
                    manager's config); account/repository URLs used as
                    an additional package source
```

## How It Works

### Establish identity and a claim on the namespace

```text
Create an account on the registry
→ verify identity (email / external developer account)
→ obtain publish credentials (API token; commonly with second-factor protection)
→ the account can now own package names
```

Name ownership is the entry ticket: on public venues, names are commonly allocated first-come-first-serve and thereafter owned — publishing a package under an unowned name *creates* the ownership; publishing under an owned name requires the owner's permission. Registries police the namespace with name rules (reserved names, confusability blocks) and dispute processes.

### Publish a package

```text
Build the package artifact per the ecosystem's packaging rules
→ authenticate to the registry (token / delegated CI identity)
→ upload: the artifact + its metadata (name, version, dependencies declared by the package)
→ the registry performs its own checks (format, name permission, size policy)
→ a new catalog entry appears: the package (or an existing package gains a version)
```

The registry is not a passive drop box: it validates the submission against its own rules before admitting it, and the publication is what *creates* or *extends* the catalog record. Automation is a first-class publisher on modern venues — CI pipelines publish releases directly, using scoped tokens or delegation mechanisms instead of personal credentials.

### Consume packages

```text
Point the package-manager client at the registry
  (the ecosystem's default, or a configured source: a private registry,
   an organization's account URL, a mirror)
→ client asks the registry: which versions exist for this package name?
→ client selects a version (selection logic lives on the client side)
→ client fetches the distribution file(s) for that name + version
→ integrity is checked against published hashes
```

The division of labor is strict and worth stating: **the registry serves; the client decides**. The registry answers "what exists" and "hand me this version"; the choice of *which* version to use — ranges, resolution, locking — belongs to the client tooling (Dependency Management territory). This is why the same registry serves every client generation and every resolution strategy its ecosystem invents.

### Manage the published record

```text
Maintainers add collaborators (extending publish permission)
→ broken release? soft-remove it: deprecate / yank / archive
   (existing consumers unaffected; new resolutions steered away)
→ sensitive release? removal is policy-gated and commonly irreversible
→ ownership changes: transfer the package, add/remove owners
```

Version history on mature venues is treated as part of the ecosystem's long-lived record — some public venues state an archive mission explicitly, positioning the catalog as a public good whose integrity outlives any single maintainer.

### Core vs Common vs Optional

**Defining core** — without these, not a package registry:

- package catalog of record under the ecosystem's name vocabulary
- publication path with name-ownership rules
- resolution path consumed by the ecosystem's package-manager clients
- binding to a package-manager ecosystem protocol

**Standard capabilities** — present in most mature products:

- package pages, search, statistics
- ownership/permission model beyond a single owner
- publish authentication (tokens, 2FA, CI delegation)
- version-immutability posture and soft-removal affordances
- web APIs / webhooks
- hosting the distribution files

**Optional / variant** — depends on venue posture and customer:

- public open self-service vs private organizational access (or both)
- single-ecosystem vs multi-format venue (several ecosystem protocols on one venue)
- review/curated publishing gates
- signing, provenance, malware quarantine
- upstream proxying of public sources, mirrors, organization billing

## Interfaces

### Package page

The public face of one catalog entry — the surface consumers see before installing.

- readme, metadata (license, authors, links), dependency list, version history, download statistics
- primary actions: view versions, copy the install command, inspect a version

### Search

Discovery over the catalog.

- keyword search with ecosystem-specific ranking (downloads, relevance, maintenance signals)
- primary action: reach a package page

### Publisher surfaces

What maintainers operate.

- account settings (credentials, tokens, two-factor)
- package management (collaborators, visibility, deprecation, yank/unpublish, ownership transfer)
- web/dashboard upload where offered; otherwise the CLI publish command against the registry endpoint

### Organization administration (private venues)

- member and team management, package access grants, storage/billing views
- primary actions: invite, grant/revoke access, audit

### Endpoints (protocol surfaces)

The registry's machine-facing interfaces, distinct from its web UI:

- the ecosystem's client protocol endpoints (publish + resolve, per format on multi-format venues)
- web APIs (query metadata, statistics), feeds (new releases), webhooks (package events)

## Important Rules / Behaviors

### The namespace is owned, not free

A package name is allocated under registry rules (first-come on public venues) and thereafter belongs to someone. Publish permission to a name is an authorization decision, enforced server-side on every publish. This makes the catalog simultaneously a directory and an access-control surface.

### A published version is a stable resolution target

Across the researched sample, published versions are not silently mutable: overwriting a version or reusing a distribution filename is forbidden or heavily constrained, because the whole ecosystem — lockfiles, mirrors, caches — assumes that name + version keeps meaning the same bytes. Consequences follow: mistakes are handled with *soft removal* (yank/deprecate/archive) that protects existing consumers, and true deletion is rare, policy-gated, and commonly permanent with the name potentially released or retained depending on the venue.

### The registry serves; the client decides

Version selection, range semantics, and locking are client-side concerns. The registry's contract is to expose the catalog truthfully and serve what is requested. Registries therefore stay compatible with all client tooling of their ecosystem, including third-party clients and update-automation bots.

### The venue speaks its ecosystem's language

A registry accepts only its ecosystem's packages (name rules, metadata format, dependency declarations). Because a package's dependency graph must stay resolvable within one namespace, at least the strictest public venues refuse packages that depend on packages from *other* registries; multi-format venues resolve the same constraint by operating one registry surface per ecosystem protocol.

### Public venues are trust surfaces

Because anyone can publish, mature public venues carry moderation machinery: name-confusability blocks against typosquatting, malware reporting and quarantine, security-advisory integration, and authentication requirements for publishers. These govern *admission to and continued presence in* the catalog — the registry's unique leverage point over the ecosystem's supply chain.

## Variants

- **Public ecosystem venue** — open self-service publishing; the ecosystem's default source; funded as infrastructure (company-backed, foundation-run, or project-run). Governance burden is the defining management problem.
- **Private organizational registry** — the same catalog/publish/resolve core operated inside one organization: internal packages under the ecosystem's own name vocabulary, access-controlled, commonly provided by a development platform or a commercial hosted service.
- **Platform-embedded registries** — package registries offered as a feature area of a source-hosting/DevOps platform, with permissions inherited from or linked to repositories and billing on the platform account.
- **Multi-format commercial venue** — one hosted product speaking many ecosystem protocols, so one account serves all of a team's package types; each ecosystem gets its own endpoint and configuration.
- **Curated-publishing venue** — publication passes a review/staging gate before entering the catalog (historically common in older ecosystems' central registries).
- **Mirrors** — not a registry variant but the ecosystem's replication mechanism: a mirror copies the catalog and serves it but has no publication path. Registries commonly document or bless mirroring for scale and availability.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Artifact Repository | adjacent, sharpest seam: custody of an organization's build outputs across formats, with repository topology and upstream proxy/aggregation as its differentiating layer; the package registry's center is the ecosystem venue (catalog + publish + resolve per ecosystem protocol). Public ecosystem registries are the prototype of this Type, not of Artifact Repository. Multi-format platform-embedded products genuinely straddle the two; classify by center of gravity |
| Dependency Management Application | the client side of the same flow: declares, resolves, and records which versions a project uses; the registry is one of its configured supply sources and never decides versions itself |
| Build Automation System | produces the artifacts; may carry a *publish command* in ecosystem-native tools, but it does not operate the venue the command talks to |
| Continuous Integration Platform | executes builds and archives run outputs for inspection; a registry is a standing catalog with publication rights, not a per-run output store |
| Source Code Hosting Platform | hosts source repositories; a registry hosts package artifacts. On platforms that offer both, they are separate feature areas with separate storage and permission surfaces |
| Model Registry | parallel registry concept for ML: its records carry ML governance semantics (metrics, approval status, lineage) rather than package coordinates and dependency metadata |
| Container / OCI Image Registry | distributes container images under the OCI distribution protocol rather than a package-manager ecosystem's package semantics; platforms commonly separate the two surfaces |
| Software Supply Chain Security / SCA | analyzes dependency sets and gatekeeps risk; the registry provides admission control, advisory data, and audit hooks but does not judge a project's dependency composition |

The boundary with **Artifact Repository** is the most important one, because products exist on both sides of it and the names are used loosely in the market. The working test: ask what the system's center of gravity is — *serving a package-manager ecosystem's publish/resolve flow under the ecosystem's own package semantics*, or *operating custody of an organization's outputs across many formats with repository governance*. The former is this Type; the latter is Artifact Repository; genuine straddlers are classified by which center dominates their design and documentation.

## Representative Products

- npm registry
- PyPI (Python Package Index)
- crates.io
- GitHub Packages
- Gemfury

The core model was checked against the lineage of older ecosystem registries (CPAN-era catalog + upload + mirror serving, curated central registries of the 2000s) so that the definition does not over-fit to the modern web-platform era: the defining core requires none of today's search, statistics, or authentication machinery.

## Sources

Research date: **2026-09-09**

- npm Docs — About the public npm registry: https://docs.npmjs.com/about-the-public-npm-registry (plus official documentation navigation)
- PyPI — Help / Common questions: https://pypi.org/help/
- The Cargo Book — Registries: https://doc.rust-lang.org/cargo/reference/registries.html ; Publishing on crates.io: https://doc.rust-lang.org/cargo/reference/publishing.html
- GitHub Packages documentation: https://docs.github.com/en/packages and Introduction to GitHub Packages: https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages
- Gemfury Dev Center: https://gemfury.com/help and Getting Started: https://gemfury.com/help/getting-started

> Sourcing limitation: the crates.io policy page was not reachable from the research environment (JavaScript-gated); crates.io behavior is evidenced through the official Cargo Book documentation instead. Deeper npm policy articles (unpublish policy, scope rules) were observed at navigation level only. Precise operational figures (size limits, time windows, quota defaults) observed in official docs are deliberately not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, boundary adjudications with neighboring Types, and the historical breadth check are recorded in the paired Research Notes.
