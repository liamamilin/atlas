# Research Notes — Service Mesh Management

## Research Goal

Understand what "Service Mesh Management" is as an Application Type: the operator-facing application through which a service mesh — a dedicated layer that mediates service-to-service communication — is installed, configured, operated, and observed. Distinguish it from (a) the mesh data plane itself as pure infrastructure, (b) load balancer management, (c) Kubernetes/container management, (d) API gateway / API management, (e) observability/tracing products, (f) machine-identity/certificate products, (g) network management.

## Initial Boundary

Hypothesis at start:

- The Type is the **management/control surface** over a service mesh: the mesh system (control plane + data plane), the service graph (registered, identity-bearing services/workloads), declarative per-service traffic and security policy, and mesh-wide observation.
- A service mesh is a dedicated infrastructure layer for service-to-service (east-west) communication, realized by intercepting traffic with proxies (sidecars, node proxies, or sidecar-free mechanisms) that a control plane programs.
- Nearest directory neighbors: Load Balancer Management (processed — pre-hung seam), Kubernetes Management Platform (processed — "mesh owns inter-service traffic, not the cluster estate"), Container Management (processed — "mesh manages inter-service traffic/mTLS"), API Gateway Management Console + API Management Platform (processed — north-south API machinery), Distributed Tracing (processed — "mesh can supply the propagation substrate; the trace system remains the record keeper"), Machine Identity Management (processed — "meshes issue workload identities as an embedded runtime capability"), Network Management (unprocessed), Observability Platform / Infrastructure Monitoring (processed siblings), Certificate Lifecycle Management (processed — cert-manager ships istio-csr for service mesh).
- Market shapes expected: OSS mesh systems (Istio, Linkerd, Kuma) whose management surface is CLI + CRDs + dashboard; service-networking suites with a mesh inside (Consul); commercial mesh management planes (Kong Mesh on Konnect, Tetrate, Solo Gloo); cloud-managed mesh services (AWS App Mesh class — not sampled this pass).

## Research Questions

1. What is the managed subject — the mesh instance? What does "install/upgrade/operate the mesh" look like?
2. What is the service graph? How do workloads join the mesh (injection/enrollment), and what identity do they carry?
3. What traffic policy exists (routing, shifting, retries, timeouts, circuit breaking/outlier detection, locality), and how is it expressed (per-service objects? targetRef?)?
4. What security policy exists (mTLS, authorization between services), and how does the mesh's identity/CA machinery work?
5. What observation exists (per-service-link metrics, topology, logs, traces), and what is in-product vs delegated to external backends?
6. What are the management surfaces (CLI, CRDs/config entries, dashboards/GUI, APIs) and the change loop (declarative config → data plane programming)?
7. What variants exist (sidecar vs ambient/node vs sidecar-free; Envoy vs custom proxy; K8s-only vs multi-platform; single vs multi-cluster/multi-zone; single vs multi-mesh; OSS vs commercial management plane)?
8. Where are the boundaries vs load balancer management, K8s/container management, API gateway, observability, machine identity, network management?
9. What does the historical record show (library-era lineage; first-generation meshes without Kubernetes/mTLS-by-default)?

## Representative Products

| Product | Why selected | Doc tier reached |
|---|---|---|
| Istio | feature-maximal OSS mesh, de facto standard; sidecar + ambient data planes; K8s-centric with VM extension | Tier-1 (overview, traffic-management concepts, security concepts, full docs nav) |
| Linkerd | simplicity-first OSS mesh (CNCF graduated); purpose-built Rust micro-proxy; K8s-focused | Tier-1 (overview, architecture, what-is-a-service-mesh essay, full docs nav) |
| HashiCorp Consul | service-networking suite with mesh inside; multi-platform (VMs, K8s, ECS, Lambda, Nomad); intentions vocabulary | Tier-1 (docs root, service-mesh use case, connect, secure-mesh, manage-traffic) |
| Kuma / Kong Mesh | OSS mesh (CNCF sandbox) + commercial enterprise pole (Kong Mesh); multi-mesh, multi-zone, Universal (VM) mode, Konnect management plane | Tier-1 (Kuma mesh/multi-tenancy page + full policy nav; Kong Mesh docs landing) |

Rejected / not sampled (recorded, not silently dropped):

