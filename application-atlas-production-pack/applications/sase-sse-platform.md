# SASE / SSE Platform

## Overview

A **SASE / SSE Platform** is a cloud-delivered security platform that intercepts user traffic — both user-to-internet/SaaS and user-to-private-application — at vendor-operated points of presence distributed around the world, and enforces a converged set of security services on that traffic under a single policy and management plane keyed to user identity and device context.

The defining core is small:

```text
User traffic (internet/SaaS + private apps)
  → steered to vendor-operated cloud points of presence
    → enforced by converged security services
      → under one policy plane binding identity + device context + destination
```

Three properties hold the type together. Remove any one and it stops being this type:

- **Cloud-edge mediation** — user traffic actually flows through the platform's cloud points of presence (reached via a client agent, a site edge device or tunnel, or a proxy/DNS configuration). Without this, the product is an on-premises security stack or an API-side tool with no traffic path.
- **Converged services under one control plane** — multiple security services (web security, private-application access, cloud app control, data protection, firewall) are delivered and administered as one platform with unified policy and logging. Without this, the product is a portfolio of point products — a standalone secure web gateway, a standalone ZTNA.
- **Identity- and context-based policy** — enforcement decisions bind who the user is (from the enterprise identity provider), the state of their device, and what they are reaching — not merely a network address. Without this, the product is a network firewall moved to the cloud.

The market uses two names for the same platform at two packaging tiers: **SSE** (Security Service Edge) is the converged security service set; **SASE** (Secure Access Service Edge) is SSE plus SD-WAN and site networking on the same platform. Vendors' own materials treat them as one category with two scopes — one major vendor labels SASE "security and network convergence" and SSE "security convergence" in the same navigation; another defines SASE as "an architectural model that unifies enterprise networking services with Zero Trust security."

The platform's standing enemy is the legacy model it replaces: VPN concentrators for remote access, and stacks of firewalls, web proxies, and point appliances at the network perimeter. "Replace the VPN" and "retire the appliance stack" are explicit, universal use cases.

## Users & Context

**Primary users are security and network administrators** in organizations that have adopted cloud applications and hybrid work:

- the security admin writes policy: which users, from which devices, may reach which internet destinations, cloud applications, and private applications, and what inspection applies;
- the network admin owns connectivity: how sites and users are steered to the platform (agents, tunnels, edge devices), routing, and egress addresses;
- the security operations analyst consumes the visibility plane: logs, events, incidents, analytics.

**End users are enforced upon, not operated on.** Their experience of the platform is deliberately thin: a client agent (often invisible when on a managed device), an authentication prompt redirected to the company's identity provider, and block or isolation pages when policy denies something. There is no user-facing workspace to learn.

**Secondary stakeholders**: the CISO/procurement side buys the platform for consolidation (fewer appliances, fewer point products, one policy language); managed service providers deliver it to their own customers; third parties and contractors are granted access to specific private applications without joining the corporate network.

Typical context: a workforce distributed across offices, homes, and travel; business applications that are SaaS or hosted in private data centers/clouds; branch offices; and a mix of managed and unmanaged (BYOD) devices. The platform is bought precisely because the old assumption — users, apps, and data inside one network perimeter — no longer holds.

## Core Model

The platform's world consists of six structures organized around two traffic domains.

### Two traffic domains

Everything else exists to serve one of two flows:

1. **Internet / SaaS access** — the user reaches public web destinations and SaaS applications; the platform filters, inspects, and controls that traffic (the secure-web-gateway family of services, plus cloud-app control and data protection).
2. **Private application access** — the user reaches applications hosted in the organization's own data centers or clouds; the platform authenticates the user and brokers a per-application connection (the zero-trust-network-access family).

Mature platforms treat both domains with the same policy language, the same identity sources, and the same logging.

### The six structures

**1. Points of presence (the cloud edge).** Vendor-operated, geographically distributed sites where traffic is actually processed. Architectures differ — some vendors run a private dedicated backbone between their PoPs, others run enforcement on a large public global network, others on a multicloud footprint — but in every case enforcement happens in the vendor's cloud, close to the user, not on a customer-owned appliance.

**2. On-ramps (how traffic gets there).** The mechanisms that steer user traffic into the platform:

- a **client agent** installed on managed devices — the primary, full-coverage on-ramp in every researched platform;
- a **site edge device or network tunnel** (SD-WAN appliance, IPsec/GRE tunnel) that connects a branch office or data center and carries all its traffic;
- **agentless configurations** — a DNS resolver setting, or a browser/proxy (PAC-file) configuration — that cover unmanaged devices or serve as a low-friction first rollout, at the cost of enforcing fewer policy layers.

