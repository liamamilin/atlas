# Feature Flag Management Platform

## Overview

A **Feature Flag Management Platform** is an engineering-side release-control system that holds a software product's feature flags as managed records, lets the team change flag state while the software is running, and integrates runtime evaluation into the application so that features can be enabled, targeted, or disabled **without redeploying the software**.

The defining core is small:

```text
Feature Flag Registry of Record
└── Runtime-mutable state (changes reach running software without a new deployment)
    └── Runtime evaluation integrated into the application
        └── The application branches its behavior on the resolved flag value
```

The problem it exists to solve is the coupling between *deploying code* and *releasing features*. With flags, new code ships inside a normal deployment but stays dark; exposure is then controlled from the platform — to internal users, to a percentage of users, to named audiences — and a faulty feature can be switched off in seconds instead of rolled back by redeployment. Everything else commonly associated with the category — environments, targeting rules, segments, percentage rollouts, multivariate values, dashboards, experimentation — is mature structure layered on that core, not what makes the Type.

## Users & Context

Primary users are members of the engineering organization that owns the software:

- **Software engineers** create flags, give them meaning (description, key, values), and instrument the application to evaluate them — the flag is worthless until code branches on it.
- **Release and product managers** drive rollout decisions: who sees a feature, in which order, at what pace; they work through targeting rules and rollout percentages rather than through code.
- **Operations / SRE** use flags as kill switches — an instant, deploy-independent way to disable a misbehaving feature in production.
- **Platform / team administrators** govern the estate: environments, permissions, change approvals, integrations.

The typical working context is a software team practicing progressive delivery: continuous integration and delivery pipelines deploy code frequently, and the flag platform decouples "the code is in production" from "users can see the feature". The same infrastructure serves longer-lived uses — entitlements (features enabled per customer plan), kill switches, and configuration values delivered to applications.

## Core Model

### The Defining Core

**Feature flag (registry of record).** A flag is a persistent, individually named toggle — a managed record in the platform, not a line in a config file. It carries an identity (a unique **key**, which the application code references), human context (what it controls, who owns it), and a configurable current state. The platform, not the application's repository, is the place of record for what is on, off, or partly on.

**Runtime-mutable state.** Changing a flag's state in the platform's management surface changes the behavior of already-running software. No build, no release, no deployment step sits between the decision and the effect. This is the property that makes the platform a release-control instrument rather than configuration storage.

**Runtime evaluation in the application.** The running application resolves flag values at runtime through an SDK or API integration bound to the platform by credentials, and branches its behavior on the result (`if flag enabled → new behavior else old behavior`). The application is the consumer of decisions; the platform is the decision point of record. How the SDK stays current with the platform (polling, streaming, local evaluation, downloadable snapshots) is an implementation choice that varies by product.

Remove any leg and the Type collapses:

- No registry → toggles scattered in code or config files; nothing to manage.
- No runtime mutability → build-time configuration; releases still require deployment.
- No in-application evaluation → a dashboard over configuration with nothing acting on it.

### What Mature Products Add

The working layer that current products carry — expected in the market, but not the definition:

- **Environments** — the flag's state is configured separately per deployment context (development, staging, production), so a feature can be on in development and dark in production. Applications connect with credentials bound to a specific environment, which decides which configuration they see.
- **Caller context** — evaluations carry a description of the caller (an identified user, an account, a session) with attributes such as email, plan, region, or device. Without context, only environment-wide on/off is possible.
- **Targeting rules** — conditions on caller attributes that decide, per evaluation, which behavior the caller receives.
- **Segments / audiences** — named, reusable collections of users or conditions that flags reference, so the same audience can drive many flags and be maintained in one place.
- **Percentage rollout** — gradual exposure: the flag serves the new behavior to a percentage of callers, raised stepwise to 100%. Where mechanics are documented, the platform computes a caller's bucket consistently so the same user does not flip in and out as the percentage changes.
- **Multivariate values** — beyond on/off: named variations with payloads (strings, numbers, JSON) or weighted variants, letting one flag select *which version* of a feature a caller gets.
- **Kill switch posture** — an instant path from "on for everyone" to "off for everyone"; the strongest realizations make kill/restore an explicit, first-class operation on the flag.
- **Change governance** — recorded change history, required comments on saves, approval (change-request) flows for sensitive changes, scheduled changes.
- **Organization and metadata** — containers above flags (projects/products) with role-based access; descriptions, owners, tags, key conventions.

### One Structure, Many Implementations

The core is conceptual; realizations differ across products and eras:

```text
Concept:          Flag as managed record
Implementations:  named flags with permanent keys (SaaS platforms);
                  flags in self-hosted instances; typed "settings"
                  where a flag is the boolean subtype of a general setting

Concept:          Per-context configuration separation
Implementations:  environments per project; configuration objects;
                  environment-bound SDK credentials or API keys

Concept:          Caller context
Implementations:  user/account identity kinds with attributes; identity
                  plus traits; extensible context fields

Concept:          Value of a flag
Implementations:  boolean on/off; typed values (string/number/JSON);
                  weighted named variants with payloads; "treatments"

Concept:          Consistent exposure buckets
Implementations:  hashing identity + flag/segment identifiers into a
                  stable assignment; seeded buckets that can be reseeded
                  deliberately
```