- **AWS App Mesh** (cloud-managed mesh service pole) — not fetched; market status uncertain at research time; cloud-managed pole rests on indirect evidence. Recorded as uncertainty.
- **Cilium Service Mesh** (sidecar-free eBPF pole) — not fetched this pass; sidecar-free realization covered via Istio ambient (node proxies) evidence.
- **Tetrate Service Bridge, Solo Gloo Mesh, Aspen Mesh** (commercial Istio management planes) — not fetched; commercial management-plane pole covered via Kong Mesh/Konnect.
- **Open Service Mesh** — not fetched (believed retired; no claims made).

## Sources

Fetched 2026-09-09:

- Istio — What is Istio? — https://istio.io/latest/docs/overview/what-is-istio/
- Istio — Traffic Management concepts — https://istio.io/latest/docs/concepts/traffic-management/
- Istio — Security concepts — https://istio.io/latest/docs/concepts/security/
- Istio — full docs navigation tree (setup/install/upgrade/ambient/tasks/ops/reference) — https://istio.io/latest/docs/
- Linkerd — Overview — https://linkerd.io/2.17/overview/
- Linkerd — Architecture — https://linkerd.io/2.17/reference/architecture/
- Linkerd — What is a service mesh? — https://linkerd.io/what-is-a-service-mesh/
- Linkerd — full docs navigation tree (features/tasks/reference) — https://linkerd.io/2.17/
- Consul — Documentation root — https://developer.hashicorp.com/consul/docs
- Consul — Service mesh use case — https://developer.hashicorp.com/consul/docs/use-case/service-mesh
- Consul — Connect workloads to service mesh — https://developer.hashicorp.com/consul/docs/connect
- Consul — Secure service mesh overview — https://developer.hashicorp.com/consul/docs/secure-mesh
- Consul — Manage application traffic — https://developer.hashicorp.com/consul/docs/manage-traffic
- Kuma — Configuring your Mesh and multi-tenancy — https://kuma.io/docs/2.11.x/production/mesh/
- Kuma — full docs navigation tree (policies, production, networking) — https://kuma.io/docs/2.11.x/
- Kong Mesh — documentation landing — https://docs.konghq.com/mesh/

Sibling research context (internal): research/load-balancer-management.md (pre-hung seam), research/kubernetes-management-platform.md, research/container-management.md, research/distributed-tracing.md, research/machine-identity-management.md, research/certificate-lifecycle-management.md, research/api-management-platform.md, applications/api-gateway-management-console.md.

## Product A — Istio (evidence layer A)

- Self-definition: "an open source service mesh that layers transparently onto existing distributed applications… a uniform and more efficient way to secure, connect, and monitor services… with few or no service code changes." Capabilities listed: mTLS + identity-based authn/authz; automatic load balancing for HTTP/gRPC/WebSocket/TCP; fine-grained traffic behavior (routing rules, retries, failovers, fault injection); pluggable policy layer + configuration API (access controls, rate limits, quotas); automatic metrics, logs, traces for all traffic including ingress/egress.
- Architecture: control plane takes desired configuration + its view of the services and "dynamically programs the proxy servers, updating them as the rules or the environment changes." Data plane = communication between services, intercepted by proxies. Two data plane modes: **sidecar** (Envoy proxy alongside each pod / alongside VM services) and **ambient** (per-node Layer 4 proxy — ztunnel — plus optional per-namespace Envoy waypoint for L7). Control plane runs on Kubernetes; mesh extendable to other clusters and to VMs/endpoints outside Kubernetes.
- Traffic management objects (concepts page): **VirtualService** ("how requests are routed to a service… a set of routing rules evaluated in order"), decoupling "where clients send their requests from the destination workloads that actually implement them"; **DestinationRule** ("what happens to traffic for that destination" — named service subsets e.g. by version, applied after routing rules); **Gateway** (manage inbound/outbound traffic at the mesh edge, applied to standalone edge proxies; L4-6 properties in the Gateway resource, L7 routing bound via VirtualService); **ServiceEntry** (external services into the registry); **Sidecar** (fine-tune ports/protocols/reachability per proxy). Routing rules carry match conditions (URI/header/user) and destinations (subsets, weights — "20% of calls go to the new version", canary rollout; routing "completely separate from the instance deployment").
- Resilience & testing (built into the API resources): timeouts, retries, circuit breakers (connection/request limits + outlier detection), fault injection, mirroring/shadowing, locality load balancing (failover, weighted distribution).
- Security (concepts page): identity is fundamental — "first-class service identity" per workload; X.509 certificates provisioned to every workload; istiod + per-proxy agents automate key/cert rotation (CSR flow); **PeerAuthentication** (mutual TLS requirements per workload/namespace/mesh; "Istio automatically upgrades all traffic between two PEPs to mutual TLS"; can be disabled → plaintext), **RequestAuthentication** (JWT), **AuthorizationPolicy** (selector + action ALLOW/DENY + rules with from/to; enforced by an authorization engine in each proxy at runtime; implicit enablement — deny-all semantics once a policy applies to a workload); custom CA integration (Kubernetes CSR, cert-manager, SPIRE via SDS); trust-domain migration; dry-run mode for authz policies (alpha).
- Observability: metrics, access logs, distributed traces (Telemetry API to configure; providers Prometheus/Grafana dashboards, Jaeger/Zipkin/SkyWalking/OpenTelemetry); **Kiali** for "visualizing your mesh" (service graph).
- Operations: install via istioctl/Helm with configuration profiles; **canary upgrades** of the control plane via revisions (multiple control planes in one cluster); in-place upgrades; multicluster installs (multi-primary, primary-remote, different networks); external control plane; VM workload installation; MeshConfig ("configuration affecting the service mesh as a whole"); diagnostic tooling (istioctl analyze/describe/check-inject, proxy config debug, ControlZ); sidecar injection via webhook or istioctl; gateways installation; CNI node agent.

