# Research Notes — DDoS Protection Platform

Research date: 2026-09-07

## Research Goal

Understand what a DDoS Protection Platform is as an Application Type: its defining structure, the objects it manages, how detection and mitigation actually work, what users configure and observe, and how it differs from adjacent Types (WAF, CDN, Network Monitoring, firewalls).

## Initial Boundary

Initial hypothesis (before research):

- Core use: detect and mitigate Distributed Denial-of-Service attacks against internet-facing services (networks, applications, DNS), preserving availability under traffic-level assault.
- Users: network operations / infrastructure / security operations teams; service providers; on-call responders during attacks.
- Nearest neighbors: Web Application Firewall, CDN, Network Monitoring, Network Security Platform, Incident Management.
- Likely confusion: WAF (content filtering) vs DDoS (availability protection); CDN (delivery) that also absorbs floods.
- Unknowns: core object model (protected asset? attack event? mitigation rule?), always-on vs on-demand posture, mitigation action spectrum, deployment variants.

## Research Questions

1. What are the core objects: protected asset/resource, attack event, mitigation rule/policy, mitigation action?
2. How are attacks detected (thresholds, signatures, baselines, behavioral/ML profiling)?
3. What mitigation actions exist (drop, rate-limit, challenge, connection control, divert-to-scrubbing)?
4. Is the baseline posture always-on/automatic, or operator-triggered? What does the user configure?
5. What lifecycle does an attack event have, and how is it surfaced (console, metrics, reports, alerts)?
6. What are the deployment variants (cloud edge, cloud-provider native, on-prem appliance, cloud scrubbing, managed service)?
7. Where are the boundaries vs WAF / CDN / Network Monitoring / firewalls?

## Representative Products

Chosen for market representativeness + documentation quality + different product philosophies + different deployment models:

| Product | Philosophy / deployment | Evidence level |
|---|---|---|
| Cloudflare DDoS Protection | always-on cloud edge (reverse proxy + network services); managed rulesets with user overrides | A (official developer docs) |
| AWS Shield (Standard/Advanced) | cloud-provider native, inline at network border/edge, deep WAF integration | A (official developer guide) |
| Azure DDoS Protection | cloud-provider native, vnet/public-IP bound, auto-tuned threshold policies | A (official docs on Microsoft Learn) |
| NETSCOUT Arbor (AED / Sightline / TMS / Arbor Cloud / AEM) | on-prem inline appliance + carrier-scale detection + cloud scrubbing; enterprise & service-provider managed model | B (official product pages only; operational docs gated) |

Replaced sample: Akamai Prolexic (scrubbing-center/BGP-divert philosophy) was intended as a fourth sample; both its techdocs and product page were unreachable (404 / 403). Dropped per source-access rules. The scrubbing-center model is still represented through NETSCOUT Arbor Cloud / cloud signaling and via AWS/Azure references to rerouting vs not rerouting to external scrubbing centers.

## Sources

- Cloudflare — DDoS Protection docs (overview, managed rulesets, adaptive protection, attack coverage, override parameters): https://developers.cloudflare.com/ddos-protection/ and child pages (fetched 2026-09-07)
- AWS — AWS Shield developer guide (overview, capabilities, detection, mitigation, event visibility, events): https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html and child pages (fetched 2026-09-07)
- Azure — Azure DDoS Protection overview: https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview (fetched 2026-09-07)
- NETSCOUT — DDoS Protection solutions page and Arbor Edge Defense product page: https://www.netscout.com/solutions/ddos-protection , https://www.netscout.com/products/arbor-edge-defense (fetched 2026-09-07; product-page level only)
- Akamai Prolexic — attempted https://techdocs.akamai.com/prolexic/docs (404) and https://www.akamai.com/products/prolexic-solutions (403); abandoned.

Sourcing limitation: NETSCOUT evidence is marketing/product-page level (Tier 2), so observations from it are structurally reliable (what the product line exists to do) but operational specifics (exact workflows, rule semantics) were not verified and are not asserted. No precise numeric claims are made in the final document beyond what official docs state.

## Product A — Cloudflare DDoS Protection

Key observations (A = directly observed in official docs):

