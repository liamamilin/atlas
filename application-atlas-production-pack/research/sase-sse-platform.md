# Research Notes — SASE / SSE Platform

Research date: 2026-09-09
Leaf: `SASE / SSE Platform` (Directory §15 Cybersecurity, Identity & Trust)
Slug: `sase-sse-platform`

---

## Research Goal

Understand what a SASE (Secure Access Service Edge) / SSE (Security Service Edge) platform actually is as an application type: what structures define it, how user traffic is intercepted and enforced, how policy is expressed and unified across services, what the admin and end-user surfaces look like, and where its boundaries lie against neighboring types (ZTNA, Network Security Platform, DLP, SSPM/DSPM, Email Security, Browser Security).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a cloud-delivered, converged security platform that intermediates user↔internet and user↔private-app traffic at vendor-operated points of presence, enforcing multiple security services (SWG, CASB, ZTNA, optionally FWaaS/DLP/RBI) under one policy and management plane.
- Likely confusions:
  - vs **ZTNA** (separate leaf): ZTNA is one service inside the platform; standalone ZTNA products exist.
  - vs **Network Security Platform** (separate leaf): firewall-centric, typically on-premises; SASE/SSE is cloud-edge and user-traffic-centric.
  - vs **DLP / SSPM / DSPM** (separate leaves): single-capability products; inside SSE they appear as inline or API-side components.
  - **SASE vs SSE**: suspected to be two packaging tiers of one type (SSE = security services; SASE = SSE + SD-WAN/networking), not two types.

## Research Questions

1. Which security services does the platform converge, and which are definitional vs optional?
2. How does user traffic reach the cloud enforcement points (client agent, edge device, tunnel, proxy config, DNS resolver)?
3. How is policy expressed (identity, device posture, destination/app, action) and is it unified across services?
4. How do the internet-access flow (SWG/CASB) and the private-access flow (ZTNA) differ mechanically?
5. What identity integrations gate access (IdP/SSO, MFA, SCIM, device posture/EMM)?
6. What does the admin console look like, and what visibility surfaces exist (logs, analytics, DEM, incidents)?
7. What is the boundary vs standalone ZTNA, vs network security platform, vs DLP/SSPM, vs email security / browser isolation?
8. How do vendors themselves define SASE vs SSE, and does the market treat them as one type or two?

## Representative Products

Selected for market representation, documentation quality, different product philosophy/heritage, and different customer tiers:

| Product | Heritage / philosophy | Tier |
|---|---|---|
| Zscaler (Zscaler Internet Access + Zscaler Private Access) | SSE archetype; security-first, cloud proxy | Global enterprise |
| Netskope (Netskope One) | CASB heritage; SSE leader expanding to SASE | Enterprise / mid-market |
| Cloudflare One | Network/CDN heritage; developer-friendly, broad platform | All tiers (free plan exists) |
| Prisma SASE / Prisma Access (Palo Alto Networks) | Firewall heritage; enterprise, multicloud | Global enterprise |
| Cato Networks | Full-SASE pure-play; networking + security on private backbone | Mid-market / enterprise |

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Zscaler — ZIA product page: https://www.zscaler.com/products/zia ; ZPA product page: https://www.zscaler.com/products-and-solutions/zscaler-private-access ; platform nav (Zero Trust SASE Everywhere pillar). Help portal https://help.zscaler.com/ is a JavaScript app — **not fetchable** (limitation recorded below).
- Netskope — Products page: https://www.netskope.com/products ; SSE page: https://www.netskope.com/products/security-service-edge ; docs portal: https://docs.netskope.com/ (service inventory readable; article bodies JS-rendered).
- Cloudflare — Cloudflare One docs overview: https://developers.cloudflare.com/cloudflare-one/ ; Access policies: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/ ; Gateway traffic policies: https://developers.cloudflare.com/cloudflare-one/traffic-policies/
- Palo Alto Networks — Prisma SASE: https://www.paloaltonetworks.com/sase (marketing page; product roster readable).
- Cato Networks — Knowledge Base: https://knowledge.catonetworks.com/ ; "Welcome to Cato Networks": https://knowledge.catonetworks.com/docs/welcome-to-the-cato-service . Marketing site (catonetworks.com/platform, /network-architecture) JS-rendered/404 — knowledge base used instead.

