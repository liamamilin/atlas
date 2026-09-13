# Research Notes — Load Balancer Management

Slug: `load-balancer-management` (Directory §14 IT, Cloud & Infrastructure)
Research date: 2026-09-08

## Research Goal

Understand what "Load Balancer Management" is as an Application Type: the operator-facing application through which load balancers are defined, changed, observed, and operated — as distinct from (a) the load balancer data plane itself, (b) CDN delivery management, (c) API gateway machinery, (d) generic network/server management, (e) DNS-level traffic steering, and (f) service-mesh traffic policy.

## Initial Boundary

Hypothesis at start:

- The Type is the **management/control surface** (console, CLI, API, config files) for load balancing: distribution points, backend pools, distribution policies, health-gated traffic handling, operational observation.
- Nearest directory neighbors: CDN Management (processed — its pass explicitly held the seam "remove cache control → generic traffic routing (load balancer management)"), API Gateway Management Console (processed — "remove → generic infrastructure admin panel (load balancer/server management)"), DDoS Protection Platform (processed — "load balancer that merely absorbs traffic" is outside), DNS & DHCP Management (processed), IPAM (processed), Service Mesh Management (unprocessed), Network Management (unprocessed), Infrastructure-as-Code Platform (processed — declares load balancers as resources among many), Container Management (processed — exposes k8s ingress/LB resources), Load Testing Platform (false friend: "load").
- Market shapes expected: cloud-provider managed LB consoles; enterprise ADC appliance management; software load balancer config/API management; DNS-based global traffic management (GSLB) as a contested edge.

## Research Questions

1. What are the core managed objects (listener/virtual server/frontend; pool/target group/upstream; member/node/target/server)?
2. What distribution policies exist (algorithms, weights, persistence/affinity), and where are they configured?
3. How does health checking gate distribution, and how do operators act on health state (drain, disable, deregister, slow-start)?
4. How is the balancer itself made highly available / provider-operated?
5. What L7 routing rules (host/path/header) exist on the listener, and how do they relate to pools?
6. What are the management surfaces (GUI, CLI, API, config files, IaC) and the runtime change loop?
7. What observation exists (metrics, logs, per-pool/member state)?
8. What variants exist (cloud service / ADC appliance / software OSS / L4 vs L7 / internal vs public / global steering)?
9. Where are the boundaries vs CDN, API gateway, service mesh, DNS steering, network monitoring?
10. What does the historical record show (pre-cloud hardware LBs; round-robin DNS pre-history)?

## Representative Products

| Product | Why selected | Doc tier reached |
|---|---|---|
| AWS Elastic Load Balancing (ALB focus) | cloud-managed LB service pole; hyperscaler console+API model | Tier-1 (ALB intro) |
| F5 BIG-IP LTM | enterprise ADC appliance pole; the canonical virtual-server/pool/monitor vocabulary | Tier-1 via official NGINX↔BIG-IP migration guide (concept mapping, tmsh examples); F5 techdocs itself 404 |
| NGINX Plus | commercial software LB; config-file-first + runtime API | Tier-1 (admin guide + dynamic config API) |
| HAProxy | OSS/algorithm-rich software LB pole | Tier-1 (configuration manual, keyword reference) |
| Istio (boundary only) | service-mesh traffic policy adjacency for the service-mesh-management pre-hold | Tier-1 concepts page (partially truncated) |

Rejected from sample (recorded, not silently dropped):

- **Google Cloud Load Balancing** — cloud.google.com timed out twice; abandoned per network rules. Cloud pole rests on AWS + cross-references in NGINX docs (NGINX Plus GCP HA deployment guide exists).
- **F5 techdocs.f5.com BIG-IP pages** — 404 on target page; F5 BIG-IP concepts recovered from the official NGINX migration guide (an F5-owned documentation site) and the F5 glossary (Tier-2).
- **HAProxy runtime API page** (hapee traffic-management/runtime-api) — 404; HAProxy runtime-change evidence limited to what the config manual itself states ("may be changed at run time using 'set …'", stats page, state files).
- **Citrix ADC, Azure LB, Kemp** — not attempted (budget); ADC family cross-checked via NGINX's Citrix ADC migration guide existence.

## Sources

Fetched 2026-09-08:

- AWS — What is an Application Load Balancer? — https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html
- NGINX — HTTP Load Balancing (NGINX Plus Admin Guide) — https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/
- NGINX — Dynamic Configuration of Upstreams with the NGINX Plus API — https://docs.nginx.com/nginx/admin-guide/load-balancer/dynamic-configuration-api/
- NGINX — Migrating Load Balancer Configuration from F5 BIG-IP LTM to F5 NGINX Plus — https://docs.nginx.com/nginx/deployment-guides/migrate-hardware-adc/f5-big-ip-configuration/
- HAProxy — HAProxy Enterprise Configuration Manual (keyword reference) — https://www.haproxy.com/documentation/haproxy-configuration-manual/latest/
- F5 — Glossary: What Is a Load Balancer? — https://www.f5.com/glossary/load-balancer (Tier-2; used for taxonomy/variant confirmation, not operational rules)
- Istio — Traffic Management concepts (nav/task structure; body partially truncated) — https://istio.io/latest/docs/concepts/traffic-management/

Unreachable / abandoned:

- Google Cloud Load Balancing docs — timeout ×2
- F5 techdocs.f5.com BIG-IP LTM pages — 404
- HAProxy Enterprise runtime API page — 404

Sibling research context (internal): research/cdn-management.md (seam held from CDN side), research/ddos-protection-platform.md, research/ip-address-management-ipam.md, research/dns-dhcp-management.md, applications/api-gateway-management-console.md, research/infrastructure-as-code-platform.md, research/container-management.md.

## Product A — AWS Elastic Load Balancing (Application Load Balancer)

### Key observations [A]

- **Load balancer = single point of contact for clients**, distributes incoming application traffic across multiple targets (EC2 instances, containers, IP addresses) in one or more Availability Zones.
- **Listener** checks for connection requests using a configured protocol and port. **Listener rules** (priority + actions + conditions; a **default rule is mandatory**) determine routing to target groups.
- **Target group** routes requests to one or more **registered targets** using protocol/port. A target can be registered with multiple target groups. **Health checks are configured per target group.**
- **Health gating**: "It monitors the health of its registered targets, and routes traffic only to the healthy targets."
- **Routing algorithm configured at target-group level**: default round robin; alternative least outstanding requests.
- **Membership dynamics**: "You can add and remove targets from your load balancer as your needs change, without disrupting the overall flow of requests."
- **Auto-scaling/containers integration**: Auto Scaling instances auto-registered/deregistered with target groups; ECS registers tasks with target groups on dynamic ports.
- **L7 listener rules**: path, host, HTTP header, method, query param, source-IP conditions; redirect; fixed (custom) HTTP response.
- **TLS**: HTTPS listeners terminate with ACM-provided certificates ("terminate connections and decrypt requests").
- **Observation**: CloudWatch metrics (load balancer and target-group level), access logs (stored compressed).
- **Balancer itself**: provider-operated; "Elastic Load Balancing scales your load balancer as your incoming traffic changes"; HA across AZs is inherent to the service.
- Product family split (L3): ALB (L7), NLB (L4), Gateway LB, Classic; Route 53 for DNS naming; WAF/Global Accelerator integrations.

## Product B — F5 BIG-IP Local Traffic Manager

### Key observations [A via official NGINX↔BIG-IP migration guide; taxonomy cross-checked with F5 glossary Tier-2]

- **Virtual server** = "the IP address:port combination used by BIG-IP LTM as the public destination IP address for the load-balanced applications"; shifts to secondary device on failover.
- **Pool** = "a collection of backend nodes, each hosting the same application or service, across which incoming connections are load balanced. Pools are assigned to virtual servers." **Node list** = distinct services on the same IP at different ports.
- **Monitors** (health checks) = "the monitor is associated directly with a pool and applied to each node in the pool"; interval/timeout/fails parameters.
- **Session persistence** configured at the pool: cookie insert ("create persistence cookie … modify virtual … persist replace-all-with"), source-address persistence.
- **SSL profiles** attached to virtual servers: client-ssl (termination), server-ssl (re-encryption upstream) — termination vs proxy documented.
- **Profiles** (http, oneconnect) attached to virtual servers; **iRules** = "proprietary, event-driven, content-switching and traffic-manipulation engine (TCL)" attached to virtual servers for pool selection by URI, header insertion, affinity.
- **Management**: three methods — GUI, CLI (TMSH), iControl API; "Ultimately all changes made via the GUI or API are translated to a TMSH CLI command." tmsh examples: `create pool … members add { ip:port … }`, `create virtual … { destination ip:port pool … profiles … }`.
- **Management plane vs data plane** split; client-side vs server-side networks; **HA** = active-passive pair sharing a floating VIP; failover to passive.
- Reverse-proxy posture: "the client sees the load balancer as the application and the backend servers see the load balancer as the client."
- F5 glossary (Tier-2) taxonomy: L4 vs L7 ("L7 adds content switching"); algorithm list (round robin, threshold, random with two choices, least connections, least time, URL hash, source IP hash, consistent hashing); product shapes (cloud-based, GSLB "sends users to the nearest endpoint", DNS load balancing "configuring a domain in DNS so that requests are distributed across a group of server machines", ADC "effectively making the group look like a single virtual server to the end user", hardware/software/virtual load balancers).