- Positioned as automatic detection + mitigation of DDoS attacks "via our autonomous DDoS systems", available on all plans, unmetered. [A]
- Structure: "DDoS attack protection managed rulesets" — two main sets: HTTP DDoS Attack Protection (L7) and Network-layer DDoS Attack Protection (L3/4: UDP floods, SYN-ACK reflection, SYN floods, DNS floods). Vendor "constantly updates" the rulesets. [A]
- User customization = overrides on managed rules: per rule, set (a) action — block, managed challenge, interactive challenge, log (log gated to Enterprise w/ Advanced subscription) — and (b) sensitivity level (High=default / Medium / Low / Essentially Off), where sensitivity determines the threshold at which the rule triggers. Expression filters scope rules. [A]
- Internal actions users cannot set: connection close / force connection close, "DDoS dynamic" (undisclosed mitigation action). [A]
- Adaptive DDoS Protection (Enterprise tiers): learns per-dimension traffic profiles (origin errors, user agents, locations, protocols) from maximum rates over a 7-day window at 95th percentile, recalculated daily; HTTP rules also use ML bot scores; default action is log so users can validate before escalating; users lower sensitivity until false positives disappear, then enable a mitigation action. [A]
- Events surfaced via Security Analytics (filter by service = HTTP DDoS, rule ID); export via Logpush / GraphQL API. [A]
- Proactive false-positive detection: new managed rules are checked against Business/Enterprise zones' traffic before enforcement; customers contacted to tune before rules start blocking. [A]
- Scope rule: "you are protected up to the layer on which your service operates" — CDN/WAF service protects L7 downward; network-layer services (Magic Transit for networks) get L3/4 with additional Advanced TCP/DNS protection systems. [A]
- Network-safety override: at "Essentially Off" sensitivity, the rule still triggers "at exceptional levels to ensure the safety and stability of the Cloudflare network" — the provider's own protection trumps customer preference at extreme scale. [A]
- Attack coverage table (sample): reflection/amplification (memcached, SSDP, CHARGEN, NTP-class), floods (SYN, ACK, RST, UDP, ICMP, GRE, ESP, QUIC), DNS (query flood, NXDOMAIN, water torture, random prefix, laundering), HTTP (flood, cache busting, slowloris, HTTP/2 rapid reset & MadeYouReset, TLS/SSL exhaustion, botnets), carpet bombing. Email protocols (SMTP/IMAP/POP3) explicitly not covered. [A]

## Product B — AWS Shield (Standard / Advanced)

Key observations:

- Two-tier packaging: Shield Standard automatic at no extra charge for all AWS customers; Shield Advanced paid subscription for higher protection. [A]
- Attack classes detected: network volumetric (L3), network protocol (L4, e.g. TCP SYN flood exhausting connection state on servers/load balancers/firewalls), application layer (L7, floods of valid queries). [A]
- Detection: AWS operates service-level detection systems (network-wide) plus resource-level detection per protected resource; anomaly creates a separate event per affected resource; events named by attack vector or "Volumetric" when volume-based. [A]
- Baseline dependence: infra-layer events reported after ≥15 min of protection; L7 detection accuracy best after ~30 days of observed expected traffic. [A]
- Mitigation: infrastructure mitigations at AWS network border and edge locations; inline and always-on; traffic rerouted through mitigation systems at each ingress; explicitly no rerouting to external/remote scrubbing centers (latency rationale). [A]
- L7 mitigation via AWS WAF integration: associate a WAF web ACL with the protected resource; automatic application-layer DDoS mitigation enforces WAF rate limiting on known DDoS sources and adds/manages custom WAF protections (count or block); rate-based rules can mitigate before detection level. [A]
- Advanced capabilities: health-based detection (Route 53 health checks inform detection/mitigation, reduce false positives; required for proactive engagement); protection groups (logical groupings of resources, membership criteria auto-include new resources; a resource can belong to multiple groups); enhanced visibility (real-time metrics, reports via API/console/CloudWatch); centralized management via Firewall Manager; SRT (Shield Response Team, human experts, contact during attacks, create/manage custom mitigations); proactive engagement (SRT contacts customer when health check unhealthy during a detected event); cost protection (service credits for attack-caused bill spikes). [A]
- Console surfaces: global threat dashboard (aggregated activity ~2 weeks), account event summary (prior year), Events page (current status e.g. "Mitigation in progress", attack vectors, start time, duration), event summaries + details, CloudWatch metrics + alarms, notifications. [A]

