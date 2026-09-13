# Research Notes — Zero Trust Network Access / ZTNA

## Research Goal

Understand what a Zero Trust Network Access product actually is and how it works, from real products: what the unit of access is, what objects exist inside the system, how a user gets access to a private application, how applications are connected without being exposed, what admins and end users actually do, and where the Type's boundaries lie (vs VPN, vs SASE/SSE platform, vs IAM/SSO, vs PAM, vs network security / microsegmentation, vs service mesh).

## Initial Boundary

Initial hypothesis (before research): ZTNA is a security access service that grants identity-based, policy-controlled access to specific private (internal, non-public) applications, brokering per-application connections so that applications are never exposed to the network — replacing network-level VPN access.

Neighboring Types to test:
- SASE / SSE Platform (§15 sibling, processed 2026-09-09) — left a delegated test for this pass
- VPN (not a directory leaf, but the category's standing enemy — must be documented)
- IAM / SSO (§15) — authentication vs connection path
- Privileged Access Management / PAM (§15) — privileged sessions vs workforce access
- Network Security Platform / microsegmentation (§15) — network-level vs user-to-app
- Service Mesh Management (§14) — east-west service identity vs user-to-app
- Browser Security Platform (§15) — clientless browser access mode vs browser-as-product
- Endpoint Management / UEM (§14) — posture signals consumed, not device management

## Research Questions

1. What is the unit of access — application, resource, network segment?
2. What objects exist? (applications/resources, policies, connectors/gateways, clients, identities, devices)
3. How does a user get access? (authentication → policy evaluation → connection establishment)
4. How are applications connected without being exposed? (connector/gateway placement, outbound connections, cloaking)
5. What is deny-by-default in practice?
6. What do admins configure, and in what console?
7. What do end users see and do? (client, browser, app launcher)
8. Is device posture definitional or common?
9. What connection substrates exist? (cloud-brokered, direct-routed, mesh overlay)
10. Where exactly is the seam vs SASE/SSE (delegated test), vs VPN, vs SSO, vs PAM?

## Representative Products

Selected for market representation + documentation quality + different product philosophy + different customer tiers + different connection substrates:

1. **Zscaler Private Access (ZPA)** — the category-defining enterprise ZTNA; cloud-brokered substrate; component of the Zscaler Zero Trust Exchange (SASE) platform; global-enterprise tier.
2. **Cloudflare Access** — cloud-native identity-proxy ZTNA on a public global network; excellent Tier-1 developer documentation; all-sizes tier (free tier exists); component of Cloudflare One.
3. **Twingate** — standalone pure-play ZTNA; SMB/mid-market + MSP tier; Controller/Client/Connector/Relay architecture; Tier-1 documentation.
4. **Tailscale** — mesh-overlay substrate (WireGuard peer-to-peer), developer/IT tier; positions itself against VPN, SASE, AND PAM — a deliberate boundary pole.
5. **AppGate ZTNA** — standalone pure-play with Software-Defined Perimeter heritage; direct-routed (non-cloud-routed) substrate; enterprise/federal tier; supports fully isolated (no-vendor-cloud) deployment — the historical/off-cloud anchor.

## Sources

Fetched 2026-09-09:

- Cloudflare — Access policies: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/ (Tier 1, full text)
- Cloudflare — Access controls index: https://developers.cloudflare.com/cloudflare-one/access-controls/ (Tier 1)
- Cloudflare — Applications index: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/ (Tier 1)
- Cloudflare — Publish a self-hosted application: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/ (Tier 1, full text)
- Cloudflare — Secure a private IP or hostname: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/ (Tier 1, full text)
- Twingate — docs index: https://www.twingate.com/docs/ (Tier 1)
- Twingate — How Twingate Works: https://www.twingate.com/docs/how-twingate-works (Tier 1, full text)
- Twingate — Resources: https://www.twingate.com/docs/resources (Tier 1, full text)
- Twingate — Understanding Connectors: https://www.twingate.com/docs/understanding-connectors (Tier 1, full text)
- Twingate — Twingate vs. VPNs: https://www.twingate.com/docs/twingate-vs-vpn (Tier 1, full text)
- Tailscale — docs index: https://tailscale.com/kb/1152/ztna (Tier 1)
- Tailscale — What is Tailscale: https://tailscale.com/docs/concepts/what-is-tailscale (Tier 1, full text)
- Zscaler — ZPA product page: https://www.zscaler.com/products-and-solutions/zscaler-private-access (Tier 2)
- AppGate — homepage: https://www.appgate.com/ (Tier 2)
- AppGate — How AppGate ZTNA Works: https://www.appgate.com/products/zero-trust-network-access/how-it-works (Tier 2, incl. FAQ)

Unreachable / degraded:
- Zscaler help portal (help.zscaler.com) — JavaScript-rendered, returns "enable JS" page (×1 attempt; consistent with the sase-sse-platform pass finding). ZPA evidence held at product-page (Tier 2) strength.
- AppGate product URLs /products/software-defined-perimeter and /products/sdp — 404 (×1 each); correct path discovered via homepage nav.
- Zscaler Zpedia /zpedia/what-is-ztna — 404 (×1).
- AppGate support/docs portal (support.appgate.com) — not fetched (time budget); AppGate evidence held at product-page strength.

## Product A — Zscaler Private Access (ZPA)

### Key observations (evidence layer A — official product page)

- Positioning: "Zscaler Private Access™ (ZPA) offers seamless zero trust connectivity for all users, with AI-powered user-to-app segmentation and context-aware policies. The world's most deployed ZTNA solution, ZPA can replace legacy tools like VPNs and VDI."
- Defining sentence: "ZPA brokers direct, one-to-one connections between authorized users and specific apps. Unlike with a VPN, users never access the corporate network, and apps are never exposed to the public internet."
- Problem framing (the standing enemy): "VPNs are exposed to the public internet for remote access by design, creating a massive attack surface. They also give users direct network access, allowing lateral movement and unauthorized access when implemented without complex segmentation rules."
- Capability roster: AI-powered app segmentation; workload-to-workload segmentation; privileged remote access (clientless RDP/SSH/VNC to production systems); browser access (lightweight, infrastructure-agnostic, paired with browser access); Private Service Edge (ZTNA for on-premises users); business continuity; extranet application support (partner-hosted apps); digital experience monitoring; AppProtection (L7 inspection of private app traffic); full inline inspection; DLP; browser isolation.
- Use cases: VPN alternative; hybrid work/business continuity; BYOD and third-party access; replace legacy VDI; OT connectivity; microsegmentation (user-to-app and app-to-app); partner-network apps.
- Platform context: ZPA is one service inside the Zscaler unified platform ("Zero Trust Exchange") alongside ZIA (internet access), Zero Trust Branch, Zero Trust Cloud, ZDX, browser isolation, firewall, etc. — the component-vs-platform relationship, from the component side.
- Customer tier: global enterprise (Siemens 360,000 employees; PTC; Deutsche Börse).
- Note: operational mechanics (App Connector deployment, app segment configuration) live in the JS-blocked help portal — not asserted here.

## Product B — Cloudflare Access

### Key observations (evidence layer A — official developer docs)

- Model: "Cloudflare Access determines who can reach your application by applying the Access policies you configure." Applications are first-class objects: self-hosted (public hostname), self-hosted private (private IP/hostname + port), SaaS, bookmarks, non-HTTP/infrastructure (SSH).
- Deny-by-default, explicit: "All Access applications are deny by default — a user must match an Allow policy before they are granted access." Also: "Since Access is deny by default, users who do not match a Block policy will still be denied access unless they explicitly match an Allow policy."
- Policy structure: Actions (Allow / Block / Bypass / Service Auth) × rule types (Include = OR, Exclude = NOT, Require = AND) × selectors (emails, email domains, IdP groups, SAML/OIDC attributes, country, IP ranges, device posture, client connectivity (WARP/Gateway), valid certificate, service token, user risk score, login method, authentication method/MFA).
- Continuous evaluation: "Non-identity attributes are polled continuously, meaning they are evaluated with each new HTTP request for changes during the user session." SCIM revocation in the IdP can force re-attestation of all attributes.
- Ordered, first-match evaluation: Bypass and Service Auth first, then Block and Allow, top to bottom; "Once a user matches an Allow or Block policy, evaluation stops."
- Session: application token checked on every HTTP request; session duration configurable; re-authentication on expiry.
- Connection context (per-policy session restrictions): clipboard controls and file-transfer controls for browser-based RDP; allowed UNIX usernames for SSH infrastructure apps.
- Connection path: Cloudflare Tunnel (cloudflared daemon) connects the origin to Cloudflare; "Only users who match your Access policies will be granted access." Ordering warning: "If you do not have an Access application in place, the published application will be available to anyone on the Internet" — the Access application must exist before the tunnel route. Origin-side token validation ("Protect with Access") guards against bypass.
- Private-network model: private IP/CIDR + port, or private hostname + port, reached over the Cloudflare One Client / Cloudflare WAN / browser isolation; local domain fallback routes private hostnames to the custom resolver; non-HTTP apps authenticate via a client notification that opens the browser login.
- Clientless access: "Allow clientless access — users who pass your Access policies will see a tile in their App Launcher which points to a prefixed URL... route traffic through Clientless Web Isolation. This setting is useful for users on unmanaged devices or contractors who cannot install a device client."
- Machine access: Service Auth policies with service tokens or mutual TLS ("enforce authentication flows that do not require an identity provider IdP login").
- User surfaces: App Launcher (tiles for available apps), Access login page (IdP redirect, instant-auth option), block pages (default message / redirect / custom template).
- Platform context: Access is one service of Cloudflare One (Zero Trust dashboard); Gateway (traffic policies: HTTP/network/DNS/egress) is the internet-security sibling; TLS decryption, remote browser isolation, Magic WAN are platform siblings.

## Product C — Twingate

### Key observations (evidence layer A — official docs)

- Architecture (four components): **Controller** (Twingate-hosted, multi-tenant; stores admin-console configuration; delegates user authentication to third-party IdPs; generates signed ACLs for Clients — "the discrete set of Resources that a given user is allowed to access... the 'least privileged access' representation" — and ACLs for Connectors; "traffic can only be forwarded to a Resource if it falls in the intersection set between the two ACLs"); **Client** (installed on user devices; combined authentication and authorization proxy; obtains signed ACL; detects connection requests to protected Resources; proxies DNS and TCP/UDP transparently; establishes certificate-pinned TLS tunnel); **Connector** (deployed behind the firewall of a private Remote Network; maintains outbound connections; verifies inbound Client connections — tunnel integrity, signature, ACL claim — "for every inbound connection request"; performs local DNS resolution); **Relay** (TURN-like; no data stored; connects Client to Connector; peer-to-peer attempted first, relayed as backup).
- The Resource (unit of access): "A Resource can be **any network address** that you wish users to access via Twingate" — FQDN, wildcard FQDN, IP, or CIDR; plus port restrictions (default all TCP/UDP); plus the Remote Network it belongs to; plus access (groups); plus tags; plus client visibility.
- Deny-by-default, explicit: "Twingate denies traffic by default, following Zero Trust principles. If a user has not explicitly been given access to a Resource, they will not be able to connect to it, with network connection requests denied from the user's endpoint device."
- Address resolution is local to Connectors: "name and address resolution of that Resource does not take place on the user's device, but is instead forwarded to the Remote network the Connector resides in."
- Connectors are not VPN gateways: "Connectors should never be accessible from the public internet. Connectors should always reside behind a firewall, *within* the private network"; "Users never choose to connect directly to a Connector"; "Connectors do not ever allow users to join the private network. Instead, Connectors should be seen as narrow keyholes that only allow individual network connections to proceed to the Resources that users are authorized to access"; "sophisticated, centrally-coordinated proxies"; precise split tunneling — only traffic destined to authorized Resources is routed.
- Security policies: Sign In Policy, Resource Policies, Device Posture Checks (incl. third-party EDR/MDM signals: CrowdStrike, SentinelOne, Intune, Jamf, 1Password), Manually Verified Devices, Location Requirements, Native MFA, Sessions.
- Dynamic access: JIT Access Requests (request → review → grant), Ephemeral Access, usage-based auto-lock.
- Visibility: audit logs (schema, admin-console export, S3 sync), network events, user activity, device reports.
- Workload access: headless clients (Linux/Windows), CI/CD configurations, userspace networking, Kubernetes access.
- Adjacent product lines (separate doc sections, not the private-access core): Identity Firewall; Privileged Access for Kubernetes / SSH / Web Apps; Internet Security (DNS filtering, DoH, exit networks).
- Boundary self-articulation: dedicated docs "Twingate vs. VPNs" and "Twingate vs. Mesh VPNs".
- vs VPNs (vendor's own framing): "With VPNs, user access is granted to the entire network... Twingate allows access to be granted on a per application basis"; least privilege; "an attacker's access is limited to specific apps, and they cannot move laterally... In fact, the network isn't even visible to an attacker"; "With Twingate, you don't need to install a public gateway, so no network resources are publicly exposed on the internet and your network stays hidden... Twingate connectors are installed inside your hidden network, and these facilitate outbound connections to authorized users"; rich contextual authorization (SSO/MFA identity, physical location, time of day, device posture, risk score); centralized visibility + SIEM integration.
- Customer tier: SMB/mid-market; MSP program (customer networks, MSP billing); free/personal tier ("Twingate Home").

## Product D — Tailscale

### Key observations (evidence layer A — official docs index + concept page)

- Self-positioning: "Tailscale is a Zero Trust identity-based connectivity platform that replaces your legacy VPN, SASE, and PAM and connects remote teams, multi-cloud environments, CI/CD pipelines, Edge & IoT devices, and AI workloads."
- Substrate: "Tailscale creates a peer-to-peer mesh network (known as a tailnet)... enables encrypted point-to-point connections using the open source WireGuard protocol, which means only devices on your private network can communicate with each other." Coordination server distributes keys/policy; data flows peer-to-peer ("avoids centralization where possible").
- Access control: "access control policies" (ACLs) as the managed policy surface; default ACL exists (docs reference an "allow-all default ACL" sample — default posture not asserted further this pass).
- Network extension features: subnet routers ("give devices outside your local network access to services within specific subnets"), exit nodes ("route all internet traffic through a specific device" — VPN-like mode, explicitly offered).
- Use cases: business VPN replacement; PAM ("Enable Zero Trust with just-in-time access and robust recording"); workload connectivity (pipelines, apps, Kubernetes); CI/CD; edge/IoT; AI governance.
- Boundary relevance: Tailscale claims the ZTNA job (identity-based access to private resources) over a mesh substrate rather than a brokered proxy, and explicitly claims to replace SASE and PAM — the drift-zone pole for both seams. It is retained in-sample as the mesh-overlay variant/boundary pole, not as the center of the Type.

## Product E — AppGate ZTNA

### Key observations (evidence layer A — official product pages; Tier 2)

- Positioning: "Industry-leading Zero Trust Network Access (ZTNA) enforces identity-based policies to secure access across users, devices, and workloads." "The only direct-routed ZTNA solution built for peak performance... Point-to-point access. No cloud detours." "Cloaked Infrastructure — Invisible… until trust is validated."
- SDP heritage: case-study URLs reference "appgate-sdp" (Nequi, Reltio); customer logo wall includes "Software Defined Perimeter WW"; FAQ: "Is AppGate ZTNA a VPN? No. Software-defined perimeter architectures are very different from VPNs. VPN has been traditionally used to provide remote workers with access to corporate resources, its only real security features are user authentication to the network. In comparison, AppGate ZTNA is fundamentally an identity-centric and security-driven solution..."
- Components ("the AppGate ZTNA collective"): **Controller** ("the policy engine and decision point (PDP). It manages the authentication, policies, conditions and entitlements granting access for all users, devices and workloads"); **Gateway** ("the policy enforcement point (PEP). Gateways control the flow of access to protected resources. It dynamically builds session-based microfirewalls or microperimeters based on granted entitlements that limit lateral movement and attack surface"); optional roles: **Connector** (branch office and IoT/OT enforcement), **Portal** (clientless, browser-based access), **Log Server** (ELK-based aggregation), **Log Forwarder** (to enterprise SIEM/syslog).
- Single Packet Authorization (SPA): "uses proven cryptographic techniques to make internet-facing resources invisible to unauthorized users... Only devices that have been seeded with the cryptographic secret will be able to generate a valid SPA packet, and subsequently be able to establish a network connection. This in essence is how SPA reduces the attack surface and makes the infrastructure invisible to adversarial reconnaissance."
- Microperimeters: "individual just-in-time session-based 'micro' firewalls or 1-1 connections between users and the resources they are authorized to access behind a gateway... These microperimeters provide least privilege access and reduces the attack surface."
- Deployment models (critical for abstraction): **Cloud Hosted** ("your controller is hosted in the Zero Trust platform cloud environment, but other appliances remain hosted in your controlled environment"); **Self Hosted** ("all AppGate ZTNA appliances are deployed in your controlled environment"); **Isolated** ("all AppGate ZTNA appliances are deployed in your controlled environment with no connection to the Zero Trust platform") — a full ZTNA deployment with NO vendor cloud.
- Connection security: "all traffic from the client to the gateway travels across a secure, encrypted network tunnel... mTLS FIPS 140-2 compliant... on every connection."
- Bidirectional rules: supports both "up rules" (user/device → resource) and "down rules" (resource → user device; remote desktop support, EPP/EDR/AV, VoIP).
- Access options: "Select from client- or browser-based access options."
- Use cases: secure remote access (VPN replacement); agentic AI workloads; server-initiated connectivity; branch/site connectivity; OT/IoT; SaaS application access; workload-to-workload communication.
- Adjacent products: Risk Sentinel (adaptive risk scoring), Application Discovery (AI discovery + entitlement recommendations).
- Customer tier: enterprise + federal/government (US Air Force, GSA, US Marine Corps logos; Federal Division; state/local government/education).

## Cross-product Comparison

| Dimension | ZPA | Cloudflare Access | Twingate | Tailscale | AppGate ZTNA |
|---|---|---|---|---|---|
| Unit of access | specific apps (app segments) | Access application (public hostname / private IP+port / private hostname) | Resource (address + ports + remote network) | node/resource governed by ACLs | resource behind a Gateway |
| Deny-by-default | least-privileged user-to-app (explicit) | explicit ("deny by default") | explicit ("denies traffic by default") | ACL-governed (policy-based) | entitlement-based + SPA cloaking |
| Identity source | enterprise IdP (context-aware policies) | IdP login (many IdPs; instant-auth option) | delegated to third-party IdP | identity-based (SSO) | IAM / directory integration |
| Device posture | context-aware policies | posture-check selectors (own + third-party) | device posture checks (own + EDR/MDM) | device posture features | posture checking |
| Enforcement component near apps | App Connector (outbound; per sase-pass + product page) | Cloudflare Tunnel (outbound daemon) | Connector (behind firewall, outbound) | none — each node enforces (mesh) | Gateway (+ optional Connector) |
| Connection substrate | cloud-brokered (Zero Trust Exchange) | cloud-brokered (edge proxy) | client↔connector via relay / P2P | peer-to-peer mesh overlay | direct-routed client↔gateway |
| Resource exposure | "apps are never exposed to the public internet" | origin protected; tunnel outbound; app-first ordering | "never accessible from the public internet"; "narrow keyholes" | nodes unreachable outside tailnet | SPA makes resources "invisible"; cloaked infrastructure |
| User joins a network? | "users never access the corporate network" | per-app/per-resource routing, not network join | "do not ever allow users to join the private network" | device joins tailnet overlay (mesh pole) | 1-1 microperimeter connections |
| Clientless/browser access | browser access; privileged remote access (clientless RDP/SSH/VNC) | browser-first; clientless web isolation | Privileged Access for Web Apps | client-centric | Portal (clientless browser) |
| Machine/workload access | workload-to-workload segmentation | Service Auth (service tokens, mTLS) | headless clients, CI/CD, userspace | workload/CI-CD first-class | workload-to-workload, server-initiated, down rules |
| JIT access | (not on fetched page) | (not on fetched pages) | JIT Access Requests, Ephemeral Access | JIT (PAM positioning) | just-in-time session-based microperimeters |
| Session restrictions | (platform-level) | connection context (RDP clipboard/file controls; SSH usernames) | (policy-level; not fetched in detail) | (ACL-level) | microperimeter rules |
| Logging | platform visibility | Access events/logs | audit logs + SIEM export | logging/audit features | Log Server + SIEM forwarder |
| Suite component? | yes — Zero Trust Exchange (SASE) | yes — Cloudflare One | no — standalone (internet security a separate line) | no — standalone (claims to replace SASE) | no — standalone (Risk Sentinel sibling) |
| Customer tier | global enterprise | all sizes (free tier) | SMB/mid-market + MSP | developer → enterprise | enterprise + federal |
| Deployment | vendor cloud | vendor cloud | vendor cloud (controller hosted) | vendor cloud (coordination) | vendor cloud / self-hosted / fully isolated |

### Stable commonalities (evidence layer B)

1. Discrete protected resources (applications/hosts/services defined by address, hostname, or app segment) as the unit of access — all five.
2. Identity-based per-resource authorization with deny-by-default semantics — all five (explicitly documented in three).
3. The product owns the connection path: users never join a network; connections are established per session/per resource through an enforcement component — all five (substrate differs).
4. Resources hidden / not publicly exposed — all five (strongest wording at Zscaler/Twingate/AppGate; structural at Cloudflare via tunnel + app-first ordering; structural at Tailscale via tailnet membership).
5. Identity delegated to / integrated with an enterprise IdP — all five.
6. Device posture as a policy input — all five (depth varies).
7. Admin console defining resources/apps + policies + enforcement components + users/devices — all five.
8. Audit logging of access decisions — all five.
9. VPN replacement as the headline use case — all five (vendor-articulated).

### Divergences (implementation, not definition)

- Connection substrate: cloud-brokered proxy (ZPA, Cloudflare) vs direct-routed gateway (AppGate) vs mesh overlay (Tailscale) vs client-connector relay (Twingate).
- Vendor cloud required: no (AppGate isolated model).
- Clientless/browser access: first-class in some (Cloudflare, AppGate Portal, ZPA browser access), secondary in others (Twingate, Tailscale).
- Machine/workload access: first-class in some (Tailscale, AppGate, Cloudflare service tokens), secondary in others.
- App definition granularity: hostname/port (Cloudflare, Twingate) vs app segments (ZPA) vs nodes/subnets (Tailscale) vs resources behind gateways (AppGate).
- Public-hostname publishing (Cloudflare's "publish internal tools" model) vs strictly private-network access (Twingate, AppGate, ZPA private apps).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

Three jointly-held structures. Remove any one and the product stops being a ZTNA:

1. **The private application/resource as the unit of access.** The product defines discrete protected resources (an application, host, or service — addressed by hostname, IP/port, or app segment) and grants access per resource, never per network. Remove → a network-access product (VPN family).
2. **Identity-based per-resource authorization, deny-by-default.** Access is decided per user (and commonly per device) against policy bound to the specific resource; nothing is reachable without an explicit entitlement. Remove → network-location-based access control (firewall/NAC territory) or plain SSO.
3. **The product-owned connection path.** The product mediates and enforces the network path between the user and the resource — the user's device reaches the resource only through the product's enforcement point, per session. In the dominant implementation the resource is additionally never exposed to the public internet (outbound-only connectors, cloaking, or overlay membership). Remove → SSO/IAM in front of publicly reachable apps (no path ownership), or a published/VPN-exposed app.

Jointly load-bearing:
- 1 alone = a resource inventory with no access model.
- 2 alone = IAM/SSO or a firewall policy engine.
- 3 alone = a VPN/tunnel product.
- 1+2 without 3 = SSO-gated publicly reachable applications (IAM territory).
- 1+3 without 2 = a tunnel with no identity model (VPN territory).
- 2+3 without 1 = identity-aware network access without per-resource granularity (VPN-with-MFA / NAC territory).

### L1 — Common Mature Structure

- Client agent on the user device (transparent proxy / tunnel; headless variants for servers/CI).
- Server-side enforcement component deployed near the resources (connector/gateway), typically outbound-only to the control plane.
- IdP/SSO/MFA integration; SCIM-style user/group sync.
- Device posture checks (own signals + third-party EDR/MDM feeds).
- Session management (duration, re-authentication; continuous re-evaluation of non-identity signals in some products).
- Audit logging of access decisions; SIEM export.
- End-user surfaces: app launcher / resource list; login redirect; block/denied states.
- Admin console: resource/app definitions, policies, enforcement-component management, user/device inventories.

### L2 — Variant / Optional Structure

- Connection substrate: cloud-brokered proxy vs direct-routed gateway vs mesh overlay vs client-connector relay.
- Deployment: vendor-operated cloud vs self-hosted vs fully isolated (no vendor cloud).
- Client-based vs clientless/browser-based access (BYOD/third-party populations).
- App-definition granularity: hostname/port vs IP/CIDR vs app segment vs node/subnet.
- Public-hostname publishing vs strictly private-network access.
- Audience variants: workforce remote access; third-party/contractor/BYOD; OT/IoT device access; branch/site connectivity; workload/machine access (service tokens, headless clients, server-initiated flows).
- JIT access requests / ephemeral access / approval workflows.
- Per-session restrictions (clipboard/file-transfer controls, read-only, allowed usernames).
- Bidirectional ("down") rules for resource→device flows.
- Inline inspection / DLP / browser isolation on the private path (suite-strength add-ons).
- Internet-security add-ons (DNS filtering etc.) — the SSE drift, present as separate product lines in standalone vendors.

### L3 — Vendor-specific (research notes only)

- Zscaler: Zero Trust Exchange; AI-powered app segmentation; Private Service Edge; extranet application support; business continuity; AppProtection; ZDX.
- Cloudflare: service tokens / Service Auth / Bypass actions; WARP/Gateway posture checks; Cloudflare WAN (Magic WAN); Clientless Web Isolation; App Launcher; initial resolved IP ranges; Chrome LNA workarounds.
- Twingate: Relay + peer-to-peer NAT traversal; ACL intersection model (Client ACL × Connector ACL); Identity Firewall; Privileged Access for SSH/Kubernetes/Web Apps; usage-based auto-lock; resource aliases/tags.
- Tailscale: tailnet; WireGuard; subnet routers; exit nodes; Tailnet Lock; PAM positioning.
- AppGate: collective (Controller/Gateway/Connector/Portal/Log Server/Log Forwarder); SPA; microperimeters; Risk Sentinel; Application Discovery; FIPS 140-2 mTLS claim.

## Vendor-specific Findings

- ZPA's "AI-powered app segmentation" and "world's most deployed ZTNA" are vendor claims (marketing page) — recorded as claims, not facts.
- AppGate's "only direct-routed ZTNA" is a vendor differentiation claim — recorded as a claim; the direct-routed vs cloud-routed distinction itself is structurally real (deployment models documented).
- Tailscale's "replaces your legacy VPN, SASE, and PAM" is vendor positioning — evidence that the mesh pole claims all three adjacent jobs, not evidence that the Types merge.
- Cloudflare's Bypass action and its "does not enforce any Access security controls and requests are not logged" warning — product-specific policy action, not a Type behavior.
- Twingate's Relay/peer-to-peer preference and AppGate's SPA are substrate implementations of the same "hidden resource, mediated path" invariant — not definitional.

## Boundary Findings

### vs SASE / SSE Platform (§15 sibling) — DELEGATED TEST DISCHARGED

The sase-sse-platform pass (2026-09-09) recorded: ZTNA is universally a component service inside SASE/SSE platforms (5/5 sampled platforms ship a private-access/ZTNA service); standalone ZTNA products also exist; keep-both expected; test = "remove convergence + the internet-security domain → standalone ZTNA."

**Ratified from this side with fresh evidence.** The standalone pole is real and populated: Twingate (pure-play, no convergence — its internet-security DNS filtering is a separate product line), AppGate ZTNA (pure-play, direct-routed, deployable fully isolated from any vendor cloud), Tailscale (standalone, explicitly positions against SASE). All three carry the full private-access core (resource unit, identity policy, deny-by-default, owned path, hidden resources) with no convergence and no internet-security domain. Conversely, the platform-side private-access flow documented by the sase pass (IdP auth + identity/posture policy + brokered per-app connection via outbound-only connectors, deny-by-default, apps never publicly exposed) matches exactly what the standalone products do — the service is the same Type at component grain. The platform-side discriminator (convergence: multiple services + one policy plane + cloud-edge mediation of internet traffic too) holds: ZPA and Cloudflare Access are the same private-access service embedded in converged platforms. Keep-both ratified; component-vs-platform relationship (analogous to EDR-inside-XDR).

### vs VPN (no directory leaf; the category's standing enemy)

The boundary every sampled vendor articulates themselves: VPN grants access to a network (user joins, can move laterally, gateway publicly exposed); ZTNA grants access to specific applications (user never joins a network, lateral movement structurally limited, resources hidden, enforcement components outbound/behind-firewall). Policy model: network location vs identity + device + context. The exit-node/subnet-router features in mesh products (Tailscale) are explicitly VPN-like modes inside a ZTNA-capable product — variant, not the center.

### vs IAM / SSO (§15)

SSO/IAM decides *authentication into applications*; the application is publicly reachable and enforces the login. ZTNA owns the *connection path* to resources that are otherwise unreachable — it is a network-path function that consumes identity from the IdP (every sampled product delegates authentication to an external IdP; none is the identity source of truth). 1+2 without 3 = SSO territory. Cloudflare's public-hostname publishing model is the closest approach to the SSO seam (Access as "an authentication layer" on a publicly-routable hostname) — but the path still routes through the product's edge and the origin stays unexposed, so it remains in-type.

### vs Privileged Access Management / PAM (§15)

PAM's center: credential vaulting, credential injection, privileged session brokering/recording for administrative access to infrastructure. ZTNA's center: identity-based network-path access to private resources for the workforce. Drift zone is real and vendor-articulated: ZPA Privileged Remote Access (clientless RDP/SSH/VNC), Twingate Privileged Access for SSH/Kubernetes, Tailscale's PAM use-case claim, AppGate's server-initiated connectivity. The seam: ZTNA products add privileged-access features on top of the access path; PAM products center the credential/session machinery. A ZTNA product without vaulting is still ZTNA; a PAM product without network-path ownership is still PAM.

### vs Network Security Platform / microsegmentation (§15)

Network security inspects/filters network flows keyed to addresses/ports; ZTNA mediates user-to-resource access keyed to identity. Drift zone: ZPA markets "user-to-app and app-to-app segmentation" and AppGate/Tailscale claim workload-to-workload — identity-based microsegmentation vocabulary overlaps. The seam: ZTNA's primary subject is the *user-to-private-app* path; east-west/app-to-app segmentation is an extension (and Service Mesh Management's territory when the mesh owns the service graph — per the service-mesh pass's own boundary note).

### vs Service Mesh Management (§14)

Mesh: service-to-service (east-west) authorization enforced by the mesh data plane over service identity, with a service graph. ZTNA: user/device-to-resource (north-south) access over user identity. Workload-access features in ZTNA products (service tokens, headless clients, server-initiated connectivity) approach the seam but do not constitute a service graph.

### vs Browser Security Platform (§15)

Clientless browser access (browser isolation delivering private-app access) is a *mode* inside ZTNA products (Cloudflare clientless web isolation, AppGate Portal, ZPA browser access). The browser-as-the-product (managed/isolated browser itself) is the other Type.

### vs Endpoint Management / UEM (§14)

ZTNA consumes device posture signals (often from EDR/MDM tools); it does not manage devices. Posture is a policy input, not the object of record.

## Historical / Market-Sample Check (§24)

- The Type's ancestry is the Software-Defined Perimeter (SDP): AppGate's own lineage (case studies and reference architecture still carry the "sdp" name; the FAQ contrasts "software-defined perimeter architectures" with VPNs) documents that the pattern predates the "ZTNA" label. An SDP deployment — on-prem controller + client + gateway, SPA cloaking, per-session entitlements — satisfies all three L0 legs with no vendor cloud, no AI, no browser isolation.
- AppGate's **Isolated** deployment model (no connection to any vendor cloud) proves the definition does not require vendor-cloud mediation; Tailscale's mesh proves it does not require the broker-proxy shape; Cloudflare's public-hostname model proves it does not require the resource to be strictly unroutable (the path ownership is the invariant, not the darkness of the DNS record).
- Older/regional/platform-native products (on-prem SDP appliances, government/federal deployments — AppGate's federal tier) fit the definition unchanged. The check passes: the L0 is not an artifact of the current cloud-delivered market.

## Uncertainties

- Zscaler ZPA operational mechanics (App Connector deployment, app-segment configuration, policy evaluation order) — help portal JS-blocked; held at product-page strength; no operational specifics asserted.
- AppGate operational details — product pages + FAQ only; support portal not fetched; component roles and deployment models asserted from vendor FAQ (Tier 2).
- Tailscale ACL default posture — docs index and concept page only; the existence of an "allow-all default ACL" sample is visible in a link name but its role was not researched; not asserted.
- Precise numeric limits (session durations, connector counts, policy counts), default settings, and exact selector lists per product — deliberately not stated in the final document.
- Netskope Private Access / Prisma Access ZTNA modules — covered from the platform side by the sase-sse-platform pass; not re-sampled here (component view inherited from that pass's evidence).
- Whether "down rules" (resource→device flows) are common or rare across the market — observed at AppGate only this pass; held as variant/optional.

## Final Synthesis

ZTNA is the private-access security service: it defines discrete private resources, decides access per resource from user (and device) identity with deny-by-default semantics, and owns the connection path so that users never join a network and resources stay unexposed. The market realizes this with three connection substrates (cloud-brokered, direct-routed, mesh overlay), two deployment families (vendor cloud, self-hosted/isolated), and two access surfaces (client agent, clientless browser). It is simultaneously the component service inside every SASE/SSE platform and a standalone product family — the convergence test separates the two. Its standing enemy is the VPN (network-level access, public gateways, lateral movement); its upstream dependency is the IdP; its nearest drift zones are PAM (privileged access features), microsegmentation (app-to-app vocabulary), and service mesh (workload access).