## Product B — Linkerd (evidence layer A)

- Self-definition (overview): "a service mesh for Kubernetes… runtime debugging, observability, reliability, and security — all without requiring any changes to your code." Two basic components: control plane and data plane; "once Linkerd's control plane has been installed… you add the data plane to your workloads (called 'meshing' or 'injecting' your workloads)."
- Architecture: control plane = set of services in a dedicated namespace — **destination service** (service discovery info, "the TLS identity expected on the other end", policy about which requests are allowed, service profiles for per-route metrics/retries/timeouts), **identity service** (TLS certificate authority accepting CSRs from proxies, issuing certs used for proxy-to-proxy mTLS), **proxy injector** (admission controller mutating pods carrying the inject annotation, adding proxy + init containers). Data plane = ultralight Rust "micro-proxies" as sidecars; iptables/CNI redirect traffic through them. **Meshed connections**: outbound proxy does discovery, load balancing, circuit breakers, retries, timeouts; inbound proxy enforces authorization policy; both report traffic metrics.
- Feature set (docs nav): automatic mTLS; telemetry and monitoring; retries and timeouts; load balancing (latency-aware); authorization policy; automatic proxy injection; CNI plugin; dashboard + on-cluster metrics stack (viz extension); distributed tracing; dynamic request routing; traffic split (canaries, blue/green); fault injection; rate limiting; service profiles; topology-aware routing; multicluster communication (+ automatic failover, federated services); non-Kubernetes workloads (mesh expansion); ingress; Gateway API support; HTTP access logging; egress; high availability.
- Canonical definition (vendor essay): "a tool for adding security, reliability, and observability features to cloud native applications by transparently inserting this functionality at the platform layer rather than the application layer… typically implemented as a scalable set of network proxies deployed alongside application code (sidecar)… The proxies comprise the service mesh's data plane, and are controlled as a whole by its control plane." Lineage: library-based communication layers (Twitter Finagle, Netflix Hystrix, Google Stubby) → proxy-based mesh enabled by containers + orchestrators; Linkerd "the first service mesh project" (CNCF 2017). Per-request walkthrough: dynamic routing rules (local vs remote cluster, current vs canary version) → endpoint choice by latency history → connection pool + automatic mTLS (confidentiality + identity validation of both sides) → retries on another instance within a retry budget, eviction of consistently failing instances → metrics + traces emitted to centralized systems, reported via dashboards and CLI.
- Management surfaces: CLI (install, upgrade, inject/uninject, check, diagnostics, identity, multicluster, viz), dashboard (viz extension), Helm install, GitOps integration (Argo CD), mTLS credential rotation tasks (manual + automatic), troubleshooting/debug endpoints.

## Product C — HashiCorp Consul (evidence layer A)

