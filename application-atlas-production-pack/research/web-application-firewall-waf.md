# Research Notes — Web Application Firewall / WAF

Research date: 2026-09-09
Slug: `web-application-firewall-waf`
Directory leaf: "Web Application Firewall / WAF" (§15 Cybersecurity, Identity & Trust)

## Research Goal

Understand what a Web Application Firewall actually is as an Application Type: the objects inside its world, the request-evaluation flow, the operating lifecycle (deploy → tune → monitor → update), the interfaces operators use, and the boundaries against neighboring security Types (DDoS protection, API security, network security, application security testing).

## Initial Boundary (working hypothesis before research)

- A WAF is an inline security control placed in the HTTP(S) request path of a web application that inspects requests (and sometimes responses) against application-layer attack criteria and enforces a disposition (allow / block / intermediate actions).
- Nearest neighbors suspected: DDoS Protection Platform (volumetric availability), API Security Platform (API-specific discovery/schema), Network Security Platform (L3/L4), Application Security Platform / SAST / DAST (pre-production code testing), CDN Management and Load Balancer Management (delivery functions that often bundle WAF).
- Unknowns going in: how products model the policy container (per-app policy vs per-zone rulesets vs platform-attached ACL); how blocking vs monitoring modes work; how false-positive tuning is structured; how much bot management is inside the WAF vs a separate Type.

## Research Questions

1. What are the core objects? (protected asset, request, rule, rule set/policy, security event, exception/tuning)
2. How does a request flow through the WAF? What actions exist?
3. What is a rule? Managed rule sets vs custom rules? What role does OWASP CRS play?
4. What deployment substrates exist? (cloud service, edge proxy, appliance, web-server module, in-cluster)
5. How do blocking vs monitoring (count/alarm) modes work? How is the false-positive loop handled?
6. What attack coverage vocabulary is used? (OWASP Top 10, signatures, scoring)
7. What is the operational lifecycle? (deploy, tune, update rule sets, virtual patching)
8. What interfaces exist? (console, event viewer, rule editor, API/CLI/IaC)
9. Which rules matter? (default action, rule precedence, rate limits, IP reputation, geo)
10. Where are the boundaries vs DDoS / API security / network firewall / CDN / testing tools?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| AWS WAF | hyperscaler cloud-native; policy attached to platform resources | dominant cloud-native pattern; rich official docs |
| Cloudflare WAF | edge SaaS; expression-language rulesets; free→enterprise plan ladder | dominant edge pattern; rich official docs |
| F5 WAF for NGINX (ex NGINX App Protect WAF) | enterprise software WAF embedded in the delivery tier (NGINX); declarative policy + violations model | enterprise/on-prem heritage; deep policy model docs |
| Imperva WAF (Cloud WAF / WAF Gateway / Elastic WAF) | dedicated security vendor; managed-service posture; cloud + appliance + Kubernetes forms | dedicated-vendor pattern; three deployment forms |
| ModSecurity (+ OWASP CRS) | open-source web-server module; the historical origin; engine + rules language | historical/market-sample check; CRS is the common rule-set baseline |

## Sources

Fetched 2026-09-09 (all reachable unless noted):

- AWS WAF documentation root — https://docs.aws.amazon.com/waf/ (Tier 1)
- AWS WAF Developer Guide: how it works — https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html (Tier 1)
- AWS WAF Developer Guide: configuring protection (web ACL) — https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html (Tier 1)
- AWS WAF Developer Guide: rules — https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html (Tier 1)
- AWS WAF Developer Guide: intelligent threat mitigation — https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections.html (Tier 1)
- Cloudflare WAF docs root — https://developers.cloudflare.com/waf/ (Tier 1)
- Cloudflare WAF: get started — https://developers.cloudflare.com/waf/get-started/ (Tier 1)
- Cloudflare WAF: concepts — https://developers.cloudflare.com/waf/concepts/ (Tier 1)
- Cloudflare WAF: managed rules — https://developers.cloudflare.com/waf/managed-rules/ (Tier 1)
- F5 WAF for NGINX docs root — https://docs.nginx.com/waf/ (Tier 1)
- F5 WAF for NGINX: overview — https://docs.nginx.com/waf/fundamentals/overview/ (Tier 1)
- F5 WAF for NGINX: violations — https://docs.nginx.com/waf/policies/violations/ (Tier 1)
- Imperva WAF product page — https://www.imperva.com/products/web-application-firewall-waf/ (Tier 2)
- ModSecurity project site — https://modsecurity.org/ (Tier 1/2 hybrid: official project site)
- OWASP CRS project page — https://owasp.org/www-project-modsecurity-core-rule-set/ (Tier 1 for the rule set)

