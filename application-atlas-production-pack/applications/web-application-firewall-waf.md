# Web Application Firewall / WAF

## Overview

A **Web Application Firewall (WAF)** is an inline, application-layer security control that intercepts HTTP(S) traffic destined for a web application, inspects each request against a configured policy of application-attack rules, enforces a per-request disposition — allow it through, block it, or apply an intermediate action such as counting it or challenging the client — and records the outcomes as security events the operator can review.

It solves a problem that network firewalls cannot: web attacks (injection, scripting, protocol abuse, credential and bot abuse) arrive inside legitimate-looking HTTP requests on ports the firewall happily lets through. The WAF reads the application layer — URLs, parameters, headers, bodies — and decides, request by request, whether the traffic is safe to forward.

The defining core is small:

```text
Inline interception of HTTP(S) traffic to a protected application
└── Application-layer attack inspection
    └── Policy-driven disposition (allow / block / intermediate actions)
        └── Security event recording
```

Everything else commonly associated with WAFs — where the inspection runs (cloud service, edge network, appliance, web-server module), vendor-maintained rule subscriptions, machine-learning scoring, bot management, plan-based packaging — is widespread in current products but is not what makes a WAF a WAF. An open-source module inside a web server with a community rule set satisfies the same definition; so does a managed edge service.

## Users & Context

Primary users are the people responsible for keeping a production web application or API safe and available:

- **Security engineers / AppSec teams** — define the protection policy, choose and tune managed rule sets, investigate security events, decide what gets blocked.
- **Platform / DevOps / SRE teams** — attach the WAF to the application's delivery path (load balancer, CDN, ingress, reverse proxy), automate configuration through APIs or infrastructure-as-code, and watch for traffic impact.
- **Application owners** — consume the security events and dashboards for their application, request exceptions when legitimate traffic is blocked.

Secondary concerns sit with **compliance functions**: WAF controls and their logs are commonly used as evidence for payment-card and data-protection requirements, and vendors position the product accordingly.

The working context is always the same shape: the WAF stands between the internet and the application's origin. Requests reach the WAF first; only dispositions of "allow" continue to the application. The operator's daily loop is reviewing what was blocked or flagged, distinguishing attacks from false positives, and adjusting the policy.

## Core Model

### The Defining Core

Four structures, jointly held. Remove any one and the product is no longer a WAF:

- **Inline interception point.** The WAF sits in the request path of the protected application — as a reverse proxy, an edge service, an appliance, or a module inside the web server itself. This is what separates it from tools that test or analyze an application from outside the traffic path.
- **Application-layer attack inspection.** Requests (and, in many products, responses) are evaluated against criteria that target web-application attack patterns — injection and scripting payloads, protocol violations, evasion encodings, malicious automation — rather than only network-layer properties like addresses and ports.
- **Policy-driven disposition with enforcement.** A configured policy of rules decides each request's outcome: forward it, block it, or apply an intermediate action (count it without blocking, verify the client is human, throttle it). The policy also defines what happens to traffic no rule matches. The *capability* to enforce is definitional; operating in a monitor-only mode is a configuration choice, not a different product.
- **Security event recording.** Matches and dispositions are recorded as security events and logs. Without this record the operator could not distinguish real attacks from false positives, and the tuning loop that defines WAF operation could not function.

### The Policy Container

Every product organizes its rules inside a container that is bound to one or more protected applications. The concept is stable; the implementations differ:

```text
Concept:      Policy container bound to a protected application
Implementations:
              a web access control list associated with platform resources
              ordered rulesets attached to a protected zone/domain
              a declarative security policy compiled into the delivery tier
              a console-managed policy per application
              rule files loaded into a web-server module
```

Inside the container live two kinds of rules:

- **Managed rules** — maintained by the vendor (or, in the open-source case, by a community project), covering known attack techniques and newly disclosed vulnerabilities, and updated on the vendor's schedule without operator effort. Managed rule sets are the practical reason most deployments get value on day one.
- **Custom rules** — written by the operator, usually as conditions over request properties (origin, path, headers, body content, geography) combined with an action. Custom rules express what is specific about *this* application: which endpoints are sensitive, which clients are trusted, which countries are unacceptable.

