# Artifact Repository

## Overview

An **Artifact Repository** is an organization-operated store for built software artifacts. It holds published binaries, packages, container images, and other build outputs as persistent records inside named repositories, gives producers (build systems and maintainers) a path to publish artifacts under a stable identity, and serves those artifacts back to consumers — developer tooling, other builds, deployments — by stable coordinates.

The problem it solves is durable custody of build output: a build produces files once, but many parties need to retrieve exactly those files for years afterward. Public package registries host community packages but not an organization's first-party artifacts; ad-hoc file shares have no coordinate model, no client integration, and no access control. The artifact repository is the system of record that sits between the build system and everyone who consumes what the build produces.

The defining structure is deliberately small: named repositories holding published artifacts, a publish path, a coordinate-based retrieval path, and persistence over time. Everything else commonly associated with the category — multi-format support, proxying of public registries, aggregated repository views, promotion machinery, security integrations — is standard equipment of mature products rather than what makes the product this Type.

## Users & Context

Primary users:

- **Developers**: consume dependencies from the repository through their package managers, and publish packages or binaries they maintain. They rarely see the repository itself; they see configuration that points their tools at it.
- **CI/CD pipelines**: the highest-volume producer and consumer. A pipeline publishes the artifacts it builds and resolves the dependencies it needs from the same repository system, typically with machine credentials.

Secondary users:

- **Release or build engineers**: define the repository layout (which repositories exist, what flows between them), manage promotion of validated artifacts, and set retention rules.
- **Platform / DevOps administrators**: configure repositories, upstream sources, permissions, authentication, and storage; watch storage growth.

The context is the software delivery pipeline: after code is built and before it is deployed, its output must live somewhere controlled. Teams treat the artifact repository as the boundary between "what the build produced" and "what anyone is allowed to consume".

## Core Model

### The Defining Core

```text
Producer (maintainer or build system)
  ↓ publish
Repository (named container, organized by format and purpose)
  └── Package (a named identity within its format)
        └── Version (a specific release of that identity)
              └── Files (checksum-identified) + format metadata
  ↓ resolve by coordinates
Consumer (developer tooling, other builds, deployment)
```

Four properties. Remove any one and the product is no longer an artifact repository:

- **Repositories as named containers.** Artifacts are stored inside named repositories — typically one repository per package format and per purpose (for example, separating in-progress from released output). The repository is the unit of organization, permission, and policy.
- **Publish path.** Producers place artifacts into the system under a stable identity. The identity follows the conventions of the artifact's format: a package name, a version, and — depending on format — a namespace or scope. Files are stored with checksums, which is how the system guarantees that what is retrieved is bit-for-bit what was published.
- **Resolve path.** Consumers retrieve artifacts by those coordinates. The modern form of this path is a set of endpoints that speak the native protocols of package-manager clients: a build tool or package manager is pointed at the repository URL and then works as if it were talking to the format's public registry.
- **Persistent retention.** A published artifact remains available after publication — through subsequent builds, renames, and reorganizations. The repository is a record, not a transient cache of one session.

### Structure Around the Core

Mature products surround this core with a recognizable set of standard capabilities:

- **Multi-format support.** One system hosts repositories for many package formats — language package formats (Maven, npm, PyPI, NuGet, Cargo, RubyGems, Conan, Swift, Go, and so on), container image formats (Docker/OCI), and operating-system package formats, plus a generic channel for arbitrary files that belong to no package manager. The count and mix vary widely by product.
- **Upstream sources.** A repository can proxy and cache an external registry — usually the format's public registry — so that third-party dependencies are fetched through the organization's own system, cached locally, and remain available even if the upstream is slow, changed, or unreachable. Names differ (remote repository, proxy repository, upstream source, dependency proxy), but the mechanism is the same shape across the category.
- **Aggregated resolution.** Several repositories can be merged into one endpoint, so a consumer resolves against a single URL that transparently covers first-party artifacts, cached third-party artifacts, and artifacts from other internal teams. The aggregation order determines which repository wins when the same coordinates exist in more than one place.
- **Client configuration.** Because every package manager has its own configuration format, products provide generated setup instructions or snippets so each developer's tools point at the right endpoints with the right credentials.
- **Access control.** Permissions attach to repositories (read/consume vs publish vs administer). Anonymous read-only consumption is a common posture for internal networks; publishing almost always requires credentials — a user token, a machine identity, or a CI-issued job credential.
- **Provenance records.** When a build publishes an artifact, the system commonly records where it came from — which pipeline, which commit, which trigger — so consumers can trace an artifact back to the build that produced it.
- **Retention and storage governance.** Artifacts accumulate; products provide deletion with recovery windows, cleanup rules that remove stale versions, and storage monitoring.
- **Browsing and search.** A web interface over the repository tree: browse by repository, search by name or checksum, inspect a package's versions, files, metadata, and provenance.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:            named repository container
Implementations:    per-format repositories, format-permissive feeds, project- or group-scoped registries

Concept:            artifact identity
Implementations:    package name + version; component + asset; package + version + revision; namespace/scope variants

Concept:            upstream source
Implementations:    remote repository, proxy repository, upstream source, dependency proxy

Concept:            aggregated resolution
Implementations:    virtual repository, group repository, feed with upstream chain, repository upstream links

