# Research Notes — Message Queue Management

Research date: 2026-09-08
Leaf: Message Queue Management (DIRECTORY.md §14 IT, Cloud & Infrastructure)
Slug: message-queue-management

---

## Research Goal

Understand what the operator-facing application for message-queue / messaging-middleware administration actually is in the real market: what objects it manages, what an operator does with it day to day, which surfaces it exposes, which rules govern its behavior, and where it ends relative to (a) the messaging middleware itself, (b) generic observability, and (c) the processed sibling Type Event Stream Processing Platform.

---

## Initial Boundary

Working hypothesis before research (temporary, used only to guide sampling):

- The leaf sits in §14 among "* Management" leaves (Load Balancer Management, CDN Management, Service Mesh Management, Email Infrastructure Management, CPaaS Management) → the intended center of gravity is the **management/administration plane over messaging infrastructure**, not the broker engine itself.
- The market reality is that the management plane is usually *bundled* with the messaging product (embedded console, cloud-provider console, CLI/API) and sometimes exists as a standalone console product. This creates a taxonomy question to record, not silently resolve.
- Nearest Types: Event Stream Processing Platform (processed; recorded pending boundary "transport vs computation"), Observability/Infrastructure Monitoring, Cloud Management Platform, API Gateway Management Console, Email Infrastructure Management, Data Integration Platform.

---

## Research Questions

1. What are the managed objects in each product? (queues, exchanges/bindings, topics, subscriptions, partitions, namespaces, consumer groups)
2. What does an operator actually do? (declare/configure destinations, monitor depth/rates/lag, inspect messages, handle dead letters, close connections, reset offsets, purge, permissions)
3. What surfaces exist? (web console, CLI, HTTP API, infrastructure templates; GUI-first vs CLI/API-first posture)
4. Which visibility is message-specific vs generic infrastructure telemetry?
5. Where do interventions on the message path happen, and what rules govern them (delivery failure, dead-lettering, redrive)?
6. Where is the seam vs observability platforms (Prometheus/Grafana-class) and vs the ESP sibling?
7. Historical check: does the Type hold without the modern web console (older/CLI-first/region-specific products)?

---

## Representative Products

Selected for market representativeness, documentation quality, product philosophy spread, and customer-tier spread:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| RabbitMQ (Management Plugin / Management UI) | open-source classic message broker; management plane embedded as an official plugin (UI + HTTP API + CLI) | the classic queue-middleware pole; docs are the vendor's operational documentation |
| Confluent Control Center (over Apache Kafka) | standalone enterprise web console over a log-based messaging platform; separate product deployed alongside the brokers | the log/stream-flavored pole; the vendor whose catalog vendor-documents the broker-vs-processor split referenced by the ESP pass |
| Amazon SQS (AWS console + API) | fully managed cloud queue service; management surface is the cloud console + service API/IAM | the managed-cloud pole; serverless-style queue semantics |
| Azure Service Bus (Azure portal + Service Bus Explorer + CLI) | managed enterprise bus; queues + topics/subscriptions with rich entity semantics | the enterprise-bus cloud pole; dead-letter and re-dispatch tooling documented in detail |

Attempted and abandoned: **IBM MQ** (oldest enterprise lineage, would have anchored the historical check). `ibm.com/docs` returned 403 and `cloud.ibm.com/docs/mq` returned 404 — two attempts each, abandoned per the source-access rule. No claims about IBM MQ are made from memory; the limitation is recorded in Sources.

---

## Sources

All fetched 2026-09-08 (WebFetch, official vendor documentation, Tier 1):