## Product C — NGINX Plus

### Key observations [A]

- **Upstream group** (`upstream` block) = group of servers; members are `server` directives (address:port) with attributes: **weight**, **backup** ("does not receive requests unless both of the other servers are unavailable"), **down** ("temporarily removed from the load-balancing rotation… preserves the current hashing"), **max_conns** (+ queue), **slow_start** ("gradually recover its weight from 0 to its nominal value after it has recovered").
- **Virtual server** (`server` block + `listen`) = frontend; `proxy_pass` to the upstream group. Host-based selection via `server_name`.
- **Methods**: Round Robin (default, weights honored), Least Connections, Least Time (header/last_byte), IP Hash, Generic Hash (**consistent hashing** — "only a few keys are remapped" on membership change), Random (Plus; incl. two-choice "power of two").
- **Session persistence**: sticky cookie (LB-issued cookie), sticky route (route IDs in cookie/URI), sticky learn (server-side session table in shared memory zone); OSS parity via ip_hash/hash. Cluster sync of sticky state (zone_sync).
- **Health checks**: active (`health_check` directive; separate HTTP/TCP/UDP/gRPC health check guides) and passive (max_fails/fail_timeout); `zone` directive (shared memory) required for active checks and dynamic reconfiguration; guarantees coherent failure counting across workers.
- **Runtime management via REST API** [A]: "configuration of upstream servers in a server group can be modified on-the-fly without reloading" — stated uses: **autoscaling** (add servers), **maintenance** ("remove a server, specify a backup server, or take a server down temporarily"), **quick setup** (weight, active connections, slow start, failure timeouts), **monitoring** ("get the state of the server or server group with one command"). Methods GET/POST/PATCH/DELETE; e.g. PATCH `{ "down": true }`. **State file** (`state` directive) persists dynamic changes across reloads; "do not modify the file directly".
- **DNS-derived membership**: `resolve` parameter — "monitor changes to the list of IP addresses in the corresponding DNS record, and automatically apply the changes to load balancing for the upstream group, without requiring a restart."
- TLS termination + upstream re-encryption (proxy_ssl*); keepalive pools; live activity monitoring dashboard + API; HA via keepalived VIP pairs (on-prem) or cloud patterns.
- Market structure: NGINX is F5-owned; NGINX publishes ADC migration guides for BIG-IP LTM and Citrix ADC (hardware-ADC family equivalence); GSLB deployment guide pairs NGINX with NS1 (DNS-based steering).

## Product D — HAProxy

### Key observations [A — configuration manual]