- Definition (use-case page): "A service mesh is a dedicated network layer that provides secure service-to-service communication within and across infrastructure… A service mesh typically consists of a control plane and a data plane. The control plane maintains a central registry that keeps track of all services and their respective IP addresses… The control plane is responsible for securing the mesh, facilitating service discovery, health checking, policy enforcement… The data plane handles communication between services. Many service mesh solutions employ a sidecar proxy…"
- Benefits enumerated: service discovery, application health monitoring, load balancing, automatic failover, traffic management, encryption, observability and traceability, authentication and authorization, network automation. Zero-trust framing: "applications require identity-based access to ensure all communication within the service mesh is authenticated with TLS certificates and encrypted in transit."
- Problems solved: dynamic/ephemeral infrastructure (central registry aware of instance state); intelligent dynamic routing (L7 traffic management: load balancing, traffic splitting, dynamic failover, custom resolvers — "no application changes"); encryption (mTLS — "automatically generate an SSL certificate for each service and its instances"); identity-based authorization replacing IP-based firewall rules ("only allow service A to communicate with service B. Otherwise, the default action is to deny").
- API gateway vs mesh (vendor-drawn seam): gateway = centralized access point for incoming client requests, north-south; mesh = "network management of services and the communication between services," east-west, tracks registered services' lifecycle, routes to healthy instances; "API gateways can be used with a service mesh to bridge external networks (non-mesh) with a service mesh"; federated meshes across datacenters.
- Connect (mesh enablement): Envoy sidecar proxies deployed per service; built-in certificate authority enforcing mTLS between sidecars; configuration entries configure mesh behavior; per-runtime connect guidance (VMs, Kubernetes, ECS, Lambda, Nomad).
- Security: fully configured mesh enforces zero trust — sidecars encrypt/decrypt with mTLS certs signed by Consul; sidecars **deny incoming requests by default**; sidecars authorize per explicitly defined **service intentions** (L4 and L7 depending on protocol; deny-all then allow defined traffic; JWT requirement option). Built-in CA (bootstrap root/key; Vault as alternative CA provider); automatic cert rotation without restarts.
- Traffic management: **discovery chain** stages — routing (service router: L7 attributes like path prefixes/headers → route to service/subset), splitting (service splitter: percentage splits for canary rollouts, versioned releases; chained splitters flatten), resolution (service resolver: failover on unhealthy instances, subsets by DNS, route to specific datacenters, virtual services); locality-aware routing (prefer same region/zone); rate limiting; progressive delivery; UI shows discovery chain in the Services page Routing tab.
- Platform breadth: control plane AND data plane can run on VMs (not only Kubernetes) — "other service mesh software… require you to run the control plane solely on Kubernetes. With Consul, you can run both the control plane and data plane in different runtimes" (K8s, EKS/AKS/GKE, VMs, ECS, Lambda, Nomad, OpenShift); WAN federation and cluster peering to connect datacenters (east-west expansion); HCP Consul Dedicated (managed); multi-tenancy (admin partitions, namespaces, sameness groups — enterprise).

## Product D — Kuma / Kong Mesh (evidence layer A)

- Kuma: **Mesh is the parent resource** of every other resource (data plane proxies, policies); multiple isolated meshes per team/environment/line-of-business ("policies applied to one Mesh do not affect another"); a data plane proxy belongs to exactly one mesh; cross-mesh communication requires an API gateway. Mesh resource carries mTLS config (identity assignment + encryption), zone egress, non-mesh traffic passthrough settings.
- Policy model: policies target resources via **targetRef** (mesh-wide, or specific services/proxy types); policy families: MeshHTTPRoute, MeshTCPRoute, MeshRetry, MeshTimeout, MeshCircuitBreaker, MeshHealthCheck, MeshFaultInjection, MeshRateLimit, MeshLoadBalancingStrategy (incl. locality awareness), MeshTLS, MeshTrafficPermission, MeshAccessLog, MeshTrace, MeshMetric, MeshProxyPatch, MeshPassthrough; shadow mode for applying policies without enforcement; producer/consumer policy scoping; default policies auto-created with a new mesh.
- Deployment: single-zone and **multi-zone** (global control plane + zone control planes; zone ingress/egress; zone proxy authentication); Kubernetes and **Universal** (VM/bare metal) modes; transparent proxying; DNS (kuma-dp + hostname generation); MeshService/MeshMultiZoneService/MeshExternalService objects (service discovery layer); gateways (built-in, delegated e.g. Kong, Kubernetes Gateway API).
- Management surfaces: kumactl CLI, HTTP API, **GUI** (Kuma user interface), **Inspect API** (matched policies per data plane proxy, affected data plane proxies per policy, generated Envoy config), observability stack (Prometheus/Grafana/Datadog/OTel), upgrade machinery.
- Kong Mesh (commercial): "run and manage a distributed service mesh across Kubernetes and VMs in any environment"; built-in mTLS, service discovery, traffic management; multi-zone and multi-tenant topologies; **Konnect Mesh GUI** — Kong-managed global control plane, "centralized view: see all your Services, control planes, and data plane proxies in one place"; enterprise governance: **AccessRole/AccessRoleBinding** RBAC over policies and actions, **AccessAudit** audit logs; **MeshIdentity** issuing SPIFFE-compliant workload identities (bundled provider or SPIRE); MeshTrafficPermission with SPIFFE ID matching; SBOM/vulnerability patching/support policy.