1. RabbitMQ — Management Plugin guide — https://www.rabbitmq.com/docs/management (fetched; full operational guide)
2. Confluent — Control Center documentation hub — https://docs.confluent.io/platform/current/control-center/index.html (fetched; full TOC + section structure)
3. Confluent — Documentation home / product catalog — https://docs.confluent.io/platform/current/control-center/clients/manage-offsets.html (fetched; redirected to docs home; the catalog page itself documents product split: "Topics and message management", "Consumer groups and offset management", "Monitor and manage Confluent Platform clusters through a web UI", REST Proxy "Produce, consume, and administer Kafka using an HTTP interface", Flink/Kafka Streams/ksqlDB as processing products)
4. AWS — "Configure a dead-letter queue using the Amazon SQS console" — https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-dead-letter-queue.html (fetched)
5. AWS — "What is Amazon Simple Queue Service?" — https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html (fetched)
6. Microsoft — "Azure Service Bus queues, topics, and subscriptions" — https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-queues-topics-subscriptions (fetched)
7. Microsoft — "Service Bus dead-letter queues" — https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues (fetched)

Source-access limitations:

- IBM MQ documentation unreachable (403/404). Consequence: no assertions about IBM MQ-specific machinery; the historical check is argued from in-sample multi-surface evidence (CLI/API-first administration present in all four sampled products) rather than from a legacy product's own docs. Assertion strength for the "predates the web console" framing is kept low (canonical inference, layer C).
- Confluent Control Center evidence is largely structural (section TOC + catalog descriptions) rather than step-by-step walkthroughs; per-page detail (e.g. exact alert-trigger fields) was not fetched. Claims about Control Center are kept at the level the TOC/catalog supports.
- SQS console actions other than the DLQ workflow (e.g. queue creation via console, message send/receive from console) were not directly fetched; they are not asserted as A-layer observations. The welcome page's API-level facts (lifecycle, retention configurability via `SetQueueAttributes`) are A-layer.

---

## Product A — RabbitMQ (Management Plugin)

Evidence layer: A (directly observed from the Management Plugin guide).

Key observations:

- The management plugin is described as "an HTTP-based API for management and monitoring of RabbitMQ nodes and clusters, along with a browser-based UI and a command line tool" (rabbitmqadmin). Three parallel surfaces over one management plane.
- Topology management: "Declare, list and delete exchanges, queues, bindings, users, virtual hosts and user permissions."
- Flow visibility: "Monitor queue length, message rates (globally and per queue, exchange or channel), resource usage of queue, node GC activity, data rates of client connections."
- Node/infrastructure visibility: sockets and file descriptors, memory usage breakdown, available disk space, inter-node bandwidth.
- Policy layer: "Manage policies and runtime parameters" (policymaker permission).
- Definitions export/import: schema of vhosts, users, permissions, queues, exchanges, bindings, parameters, policies can be exported and imported "for recovery purposes or setup automation of new nodes and clusters" — the topology is a portable definition artifact.
- Interventions: "Force close client connections, purge queues." Also "Send and receive messages (useful in development environments and for troubleshooting)" — the console can act as a temporary client.
- Permission tiers over the management surface itself: none / management / policymaker / monitoring / administrator tags, each documented with escalating capabilities (list/view own vs all connections; view node data; manage users/vhosts; close other users' connections). Monitoring-only read-only users are documented.
- Cluster behavior: any node with the plugin serves the UI/API and aggregates stats from other nodes.
- **Boundary statement (vendor-documented)**: "Prefer external monitoring options where possible… The monitoring system is intertwined with the system being monitored… It only stores recent data… Long term metric storage and visualisation services such as Prometheus and Grafana… are more suitable options for production systems." The vendor itself draws the seam between its management plane's built-in monitoring and the observability platform.
- OAuth 2 login to the management UI, HTTPS, reverse-proxy guidance, stats retention configuration — the console is treated as a production-grade access-controlled application.

## Product B — Confluent Control Center (Apache Kafka management console)

Evidence layer: A for structure (official docs hub + product catalog descriptions); page-level detail not fetched.

Key observations (from the documentation hub TOC and the catalog):

- Positioning: "Monitor and manage Confluent Platform clusters through a web UI." A separate, deployed console component (install pages: single-node, multi-node production, high availability; "Kafka-less mode" for running the UI without a fabric behind it).
- "Monitor and Manage" sections: Clusters, Brokers, Topics (Overview / Create Topics / Topic Metrics / View Messages / Configure Topics / Delete Topics), Schemas, Clients (Overview / Consumer Groups / Share Groups / Reset Offsets / Configure Cluster for Client Monitoring), Connect, Replicator, Flink, ksqlDB.
- So the console manages: the cluster/broker fleet, destinations (topics: create/configure/delete, per-topic metrics), message content (View Messages), consumer-side state (consumer groups, **reset offsets**), schemas, and — as extensions — the vendor's processing/integration components.
- Alerts section: alert concepts, triggers, actions, PagerDuty integration, REST API for alerts — alerting is built into the console.
- Security section: TLS, SASL, HTTP basic auth, LDAP, RBAC, Kafka ACLs — access control over both the fabric and the console.
- The same vendor documents the split relevant to the ESP boundary: catalog entries "Topics and message management — Create, configure, and manage topics, partitions, and records" and "Consumer groups and offset management — Track consumer group membership and committed read offsets" sit under core platform, while Flink ("Execute stateful, low-latency stream processing workloads"), Kafka Streams ("Build stateful stream processing applications directly in Java"), and ksqlDB ("Process and query streaming data in real time using SQL directly against Kafka topics") are listed as processing products. Connect ("Stream data between Kafka and external systems") is the integration component. I.e. the vendor itself separates transport administration from computation and integration.
- Companion surfaces in the same catalog: Confluent CLI ("Administer Confluent Cloud and Platform resources directly from your terminal"), REST Proxy ("Produce, consume, and administer Kafka using an HTTP interface"), Kafka CLI tools (Topic Operations, View Consumer Group Info), kcat, Terraform provider, Confluent for Kubernetes, Ansible — multi-surface administration plus automation/IaC paths around the console.
- Consumer lag monitoring is documented as its own concern ("Monitor consumer lag and track processing delays across topics").

## Product C — Amazon SQS (managed cloud queue)

Evidence layer: A (welcome page + DLQ console walkthrough).

Key observations:

- The managed object is the queue; the service decouples distributed systems: producers send, consumers receive; message lifecycle is send → receive (message stays in queue but hidden for a visibility timeout while processed) → delete.
- Queue attributes are configurable through the API (`SetQueueAttributes`) — e.g. message retention period is configurable within documented bounds; messages auto-delete after the retention period. (Precise numbers observed but treated as vendor detail.)
- DLQ configuration is a first-class console workflow (observed step-by-step): open console → navigation pane "Queues" → select the source queue → Edit → "Dead-letter queue" section → toggle Enabled → choose the ARN of an existing queue as the DLQ → set "Maximum receives" (valid range documented, 1–1,000) → Save. DLQs are never auto-created; the operator must create the target queue first, and queue types must match (FIFO↔FIFO, standard↔standard).
- Access control over the messaging surface itself is IAM-based ("You control who can send messages to and receive messages"), separate from queue configuration — the management plane and the message path are both permissioned.
- Delivery guarantees differ by queue type (standard: at-least-once; FIFO: exactly-once processing semantics) — destination-model variation with operational consequences.
- The console + SDK API are the surfaces; the service is fully managed (no broker nodes for the customer to administer — the fabric itself is invisible; visibility is at the queue/message level).

## Product D — Azure Service Bus (managed enterprise bus)

Evidence layer: A (entities concept page + DLQ page).

Key observations:

- Entity model: namespaces contain queues (point-to-point, competing consumers) and topics with subscriptions (publish/subscribe; subscription = "virtual queue" receiving copies, with named filter rules/actions).
- Destinations are created "using one of the following options: Azure portal, PowerShell, CLI, Azure Resource Manager templates" — the same creation act is available GUI-first and automation-first.
- Delivery machinery is entity semantics, operator-visible: receive modes (receive-and-delete vs peek-lock with complete/abandon), lock timeout, and **maximum delivery count** — when delivery attempts exceed the limit the message is moved to the DLQ (system reason `MaxDeliveryCountExceeded`); this behavior is documented as not disableable (count configurable).
- DLQ model: every queue and every subscription has its own dead-letter *sub-queue* ("doesn't need to be explicitly created and can't be deleted or managed independently of the main entity"), addressable by a documented path syntax; messages carry dead-letter reason/description properties; system reason codes documented (e.g. `TTLExpiredException`, `HeaderSizeExceeded`, `Session ID is null`, `MaxTransferHopCountExceeded`, `MaxDeliveryCountExceeded`).
- **No automatic cleanup**: "Messages remain in the DLQ until you explicitly retrieve them from the DLQ and complete the dead-letter message." Drainage is an explicit operational act.
- Re-dispatch tooling: "use Service Bus Explorer in the Azure portal… lets you peek messages in the dead-letter queue, edit their content or properties if needed, and resend them — individually or in batches. Operators often prefer this UI because it surfaces which message types failed, from which source entities, and why, while still allowing batch resubmission." — a documented operator workflow combining inspection, diagnosis (reason codes), and corrective re-dispatch.
- Counts are runtime properties of entities (message counts, transfer-DLQ counts; CLI command `az servicebus topic subscription show` returns DLQ count) — visibility is exposed both in portal and CLI.

---

## Cross-product Comparison

| Dimension | RabbitMQ (mgmt plugin) | Confluent Control Center | Amazon SQS | Azure Service Bus |
|---|---|---|---|---|
| Management plane packaging | embedded official plugin in the broker | separate deployed console product | cloud-provider console + service API | cloud-provider portal + tooling (Service Bus Explorer) |
| Surfaces | browser UI + HTTP API + CLI (rabbitmqadmin, rabbitmqctl) | web UI + companion CLI/REST/API catalog | AWS console + SDK API (+ IAM) | portal (+ explorer UI) + CLI/PowerShell/ARM templates |
| Destination objects | exchanges, queues, bindings, vhosts | topics (+ partitions), consumer groups | queues (standard/FIFO), DLQ as target queue | queues; topics + subscriptions (+ filters) |
| Destination creation/config | declare/list/delete via UI/API/CLI; policies & runtime parameters | create/configure/delete topics via UI | create queue; attributes via SetQueueAttributes; DLQ binding via console edit | portal/CLI/PowerShell/ARM; entity properties |
| Flow visibility | queue length; message rates global/per queue/exchange/channel; connection data rates | topic metrics; consumer lag monitoring; client monitoring | queue message counts (incl. DLQ counts via service) | entity message counts, runtime properties, DLQ counts |
| Message inspection | send/receive test messages from console (dev/troubleshooting) | View Messages per topic | (console send/receive not directly observed) | peek messages; DLQ peek with reason/description |
| Failure handling | purge queues; DLQs via dead-letter-exchange policy configuration | reset offsets (replay cursor) | DLQ binding + maximum-receives redrive config | per-entity DLQ sub-queues with reason codes; peek/edit/resend in batches |
| Consumer/connection administration | list/close connections & channels (tiered rights) | consumer groups, offset reset, client monitoring | consumers are IAM-principals, not administered entities | subscriptions administered as entities; lock/delivery machinery documented |
| Permissions over management | management UI tags (management/policymaker/monitoring/administrator) | console RBAC + Kafka ACLs | IAM (separate send/receive vs configure) | (Azure access machinery not directly fetched; not asserted) |
| Topology as artifact | definitions export/import (recovery/automation) | Terraform/K8s operator/Ansible around the platform | (IaC not directly fetched; not asserted) | ARM templates alongside portal |
| Built-in alerting | pushes users to external Prometheus/Grafana | alerts with triggers/actions + PagerDuty + REST API | (CloudWatch adjacent; not fetched) | (not asserted) |
| Cluster/node view | nodes, memory breakdown, fds, disk, inter-node links | clusters, brokers pages | invisible fabric (fully managed) | namespace/messaging-unit level (not deeply fetched) |
| Vendor-documented boundary | management-UI monitoring "intertwined" — Prometheus/Grafana recommended for production | broker/transport products vs processing products (Flink/Streams/ksqlDB) vs Connect | queue service vs SNS/MQ service split | DLQ vs main entity; portal vs CLI parity |

Reading of the table:

- The three constant columns of behavior across all four products: (1) a managed messaging topology of named destinations with configuration; (2) message-flow visibility bound to those destinations and their consumers; (3) operator interventions that change message/consumer/destination state. These recur in different packages (embedded console / standalone console / cloud console) and different surfaces (UI/CLI/API).
- Everything else varies: packaging, entity vocabulary, failure machinery, alerting, node visibility. These are variant/vendor layers, not the Type.

---

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures over one object domain (the messaging fabric):

1. **Messaging topology as managed objects of record.** Named destinations on the messaging fabric — queues, exchanges, topics, subscriptions, and their routing bindings — exist as declarable, configurable, inspectable, deletable administration objects, together with access control over them. Remove this → there is no messaging to administer; the product is not this Type.

2. **Message-flow visibility bound to the topology.** Operator-visible state of the message path per destination and per consumer side: message depth/backlog, flow rates, consumer/consumption state (lag, active consumers, delivery counts), exposed through the application's surfaces (UI *or* CLI/API output). Remove this → blind administration; the operator cannot see where messages are stuck or flowing.

3. **Operational intervention on the message path.** The application's actions change message/consumer/destination state: purge/drain destinations, dead-letter handling and re-dispatch (redrive/resubmit), closing client connections, managing consumer-side cursors (offset reset), editing delivery/retention attributes, and enforcing access policy. Remove this → passive monitoring/observability, not management (the "Management" in the leaf name is load-bearing).

Jointly-held load-bearing test:

- 1 alone = a configuration registry / IaC manifest with no eyes and no hands.
- 2 without 1 = a monitoring dashboard over queue metrics (the Prometheus/Grafana pole — exactly where vendors point for long-term monitoring).
- 3 without 1+2 = blind scripted ops.
- 1+2 without 3 = observability plus a catalog; nothing can be *managed*.
- 1+3 without 2 = administration without state feedback — degraded; in-sample, even pure-CLI surfaces report counts/lag as command output, so visibility is part of the held structure in every sampled product.

### L1 — Common Mature Structure (cross-product commonality, layer B)

- Multiple parallel administration surfaces over one management plane: web console + CLI + management HTTP API (RabbitMQ explicitly; Confluent via CLI/REST catalog; Azure via portal/CLI/PowerShell/ARM; AWS via console + API).
- Consumer-side administration: listing/inspecting consumer state; closing connections or resetting consumer cursors; consumer-group/subscription administration (three of four directly observed; SQS treats consumers as IAM principals instead — variant).
- Dead-letter machinery as an operator-facing workflow: binding DLQs (SQS), per-entity DLQ sub-queues with reason codes (Azure), DLQ via policy configuration (RabbitMQ); inspection + diagnosis + re-dispatch tooling. (Kafka-class fabrics have no native DLQ; DLQ is a pattern the tooling surfaces — noted as mechanism variation.)
- Message inspection: viewing/peeking message payloads and properties from the management surface (Control Center "View Messages"; Azure DLQ peek; RabbitMQ send/receive from console).
- Permission models specifically governing the management plane, distinct from message-produce/consume rights (RabbitMQ management tags; Confluent RBAC/ACLs; SQS IAM actions).
- Topology as portable definition / automation paths alongside the GUI (RabbitMQ definitions export/import; Azure ARM; Confluent Terraform/K8s/Ansible catalog).
- Cluster/fabric-level views where the fabric is self-hosted (node memory/fds/disk; broker pages); absent when fully managed (SQS — invisible fabric).
- Message-count/rate metrics as first-class, with vendor-documented caveats that long-term metric storage belongs in an external observability stack (RabbitMQ explicit).

### L2 — Variant / Optional Structure

- Packaging: embedded console of a self-hosted broker (RabbitMQ) / standalone console product deployed beside the fabric (Control Center) / cloud-provider console over an invisible managed fabric (SQS, Service Bus).
- Destination model: queue-with-delete semantics (purge/drain exists) vs log-with-offset semantics (retention + cursor reset instead of purge); point-to-point vs publish/subscribe entity families; DLQ-native vs DLQ-as-pattern.
- Operations posture: GUI-first operators vs API/CLI-first/IaC-first teams; multi-cluster/fleet consoles vs single-fabric consoles.
- Governance extensions riding on the fabric: schema registries, data contracts, lineage (Confluent catalog) — present in the streaming pole, absent in the classic pole.
- Built-in alerting vs delegation to external alerting/monitoring.
- Identity integration for console access (OAuth 2 / SSO / LDAP) — common in enterprise deployments, implementation-specific.

### L3 — Vendor-specific (research notes only; must not enter the final document)

- RabbitMQ: exchanges/bindings/vhosts model, dead-letter-exchange policy configuration, rabbitmqadmin v2, specific tag names (management/policymaker/monitoring/administrator), definitions schema contents, stats retention keys, OAuth provider list.
- Confluent: ksqlDB/Flink/Connect/Replicator management inside Control Center, share groups, "Kafka-less mode", PagerDuty alert actions, Unified Stream Manager, specific catalog wording.
- AWS SQS: maximum-receives range (1–1,000), SetQueueAttributes as the attribute API, FIFO/standard type matching rule for DLQs, retention bounds (60 s–14 days), S3-backed large messages.
- Azure Service Bus: `$deadletterqueue` path syntax, named system reason codes (`TTLExpiredException`, `MaxDeliveryCountExceeded`, …), default max delivery count = 10, transfer DLQ sub-queue, Service Bus Explorer tool, session/express entity semantics, auto-forward hop limit 4.

---

## Vendor-specific Findings

(See L3 above.) One vendor finding is worth keeping as a *cited example* rather than a core claim: RabbitMQ's own documentation recommends external monitoring (Prometheus/Grafana) for production and describes its management UI's monitoring as intertwined with the monitored system — vendor-documented seam between this Type and observability platforms.

---

## Boundary Findings

1. **vs Event Stream Processing Platform (§13, processed 2026-09-08).** Transport vs computation. The ESP pass recorded this boundary as pending against this leaf, with the broker-vs-processor split noted as vendor-documented within Confluent's catalog. Cross-check performed this pass and **consistent**: the same catalog separates core transport administration ("Topics and message management", "Consumer groups and offset management", Control Center "Monitor and manage Confluent Platform clusters through a web UI") from processing products (Flink, Kafka Streams, ksqlDB) and from the integration component (Connect). The management console here administers the transport and its consumers; user-defined continuous computation over the stream is ESP territory. The Kafka Streams library-packaging straddler stays inside ESP per that pass's ruling; nothing in this pass's evidence contradicts it. A management console may *embed management surfaces for* processing components (Control Center manages Flink/ksqlDB entries) — that is bundle packaging, not Type merger.

2. **vs Observability Platform / Infrastructure Monitoring / Metrics Monitoring.** Generic telemetry, long-term storage, alerting, dashboards over arbitrary infrastructure vs messaging-specific administration bound to destinations, messages, and consumers with intervention rights. Vendor-documented support: RabbitMQ's own guide delegates long-term monitoring to Prometheus/Grafana; Confluent's catalog lists "Observability integrations — Export cluster metrics and logs to external monitoring tools like Datadog and Prometheus" as separate from Control Center. The seam: an observability product watches the messaging fabric; this Type *operates* it.

3. **vs Cloud Management Platform.** Whole-fleet cloud resource management vs administration of one messaging domain. The cloud consoles (SQS, Service Bus) are this Type's realization *within* their vendor's cloud; they are not fleet managers.

4. **vs §14 siblings (Load Balancer Management, CDN Management, API Gateway Management Console, Service Mesh Management).** Same "operator-facing management plane for an infrastructure component" shape; different managed object — application-to-application message transport vs HTTP traffic routing/mesh configuration. This leaf's defining content is the messaging domain (destinations, messages, consumers, delivery failure), not the console shape.

5. **vs Email Infrastructure Management.** Both are "message transport" but the domains differ: email (MTAs, mailboxes, deliverability) vs application-to-application messaging (queues/topics, consumers). No shared managed object.

6. **vs Data Integration Platform / ETL / ELT.** Queues decouple applications by holding messages in transit (transport contract); integration platforms move data between systems with connectors/transformations (movement contract). Kafka Connect appears inside the Confluent catalog as an integration component managed from the same console — adjacency documented, Types not merged.

7. **vs Workflow Management / Approval Workflow Platform (§10).** Vocabulary collision only: "queue" there = pending human work items; here = message transport. Worth recording because the leaf name is collision-prone.

8. **Taxonomy question (record, do not rewrite):** the leaf is named "Message Queue Management" and sits in the §14 management family; in the market, the management plane is almost always bundled with a broker product, and there is no separate directory leaf for "Message Broker / Messaging Middleware" itself. This pass documents the operator-facing administration Type (consistent with the leaf's position and name). If the taxonomy later wants the messaging middleware *engine* as its own Type, that is a split to make at a taxonomy pass, not silently here.

---

## Historical / Market-Sample Check

- Can the Type be recognized without the modern web console? Yes — in all four sampled products the CLI/API surfaces carry the same three L0 structures (declare/configure destinations, report counts/lag as command output, perform purges/redrives/resets). A CLI-only or API-only administration posture satisfies the core; the GUI is a common realization, not the definition.
- Legacy/enterprise fit: IBM MQ was the intended anchor (1990s lineage) but its documentation was unreachable (403/404). The historical check therefore relies on in-sample multi-surface evidence and is phrased conservatively in the final document (no claims about specific legacy products). Nothing in the derived core depends on era-specific machinery: no web-UI requirement, no cloud requirement, no Kafka-class log semantics in the core (log-vs-queue destination model is held at variant level).
- Region/scale fit: no part of the core is region-specific; the fully-managed cloud pole (fabric invisible to operators) still satisfies the core at queue/message level — so the core must not require broker-node administration (held at L1, conditional on packaging).

---

## Uncertainties

1. Whether the leaf should ultimately be documented as the management plane (as done here) or as the messaging middleware engine itself — flagged as a taxonomy question; this pass's choice follows the leaf name and §14 family position.
2. SQS console capabilities beyond the DLQ workflow (queue creation UI, console message send/receive) were not directly observed; the document avoids asserting them.
3. Azure Service Bus access-control machinery (RBAC specifics) not fetched; permission claims for Azure are avoided.
4. Control Center page-level behavior (exact alert trigger fields, client-monitoring setup steps) not fetched; claims kept at TOC/catalog level.
5. DLQ support strength: directly observed in three of four products, but with three different mechanisms (policy-configured DLQs, DLQ target binding, native sub-queues). The final document treats "dead-letter handling as an operator workflow" as standard capability while explicitly noting mechanism variation — not as a definitional invariant.
6. Standalone third-party console products for Kafka-class fabrics (known to exist in the market) were not sampled; the Type does not depend on them, but the "standalone console product" packaging variant is evidenced by Control Center alone — kept at variant strength.

---

## Final Synthesis

Message Queue Management is the operator-facing administration application for a message-queue / messaging infrastructure. Its defining core is three jointly-held structures over one object domain: (1) the messaging topology of named destinations (queues/topics and their routing and access configuration) as managed objects of record; (2) message-flow visibility bound to that topology — depth/backlog, rates, consumer state/lag — surfaced through the application's surfaces; (3) operational intervention on the message path — purge/drain, dead-letter handling and re-dispatch, connection termination, consumer-cursor management, attribute and policy changes. The market realizes it three ways (embedded console of a broker product, standalone console product beside the fabric, cloud-provider console over an invisible managed fabric), always with parallel CLI/API surfaces. It ends where computation begins (ESP), where generic telemetry begins (observability), and where other infrastructure domains begin (other §14 management leaves).

Suggested one-line L0 for STATUS.md:

> the operator-facing administration application for a messaging fabric whose defining core is exactly three jointly-held structures: the messaging topology as managed objects of record (named destinations — queues/topics/exchanges/subscription entities — with routing bindings and access configuration, declared/configured/inspected/deleted through the application; remove → no messaging to administer) + message-flow visibility bound to the topology (depth/backlog, flow rates, consumer state/lag per destination and consumer side, surfaced via UI or CLI/API output; remove → blind administration) + operational intervention on the message path (purge/drain, dead-letter handling and re-dispatch, close connections, manage consumer cursors, edit delivery attributes and policy; remove → passive monitoring, not management)
