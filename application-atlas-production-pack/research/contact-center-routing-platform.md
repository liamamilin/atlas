# Research Notes — Contact Center Routing Platform

Research date: 2026-09-07

## Research Goal

Understand the routing machinery of contact centers as a documentable Application Type: what a "contact center routing platform" consists of, how the interaction-to-agent matching decision actually works, how routing is configured and consumed, and how this Type relates to the Contact Center Platform Type (whose distribution core this machinery is) and to the IVR / WFM / Help Desk siblings.

Special attention: the directory sibling `applications/contact-center-platform.md` (processed 2026-09-07) already characterizes this leaf as a **component** — "routing decisioning on its own, without the telephony, agent-workspace, and operational layers". This pass verifies that characterization against live vendor documentation and decides whether the Type stands on its own, how it should be framed, and whether a boundary issue must be recorded.

## Initial Boundary

Preliminary understanding before research:

- Core use: decide, for every arriving customer interaction, where it goes — which queue, which agent, in what order — under configurable rules over live state.
- Users: contact center administrators / queue admins (configure routing), operations managers (consume routing outcomes), developers (API-controlled routing in some products).
- Nearest neighbors: Contact Center Platform (whole machine), IVR Platform (pre-queue automated handling), Call Center Platform (voice-restricted sibling), Workforce Management / Agent Scheduling (staffing the pool the router draws from), Contact Center Quality Management (evaluation of what routing produced), Help Desk / Ticketing (assignment of records, not live interactions).
- Likely risk: this Type may be a Capability of Contact Center Platform rather than an independently sold product. Must verify whether the market realizes "routing" standalone (named products, API services) or only embedded.
- Unknowns: depth of AI/predictive routing; whether routing can be documented as a self-contained subsystem; historical premise-ACD fit.

## Research Questions

1. What objects does a routing engine operate on? (interaction/contact/task, queue, agent/worker, skills/attributes, availability state, routing policy)
2. What is the full decision path from arrival to assignment? (classification → queueing → eligibility → ordering → assignment → fallback)
3. What rule types are configurable, and by whom? (routing methods, evaluation methods, priorities, skills, capacity, hours)
4. What inputs drive decisions? (channel, IVR/flow attributes, customer identity/value, agent state, real-time queue health)
5. What happens when nothing is eligible/available? (wait semantics, expansion/overflow, callback, voicemail, cancellation)
6. How is routing realized per product: suite subsystem, platform component, API primitive, [CRM/help-desk-embedded engine]?
7. What is AI-era routing (predictive, intent-based, value-based)?
8. What visibility/reporting does routing produce?
9. Historical check: does the minimal definition hold for premise-era ACDs?

## Representative Products

Chosen for: market representativeness, documentation completeness, different product philosophies (enterprise CX suite / hyperscaler platform / call-center-native cloud vendor / developer-API primitive), different realization forms.

| Product | Realization form | Documentation level reached |
|---|---|---|
| Genesys Cloud CX | routing as a documented, self-contained subsystem of an enterprise CX/CCaaS suite | Tier 1 (Resource Center: glossary + Bullseye overview + About interaction routing index + Routing and evaluation methods) |
| Amazon Connect | routing as a native concept of a hyperscaler contact-center platform (routing profiles) | Tier 1 (admin guide, concepts-routing) |
| Twilio TaskRouter | routing as an independent API-level service ("the heart of a contact center") | Tier 1 (docs root + Workflows Overview with full configuration model) |
| Five9 | routing packaged as a named capability ("Intelligent Routing" / "Genius Routing") of a call-center-native cloud vendor | Tier 2 (official product pages; help-center body not reachable) |

Unreached poles (recorded, no claims made): Salesforce Help (Omni-Channel routing engine) — JavaScript application, CSS error on fetch; Zendesk support center (Omnichannel Routing) — search results JS-rendered, article URLs undiscoverable; Microsoft Dynamics 365 unified routing — two URL attempts 404; premise-heritage ACDs (Cisco/Avaya) — not attempted this pass (known 403 from prior sibling pass).

## Sources

All fetched 2026-09-07.