## Cross-product Comparison

| Dimension | Istio | Linkerd | Consul | Kuma / Kong Mesh |
|---|---|---|---|---|
| Managed subject | mesh (control plane + sidecar/ambient data plane) | mesh (control plane + sidecar data plane) | mesh inside the Consul service-networking platform | mesh (explicit `Mesh` resource; multi-mesh) |
| Service graph | service registry + ServiceEntry externals; VMs joinable | meshed workloads via injection; non-K8s workloads via mesh expansion | central registry of services + instances; per-runtime connect | data plane proxies join a Mesh; MeshService/MeshExternalService |
| Workload identity | service identity, X.509 via istiod CA | identity service CA, proxy CSRs | built-in CA; certs per service instance | mTLS per mesh; MeshIdentity (SPIFFE) in Kong Mesh |
| Traffic policy | VirtualService/DestinationRule (routing, subsets, weights), retries/timeouts/circuit breaking/fault injection/mirroring/locality | dynamic request routing, traffic split, retries/timeouts, circuit breakers, rate limiting, fault injection | discovery chain (router/splitter/resolver), failover, locality-aware routing, rate limiting | MeshHTTPRoute/TCPRoute/Retry/Timeout/CircuitBreaker/HealthCheck/FaultInjection/RateLimit/LoadBalancingStrategy via targetRef |
| Security policy | PeerAuthentication (mTLS modes), RequestAuthentication (JWT), AuthorizationPolicy (ALLOW/DENY, deny-by-default once applied) | automatic mTLS; authorization policy (inbound enforcement) | intentions (deny by default, allow lists, JWT) | MeshTrafficPermission; MeshTLS; permissive mTLS option |
| Observation | metrics/logs/traces via Telemetry API; Kiali graph | telemetry + dashboard (viz), per-route metrics, tracing | telemetry + Grafana; UI discovery-chain visualization | MeshMetric/AccessLog/Trace; GUI; Inspect API |
| Gateways | ingress/egress gateways; Gateway API | ingress; Gateway API support | API gateway (north-south); ingress gateways | built-in/delegated gateways; zone ingress/egress |
| Federation | multicluster (multi-primary/primary-remote), external control plane | multicluster (+ failover, federated services) | WAN federation, cluster peering | multi-zone (global + zone control planes) |
| Platform scope | K8s control plane; VM workloads joinable | Kubernetes-first; non-K8s workloads via expansion | VMs, K8s, ECS, Lambda, Nomad, OpenShift (control plane not K8s-bound) | Kubernetes + Universal (VM/bare metal) |
| Surfaces | istioctl, kubectl+CRDs, Helm, dashboards (Kiali/Grafana), MeshConfig | CLI, dashboard (viz), Helm, annotations | CLI, API, UI, config entries, Terraform/CTS | kumactl, HTTP API, GUI, Inspect API; Konnect GUI (commercial) |
| Governance extras | revisions/canary upgrades, profiles | credential rotation, GitOps | Vault CA integration, ACLs, multi-tenancy (enterprise) | RBAC + audit logs, multi-tenancy, support policy (commercial) |

Stable commonalities (evidence layer B, cross-product):

