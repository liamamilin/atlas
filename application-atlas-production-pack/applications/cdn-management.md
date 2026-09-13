# CDN Management

## Overview

A **CDN Management** application is the operator-facing control plane of a content delivery network (CDN) service: the surface through which an organization defines how its sites, applications, APIs, and media are delivered from a provider-operated global edge network.

Its defining core is small:

```text
Delivery configuration
└── binds customer hostnames to content origins
    └── defines edge delivery behavior (caching rules)
        ├── deployed onto the provider's edge network
        ├── reached by end users through DNS-level routing
        └── governed by cache control (behavior + purge)
```

Everything else commonly associated with CDN products — TLS certificate automation, traffic analytics, origin failover, edge security, edge compute — is standard capability layered on this core, not what makes the product a CDN management application.

The boundary in one sentence: a CDN management application **configures and operates content delivery over someone else's edge network**. Remove the caching semantics and it becomes traffic management; remove the provider's edge network and it becomes self-hosted reverse-proxy configuration; remove the delivery configuration and nothing is being managed.

## Users & Context

Primary users are technical operators of internet-facing properties:

- **Infrastructure / platform engineers** — onboard new sites and APIs onto the CDN, bind hostnames, configure origins and caching, manage certificates.
- **Web / application developers** — adjust cache behavior for their application's assets, wire deployments to purge or version content, often through APIs and infrastructure-as-code rather than the console.
- **SRE / operations** — watch traffic, cache hit ratios, and error rates; purge or roll back configuration during incidents.
- **Security engineers** — operate the edge security capabilities that ride on the same configuration (rate limits, geo restrictions, bot/WAF controls where bundled).

The work context is operating properties whose traffic comes from the public internet: websites, e-commerce, APIs, software downloads, video. The CDN provider runs the edge; the operator's job is to keep the delivery configuration correct, current, and observable. Teams typically manage many delivery configurations (one or more per site, environment, or region) under one organizational account.

## Core Model

### The Defining Core

**Delivery configuration.** The central managed object is a per-property configuration that binds a set of customer hostnames to one or more content origins and defines how the edge handles requests. Products name it differently — zone, distribution, service, property, endpoint — but the structure is the same: it is the unit that carries delivery behavior, and it is the unit that is versioned, activated, and monitored. A typical organization holds many of them.

**Provider-operated edge network.** The configuration is not run on the customer's infrastructure. It is propagated to a global network of edge locations (points of presence) operated by the CDN provider, where it governs how edge servers respond to requests. The operator's leverage is configuration; the provider's leverage is the network.

**Hostname routing integration.** End-user traffic reaches the edge through DNS. The product either provides the DNS itself (acting as authoritative DNS and reverse proxy for the domain) or generates the routing target the customer points their own DNS at — a provider-owned hostname that the customer's domain becomes an alias of (via CNAME or equivalent records). This integration is what puts the customer's hostnames onto the edge network; without it the delivery configuration is inert.

**Cache control.** The CDN's defining function is caching content at the edge, so the defining control is cache behavior: what is eligible to cache, how long it stays cached (time-to-live, honoring or overriding origin cache headers), and what makes two requests distinct objects (the cache key — typically the URL, extendable to selected headers, cookies, or query strings). The inseparable counterpart is **purge/invalidation**: the operator's ability to remove cached content before it expires, by URL, by prefix, by tag, by hostname, or wholesale.

### Standard Capabilities of Mature Products

These are near-universal in current products and necessary for practical operation, but they are additions to the core rather than the definition:

- **TLS for custom hostnames** — certificates covering the customer's domains, either issued and renewed by the provider (with domain-ownership verification) or uploaded by the customer. Serving a custom hostname over HTTPS requires a certificate that covers it, and possession of that certificate is how the product verifies the customer's authority to claim the hostname.
- **Origin machinery** — multiple origins per configuration, origin groups with failover, health checks against origins, and mid-tier caching layers (origin shielding / regional caches) that concentrate origin fetches and reduce origin load.
- **Rule-based configuration** — ordered rules that match requests (by path, file extension, hostname, cookies, headers, geography) and apply behaviors (caching settings, redirects, header manipulation). Rule evaluation order is part of the model: first match or explicit precedence determines the outcome.
- **Configuration versioning and activation** — changes are made as new versions and then deployed ("activated") to the edge network, commonly with a staging target distinct from production, and rollback to a previously activated version.
- **Operational visibility** — traffic volume, cache hit/miss, bandwidth, error rates, per-geography breakdowns; request logs; alerts on metrics such as error-rate spikes.
- **Multi-surface management** — a web console plus a programmatic API as the constant pair; command-line tools and Terraform/infrastructure-as-code support are common.
- **Organizational access control** — accounts containing the delivery configurations, with members, groups, and roles governing who can view or change what.
- **Content access controls** — restricting who can fetch content: signed URLs or tokens for private content, geographic allow/block lists.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Delivery configuration
Implementations:    zone (DNS-anchored), distribution (cloud resource),
                    service (code-defined), property (rule tree),
                    endpoint (profile member)

Concept:            Routing integration
Implementations:    provider as authoritative DNS + proxied records,
                    CNAME to a provider edge hostname,
                    alias records for zone apex domains

Concept:            Cache behavior definition
Implementations:    declarative rule UI, ordered cache-behavior list,
                    configuration code (VCL / edge-language),
                    global + custom caching rules
```

A reader who has only seen one implementation should still be able to recognize the others from the core model.

## How It Works

### Onboard a property onto the edge

```text
Create a delivery configuration
→ define the origin (where the definitive content lives)
→ add the customer hostname(s) to the configuration
→ obtain or upload a TLS certificate covering the hostname
→ point DNS at the edge (CNAME/alias to the provider's routing target,
  or hand DNS to the provider)
→ activate/deploy the configuration to the edge network
→ traffic for the hostname now flows through the edge
```

The DNS step is the go-live moment: until the customer's domain resolves to the edge, the configuration receives no traffic. After it, every request for the hostname is answered by an edge location, which serves from cache or fetches from the origin per the configuration.

### Operate the delivery configuration

```text
Observe analytics (traffic, cache hit ratio, errors)
→ adjust cache rules / behaviors for problem paths
→ activate the new configuration version
→ verify the effect in analytics
```

This is the standing loop of the role. Configuration changes are deliberate deployments, not live edits: they are made against a version and pushed to the network, with staging-and-production discipline and rollback available in mature products.

### Keep content fresh

Two complementary mechanisms, and choosing between them is a daily decision:

- **Purge/invalidate** — remove cached objects from the edge so the next request refetches from the origin. Used for corrections, emergency rollbacks of published content, and coordinated deploys.
- **Versioned content URLs** — publish updated assets under new names so caches naturally treat them as new objects. Products recommend this for high-frequency updates because it avoids purge entirely and works even through caches the CDN does not control.

### Handle incidents

```text
Error-rate alert fires
→ inspect analytics (which hostnames, paths, geographies, status codes)
→ remediate: purge bad content, adjust or bypass caching for a path,
  fail over to another origin, or roll back the last activation