- Genesys Cloud Resource Center — Glossary — https://help.mypurecloud.com/691/ (ACD, distribution queue, skill, skills-based routing, bullseye routing, automated call routing, route paths, agent-owned callback, preferred agent routing, call blending, abandonment/ASA metrics, configuration objects incl. call routing objects, divisions)
- Genesys Cloud Resource Center — Bullseye routing overview — https://help.mypurecloud.com/3492/
- Genesys Cloud Resource Center — About interaction routing (ACD) — https://help.mypurecloud.com/articles/about-interaction-routing/
- Genesys Cloud Resource Center — Routing and evaluation methods — https://help.mypurecloud.com/42040/
- Amazon Connect admin guide — How Connect Customer uses routing profiles (concepts-routing) — https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing.html
- Twilio Docs — TaskRouter: Skills-based routing for contact centers — https://www.twilio.com/docs/taskrouter
- Twilio Docs — Workflows Overview (workflow configuration) — https://www.twilio.com/docs/taskrouter/workflow-configuration
- Five9 — Intelligent Routing (omnichannel contact center software page) — https://www.five9.com/products/capabilities/intelligent-omnichannel-contact-center-software
- Five9 — products/capabilities index (site navigation) — https://www.five9.com/products/capabilities
- Context from sibling pass: applications/contact-center-platform.md + applications/ivr-platform.md (processed 2026-09-07)

## Product Observations

### Product A — Genesys Cloud CX (evidence layer A throughout)