1. **Control plane + data plane decomposition.** All four describe the mesh as a control plane that programs a data plane of traffic-intercepting proxies. The management application's change loop is: declarative config → control plane → proxy configuration.
2. **A registry/graph of services with identity.** All four maintain a view of the mesh's services/workloads and attach cryptographic identity to them (X.509 via a mesh CA; SPIFFE-class in Kong Mesh).
3. **Declarative per-service traffic policy.** Routing (incl. version subsets and weighted shifting), retries/timeouts, circuit breaking/outlier detection, health checking, locality awareness — expressed as objects bound to services, not to individual proxy config files.
4. **Declarative security policy over service-to-service traffic.** mTLS encryption + identity-based authorization between services; deny-by-default posture documented at Consul (intentions) and Istio (implicit enablement); mTLS posture varies (Linkerd automatic; Istio configurable strict/permissive; Kuma permissive option).
5. **Mesh-wide telemetry.** Per-service-link metrics (traffic, errors, latency), logs, traces; visualization of the service graph (Kiali, Linkerd viz, Consul UI routing tab, Kuma GUI).
6. **Mesh boundary machinery.** Ingress/egress gateways connecting the mesh to the outside; external services represented as graph members.
7. **Onboarding as a first-class operation.** Joining workloads to the mesh (sidecar injection, enrollment, connect) is a distinct operator action with its own tooling.
8. **Lifecycle of the mesh itself.** Install, upgrade (incl. canary/revision patterns at Istio; upgrade docs at all four), and uninstall as managed operations.
9. **Multi-surface management.** CLI + declarative config (CRDs/config entries) + dashboard/GUI + API; GitOps/IaC as delivery channels.
10. **Federation across clusters/zones/datacenters** in mature products (all four ship it; single-mesh operation remains the base case).

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The mesh as the managed system.** A dedicated service-to-service mediation layer — a control plane configuring a data plane of traffic-intercepting proxies — held as a named, persistent system that the application installs, upgrades, and operates. Remove → proxy/control-plane tooling with no mesh, or a policy editor with nothing to enforce.
2. **The service graph.** The mesh's member services/workloads held as registered, identity-bearing records forming the graph over which policy and telemetry are expressed; onboarding workloads into the mesh (injection/enrollment) is the entry operation. Remove → generic proxy or load balancer management (no service identity, no graph).
3. **Declarative service-to-service policy enforced by the data plane.** Traffic behavior (routing, shifting, resilience) and security posture (encryption, authorization between services) expressed as per-service rules in the mesh's own model and compiled down to the proxies. Remove → a bare proxy fleet, or monitoring without control.

Jointly-held load-bearing:

- 1 alone = control-plane installer / proxy fleet tooling.
- 2 without 1+3 = service registry/catalog (Consul-catalog territory).
- 3 without 1+2 = policy rules with nothing to apply to.
- 1+2 without 3 = mesh membership with telemetry plumbing but no policy.
- 1+3 without 2 = policy over unregistered targets = load balancer / proxy configuration territory.
- 2+3 without 1 = a policy model with no mediation layer = API-management / config-tooling territory.

### L1 — Common Mature Structure

- Mesh-wide telemetry: per-service-link golden signals (request rate, error rate, latency), access logs, trace-context propagation; service-graph visualization.
- Ingress/egress gateways as the mesh boundary; external services as graph members.
- Onboarding automation (injection webhooks, annotation- or label-based enrollment).
- Resilience policy set: retries, timeouts, circuit breaking/outlier detection, health checks.
- Certificate/identity machinery: mesh CA, issuance, rotation; external CA integration.
- Multi-cluster / multi-zone federation.
- Diagnostic tooling: policy-to-proxy inspection ("which policies affect this proxy", generated proxy config), config analysis.
- CLI + dashboard + API as peer management surfaces; GitOps/IaC delivery of mesh config.

### L2 — Variant / Optional Structure

- Data plane realization: sidecar proxies vs node-level proxies (ambient) vs sidecar-free mechanisms; proxy engine (Envoy vs purpose-built).
- Platform scope: Kubernetes-only vs multi-platform (VMs, ECS, Lambda, Nomad); where the control plane runs.
- mTLS posture: default-on vs permissive/opt-in; CA source (built-in vs external/Vault/SPIRE).
- Single mesh vs multi-mesh/multi-tenancy; commercial management planes (hosted global control plane, centralized GUI, RBAC, audit logs).
- Advanced traffic features: fault injection, mirroring, rate limiting, request-timeout tuning depth.
- Extensibility (WASM/Lua proxy plugins); protocol breadth (HTTP/gRPC/WebSocket/TCP).
- Progressive-delivery integrations (canary automation via external tools).