→ confirm recovery in analytics
```

### Core vs standard vs optional

- **Defining core** — delivery configuration; provider edge network as deployment target; DNS-level routing integration; cache behavior control; purge/invalidation.
- **Standard capabilities** — TLS/certificates, origin machinery, rule-based configuration, versioned activation, analytics/logs/alerts, console+API, organizational access control, content access controls.
- **Optional / variant** — edge compute, bundled edge security, multi-tenant delivery machinery, media-streaming specialization, multi-CDN steering (see Variants).

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Delivery configuration list

The operator's home surface.

- lists the delivery configurations in the account, with status (active/inactive), hostnames, and recent activity
- primary actions: create a configuration, open one, search

### Configuration editor

Where delivery behavior is defined.

- origin settings (origin address, protocol, host header), hostname bindings, cache rules/behaviors with their match conditions and evaluation order, TLS settings
- primary actions: edit settings as a new version, validate, save

### Activation / deployment control

The go-live surface for configuration changes.

- shows versions, their state (draft / staged / active), and activation history
- primary actions: activate to staging or production, promote, roll back to a previous version

### Purge / invalidation surface

- form to submit purge requests by URL, path prefix, tag, hostname, or everything, scoped to a configuration
- primary actions: submit purge, view recent purge activity

### Certificate / TLS management

- lists certificates and the hostnames they cover, issuance/renewal state, ownership-verification steps
- primary actions: request a managed certificate, upload one, complete domain verification

### Analytics dashboards

- traffic volume, cache hit ratio, bandwidth, error rates over time; breakdowns by hostname, path, geography, status code; links into logs and alert configuration
- primary actions: filter, drill down, configure alerts

### API / CLI / infrastructure-as-code

The same objects and operations exposed programmatically. Mature products treat the API as a first-class surface — many teams never touch the console for routine changes, driving configuration from code repositories and deployment pipelines.

## Important Rules / Behaviors

### Configuration is deployed, not edited live

Changes take effect through activation/propagation to the edge network. Products enforce discipline around this: versions must be explicitly activated; validation errors block activation; some products separate staging from production and support rapid rollback of a bad activation.

### One delivery configuration owns a hostname

A hostname can be bound to only one delivery configuration at a time within the provider. This makes hostname binding an ownership claim, enforced in part through TLS: adding a custom hostname requires a certificate covering it, which only the domain's controller possesses.

### The cache key defines object identity

What distinguishes one cached object from another — URL alone, or URL plus selected headers/cookies/query strings — is operator-configurable. This has a practical consequence: purging must address the object under its cache key, so purge capabilities interact directly with cache-key configuration.

### Purge clears the edge, not the world

Purging removes content from the CDN's edge caches. Downstream caches — corporate proxies, browsers — may retain copies until their own expiry. This is why versioned URLs are the recommended mechanism for frequent content changes.

### Cache rules do not rewrite history

Changing cache behavior typically affects objects cached from that point on; objects already cached under the old behavior keep their existing freshness until they expire or are purged. Operators pair rule changes with purges when they need the change to take effect immediately.

### Rule order is behavior

Where configuration is rule-based, evaluation order (first match, or explicit precedence) is part of the semantics. A mis-ordered rule silently changes delivery behavior — a classic operational error this class of application must make visible.

### Traffic visibility is billing-relevant

CDN services bill primarily on delivery volume (data transfer out of the edge) and request counts. The same analytics that show operators their traffic also underpins charging and, in contract-based products, reporting granularity — which is why per-configuration traffic attribution identifiers exist in some products.

## Variants

- **Declarative rule consoles** — configuration assembled from match/behavior rules in a UI, with templates for common cases (typical of self-serve and cloud-provider products).
- **Code-defined configuration** — delivery logic expressed as configuration code or edge-language programs, versioned in the same clone-edit-activate cycle (developer-centric products).
- **Enterprise rule trees** — deeply structured rule hierarchies gated by contract-level product entitlements, with shared configuration fragments and bulk operations across large property estates (large-enterprise products).
- **Edge compute extension** — the same configuration gains the ability to run customer code at the edge (edge functions/Wasm). The delivery configuration remains the anchor; when code deployment becomes the primary object, the product is drifting toward an edge/serverless platform Type.
- **Bundled edge security** — WAF, DDoS protection, bot management, rate limiting delivered on the same edge and managed alongside delivery configuration; depth varies from built-in to separately licensed products.
- **Multi-tenant / SaaS delivery** — machinery for serving thousands of customer domains off shared configuration (hostname bulk management, multi-tenant distributions), aimed at SaaS platforms.
- **Media/streaming specialization** — configurations tuned for video delivery (adaptive formats, origin integration with packaging services).
- **Business-model variants** — self-serve freemium tiers, usage-based pay-per-use, contract-gated enterprise engagements; these shape onboarding and limits, not the core model.
- **Platform convergence** — CDN capabilities being absorbed into broader edge/application-delivery platforms; several cloud providers now steer customers from standalone CDN products toward combined edge services. The management surface described here persists inside those platforms.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| DNS & DHCP Management | adjacent, frequently co-used | managed object is the DNS zone and its records; CDN management only *uses* DNS to route traffic onto the edge — its managed object is the delivery configuration and cache behavior |
| Load Balancer Management | adjacent, overlapping capability | balances traffic across customer-controlled backends; lacks the defining caching semantics (TTL, cache key, purge). Some CDN products include load balancing as a capability — the presence of caching is the seam |
| Network / Infrastructure Monitoring | adjacent | observes infrastructure; CDN management configures and operates delivery. Analytics is a capability inside CDN management, not the whole |
| DDoS Protection Platform / WAF | adjacent, often bundled | managed object is threats and security policy riding the edge; remove delivery/caching configuration and only the security product remains |
| Cloud Management Platform | broader | manages heterogeneous cloud resources; CDN management is specific to content delivery over a provider's edge network |
| Serverless Management Platform | drift neighbor | edge functions are an extension of CDN configurations; when code deployment, not delivery configuration, is the primary object, it is the serverless/edge-compute Type |
| Storage Management | upstream integration | manages the origin stores (object storage, web servers); CDN management manages delivery from them |
| Content Distribution Platform (media domain) | false friend | despite the similar name, that Type concerns media/entertainment content distribution to channels and platforms (publishing semantics), not edge-caching infrastructure control |
| Website builder / deployment platforms | different Type | when a hosting platform fully abstracts the CDN away, end users face no CDN management surface at all — the Type requires an operator-facing control plane |

The sharpest boundary is with **Load Balancer Management**: both route traffic and both do health checks and failover. The discriminator is caching — cache behavior and purge are what make a CDN a CDN.

## Representative Products

- **Cloudflare** — reverse-proxy model: the provider is the authoritative DNS and the edge; delivery behavior configured as zone-level rules
- **Amazon CloudFront** — cloud-resource model: distributions with ordered cache behaviors, deep integration with the surrounding cloud platform
- **Fastly** — code-defined model: services whose delivery logic is configuration code, deployed through strict version activation
- **Akamai** — enterprise model: contract-gated properties with structured rule trees, shared configuration fragments, and bulk estate management
- **Azure CDN** — cloud-provider standard model: profiles and endpoints; documented as transitioning into the provider's broader edge/application-delivery platform

These five were chosen to span configuration philosophies, customer tiers (self-serve to contract-gated enterprise), and delivery form factors (standalone service to cloud-platform module).

## Sources

Research date: **2026-09-07**

- Cloudflare Fundamentals & Cache docs — https://developers.cloudflare.com/fundamentals/ , https://developers.cloudflare.com/cache/how-to/purge-cache/ , https://developers.cloudflare.com/cache/how-to/cache-rules/
- Amazon CloudFront Developer Guide — https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html (plus How CloudFront Works, Cache behavior settings, Invalidation, Alternate domain names, CloudWatch monitoring pages)
- Fastly documentation (guides) — https://www.fastly.com/documentation/guides/ (Core concepts, Selecting a service type, Observability)
- Akamai TechDocs, Property Manager — https://techdocs.akamai.com/property-mgr/docs/welcome-prop-manager (plus Key concepts and terms)
- Azure CDN documentation — https://learn.microsoft.com/en-us/azure/cdn/cdn-overview (plus Purge endpoint, Caching rules)

> Sourcing note: all findings above come from official product documentation fetched on the research date. Product-specific numeric limits, default values, and pricing details observed during research were deliberately kept out of this document. One product's monitoring overview page was not retrievable (recovered via its CloudWatch integration page); one vendor's analytics surface was evidenced only indirectly. Regional CDN markets were not sampled; the definition is believed to hold there but was not verified against those products.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