- **Proxies**: frontend (bind = listening socket) and backend (server list); `bind` options; `server`/`default-server` options.
- **balance** directive: "Define the load balancing algorithm to be used in a backend" — examples in manual: roundrobin, static-rr, leastconn, first, source, uri, url_param, hdr(host), random, hash(req.cookie(...)), hash with ipmask. Backend-scoped, set once.
- **Health checking**: `check`, `option httpchk`, `http-check` (multi-step, expect, disable-on-404), `tcp-check`, agent checks; **fall / rise / inter / fastinter / downinter** state-transition parameters; external-check.
- **agent-check** [A]: "an auxiliary agent check which is run independently of a regular health check" — an external agent returns an ASCII string with a percentage / `weight:` / `maxconn:` values; "A zero weight is reported on the stats page as **DRAIN** since it has the same effect on the server (it's removed from the LB farm)" — externally-driven weight and drain state.
- **Member states**: **backup** ("only used in load balancing when all other non-backup servers are unavailable"), **disabled**, `on-marked-down` / `on-marked-up` action hooks, `observe` (passive health from live traffic), maxconn/maxqueue per server, option allbackups.
- **Persistence**: cookie-based (`cookie` directive, dynamic-cookie-key), stick-tables (section 11) + `stick` rules, persist/force-persist/ignore-persist, prefer-last-server, rdp-cookie.
- **Stats/observation**: "a permanent page reporting the load balancer's activity" (HTML stats page with refresh), fe_*/be_* sample fetches (connection counts, queue, session rates), logging subsystem (tcp/http log formats).
- **State persistence across restarts**: `load-server-state-from-file`, server-state-file (also used for address resolution via init-addr last,libc).
- Peers section: stick-table synchronization between HAProxy nodes; mailers for alerts; monitor-uri endpoint.

## Cross-product Comparison

| Dimension | AWS ELB (ALB) | F5 BIG-IP LTM | NGINX Plus | HAProxy | Level |
|---|---|---|---|---|---|
| Distribution point object | load balancer + **listener** (protocol+port) | **virtual server** (IP:port + profiles) | **virtual server** (`server`+`listen`) | **frontend** (`bind`) | L0 |
| Backend set object | **target group** (registered targets) | **pool** (+ node list) | **upstream** group (`server` lines) | **backend** (`server` lines) | L0 |
| Member attributes | registration (instance/IP/lambda), multi-group membership | member/node; monitors applied per pool | weight, backup, down, max_conns, slow_start | weight, backup, disabled, maxconn, maxqueue, agent-check | L0/L1 |
| Distribution policy | round robin / least outstanding requests (per target group) | static & dynamic methods (glossary taxonomy) | RR default; least_conn, least_time, ip_hash, hash+consistent, random | roundrobin, static-rr, leastconn, first, source, uri, url_param, hdr, random, hash | L0 policy + L1 algorithm breadth |
| Health gating | "routes traffic only to the healthy targets" (per-target-group checks) | monitors associated with pool, applied to nodes | active health_check + passive max_fails; zone-shared state | check/http-check/agent-check; fall/rise/inter; observe | L0 |
| Operator member-state actions | register/deregister (manual or auto via ASG/ECS) | (marking via monitors; state control in-product — not directly evidenced in fetched pages) | runtime API: add/remove/modify, PATCH `down:true`, state file | disabled keyword; agent-driven DRAIN (0 weight); on-marked-* hooks | L0/L1 |
| Session persistence | (documented in product; not in fetched page — not asserted here) | cookie insert, source_addr | sticky cookie/route/learn; ip_hash | cookie, stick-tables, persist/ignore-persist | L1 |
| L7 routing on listener | rule conditions: path/host/header/method/query/src-IP; redirect; fixed response | iRules (event-driven content switching) | server_name + location blocks | ACLs + use_backend/use_server; http-request rules | L1 |
| TLS at the balancer | HTTPS listener, ACM certs, termination | client-ssl/server-ssl profiles; termination vs re-encrypt | ssl termination + upstream re-encrypt | crt storage, ACME module | L1 |
| Management surfaces | console (documented: "select your load balancer in the AWS Management Console"), APIs/IaC integrations implied by service model (not directly fetched) | GUI + TMSH CLI + iControl API (all → tmsh) | config files + REST API (GET/POST/PATCH/DELETE) + state file | config file + runtime changes ("set …" at run time) + stats page | L0 surfaces, L1 depth |
| Balancer HA / operation | provider-managed; scales with traffic; multi-AZ | active-passive pair + floating VIP; mgmt/data plane split | keepalived VIP pairs; zone_sync cluster state | peers (stick-table sync); state files | L1/L2 (substrate-dependent) |
| Observation | CloudWatch metrics + access logs | (not fetched) | live activity monitoring dashboard + API; per-server state via API | stats page; logs; sample fetches | L1 |