### Source-access limitations

- Zscaler operational help center could not be fetched (JS-only). Zscaler observations rely on Tier-2 product pages; precise operational details (on-ramp enumeration, default settings) are **not** asserted from memory.
- Cato marketing pages unreachable; Tier-1 knowledge-base article used, which is operational in nature.
- Netskope docs article bodies not fetchable; service inventory taken from the docs portal index and product pages.
- Gartner Magic Quadrant reports are referenced by vendors but not directly consulted (paywalled); analyst positioning is recorded only as vendor claims.

---

## Product A — Zscaler (ZIA + ZPA)

### Key observations (Evidence layer A unless noted)

- Platform framing: "Zscaler unified cybersecurity platform, built on the Zero Trust Exchange"; a "Zero Trust SASE Everywhere" pillar bundles: ZIA (Secure Internet Access), ZPA (Secure Private Access), Zero Trust Branch, Zero Trust Cloud, ZDX (Digital Experience), Zero Trust Browser, Cloud Sandbox, Zero Trust Firewall, Zero Trust Gateway, Business Continuity, Privileged Remote Access, Zscaler Cellular.
- ZIA is described as "the world's most deployed security service edge (SSE)" (vendor claim) delivering: SWG (real-time analysis + URL filtering), IPS, Advanced Threat Protection, DNS Security, AI phishing detection, AI cloud sandbox, browser isolation, CASB, Cloud DLP (EDM/IDM/ML), URL filtering, Zero Trust Firewall ("all ports and protocols"), Cloud App Control, Bandwidth Control.
- ZIA architecture claim: "a true zero trust proxy architecture inspects 100% of TLS/SSL traffic at scale, with direct user-to-app connections based on identity, context, and business policies" (vendor claim; the structural point — proxy architecture + identity/context policies — is the usable observation).
- ZPA: "brokers direct, one-to-one connections between authorized users and specific apps. Unlike with a VPN, users never access the corporate network, and apps are never exposed to the public internet." Capabilities: AI-powered app segmentation, workload-to-workload segmentation, privileged remote access (clientless RDP/SSH/VNC), browser access, Private Service Edge (on-prem ZTNA), business continuity, extranet application support, DEM; AppProtection (L7 inspection of private app traffic), full inline inspection, web + endpoint DLP, browser isolation.
- Use cases enumerated: VPN replacement, hybrid work/continuity, BYOD & third-party access, VDI replacement, OT connectivity, microsegmentation, partner-network app access.
- Multiple cloud admin portals exist (admin.zscaler.net, admin.zscalerone.net, admin.private.zscaler.com, …) — cloud-portal delivery model.
- SIEM/SOAR/XDR integrations, MITRE ATT&CK mapping, forensically complete logging (vendor claim).

## Product B — Netskope (Netskope One)

### Key observations

- Platform framing: "Netskope One" single-cloud platform + "NewEdge" network + "Zero Trust Engine" + "AgentSkope" (client).
- Nav taxonomy is itself evidence of the market's SASE/SSE split: SASE labeled "Security and Network Convergence (SASE)"; SSE labeled "Security Convergence (SSE)".
- Service roster under "Web, Cloud and AI Security": Next Gen SWG, CASB ("Cloud Inline Security"), ZTNA ("Private Access" / NPA), FWaaS ("Cloud Firewall"), Enterprise Browser, Remote Browser Isolation, Threat Protection.
- Data security roster: DLP, DSPM, CASB, SSPM, "Unified Data Security".
- Networking roster: Secure SD-WAN ("Next Gen SASE Branch"), Endpoint SD-WAN, Micro Branch, Device Intelligence.
- Analytics roster: Advanced Analytics, Digital Experience Management.
- Docs portal inventory confirms operational components: Netskope Cloud Platform, Private Access (NPA), Inline App Connector, Streaming Client, Virtual Appliance, Physical Appliance (deprecated), Enterprise Browser, Cloud Exchange (integration hub), AI Gateway, DSPM, Device Intelligence, DEM, DLP On Demand Appliance, Advanced Analytics.
- Gartner MQ for SASE Platforms and for SSE cited as separate reports (vendor claim of Leader in both).