## Product C — Azure DDoS Protection

Key observations:

- Explicit layer scope: protects L3/L4 only; for L7 "you need to add protection at the application layer using a WAF offering". [A]
- Always-on monitoring of traffic patterns "24 hours a day, 7 days a week"; mitigation starts "instantly and automatically" once attack detected. [A]
- Adaptive real-time tuning: ML-based traffic profiling learns the application's traffic over time and selects/updates the most suitable profile. [A]
- Mitigation policy object: three auto-tuned policies (TCP SYN, TCP, UDP) per public IP of protected resources in the enabled vnet; thresholds auto-configured via ML profiling; mitigation occurs for an IP under attack only when policy threshold is exceeded. Custom policy (preview) lets users fine-tune thresholds per protocol. [A]
- Attack analytics: detailed reports in five-minute increments during an attack; complete summary after attack ends; mitigation flow logs streamable to Sentinel/SIEM. [A]
- Metrics via Azure Monitor; alerting configurable at attack start, stop, and duration; integrates with Azure Monitor logs, Splunk, Storage, email, portal. [A]
- DDoS Rapid Response (DRR): human team access during active attack (investigation + post-attack analysis). [A]
- Tiers: DDoS Network Protection (vnet-level plan, tenant-wide) vs DDoS IP Protection (pay-per-protected-IP; adds DRR, cost protection, WAF discounts). [A]
- Turnkey/native: enable on vnet or public IP; no application changes; platform understands resources and configuration. Cost guarantee: service credits for data-transfer/scale-out costs from documented attacks. [A]
- For non-vnet services, default infrastructure-level protection applies (common network-layer attacks). [A]

## Product D — NETSCOUT Arbor (AED / Sightline / TMS / Arbor Cloud / AEM)

Key observations (structural level; product-page evidence):

- Product family spanning deployment models: Arbor Edge Defense (AED) = on-prem, inline, stateless, always-on appliance deployed "between your internet router and firewall"; Arbor Sightline = carrier/ISP-scale network detection; Arbor Threat Mitigation System (TMS) = mitigation; Arbor Cloud = cloud scrubbing for large volumetric attacks; Arbor Enterprise Manager (AEM) = centralized management/reporting console for AED fleets. [B-structure]
- Positioning vs upstream protection: ISPs pass through sub-1 Gbps attacks; CDNs can't mitigate direct-to-origin attacks; cloud protection covers only cloud workloads — AED "completes" them. Hybrid on-prem + cloud is called an industry best practice. [B]
- Cloud signaling: AED automatically signals Arbor Cloud to divert/scrub volumetric attacks that overwhelm the internet circuit — integration of on-prem mitigation with cloud scrubbing. [B]
- Beyond-DDoS scope on the appliance: inbound scanning/brute-force blocking and outbound C2 blocking using ATLAS Intelligence Feed / third-party feeds; CDN-aware mitigation (countermeasures per source exploiting CDN proxies); firewall protection from state-exhaustion attacks (removes nuisance traffic ahead of firewalls). [B]
- AI/ML adaptive protection: detect new attacks, classify their nature, recommend countermeasures, automatically mitigate "if required" — with emphasis on evidence-based, explainable, auditable automation ("transparent automation", "glass box" framing). [B]
- Audiences: enterprises (keep traffic control in own hands) and service providers (multi-tenant, carrier-grade; managed DDoS protection sold as a revenue-generating service to their customers). [B]
- Named attack types: DNS water torture, carpet bombing, state exhaustion, volumetric floods. [B]
- Global threat intelligence (ATLAS) derived from internet-wide visibility feeds the products (feed subscription model). [B]

## Cross-product Comparison