A reader who has only seen one shape — a cloud SaaS dashboard — should still recognize a self-hosted, boolean-only instance as the same Type from the defining core.

## How It Works

The Type runs as two loops: a **management loop** operated by people, and an **evaluation loop** executed inside the application.

### Management loop — the life of a release flag

```text
Create the flag
  → name, permanent key, description, value type (boolean or variants)
→ Instrument the code
  → SDK added to the application; code branches on the flag's value
→ Configure per environment
  → enabled in development, disabled (dark) in production
→ Deploy the code
  → the feature ships to production hidden behind the flag
→ Roll out progressively
  → enable for internal/beta users, then a percentage, then everyone —
    by raising rollout settings, not by deploying
→ Hold or kill
  → if the feature misbehaves, switch it off for everyone in one action
→ Retire
  → remove the flag from the code, deploy, then remove it from the
    platform; long-lived flags (kill switches, plan-gated features)
    stay and are maintained
```

### Evaluation loop — what happens in the application

```text
Application receives a request / user session
→ SDK supplied with caller context (identity, attributes)
→ SDK resolves the flag against the current configuration
   (locally cached / streamed / fetched, depending on the product)
→ Application branches on the resolved value or variant
→ If the platform cannot be reached, the application falls back to a
   declared safe default for the flag
```

The evaluation loop is what makes the platform's decisions real: every page render, API call, or app session consults the flag layer, and the same flag can serve different behavior to different callers in the same running version.

### Capability tiers

**Defining core** — flag registry of record; runtime-mutable state; in-application runtime evaluation.

**Standard capabilities** — environments; caller context and targeting rules; segments; percentage rollout with consistent bucketing; multivariate values; kill switch; change history and governance; containers, roles, and flag metadata; management API/CLI alongside the UI.

**Common variants / optional** — native experimentation (metrics and A/B tests on flags) or experimentation by exporting exposures to external analytics; rollout automation (health metrics that advance or pause a staged rollout); release templates and pipelines; flag-hygiene tooling (stale-flag detection, zombie-flag reports, code-reference scanning); edge/proxy delivery topologies; self-hosted or data-governance deployment modes.

## Interfaces

### Flags list

The registry view and the primary entry surface.

- lists every flag in the project/container with current state per environment
- primary actions: create flag, search/filter, open a flag, archive/delete

### Flag detail / targeting

The working surface for a single flag.

- key, description, values/variations, per-environment state
- targeting rules, segments, rollout percentage, prerequisites, metadata
- primary actions: toggle per environment, edit rules, adjust rollout, save with comment / request approval

### Environments and containers

- environment list with per-environment SDK credentials; project/product organization
- primary actions: create/rename, manage credentials, assign roles

### Segments / audiences

- reusable audience definitions (user lists or attribute conditions)
- primary actions: create segment, define rules, attach to flags, maintain membership

### Change history / activity

- who changed what, when, and (where required) with which approved comment
- change requests and their approval states in products with approval flows

### Code-side surfaces

- **SDK integration** — the surface engineers work in: initialize with environment credentials, pass context, evaluate flags/variants
- **Management API / CLI / infrastructure-as-code** — create and configure flags programmatically; parity with the dashboard
- **Code-reference scanning** (in some products) — finds where a flag key appears in the repository, supporting cleanup

## Important Rules / Behaviors

### The flag key is the contract with the code

The key is what application code references. Mature products treat it as immutable once created, or strongly discourage changing it — renaming a flag silently breaks the branches written against it. Names and descriptions remain editable.

### Flag configuration is per-environment

The same flag exists in every environment of its container, but its state, rules, and values are configured independently per environment. Turning a flag on in staging says nothing about production.

### Targeting evaluates against caller context

Attribute rules and percentage rollouts resolve per evaluation, using the context the application passes. Percentage exposure applies to *identified* callers: an evaluation without a caller context cannot fall into a user percentage split. Some products make client-side/mobile availability an explicit per-flag decision, because exposing flag configuration to untrusted clients has security implications.

### Exposure is consistent for a given caller

Where percentage rollout is implemented, a caller's assignment is computed consistently (from stable identifiers), so raising the rollout percentage only ever adds callers who were next in line — the same user does not randomly flip between old and new behavior as the percentage changes. Reseeding or changing the assignment basis is an explicit, exceptional operation in the products that support it.

### There is a defined safe answer when the platform is unreachable

Applications declare fallback/default values per flag, and products define what an evaluation returns when a flag is not configured or the platform cannot be consulted (a declared default; in some products, a reserved "control" value). Defensive use of flags — assuming the safe path — is part of the practice, because evaluation failures must degrade to the old behavior, not to an error.

### Flags accumulate debt; lifecycle discipline is part of the job