## Canonical Model (abstraction)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The distribution point as the managed object of record.** A persistent, identified load balancer frontend (virtual server / listener / bind) bound to an address and port (and protocol), held as the stable client contact point that operators create, modify, and delete through the application. *(Remove → server/proxy management or a port-forwarding tool.)*
2. **A managed backend set carrying the distribution policy.** A pool of backends behind the distribution point (targets / nodes / members / upstream servers), each individually addable, removable, weightable, and state-changeable, together with the configured distribution policy (balancing algorithm; optionally persistence) that decides how traffic spreads across members. *(Remove → a reverse proxy with a fixed upstream, i.e. proxy configuration, not load balancing management.)*
3. **Health-gated distribution on the managed record.** The balancer continuously evaluates backend health — configured checks, externally reported agent state, or observed connection failures — and gates which members receive traffic; failures, recoveries, drains, and additions change the distribution without changing the client-facing endpoint, and health/member state is visible in the management surface. *(Remove → static traffic-splitting config; monitoring without control.)*

Jointly-held is load-bearing:

- 1+2 without 3 = static splitting among fixed upstreams (thin reverse-proxy config).
- 1+3 without 2 = single-backend failover pair / health-probed port forwarding.
- 2+3 without 1 = backend health monitoring without a managed distribution point (observability platform).