A third, older tradition — the **positive security model** — declares what the application *is* supposed to receive (its URLs, parameter names, types, lengths, allowed methods and file types) and treats deviations as violations. Some products center the policy on this declared structure; others treat it as one more rule source alongside signatures.

### The Request Disposition

Each request that flows through the WAF receives exactly one disposition, produced by evaluating the policy:

```text
Request arrives
→ evaluated against the policy's rules, in a defined order
→ first decisive match (or an aggregated score crossing a threshold) determines the outcome
→ disposition applied:
     allow        — forward to the application
     block        — refuse the request (error page or custom response)
     count/log    — record the match without acting (monitoring)
     challenge    — verify the client is a human or legitimate browser
     throttle     — rate-based action when a client exceeds a defined request rate
→ outcome recorded as a security event
```

Two evaluation models exist across products, and many products combine them:

- **Ordered rules with terminating actions** — rules run in sequence; a terminating action (block, challenge, redirect) ends evaluation; non-terminating actions (log, label) let later rules still run.
- **Scored evaluation** — individual detections add to a per-request score (signature matches, violation severity, machine-learning scores); the configured action fires when the score crosses a threshold.

### Security Events

Every disposition produces a record: what matched, which rule or signature, the action taken, and enough request context to judge whether the decision was right. Products surface these records as event viewers and dashboards, commonly alongside analytics over *all* traffic — including requests that were never touched by any rule — so the operator can see both what was mitigated and what was merely observed.

### Standard Capabilities of Mature Products

These are near-universal in current products. They make a WAF practical; they do not define the Type:

- vendor-updated **managed rule sets** with scheduled and emergency updates
- **rate-based rules** and brute-force throttling on sensitive endpoints
- **IP and geography controls** (allow/deny lists, reputation feeds, country rules)
- **bot detection and mitigation**, at depths ranging from a built-in setting to a paid add-on to a separate sibling product
- **human-verification challenges** (CAPTCHA-style or silent browser checks) as an intermediate action
- **tuning machinery**: exceptions, exclusions, rule overrides, monitor/count modes, staged rollout of new signatures
- **log export** to SIEM and data platforms
- **response-side inspection** in some products (sensitive-data or leakage checks on what the application sends back)

## How It Works

The operational life of a WAF is a loop, not a single flow:

### 1. Attach the policy to the application

```text
Create the policy container
→ add managed rule set(s) and/or custom rules
→ set the default action for unmatched traffic
→ bind the container to the protected application
   (load balancer, CDN distribution, domain/zone, reverse proxy, web server)
→ traffic begins flowing through inspection
```

Binding is the act that turns a rule set into protection: the same policy can often serve several applications, and an application is normally protected by one active policy at a time.

### 2. Start in monitoring, then enforce

Because wrong decisions block real customers, mature products support a **monitoring posture**: rules run, matches are recorded as events, but nothing is blocked. The recommended pattern across products is to observe real traffic first, then switch rules to blocking once the false-positive rate is understood. Some managed services with pre-tested rule sets are positioned for blocking from the start; the monitor-first pattern remains the general discipline.

### 3. Tune against false positives

```text
Review security events
→ identify legitimate requests that matched a rule (false positives)
→ narrow the rule's scope, add an exception for that traffic,
   or override the rule's action
→ re-observe
```

Tuning surfaces differ by product — skip-rules, exclusions, scope-down conditions, per-rule action overrides, signature staging — but the loop is the same everywhere. False positives are the central operational cost of the Type; the entire event-and-tuning machinery exists to manage them.

### 4. Keep the rule set current

Managed rule sets are updated by the vendor as new vulnerabilities and attack techniques appear; the operator's job is to review what changed and adjust exceptions. Updating WAF rules to mitigate a newly disclosed vulnerability before the application code itself is fixed is a standard practice (**virtual patching**) and one of the main reasons organizations keep a WAF in front of applications they cannot patch quickly.

### 5. Watch and respond

Dashboards summarize dispositions over time — blocked, allowed, challenged, throttled — by rule, by attack type, by source. Security teams feed event logs into their SIEM, investigate incidents with the recorded request context, and adjust policy as the application changes.

### Capability tiers