The on-ramp determines what can be enforced: a DNS-level on-ramp can only filter name resolution; a full client can route everything through DNS, network-layer, and application-layer inspection.

**3. Security services (the converged set).** The services enforced on mediated traffic:

- **Web/internet security (secure web gateway)** — URL and category filtering, DNS filtering, decryption and inspection of encrypted traffic, malware scanning, file sandboxing/quarantine;
- **Cloud application control (CASB, inline)** — discovery and control of SaaS usage, sanctioned vs unsanctioned apps, restrictions such as "corporate tenant allowed, personal tenant blocked";
- **Private application access (ZTNA)** — per-application, brokered connections for hosted apps;
- **Firewall service (FWaaS)** — network-layer filtering by address, port, protocol;
- **Data protection (inline DLP)** — content inspection of traffic in motion to detect and block sensitive data leaving;
- commonly also: **remote browser isolation** or a managed **enterprise browser** (execute risky web code in a cloud browser), **digital experience monitoring**, and **email security** in some bundles.

No single service defines the type; the convergence of several under one plane does. Web security and private access are the two every platform has; the rest are standard but individually optional.

**4. The policy plane.** One rule model applied across services. A policy binds:

- **who** — user and group identity from the enterprise identity provider (SSO), sometimes plus authentication-method requirements (e.g., MFA) or user risk scores;
- **from what** — device posture signals (managed-device membership, disk encryption, OS state, security-software state) and connection properties (country, IP);
- **to what** — destination category, URL, cloud application, or private application;
- **doing what** — the action: allow, block, isolate, or grant with session restrictions (e.g., clipboard and file-transfer controls on a remote session).

Policies are evaluated in a defined order, and private-application access is deny-by-default: nothing is reachable unless a policy allows it.

**5. Private application connectors.** For the private-access domain, a server-side component (a lightweight connector/appliance or outbound tunnel) is installed inside the customer's data center or cloud. It establishes an outbound-only connection to the platform's edge. This is what makes the defining ZTNA property possible: applications are never exposed to the public internet, and users are connected to specific applications — never to the network itself, which eliminates lateral movement.

