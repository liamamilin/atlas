# Research Notes — CDN Management

Research date: 2026-09-07
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what "CDN Management" is as an Application Type: the operator-facing control surface through which an organization configures, deploys, and operates content delivery over a CDN provider's edge network. The leaf sits in DIRECTORY §14 (IT, Cloud & Infrastructure) next to DNS & DHCP Management, Load Balancer Management, and Network Monitoring — the "management console for an infrastructure function" family.

## Initial Boundary

Working hypothesis before research:

- Core use: bind customer hostnames to content origins, define caching/delivery behavior, deploy that configuration to a provider-operated global edge network, purge cached content, manage TLS for custom hostnames, observe traffic.
- Users: infrastructure/ops engineers, web platform engineers, SRE, security engineers, developers.
- Nearest types: DNS & DHCP Management (routing integration), Load Balancer Management (traffic distribution), Network Monitoring (observability), DDoS Protection / WAF (edge security bundling), Cloud Management Platform (broader resource management), Content Distribution Platform (§27 — media-domain false friend).
- Unknowns: whether the Type is provider-console-only or includes third-party multi-CDN management tools; how deep edge-security bundling goes before the product becomes a security Type; whether edge compute is part of the Type.

## Research Questions

1. What is the central managed object (zone / distribution / service / property / endpoint) and what does it bind?
2. How does end-user traffic get routed onto the provider's edge network (DNS/CNAME/anycast machinery)?
3. What is the origin model (origin servers, origin groups, health checks, shielding/mid-tier caches)?
4. What is the cache model (rules, TTLs, cache keys, purge/invalidation)?
5. How is configuration deployed and changed (versioning, staging vs production activation, rollback, propagation)?
6. What TLS/certificate machinery exists for custom hostnames?
7. What operational visibility is exposed (traffic, cache hit ratio, errors, logs, alerts)?
8. What access/security controls exist — on the configuration (roles) and on the content (signed URLs, geo restrictions)?
9. What interfaces exist (console, API, CLI, IaC)?
10. Where is the boundary with DNS management, load balancer management, monitoring, and security products?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Primary docs used |
|---|---|---|
| Cloudflare | reverse-proxy/security-first, zone-based, self-serve freemium → enterprise | developers.cloudflare.com (fundamentals, cache) |
| Amazon CloudFront | AWS-native distribution model, pay-per-use, developer-oriented | docs.aws.amazon.com (CloudFront Developer Guide) |
| Fastly | developer-first, code-defined config (VCL/Compute), service versioning | fastly.com/documentation (guides/concepts) |
| Akamai | enterprise-first, contract/product-gated, rule-tree properties | techdocs.akamai.com (Property Manager) |
| Azure CDN | cloud-provider standard profile/endpoint model (market in transition to Azure Front Door) | learn.microsoft.com (Azure CDN docs) |

## Sources

All fetched 2026-09-07. All Tier-1 official documentation.

- Cloudflare Fundamentals — https://developers.cloudflare.com/fundamentals/
- Cloudflare Concepts: How Cloudflare works — https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/
- Cloudflare Concepts: Accounts, zones, and profiles — https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/
- Cloudflare Cache: Concepts — https://developers.cloudflare.com/cache/concepts/
- Cloudflare Cache: Purge cache — https://developers.cloudflare.com/cache/how-to/purge-cache/
- Cloudflare Cache: Cache Rules — https://developers.cloudflare.com/cache/how-to/cache-rules/
- AWS: What is Amazon CloudFront — https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
- AWS: How CloudFront delivers content — https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html
- AWS: Cache behavior settings — https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesCacheBehavior.html
- AWS: Invalidate files — https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html
- AWS: Alternate domain names (CNAMEs) — https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html
- AWS: Monitor CloudFront metrics with CloudWatch — https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.html
- Fastly: Guides index — https://www.fastly.com/documentation/guides/
- Fastly: Core concepts — https://www.fastly.com/documentation/guides/concepts/
- Fastly: Selecting a service type — https://www.fastly.com/documentation/guides/concepts/services/
- Fastly: Observability guides — https://www.fastly.com/documentation/guides/observability/
- Akamai: Welcome to Property Manager — https://techdocs.akamai.com/property-mgr/docs/welcome-prop-manager.md
- Akamai: Key concepts and terms — https://techdocs.akamai.com/property-mgr/docs/key-concepts-terms.md
- Azure CDN: What is a content delivery network — https://learn.microsoft.com/en-us/azure/cdn/cdn-overview
- Azure CDN: Purge an endpoint — https://learn.microsoft.com/en-us/azure/cdn/cdn-purge-endpoint
- Azure CDN: Caching rules — https://learn.microsoft.com/en-us/azure/cdn/cdn-caching-rules (archived page, still served)