Release flags are temporary by design: once fully rolled out, they should be removed from code and from the registry. Because teams ship many flags, mature products provide lifecycle support — marking flags temporary vs permanent, detecting stale flags that nobody has touched, listing flags no longer referenced in code, and archiving instead of hard-deleting. Kill switches and plan-gating flags are the deliberate exceptions: they are long-lived.

### Changes are governed

Because a single toggle can change production behavior instantly, platforms record who changed what and when; some require a comment with each save; sensitive environments or flags can require an approved change request; changes can be scheduled for a release moment. Role-based permissions separate who may view, toggle, approve, and administer.

## Variants

- **SaaS commercial platforms** — hosted control plane, per-seat or usage pricing, the dominant enterprise shape.
- **Open-source / self-hosted** — the platform runs inside the customer's infrastructure; the OSS pole often carries the same core (projects, environments, strategies) with commercial tiers adding governance and scale.
- **Cloud-provider-embedded flag services** — toggles delivered as part of a cloud configuration service; the flag core appears as one capability inside a broader configuration product.
- **Server-side-first vs client/mobile-inclusive** — products differ in how flags reach browsers and mobile apps (explicit opt-in, public credentials, SDK type differences).
- **Experimentation-native vs experimentation-by-integration** — some platforms carry metrics and A/B testing as a product layer; others push flag exposures to external analytics tools.
- **Release-machinery depth** — from manual percentage increases to templated rollout plans with automated health-based advancement and pausing.
- **Remote-config-leaning products** — platforms that present themselves equally as feature flags and remote configuration, delivering arbitrary values to client apps; the feature-control core remains recognizable.

## Related Application Types

| Application Type | Distinction |
|---|---|
| A/B Testing Platform | measurement is the point: assign variants, collect metrics, analyze causal impact; a flag platform's point is controlling running software — measurement is optional and sometimes delegated to external analytics |
| Digital Experimentation Platform | broader experimentation lifecycle (hypotheses, metrics, holdouts) riding on assignment machinery; flag control is one input to it |
| Continuous Delivery Platform | unit of work is the versioned deliverable promoted through environments; the flag platform changes the behavioral state of an already-deployed version — they interlock but neither contains the other |
| Application Deployment Management | manages the act of getting software onto infrastructure; flags change behavior without any deployment |
| Release Management Platform | organizes the release process (scope, approval, scheduling of releases); flag platforms execute one release-control mechanism within it |
| Configuration Management (IT) | manages infrastructure/server configuration state; flag platforms manage feature availability of application behavior for a different user population |
| Business Rules Management System | executes authored business-rule sets as decision logic; a flag resolves one named availability decision consumed by application code |
| Remote configuration services (mobile/cloud-native) | deliver configuration values to client application populations, with feature gating as one use; the flag platform's center is release control over a software product — a genuinely overlapping family, separated by orientation |

The boundary with experimentation is the most important one: both decide "who sees what", but the flag platform's deliverable is *controlled software behavior* (registry, evaluation, kill switch, rollout), while the experimentation platform's deliverable is *a measured comparison* (assignment plus metric collection and analysis). When measurement and analysis become the center, the product has crossed into the experimentation Types.

## Representative Products

- **LaunchDarkly** — commercial category leader; the enterprise SaaS shape with the fullest governance surface.
- **Unleash** — open-source-first platform; the self-hosted pole with an extensible strategy model.
- **Flagsmith** — open-core platform (SaaS and self-hostable); documents the segment/percentage mechanics openly.
- **ConfigCat** — simplicity-oriented SaaS for smaller teams; typed settings model.
- **Split (Harness Feature Management & Experimentation)** — experimentation-led enterprise platform; explicit kill/restore and treatment/bucket semantics.

## Sources

Research date: **2026-09-08**

Primary official documentation:

- Unleash — Core concepts: https://docs.getunleash.io/concepts
- Flagsmith — What are Feature Flags: https://docs.flagsmith.com/getting-started/feature-flags
- Flagsmith — Feature Flags Lifecycles: https://docs.flagsmith.com/best-practices/flag-lifecycle
- Flagsmith — Rollout by Percentage: https://docs.flagsmith.com/managing-flags/rollout/rollout-by-percentage
- LaunchDarkly — Get started: https://launchdarkly.com/docs/home/getting-started.md
- LaunchDarkly — Creating new flags: https://launchdarkly.com/docs/home/flags/new.md
- ConfigCat — Docs index and Main Concepts: https://configcat.com/docs/ , https://configcat.com/docs/main-concepts/
- Split (Harness FME) — Documentation index and Feature flag definition reference: https://docs.split.io/llms.txt , https://docs.split.io/reference/feature-flag-definition.md

> Sourcing limitation: platform-native remote-configuration services could not be reached during research (fetch timeouts on 2026-09-08); the distinction from that family is drawn from the flag platforms' own self-description and is stated without claims about any specific remote-config product. Percentage-rollout internals are described only where directly documented; product-specific mechanics are kept out of this document.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical-sample check are recorded in the paired Research Notes.