Source-access limitation: the Imperva documentation portal (docs.imperva.com, now a Thales docs hub) is a JavaScript application whose content could not be fetched from the research environment (2 attempts). Imperva observations therefore rest on the official product page (Tier 2) only; operational detail for Imperva is kept weaker than for the other products and no precise operational claims are made from it. Marketing claims (e.g., "over 90% of customers deploy in blocking mode", "near-zero false positives") were observed but are treated as vendor positioning, not evidence.

## Product Observations

Evidence layer noted per observation: **A** = directly observed in that product's official docs; **B** = cross-product commonality.

### AWS WAF

- **A** — Definition: "a web application firewall that lets you monitor the HTTP(S) requests that are forwarded to your protected web application resources." Protected resource types: CloudFront distributions, API Gateway REST APIs, Application Load Balancers, AppSync GraphQL APIs, Cognito user pools, App Runner, Amplify, Verified Access, Bedrock AgentCore Gateway.
- **A** — Policy container: the **web ACL** (new console: "protection pack"). You create a web ACL, define rules in it, set a **default action** (block or allow) for requests no rule matched, then **associate** the web ACL with one or more protected resources. Associated resources forward incoming requests to AWS WAF for inspection.
- **A** — Rule = inspection **statement** + **action**. Actions: Allow, Block, Count, CAPTCHA, Challenge. Rule statements can nest with logical AND/OR/NOT. Inspection criteria include: malicious script patterns (XSS), malicious SQL patterns (SQLi), IP origin, country/geo origin, string/regex match on request components, size of request parts, and **labels** added by prior rules.
- **A** — **Rule groups** are reusable containers of rules; AWS Managed Rules and Marketplace sellers provide **managed rule groups**; customers can define their own rule groups. Rules exist only inside a web ACL or rule group (not standalone resources).
- **A** — **WCUs (web ACL capacity units)** measure the operating resources rules consume; a cost/complexity budget for the policy.
- **A** — **Rate-based rules**: block/count requests that exceed a specified rate in a time window.
- **A** — Dashboards: summary (request counts by rule/action/traffic type), protection activity (traffic flow through rules, rule order effects), action totals, all-rules metrics, overview (traffic by origin/attack type/device, top rules, bots, L7 DDoS).
- **A** — Testing/tuning guidance: test changes in staging, then run in **count mode** against production traffic before enabling blocking. Explicit production-traffic-risk warning.
- **A** — Intelligent threat mitigation (separately priced): Bot Control, Account Takeover Prevention (ATP), Account Creation Fraud Prevention (ACFP), L7 DDoS prevention, CAPTCHA/Challenge, client-side tokens.
- **A** — Logging: web ACL traffic logging with data-protection options; propagation of changes takes seconds to minutes; on internal errors CloudFront tends to fail open while regional services fail closed.
- **A** — Vendor-specific extras: AI traffic monetization (charging AI bots per request), Firewall Manager for multi-account policy rollout, labels as inter-rule communication.

### Cloudflare WAF

