# Zero Trust Network Access / ZTNA

## Overview

A **Zero Trust Network Access (ZTNA)** product is a security access service that gives users identity-verified, policy-controlled connections to specific private applications — without ever letting them join the network those applications live on.

The defining core is small:

```text
Private application / resource (the unit of access)
  → access decided per user (and device) identity, deny-by-default
    → connection path owned and enforced by the product, per session
      → the application itself stays unexposed
```

Three properties hold the type together. Remove any one and it stops being a ZTNA:

- **The private application is the unit of access.** The product defines discrete protected resources — an application, host, or service addressed by hostname, IP and port, or an application segment — and grants access per resource, never per network. A product that grants access to a network is a VPN, not a ZTNA.
- **Access is decided from identity, deny-by-default.** Every connection attempt is evaluated against policy bound to the specific resource; nothing is reachable without an explicit entitlement. A product that grants reachability based on network location is a firewall, not a ZTNA.
- **The product owns the connection path.** The user's device reaches the resource only through the product's enforcement point, connection by connection — the user never joins a network, and in the dominant implementation the application is never exposed to the public internet. A product that only puts a login page in front of a publicly reachable application is an SSO implementation, not a ZTNA.

The category's standing enemy is the corporate VPN, and every structural choice is made against it: VPNs grant network-level access, expose public gateways, and permit lateral movement; ZTNA grants application-level access, hides the application, and connects the user to exactly the resources policy allows — nothing more.

ZTNA exists in the market in two forms: as **standalone products** and as the **private-access service inside broader SASE/SSE platforms**. The service is the same in both; the platform adds convergence (internet security, data protection, and other services under one policy plane). The boundary is documented in Related Application Types.

## Users & Context

**Primary users are security and network administrators** in organizations replacing or avoiding VPN-based remote access:

- the security admin defines resources and writes access policy: which users (and from which devices) may reach which private applications, under what conditions;
- the network/infrastructure admin deploys and operates the enforcement components — the connectors or gateways placed inside the networks where applications live;
- the security operations analyst consumes access logs and audit records.

**End users are enforced upon, not operated on.** Their experience is deliberately thin: a client agent (or a browser), a login redirected to the company's identity provider, a list of the applications they may open, and a denial when policy says no. There is no workspace to learn.

**Secondary populations** are a structural part of the use case rather than an afterthought: third parties, contractors, and BYOD devices that must never join the corporate network but must reach specific applications — frequently served through clientless browser access. Workload and machine access (CI/CD pipelines, servers, service-to-service calls) appears in many products as a first-class audience alongside people.

Typical context: applications hosted in private data centers or clouds (web apps, SSH/RDP infrastructure, databases, legacy systems, OT/IoT devices), a workforce distributed across offices, homes, and travel, and a mix of managed and unmanaged devices. The product is bought precisely because the old assumption — users, apps, and data inside one network perimeter — no longer holds.

## Core Model

### The Defining Core

```text
Resource (private application / host / service)
  ├── defined by address: hostname, IP + port, CIDR, or app segment
  ├── bound to an enforcement point placed near it
  └── reachable only through the product
Identity (user, from the enterprise IdP; device, as a policy input)
  └── evaluated against
Policy (per-resource rules: who + from what + to what → allow/deny)
  └── grants
Session (a per-user, per-resource, time-bounded connection)
```

**Resource.** The object of record. A resource is a specific private destination — an internal web application, an SSH host, a database, a desktop, an OT device — defined by an address (hostname, IP/port, CIDR range, or a named application segment) and attached to the network location where it lives. Resources are the granularity of everything: policy is written per resource, connections are established per resource, and logs are recorded per resource. The resource, not the network, is what a user is allowed to reach.

**Identity.** The decision input. The product delegates authentication to the organization's identity provider — it is never the source of truth for who users are. User and group identity come from the IdP; device identity and posture come from the client agent and often from third-party endpoint tools. Revoking a user in the IdP is what cuts access.