### L3 — Vendor-specific (research notes only)

- Istio: istiod; VirtualService/DestinationRule/Gateway/ServiceEntry/Sidecar vocabulary; ambient ztunnel/waypoints/HBONE; revisions + canary upgrades; MeshConfig; istioctl analyze/describe/check-inject; Bookinfo; configuration profiles; trust-domain migration.
- Linkerd: linkerd2-proxy (Rust); destination/identity services + proxy injector decomposition; `linkerd.io/inject` annotation; viz/jaeger extensions; Service Profiles; retry budgets; linkerd-init/CNI traffic redirection.
- Consul: intentions vocabulary; discovery chain (router/splitter/resolver); config entries; WAN federation + cluster peering; admin partitions/namespaces/sameness groups; Vault CA integration; HCP Consul Dedicated; built-in proxy vs Envoy.
- Kuma/Kong: `Mesh` parent resource; targetRef policy model; zone ingress/egress; kumactl; Universal mode; MeshService/MeshMultiZoneService/MeshExternalService; HostnameGenerator; Kong Mesh Konnect Mesh Manager, MeshIdentity (SPIFFE), AccessRole/AccessAudit; shadow-mode policies.

## Boundary Findings

- **vs Load Balancer Management** (processed — pre-hung seam RATIFIED from this side): the mesh centers per-service routing/policy objects over an identity-bearing service graph, enforced by a mesh-managed data plane; load balancer management centers distribution points + health-gated backend pools at infrastructure boundaries. Overlap is real but facet-level: locality load balancing, gateways, health checks/outlier detection exist in both. In the mesh, "load balancing" is endpoint selection within a service's instances, computed by the data plane from the service registry — there is no operator-managed balancer object with listeners/pools. Removal tests hold both directions: remove the service graph/identity → load balancer management; remove the distribution-point/pool record → mesh policy editor. Istio's own docs list "Third Party Load Balancers" as an *integration*, supporting the seam.
- **vs Kubernetes Management Platform** (processed): the mesh installs into clusters and uses K8s CRDs as config substrate, but the managed record is the mesh (its services, policies, proxies), not the cluster estate. Consistent with that pass's boundary ("mesh owns inter-service traffic, not the cluster estate"; Istio appears there as an installable cluster tool).
- **vs Container Management** (processed): workload lifecycle vs inter-service traffic/mTLS. Consistent with that pass's recorded seam.
- **vs API Gateway Management Console / API Management Platform** (processed): north-south API-shaped machinery (API definitions, consumers, credentials, subscriptions) vs east-west service-to-service policy. Meshes expose ingress gateways, but the gateway is an entry point into the service graph, not an API product surface. Consul's own docs draw this seam explicitly (north-south vs east-west; "API gateways can be used with a service mesh to bridge external networks with a service mesh"). Kong ships API management and Kong Mesh as separate product lines.
- **vs Distributed Tracing / Observability Platform / Infrastructure Monitoring** (processed): the mesh emits telemetry as a substrate (proxies emit metrics/spans, propagate trace context); the trace/observability system remains the record keeper. The mesh's own observation surfaces (topology, per-link metrics) exist to operate the mesh. Consistent with the distributed-tracing pass's recorded seam.
- **vs Machine Identity Management / Certificate Lifecycle Management** (processed): the mesh issues workload identities as an embedded runtime capability (Istio/Consul appear in SPIFFE's implementer matrix per the MIM pass); MIM/CLM make the identity/certificate population itself the managed object. The mesh's CA is internal machinery, not the product.
- **vs Network Management** (unprocessed — pre-hung seam for that pass): the mesh operates the service-to-service layer over service identity; network management centers the device estate and its configuration/monitoring. The mesh is not a device; its "members" are services/workloads.
- **vs Network Security Platform / microsegmentation / ZTNA**: mesh authorization is enforced by the mesh's own data plane over service identity (Consul's own framing: shift from IP-based firewall rules to service-to-service permissions); ZTNA mediates user→private-app access; network security products inspect/protect network traffic without owning a service graph. Consul frames the mesh as zero-trust for east-west traffic — vocabulary overlap, different subject.
- **vs Infrastructure-as-Code Platform** (processed): IaC declares mesh resources among many; the mesh's own surfaces (CLI/CRDs/GUI) are where mesh semantics are operated. Same record-level seam as the LB pass recorded.