Historical check (§24): the late-1990s hardware-generation model — virtual servers + pools + monitors configured via CLI/web UI (documented today in the BIG-IP↔NGINX migration guide's tmsh examples and concept mapping) — satisfies all three legs; LVS-style ipvsadm (virtual service + real servers + scheduler + health daemons) satisfies at CLI level. Round-robin DNS (distribution via DNS records, no balancer object, no managed pool) does **not** satisfy leg 1 — it is the pre-history, adjacent to DNS steering. The definition names no cloud, API-gateway, mesh, autoscaling, or AI machinery. **Pass.**

### L1 — Common Mature Structure

- Algorithm breadth beyond round robin: least-connections/least-outstanding/least-time, weighted variants, hashing (source IP, URI, cookie, consistent hashing), random with two choices. (A: all four products)
- Session persistence / affinity: cookie insert, source-address, learned/token, sticky tables. (A: F5, NGINX, HAProxy; AWS documented in-product but not fetched — common, not asserted beyond)
- L7 content routing on the listener: host/path/header/method conditions selecting different pools; redirects; fixed responses; "content switching". (A: AWS rules, BIG-IP iRules, NGINX server_name/location, HAProxy ACLs)
- TLS termination and re-encryption at the balancer; certificate attachment to listeners. (A: all four)
- Per-member capacity controls: weight, max connections/queues, slow-start, drain semantics. (A: NGINX, HAProxy; AWS via target-group algorithm + registration; F5 partial evidence)
- Membership automation: registration from autoscaling/container orchestrators, DNS-derived membership. (A: AWS ASG/ECS; NGINX resolve; HAProxy resolvers section; BIG-IP cloud posture per glossary Tier-2)
- Operational observation: metrics/logs/dashboards; per-listener/pool/member state surfaced for management. (A: AWS CloudWatch/access logs; NGINX dashboard/API; HAProxy stats page)
- Balancer self-HA: paired instances with floating VIP, or provider-operated multi-zone service. (A: BIG-IP, NGINX; AWS provider-managed)
- Multi-surface management: GUI console, CLI, REST/API, config files, IaC/CI integrations. (A: BIG-IP GUI/tmsh/iControl; NGINX files+API; AWS console+APIs; HAProxy files+runtime)

### L2 — Variant / Optional Structure

- Substrate: cloud-managed LB service (control plane of provider-operated service) vs hardware/virtual ADC appliance vs software balancer on commodity hosts vs cluster-embedded (Kubernetes ingress/gateway controllers).
- L4 vs L7 specialization; protocol scope (TCP/UDP/HTTP/gRPC/QUIC).
- Scope: internal/private balancers vs internet-facing; single-site pools vs multi-region steering (GSLB / DNS-based traffic steering — contested edge, see Boundary Findings).
- Extension/scripting engines attached to the distribution point (TCL iRules, Lua/njs, WASM).
- Offload/attached services: WAF attach, auth offload, caching/compression (drift toward ADC/CDN territory).
- Cloud features: availability-zone balancing, cross-zone balancing, autoscaling integration, Lambda/function targets.

### L3 — Vendor-specific (research notes only)

- AWS: ALB/NLB/GWLB/Classic family split; default-rule requirement; algorithm set at target-group level (round robin / least outstanding requests); Lambda targets; compressed access logs.
- F5 BIG-IP: tmsh/iControl/GUI triple surface with GUI→tmsh translation; profiles (http, oneconnect, client-ssl, server-ssl); node lists; automap source-address translation; iRules TCL engine; mgmt-plane/data-plane split; active-passive VIP failover.
- NGINX Plus: shared-memory `zone` prerequisite for dynamic config; state-file persistence for API-made changes; Swagger UI; upstream_conf deprecation (R12→R13); zone_sync; power-of-two random.
- HAProxy: agent-check ASCII protocol (percentage/weight:/maxconn:, DRAIN at zero weight); stick-tables + peers; fall/rise/inter naming; server-state files; mailers; monitor-uri.
- Market structure note: F5 owns both BIG-IP and NGINX — the enterprise-ADC and software-LB poles are one vendor's two eras; the Type's structure is nonetheless stable across AWS/NGINX/HAProxy/F5.

## Vendor-specific Findings

See L3 above. Also: NGINX docs' framing of ADC vs distributed software deployment (edge appliance → application-adjacent software) is a vendor positioning claim — recorded as variant narrative, not Type structure.

## Rejected Findings

- **"Load balancer management = monitoring dashboards"** — rejected: observation is L1; the management loop includes definition and member/state changes, not just viewing.
- **"Session persistence is definitional"** — rejected: many deployments run stateless services without persistence; every sampled product treats it as a configured option, not a required structure.
- **"Cloud autoscaling integration is definitional"** — rejected: era machinery; pre-cloud products satisfy the core (§24 check).
- **"TLS offload is definitional"** — rejected: plain TCP/L4 balancers without TLS are squarely in-Type (NLB/HAProxy tcp mode/frontend-bind evidence).
- **"DNS-based global traffic management (GSLB) belongs fully inside this Type"** — not adopted: products that steer purely via DNS records have no distribution-point object (leg 1 fails); F5's BIG-IP DNS/GSLB is family adjacency. Held as contested edge, not core.
- **"Any reverse proxy is a load balancer"** — rejected: a proxy with a single fixed upstream has no managed backend set/distribution policy (leg 2 fails).
- **"Content switching equals API gateway"** — rejected: L7 routing here is listener→pool selection among backend sets; API-gateway machinery centers API-shaped policies/consumers (API-gateway pass held this seam).

## Boundary Findings

- **vs CDN Management** (processed; seam held from that side: "remove cache control → generic traffic routing (load balancer management)"): held symmetrically here. This Type manages distribution of client traffic to operator-configured backend sets with health gating and has **no caching semantics**; add cache behavior/purge/edge delivery config → CDN territory. Remove cache control from a CDN product and what remains is this Type's object.
- **vs API Gateway Management Console** (processed): API gateway centers API-shaped machinery (APIs, consumers, per-API policies, keys, per-call auth); this Type centers distribution points and backend pools. L7 routing exists on both; the discriminator is the managed record (API definition vs pool/listener), not the presence of routing rules. The API-gateway pass itself marks "generic infrastructure admin panel (load balancer/server management)" as outside.
- **vs DDoS Protection Platform** (processed): a load balancer distributes/absorbs traffic but performs no standing attack detection; DDoS platforms add detection + mitigation execution + availability-objective machinery. Seam already held from that pass ("load balancer/CDN that merely absorbs traffic" is the removal test).
- **vs Service Mesh Management** (UNPROCESSED — pre-hold for that pass): mesh traffic management centers service-to-service policy inside a mesh (observed Istio concept space: request routing, traffic shifting, circuit breaking, outlier detection, locality load balancing, gateways). Overlap: locality load balancing and ingress gateways look like pools/health handling. Proposed seam: the managed record — mesh = per-service routing/policy objects over an mTLS service graph, with sidecar/ambient data planes; this Type = distribution points + backend pools at infrastructure boundaries, no service-graph or mTLS-identity machinery. Removal tests: remove the service graph/identity → this Type; remove the distribution-point/pool record → mesh policy editor. F5 iRules ↔ mesh policy both do "traffic policy", but iRules attach to distribution points, not to a service graph.
- **vs Network Management** (UNPROCESSED — pre-hold): network management centers the device estate and its monitoring/configuration broadly; this Type centers the distribution function specifically (listeners/pools/policies/health gating). A load balancer is one managed device class from network management's view; here it is the only record. Remove the distribution machinery → network management; remove device-estate breadth → this Type.
- **vs DNS & DHCP Management / DNS-level steering** (processed): pure DNS-based traffic steering (weighted/failover DNS records, multi-CDN steering) has no balancer object and no in-band health-gated distribution; held outside this Type's core as global-traffic-steering territory (consistent with CDN pass's multi-CDN flag). GSLB products that *do* register balancer listeners and health-monitored pools (F5 BIG-IP DNS family) sit on this seam — flagged for future review, not claimed here.
- **vs Infrastructure-as-Code Platform** (processed): IaC declares load balancers as one resource type among many (lifecycle of declarations); this Type's application is the domain console where the balancer's own semantics (algorithms, checks, drains, listener rules) are operated. Cross-referenced from IaC pass ("a load balancer with these listeners exists" as their example resource).
- **vs Container Management** (processed): k8s Services/Ingress/Gateway resources inside cluster platforms are cluster-resource records; the balancer-domain console (or controller UI) that operates listeners/pools/health remains this Type. Seam held at record-level (cluster object graph vs balancer machinery).
- **vs Load Testing Platform** (§12): false friend "load" — load testing generates synthetic load for measurement; this Type distributes real traffic. No overlap in record or flow.
- **vs Server Management / Virtualization Management**: backends (servers/VMs) are the *other side* of the distribution point; server management centers the server estate. A balancer's backend registration is not server administration.