**Policy.** The rule set that binds identity to resources. A policy names a resource (or set of resources), the users/groups who may reach it, and commonly additional conditions: device posture, location, authentication strength. Evaluation is deny-by-default — a resource with no matching allow rule is unreachable, including for users who can authenticate successfully.

**Session.** The granted connection. Access is not a standing network membership but a sequence of evaluated, time-bounded connections between one user (on one device) and one resource. Sessions expire, re-authenticate, and can carry restrictions (for example, read-only or clipboard-disabled remote sessions for untrusted populations).

### Standard Capabilities

A typical modern ZTNA product carries most of these. They are not what makes the product a ZTNA, but they make it deployable:

- **Client agent** on the user's device — a transparent proxy/tunnel that intercepts traffic destined for protected resources and routes it through the product; headless variants serve servers and CI/CD runners.
- **Enforcement component near the applications** — a connector or gateway deployed inside the private network, holding an outbound connection to the product's control plane and admitting only authorized sessions to the resources behind it.
- **IdP/SSO/MFA integration** — login redirected to the enterprise identity provider; user/group sync; MFA enforcement.
- **Device posture checks** — managed-device membership, disk encryption, security-software state, often fed by third-party EDR/MDM tools; commonly a policy condition.
- **Session management** — configurable session duration, re-authentication, and in some products continuous re-evaluation of posture and context during the session.
- **Audit logging** — every access decision recorded; export to SIEM.
- **End-user surfaces** — an application launcher or resource list, the login redirect, and block/denied states.
- **Admin console** — resource definitions, policy editors, connector/gateway management, user and device inventories.

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently, and the differences are variants, not definitions:

```text
Concept:            Resource definition
Implementations:    public hostname (published app), private IP + port,
                    private hostname, IP/CIDR range, named app segment,
                    mesh node/subnet

Concept:            Enforcement point near the application
Implementations:    outbound-only connector, gateway appliance,
                    the application host itself (mesh member)

Concept:            Connection path
Implementations:    cloud-brokered (traffic relayed through vendor PoPs),
                    direct-routed (client ↔ gateway, point-to-point),
                    peer-to-peer mesh overlay,
                    client ↔ connector via relay

Concept:            User surface
Implementations:    installed client agent, browser-only (clientless),
                    browser isolation session, app launcher portal
```

A reader who has only seen one implementation — say, a cloud-brokered service with a desktop client — should still be able to recognize a direct-routed gateway product or a mesh-overlay product as the same Type from the core model.

## How It Works

### 1. Deploy the enforcement components

The administrator installs a connector or gateway inside each network that holds protected applications (data center, cloud VPC, branch). The component dials out to the product's control plane — nothing listens on the public internet — and registers itself. From that moment the applications behind it are reachable only through the product.

### 2. Define resources and policy

The administrator defines each protected application (address and, where applicable, ports), then writes access policy: which users or groups, from what kind of device, may reach it, and under what conditions (posture, location, authentication strength). Until a policy allows a user, the resource is unreachable — deny-by-default is the starting state, not a setting.

### 3. The access flow

```text
user opens the application (via client or browser)
→ product authenticates the user against the identity provider (SSO/MFA)
→ policy evaluated: identity + groups + device posture + the specific resource
→ allowed: product establishes the connection to the resource
   (through the connector/gateway; the application is never publicly exposed)
→ denied or no policy: nothing is reachable — the request fails at the device
→ session persists for its configured lifetime, then re-authenticates
```

The structural difference from a VPN is the unit of access: the application, not the network. The user never joins a network, cannot scan laterally, and the enforcement component's outbound-only posture means there is no public attack surface to find.

### 4. The policy-authoring loop

The administrator's ongoing work is a loop: define resources and rules → observe access in logs → tune (new resources, tighter posture conditions, group changes) → repeat. Identity changes in the IdP (a user offboarded, a group membership revoked) propagate into access decisions without touching the network.

### 5. The operations loop

Security operations consumes the audit plane: who accessed what, from which device, when, and which requests were denied — exported to SIEM for correlation. Access requests with approval workflows (just-in-time access) route through reviewers when configured.

## Interfaces

### Admin console (web)

The product's center of gravity. Across researched products it consistently contains:

- **Resource/application inventory** — the defined private applications with their addresses, ports, and network placement.
- **Policy editors** — per-resource rules binding users/groups, device conditions, and actions; ordered evaluation where multiple rules apply.
- **Enforcement-component management** — connector/gateway deployment, registration, health, and versioning.
- **Identity and device inventories** — users/groups synced from the IdP; enrolled devices with posture state.
- **Audit and monitoring** — access logs, denied attempts, connector health; SIEM export.

### Client agent (end user)

A small, mostly silent surface: connection status, the identity-provider login prompt, and notifications when a non-browser application needs authentication. Traffic to protected resources is intercepted transparently — applications on the device behave as if the resources were locally reachable, without any per-application configuration.

### Browser / clientless access

For unmanaged devices, contractors, and privileged remote sessions, access through the browser without an agent: the user authenticates in a web flow and reaches the application through a brokered or isolated browser session. Some products deliver this as a first-class mode; others as an option for specific populations.

### Enforcement surfaces the user meets

- **Login redirect** to the company IdP (SSO/MFA) before access.
- **Application launcher** — the list of private applications the user is entitled to open.
- **Block/denied states** — what the user sees when policy says no.

## Important Rules / Behaviors

- **Deny-by-default is the ground state.** A resource is unreachable until a policy explicitly allows a user. Authentication alone grants nothing — a successfully logged-in user without an entitlement still reaches nothing.
- **The user never joins a network.** Connections are established per resource, per session. Lateral movement is structurally limited because there is no network to move laterally within — the enforcement component admits only the specific connections policy allows.
- **Applications are hidden by design.** Enforcement components dial out to the control plane; nothing listens on the public internet. In the dominant implementation there is no publicly discoverable endpoint for the private applications at all.
- **Identity is consumed, not owned.** The product relies on the enterprise identity provider for users, groups, and authentication. Revoking a user in the IdP is what cuts access; the product is not the source of truth.
- **Device posture is a policy input, not a gate of its own.** Posture conditions (managed device, encryption, security-software state) attach to access rules; in some products they are re-evaluated continuously during a session, so access can lapse when a device stops complying.
- **Sessions are bounded.** Access grants expire and re-authenticate; they are not standing permissions.
- **Everything is logged.** Access decisions — allowed and denied — are recorded as a structural behavior, not an add-on.

## Variants