**"去掉什么就变成另一个 Type" 判据**: remove the mediation data plane → policy-as-code with no enforcement (config tooling); remove the service graph/identity → load balancer or proxy management; remove declarative policy → telemetry overlay (observability territory); restrict to north-south → API gateway territory; remove the mesh system itself (no control plane/data plane to operate) → generic network policy tooling.

## Historical / Market-Sample Check (applied before freezing L0)

- **Library-era lineage (pre-mesh)**: Buoyant's own essay traces the mesh to library-based communication layers (Finagle, Hystrix, Stubby) — the *concept* of a dedicated service-to-service layer predates sidecar proxies. The L0's mediation-layer leg is realized by libraries in that era only partially (no uniform interception), so the library era is held as lineage, not in-type.
- **First mesh generation (Linkerd 1.x, 2016–2017; Istio 0.x, 2017)**: Linkerd 1.x ran on VMs without Kubernetes, used JVM proxies, and did not ship mTLS-by-default; it still had data-plane interception + a control plane (namerd) + routing policy + telemetry. All three L0 legs satisfied with no Kubernetes, no Envoy, no mTLS-by-default, no ambient mode. PASS.
- **Consul on VMs / Kuma Universal**: control plane and data plane on non-Kubernetes runtimes satisfy the L0 (platform scope is L2). PASS.
- **Permissive-security meshes**: Kuma documents permissive mTLS; Istio documents plaintext when mTLS disabled — a mesh manager without default-strict mTLS stays in-type (mTLS-by-default is L2 posture, not invariant). PASS.
- **Sidecar-free realization**: Istio ambient (node proxies + optional waypoints) satisfies the L0 with no sidecars — data-plane realization is variant, not invariant. PASS.
- The definition names no Kubernetes, no Envoy, no sidecars, no mTLS-by-default, no multi-cluster, no GUI — all held at L1/L2.

## Uncertainties

1. **Cloud-managed mesh services** (AWS App Mesh class) not directly researched; market status at research time uncertain (deprecation signals exist in background knowledge but were not verified from fetched sources). No claims made about them; the cloud-managed pole is a plausible variant shape only.
2. **Commercial Istio management planes** (Tetrate, Solo Gloo, Aspen Mesh) not fetched; the commercial management-plane pole rests on Kong Mesh/Konnect evidence alone. Multi-mesh governance breadth (cross-mesh policy, compliance views) asserted only at variant strength.
3. **Sidecar-free eBPF meshes** (Cilium) not fetched; sidecar-free realization evidenced via Istio ambient only.
4. **Exact defaults/limits** (certificate lifetimes, default timeouts, proxy resource footprints, scale ceilings) deliberately not asserted — vendor-specific and mostly L3; Kuma's default policy values observed but held in research notes only.
5. **Consul's non-mesh breadth** (KV, config management, DNS) is part of the Consul platform, not of the mesh Type; the mesh-inside-a-suite packaging is recorded as a variant, but a pure "service discovery platform" without mesh enforcement would fall outside this Type (registry/catalog pole of the load-bearing analysis).
6. **GUI depth varies** (Linkerd viz dashboard vs Kuma GUI vs Konnect Mesh Manager); the minimal in-type surface is CLI + declarative config — a mesh manager with no GUI stays in-type (all OSS poles are CLI-first).

## Final Synthesis

Service Mesh Management is the operator-facing application whose managed subject is a service mesh: a dedicated mediation layer (control plane + data plane of traffic-intercepting proxies) through which all service-to-service communication flows. Its defining core is three jointly-held structures: (1) the mesh as a named, persistent managed system installed/upgraded/operated by the application; (2) the service graph — registered, identity-bearing services/workloads that workloads join through onboarding; (3) declarative per-service policy — traffic behavior and security posture — expressed in the mesh's own model and compiled down to the data plane. Around that core, mature products add mesh-wide telemetry and topology, gateways, federation, diagnostics, and multi-surface management; realization choices (sidecar vs node proxies, Envoy vs custom engines, K8s-only vs multi-platform, mTLS posture, single vs multi-mesh, OSS vs commercial management planes) are variants. The Type's boundaries are held by the managed record: service-graph policy (not distribution points → LB management; not clusters → K8s management; not workloads → container management; not APIs/consumers → API gateway/management; not telemetry storage → observability; not identity populations → machine identity).