- **Defining core** — inline interception, application-layer attack inspection, policy-driven enforcement, security event recording.
- **Standard capabilities** — managed rule sets, custom rules, rate limiting, IP/geo controls, bot detection, challenges, tuning machinery, log export, dashboards.
- **Optional / variant** — response inspection, API- and protocol-specific protections (GraphQL, gRPC, JSON/XML schema enforcement), credential-leak and account-takeover checks, machine-learning scoring, AI-era bot and LLM-abuse features, compliance reporting packages.

## Interfaces

The operator-facing surfaces are consistent across products, even where the names differ:

### Policy / rule editor

The configuration surface for the policy container.

- managed rule sets with enable/disable and per-rule action settings
- custom rule builder: conditions over request properties + chosen action
- default action for unmatched traffic
- primary actions: create/edit/delete rules, reorder, enable rule sets, set actions

### Security events viewer

The investigation surface for what the WAF did.

- list of matched requests with rule, action, timestamp, and request context
- filtering by action, rule, source, time
- primary actions: inspect a request, trace why it matched, jump to the rule to tune it

### Analytics / dashboard

The posture surface over all traffic.

- disposition totals over time (allowed / blocked / challenged / logged)
- top rules, top attack types, top sources
- traffic that no rule touched (for spotting unmitigated risk)

### Tuning surfaces

- exceptions / skip rules / exclusions scoped to specific traffic
- per-rule or per-ruleset action overrides
- monitor-vs-block switches, signature staging

### Logs and automation

- log export to SIEM/data platforms
- APIs, CLIs, and infrastructure-as-code providers for managing policy as code — common in platform-team environments

## Important Rules / Behaviors

### The default action governs unmatched traffic

The policy must say what happens to requests no rule matched — typically allow (blocklist posture) or block (allowlist posture). This single setting shapes the whole false-positive economy of the deployment.

### Rule order and termination matter

Where rules are evaluated in order, the first terminating action wins and later rules never see the request; where evaluation is scored, individual matches accumulate toward a threshold. Operators must understand which model their product uses — the same rule set produces different outcomes under each.

### Blocking is a graduated decision, monitoring is a mode

Products distinguish acting on a request (block, challenge) from recording it (count, log, alarm). The same rule can usually be flipped between the two. Deployments commonly run new rules in recording mode before enabling enforcement.

### False positives are the structural cost

Every blocking decision risks blocking a legitimate user. The tuning machinery (exceptions, overrides, staging) is not an accessory; it is the mechanism that makes blocking mode usable at all. Managed rule sets are tuned by their maintainers to minimize false positives, but per-application exceptions remain a normal part of operation.

### Managed rules update on the vendor's schedule

Rule content, new signatures, and zero-day responses arrive from the vendor without operator action; operators manage *exceptions and posture*, not the signatures themselves. In the open-source case, the community rule set plays this role on a release schedule.

### Inspection has limits

Products inspect request content up to defined size limits; content beyond the limit may not be fully analyzed. Configuration changes can also take a short period to propagate across a distributed enforcement fleet in some products. Both facts push operators toward explicit handling of oversized or edge-case traffic rather than assuming total coverage.

## Variants

The Type is implemented across several axes. A variant stays a variant as long as the defining core still describes it:

- **By deployment substrate** — platform-attached cloud service (policy bound to a cloud load balancer, CDN distribution, or API gateway); edge network service (inspection at a global proxy network in front of the origin); on-premises appliance or gateway (for legacy applications and data-sovereignty requirements); web-server module (the engine lives inside the application's own server); in-cluster deployment for Kubernetes environments.
- **By policy philosophy** — signature/negative-security model (match known attack patterns); positive-security model (declare the application's expected structure, flag deviations); expression-language custom rules; scored evaluation (anomaly scores, violation ratings, ML scores). Most products mix several.
- **By operating posture** — self-managed (operator tunes everything) vs managed-service (vendor's research team writes and tests rules, positions the product for blocking from day one).
- **By packaging** — standalone WAF product; WAF as a capability inside a broader application-security or delivery platform; open-source engine plus community rule set.
- **By customer tier** — from free plan tiers with a basic managed rule set up to enterprise tiers with account-wide policies, advanced detections, and log export.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| DDoS Protection Platform | closest adjacent; frequently integrated | DDoS protection's defining object is the traffic-level availability threat (volume floods, state exhaustion) and infrastructure-layer vectors a WAF does not address; the WAF's defining object is the application request and its content/policy semantics. The seam is L7 flood mitigation — rate-based rules and challenges run inside WAF engines, and DDoS platforms commonly integrate with, manage, or delegate L7 defense to the WAF |
| API Security Platform | adjacent, overlapping traffic | WAF applies generic HTTP attack rules to API traffic too; API security adds API discovery, endpoint/schema inventories, and API authentication management. Deep GraphQL/gRPC checks inside a WAF policy are a depth variant, not a different Type. |
| Network Security Platform | same family, different layer | L3/L4 flow policy between network endpoints; the WAF inspects L7 application content. The shared word "firewall" hides a fundamentally different inspection layer and rule vocabulary. |
| Application Security Platform (SAST / DAST) | complementary, different phase | static/dynamic testing finds vulnerabilities in code or a running app, out of the traffic path; the WAF protects runtime traffic. The bridge is virtual patching — WAF rules mitigating a known vulnerability before the code is fixed. |
| CDN Management | adjacent, often co-resident | delivery, caching, and routing are the CDN's core; the WAF's core is the security policy decision. WAF capability is frequently bundled into CDN products, but stripping the security policy leaves a CDN, not a WAF. |
| Load Balancer Management | adjacent, often co-resident | traffic distribution and health are the load balancer's core; WAF inspection is a security function attached to the same delivery path. |
| Account Abuse Protection / Bot management | overlapping capability, separate Type at depth | every sampled WAF carries some bot detection, but dedicated bot management goes deeper into fingerprinting and behavioral analysis; depth varies from built-in setting to paid add-on to separate product. |

The most important boundary is with **DDoS protection**, because the two are sold together and both "protect the application." The discriminator is the primary objective: availability under volumetric/protocol assault versus request-policy enforcement on application content — and whether the product carries infrastructure-layer (L3/L4) defense at all. The seam needs care because modern L7 mitigations (rate-based rules, challenges) run inside WAF engines: a WAF's rate-based rule remains a per-request policy decision, not volumetric absorption, while DDoS platforms that need L7 defense commonly attach to or delegate it to the WAF.

## Representative Products

- **AWS WAF** — cloud-native WAF attached to platform resources (CDN distributions, load balancers, API gateways); web-ACL policy model with managed rule groups and count-mode tuning.
- **Cloudflare WAF** — edge-network WAF with expression-language rulesets, vendor-managed rulesets (including an implementation of the OWASP Core Rule Set), and plan-tiered features from free to enterprise.
- **F5 WAF for NGINX** (formerly NGINX App Protect WAF) — software WAF embedded in the NGINX delivery tier; declarative policy with a violations model and violation-rating blocking; VM, container, and Kubernetes deployments.
- **Imperva WAF** — dedicated security vendor spanning Cloud WAF (SaaS), WAF Gateway (on-premises), and Elastic WAF (Kubernetes); managed-service posture with vendor-researched rules.
- **ModSecurity + OWASP Core Rule Set** — the open-source archetype: a web-server WAF module with a rules language, paired with the community-maintained OWASP Core Rule Set that several commercial products also implement.

The defining core was checked against the open-source module and appliance-heritage forms to avoid over-fitting the definition to the current cloud/edge implementation.

## Sources

Research date: **2026-09-09**

- AWS WAF documentation — https://docs.aws.amazon.com/waf/ (Developer Guide: how it works, web ACLs, rules, intelligent threat mitigation)
- Cloudflare WAF documentation — https://developers.cloudflare.com/waf/ (Get started, Concepts, Managed Rules)
- F5 WAF for NGINX documentation — https://docs.nginx.com/waf/ (Overview, Violations)
- Imperva WAF product page — https://www.imperva.com/products/web-application-firewall-waf/
- ModSecurity project — https://modsecurity.org/
- OWASP Core Rule Set — https://owasp.org/www-project-modsecurity-core-rule-set/

> Sourcing limitation: the Imperva documentation portal could not be fetched from the research environment (JavaScript application portal). Imperva observations rest on the official product page only; no precise operational claims about that product are made in this document. Vendor efficacy statistics observed on marketing pages were not used as evidence.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