Fetch failures / limitations:

- Akamai Property Manager overview URL redirected to TechDocs home on first fetch; recovered via the documented `.md` suffix convention (documented on the page itself).
- CloudFront "monitoring-cloudfront" page returned empty (JS-rendered); recovered via the "monitoring-using-cloudwatch" page on second attempt.
- Cloudflare cache concepts page is a navigation page; underlying concept pages not individually fetched — Cloudflare caching claims kept at the level of the pages actually read.
- No third-party multi-CDN management tooling was fetched; see Uncertainties.

## Product Observations

### Cloudflare (evidence layer A unless noted)

- Organization: user profile → account → zones. Zones are domains (or subdomains) added to Cloudflare; zone-level services (Cache Rules, Load Balancers) affect only that zone; account-level products (Workers, Pages, Bulk redirects) affect all zones. Accounts contain members, billing profiles, lists.
- Traffic model: Cloudflare acts as authoritative DNS provider and reverse proxy. With a full DNS setup, proxied DNS records resolve to Cloudflare anycast IPs instead of origin IPs; HTTP/HTTPS traffic for proxied records routes through Cloudflare. Stated reverse-proxy benefits: load balancing, attack protection (origin IP hidden), caching, SSL/TLS termination.
- Caching configuration: Cache Rules customize "what is eligible to cache, how long it should be cached and where", plus interactions with cache and other Rules products. Rules can be created in dashboard, API, or Terraform; rules templates exist; rules can be versioned (Version Management product). Cache Rules require proxied DNS records. Plan-tiered rule-count limits exist (L3).
- Cache keys: a Cache Rule can set a custom cache key; the cache entry is then indexed by that key rather than the URL alone; this interacts with purge (dashboard single-file purge may not work for custom keys including headers/cookies; API purge, purge-by-host, purge-by-prefix, purge-by-tag, purge-everything are alternatives).
- Purge: "Instant Purge" with options — single-file (URL), purge everything, by cache-tags, by hostname, by prefix, cache-key resources, varied images, zone versions via API. Plan-tiered rate limits and bucket sizes documented (L3 — numeric values stay here).
- Cache concepts documented: default cache behavior, origin cache control, CDN-Cache-Control, retention vs freshness (TTL), revalidation, Vary.
- Zone used to "monitor security and performance" (indirect evidence for analytics surface; analytics product pages not fetched).

### Amazon CloudFront (evidence layer A)

- Central object: the distribution. "You create a CloudFront distribution to tell CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery." Distribution config (not content) is sent to all edge locations/POPs.
- Origins: Amazon S3 buckets or custom HTTP servers; origin access control restricts S3 access; origin groups exist (referenced in cache behavior settings).
- Delivery: CloudFront assigns a domain name (e.g., d111111abcdef8.cloudfront.net); alternate domain names (CNAMEs) let customers use their own hostnames. DNS routes each request to the best POP.
- Cache hierarchy: POPs (edge locations) + regional edge caches between POPs and origins; less-popular objects evicted from POPs persist longer at regional edge caches; invalidation removes objects from both POP and regional edge caches; dynamic requests and proxy methods bypass regional edge caches.
- Cache behaviors: ordered list evaluated by URL path pattern (first match wins; default behavior `*` always last). Per behavior: target origin or origin group, viewer protocol policy (HTTP+HTTPS / redirect / HTTPS-only), allowed HTTP methods, cached HTTP methods, cache key composition (headers allowlist / cookies forward+allowlist / query-string forward+cache policy), TTL controls (minimum/default/maximum; origin Cache-Control honored or overridden), signed URLs/cookies with trusted signers, compression, Lambda@Edge associations per event (viewer request / origin request / origin response / viewer response), gRPC toggle.
- Custom domains & TLS: alternate domain names must be lowercase and covered by a valid TLS certificate (ACM or trusted CA); SAN coverage proves the customer's authority to add the name; only one certificate per distribution; zone apex cannot use CNAME (Route 53 alias records or anycast static IPs as workarounds); duplicate/overlapping alternate domain names across distributions rejected (wildcard overlap resolved by most-specific match); domain-fronting protection (SNI vs Host checks, 421 response); distribution identified by Host header.
- Invalidation: remove files from edge caches before expiry; alternative is file versioning (new URLs), which the docs recommend for frequent updates (also cheaper — invalidation has a cost beyond the first quota, L3).
- Monitoring: CloudWatch integration; operational metrics per distribution and edge functions shown as console graphs; alarms (e.g., on 5xxErrorRate); additional metrics opt-in per distribution at extra cost.
- Variants: standard distribution vs multi-tenant distribution + distribution tenants (CloudFront SaaS Manager) for SaaS providers managing many similar sites.
- Pricing: data transfer out from edge + HTTP/HTTPS requests, varying by region and features (documented qualitatively).

