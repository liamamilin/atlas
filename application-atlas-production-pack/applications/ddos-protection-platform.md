# DDoS Protection Platform

## Overview

A **DDoS Protection Platform** is an availability-defense application for internet-facing services. It binds itself to a defined set of protected assets — network prefixes, IP addresses, applications, or DNS infrastructure — continuously evaluates the traffic arriving at those assets for signs of a distributed denial-of-service attack, and executes countermeasures in the traffic path (absorbing, filtering, dropping, rate-limiting, challenging, or diverting attack traffic) so that the protected service remains available to legitimate users.

The defining core is deliberately small and is the same regardless of where the product is deployed:

```text
Protected traffic surface (identified assets the platform takes responsibility for)
└── Standing attack detection (continuous evaluation → identified attack events)
    └── Traffic-path mitigation execution (absorb / filter / drop / rate-limit / divert)
        └── Availability objective (keep the service up under volumetric, protocol, and application-layer flooding)
```

Everything else commonly associated with these products — machine-learned traffic profiles, managed rule catalogs, dashboards and reports, human response teams, tiered pricing, WAF integration — makes the protection practical but does not define what the product is. Detection without mitigation is network monitoring; enforcement without standing detection is just a firewall; the same machinery pointed at request content rather than traffic volume is a WAF.

## Users & Context

Primary users are the people responsible for keeping internet-facing services reachable:

- **network / infrastructure operations engineers** — own the edge, prefixes, and upstream connectivity; configure and verify that protection covers their assets; respond when traffic patterns go wrong
- **security operations teams** — monitor attack events, tune detection posture, investigate what was blocked and why, manage false positives
- **application owners** — consumers of the protection rather than operators; they are told to enable it and to design services that survive elevated load

A second, distinct audience exists at the top of the market: **service providers** (carriers, ISPs, and managed service providers) who run the same category of system at carrier scale, both to protect their own networks and to resell managed DDoS protection to their customers as a service.

The working context is unusual among application types: the user spends most of their time confirming that nothing is happening, and their most intense sessions occur mid-attack, when the platform is already acting automatically and the human job is to verify effectiveness, adjust rules, and escalate. Vendors in this market therefore commonly attach an on-call engagement path — a response team reachable during a live attack — to their higher tiers.

## Core Model

### The defining core

Four structures, held together. Remove any one and the product stops being this Type.

**Protected traffic surface.** The platform starts with an explicit statement of what it protects: specific IP ranges, public IPs, application endpoints, DNS infrastructure, or whole networks. This binding is what turns generic traffic machinery into *someone's* protection — the platform takes responsibility for those assets, reports on them individually, and applies per-asset policies. Without it, the product is generic network tooling.

**Standing attack detection.** The platform continuously evaluates arriving traffic against a body of detection knowledge: known attack signatures and vectors (floods of SYN, ACK, UDP, ICMP; reflection and amplification techniques; DNS query floods and water torture; HTTP floods; slow-read attacks; protocol abuse), volume thresholds, and learned baselines of what normal traffic looks like for each protected asset. When traffic crosses into attack territory, the platform records an identified **attack event** — with the affected asset, the attack vector(s), and its progress over time. Without standing detection, a device that merely forwards or absorbs traffic (a load balancer, a CDN) is not a protection platform.

**Traffic-path mitigation execution.** The platform does not stop at alerting: it executes — or automatically orchestrates — countermeasures on the path the attack traffic takes. The action spectrum includes dropping or filtering malicious packets, absorbing floods in high-capacity infrastructure, rate-limiting aggressive sources, issuing challenges to suspected bot clients at the application layer, closing abusive connections, and diverting traffic that exceeds local capacity to cloud scrubbing systems. Without execution, the product is a monitoring or alerting tool.

**Availability objective.** The success criterion is that the legitimate user can still reach the service while the attack runs. This is what separates the Type from content-security products: the adversary being countered is *volume and state exhaustion* — traffic that may be individually valid-looking but is collectively destructive — not exploit payloads or policy violations. The platform's rules are judged by availability outcomes (did the service stay up; were legitimate users spared), not by whether a policy matched.

### Standard capabilities of mature products

These appear across the researched sample and make the core loop workable, but a product can lack some of them and remain recognizably this Type:

- **Vendor-maintained detection content.** The vendor ships and continuously updates the detection knowledge — managed mitigation rulesets, auto-tuned threshold policies, global threat-intelligence feeds — so protection does not depend on customers writing their own attack rules. User tuning happens on top of this layer, not instead of it.
- **Attack event records with lifecycle.** Events are persistent, per-asset records: when the attack started and ended, which vectors were involved, how large it was, what mitigations were applied and with what status. They feed dashboards, metrics, reports, and exports.
- **Visibility machinery.** Real-time dashboards and metrics; alerting at attack start, stop, and duration; in-attack and post-attack reports; export into log pipelines, monitoring systems, and SIEMs; APIs for automation.
- **Learned traffic baselines.** Behavior-based profiling of each protected asset's normal traffic (rates, protocols, geographies, user agents), used alongside signatures to catch novel attacks. Learned profiles also mean detection quality improves with observation time.
- **Tunable posture with safe validation.** Users can adjust how aggressively rules trigger (sensitivity or threshold settings), scope rules to specific traffic characteristics, and — critically — run rules in a log-only mode to validate that only attack traffic is flagged before switching to an enforcing action.
- **False-positive management.** Because over-blocking harms availability as surely as the attack, mature products build in mechanisms to keep legitimate traffic flowing: log-first validation, health-based detection (using the application's own health signals to confirm real impact), and in some products vendor-side checks that catch new rules misfiring before customers are affected.
- **Tiered packaging.** A free or default level of protection available to everyone, with enhanced protection, advanced features, response-team access, and cost-credit guarantees reserved for paid tiers.
- **Human response.** Access to the vendor's attack-response specialists during live incidents at higher service tiers.
- **Centralized multi-asset management.** Consoles and grouping mechanisms for estates with many protected assets — grouping resources for shared detection, applying policies across a fleet, and rolling reporting up to one view.

### Concept versus implementation

The core is written conceptually; the market realizes each concept differently:

```text
Concept:                      Protected traffic surface
Realized as:                  zones/domains, public IPs, cloud resources,
                              network prefixes, DNS services, whole data centers

Concept:                      Detection knowledge
Realized as:                  managed rulesets, auto-tuned threshold policies,
                              threat-intelligence feeds, learned traffic profiles

Concept:                      Mitigation execution
Realized as:                  inline filtering at a reverse-proxy edge, enforcement
                              at a cloud network border, on-premises inline appliances,
                              divert-to-cloud-scrubbing arrangements
```

A reader who has only seen one realization (say, a cloud provider's built-in protection) should still be able to recognize the others from the core model.

## How It Works

The platform runs a continuous protective loop rather than a single workflow. The loop has six phases.

### 1. Enroll a protected asset

```text
Choose the asset (IP, prefix, application endpoint, DNS service, network)
→ bind it to the platform (enable on the resource, point traffic at the
  protection service, or install an inline appliance in front of it)
→ protection becomes active for that asset
```

From this moment the platform is watching. The baseline posture is automatic: mature products detect and mitigate common attacks with no user-authored rules at all.

### 2. Establish the baseline

Detection quality depends on knowing what normal looks like. The platform observes the asset's traffic and builds a profile — typical rates, protocols, sources, application behaviors — using vendor-supplied detection knowledge plus learned baselines. Products differ in how long this takes; several state minimum observation periods before detection is fully accurate. An asset enrolled mid-attack has weaker detection than one that has been observed quietly first.

### 3. Detect

```text
Continuous traffic evaluation
→ signature match / threshold crossing / deviation from learned baseline
→ attack event created (asset, vectors, magnitude, timeline begins)
→ alerts dispatched per configured policy
```

Detection runs on multiple levels simultaneously — network-wide and per-asset — and an event may name a specific known vector or simply report anomalous volume. Application-layer attacks are typically detected through the platform's L7 engine where one is bundled, or through its integration with a WAF where the platform is network-layer native.

### 4. Mitigate

```text
Attack event active
→ automatic mitigation executes at the enforcement point:
   drop / filter attack traffic, absorb floods in mitigation capacity,
   rate-limit aggressive sources, challenge suspect clients,
   close abusive connections, or divert excess traffic to scrubbing systems
→ legitimate traffic continues toward the service
```

Mitigation is automatic by default. User-configured rules act as adjustments on top: they can make detection more or less sensitive for specific traffic, change the action taken (for example, challenge instead of block, or log-only while validating), or exclude known-good traffic from suspicion. A recurring structural detail: enforcement points have their own survival to consider, so at extreme attack scales the platform's own protection takes precedence over per-customer settings — a customer who disabled a rule will still see exceptional traffic mitigated when it threatens the shared infrastructure.

### 5. Observe and tune

```text
Watch the event on dashboards / metrics / reports
→ verify the service stayed available and legitimate traffic flowed
→ inspect what was blocked and why
→ adjust rule sensitivity, thresholds, or scoping
→ post-attack summary recorded
```

This is where the false-positive machinery earns its place. The standard pattern is validate-then-enforce: run a new rule in log-only mode, confirm it flags only attack traffic, then switch it to an enforcing action — lowering sensitivity first if legitimate traffic is being caught. Health-based detection adds the application's own health signals, so an event that doesn't actually hurt the service is treated with more caution.

### 6. Escalate when needed

For attacks that overwhelm automated defenses or the customer's confidence, higher service tiers include reaching the vendor's response team — humans who investigate the live event, apply custom mitigations, and in some arrangements proactively contact the customer when detection and health signals indicate a probable attack. Post-attack, some products close the loop commercially as well as technically, offering credits for attack-caused infrastructure costs under documented conditions.

## Interfaces

Mature products expose a consistent set of surfaces, typically through a web console plus APIs.

### Overview / protected-asset view

The operator's entry point.

- lists protected assets and their protection status, often with an estate-level activity summary
- primary actions: add or enable protection on an asset, open an asset's events, check protection posture

### Events list and event detail

The center of the interface during and after an attack.

- list: current and past attack events with status (e.g., mitigating, mitigated, ended), affected asset, vectors, start time, duration
- detail: vector breakdown, traffic magnitudes, mitigation actions applied and their outcomes, in-attack reports and post-attack summaries
- primary actions: inspect, correlate with alerts, export

### Detection rule and policy configuration

The tuning surface.

- the vendor's managed rules/policies shown with their current posture
- per-rule or per-policy adjustments: sensitivity or threshold settings, action selection (log-only, challenge, block, etc.), traffic scoping, exception of trusted traffic
- health-check association for health-based detection, where offered

### Alerting and integration setup

- alert definitions for attack start/stop/duration routed to email, chat, monitoring, or SIEM destinations
- log/metric export configuration and API credentials for automation

### Reports and analytics

- attack history, trends over time, per-asset summaries, and (in some products) estate or global threat-activity views
- primary actions: review, export, share

### Fleet management console

In larger estates (and in the service-provider variant), a central console manages policies, groups, and reporting across many enforcement points or many customers.

## Important Rules / Behaviors

### Mitigation is threshold-gated

Mitigation actions fire when detection knowledge decides traffic has crossed into attack territory — a threshold, a signature match, or a baseline deviation. Below the threshold, attack-shaped traffic may pass. This is deliberate: over-blocking harms availability, so products err toward documented, adjustable trigger points rather than unconditional filtering. Users who need different behavior adjust sensitivity or thresholds per rule — and inherit the false-positive risk they create.

### Baselines require observation time

Detection is strongest for assets the platform has observed under normal conditions. Several products state minimum observation periods before events are reported with full accuracy, and behavioral profiling improves with history. A newly enrolled asset gets signature- and threshold-based protection immediately, but its behavioral layer matures over time.

### The protection provider's own survival comes first

Enforcement points are shared infrastructure. When attack traffic is large enough to threaten the protection system itself, mitigation happens regardless of customer preferences — customers who set rules to "off" or "log-only" still see extreme traffic mitigated. This is a structural behavior of any shared enforcement point, not a policy nicety.

### Coverage follows where the platform sits

A protection platform covers the layers at which it operates. Network-layer-native products protect L3/4 and reach L7 through a bundled engine or through explicit WAF integration; edge reverse-proxy products protect their own protocol surface downward. L7 availability defense frequently requires the customer to attach a WAF to the protected resource — the DDoS platform either enforces it or manages it on the customer's behalf.

### The appliance complements upstream protection

On-premises enforcement is positioned to catch what upstream defenses pass through — small or short attacks below upstream thresholds, attacks that bypass a CDN by targeting the origin directly, state-exhaustion attacks aimed at the customer's own middleboxes — rather than to replace ISP, CDN, or cloud protection. Cloud-scrubbing arrangements integrate the two: local enforcement detects a volumetric attack it cannot absorb and signals the cloud layer to divert and scrub.

### Validate before enforcing

Because a misfiring protection rule is itself an availability incident, the mature posture is log-first: observe what a rule flags before letting it block, lower sensitivity until legitimate traffic is spared, and use the application's own health signals to confirm real impact. Some vendors add their own pre-enforcement checks to catch misfiring new rules before customers are affected.

## Variants

The Type is one structure realized in several deployment and business shapes:

- **Cloud-edge inline protection** — protection runs at a global reverse-proxy/network edge; protected services route traffic through it; typical of platforms that also serve CDN and WAF roles
- **Cloud-provider-native protection** — built into a cloud platform's network; enabled on the platform's resources (vnets, public IPs, distributions); deeply integrated with the platform's other security services
- **On-premises inline appliance** — dedicated hardware or software placed at the customer's network edge, ahead of firewalls; always-on, stateless filtering; common where customers want traffic control to remain in their own hands
- **Cloud scrubbing / divert** — the protected network is (permanently or on demand) diverted to vendor scrubbing capacity that filters and returns clean traffic; common at carrier scale and as the overflow layer for the appliance variant
- **Hybrid** — on-prem enforcement plus automatically signaled cloud scrubbing; frequently described as the reference architecture for complete coverage
- **Managed service** — the provider (carrier, ISP, or MSSP) operates the platform multi-tenant and resells protection; the customer buys an outcome rather than operating a console
- **Coverage scope variants** — L3/4-only products that explicitly delegate L7 to a WAF, versus products bundling their own L7 engine

Packaging varies along the same lines as deployment: unmetered protection included in a broader service, paid protection tiers with response-team access and cost credits, per-protected-IP subscriptions, and appliance licenses with threat-feed subscriptions.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Web Application Firewall / WAF | closest adjacent; frequently integrated | WAF's defining object is the application request and its content/policy semantics (exploits, access policy, bots); DDoS protection's defining object is the traffic-level availability threat (volume, floods, state exhaustion) and L3/4 vectors a WAF does not address. The seam is L7 flood mitigation, which products handle through integration — the DDoS platform rate-limits or manages WAF rules, or delegates L7 to the WAF entirely |
| CDN | adjacent; shares edge mechanics | CDN's defining job is content delivery and acceleration; flood absorption is a side-benefit and marketed add-on. A DDoS platform's defining job is the availability defense; it may deliver no content at all (network-layer and appliance variants protect without serving anything) |
| Network Monitoring / NDR | observation-side neighbor | monitors, baselines, and alerts but does not execute traffic countermeasures. The moment the product drops, scrubs, rate-limits, or diverts attack traffic, it is this Type; the moment it only reports, it is monitoring. The two are commonly paired rather than merged |
| Network Security Platform / Firewall | enforcement-side neighbor | firewalls enforce per-flow policy and are themselves frequent victims of state-exhaustion attacks; DDoS platforms handle volume-scale and state-exhaustion attacks at a level firewalls cannot, and are commonly deployed in front of them to protect them |
| Incident Management / On-call | process-side neighbor | handles response workflow, communication, and escalation; the DDoS platform is the technical enforcement layer whose alerts and events feed into that process |
| API Security / Bot Management | L7 specializations | concerned with request identity, abuse quality, and business logic abuse; integrate with (rather than constitute) DDoS protection, which is defined by availability under traffic assault |

The boundary that requires the most care in practice is the WAF seam, because modern L7 DDoS mitigations run inside WAF engines (rate-based rules, challenges). The discriminator is the primary objective: availability under volumetric/protocol assault versus request-policy enforcement — and whether the product carries the infrastructure-layer (L3/4) defense at all.

## Representative Products

- Cloudflare DDoS Protection — always-on cloud edge; managed mitigation rulesets with user overrides; network-layer service line for whole networks
- AWS Shield (Standard / Advanced) — cloud-provider native; inline mitigation at the platform's network border and edge; deep WAF integration; attack-response team
- Azure DDoS Protection — cloud-provider native; ML auto-tuned per-IP threshold policies; explicit L7 delegation to WAF; rapid-response team
- NETSCOUT Arbor (Arbor Edge Defense / Sightline / Arbor Cloud) — on-premises inline appliance plus carrier-scale detection plus cloud scrubbing; enterprise and service-provider managed model

## Sources

Research date: **2026-09-07**

- Cloudflare — DDoS Protection documentation (overview, managed rulesets, adaptive protection, attack coverage, override parameters): https://developers.cloudflare.com/ddos-protection/
- AWS — AWS Shield developer guide (overview, capabilities, detection, mitigation, event visibility): https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html
- Microsoft — Azure DDoS Protection overview: https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview
- NETSCOUT — DDoS Protection solutions page and Arbor Edge Defense product page: https://www.netscout.com/solutions/ddos-protection , https://www.netscout.com/products/arbor-edge-defense

> Sourcing limitations: Akamai Prolexic (the scrubbing-center/divert archetype) was unreachable from the research environment (technical-docs and product pages returned errors), so the on-demand divert variant is evidenced indirectly through the sampled products' own descriptions of scrubbing arrangements and is stated with reduced confidence. NETSCOUT evidence is product-page level rather than operational documentation, so that product informed the variant structure but contributed no operational specifics. Precise numeric claims (capacity figures, time windows, tier details) are intentionally omitted; qualitative statements reflect only what the official documentation supports.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