## Product C — Cloudflare One

### Key observations (Tier-1 documentation, richest operational detail)

- Definition (vendor's own docs): "Cloudflare One is Cloudflare's Secure Access Service Edge (SASE) platform. SASE is an architectural model that unifies enterprise networking services with Zero Trust security." Zero Trust = "every request is authenticated and authorized based on identity and context before granting access."
- Product roster: Access (ZTNA), Cloudflare Tunnel (outbound-only connectors via `cloudflared`), SWG ("Cloudflare Gateway"), Cloudflare One Client (device agent; posture rules), RBI, CASB (at-rest scanning, misconfigurations, unsanctioned usage), DLP (web traffic + SaaS), Email security, DEX (Digital Experience Monitoring).
- **Access (private access) policy model**: every policy = Action (Allow / Block / Bypass / Service Auth) + Rule types (Include = OR, Exclude = NOT, Require = AND) + Selectors (email, email domain, country, IP ranges, IdP group, SAML group, OIDC claim, login method, authentication method/MFA, user risk score, device posture, client connected [WARP/Gateway], service token, client certificate, external evaluation API) + Values. "Access is deny by default." Non-identity selectors (device posture, country, IP) are re-evaluated continuously during the session. Connection context per policy (e.g., clipboard/file-transfer controls for browser RDP; allowed UNIX usernames for SSH). Application types: self-hosted HTTP, SaaS, non-HTTP (SSH/RDP), infrastructure. SCIM provisioning can force re-attestation on IdP revocation. Policy order of execution documented (Service Auth/Bypass first, then Block/Allow top-to-bottom; first match stops evaluation).
- **Gateway (SWG) policy model**: policy layers — DNS policies (block before resolution), Network policies (L4: IP/port/protocol/SNI; "correspond to a Layer 4 stateful firewall, sometimes called FWaaS"), HTTP policies (L7 forward proxy with TLS decryption via installed root certificate; URL, headers, files; file sandboxing/quarantine; account control e.g. allow corporate Google Workspace, block personal Gmail), Egress policies (fixed egress IPs), Resolver policies (route DNS to custom servers), Packet filtering (pre-policy drop without user context).
- **On-ramps** (connection methods) and which policy layers each supports: Cloudflare One Client (DNS+Network+HTTP; roaming managed devices), DNS resolver configuration (DNS only; unmanaged devices/networks/initial rollout), Proxy endpoint / PAC file (HTTP, browser only; agentless), Network tunnel IPsec/GRE via Magic WAN (DNS+Network+HTTP; branches/data centers). On-ramps can be combined.
- **Traffic flow**: device → on-ramp → nearest Cloudflare edge location → policy evaluation in order (DNS → network → HTTP) → proxy to destination → response inspected on return path.
- Identity & device context in Gateway policies: user identity from IdP (Okta/Entra ID/Google Workspace named), device posture signals (OS version, disk encryption, firewall state, managed serial number), combinable with traffic selectors.
- Policy propagation note: edits may take up to ~60 seconds to reach all data centers (documented operational fact).

## Product D — Prisma SASE (Palo Alto Networks)

### Key observations

- Roster (from official SASE page + footer product index): Prisma Access (the SSE service), Prisma SD-WAN, Enterprise DLP, Prisma Browser, Remote Browser Isolation, Autonomous Digital Experience Management (ADEM), App Acceleration, SaaS Security, AI Access Security; "Zero Trust Branch" via Prisma SD-WAN + ION devices.
- Positioning: "the industry's most comprehensive SASE solution… on a unique, multicloud architecture" (vendor claim); secures "managed and unmanaged devices"; unified data policies; branch transformation.
- Marketing page is thin on operational mechanics; no Tier-1 operational doc fetched for Prisma Access itself (docs.paloaltonetworks.com exists but was not fetched — time-box). Structural claims kept at roster level.

## Product E — Cato Networks

### Key observations (Tier-1 knowledge base)

- "Cato Cloud — a global, cloud-native platform that converges networking and security into a single architecture known as SASE… Delivered through a private backbone of strategically located PoPs… Key capabilities include SD-WAN, next-generation firewall (NGFW), secure web gateway (SWG), advanced threat protection, ZTNA, and network optimization. Fully software-defined and centrally managed."
- **Cato Management Application (CMA)**: centralized cloud console — "define security policies, configure network rules, manage users and devices, and troubleshoot issues across all connected sites, Clients, and services"; real-time visibility into traffic flows, threat activity, system health, policy enforcement; RBAC, audit logs, automation.
- **Cato Socket**: edge device connecting a physical site (branch/DC/HQ) to Cato Cloud; encrypted tunnels to nearest PoP over broadband/fiber/LTE; full LAN firewall at site level (inbound/outbound policy, segmentation, east-west); site routing, application-aware handling, HA; hardware and virtual form factors; centrally managed.
- **Cato Client**: lightweight agent for individual users (Windows, macOS, Linux, iOS, Android, Chromebook); encrypted tunnel to nearest PoP; "user traffic is subject to the same security policies and traffic optimization as site-based users, including firewall rules, threat prevention, and application control"; seamless roaming, auto-reconnect, SSO integration.
- Knowledge-base index also shows: Production PoP guide, Socket HA, "Protecting Users with Always-On Security", EDM detectors for AI security, integrations (Datadog, Microsoft Defender for Cloud Apps XOps).

---

## Cross-product Comparison

| Dimension | Zscaler | Netskope | Cloudflare One | Prisma SASE | Cato |
|---|---|---|---|---|---|
| Cloud edge PoPs | Yes (cloud portals; "security cloud") | Yes (NewEdge network) | Yes (global network edge) | Yes (multicloud architecture) | Yes (private backbone PoPs) |
| SWG / web security | ZIA (SWG, URL filtering, DNS security, sandbox) | Next Gen SWG | Gateway (DNS/Network/HTTP policies) | In Prisma Access (roster) | SWG in Cato Cloud |
| CASB / cloud app control | Cloud App Control + CASB | CASB (inline) + CASB API | CASB (API, at-rest) | SaaS Security | (not itemized in fetched doc) |
| ZTNA private access | ZPA (brokered user-to-app) | Private Access (NPA) | Access (policy-gated apps via Tunnel) | Prisma Access | ZTNA in Cato Cloud |
| FWaaS / network policy | Zero Trust Firewall | Cloud Firewall (FWaaS) | Network policies (L4) | (roster-level) | NGFW |
| Inline DLP | Cloud DLP + endpoint DLP | DLP | DLP (web + SaaS) | Enterprise DLP | (EDM detectors documented) |
| RBI / enterprise browser | Zero Trust Browser | RBI + Enterprise Browser | RBI | RBI + Prisma Browser | (not in fetched doc) |
| Client agent | Yes (client portals; AgentSkope-equivalent not named) | Netskope One Client / AgentSkope | Cloudflare One Client (WARP) | Agent (roster-level) | Cato Client |
| Site/branch edge device | Zero Trust Branch | Secure SD-WAN appliances | Network tunnels (IPsec/GRE); no own appliance documented | Prisma SD-WAN + ION devices | Cato Socket (HW + virtual) |
| Unified admin console | Cloud portals (per service clouds) | Netskope One | One dashboard | (roster-level; Strata Cloud Manager adjacent) | CMA (explicitly unified) |
| Identity integration | "identity, context" policies | Device Intelligence + IdP (implied by roster) | IdP login, groups, SCIM, MFA selectors (explicit) | "managed and unmanaged devices" | SSO integration (explicit) |
| Device posture | Dynamic risk-based policy (user/device/app/content risk) | Device Intelligence | Device posture checks (explicit, continuous) | Managed/unmanaged device security | Client + site posture (roster-level) |
| DEM / experience monitoring | ZDX | DEM | DEX | ADEM | (not in fetched doc) |
| SD-WAN (SASE vs SSE axis) | Zero Trust SD-WAN (use case) | Secure SD-WAN | Magic WAN (tunnels) | Prisma SD-WAN | SD-WAN (core) |
| Email security | (not in fetched roster) | (not in fetched roster) | Email security (bundled) | (not in fetched roster) | (not in fetched doc) |
| AI/GenAI security controls | AI-powered detection; secure AI use | AI Security suite (GenAI, AI Gateway, guardrails) | (not emphasized in fetched docs) | AI Access Security; agentic-AI browser | EDM for AI security |

### Cross-product commonalities (Evidence layer B)

1. **All five** deliver enforcement from vendor-operated cloud points of presence reached from user devices/sites — none is appliance-first.
2. **All five** converge multiple security services (web security + private access + more) rather than selling a single service.
3. **All five** key enforcement to user identity and device/context, integrated with enterprise IdPs (SSO named at Cato; IdP selectors explicit at Cloudflare; "identity, context" at Zscaler).
4. **All five** have a client agent as a primary on-ramp for user traffic.
5. **All five** expose a central admin console managing policy across services and sites/users.
6. **All five** provide visibility surfaces (logs/analytics; DEM in 4 of 5 fetched rosters).
7. **All five** market against the VPN + on-prem security stack model (VPN replacement is an explicit use case at Zscaler; implied platform-wide).

### The SASE/SSE naming axis (Evidence layer A+B)

- Netskope's own nav: SASE = "Security and Network Convergence"; SSE = "Security Convergence".
- Cloudflare docs: SASE "unifies enterprise networking services with Zero Trust security".
- Cato: SASE = networking + security converged on one backbone (SD-WAN is core).
- Zscaler: leads with SSE (ZIA) and packages SASE as a pillar including branch/workload products.
- Palo Alto: sells "Prisma SASE" = Prisma Access (SSE) + Prisma SD-WAN.
- Conclusion: SASE and SSE are two packaging tiers of the same platform type; SSE = the security service set; SASE = SSE + SD-WAN/site networking. The directory leaf "SASE / SSE Platform" correctly covers both.

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures. Remove any one and the product stops being a SASE/SSE platform:

1. **Cloud-edge mediation of user traffic.** The platform intercepts and processes user traffic — user↔internet/SaaS and user↔private-app — at vendor-operated, distributed cloud points of presence, reached via client agents, site edge devices/tunnels, or proxy/DNS configurations. Remove → on-premises security stack / NGFW / VPN concentrator territory (no cloud edge).
2. **Converged security services under one control plane.** Multiple security services — at minimum web/internet security and private-application access, commonly plus cloud app control, data protection, and firewall — are delivered as one platform with unified policy, administration, and logging. Remove → a portfolio of point products (standalone SWG, standalone ZTNA); the "platform" is gone.
3. **Identity- and context-based policy.** Enforcement decisions bind user identity (from the enterprise IdP), device posture/context, and destination/application classification — not merely network address. Remove → network-address firewalling = Network Security Platform territory.

Jointly-held load-bearing check:

- 1 alone = a cloud proxy / hosted web-filtering service (single-service point product).
- 2 without 1 = an API-side security suite (SSPM/CASB-API class) with no traffic path.
- 3 without 1+2 = an IdP/IAM policy engine.
- 1+2 without 3 = a legacy cloud proxy with IP-based rules (not the modern type).
- 1+3 without 2 = a single-service ZTNA or SWG product (point product, not platform).

### L1 — Common Mature Structure (very common, not definitional)

- SWG mechanics: URL/category filtering, DNS filtering, TLS decryption + inspection, malware scanning, file sandboxing/quarantine.
- CASB inline: cloud-app discovery/control, sanctioned vs unsanctioned, tenant/account restrictions.
- ZTNA private access: per-app brokered connections, app connectors on the server side, no network-level access, apps never exposed publicly.
- FWaaS / L4 network policies.
- Inline DLP (content inspection in motion).
- RBI / enterprise browser.
- Device posture checks (OS state, disk encryption, managed-device lists) as policy inputs.
- Digital experience monitoring; analytics; logging/SIEM integration.
- Multiple on-ramps beyond the client (DNS resolver, PAC/proxy endpoint, IPsec/GRE tunnels, SD-WAN edge device).
- Egress IP control (fixed egress addresses for partner/service allowlists).

### L2 — Variant / Optional Structure

- **SD-WAN / branch networking** — the SASE-vs-SSE axis itself: full-SASE products (Cato, Prisma, Netskope) include site networking; SSE-only packaging (Zscaler's ZIA/ZPA core, Cloudflare's Zero Trust set) treats it as optional or adjacent.
- Edge architecture: private backbone (Cato) vs public-cloud/global-network PoPs (Cloudflare) vs hybrid/multicloud (Palo Alto).
- Clientless/browser-based access modes (privileged remote access, browser access) for BYOD/third parties.
- Bundled adjacent products: email security (Cloudflare bundles it), endpoint DLP, DSPM/SSPM (Netskope bundles), workload/east-west security (Zscaler Zero Trust Cloud), OT/IoT segmentation, cellular.
- AI/GenAI security controls (prompt inspection, AI gateways, guardrails) — emerging, unevenly present.
- Deployment/compliance variants: sovereign/regional data requirements, government clouds, MSP delivery.

### L3 — Vendor-specific Structure (stays in Research Notes)

- Zscaler: Zero Trust Exchange; ZIA/ZPA product split; Single Scan Multi-Action engine; ZDX; Private Service Edge; Business Continuity; per-cloud admin portals (admin.zscaler*.net).
- Netskope: Netskope One; NewEdge; Zero Trust Engine; AgentSkope; Cloud Exchange (integration hub); Inline App Connector / Streaming Client / Virtual Appliance (deprecated Physical Appliance).
- Cloudflare: WARP-based Cloudflare One Client; `cloudflared` Tunnel; Magic WAN; packet-filtering policy layer; free plan tier; ~60s policy propagation (documented).
- Palo Alto: Prisma SASE 4.0/5.0 branding; ADEM; App Acceleration; ION devices; Strata Cloud Manager adjacency.
- Cato: Cato Socket (HW/virtual) + Socket HA; CMA; private backbone; "Coffee Shop Networking"-class marketing concepts.

## Rejected Findings (not promoted to core)

- "All SSE platforms include RBI/enterprise browser" — present in 4/5 fetched rosters but absent from Cato's fetched doc; held as common-optional, not definitional.
- "FWaaS is definitional" — present in all, but the type is recognizable without it (Zscaler sells ZIA without emphasizing firewall; Cloudflare treats network policies as one layer among several). Held as common.
- "Private backbone is definitional" — only Cato's fetched doc claims it; Cloudflare explicitly runs on its public global network. Variant, not invariant.
- "AI security controls are definitional" — 2026 marketing emphasis at 3/5 vendors; absent from Cloudflare's and Cato's fetched operational docs. Emerging optional.
- "Email security is part of SSE" — only Cloudflare's fetched roster bundles it; others sell it separately or not at all. Optional bundle.
- "DEM is definitional" — 4/5 rosters; a visibility feature, not a defining structure.
- Zscaler's "inspects 100% of TLS traffic" and "world's most deployed" — vendor claims; not independently verifiable from fetched sources; excluded from canonical claims.

## Boundary Findings

| Neighboring type | Relationship | Distinction (what to remove from SASE/SSE to become the neighbor) |
|---|---|---|
| Zero Trust Network Access / ZTNA (leaf) | component / point-product pole | Keep only the private-access service, drop convergence + internet security → standalone ZTNA. ZTNA is universally a service inside SSE; the platform adds SWG/CASB/etc. and the unified plane. |
| Network Security Platform (leaf) | adjacent, heritage overlap | Move enforcement back on-premises/appliance, key policy to network address rather than identity/context → NGFW-class platform. FWaaS inside SSE is the shared capability; the delivery and policy model differ. |
| Data Loss Prevention / DLP (leaf) | capability inside + standalone pole | Keep only content inspection as a standalone product → DLP. Inside SSE, DLP is one inline service among several sharing the same policy plane. |
| SaaS Security Posture Management / SSPM, DSPM (leaves) | API-side sibling | Drop traffic mediation entirely; operate via API against SaaS/cloud configs → SSPM/DSPM. Some vendors bundle both; the traffic path is the seam. |
| Email Security Gateway (leaf) | channel-specific adjacent | Restrict mediation to the email channel → email security. Bundled by some SSE platforms (Cloudflare) but not definitional. |
| Browser Security Platform (leaf) | surface-specific adjacent | Make the isolated/managed browser the primary product → browser security. Inside SSE, RBI/enterprise browser is an enforcement mode. |
| Endpoint Protection / EDR (leaf) | complementary, different locus | Move enforcement onto the endpoint's processes/files → EDR. SSE enforces the network path, not endpoint internals; posture checks read endpoint state but don't protect it. |
| IAM / SSO (leaves) | upstream dependency | Keep only identity and policy decisioning without traffic mediation → IdP/IAM. SSE consumes IdP identity; it does not issue it. |
| Cloud Management Platform / CDN | different object of work | SASE/SSE mediates *user* traffic for security policy; CDN caches/accelerates *published* content; CMP operates cloud resources. Heritage overlap (Cloudflare) does not make them the same type. |

**SASE vs SSE within the leaf**: one type, two packaging tiers. SSE = the converged security service set; SASE = SSE + SD-WAN/site networking on the same platform. Evidence: Netskope's own nav labels; Cloudflare's definition; Cato's architecture; Palo Alto's packaging (Prisma Access + Prisma SD-WAN = Prisma SASE).

**Historical / market-sample check**: SASE is a recently coined category (market term, 2019-era), so the "older generation" test runs against (a) hosted/cloud web-filtering services and (b) appliance-based perimeter stacks. A hosted web-filtering service satisfies cloud-edge mediation but fails convergence (single service) → correctly a point product, not this type. An MSSP-managed appliance stack fails cloud-edge mediation → not this type. The L0 therefore does not overfit to 2026 features: no AI, no SD-WAN, no DEM, no specific on-ramp technology is required. Regional and smaller-market SSE vendors would satisfy L0 with any client/tunnel/proxy on-ramp and any PoP architecture.

## Uncertainties

- Prisma Access operational mechanics (policy model, on-ramps) were not fetched from Tier-1 docs; Prisma observations are roster-level. Assertion strength for Palo Alto kept low.
- Netskope operational article bodies not fetched; service inventory is from the docs index and product pages. Policy-model specifics for Netskope not asserted.
- Zscaler on-ramp enumeration (agent vs PAC vs IPsec etc.) not verified — help portal JS-blocked; deliberately not filled from memory.
- Cato's CASB-equivalent service naming not confirmed from fetched sources.
- Whether every SSE platform supports *continuous* (in-session) posture re-evaluation: explicit at Cloudflare; not verified elsewhere. Written as product-documented behavior, not generalized.
- Gartner MQ definitions of SSE/SASE not directly consulted (paywalled); the SASE/SSE relationship is established from vendor-primary sources only.

## Final Synthesis

A SASE/SSE platform is defined by three jointly-held structures: (1) cloud-edge mediation of user traffic at vendor-operated points of presence reached via clients, edge devices/tunnels, or proxy/DNS configurations; (2) a converged set of security services — web/internet security and private-application access at minimum, commonly plus cloud app control, data protection, and firewall — under one policy/administration/logging plane; (3) identity- and context-based policy binding IdP identity, device posture, and destination/app classification. The standard capability set adds SWG mechanics, inline CASB, ZTNA with app connectors, FWaaS, inline DLP, RBI/browser, posture checks, DEM/analytics, and multiple on-ramps. Variants: SSE-only vs full-SASE (SD-WAN included), private backbone vs public-cloud PoPs, clientless/browser modes, bundled adjacent products (email security, endpoint DLP, DSPM/SSPM, workload security, AI security). SASE and SSE are two packaging tiers of one type, not two types.