| Dimension | Cloudflare | AWS Shield | Azure DDoS | NETSCOUT Arbor |
|---|---|---|---|---|
| Protected objects | zones (L7 services), prefixes/networks (Magic Transit) | AWS resources (CloudFront, Route 53, ALB, Elastic IPs...) + protection groups | public IPs / vnets in Azure | network edge, prefixes, data centers, carrier networks (fleet via AEM) |
| Standing posture | always-on automatic (autonomous systems) | always-on automatic (Standard + Advanced) | always-on automatic (24/7 monitoring) | always-on inline appliance + on-demand cloud scrubbing via signaling |
| Detection basis | managed rules + traffic profiling (7-day profiles, ML) | signature/vector + volume anomaly per resource, service-level systems | ML auto-tuned threshold policies per IP (TCP SYN/TCP/UDP) | threat-intel + behavioral/statistical detection (carrier scale), AI classification |
| User-configurable | rule overrides: action + sensitivity + expressions | WAF web ACL association, auto-mitigation on/off, protection groups, health checks | tier selection; custom thresholds (preview) | appliance policies, countermeasures, AEM central policy |
| Mitigation actions | block, challenges, log, connection close, undisclosed dynamic actions | drop/reroute at border; WAF rate limiting; auto WAF rule management; count/block | threshold-exceeding traffic mitigation at platform scale | stateless inline filtering; cloud scrubbing divert; countermeasures per source |
| Attack event record | security events (filterable), log export | Events page: status, vectors, start, duration; metrics; summaries/details | 5-min reports during attack + post-attack summary; flow logs | AEM reporting, alerting, attack records |
| Alerting/integration | notifications, Logpush/GraphQL | CloudWatch alarms, SNS, Security Hub | Azure Monitor alerts, Sentinel/Splunk/email | SIEM/central console integrations |
| Human expert response | (professional services; not a documented core tier in fetched docs) | SRT + proactive engagement | DRR team | support/managed services (product-page level) |
| Cost posture | unmetered on all plans; add-on tiers | free Standard; paid Advanced; service credits | tiers (vnet plan vs per-IP); cost guarantee credits | license/appliance + subscription + managed service |
| L7 story | bundled (HTTP rulesets) | via WAF integration (web ACL + auto mitigation) | explicitly delegated to WAF | L7 in-line for small/short attacks; CDN-aware; recommends layered stack |

Repeated across the sample (evidence B unless noted):

1. A protected-surface definition: specific assets (IPs/prefixes/zones/resources) the platform takes responsibility for.
2. Standing, automatic detection producing identified attack events (all four).
3. Executable mitigation on/near the traffic path: drop/filter, rate-limit, challenge, connection control, or divert-to-scrubbing (all four).
4. Availability as the success criterion (all four frame the problem as keeping the service available).
5. Vendor-maintained detection content (managed rulesets / auto-tuned policies / threat-intel feeds) with user tuning on top (all four).
6. Learned baselines/profiling of normal traffic as a detection input (Cloudflare, AWS, Azure; NETSCOUT AI framing).
7. Attack event records with lifecycle + metrics + reports + alerting (all four).
8. False-positive management as a designed concern (log-first validation, health-based detection, proactive FP checks).
9. Human expert response available at higher tiers (AWS SRT, Azure DRR directly documented; NETSCOUT support; Cloudflare professional services).
10. Tiering: free/default baseline protection vs paid/enhanced protection (Shield Standard/Advanced; Azure tiers; Cloudflare plans; AED vs managed services).

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

A DDoS Protection Platform is recognizable by exactly this structure, held jointly:

1. **Protected traffic surface** — the platform is explicitly bound to identified internet-facing assets (network prefixes, IPs, applications, DNS infrastructure) for which it takes protection responsibility. (Remove → generic network tooling.)
2. **Standing attack detection** — continuous evaluation of traffic toward those assets against attack signatures, thresholds, and/or learned baselines, yielding identified attack events. (Remove → load balancer/CDN that merely absorbs traffic; or pure monitoring.)
3. **Traffic-path mitigation execution** — the platform executes, orchestrates, or automatically hands off enforcement (filter/absorb/drop attack traffic, sparing legitimate traffic) rather than only alerting. (Remove → Network Monitoring / alerting tool.)
4. **Availability objective** — the protection goal is preservation of service availability under volumetric/protocol/application-layer flooding, not content-policy enforcement. (Remove → WAF content-security framing; the availability-vs-content objective is what keeps this a distinct Type.)

All four are load-bearing. Detection without mitigation = monitoring; mitigation without standing detection = a bare filter/firewall; no protected surface = generic security product; content objective = WAF.

