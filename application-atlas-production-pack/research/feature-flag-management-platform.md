# Research Notes — Feature Flag Management Platform

Research date: 2026-09-08
Methodology: v1.1 (update-v1/)

---

## Research Goal

Understand what a Feature Flag Management Platform actually is as an Application Type: the objects it manages, the mechanism by which it affects running software, the work its users perform around releases, and where its boundary lies against experimentation platforms, continuous-delivery tools, remote-config services, and plain application configuration.

## Initial Boundary

Initial hypothesis before research:

- Core purpose: control which features of a piece of software are enabled, for whom, and when — at runtime, without redeploying the software ("decouple deployment from release").
- Likely core objects: flag (named toggle), environment, targeting rule / segment, variation/variant, SDK evaluation context.
- Likely users: software engineers (instrument + create), release/product managers (rollout decisions), ops/SRE (kill switches), platform admins (governance).
- Nearest neighbors: A/B Testing Platform / Digital Experimentation Platform (§06), Continuous Delivery Platform (§12), Application Deployment Management (§14), Configuration Management (§14), plus platform-native remote-config services (Firebase Remote Config class).
- Unknowns: whether "platform" (central service + SDK) is definitional or whether library+admin-UI tools qualify; how far experimentation belongs; how the mobile remote-config shape relates.

## Research Questions

1. What is the flag as an object? (name/key, types, variations, defaults, metadata, owner)
2. How does flag state reach running software? (SDK evaluation, streaming/polling/download, caching, offline behavior)
3. How does targeting work? (identity/context attributes, rules, segments, percentage rollout, bucketing consistency)
4. What role do environments play? (per-environment flag configuration, projects/containers, SDK credentials per environment)
5. What is the flag lifecycle? (create → instrument → rollout → full enable → cleanup/archive; flag debt management)
6. What governance and safety machinery matters? (audit/comment, change requests/approvals, scheduled changes, kill switches, RBAC)
7. Where does experimentation begin and where does the flag Type end? (metrics, A/B on flags, integration vs native)
8. What deployment/packaging variants exist? (SaaS vs self-hosted OSS vs cloud-provider-embedded; server vs client/mobile evaluation; edge/proxy)

## Representative Products

| Product | Position in market | Why selected |
|---|---|---|
| LaunchDarkly | Commercial category leader, enterprise | Richest doc surface; defines much of the market vocabulary |
| Unleash | Open-source-first, self-hosted pole | Non-SaaS philosophy; strategy/constraint model |
| Flagsmith | Open-core, SaaS + self-hostable, mid-market | Explicit feature-flag education docs; segment/percentage mechanics |
| ConfigCat | SMB / simplicity-oriented SaaS | Typed "settings" model; smallest-product pole |
| Split (Harness FME) | Enterprise experimentation-led | Flag-vs-definition split, treatments/buckets, kill API, change requests |

Boundary anchor (unreachable): Firebase Remote Config (mobile platform-native remote config). WebFetch timed out twice; recorded as source-access limitation — no operational claims made about it.

## Sources

Tier 1 — official operational documentation (all fetched 2026-09-08):

- Unleash — Core concepts: https://docs.getunleash.io/concepts
- Flagsmith — What are Feature Flags: https://docs.flagsmith.com/getting-started/feature-flags
- Flagsmith — Feature Flags Lifecycles: https://docs.flagsmith.com/best-practices/flag-lifecycle
- Flagsmith — Rollout by Percentage: https://docs.flagsmith.com/managing-flags/rollout/rollout-by-percentage
- LaunchDarkly — Get started: https://launchdarkly.com/docs/home/getting-started.md
- LaunchDarkly — Creating new flags: https://launchdarkly.com/docs/home/flags/new.md
- ConfigCat — Docs index: https://configcat.com/docs/ ; Main Concepts: https://configcat.com/docs/main-concepts/
- Split — docs root + llms.txt index: https://docs.split.io/ , https://docs.split.io/llms.txt
- Split — Feature flag definition reference: https://docs.split.io/reference/feature-flag-definition.md

Source-access limitations:

- Firebase Remote Config: https://firebase.google.com/docs/remote-config and /get-started timed out twice (2026-09-08). Used only as an unnamed-adjacent market shape in boundary reasoning; no claims about its specifics.
- Harness Developer Hub (Split's FME concept pages): overview URL not found; evidence for Split taken from docs.split.io API reference, which is official and definitional (object schemas, kill/restore semantics), but concept-narrative pages were not reached.
- LaunchDarkly concept pages beyond the fetched two were not needed; percentage-rollout mechanics for LaunchDarkly were NOT directly observed (avoid precise claims).

---

## Product A — LaunchDarkly (Layer A observations unless noted)

### Key observations

- Definition given by vendor docs: "a feature flag is a small piece of code used in software development to enable or disable a feature without modifying your source code or redeploying your app"; progressive rollout across subsets of users; one-click toggle in the UI.
- Management surface: **Flags list** per project; "Create flag" dialog: name, auto-generated **key** (permanent — cannot be modified after save), description (Markdown), flag **templates** (Custom, Release, Kill switch, Experiment, 2/4/6-stage migration), **variations** (boolean, string, number, JSON; multiple variations for multivariate; JSON-schema validation), **default on / default off** variations, **maintainer**, **tags**, **views**, availability to client-side/mobile SDKs (opt-in), **temporary vs permanent**, **prerequisites** (flag dependencies).
- Environment model: project contains environments; every flag exists in every environment of the project; **targeting configuration is per environment**; edits in one environment do not affect others; "Review and save" flow with an optional **comment** on each change.
- Evaluation integration: SDKs per language; server-side SDKs **evaluate flags locally** (do not network per call); client-side SDKs fetch; SDK credentials bound to environment (SDK key / mobile key / client-side ID); the app passes a **context** (kind, key, attributes — email, org, device, anything) with each evaluation; code calls `variation(key, context, fallback)` and branches on the result; fallback value used when the flag can't be evaluated.
- Targeting: targeting rules per environment on context attributes; per-context-kind rules (example: `beta-user` kind stays on while `user` kind is off).
- Experimentation adjacency: an "Experiment" flag template exists in-product; experimentation is a first-class LaunchDarkly domain (evidence: template naming only; not deep-fetched).

## Product B — Unleash

### Key observations

- Root level: API tokens, **projects**, **segments**, strategy types, tag types, **Unleash context** fields (incl. custom), users/groups/roles (RBAC). OSS edition = single "Default" project + development/production environments; enterprise = many projects/environments.
- **Feature flags** belong to projects and live next to project environments; a flag by itself "doesn't do anything" until **activation strategies** are assigned; creation requires unique name, flag type, project, optional description.
- **Activation strategies** (who gets the feature) are assigned per flag **per environment**; OR semantics across strategies (any strategy true → enabled); same strategy in different environments are independent instances; strategies can be copied between environments.
- **Strategy constraints** (AND semantics) narrow a strategy by context fields (e.g., email domain; timing; region); **segments** are reusable named constraint collections referenced by strategies, kept in sync everywhere they are referenced.
- **Release templates** (enterprise-era capability): milestones of strategies/segments standardizing a rollout; applied to a flag in an environment creating a **release plan**; **impact metrics** (error counts, memory, latency sent from the app) can auto-advance milestones and **pause the rollout when a metric crosses a safety threshold**.
- **Variants** with weights and payloads decide *which version* of a feature a user gets; can differ per environment; variants also enable A/B testing guides.
- Evaluation integration: SDKs (`isEnabled(key)`, `getVariant(key)`); pseudocode example renders old/new stylesheet by flag; **the API key decides which environment's flags the SDK gets**.

## Product C — Flagsmith

### Key observations

- Vendor definition: "a feature flag is a control point in your code that determines whether a particular feature or behaviour is active"; simple on/off (boolean) or multivariate.
- What flags enable: **decouple deployment from release**; staged rollouts; A/B testing and experimentation; **remote configuration** (change behavior in real time without redeploying).
- Documented workflow: create flag ("sharing_button"), enable on development, disable on production; wrap UI code in a conditional on the flag; deploy code while feature is hidden; enable for team/beta testers; enable for everyone in production.
- **Rollout by percentage**: implemented as a segment with a **% split rule** (1–100) connected to the flag via **segment overrides** per environment; mechanics documented precisely — identity ID + segment ID merged and hashed into a stable 0–1 float; identity stays consistently in/out as the percentage changes (stickiness); requires passing an identity (`flagsmith.identify('user_123')`) — environment-level (anonymous) fetches never fall in the split.
- **Flag lifecycle** (vendor-documented): short-lived flags (rollouts, experiments) get removed from code *and* platform after use; long-lived flags = **kill switches** (remotely remove a feature; long-lived by design) and **feature-management flags** (segments+flags driving features by plan for the app's lifetime). **Stale flag detection** automatically flags features unchanged for a configurable period.
- Platform machinery: projects/environments, **scheduled flags**, **feature versioning**, **release pipelines**, **feature health metrics**, flag analytics, **code references**, RBAC (role-based access control), audit; **A/B testing with integrations** (push flag exposures to third-party analytics) plus a native **Experimentation (Beta)** product area.
- SDK integration: client-side and server-side SDKs; identity + **traits** sent from the app; OpenFeature compatibility.

## Product D — ConfigCat

### Key observations

- Object model: a **Setting** is the essential unit — types: bool (on/off toggle), string, integer, double; "a Feature Flag is a Setting of type Bool". Anatomy: **name** (human readable), **key** (variable name in code), **type**, **value** (actual value; **can be different in each environment**). Text settings optionally JSON-validated. Two value modes: **free-form values** vs **predefined variations** (reusable value set picked from a dropdown in rules).
- A **Config** is a collection of Settings — "like an online version of a traditional config file". **Product** = collection of Configs, Environments, team members (≈ one application + its team). **Organization** above products (billing/auth/privacy).
- Environments: "represent an environment in your development lifecycle (like production, staging, development)"; same settings, different values; **each environment-config pair has its own SDK key** used to initialize the SDK.
- Delivery model: SDKs poll/download the **config JSON** for the SDK key's environment; polling modes & caching documented; a **Proxy** exists for in-cluster evaluation; **data governance via CDN** choice.
- Governance: **approval flow & scheduled changes** (change requests), organization/roles, team management (SSO, SCIM, SAML).
- Hygiene: **zombie flags** documentation; **scan & upload code references**; **variation ID for analytics**; migration guide *from LaunchDarkly*; public management API; CLI; MCP server; integrations (analytics, CI, chat).

## Product E — Split (Harness Feature Management & Experimentation)

### Key observations (from official API reference; concept-narrative pages not reached)

- Two-level object model: a **feature flag** exists at account/project level (name, description, tags, rollout status, **traffic type**); a **feature flag definition** is the flag's configuration **in a specific FME environment** (`name, environment, trafficType, killed, treatments[], defaultTreatment, trafficAllocation, rules[], defaultRule(buckets), creationTime, lastUpdateTime`).
- Targeting vocabulary: **treatments** (the values/labels the app receives), **rules → conditions → matchers** (attribute-based targeting), **buckets** (traffic allocation within rules), **traffic allocation** (overall %), **default rule** (everyone else), **default treatment**.
- **Kill** is an explicit first-class operation: `killed` boolean in the definition; dedicated API "Kill feature flag in environment" / "Restore"; unconfiguring or deleting a flag makes SDKs return the reserved **"control"** treatment.
- **Reallocate traffic (reseed bucketing)** API — resets bucketing seeds, rehashing users into new buckets under the same rules (explicit evidence that bucket assignment is a persisted, seed-based mechanism).
- **Segments**: list-based (keys uploaded per environment; plan-limited sizes), **large segments**, and **rule-based segments** (rules + exclusions); segments enabled per environment.
- **Traffic types** (user, account, …) — the kind of identity a flag evaluates against, declared per flag.
- Governance: **change requests** (submit a change to a flag or segment for approval, with comments and approvers), projects (formerly workspaces), environments, **flag sets** (grouping), restrictions, rollout statuses; **archive/unarchive** a flag (archived flags remain but are "no longer active for regular use").
- Positioning from docs root: "release a feature without re-deploying your application"; product family naming = "feature management experimentation" (FME).

---

## Cross-product Comparison

| Dimension | LaunchDarkly | Unleash | Flagsmith | ConfigCat | Split (FME) | Evidence |
|---|---|---|---|---|---|---|
| Named flag registry managed in a separate surface | Flags list per project; key permanent | Flags in projects; unique name required | Features in projects; create-first workflow | Settings/Flags in Configs within Products | Flags at project level + definitions per env | A×5 |
| Management surface distinct from running software | Web UI (+API/agent skills) | Web UI (self-hosted or SaaS) | Web UI (SaaS/self-hosted) | Dashboard (+CLI/API) | Dashboard (+API) | A×5 |
| State change affects running software without redeploy | "enable or disable … without redeploying" | toggling + strategies take effect live | "enable … and your feature is rolled out" | "change behavior remotely, without a new deployment" | "release a feature without re-deploying" | A×5 |
| Programmatic evaluation in app code | SDKs; `variation(key, context, fallback)` | SDKs; `isEnabled` / `getVariant` | SDKs; identify + flag fetch | SDKs init with env SDK key; config JSON download | SDKs; treatments returned; "control" when unconfigured | A×5 |
| Caller context for evaluation | Context (kinds, attributes) | Unleash context + custom fields | Identity + traits | User object for targeting (per targeting docs structure) | Traffic type + identity attributes | A×4, A/B×1 (ConfigCat context detail not deep-fetched) |
| Per-environment flag configuration | Targeting per env; env-bound SDK credentials | Strategies assigned per env; env-bound API keys | Env state/overrides; env-scoped segments | Values per env; SDK key per env×config | Definition per environment | A×5 |
| Container above environments | Projects | Projects (+root-level config) | Projects | Product (over Configs) | Projects (workspaces) | A×5 |
| Targeting rules on identity attributes | Targeting rules on context | Strategies + constraints on context fields | Segment rules on traits | Targeting rules (targeting-overview) | Rules → conditions → matchers | A×5 |
| Reusable audience object | Segments (referenced; not deep-fetched) | Segments (constraint sets) | Segments (% split + attribute rules) | Segments (referenced in docs index) | Segments (list/large/rule-based) | A×5 (surface-level for LD/ConfigCat) |
| Percentage rollout | Progressive rollout; % not mechanically documented | Gradual rollout strategy (5% example) | % split with documented hash-stickiness | (referenced; not deep-fetched) | Traffic allocation + buckets | A×3 (LD, ConfigCat moderate wording) |
| Consistent bucketing / stickiness | not directly observed | not directly observed | documented hashing mechanics | not directly observed | buckets + reseed API | A×2 — write as common with named support |
| Multivariate values / payloads | Variations: bool/string/number/JSON (+schema) | Variants with weights + payloads | Multivariate flags | Typed settings + predefined variations | Treatments | A×5 |
| Kill switch / instant off | Kill switch flag template; toggle off | Disable flag in environment | Kill switches (long-lived); disable | toggle off (bool setting) | Kill/restore API per environment | A×5 |
| Change governance | Review-and-save with comment | RBAC (change-request machinery enterprise; not fetched) | RBAC; scheduled flags | Approval flow & scheduled changes | Change requests with approvers | A×3 + partial |
| Lifecycle hygiene | Temporary-vs-permanent flag attribute | (not observed in fetched pages) | Stale flag detection; short-vs-long-lived lifecycle doc | Zombie flags; code references | Archive/unarchive | A×4 |
| Automated rollout safeguards | not observed in fetched pages | Impact metrics + auto-advance/pause | Feature health metrics; release pipelines | not observed | not observed | A×2 |
| Experimentation layer | Experiment template (native domain) | Variants enable A/B guides | A/B via integrations + Experimentation (Beta) | Variation ID for analytics (external analytics) | Native FME experimentation | A×5, but packaging varies: native vs integration |
| Delivery posture | SaaS | Self-hosted OSS / paid SaaS | Open-core SaaS + self-hosting | SaaS (+on-prem plan) | SaaS (Harness platform) | A×5 |

### Reading of the comparison

- The five legs with unbroken cross-product support (A×5): named flag registry in a separate management surface; state change without redeploy; SDK/API evaluation inside the running software; per-environment configuration; container above environments. Together with identity/context passing (A×4.5) these are the Type's skeleton.
- Targeting, percentage rollout, multivariate values, kill switch, governance are present everywhere in some form but with materially different depth — mature structure, not definition.
- Bucketing stickiness is directly documented only where mechanics pages were fetched; treat as a common engineering property of percentage rollout with named support, not a definitional requirement.
- Experimentation exists in all five but as a *layer* with different packaging (native product area, guides, integration hooks, analytics IDs); it never appears as the flag registry itself.

---

## Canonical Model — L0 / L1 / L2 / L3

### L0 — Defining Invariant (jointly-held; remove any leg → different Type)

1. **The feature-flag registry of record** — persistent, individually named flags (toggles) held as managed records in the platform, separate from the application's code and configuration files. Each flag carries identity (unique key), meaning (what it controls), and configuration state.
2. **Runtime-mutable behavior, deploy-independent** — changing a flag's state/configuration in the management surface changes the behavior of already-running software without building or redeploying it. (The vendors' own framing: "without redeploying", "without a new deployment", "release a feature without re-deploying".)
3. **Runtime evaluation integrated into the software** — the running application resolves flag values at runtime through an SDK/API integration (bound to the platform via credentials) and branches its behavior on the result. The application is the consumer of decisions; the platform is the decision point of record.

Jointly-held is load-bearing:
- 1 alone = a settings database / config file manager (no release control over running software).
- 2 without 1+3 = ad-hoc config reloading.
- 3 without 1+2 = hard-coded in-code toggles (the thin ancestor) — no management surface, no runtime mutability from a platform.
- 1+2 without 3 = a dashboard over configuration with nothing consuming it.
- 1+3 without 2 = build/deploy-time configuration, not release control.

Deliberately NOT in L0 (each fails the "would older/different products still fit" test):
- targeting/segments/percentage rollout (an on/off-only kill-switch deployment is still this Type);
- multivariate values (boolean-only realizations exist);
- cloud SaaS delivery (self-hosted OSS satisfies);
- SDKs in specific languages (any programmatic integration satisfies);
- web UI as the only surface (API/CLI/declarative management satisfies);
- environments as a specific feature name (per-context configuration separation is the concept; the dev/prod naming is convention).

### L1 — Common Mature Structure (very common; not definitional)

- **Environments** (dev/staging/production-class separation of flag state; environment-bound credentials deciding what the SDK sees) — 5/5.
- **Caller context + targeting rules** — identity/context attributes passed at evaluation; rules on attributes decide per-request outcomes — 5/5.
- **Segments** (named reusable audiences/constraint sets referenced by flags) — 5/5.
- **Percentage rollout** (gradual exposure; where documented, with consistent bucketing so identities don't flip as the percentage changes) — 5/5 present, mechanics documented in 2.
- **Multivariate flags** (string/number/JSON values or named variants, weights, payloads) — 5/5.
- **Kill switch posture** (instant all-off path; explicit kill/restore semantics in the strongest form) — 5/5.
- **Change history / audit and change governance** (comments on save, change requests/approvals, scheduled changes) — strong in 3, present elsewhere.
- **Flag metadata & organization** (description, owner/maintainer, tags, key conventions, containers above environments: project/product/workspace) — 5/5.
- **Management API/CLI parity** with the UI — 5/5 (surface evidence).

### L2 — Variant / Optional Structure

- **Native experimentation layer** (metrics, A/B on flags, holdouts) vs **experimentation-by-integration** (export exposures to analytics tools) — both documented; packaging varies.
- **Automated rollout safeguards** (health metrics auto-advancing/pausing milestone plans).
- **Release machinery** (templates/milestones/pipelines standardizing rollout sequences).
- **Flag hygiene tooling** (stale-flag detection, zombie flags, code-reference scanning, temporary-vs-permanent labeling, archive states).
- **Delivery topology variants**: SaaS vs self-hosted OSS vs open-core; local evaluation/edge proxies/CDN distribution for latency/data-governance.
- **SDK-side resilience behaviors**: fallback/default values on failure; reserved "control" treatment when unconfigured (product-specific labels; the *pattern* is common).
- **Client-side/mobile availability as an explicit per-flag decision** (security-motivated).
- **Platform-embedded realizations**: cloud-provider configuration services that include flag-shaped toggles (Firebase Remote Config class) — treated as boundary/adjacent; see below.

### L3 — Vendor-specific Structure (research notes only)

- LaunchDarkly: flag templates (Release / Kill switch / Experiment / 2-4-6-stage migration), views, multi-kind contexts, JSON-schema validation of variations, maintainer field, client-side availability default flipped for new accounts (Oct 2025 note), 5,000 flags/project default limit, migration-from-LD guides existing elsewhere (market position evidence).
- Unleash: activation-strategy abstraction (strategy types as extensible plugin surface), constraint AND / strategy OR semantics as named concepts, release templates + milestones + impact metrics safeguards, root-vs-project environment subsetting, OSS edition limits (single project, two environments).
- Flagsmith: % split implemented as a segment rule with documented identity+segment hash; segment overrides per environment as the rollout mechanism; feature versioning; release pipelines; "features" terminology.
- ConfigCat: Setting/Config/Product/Organization hierarchy ("online config file"), typed settings (bool/int/double/string) with the flag as bool subtype, free-form vs predefined variations value modes, per env×config SDK keys, proxy + CDN data governance, zombie flags.
- Split: flag (account) vs definition (environment) two-level model, traffic types, treatments/buckets/default-treatment vocabulary, killed boolean + kill/restore APIs, "control" treatment, reseed bucketing, large/rule-based segments, flag sets, FME family naming under Harness.

---

## Rejected Findings

- "A feature flag platform is a mobile remote-config service" — rejected as definition. Value delivery to clients is a *use* the vendors themselves name (Flagsmith explicitly lists remote configuration as an outcome), but the registry + release-control orientation is the Type's center. The remote-config-first shape is recorded as an adjacent/overlapping family, not the definition.
- "Percentage rollout is the defining capability" — rejected; boolean-only realizations satisfy the Type, and rollout percentage is absent from several sampled products' core flows (still present somewhere in each, but as L1 machinery).
- "SDKs with local caching/streaming are definitional" — rejected at that precision. What is definitional is *programmatic runtime evaluation*; how the SDK stays current (streaming, polling, download) is implementation detail varying by product (server-side local evaluation in one product, config-JSON polling in another, proxy/edge options in others).
- "Environments are definitional as a named object" — rejected at label level; the *separation of flag configuration per deployment context* is definitional-shaped and universal, but the specific object name/model varies (environment, config, project-subsetting). Kept in L1 with conceptual framing.
- "Experimentation is part of the definition" — rejected; every sampled product carries a flag core without requiring the measurement layer, and one realizes experimentation purely by integration.
- "Multivariate/typed values are definitional" — rejected; boolean flags are the canonical minimal form (ConfigCat even defines the flag as the bool subtype of Setting).

## Boundary Findings

### vs A/B Testing Platform / Digital Experimentation Platform (§06)

The sharpest functional overlap: flag platforms evaluate *and* sometimes measure. Separation test:
- The flag platform's deliverable is **controlled behavior of running software** (registry + evaluation + rollout machinery). Measurement of impact is optional and, in one sampled product, delegated to external analytics entirely.
- The experimentation platform's deliverable is **a measured causal comparison** (assignment + metric collection + analysis + winner). A flag platform can exist with zero metrics.
- Remove measurement and analysis machinery from an experimentation platform → you have a flag platform's assignment layer. Remove the release-control registry (lifecycle, kill, per-environment control) from a flag platform → you have an experiment assignment service. The leaves are distinct Types with an interlock (experiments commonly ride on flags).

### vs Continuous Delivery Platform (§12) / Application Deployment Management (§14)

- CD's unit of work is the **versioned deliverable** promoted through environments; the flag platform's unit is the **behavioral state of an already-deployed version**. They interlock (deploy code dark behind flags; flags make releases progressive), but removing the flag registry from a CD platform leaves deployment intact, and removing deployment machinery from a flag platform leaves release control intact. Distinct Types.

### vs Remote configuration services (mobile/cloud-platform-native, e.g., Firebase Remote Config class)

- Genuine partial overlap (Flagsmith names remote configuration as an outcome; the sampled platforms deliver values/payloads). The directional test recorded:
  - Center = **feature-availability control of a software release** (flag as managed feature record; engineer-authored code branches; flag lifecycle/cleanup; kill switch) → Feature Flag Management Platform.
  - Center = **delivery of configuration values to a client application population** (arbitrary parameter trees; app-version conditioning; per-app defaults), with feature gating as one use → remote config, a different (unprocessed) Type/shape.
- Source-access limitation: the mobile-native exemplar could not be fetched; this boundary is reasoned from the sampled platforms' own "remote config" self-description plus the flag-centric evidence, and is recorded for future verification. No claims about the exemplar's specifics are made.

### vs Configuration Management (§14) and Business Rules Management System (§10)

- Configuration Management (IT) manages server/infrastructure state; the flag platform manages feature availability of application behavior. Different subject and user population.
- BRMS executes business rules as decision logic; a flag evaluation is a single named availability decision consumed by application code, not a rule set governing business operations.

### "Remove what → becomes what" summary

- Remove the registry/management surface (flags as managed records) → in-code toggles / config files (thin ancestor, not the Type).
- Remove runtime evaluation integration → a config dashboard/database, not release control.
- Remove deploy-independence (state only changes via new builds) → build-time configuration, not this Type.
- Add metric-driven assignment + analysis as the center → A/B Testing / Experimentation Platform.
- Replace the release-control center with value delivery to clients → remote config family.

## Historical / Market-Sample Check (§24)

- Thin ancestor: in-code and config-file toggles (the practice Flagsmith's docs date to a 2009 engineering blog post by Flickr). No management surface, no platform record → fails L0 leg 1/3 jointly; correctly excluded as ancestor.
- Early platform-native realizations: self-hosted, library-plus-admin-UI tools satisfy the L0 (registry + separate surface + runtime mutability + in-app evaluation) without SaaS, cloud, streaming, or targeting depth. Unleash (OSS) is the live exemplar of this shape.
- Older/differently positioned products pass: a self-hosted instance with boolean flags and two environments satisfies the core; a cloud-provider-embedded flag service satisfies it as an embedded realization. No sampled or remembered era requires targeting, dashboards, or experimentation to be recognizable as the Type.
- Current-market checks passed: no L0 element is a post-2015-only implementation (runtime evaluation and registry predate the modern SaaS wave).

## Uncertainties

- LaunchDarkly percentage-rollout mechanics and segment objects were not deep-fetched; stickiness claims rely on Flagsmith/Split documentation.
- ConfigCat's identity/context evaluation details were not deep-fetched (targeting-overview not fetched); its context passing is inferred from documented targeting + SDK-key model with moderate confidence.
- Split concept-narrative pages (treatments narrative, SDK behavior) were not reached; evidence is API-reference-shaped (strong for object structure, weaker for UX narrative).
- Firebase Remote Config unreachable — the remote-config boundary line is reasoned, not source-verified against the exemplar.
- Unleash change-request/approval machinery exists at enterprise tier but was not fetched; approval flows asserted as common-mature from 3 products with direct evidence.
- The exact edge/proxy/data-governance landscape is only surface-observed (Flagsmith edge-proxy and ConfigCat proxy/CDN exist; depth not studied).

## Final Synthesis

A Feature Flag Management Platform is the engineering organization's release-control system of record for feature availability: it holds named feature flags as managed records separate from application code; it makes flag state runtime-mutable so that behavior changes reach already-running software without a redeploy; and it integrates runtime evaluation into the software via SDK/API so applications branch on the platform's decisions. Environments separate flag configuration per deployment context; targeting (context attributes, rules, segments) and percentage rollout determine who gets what; multivariate values, kill switches, change governance, and flag-lifecycle hygiene form the mature working layer; experimentation rides on top as either a native layer or an integration. The Type's boundary against experimentation is measurement-as-center vs control-as-center; against continuous delivery it is behavioral state of a deployed version vs versioned deliverables; against remote-config families it is release-control orientation vs value-delivery orientation. The definition survives the historical check: registry + separate management surface + runtime evaluation is the invariant; everything else modern is layered maturity.