### Fastly (evidence layer A)

- Central object: the service. Two service types: VCL-powered CDN services and Wasm-powered Compute services. Common setup needs: domains (receive traffic), backends (forward traffic onward), TLS (secure connections), DNS (point domains to Fastly).
- Service versions: configuration is versioned; edit flow is "clone the active version → edit → Activate on Production". Versions referenced across web interface, CLI (`fastly service-version activate`), and API.
- Backends: origin servers defined as part of service configuration (host, override host, SSL settings); creatable via web, CLI, API, or VCL declaration; health checks are pre-configured requests POPs make to backends to confirm readiness; load balancing, failover/redundancy, rate limiting, ACLs, geolocation documented as concepts.
- Domains & TLS: TLS subscription flow — add domain to service version, activate, create TLS subscription (Fastly can obtain certificates, e.g., via Let's Encrypt ACME), publish the `_acme-challenge` CNAME for domain verification, then retrieve the CNAME/A/AAAA records to point the domain at Fastly (CNAME for subdomains; A/AAAA for apex). TLS configurations expose protocol/HTTP versions.
- Cache: content cached per POP based on freshness rules from Cache-Control headers or service configuration; POPs operate independently and forward misses to origin; concurrent similar requests in a POP are collapsed (request collapsing); shielding focuses all origin fetches across the network to a single POP to reduce origin traffic; purging marks objects stale or invalidates them; serving stale documented.
- Observability: control-panel observability pages, dashboards, alerts.
- Interfaces: web (manage.fastly.com), CLI (fastly), API (api.fastly.com), VCL as configuration language; Compute services run customer code (Rust/JavaScript/Go → Wasm) handling the full request-response cycle.

### Akamai (evidence layer A)

- Access structure: Akamai Control Center → Content delivery > CDN > Properties. Hierarchy: account → groups (access control, roles, reporting consolidation, typically mapping to org structure) → contracts (fixed terms enabling products) → products (determine baseline rule behaviors; allow creating properties, CP codes, edge hostnames) → modules (add-ons enabling additional behaviors) → properties.
- Central object: the property — "a container for your Akamai setup and services for your site, application, download files, or streams"; applies rules to a set of hostnames; only one property at a time per hostname.
- Hostname machinery: property hostname (customer's FQDN, e.g., www.example.com) → DNS CNAME → edge hostname (Akamai-generated canonical name, e.g., www.example.com.edgesuite.net or .edgekey.net) → Akamai mapping algorithms resolve to the optimal edge server IP; origin hostname (e.g., origin-www.example.com) is a new DNS record pointing at the origin server. Edge hostname security options vary.
- Property versions: snapshot versions with ascending IDs, timestamps, last-modifier, notes; freely modifiable until activated; after activation a new version is required. Activations deploy a version to staging or production network; same version can be activated multiple times; activation can be cancelled shortly after request, or rolled back via "fast fallback" within seconds. Activated settings are distributed to the network as an XML metadata configuration file.
- Rules: rule tree with a top-level default rule plus rules arranged in a tree up to five levels deep; each rule = match criteria (the IFs, e.g., "origin failure like a timeout") + behaviors (the THENs, e.g., "redirect to alternate hostname"); rule templates; rule formats (versioned feature sets, freezable for stability); variables interpreted at runtime on edge servers; advanced/custom behaviors via professional services.
- Includes: reusable config snippets without hostnames, independently versioned and activated, for sharing settings across properties or delegating rule management to application teams.
- Hostname buckets: for SaaS/PaaS providers with thousands of custom domains — add/remove hostnames without incrementing property versions, auto-activated separately from config logic.
- CP codes: content provider codes required to activate properties; used for traffic tracking, billing, and reporting granularity.
- Validation: errors prevent activation; warnings can be acknowledged/skipped.
- Interfaces: Property Manager UI in Control Center; PAPI (Property Manager API); Terraform provider (Property Provisioning module); Property Manager CLI; VS Code and Eclipse plugins; Postman collection; bulk operations (bulk search → bulk versions → bulk patches → bulk activations, asynchronous).
- Sibling products on the same edge: EdgeWorkers (edge compute), Adaptive Media Delivery, Purge Cache (separate product docs), Edge DNS, security products.

### Azure CDN (evidence layer A)

- Structure: profile → endpoints. "You also need to create a content delivery network profile, which is a collection of content delivery network endpoints. Every content delivery network endpoint is a specific configuration which users can customize with required content delivery behavior and access." Profiles organize endpoints by internet domain, web application, or other criteria. Subscription-level limits on profiles/endpoints/custom domains documented.
- Delivery: user requests a URL on the endpoint hostname (*.azureedge.net) or a custom domain; DNS routes to the best-performing POP (usually geographically closest); cache miss → fetch from origin (Azure Web App, Cloud Service, Storage, or any public web server); cached until TTL from HTTP headers expires; if origin specifies no TTL, a default TTL applies (L3: 7 days — documented but kept out of final doc).
- Caching rules: one global rule per endpoint (affects all requests; overrides HTTP cache-directive headers) + custom rules matching path (wildcard-supported, max length documented) or file extension (comma-separated list); caching behaviors: Bypass cache / Override / Set if missing; custom rules processed in order, later (more specific) rules take precedence; rule changes don't retroactively affect already-cached files (purge needed).
- Purge: per endpoint — single URL purge, wildcard purge (`/*`, `/pictures/*`), root purge, or purge-all; query strings ignored in purge paths (documented); caveat that purge clears only CDN edge caches, not downstream proxy/browser caches; recommended alternative is asset versioning (new URLs).
- Features: dynamic site acceleration (route optimization bypassing BGP), HTTPS custom domain support, Azure diagnostics logs, file compression, geo-filtering (restrict access by country/region).
- Market transition (documented on the pages): Azure CDN from Microsoft (classic) stopped new onboarding Aug 2025 and retires Sep 2027 in favor of Azure Front Door Standard/Premium; Azure CDN from Edgio retired Jan 2025. CDN is converging with broader edge/application delivery platforms in this cloud.

## Cross-product Comparison

| Dimension | Cloudflare | CloudFront | Fastly | Akamai | Azure CDN |
|---|---|---|---|---|---|
| Central config object | Zone (+ Cache Rules etc.) | Distribution | Service (VCL CDN or Compute) | Property (under account/group/contract/product) | Endpoint (under profile) |
| Hostname binding | proxied DNS records on the zone | alternate domain names (CNAMEs) on distribution | domains on service + TLS subscription | property hostnames → edge hostnames via CNAME | custom domains on endpoint |
| Routing onto edge | authoritative DNS + anycast proxy | DNS CNAME/alias to distribution domain | DNS CNAME/A/AAAA to Fastly | DNS CNAME chain to edge hostname | DNS to endpoint hostname |
| Origin concept | origin behind reverse proxy | origin servers (S3/custom) + origin groups | backends (+ health checks) | origin server/hostname in property rules | origin (Azure or public web server) |
| Cache behavior config | Cache Rules (match → cache settings, custom cache keys) | cache behaviors (path pattern → settings, TTL trio, cache key via headers/cookies/query strings) | VCL/config + Cache-Control semantics | rule tree (matches → behaviors incl. caching) | global + custom caching rules (bypass/override/set-if-missing) |
| Purge/invalidation | purge by URL/host/tag/prefix/everything | invalidation (+ file versioning alternative) | purge (URL/key/tag; stale marking) | Purge Cache product | purge by URL/wildcard/root/all per endpoint |
| Config deployment | rules versioning (Version Management); zone-level settings | distribution config propagated to all edge locations | service versions: clone → activate on production | property versions → activation to staging/production; fast fallback rollback; metadata distributed to network | config changes propagate through network |
| TLS for custom domains | SSL/TLS zone settings (docs read: reverse proxy handles SSL) | cert attached to distribution, SAN proves ownership | TLS subscriptions, ACME verification | edge certificates prepared before property setup | HTTPS custom domain support |
| Analytics/monitoring | zone monitors security & performance (indirect) | CloudWatch metrics + console graphs + alarms | observability dashboards + alerts | CP-code-based traffic tracking/billing/reporting | diagnostics logs |
| Access control on config | account members; zone vs account scope | AWS IAM (implied; not fetched) | account access management | groups with roles per property | Azure subscription/RBAC (implied) |
| Access control on content | (WAF/rate limiting products adjacent) | signed URLs/cookies + trusted signers; geo restrictions (settings list) | ACLs, rate limiting | security products/modules on edge | geo-filtering |
| Interfaces | dashboard, API, Terraform | console, API, CLI (implied), IaC | web, CLI, API, VCL/Compute code | Control Center UI, PAPI, Terraform, CLI, IDE plugins, Postman, bulk ops | portal, ARM/API |
| Edge compute extension | Workers (account-level product) | CloudFront Functions / Lambda@Edge | Fastly Compute (Wasm) | EdgeWorkers | (Front Door direction) |
| Multi-tenant machinery | (account/zone model) | CloudFront SaaS Manager (multi-tenant distributions + tenants) | — | hostname buckets (thousands of domains) | — |

### Stable cross-product structure (candidate canonical model)

1. A managed delivery configuration object per site/app/API (zone / distribution / service / property / endpoint) that binds customer hostnames to content origins and carries delivery behavior. — All five.
2. A provider-operated global edge network (POPs) as the deployment target; configuration is propagated to the network, not run locally. — All five (explicit in CloudFront, Akamai, Azure; structural in Cloudflare/Fastly).
3. DNS-level routing integration that directs end-user traffic for the customer's hostnames onto the edge network (CNAME/alias/anycast/proxied records). — All five.
4. Cache behavior control: rules or settings deciding what is cached, for how long (TTL), and keyed on what (URL/headers/cookies/query strings). — All five.
5. Cache purge/invalidation as an operator action. — All five.
6. TLS/certificate machinery for serving custom hostnames over HTTPS, with domain-ownership verification. — CloudFront, Fastly, Akamai, Azure explicit; Cloudflare structural (reverse proxy terminates SSL; SSL/TLS zone settings exist).
7. Configuration versioning with controlled activation (and in several products staging vs production + rollback). — Fastly, Akamai explicit; Cloudflare (rules versioning), CloudFront (config propagation), Azure (propagation) weaker forms.
8. Operational visibility: traffic/cache/error analytics, logs, alerts. — All five (Cloudflare indirect).
9. Multi-surface management: web console + API, commonly CLI and Terraform/IaC. — All five (console+API universal; CLI/IaC common).
10. Account/organization hierarchy with roles governing who can change what. — Akamai explicit; Cloudflare explicit (accounts/members); others implied by cloud IAM.

### Common but not defining (L1 candidates)

- Origin resilience machinery: origin groups/failover, health checks, shielding/mid-tier caches (CloudFront regional edge caches, Fastly shielding).
- Content access controls: signed URLs/cookies, geo restrictions, hotlink/rate protections.
- Edge security bundling: WAF, DDoS protection, bot management — bundled in some products (Cloudflare zone proxy), separate products/modules in others (Fastly Next-Gen WAF, Akamai security products).
- Edge compute extension (Workers / Functions+Lambda@Edge / Compute / EdgeWorkers).
- Multi-tenant/SaaS delivery machinery (CloudFront SaaS Manager, Akamai hostname buckets).
- Media/streaming specialization (Akamai Adaptive Media Delivery, CloudFront MediaPackage/Smooth Streaming settings).
- Rule templates, includes/shared config, bulk operations (Akamai; Cloudflare templates).

### Variant / optional (L2 candidates)

- Configuration philosophy: declarative rule UI (Cloudflare, Azure) vs code-defined config (Fastly VCL/Compute) vs enterprise rule-tree with contract-gated behaviors (Akamai) vs cloud-native resource model (CloudFront).
- Business model: freemium self-serve tiers (Cloudflare), pay-per-use (CloudFront, Fastly), contract/product-gated enterprise (Akamai), cloud-subscription (Azure).
- Convergence posture: CDN merging into broader edge/application delivery platforms (Azure CDN → Front Door; Cloudflare's platform breadth; Akamai's edge portfolio).
- Deployment scope: standalone CDN service vs module of a cloud platform vs part of a connectivity/edge platform.
- Regional/market variants: China-market CDNs and regional providers were not sampled; the definition is provider-agnostic and should hold (config object + edge network + DNS routing + cache control), but their consoles were not verified.

### Vendor-specific (L3 — keep out of final doc)

- Cloudflare: plan-tiered purge rate limits/bucket sizes and Cache Rule counts; purge-by-cache-tags; Version Management product naming; CDN-Cache-Control extension.
- CloudFront: default TTL values (86400s default / 31536000s max defaults), path-pattern length (255 chars), invalidation pricing beyond free quota, domain-fronting 421 behavior, SaaS Manager naming, `d*.cloudfront.net` naming.
- Fastly: "~150ms" global purge claim; VCL specifics (clustering, segmented caching); `manage.fastly.com`/`api.fastly.com` surfaces; `.fastly-validations.com` ACME CNAME; TLS configuration IDs.
- Akamai: CP codes; `.edgesuite.net`/`.edgekey.net` edge hostnames; XML metadata format; 5-level rule tree depth; fast fallback; hostname buckets; contract/product/module gating; PAPI bulk operations.
- Azure: 7-day default TTL; `*.azureedge.net` naming; 260-char path / 50-extension rule limits; retirement dates (Edgio Jan 2025; Microsoft classic Sep 2027); profile/endpoint subscription limits.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

CDN Management is the operator-facing control plane of a CDN service. Minimal structure without which the Type is unrecognizable:

1. **Delivery configuration object** — a managed per-property configuration (zone/distribution/service/property/endpoint) binding customer hostnames to content origins and defining edge delivery behavior.
2. **Provider-operated edge network as deployment target** — the configuration is propagated to a global network of edge locations run by the CDN provider; operators configure, they do not run the edge servers.
3. **DNS-level traffic routing integration** — the customer's hostnames are directed onto the edge network via DNS machinery (CNAME/alias/anycast/proxied records).
4. **Cache control** — operator-defined cache behavior (what to cache, how long, keyed on what) plus the ability to purge/invalidate cached content.

Remove the delivery configuration object → nothing is managed. Remove the provider edge network → it's a self-hosted cache/reverse proxy, not CDN management. Remove DNS routing integration → traffic never reaches the edge (the config is inert). Remove cache control → it's generic traffic routing (load balancer management), not a CDN.

### L1 — Common Mature Structure

- TLS/certificate management for custom hostnames (managed issuance, upload, ownership verification via SAN/ACME).
- Operational analytics: traffic volume, cache hit/miss, error rates, per-geo/per-CP-code breakdowns; logs; alerts.
- Origin machinery: multiple origins, origin groups/failover, health checks, origin shielding / mid-tier caches.
- Rule-based configuration: ordered match→behavior evaluation; rule templates; shared/reusable config fragments.
- Configuration versioning with activation discipline (staging/production, rollback where offered).
- Multi-surface management: console + API, commonly CLI and Terraform/IaC.
- Organizational access control over the configuration (accounts, groups, roles).
- Content access controls: signed URLs/token auth, geo restrictions.

### L2 — Variant / Optional Structure

- Configuration philosophy (declarative rules vs code-defined config vs enterprise rule tree vs cloud resource model).
- Edge compute extension (edge functions/Wasm) — drift toward edge application platform.
- Edge security bundling depth (WAF/DDoS/bot as bundled capability vs separate products).
- Multi-tenant/SaaS delivery machinery.
- Media/streaming specialization.
- Business model and onboarding posture (self-serve freemium / usage-based / contract-gated).
- Convergence into broader edge/application-delivery platforms.

### L3 — Vendor-specific

See Vendor-specific list above. None of these enter the final document.

### Anti-overfitting check (historical / market-sample)

- Would older CDNs fit? Early CDN-era products were sales-led with vendor professional services configuring delivery; the defining structure (config object + edge network + DNS routing + cache control) still holds — the console/API is the modern surface form, not the definition. The definition does not require self-serve.
- Would regional CDNs (e.g., China market) fit? Structurally yes (same four invariants), though consoles were not fetched — noted as uncertainty, not asserted.
- Would platform-embedded CDNs fit? When a deployment platform (e.g., a hosting platform) fully abstracts the CDN away, there is no CDN Management surface for the end user — that is a different Type (deployment/hosting platform); the CDN Management Type requires an operator-facing control surface.
- Phone-number-style overfit risk: none observed; the sampled products span four configuration philosophies and the L0 avoids naming any of them (no "zone", no "distribution", no "property" in the definition).

## Boundary Findings

- **vs DNS & DHCP Management (§14 sibling)**: DNS management's managed object is the DNS zone and its records. CDN management *uses* DNS as a routing integration (CNAME the hostname to the edge) but its managed object is the delivery configuration and cache behavior. Test: remove the delivery/caching configuration and keep DNS → you have DNS management; remove DNS record editing and keep delivery config → still CDN management (CloudFront customers often keep DNS elsewhere).
- **vs Load Balancer Management (§14 sibling)**: LB management balances traffic across customer-controlled backends; CDN management's defining act is edge caching of content with TTL/purge semantics. Overlap is real (both route, both health-check, both fail over — Fastly documents load balancing inside its CDN service; Cloudflare lists Load Balancers as a zone-level product). Test: remove caching/purge → traffic-management product; keep caching → CDN.
- **vs Network Monitoring / Infrastructure Monitoring (§14 siblings)**: monitoring observes infrastructure; CDN management configures and operates delivery. Analytics is a capability inside CDN management, not the whole. Test: remove configuration/activation/purge → monitoring dashboard.
- **vs DDoS Protection Platform / WAF (§15)**: security products' managed object is threats/policies; CDN management's is delivery configuration. Edge security is bundled (Cloudflare) or modular (Akamai/Fastly). Test: remove delivery config and caching → security platform riding the same edge.
- **vs Cloud Management Platform (§14)**: CMP manages heterogeneous cloud resources; CDN management is specific to content delivery over one provider's edge. Test: scope of managed objects.
- **vs Content Distribution Platform (§27)**: false friend — that Type is media/entertainment-domain distribution of content to channels/platforms (publishing semantics), not edge-caching infrastructure control.
- **vs Serverless Management Platform / edge compute**: edge functions are an extension capability of CDN platforms; when compute becomes the primary object (code deployment, not delivery config), it's the edge/serverless Type.
- **vs Storage Management**: origin storage is an integration point (S3 origins, Azure Storage origins); storage management manages the stores, CDN management manages delivery from them.
- **"去掉什么就变成另一个 Type" 判据**: remove cache control (rules+purge) → load balancer / traffic management; remove the provider edge network → self-hosted reverse proxy config; remove the delivery config object → DNS management or monitoring; remove everything but security policy → WAF/DDoS platform.

## Uncertainties

- Third-party multi-CDN management/steering tooling exists as a market category (multi-CDN traffic steering across providers) but was not researched; no claims made. If the directory ever needs it, it is likely a distinct Type or a Variant of global traffic management — flagged for future review.
- Cloudflare analytics surface was evidenced only indirectly ("use your zone to monitor security and performance"); analytics product pages not fetched. Final doc keeps Cloudflare analytics at capability level.
- CloudFront CLI/IaC evidence was not directly fetched (console/API documented); CLI/IaC claims kept at "commonly" strength.
- Akamai activation/rollback detail rests on the key-concepts page (fast fallback described there); deeper activation docs not fetched.
- Regional CDN markets (China, etc.) not sampled; definition believed to hold but unverified.
- Azure CDN is documented as a market in transition (classic retiring toward Azure Front Door); the profile/endpoint model evidence is from the classic-era docs, which remain the clearest statement of the standard cloud-CDN shape.

## Final Synthesis

CDN Management is the operator-facing control plane of a content delivery network service. Its defining core is a four-part structure: (1) a managed delivery configuration object binding customer hostnames to content origins with edge delivery behavior; (2) a provider-operated global edge network as the deployment target for that configuration; (3) DNS-level routing integration that puts customer hostnames on the edge; (4) cache control — operator-defined cache behavior plus purge/invalidation. Around this core, mature products add TLS/certificate management, operational analytics, origin resilience machinery, rule-based configuration with versioned activation, multi-surface management (console/API/CLI/IaC), organizational access control, and content access controls. Products differentiate on configuration philosophy (declarative rules vs code-defined config vs enterprise rule trees), business model, edge-security bundling, edge compute extension, and convergence into broader edge platforms. The Type is distinct from DNS management (different managed object), load balancer management (no caching semantics), monitoring (observe vs operate), security platforms (threats vs delivery), and the media-domain Content Distribution Platform (§27 false friend).