**6. The visibility plane.** Every enforced decision produces records: traffic logs, security events, threat verdicts, data-protection matches, session metadata. Mature platforms add analytics over these records, digital-experience monitoring (is the user's path to apps slow or broken?), and export/integration into SIEM and SOAR tooling.

```text
Identity provider (IdP)          Device posture signals
        │                                │
        ▼                                ▼
   ┌──────────────── POLICY PLANE ────────────────┐
   │  who + from what + to what → action          │
   └──────────────────────────────────────────────┘
        ▲                    ▲
        │                    │
   user device           private app
   (on-ramp: client /    (server-side connector,
    proxy / DNS /         outbound-only to edge)
    site edge device)
        │                    │
        ▼                    ▼
   CLOUD POINTS OF PRESENCE  ──  security services
   (web security · cloud app control · private access ·
    firewall · data protection · isolation)
        │
        ▼
   visibility plane (logs · analytics · DEM · SIEM export)
```

## How It Works

### 1. Enroll the organization and steer traffic

The administrator connects identities (the identity provider), enrolls devices (installs the client agent, often pushed by endpoint management), and connects sites (deploys an edge device or builds a tunnel). Unmanaged populations may be covered by DNS or proxy configuration instead. From this point, user traffic flows to the nearest platform point of presence instead of backhauling to a corporate data center.

### 2. The internet-access flow

```text
user requests a destination
→ request arrives at the nearest point of presence via the on-ramp
→ policy evaluated layer by layer (DNS first, then network, then application)
→ threat inspection, data-protection inspection on allowed traffic
→ allowed: proxied to the destination; response inspected on the return path
→ blocked: connection refused, user shown a block page; event logged
```

Encrypted traffic is decrypted for inspection by trusting a platform root certificate installed on managed devices. Typical outcomes beyond allow/block: quarantine a suspicious download, isolate a risky site in a remote browser, force the corporate tenant of a SaaS app, or assign a fixed egress IP so partner services recognize the organization.

### 3. The private-access flow

```text
user opens a private application (via client or browser)
→ platform authenticates the user against the identity provider
→ policy evaluated: identity + groups + device posture + the specific app
→ allowed: platform brokers a one-to-one connection to the app
   (via the customer-side connector; the app is never exposed publicly)
→ denied or no policy: nothing is reachable — deny by default
→ session may carry restrictions (e.g., read-only, no clipboard)
```

The structural difference from a VPN is the unit of access: the application, not the network. The user never joins a network, cannot scan laterally, and the connector's outbound-only connection means there is no inbound attack surface to find.

### 4. The policy-authoring loop

The administrator's daily work is a continuous loop: define rules (who/from what/to what/action) → observe enforcement in logs and analytics → tune (new categories, new app definitions, posture requirements) → repeat. Because one policy plane spans services, a single rule can carry identity and posture conditions into web filtering, cloud-app control, and private access alike. Policy changes propagate to the distributed points of presence (one platform documents propagation on the order of a minute).

### 5. The operations loop

Security operations consumes the visibility plane: review events and incidents, hunt in logs, export to SIEM/SOAR, and use analytics to find risky patterns (unsanctioned app adoption, data-protection near-misses, threat trends). Network operations watch the experience side: digital-experience monitoring surfaces whether slowness originates in device, network, or application.

## Interfaces

### Admin console (web)

The platform's center of gravity. Across researched products it consistently contains:

- **Policy editors per service** (web/DNS/network/HTTP rules; private-application definitions and access rules; data-protection rules) sharing common building blocks: identity selectors from the IdP, device-posture conditions, destination/app selectors, and actions.
- **Application and destination inventories** — URL/category databases, cloud-app catalogs, and the customer's own private-application definitions.
- **Device and user inventories** — enrolled devices, posture state, users/groups synced from the IdP.
- **Monitoring and analytics** — traffic and security event exploration, dashboards, threat and data-protection reports.
- **Connectivity management** — on-ramp configuration (client provisioning packages, tunnel/edge-device management), egress IP assignment.
- **Administration** — administrator roles (RBAC), audit logs, integrations (SIEM/SOAR, ticketing, threat intel).

### End-user client agent

A small, mostly silent surface: connection status, the identity-provider login prompt, and notifications when policy blocks or isolates something. On unmanaged devices the same surface may carry the authentication step for browser-based private access.

### Enforcement surfaces the user meets

- **Block pages** with reason and (optionally) a request-for-access path.
- **Authentication redirects** to the company IdP (SSO/MFA) before access — most visibly for private applications and BYOD scenarios.
- **Isolated browsing sessions** — a cloud-rendered browser surface for risky destinations, visually near-native but executing remotely.
- **Restricted sessions** — remote application sessions with disabled clipboard/file transfer for untrusted populations.

## Important Rules / Behaviors

- **Private access is deny-by-default.** A private application is unreachable unless a policy explicitly allows a user (with whatever posture conditions apply). This is the opposite of the network-perimeter model, where being on the network grants reachability.
- **The on-ramp bounds enforcement.** DNS-level on-ramps can only filter resolution; proxy-only on-ramps cover browser traffic; only the full client enforces every policy layer. Administrators choose per population, trading coverage against deployability.
- **Decryption requires device trust.** Inspecting encrypted traffic requires the platform's root certificate on the device. Populations without it (BYOD, some agents) get a reduced inspection posture.
- **Identity is consumed, not owned.** The platform relies on the enterprise identity provider for users, groups, and authentication; it does not maintain its own user directory as the source of truth. Revoking a user in the IdP (ideally via automated provisioning integration) is what cuts access.
- **Posture can be a live condition.** At least one platform documents that device-posture and connection properties are re-evaluated continuously during a session, not only at login — access can effectively lapse when a device stops complying. Where this is not documented, posture is at minimum a login-time condition.
- **Policy evaluation is ordered and first-match.** Rules are evaluated in a defined sequence (documented per product; commonly deny/exception rules ahead of allow rules), and the first matching decision stands.
- **Applications are hidden by design in the private domain.** Connectors dial out to the platform; nothing listens on the public internet. Discovery of private apps by outsiders is not part of the model.
- **Everything is logged.** Enforcement without a record is treated as a defect; the visibility plane is structural, not an add-on.

## Variants

- **SSE-only vs full SASE.** The same platform sold with or without SD-WAN/site networking. Full-SASE packaging (common among firewall- and networking-heritage vendors) adds branch edge devices, site routing, and application-aware WAN handling; SSE-only packaging leaves site networking to other products. This is the primary market segmentation inside the type.
- **Edge architecture.** Private dedicated backbone between PoPs (one pure-play vendor's approach) vs enforcement on a large public global network vs multicloud footprints. Performance and sovereignty implications, not structural differences.
- **Clientless / browser-first access.** Privileged remote access and third-party/BYOD access delivered through the browser without an agent — same policy plane, reduced device coverage.
- **Scale and tier.** Global enterprises buy the full multi-service platform; mid-market deployments often start with one domain (usually internet security or VPN replacement) and expand. At least one platform offers a free tier for small deployments.
- **Bundled adjacents.** Email security, endpoint data protection, SaaS/cloud posture management (API-side products), workload/east-west security, IoT/OT access, and AI-application controls appear as bundled or sibling products depending on vendor; they ride the same console but are not part of the defining core.
- **Delivery variants.** Direct enterprise purchase vs managed-service-provider delivery; regional/sovereign deployments for data-residency requirements; government-cloud variants.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Zero Trust Network Access / ZTNA | component / point-product pole | ZTNA is the private-access service inside the platform. A standalone ZTNA product drops convergence and internet security; the platform adds the other services and the unified plane. |
| Network Security Platform | adjacent, heritage overlap | Firewall-centric and typically appliance/on-premises; policy keyed to network address rather than identity and context. The firewall service inside this platform is the shared capability; delivery and policy model differ. |
| Data Loss Prevention / DLP | capability inside + standalone pole | Standalone DLP is one capability without the traffic-mediation platform. Inside this platform, DLP is an inline service sharing the policy plane. |
| SaaS / Data Security Posture Management (SSPM/DSPM) | API-side sibling | Posture products operate via APIs against SaaS/cloud configurations and never mediate traffic. Some vendors bundle both; the traffic path is the seam. |
| Email Security Gateway | channel-specific adjacent | Mediates only the email channel. Bundled by some platforms; not definitional. |
| Browser Security Platform | surface-specific adjacent | Makes the isolated or managed browser the product itself. Inside this platform, browser isolation is one enforcement mode. |
| Endpoint Protection / EDR | complementary, different locus | EDR protects endpoint internals (processes, files); this platform enforces the network path. Posture checks read endpoint state but do not protect the endpoint. |
| IAM / SSO | upstream dependency | The identity provider issues and manages identity; this platform consumes it for enforcement decisions. |
| CDN / Cloud Management Platform | different object of work | CDNs accelerate published content; cloud management operates cloud resources. This platform mediates *user* traffic for security policy. Vendor heritage overlap (a CDN company selling SASE) does not merge the types. |

The most important boundary is with **ZTNA**: every platform here contains a ZTNA service, and ZTNA-only products exist in the market. The test is convergence — one traffic path, one policy plane, multiple services — not the presence of any single service.

## Representative Products

- **Zscaler** (Zscaler Internet Access + Zscaler Private Access) — the SSE archetype; security-first cloud proxy; private access built on brokered user-to-app connections.
- **Netskope** (Netskope One) — CASB heritage; SSE leader packaging security convergence, with SD-WAN for full SASE.
- **Cloudflare One** — network/CDN heritage; SASE platform on a public global network with a unified Zero Trust dashboard; free tier exists.
- **Prisma SASE / Prisma Access** (Palo Alto Networks) — firewall heritage; enterprise SASE combining the SSE service set with SD-WAN on a multicloud architecture.
- **Cato Networks** — full-SASE pure-play; networking and security converged on a private backbone with site edge devices and a user client.

The defining core was checked across all five; the SASE-vs-SSE packaging axis, on-ramp variety, and bundled-adjacent differences were checked to avoid defining the type by any one vendor's portfolio.

## Sources

Research date: **2026-09-09**

- Zscaler — ZIA product page: https://www.zscaler.com/products/zia ; ZPA product page: https://www.zscaler.com/products-and-solutions/zscaler-private-access
- Netskope — Products: https://www.netskope.com/products ; SSE: https://www.netskope.com/products/security-service-edge ; documentation portal index: https://docs.netskope.com/
- Cloudflare — Cloudflare One docs: https://developers.cloudflare.com/cloudflare-one/ ; Access policies: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/ ; Gateway traffic policies: https://developers.cloudflare.com/cloudflare-one/traffic-policies/
- Palo Alto Networks — Prisma SASE: https://www.paloaltonetworks.com/sase
- Cato Networks — Knowledge Base: https://knowledge.catonetworks.com/ ; "Welcome to Cato Networks": https://knowledge.catonetworks.com/docs/welcome-to-the-cato-service

> Sourcing limitations: Zscaler's operational help center and Netskope's documentation article bodies are JavaScript-rendered and could not be fetched; observations for those vendors rest on official product pages and documentation indexes, so operational specifics (on-ramp enumerations, default settings, numeric limits) are deliberately not stated. Palo Alto Networks observations are roster-level (marketing page only). Gartner Magic Quadrant positioning is recorded only as vendor claims. Detailed product-by-product observations and the cross-product comparison are in the paired Research Notes.