- **Connection substrate.** Cloud-brokered (user traffic relayed through vendor-operated points of presence), direct-routed (client connects point-to-point to a gateway near the application), peer-to-peer mesh overlay (devices connect directly under a coordination plane), and client-to-connector relay designs. Performance and architecture implications, not structural differences.
- **Deployment.** Vendor-operated cloud (the dominant model), self-hosted (control plane or enforcement in the customer's environment), and fully isolated deployments with no vendor cloud connection at all — the definition holds in all three.
- **Client-based vs clientless.** Installed agent for managed devices; browser-only access for BYOD, contractors, and privileged remote sessions. Many products carry both.
- **Published vs strictly private.** Some products can publish an internal application at a public hostname with the product's edge enforcing access (the origin stays unexposed); others operate strictly inside private address space.
- **Audience variants.** Workforce remote access (the headline use case); third-party/contractor access; OT/IoT device access; branch/site connectivity; workload and machine access (service tokens, headless clients, server-initiated flows).
- **Just-in-time access.** Request-and-approval workflows granting time-bounded access to specific resources.
- **Suite add-ons on the private path.** Inline threat inspection, data-loss prevention, and browser isolation for private-application traffic — common in platform-embedded ZTNA, optional in standalone products.
- **Internet-security add-ons.** Some standalone vendors ship DNS filtering or similar as a separate product line — the first step toward platform convergence, not part of the private-access core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| SASE / SSE Platform | component / platform | ZTNA is the private-access service inside every SASE/SSE platform. The platform adds convergence: multiple security services (internet security, data protection, cloud app control) under one policy plane, mediating internet traffic too. Remove convergence and the internet-security domain → a standalone ZTNA; add them → the platform. |
| VPN (no directory leaf; the standing enemy) | replaced predecessor | VPN grants access to a network (user joins, gateway publicly exposed, lateral movement possible); ZTNA grants access to specific applications (user never joins, resources hidden, per-resource policy). |
| IAM / SSO | upstream dependency | SSO decides authentication into publicly reachable applications; ZTNA owns the connection path to resources that are otherwise unreachable. ZTNA consumes identity from the IdP; it is never the identity source of truth. |
| Privileged Access Management / PAM | adjacent, drift zone | PAM centers credential vaulting and privileged session brokering/recording; ZTNA centers identity-based network-path access. ZTNA products add privileged-access features (clientless RDP/SSH, just-in-time grants) without becoming PAM; the credential/session machinery is the seam. |
| Network Security Platform | adjacent | Network security inspects and filters flows keyed to addresses and ports; ZTNA mediates user-to-resource access keyed to identity. Identity-based microsegmentation vocabulary overlaps; the user-to-app path is ZTNA's subject. |
| Service Mesh Management | different traffic domain | A mesh enforces service-to-service (east-west) authorization over a service graph; ZTNA mediates user/device-to-resource (north-south) access. Workload-access features approach the seam without constituting a service graph. |
| Browser Security Platform | mode vs product | Clientless browser access is one delivery mode inside ZTNA; the managed/isolated browser as the product itself is the other Type. |
| Endpoint Management / UEM | signal provider | ZTNA consumes device posture signals (often from EDR/MDM tools); it does not manage devices. |

The most important boundary is with the **SASE/SSE platform**: every platform contains a ZTNA service, and standalone ZTNA products exist in the market. The test is convergence — one traffic path, one policy plane, multiple services — not the presence of private-access capability.

## Representative Products

- **Zscaler Private Access (ZPA)** — the category-defining enterprise ZTNA; cloud-brokered connections between authorized users and specific apps; the private-access service of the Zscaler platform.
- **Cloudflare Access** — cloud-native identity-proxy ZTNA on a global network; application- and policy-centric model with extensive clientless/browser access; part of the Cloudflare One platform.
- **Twingate** — standalone pure-play; Controller/Client/Connector architecture with resource-level ACLs; SMB/mid-market and MSP tier.
- **Tailscale** — mesh-overlay substrate (WireGuard peer-to-peer) with identity-based access policies; developer/IT tier; positions itself against VPN, SASE, and PAM.
- **AppGate ZTNA** — standalone pure-play with Software-Defined Perimeter heritage; direct-routed architecture, single-packet-authorization cloaking, and fully isolated (no-vendor-cloud) deployment; enterprise and federal tier.

The defining core was checked across all five — three connection substrates, two deployment families, and three customer tiers — to avoid defining the type by any one vendor's architecture.

## Sources

Research date: **2026-09-09**

- Cloudflare — Access policies: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/ ; Publish a self-hosted application: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/ ; Secure a private IP or hostname: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/
- Twingate — How Twingate Works: https://www.twingate.com/docs/how-twingate-works ; Resources: https://www.twingate.com/docs/resources ; Understanding Connectors: https://www.twingate.com/docs/understanding-connectors ; Twingate vs. VPNs: https://www.twingate.com/docs/twingate-vs-vpn
- Tailscale — What is Tailscale: https://tailscale.com/docs/concepts/what-is-tailscale ; docs index: https://tailscale.com/kb/1152/ztna
- Zscaler — Zscaler Private Access product page: https://www.zscaler.com/products-and-solutions/zscaler-private-access
- AppGate — How AppGate ZTNA Works: https://www.appgate.com/products/zero-trust-network-access/how-it-works ; https://www.appgate.com/

> Sourcing limitations: Zscaler's operational help portal is JavaScript-rendered and could not be fetched; ZPA observations rest on the official product page, so operational specifics (connector mechanics, app-segment configuration, policy evaluation order) are deliberately not stated. AppGate observations rest on official product pages and the vendor's own architecture FAQ (no support-portal depth). Precise numeric limits, session defaults, and per-product selector lists are intentionally omitted. Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are in the paired Research Notes.