**"去掉什么就变成另一个 Type" 判据**: remove health gating → static splitting/proxy config; remove the backend set → single-target proxy or port forwarding; remove the distribution point → backend monitoring or DNS steering; add caching/edge delivery → CDN management; add API-shaped policy machinery → API gateway; add service-graph policy → service mesh territory.

## Uncertainties

1. **AWS stickiness/persistence** not directly fetched (documented in-product; persistence asserted as common from F5/NGINX/HAProxy Tier-1 only).
2. **F5 BIG-IP node state controls (enable/disable/force-offline)** not evidenced in fetched pages (techdocs 404); F5 leg rests on migration-guide concept mapping + glossary. Assertions about BIG-IP kept to documented concepts (virtual server/pool/node/monitors/persistence/profiles/iRules/tmsh).
3. **HAProxy runtime management depth** (Data Plane API specifics) not fetched (404); only manual-stated runtime changeability + stats page asserted.
4. **GCP cloud pole** absent (timeouts); cloud-model breadth rests on AWS + NGINX cloud deployment guides. Assertions about cloud consoles kept generic.
5. **DNS/GSLB seam** unresolved product-wise (NS1, Route 53 traffic policies, BIG-IP DNS not fetched) — held as flagged edge, no claims about those products' internals.
6. Whether Kubernetes ingress/gateway controller management should later be read as a full Variant pole of this Type (evidence here indirect via NGINX Ingress Controller product line and Istio gateway tasks) — left to future passes.
7. Third-party multi-LB / multi-cloud LB management/steering consoles (e.g., aviatrix-class or ADC-centralized managers like BIG-IQ/NGINX Instance Manager) not researched — likely a management-fleet overlay on this Type; flagged like the CDN pass's multi-CDN flag.

## Final Synthesis

Load Balancer Management is the operator-facing application for defining and operating load balancers: the managed record is a **distribution point (listener/virtual server) bound to an address+port**, backed by a **managed backend set (pool/target group/upstream)** carrying a **distribution policy** (algorithm, weights, optionally persistence), with **health-gated distribution** continuously keeping unhealthy members out of rotation and member/state changes (add, remove, weight, drain, disable) reshaping traffic without moving the client-facing endpoint. Around this core, mature products add algorithm breadth, session persistence, L7 content routing on listeners, TLS termination, per-member capacity controls, membership automation (autoscalers, DNS), operational observation, balancer self-HA, and multi-surface management (console/CLI/API/config). The market realizes the same structure across three substrates — cloud-managed services, enterprise ADC appliances, and software balancers — plus cluster-embedded controllers; DNS-based global steering is an adjacent edge, not the core. Boundaries: CDN adds caching/delivery semantics; API gateways center API-shaped machinery; service meshes center service-graph policy; DDoS platforms center attack detection; network management centers the device estate.