Concept:            consumer subset ("what is safe to use")
Implementations:    read-only views, staging suites, signed release bundles, package protection/origin rules
```

## How It Works

### Set up the repository landscape

```text
Administrator creates repositories
→ chooses format, storage backend, and access rules per repository
→ optionally attaches upstream sources (public registries or other internal repositories)
→ optionally assembles repositories into an aggregated endpoint for consumers
```

A common layout separates work-in-progress from published output — for example, distinct repositories for development versions and released versions, or a default landing area plus curated views — so that consumers can be pointed at "the things we stand behind" rather than "everything that was ever built".

### Connect producers and consumers

```text
Developer or pipeline gets credentials (token / job identity)
→ package manager or build tool is pointed at the repository endpoint
→ the system provides per-format configuration snippets to make this mechanical
```

From this point on, the repository is invisible in the happy path: `npm install`, `mvn`, `pip`, `docker pull`, and their peers behave normally — they just resolve against the organization's repositories instead of (or in front of) the public registries.

### Publish

```text
A maintainer publishes from a workstation, or a CI job publishes after a successful build
→ artifact lands in the target repository under its format's coordinates
→ the system records the content (checksums) and, commonly, the provenance (pipeline, commit, trigger)
```

Publishing is gated: write access to the target repository is the permission that matters, and some organizations add protection rules so that only designated pipelines or roles may publish to release-designated places.

### Resolve

```text
Consumer requests coordinates (directly or through its package manager)
→ the system serves the artifact from local storage
→ if the artifact exists only upstream, the system fetches, caches, and serves it
→ artifacts are identified by their checksums end to end
```

Aggregated endpoints make this step span multiple repositories in a defined order, which is how a single configuration serves both first-party and third-party dependencies.

### Govern over time

```text
Validated artifacts are promoted to consumer-facing views or repositories
→ stale versions are cleaned up under retention rules
→ deletions are recoverable within a defined window
→ publish and delete events are recorded for audit
```

### Capability tiers

**Defining core** — without these, not an artifact repository:

- named repositories holding published artifacts
- publish path under stable coordinates
- coordinate-based resolve path
- persistent retention

**Standard equipment of mature products:**

- multi-format support and package-manager protocol endpoints
- upstream proxying/caching of external registries
- aggregated resolution endpoints
- client configuration machinery
- per-repository access control with anonymous-read option
- web browse/search and REST API
- CI publish integration with provenance
- deletion/recovery, retention rules, storage monitoring

**Optional or variant, depending on product and organization:**

- promotion machinery (views, staging, signed release bundles)
- package protection rules / origin controls
- security scanning (usually delivered by a companion product or platform feature rather than the repository itself)
- multi-site replication, edge distribution, high-availability topologies
- public-facing hosting of packages for outsiders
- symbol servers and other artifact-adjacent services

## Interfaces

The category's most important "interface" is invisible: package-manager-native endpoints. Producers and consumers mostly interact through their existing tools. The product's own surfaces are:

### Repository browser (web)

- Purpose: inspect what the system holds.
- Typical information: repository tree, packages and versions, files with checksums, metadata, provenance (originating build/commit where recorded), size and age.
- Primary actions: search, inspect, download an artifact directly, copy client-configuration snippets, delete (where permitted).

### Client configuration surface

- Purpose: connect a package manager or build tool.
- Typical information: per-format endpoint URLs, credential setup, ready-to-paste configuration snippets.
- Primary actions: generate or copy configuration; authenticate.

### Administration console

- Purpose: run the repository landscape.
- Typical information: repositories and their types/settings, upstream sources, users/roles/tokens, storage usage, cleanup policies, system health.
- Primary actions: create/edit repositories, attach upstreams, manage permissions and tokens, configure retention and cleanup, monitor storage.

### API / automation surface

- Purpose: let pipelines and scripts do everything the UI does.
- Typical information: repositories, components/packages, search results, permission objects.
- Primary actions: upload/download, query, configure, trigger cleanup.

### CI integration points

- Purpose: make the pipeline a first-class producer and consumer.
- Typical information: build/publish provenance, credentials scoped to the job.
- Primary actions: publish artifacts during the build, resolve dependencies from the repository.

## Important Rules / Behaviors

### Publish and consume are different permissions

Reading (resolving) artifacts and publishing them are separately controlled. Internal read-only access — including fully anonymous consumption inside a trusted network — is a common posture; publishing requires explicit credentials, and organizations commonly restrict who may publish to release-designated repositories or views.

### What happens when the same coordinates are published again is format- and product-dependent

Some formats treat a published version as immutable and reject re-publication; other combinations accept an update (creating a new revision of that version) or overwrite. Mature organizations therefore treat "republish the same version" as a discipline question — build pipelines aim to publish each version exactly once — but the enforcing rule itself varies and should be checked per format and product rather than assumed.

### Proxied artifacts become local records

When a repository proxies an upstream registry, artifacts pulled through it are typically retained by the organization's own system. Consumers then depend on the repository, not the public registry: even if the upstream removes or changes a version, the cached copy remains what the organization resolves. This is one of the main reasons teams route third-party dependencies through the repository at all.

### Resolution order matters in aggregated endpoints

When multiple repositories are merged into one resolve endpoint, the configured order decides which repository satisfies a request when the same coordinates exist in more than one. Misconfigured order can shadow internal artifacts with (or expose internal names to) upstream content, so order is treated as configuration with security consequences.

### Promotion separates "built" from "endorsed"

In products with promotion machinery, publishing lands in a default or staging area that general consumers do not treat as production-ready; a deliberate act — moving the artifact into a release view, approving a staging promotion, or publishing a signed bundle — exposes it to the "ready to use" audience. The mechanisms differ widely; the built-vs-endorsed distinction is the pattern.

### Storage is governed, not just used

Because artifacts accumulate indefinitely, mature deployments run cleanup rules (remove versions unused for a period, keep only the last N builds where the product supports it) and monitor storage. Deletion is commonly recoverable for a limited window, reflecting the record-keeping role of the system.

### Audit trails cover the dangerous actions

Publication and deletion are the actions organizations audit. Some products expose audit events or logs for these; others integrate with the surrounding platform's audit machinery.

## Variants

- **Standalone repository managers** — self-hosted or SaaS products whose whole job is this Type; the historical and market center of the category, ranging from free community editions to enterprise deployments with high-availability and multi-site topologies.
- **Platform-embedded registries** — the registry shipped as a feature of a source-code hosting or DevOps platform, scoped to the platform's projects/groups, tightly coupled to its CI and permission model.
- **Suite feeds** — a package-feed capability inside a broader ALM/developer suite, often organized around "feeds" (multi-format containers) with views for promotion rather than many single-format repositories.
- **Cloud-provider managed services** — fully managed repositories offered by a cloud platform, integrated with the platform's identity and access system and organized around org-level containers.
- **Format-scoped deployments** — a repository serving a single format (a private Maven repository, a Docker registry) still fits the Type; universal multi-format support is common, not required.
- **Public-facing deployments** — some deployments serve packages to outside parties; the dominant posture is internal/first-party custody.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Package Registry | closest sibling | centers on publishing and consuming packages of a package-manager ecosystem (often one ecosystem, frequently public or platform-embedded); the artifact repository centers on the organization's custody of build outputs across formats, with repository topology, upstream proxying, and pipeline governance. The boundary deserves joint review where platform-embedded products sit on both sides |
| Continuous Integration Platform | upstream producer | executes builds; the artifact repository stores and serves what builds produce. Transient pipeline-internal outputs (intermediate artifacts passed between pipeline stages) are not this Type's custody |
| Dependency Management Application | downstream counterpart | manages dependency declarations and version selection inside projects (lockfiles, upgrades); the artifact repository is the supply side that satisfies those declarations. One decides "which version do we use"; the other stores and serves "the artifact itself" |
| Source Code Hosting Platform | suite sibling | hosts source under version control; the artifact repository hosts built output. Both appear in developer platforms as separate features with separate storage and access rules |
| Model Registry | parallel registry | catalogs ML model versions with lifecycle governance (stages, approvals); an artifact repository may store model files as artifacts but does not run the model lifecycle. Boundary to be confirmed when the Model Registry leaf is documented |
| Software Composition Analysis / Software Supply Chain Security | governance neighbor | scans and gates artifacts for risk; the repository is the custody and supply layer, typically integrating with scanning rather than performing it |
| Generic object storage | distant | holds files but has no package-coordinate model, no package-manager protocol endpoints, no per-format metadata or version semantics |

## Representative Products

- JFrog Artifactory — universal repository manager (self-hosted and SaaS)
- Sonatype Nexus Repository — repository manager with community and commercial editions
- GitLab Package Registry — registry embedded in a DevOps platform
- Azure Artifacts — feed-based package service in an ALM suite
- AWS CodeArtifact — fully managed cloud provider service

The defining core was checked against these five across different packaging philosophies (standalone manager, platform-embedded, suite feed, cloud-managed) and against the historical form of the category (early single-format repository managers) to avoid defining the Type by any one era or deployment style.

## Sources

Research date: **2026-09-06**

- GitLab — Package registry documentation: https://docs.gitlab.com/user/packages/package_registry/
- AWS — CodeArtifact concepts: https://docs.aws.amazon.com/codeartifact/latest/ug/codeartifact-concepts.html
- JFrog — Artifactory documentation (artifacts & packages; repository management): https://docs.jfrog.com/artifactory/docs/understanding-artifacts-and-packages , https://docs.jfrog.com/artifactory/docs/repository-management
- Microsoft — Azure Artifacts documentation (overview; feeds; feed views): https://learn.microsoft.com/en-us/azure/devops/artifacts/start-using-azure-artifacts , https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/feeds , https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/views
- Sonatype — Nexus Repository help center navigation: https://help.sonatype.com/repomanager3/

> Sourcing limitation: deep content pages of the Sonatype Nexus Repository help center were not reachable during research (repeated 404s; only the official help-site navigation was accessible). Nexus-specific observations rest on that navigation structure and are stated conservatively; no Nexus-specific operational details are asserted. Precise product parameters (numeric limits, default quotas, exact retention windows, product-specific view names) observed for individual products were deliberately not carried into this document.