- **A** — Definition: "checks incoming web and API requests and filters undesired traffic based on sets of rules called rulesets." Runs on the Cloudflare global network (edge proxy in front of the zone's origin).
- **A** — **Rule** = filter (expression over request properties: IP, URL path, headers, body) + **action**. **Ruleset** = ordered set of rules evaluated in sequence; the first rule with a **terminating action** (Block, Managed Challenge, Redirect) stops evaluation; non-terminating actions (Log) let evaluation continue.
- **A** — Main components: **Managed Rules** (signature-based, vendor-maintained, e.g. Cloudflare Managed Ruleset with weekly changelog + emergency zero-day releases), **traffic detections** (attack score, bot score, leaked credentials, malicious uploads, AI Security for Apps — these only *score* requests and never act on their own), and **user-defined rules** (custom rules, rate limiting rules).
- **A** — **Rule execution order** across features: IP Access rules → custom rules → rate limiting rules → managed rules. Phases are explicit (`http_request_firewall_custom`, `http_ratelimit`, `http_request_firewall_managed`).
- **A** — **Cloudflare OWASP Core Ruleset**: the vendor's implementation of the OWASP ModSecurity Core Rule Set; **score-based** — each matching rule adds to a cumulative threat score; action executes when the score exceeds a threshold; configurable **paranoia level (PL1–PL4)** and score threshold. Documented as prone to false positives.
- **A** — **Tuning**: **exceptions** (skip rules that bypass managed rulesets under conditions) and **overrides** (change a rule's action or disable rules; at ruleset/tag/rule grain). Exceptions take priority over overrides.
- **A** — Visibility: **Security Events** (mitigated requests with sampled logs) and **Security Analytics** (all incoming traffic, including unaffected). Enterprise can export logs.
- **A** — Deployment grain: per-**zone** (domain) configuration for all plans; **account-level** rulesets for Enterprise. Feature availability gated by plan (Free → Pro → Business → Enterprise), e.g. managed rulesets, attack score, advanced rate limiting.
- **A** — Get-started flow: deploy managed ruleset → create custom rule on attack score → configure bot protection → optionally add OWASP Core Ruleset → review dashboards. Explicit false-positive troubleshooting path.
- **A** — Related products kept separate: DDoS Protection, Bots, Client-side security, API Shield ("API-specific security products extend those protections to the unique risks in APIs such as API discovery and authentication management").

### F5 WAF for NGINX (formerly NGINX App Protect WAF)

- **A** — Definition: "an advanced, lightweight and high-performance web application firewall (WAF) for applications and APIs"; protects the OWASP Top 10 plus HTTP response inspection, protocol compliance, JSON/XML schema validation, meta-character checking, file-type disallowing. Runs natively on NGINX Plus / NGINX Ingress Controller; deploys on VM/bare metal, Docker, Kubernetes.
- **A** — Policy model: a declarative **security policy**; behavior expressed through **violations**. Each violation carries **alarm** and/or **block** flags. A **violation rating** (numerical, 1–5) aggregates violations per request: ratings 1–3 → request not blocked, log generated with **alerted** status; ratings 4–5 → request **blocked** (blocking page displayed) and logged with **blocked** status.
- **A** — Violation catalog (directly observed): attack signatures, bot clients, threat campaigns, brute-force prevention, cookie enforcement/tamper checks, data guard (sensitive-info leakage in responses), deny/allow IP lists, disallowed file types, evasion techniques (decoding/normalization: %u decoding, backslash normalization, directory traversal, multiple decoding…), file types, geolocation, GraphQL protection (malformed/format/introspection), gRPC protection, HTTP protocol compliance (sub-violations: multiple content-length headers, null bytes, host-header checks, max parameters/headers/cookies…), IP intelligence, JWT checks, JSON/XML format + schema enforcement, mandatory parameters, parameter data types/lengths/meta-characters/regex, response signatures, server-technology signatures, time-based signature **staging**, user-defined signatures/URLs/parameters/headers, URL/length checks.
- **A** — This is a **positive-security-leaning** model: the policy can declare allowed URLs, parameters (mandatory, data types, static values, lengths, patterns), file types, methods; deviations raise violations.
- **A** — Logging: security logs, operation logs, access logs, debug logs. Signature updates are a distinct operational task (update-signatures docs, changelog).
- **A** — Deployment/ops details: policy compiler tool, converters, apreload (policy updates without NGINX reload), SELinux, mTLS.

### Imperva WAF

- **A (product page, Tier 2)** — Product line spans three deployment forms: **Cloud WAF** (SaaS, managed through the vendor console, automated policy creation and rule propagation), **WAF Gateway** (on-premises enterprise appliance for legacy applications and data-sovereignty requirements, local deployment and management), **Elastic WAF** (Kubernetes-deployed, SaaS-managed, DevOps/CI-CD oriented).
- **A (product page)** — Managed rules written and tested by the vendor's threat research team and pushed proactively (regular daily updates; real-time updates for critical threats). Positioning: deploy in blocking mode from the start; automated policy creation.
- **A (product page)** — **Attack Analytics**: ML-based correlation of security alerts into incident narratives with context (origin, methods, severity) to reduce alert fatigue.
- **A (product page)** — Policy management: define/deploy/manage security policies per application across cloud and on-prem environments. Terraform provider for automated deployment. Malicious file-upload scanning. SSL/certificate management. Compliance positioning (PCI DSS, HIPAA, GDPR, ISO 27001).
- **A (product page)** — Explicitly separates sibling products: Advanced Bot Protection, API Security, DDoS Protection, Client-Side Protection, Account Takeover Protection.
- Limitation: operational detail (rule model, event model, tuning mechanics) not verifiable from official operational docs in this environment — see Source-access limitation above.

### ModSecurity + OWASP CRS

- **A** — ModSecurity: "an open source, cross-platform web application firewall (WAF) module… enables web application defenders to gain visibility into HTTP(S) traffic and provides a powerful rules language and API to implement advanced protections." Usage scenarios: real-time application security monitoring and access control; full HTTP traffic logging; continuous passive security assessment; web application hardening. Now under OWASP custodianship.
- **A** — OWASP CRS: "a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls," aiming to protect against the OWASP Top Ten "with a minimum of false alerts"; covers SQLi, XSS, Local File Inclusion, etc. Free (Apache-2.0). Described by the ModSecurity project as "the dominant WAF rule set."
- **A** — Architecture: engine (module inside the web server) + rules language + rule set. No vendor console, no managed-rule subscription, no cloud — the operator wires the engine into the web server and loads rule files. This is the historical substrate from which the commercial category grew.

## Cross-product Comparison

| Dimension | AWS WAF | Cloudflare WAF | F5 WAF for NGINX | Imperva WAF | ModSecurity/CRS |
|---|---|---|---|---|---|
| Inline position | attached to platform resources (CloudFront, ALB, API GW…) | edge proxy in front of origin | module inside NGINX (delivery tier) | edge SaaS / on-prem gateway / in-cluster | web-server module |
| Policy container | web ACL (protection pack) + rule groups | rulesets per zone (or account) | declarative security policy | per-application policies (console-managed) | rule files loaded into engine |
| Rule authoring | statements + logical combinators | expression language | policy parameters + violations + user-defined signatures | console-managed policies (detail unverified) | rules language (SecRules) |
| Vendor-managed rules | AWS Managed Rules rule groups | Managed Rulesets (weekly changelog, emergency releases) | attack-signature sets, threat campaigns, staged updates | threat-research team rules, daily + real-time updates | OWASP CRS (community) |
| Actions | Allow, Block, Count, CAPTCHA, Challenge | Block, Managed Challenge, Redirect, Log, Skip; terminating vs non-terminating | alarm / block flags per violation; violation rating decides block + blocking page | block mode vs monitoring (positioning-level) | block/pass per rule; detection-only mode possible |
| Default action | explicit default action on web ACL (allow or block) | implicit (non-matching traffic passes; phases order) | policy-driven (violation rating thresholds) | (unverified) | rule-by-rule |
| Scoring model | labels + rule order | OWASP CRS threat score; ML attack score as detection | violation rating 1–5 | (unverified) | CRS anomaly scoring (via CRS) |
| Rate limiting | rate-based rules | rate limiting rules | brute-force prevention | (unverified) | via rules (possible) |
| IP / geo controls | IP sets, geo statements | IP Access rules, custom lists, geo fields | deny/allow IP lists, IP intelligence, geolocation | (unverified) | via rules |
| Bot mitigation | Bot Control (paid add-on) | bot score detections + settings; separate Bots product | bot signatures + bot clients violation | separate Advanced Bot Protection product | via rules/CRS (limited) |
| Response inspection | (not emphasized in fetched pages) | Sensitive Data Detection (response phase, Enterprise) | response signatures, data guard | (unverified) | possible via rules |
| Tuning | count mode, scope-down statements | exceptions (skip) + overrides | override rules, whitelist, staging flags | automated policy creation (positioning) | rule exclusion/customization |
| Visibility | dashboards + logging | Security Events + Security Analytics | security/operation/access logs | console + Attack Analytics narratives | full HTTP traffic logging |
| Human verification | CAPTCHA + Challenge | Managed Challenge | user-defined browser control | (unverified) | — |
| Plan/price gating | per-rule/request pricing; WCU budget | plan ladder Free→Enterprise | license tiers | subscription | free/open source |

**B-layer commonalities (observed across ≥3 products):** inline HTTP inspection; rule/policy container bound to a protected application; vendor-maintained managed rule sets updated against new threats; custom rule authoring; block vs monitor operating modes; false-positive tuning mechanisms (exceptions/overrides/count-mode/staging); rate-based controls; IP/geo controls; bot detection; security event logging/dashboards; OWASP Top 10 as coverage vocabulary; OWASP CRS as a shared rule-set baseline (Cloudflare ships an implementation of it; ModSecurity is its home engine; F5 and others target the same coverage).

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product stops being a WAF:

1. **Inline interception of HTTP(S) traffic to a protected web application** — the WAF sits in the request path (reverse proxy, edge service, appliance, or web-server module). Remove → offline scanner / log analyzer / testing tool, not a WAF.
2. **Application-layer attack inspection** — requests (and commonly responses) are evaluated against criteria targeting web-application attack patterns (e.g., injection, scripting, protocol abuse), not merely network-layer properties. Remove → network firewall / DDoS scrubber.
3. **Policy-driven disposition with enforcement** — a configured policy of rules decides each request's disposition (allow through, block, or intermediate actions such as count-only or challenge), with defined behavior for unmatched traffic. Remove → passive monitoring only (a mode, not the Type's defining capability; the *capability* to enforce is invariant).
4. **Security event recording** — dispositions and matches are recorded as security events/logs the operator can review. Remove → the block-vs-monitor tuning loop becomes impossible; no sampled product operates without it.

Jointly held: 1+2 without 3 = detection/monitoring tooling; 3 without 2 = network ACL; 2+3 without 1 = testing tool (DAST); 1+3 without 2 = generic reverse-proxy access control.

### L1 — Common Mature Structure

Present in most mature modern products, not required for the definition:

- vendor-maintained **managed rule sets** (signature packs, threat campaigns, zero-day response) with scheduled updates
- **custom rules** / custom policy expressions authored by the operator
- **rule ordering** with terminating vs non-terminating evaluation (or aggregated scoring)
- **rate-based rules** / brute-force throttling
- **IP reputation / IP lists / geolocation** controls
- **bot detection & mitigation** (varying depth; sometimes a paid add-on or sibling product)
- **security events dashboard / analytics** over allowed and blocked traffic
- **tuning machinery**: exceptions, exclusions, overrides, count/monitor mode, signature staging
- **log export** to SIEM/data platforms
- **human-verification challenges** (CAPTCHA-style) as an intermediate action
- **response-side inspection** (sensitive-data / leakage checks) in some products

### L2 — Variant / Optional Structure

- **deployment substrate**: platform-attached cloud service / edge SaaS proxy / on-prem appliance or gateway / web-server module / in-cluster (Kubernetes) — a variant axis, not definitional
- **policy philosophy**: negative-security signature model vs positive-security (declared/learned application structure) vs expression-language custom rules — products mix these
- **scoring models**: anomaly scoring (CRS-style), violation ratings, ML attack scores
- **plan/feature gating** and pricing models (per-request, per-rule, license tiers, free open source)
- **API/protocol-specific protections** (GraphQL/gRPC profiles, JSON/XML schema enforcement) — depth varies; dedicated API-security products exist beside WAFs
- **account-protection features** (credential-stuffing/leaked-credentials, account takeover prevention)
- **compliance positioning** (PCI DSS etc.) — a use-case framing, not structure
- **virtual patching** as an operational practice (managed rules updated for known CVEs ahead of code fixes)
- **era-current extras**: AI-bot management/monetization, LLM-app protection

### L3 — Vendor-specific Structure (Research Notes only)

- AWS: web ACL/WCU capacity model, protection packs, Firewall Manager, request labels, AI traffic monetization, fail-open/fail-closed split between CloudFront and regional services
- Cloudflare: zone vs account-level rulesets, ruleset-engine phases, attack/bot score fields, plan matrix, sampled Security Events on lower plans
- F5: violation rating 1–5 with alarm/block flags, ASM cookie, policy compiler/apreload, time-based signature staging, blocking page
- Imperva: Attack Analytics incident narratives, SOC-authored rules, three-form product split (Cloud WAF / WAF Gateway / Elastic WAF)
- ModSecurity: SecRules language, engine v2/v3 split, web-server module bindings

### Rejected Findings (anti-overfitting)

- **"A WAF is a cloud/edge service"** — rejected: appliance (Imperva WAF Gateway), web-server module (ModSecurity, F5 WAF for NGINX) and in-cluster forms satisfy the Type; substrate is L2.
- **"A WAF blocks by default"** — rejected: monitoring/count-only operation is a first-class, documented mode in multiple products (AWS count mode, F5 alarm-only flags, ModSecurity detection-only); the *capability* to enforce is invariant, the default posture is a variant.
- **"A WAF is defined by OWASP Top 10 coverage"** — rejected as definition: the Top 10 is the shared *coverage vocabulary* (all sampled products cite it), but the defining structure is inline policy-driven inspection; coverage lists evolve (bots, credentials, AI abuse now included).
- **"Managed rules are the WAF"** — rejected: ModSecurity + community CRS has no vendor managed service and is still the archetype; managed rule sets are L1.
- **"ML scoring is definitional"** — rejected: signature-based and positive-security poles in-sample; ML scoring is era-current L2.
- **"Bot management is part of the WAF definition"** — rejected: depth varies from paid add-on (AWS Bot Control) to separate sibling product (Imperva Advanced Bot Protection, Cloudflare Bots); held L1/L2 with a documented seam.
- **Marketing efficacy claims** (near-zero false positives, % blocking mode) — rejected as evidence; vendor positioning only.

### Historical / Market-Sample Check

ModSecurity (early-2000s origin: web-server module, rules language, community rule set, no cloud, no console, no managed service) satisfies L0 fully — inline module, attack-rule inspection, enforcement capability, event logging. Older appliance WAFs (F5 BIG-IP heritage, Imperva SecureSphere/WAF Gateway lineage) satisfy L0 without any cloud or ML machinery. The L0 therefore does not over-fit to the current cloud/edge implementation. Conversely, modern additions (managed rule subscriptions, ML scores, bot management, plan gating) are correctly held at L1/L2.

## Boundary Findings

- **vs DDoS Protection Platform**: the WAF's unit of work is the *request-vs-policy decision* on application-layer content; DDoS protection's unit is *traffic volume/availability* (absorption, scrubbing). They coexist deliberately: Cloudflare ships them as separate products; AWS pairs WAF with Shield; F5 separates WAF from DoS for NGINX; Imperva lists DDoS as a separate product. Overlap exists at L7 rate-based rules — but rate limiting in a WAF is request-policy, not volumetric absorption. Remove inline attack-content inspection → DDoS/CDN territory.
- **vs API Security Platform**: WAFs apply generic HTTP attack rules to API traffic too (Cloudflare's WAF explicitly covers "web and API requests"); API security adds API-specific discovery, schema/endpoint inventories, and authentication management. Cloudflare draws the line itself: API Shield "extends those protections to the unique risks in APIs such as API discovery and authentication management." F5 embeds GraphQL/gRPC profiles *inside* the WAF policy — a depth variant, not a Type change. Remove generic-HTTP inline enforcement as the center → API Security Platform.
- **vs Network Security Platform / firewall**: L3/L4 flow policy vs L7 application-content policy. The word "firewall" is shared; the inspection layer and rule vocabulary differ fundamentally.
- **vs Application Security Platform / SAST / DAST**: WAF protects *runtime traffic*; SAST/DAST analyze *code/running app for vulnerabilities* pre- or during development, out of the request path. The bridge is **virtual patching**: WAF managed rules mitigate a known CVE at the traffic layer before the code is fixed.
- **vs CDN Management / Load Balancer Management**: WAF capability is frequently bundled into CDN/LB products (CloudFront+AWS WAF, NGINX as delivery tier). The defining core is the security policy decision, not delivery, caching, or routing; strip the security policy and the product remains a CDN/LB.
- **vs Bot management**: bot detection appears inside every sampled WAF at some depth, but dedicated bot-management products exist with deeper fingerprinting/behavioral analysis. Held as a documented seam, not a hard boundary.

## Uncertainties

- Imperva operational model (rule structure, event model, tuning mechanics) unverified — official operational docs unreachable in this environment; only product-page-level claims recorded.
- Exact numeric limits (request-body inspection sizes, WCU thresholds, rating cutoffs) were observed per product but are vendor-specific and deliberately excluded from the final document.
- The precise default posture (block vs monitor) a given product ships with was not uniformly verifiable; treated as product configuration, not Type structure.
- Market-share/efficacy statistics seen on vendor pages were not used as evidence.

## Final Synthesis

A Web Application Firewall is an **inline application-layer security control for web traffic**: it intercepts HTTP(S) requests to a protected web application, evaluates them against a configured policy of application-attack rules (vendor-managed and custom), enforces a per-request disposition (allow / block / intermediate actions such as count-only or human challenges), and records the outcomes as security events that drive the operator's tuning loop.

The defining core is small: inline interception + application-layer attack inspection + policy-driven enforcement + security event visibility. Everything else — where it runs (cloud, edge, appliance, module, cluster), which policy philosophy it uses (signatures, positive model, expressions, scores), how much bot/credential/API-specific machinery it bundles, and how features are packaged and priced — is variant structure. The operational life of the Type is a loop: deploy policy (often starting in monitor/count mode) → observe events → tune false positives (exceptions/overrides) → enable blocking → keep managed rules updated (virtual patching) → repeat.