- ACD defined: "the contact center art and science of getting the right call to the right person as quickly as possible"; "automatically answers incoming calls and assigns waiting interactions to the most appropriate agent based on the caller's needs using routing rules"; ACD calls are associated with a queue.
- **Distribution queue**: the object in the matching of agents and interactions; a queue is a single attribute tagged on an interaction and a 1:n attribute on an agent — agents join queues to handle tagged interactions; leaving a queue stops the interactions.
- **Skill**: "a task, expertise, or knowledge that an agent must have to handle an interaction"; agents carry proficiency ratings per skill; ACD considers proficiency when matching. Languages are a parallel skill class. "Route paths are combinations of queue, language, and skills through which interactions are routed."
- **Queue configuration is the unit of routing policy.** A queue administrator assigns each queue (1) a **routing method** and (2) an **evaluation method**; "each combination of evaluation and routing methods results in different routing behavior."
- **Routing methods (5)**: Standard ACD (next available agent, skills per evaluation method); **Predictive routing** ("routes interactions based on AI analysis that discovers the best available match between an agent and specific interaction"); **Preferred agent** (pool of preferred agents first); **Bullseye** (targeted sub-queue with skills; relaxes requested skills per configuration to expand the pool); **Conditional group routing** (dynamically expanded pool of target groups shared between queues, with rules ensuring other queues' KPI targets are not compromised).
- **Evaluation methods (3)**: Best Available Skills (longest-idle agents evaluated, all required skills, highest average proficiency, idle tiebreaker); All Skills Matching (agent with all required skills, longest idle, ignores ratings); Disregard Skills, Next Agent (longest idle, no skills). Time since last handled interaction is computed across all of an agent's queues.
- **Bullseye routing in depth**: concentric rings, each ring a sub-queue with assigned agents; expansion triggered by a configurable timeout per ring; two expansion modes — (1) add groups with same skills but lower proficiency, (2) progressively relax skill requirements; inner-ring/higher-proficiency agents keep priority throughout; agents busy, fully utilized, or logged out are unavailable; preferred agents are considered whether or not they have the required skills; works even without skills (cost-based example: less expensive agents in inner rings); explicitly framed as balancing customer experience (SLA/abandon rates) against best-matched agent.
- **Scoring**: two interaction-scoring methods (Conversation score = arrival time + priority, priority expressed in milliseconds-equivalent — one priority point = 60,000 ms; Priority score = priority value with time-in-queue tiebreaker). [Precise vendor mechanics — L3, keep out of final doc.]
- **Conditional Group Activation (CGA)**: dynamically expands/contracts the eligible agent pool based on real-time queue conditions (e.g., expected wait time exceeding a threshold activates an overflow group; queue health restored removes it); "allows CGA to decide when to bring in more capacity while predictive routing manages who would be the best available agent."
- **Skill expression filters**: interaction-level dynamic skill+proficiency conditions authored in the flow engine (Architect) or supplied via API; refine the eligible pool at runtime; invalid filters revert to queue-configured routing.
- **Channel breadth of the same machinery**: ACD email routing, ACD message routing, SMS, callbacks (incl. agent-owned callback: a callback that waits for its owning agent and, if the owner isn't available at the scheduled time, "automatically routes to the next available agent" — requires a Preferred Agent Routing rule), ACD voicemail responses, email/message "parking" for later agent handling.
- **Availability/utilization**: agents have states; utilization configurable at agent and org level (utilization labels); queue configuration "defines queue members' maximum capacity for handling interactions".
- **Blending**: call blending = "coordinated delivery of both inbound and outbound calls to the same set of agents".
- **Inputs from intake**: "A customer can request skills, for example, from the IVR" — intake flows classify and tag interactions before/at queue entry. Auto-attendant glossary: business logic to "route, categorize, define, and prioritize interactions".
- **AI-era**: "Automated call routing uses AI to analyze incoming calls and direct them to the most appropriate agent based on the query's complexity and the agent's expertise"; skills-based routing glossary entry says SBR "uses customer data and AI to match callers with agents".
- **Visibility**: abandonment/abandoned rate, ASA, service level — measured per queue and contact center; queue/skill-level live metrics (on-queue counts, agents staffed); priority visible on the interaction panel; routing objects exposed in divisions for access control ("Call routing objects", "Message routing objects", Queues).
- **Outbound coupling**: dialing campaigns deliver connected calls into queues/flows (dialing modes glossary); skills-based preview dialing exists.
- **Work automation, rule-based decisions, direct routing, last agent routing** — additional named routing features (article titles observed; bodies not fetched).

### Product B — Amazon Connect (evidence layer A, one page)

- **Routing profile**: "determines what types of contacts an agent can receive and the routing priority." Each agent is assigned exactly one routing profile; a profile can have many agents. Profiles "link queues and agents".
- Creating a profile specifies: the **channels** the agents will support, the **queues** of customers the agents will handle, and **priority and delay of the queues**.
- Framed as scale management: "to quickly change what a group of agents does, you only need to make an update in one place: the routing profile."
- Ships a default routing profile ("Basic routing profile") with a default queue and default flows so an unconfigured instance still routes.
- (From the sibling pass's sources: Connect runs contacts through flows into queues, and agents are organized around queues/routing profiles — consistent with this page.)

### Product C — Twilio TaskRouter (evidence layer A)

- Self-definition: "a skills-based routing system that provides the heart of a contact center that you can control from your code." "With flexible routing logic, you can match tasks to workers while maintaining escalation and fallback rules. TaskRouter can track the state of all tasks and workers in your system and monitor performance."
- **Objects**: Task (unit of work with attributes), Worker (serving agent with attributes/abilities), TaskQueue (holding pool per worker population), Workspace (container), Workflow (the rules artifact).
- **Workflow configuration** (JSON, documented in full): ordered **filters** with SQL-like conditional **expressions** on task attributes → each filter has ordered **targets** (queue, priority, timeout, optional target-worker expression) → a **default_filter** catch-all. "You can think of a Workflow configuration like a case statement: the Task will be routed based on the first expression matched."
- **Time-based escalation**: a target's timeout moves the Task to the next target — which may raise priority ("a long waiting Task can be bumped ahead in line") or switch to a wider queue; if no further targets, the Task "is considered timed out and will be canceled".
- **Worker matching expressions**: e.g. `task.requested_agent == worker.agent_id` (preferred-agent routing), `task.required_language IN worker.spoken_languages` (skills/language matching) — expressions evaluate over worker AND task attributes.
- **Value-based routing**: documented example tags Tasks with customer_value gold/silver/bronze; gold tasks get priority and widen their eligible queue after a wait threshold.
- **Lifecycle**: workflow "completes" once a Task is matched with a Worker and the Reservation is accepted; until then the Task keeps flowing through the workflow. FIFO behavior is the degenerate configuration (default filter only).
- **Generality**: examples include sales leads and support tickets; a PII warning states workflows should not contain directly identifying information — the system assumes pseudonymous attributes. REST API + JS SDK + TwiML integration for calls; "contact center blueprint" and dynamic-call-center tutorials position it as the core of a build-your-own contact center.

### Product D — Five9 (evidence layer B for the page's own claims)

- Markets **"Five9 Intelligent Routing"** as a named capability with its own product page: "Intelligent routing that connects customers to the right agent — every time"; "With Five9 Intelligent Routing you have control over how and when your agents are matched with customers."
- **Genius Routing**: "dynamic matching capabilities that consider granular agent characteristics, dynamic, AI-infused proficiency levels, nuanced customer intents, and progressive queuing… to ensure interactions are driven to the right agent and SLAs are maximized."
- Value props: improved agent utilization (match agents to interactions they handle best), more accurate routing (right agent first time), consistent service levels ("intelligent, adaptive queuing" during peak demand), open/future-ready (integrate third-party AI to evolve routing logic).
- "Flexible" list: skills-based routing; inbound, outbound, and blended calling; speech-enabled IVR and intelligent virtual agents; CTI screen pop; caller identification.
- Pre-built CRM integrations (Salesforce, ServiceNow, Microsoft, Oracle, Zendesk); web callback; real-time/historical/custom reporting.
- [All Layer A-for-Five9-page but single-product; used to support cross-product commonality only where it echoes Genesys/Twilio structures: skills-based routing, blending, SLA-driven routing, AI-infused matching, utilization.]

## Cross-product Comparison

| Structure | Genesys | Amazon Connect | Twilio TaskRouter | Five9 | Evidence layer |
|---|---|---|---|---|---|
| Interaction held in a queue awaiting assignment | distribution queues; ACD calls "associated with a queue" | queues linked to agents via routing profile | TaskQueues; tasks wait for assignment | "progressive queuing", omnichannel queuing | A×4 → B |
| Agents/workers with eligibility attributes (skills, languages) | skills + languages + proficiency ratings | profile determines "types of contacts an agent can receive" | worker attributes matched by expressions (`required_language IN worker.spoken_languages`) | skills-based routing | A×4 → B |
| Live availability/capacity state of agents | agent states; utilization; max capacity per agent; busy/fully-utilized/logged-out = unavailable | implicit in routing priority (profile-level) | worker state tracked ("track the state of all tasks and workers") | utilization framing | A×3 (B-level for Connect) → B |
| System-executed matching per configurable rules | queue's routing method + evaluation method; ACD assigns | routing profile + priority/delay; platform assigns | Workflow filters/targets evaluated per task | Intelligent/Genius Routing matches | A×4 → B |
| Priority & wait management | priority values; two scoring methods; priority visible on interaction | priority and delay per queue in profile | task priority; timeout-driven escalation bumps priority | adaptive queuing under SLAs | A×3 + B |
| Expanding pool / overflow on wait | bullseye rings; conditional group routing; CGA on EWT threshold | — (not on fetched page) | timeout → next target (wider queue/higher priority) | "adaptive queuing" (unspecified) | A×2 → B (common, shape varies) |
| Skills relaxation vs strict matching | evaluation methods incl. "Disregard skills"; bullseye skill relaxation | — | filter/default-filter structure allows both | — | A (Genesys), structure supports in Twilio | single-product detail → keep qualified |
| Preferred/specific agent routing | Preferred Agent Routing; agent-owned callback; direct routing; last agent routing | — | `task.requested_agent == worker.agent_id` | — | A×2 → B (common) |
| AI/predictive routing | Predictive Routing; "automated call routing" AI glossary | — | — | Genius Routing ("AI-infused proficiency, customer intents") | A (Genesys) + B (Five9 page) → B-level claim "some/major products" |
| Customer value / intent as routing input | SBR "uses customer data"; skills requested from IVR | — | customer_value gold/silver/bronze example | "nuanced customer intents" | A×2 + B → B (common) |
| Multi-channel routing on one machinery | ACD email/message/SMS/callback/voicemail routing articles | profile specifies channels (voice/chat/task per docs family) | tasks from calls, messages, chats (docs diagram) | omnichannel routing claim | A×3 + B → B |
| Inbound/outbound blending | call blending glossary | — | — | inbound, outbound, blended | A×2 (B-level Five9) → B |
| Fallback endings: wait-for-match vs cancel/redirect | waits until agent with all skills becomes available (in strict configs); callbacks/voicemail/parking | — | task timed out → canceled | — | A×2 (divergent behavior → variant, not invariant) |
| Routing admin surface | queue admins assign routing/evaluation methods; skills mgmt; org/agent utilization | create routing profiles (channels/queues/priority/delay) | JSON workflow via API/SDK | admin console | A×3 + B |
| Programmatic control (API) | skill expression filters via API; Routing APIs page | — (not on fetched page) | REST API/JS SDK first-class | APIs & SDKs | A×2 + B |
| Routing performance visibility | abandoned/ASA/service-level per queue; route paths; live queue/skill metrics | — | "monitor performance" of tasks/workers | real-time/historical reporting | A×2 + B |

## Canonical Abstraction

### Level 0 — Defining Invariant (deliberately small)

Three properties; remove any one and the product stops being recognizable as this Type:

1. **Arriving interactions held as routable work** — customer interactions (any channel) enter queues/waiting pools where they wait independent of any specific agent. (Remove → intake-only telephony/IVR: automated handling without agent distribution.)
2. **A serving population with eligibility and availability** — agents/works carry attributes that define what they may handle (skills, languages, queue memberships) and a live state/capacity the system tracks. (Remove → a directory or dialer: no matching substrate.)
3. **System-executed, configurable matching** — the assignment decision itself is made by the engine per configured policy (not by a person picking up, and not fixed), matching each waiting interaction to an eligible, available agent or an alternative destination. (Remove → telephony switch or manual console.)

The canonical context is the contact center: customer-facing interactions in, human agents out, service-level pressure over the whole population. Scoping note: the machinery is general (Twilio TaskRouter routes leads and tickets with the same primitives), which is evidence that the contact-center scoping is the Type's canonical context, not its logical boundary.

### Level 1 — Common Mature Structure

- **Skill/proficiency model** on agents (skills, languages, proficiency levels) — the standard eligibility vocabulary (A×4).
- **Queue as the unit of routing policy** — per-queue routing method, evaluation method, priority/delay, member assignment (A×3 + B).
- **Priority and wait management** — priority values interacting with wait time; aging/escalation so long-waiting work advances (A×3 + B).
- **A repertoire of routing methods** — next-available standard, skills-based variants, preferred-agent, expanding-pool/overflow strategies (A×2 + B).
- **Intake-provided classification** — attributes (skills requested, intent, customer value, channel, identity) attached by IVR/flows/API before matching (A×2 + B).
- **Fallback behavior** — overflow to wider pools on wait thresholds, callbacks, voicemail, redirection, or cancellation; products differ on the terminal behavior (A×2, divergent → variant semantics, structure common).
- **Capacity/utilization control** — max concurrent interactions per agent/channel, utilization labels, states (A×2; likely common, single-page evidence for capacity specifics → keep qualified).
- **Blended inbound/outbound** — the same distribution machinery feeds outbound-connected work to the same agents (A×2 + B).
- **Cross-channel operation on one engine** — voice, email, chat/messaging, SMS routed by the same queue/skill machinery (A×3 + B).
- **Routing analytics** — waits, speed of answer, abandonment, service level per queue/skill; live and historical (A×2 + B).
- **Admin configuration surface + programmatic control** — admin consoles, queue/skill management, APIs/SDKs (A×3 + B).
- **AI/predictive routing** — AI-analyzed intent/complexity and learned agent-affinity used in matching (A (Genesys) + B (Five9); growing but not definitional).

### Level 2 — Variant / Optional Structure

- **Realization form** (the defining market fact of this Type): routing ships as (a) a documented subsystem of a contact-center platform (Genesys — a whole Resource Center section; Five9 — named capability), (b) a native platform concept (Amazon Connect routing profiles), (c) an independent API-level service consumed by developers building their own contact center (TaskRouter), and reportedly (d) embedded routing engines inside CRM/service suites (Salesforce/Zendesk/Dynamics — NOT directly evidenced this pass). No sampled vendor sells a complete standalone "routing platform" product with its own agent workspace — routing is consumed through or inside a host.
- **Rules authoring style**: admin-UI configuration (Genesys queue settings, Connect profiles) vs code-first JSON/expression documents (TaskRouter) vs flow-builder-authored filters (Genesys Architect skill expression filters).
- **Decisioning philosophy**: deterministic rules-first vs AI-first (predictive routing poles).
- **Terminal wait semantics**: hold-until-eligible (Genesys strict-skill configs) vs timeout-cancellation/escalation chains (TaskRouter) — both documented; neither is definitional.
- **Outbound coupling depth**: dialer campaigns feeding the same distribution (blending) vs inbound-only.
- **Generic task routing**: the same machinery applied to non-contact-center work (TaskRouter examples: leads, tickets) — adjacent usage, not the Type's center.
- **Multi-tenancy/segmentation**: routing objects partitioned per division/brand/BPO client (Genesys divisions include call routing objects).

### Level 3 — Vendor-specific (kept out of the final document)

- Genesys: bullseye ring mechanics; Conditional Group Activation with EWT thresholds; conversation score (one priority point = 60,000 ms of arrival-time credit) and priority-score methods; 7-day lookback on last-handled time; skill expression filters' compatibility matrix (work with standard/predictive + All Skills Matching only); direct routing; last agent routing; work automation; email/message parking; "route paths = queue + language + skills"; divisions access model; agent-owned callback config.
- Amazon Connect: one routing profile per agent; "Basic routing profile" default; default queue + default flows onboarding pattern.
- Twilio: Workflow JSON schema (filters/targets/expressions/default_filter); reservation-acceptance lifecycle; skip-timeout expressions; SQL-like expression syntax; PII/pseudonymization warning; TaskQueue SIDs.
- Five9: "Genius Routing" branding; "AI-infused proficiency levels"; "progressive queuing"; packaging of Intelligent Routing as a capability page.

## Vendor-specific Findings

See Level 3. Additionally: Five9's page asserts percentage CX statistics (containment, attrition) — marketing figures, excluded from all claims. Genesys glossary contains an editorial AI-summary of "Automated call routing" — treated as vendor positioning for AI-era routing, not a market definition.

## Boundary Findings

1. **vs Contact Center Platform (the load-bearing one).** The routing machinery IS the platform's distribution core: the sibling application document defines the platform's core as interaction → queue → distribution rules → agent → agent state, and lists this leaf as "component: routing decisioning on its own". This pass confirms: Genesys documents routing as a self-contained subsystem with its own admin role (queue administrator), config objects, and metrics; TaskRouter sells the machinery as an independent service ("the heart of a contact center"); Five9 packages it as a named capability. **Test held both ways:** remove routing decisioning from a contact-center platform and the rest (intake, telephony, agent desktop, recording, campaigns) has nothing to distribute — the platform collapses; remove the platform layers and routing decisioning remains a coherent, sellable thing. **Conclusion:** this leaf stands as a component-Type — the Type of the distribution machinery itself. It is a real, documentable Type whose canonical realization is *inside* the platform Type. Joint review recommended when the directory is revisited (no taxonomy change made in this pass).
2. **vs IVR Platform.** IVR = automated pre-agent handling (prompts, input collection, self-service); routing = matching waiting interactions to human agents. The seam is observable in both directions: the IVR doc states drift toward routing when "management of human agents" becomes the center of gravity; Genesys states "a customer can request skills, for example, from the IVR" — the IVR feeds attributes into the router, then hands off. A flow may route ("routes the call onward — to an agent, a queue") but that is a disposition of the IVR conversation, not the standing distribution machinery.
3. **vs Call Center Platform.** Voice-restricted sibling of the whole-platform Type. Routing machinery itself is channel-agnostic (Genesys ACD email/message/SMS routing; Connect profiles specify channels; TaskRouter tasks from calls/messages/chats). No separate routing Type for voice.
4. **vs Help Desk / Ticketing System.** Ticketing assigns *persistent records* (cases) to staff queues asynchronously, without live-interaction semantics (no hold, no agent-state-triggered assignment moment). The boundary is visible but porous at the edges: TaskRouter's own examples route "support request tickets" as tasks, and CRM suites reportedly embed interaction routing. When the center of gravity is live interaction distribution over agent availability, it is this Type; when it is the case record's lifecycle, it is Ticketing. [CRM/help-desk-embedded engines not directly evidenced this pass — Salesforce/Zendesk/Dynamics unreachable.]
5. **vs Workforce Management / Agent Scheduling.** WFM forecasts and schedules the agent pool to meet the demand that routing measures and serves; routing consumes availability that WFM plans. Interlock is explicit in Genesys docs (bullseye's skill-expression groups exist "to ensure compatibility with WEM forecasting and scheduling"). WFM handles no interactions; routing forecasts nothing.
6. **vs Contact Center Quality Management.** QM evaluates recorded interactions; routing decides live assignment. Routing produces the metrics QM/workforce planners consume (abandonment, ASA, wait) but performs no evaluation.
7. **vs generic workflow/task-routing engines (§10 workflow platforms, agent-orchestration).** Same shape (work items, pools, rules) but no customer-interaction semantics, no service-level/abandonment measurement, no channel machinery. TaskRouter sits near this line by design (generic workers/tasks) but its self-positioning and blueprint remain contact-center-first.
8. **vs UCaaS/business telephony.** Internal communications lack external-party queues and agent-operation semantics; routing presupposes a serving population organized to receive customer work.

### Historical / market-sample check

The minimal three-part definition (queue-held interactions + eligibility/availability population + system-executed configurable matching) fits premise-era ACDs: skills tables, hunt groups, and routing scripts were the core of 1980s–90s premise ACDs long before cloud suites, AI scoring, expression languages, or API-driven workflows. Those era-typical additions are all Level 1/2/3, not definitional. The definition also fits a digital-only help-desk routing engine (queues + skills + availability, no telephony) and an API-level router. Historical check passes.

## Uncertainties

1. No directly observed standalone commercial product named "contact center routing platform"; the Type's independence is supported by TaskRouter (API service) and by the subsystem documentation of suite vendors, but the market may contain routing-only products not sampled. Flagged as Boundary Issues rather than resolved.
2. CRM/help-desk-embedded routing engines (Salesforce Omni-Channel, Zendesk Omnichannel Routing, Dynamics 365 unified routing) could not be fetched — all three attempts failed (SPA/JS/404). Claims about them are market-context only and none appear in the final document as product claims.
3. Amazon Connect evidence is limited to the routing-profile concept page; deeper routing mechanics (attribute-based routing, flows) are known from the sibling pass only at overview level.
4. Five9 evidence is product-page level (Tier 2); help-center bodies unreachable; capability claims used only where they echo cross-product structures.
5. Premise-ACD historical fit is asserted by reasoning, not by fetching vintage documentation (reasonable confidence, recorded as inference).
6. Terminal wait semantics (hold vs cancel) differ across the sample; the full space of fallback behaviors (cancellation, redirection to bots, parking) is documented for Genesys/Twilio only.

## Final Synthesis

A Contact Center Routing Platform is the **distribution machinery of a contact center** — the engine that turns unstructured inbound demand into ordered agent work. Its defining core is exactly three structures: (1) arriving interactions held as routable work in queues/pools independent of any agent; (2) a serving population of agents/works carrying eligibility attributes (skills, languages, queue memberships) and live availability/capacity state; (3) system-executed, configurable matching that assigns each waiting interaction to an eligible, available agent or alternative destination per standing policy.

Around that core, mature products standardize on: a skill/proficiency vocabulary; the queue as the unit of routing policy (routing method + evaluation method per queue); priority that interacts with wait time; a repertoire of methods (standard next-available, skills-based, preferred-agent, expanding-pool/overflow); intake-provided classification (skills requested, intent, customer value, channel, identity); fallback machinery (wider pools on wait thresholds, callbacks, voicemail, cancellation); capacity/utilization control; blended inbound/outbound; cross-channel operation on one engine; routing analytics (waits, ASA, abandonment, service level); admin configuration surfaces plus API control; and, increasingly, AI/predictive matching.

The Type's defining market fact: routing is almost always consumed inside a host — as the core machinery of a contact-center platform, a named capability of a suite, a native concept of a platform, or an API service for building one — rather than as a standalone product with its own agent workspace. The Type therefore stands as the component-Type of the contact-center family: real, coherent, documentable, and bounded on all sides (IVR, WFM, QM, ticketing, telephony).