Historical check (per §24 spirit): older and differently-positioned products still fit — Arbor-style detection platforms with operator-triggered BGP divert to scrubbing centers (mitigation execution is orchestrated by the platform even when operator-approved), early managed scrubbing services (on-demand variant), simple inline SYN-proxy appliances (thin variant of 1+3; event recording is L1, not required in L0). Bare blackholing/null-routing without attack detection does not qualify (2 fails) — correctly outside the Type. Phone-era/regional differences are not relevant here; the deployment-posture axis (inline vs divert vs cloud) is deliberately NOT in L0.

### L1 — Common Mature Structure

- Vendor-maintained managed detection content (managed rulesets, auto-tuned policies, threat-intelligence feeds), updated by the vendor over time.
- Attack event as a first-class recorded object: start/end, vectors, magnitude, mitigation status, per-resource granularity.
- Dashboards, metrics, alerting (attack start/stop/duration), reports (in-attack and post-attack summaries), exports/integrations (SIEM, log pipelines, monitoring systems, APIs).
- Learned traffic baselines / behavioral profiling (ML or statistical) layered over signature/threshold detection.
- Tunable detection posture per rule/protocol/asset (sensitivity levels, thresholds, scoping expressions) with a safe validate-then-enforce pattern (log-only mode).
- False-positive management machinery (log-before-block, health-based detection, proactive FP checks).
- Tiered packaging: free/default baseline vs paid enhanced protection; unmetered vs metered with cost-credit protection.
- Human expert response (attack-response team) attached to higher tiers.
- Centralized/fleet management for multi-asset estates (protection groups, management consoles).

### L2 — Variant / Optional Structure

- Deployment posture: cloud-edge inline (reverse proxy/anycast), cloud-provider native (platform networking integration), on-prem inline appliance, cloud scrubbing with BGP divert (always-on signaled or on-demand), hybrid combinations. (Deliberately NOT in L0 — the same Type is realized in all.)
- Coverage scope: L3/4-only vs L3–L7-bundled vs L3/4 + delegated L7 (WAF).
- Adjacent security bundling on the same enforcement point: firewall protection, inbound scanning/brute-force blocking, outbound C2 blocking (on-prem appliances).
- Audience/rollout: enterprise self-managed vs ISP/carrier multi-tenant vs MSP managed service (managed DDoS as resale product).
- Pricing model: unmetered-inclusive vs subscription vs per-protected-IP vs appliance license + feed subscription.

### L3 — Vendor-specific (research notes only)

- Cloudflare: sensitivity value names (default/medium/low/eoff); "Essentially Off" network-safety override; managed/interactive challenge; undisclosed "DDoS dynamic" action; 7-day/95th-percentile profile mechanics; proactive FP detection for new rules; plan matrix; Magic Transit/Spectrum/BYOIP; Logpush/GraphQL; explicit non-coverage of email protocols.
- AWS: Shield Standard vs Advanced split; protection groups semantics; Route 53 health-check-based detection; SRT proactive engagement; 15-minute/24-hour/30-day baseline windows; WCU/allotment details; service-credit process; Firewall Manager policies.
- Azure: TCP SYN/TCP/UDP auto-tuned policy triad; five-minute in-attack reports; DRR team; Network vs IP Protection tiers; vnet plan tenancy; custom-policy preview; Sentinel/Splunk connectors.
- NETSCOUT: AED/Sightline/TMS/Arbor Cloud/AEM product split; ATLAS Intelligence Feed; cloud signaling; CDN-aware mitigation; selective decryption; stateless always-on framing; "Under Attack?" engagement path; SPARK positioning claims.

## Rejected Findings (not promoted to the core)

- "Always-on automatic mitigation" as definition: rejected for L0 — on-demand divert-to-scrubbing is an accepted historical and current posture (Arbor Cloud signaling can be event-triggered; Prolexic-class services historically on-demand). The platform must stand ready and execute/orchestrate mitigation; full automation of the trigger is the modern default, not the invariant.
- "ML/AI-based detection" as definition: rejected — signature/threshold/statistical detection satisfies the Type; ML is the modern default flavor.
- "Free baseline tier" as definition: rejected — packaging, not structure.
- "Cloud delivery" as definition: rejected — on-prem appliance realizations fit equally.
- "100 Tbps-class capacity" and similar scale numbers: rejected — vendor-specific, unverifiable, time-varying; belongs nowhere in the canonical doc.
- "Specific policy triads (TCP SYN/TCP/UDP)" — Azure-specific realization of threshold policies.
- WAF feature overlap (bot management, content rules) — belongs to the WAF Type; only the integration seam is documented here.

## Boundary Findings

- **vs Web Application Firewall (WAF):** the sharpest seam, and the fuzziest in the L7 region. WAF's defining object is the application request and its content/policy semantics (exploits, injection, access policy, bot behavior); a WAF without volumetric/L3/4 concern is still a WAF. DDoS platform's defining object is the traffic-level availability threat (volumes, floods, state exhaustion, reflection/amplification) and its mitigation (absorb/drop/rate-limit/scrub). Real products integrate: Shield Advanced's L7 mitigation literally runs inside WAF (web ACLs, rate-based rules); Azure states L7 must come from a WAF; Cloudflare bundles both engines. Discriminator: primary objective (availability under flood vs request-policy enforcement) + whether the platform handles infrastructure-layer (L3/4) attack vectors at all.
- **vs CDN:** CDN's defining job is content delivery/caching/acceleration; DDoS absorption is an emergent side-benefit and marketed add-on. A DDoS platform's defining job is the availability defense; delivery is incidental (or absent — Magic Transit, AED, Shield-Advanced-on-EIP protect without serving content). Reverse-proxy edge products (Cloudflare) blur the surface but the DDoS platform here is the protection system, not the delivery service.
- **vs Network Monitoring / NDR:** monitoring observes, baselines, alerts — but does not execute traffic countermeasures. The moment the product drops/scrubs/rate-limits/diverts attack traffic, it crosses into this Type. Products in the sample explicitly pair with SIEM/monitoring rather than replacing it.
- **vs Network Security Platform / firewall:** firewalls enforce per-flow policy and are themselves common victims (state exhaustion). DDoS platforms specifically handle volume-scale and state-exhaustion attacks at a level firewalls cannot, and are commonly placed ahead of them (AED between router and firewall; "protect the firewall" is a documented use case).
- **vs Incident Management / on-call:** process-and-communication layer over response; the DDoS platform is the technical enforcement layer. Integrations (alerts → chat/SIEM) are the seam.
- **vs API Security / Bot management:** request-identity and abuse-quality concerns; adjacent L7 specializations that integrate with (rather than constitute) the DDoS platform.

"Remove what and it becomes another Type": remove mitigation execution → Network Monitoring; remove volumetric/availability framing and keep request content filtering → WAF; remove attack detection and keep traffic absorption → CDN/load balancing; remove the protected-surface binding → generic threat-intelligence product.

## Uncertainties

- Akamai Prolexic (the archetype of the scrubbing-center/BGP-divert philosophy) could not be fetched; the on-demand-divert pole is covered only via NETSCOUT cloud signaling and AWS/Azure mentions of scrubbing-center trade-offs. Assertion strength for the on-demand-divert variant is accordingly reduced (kept in L2, qualified).
- NETSCOUT operational specifics (rule semantics, console workflows) are from product pages only; structural claims only.
- Pure-play standalone DDoS vendors of the 2020s market (e.g., scrubbing pure-plays, regional providers) were not sampled; the sample is four large-platform products. The L0 was stress-tested against the appliance/divert models to compensate.
- Exact alert-channel lists, tier contents, and pricing mechanics vary and are time-sensitive; intentionally excluded from the final document.
- The extent to which modern pure-play products bundle L7 engines could not be independently verified beyond the sampled products' own framing.

## Final Synthesis

The DDoS Protection Platform is an availability-defense application: it binds itself to a protected traffic surface (network prefixes, IPs, applications, DNS), continuously evaluates arriving traffic against signatures, thresholds, and learned baselines to identify attack events, and executes or orchestrates countermeasures in the traffic path — absorbing, filtering, dropping, rate-limiting, challenging, or diverting traffic to scrubbing capacity — so the protected service stays available. Everything else commonly shipped (managed rulesets, ML profiling, dashboards, alerting, response teams, cost credits, fleet consoles, WAF integration, tiered packaging) is mature structure or variant posture, not definition. The Type is defined by deployment-agnostic structure: what varies across the market is where enforcement sits (edge, cloud platform, on-prem appliance, scrubbing center) and how automated the trigger is — not what the system is.
