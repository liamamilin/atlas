# Research Notes — Call Center Platform

Research date: **2026-09-07**
Slug: `call-center-platform` (DIRECTORY §07 Sales, Customer & Revenue)

---

## Research Goal

Understand what a Call Center Platform actually is as an Application Type: what objects and machinery it consists of, how a customer phone call moves from arrival to resolution, how agents work inside it, how the operation is run and measured, and where its boundaries lie against the neighboring leaves that share this family (Contact Center Platform, Cloud Contact Center / CCaaS, IVR Platform, Contact Center Routing Platform, WFM for Contact Centers, Agent Scheduling, Contact Center Quality Management, Sales Dialer, Help Desk).

## Initial Boundary (pre-research hypothesis)

- A call center platform is the operator-facing system that receives/originates customer **phone calls**, **queues** them, **distributes** them to **agents**, supports the live call, and measures the operation.
- Nearest confusables: Contact Center Platform (multi-channel scope), CCaaS (delivery form), IVR Platform (automated handling), Sales Dialer (individual outbound), Help Desk (ticket-based).
- Working hypothesis for the defining seam: **the voice telephone call as the unit of customer contact + distribution of calls to agents**. Omnichannel, cloud, AI, WFM are not definitional.
- This leaf is one of a sibling cluster in the directory; the call-center / contact-center / CCaaS trio risks being one Type with different media/deployment scope. To be resolved as a Boundary Issue, not silently.

## Research Questions

1. What happens to an inbound call between network arrival and agent answer?
2. What is the agent's working surface and per-call loop (answer → handle → wrap-up)?
3. What routing logic decides which agent gets which call?
4. What machinery exists for outbound calling (dialers, campaigns, compliance)?
5. What operational layer surrounds the calls (monitoring, reporting, quality, workforce)?
6. What does an administrator configure?
7. What are the agent/call state models?
8. How do products differ by delivery form, segment, and product philosophy?
9. Would older / on-prem / open-source call center products still satisfy the definition (historical check)?

## Representative Products

| Product | Why sampled | Evidence tier |
|---|---|---|
| Amazon Connect (AWS) | hyperscaler cloud platform; best public operational documentation; voice-first heritage, now omnichannel | Tier-1 (admin guide) |
| Genesys Cloud CX | market-leading CX suite; deep public glossary/articles defining ACD, queues, routing, metrics | Tier-1 (Resource Center) |
| Five9 | call-center-native cloud vendor, mid-market/enterprise; explicit inbound/outbound/blended poles and dialer modes | Tier-2 (product pages ×3) |
| Talkdesk | cloud-native contact center platform, no-code/low-code philosophy, app marketplace | Tier-2 (platform page) |

Context-only (fetched but unreachable — no claims made): NICE CXone (help 404 + empty root), VICIdial (open-source outbound dialer; site JS-redirect ×2), Avaya Call Center Elite (docs transport errors ×2). These remain market-context anchors for the historical / on-prem / outbound-only poles.

## Sources

- Amazon Connect admin guide — What is Amazon Connect (docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html) — fetched 2026-09-07 ✓
- Amazon Connect admin guide — Connect feature overview (docs.aws.amazon.com/connect/latest/adminguide/connect-concepts.html) — fetched 2026-09-07 ✓
- Genesys Cloud Resource Center — Home (help.mypurecloud.com) — fetched 2026-09-07 ✓
- Genesys Cloud Resource Center — Glossary (help.mypurecloud.com/691/) — fetched 2026-09-07 ✓
- Genesys Cloud Resource Center — Products and solutions (help.mypurecloud.com/400147/) — fetched 2026-09-07 ✓
- Five9 — Inbound Contact Center (five9.com/products/capabilities/inbound-contact-center) — fetched 2026-09-07 ✓
- Five9 — Outbound Contact Center (five9.com/products/capabilities/outbound-contact-center) — fetched 2026-09-07 ✓
- Five9 — Global Voice (five9.com/products/capabilities/global-voice) — fetched 2026-09-07 ✓
- Talkdesk — Contact Center Platform (talkdesk.com/contact-center-platform/) — fetched 2026-09-07 ✓
- NICE CXone help (help.nice-incontact.com) — 404/empty ×2 — abandoned, no claims
- VICIdial (vicidial.org) — JS redirect ×2 — abandoned, no claims
- Avaya docs (docs.avaya.com) — transport error ×2 — abandoned, no claims

Note on evidence: no vendor support/KB article bodies were reachable for Five9 or Talkdesk beyond product pages (support.talkdesk.com transport error; Five9 community login-gated). All precise operational numbers observed in sources (e.g., Amazon's 16 kHz softphone audio, 110+ countries, email-address counts, Genesys's "compliance abandon threshold default two seconds") are deliberately **excluded** from the final document per the evidence-calibration rule; they remain recorded here only as proof the details exist in vendor docs.

---

## Product observations

### Amazon Connect (evidence layer A)

- Personas: customers (contact the org because they can't self-serve, via any channel), agents (help customers "through voice, chat, SMS, or other channels, and then document the interaction"), managers/supervisors ("monitor their team's metrics and readjusting their configuration", onboard and coach), administrators ("provision phone numbers", "define queues and routing profiles, implement flows, create rules to set up alerts").
- Voice handled by a softphone on the agent's computing device (call delivered over the internet to the desktop).
- Channels: voice, chat/SMS, web/video calling, tasks, email. Omnichannel with shared routing/business logic across channels; interaction history preserved across channels.
- Conversational IVR and chatbots for self-service; flows built in a drag-and-drop designer ("design your interactive voice response (IVR) or chatbot experiences to help your customers self-serve"); native Lambda integration for custom logic.
- Routing: "routing profiles"; contact priority and routing based on agent skills, queue priorities, contact attributes, real-time metrics.
- Agent workspace: single application; customer info, tasks, schedules, agent assist, case tracking; third-party apps embeddable; step-by-step guides presented contextually (by queue/customer info/self-service responses); quick responses; post-contact AI summary for after-contact work (ACW).
- Unified customer view (profiles assembled from CRM data such as Salesforce/Zendesk/ServiceNow + contact history); case management for issues spanning multiple interactions.
- Outbound campaigns: contact list + channel + message (+ pre-recorded audio before connecting to agent); predictive dialer and ML answering-machine detection; "up to millions of customers daily" (marketing-precise — excluded from final doc).
- Tasks: "other types of agent work" delivered through "the same routing and agent experience used with voice, chat".
- Supervision: real-time metrics reports (queues drill-down), historical metrics, login/logout reports, agent activity audit; monitor live calls with Monitor ↔ Barge toggle (listen in, coach/whisper, barge-in); contact search with transcript; evaluations with forms + AI recommendations; screen recordings.
- WFM: forecasting (contact volume + average handle time from historical metrics), capacity planning (FTE vs service-level target), scheduling (shift profiles, staffing groups, per-channel service level / average speed of answer targets, HR/business rules).
- Admin: telephony managed as a service (claim DID/toll-free numbers), flows designer, security, elasticity ("tens, or tens of thousands of agents"), active-active regional resiliency (+ optional multi-region).

### Genesys Cloud CX (evidence layer A)

- **ACD defined**: "a standard contact center term used to reference the system, device, or entity that automatically answers incoming calls and assigns waiting interactions to the most appropriate agent based on the caller's needs using routing rules. ACD calls are associated with a queue." Non-ACD calls are not associated with a queue.
- **Queue**: "a 'waiting line' of interactions"; distribution queues tag interactions; agents join queues; leaving a queue stops handling.
- **Agent**: "a person who is the primary point of human customer contact and manages inbound or outbound calls and other customer interactions" (a.k.a. CSR).
- **Skill**: expertise an agent needs for an interaction, with proficiency ratings considered by the ACD when matching. Skills-based routing; bullseye routing (agent pool expands over time); preferred agent routing.
- Metrics: abandoned call (inbound = caller disconnects before reaching an agent; outbound true-abandon vs compliance-abandon), abandoned rate (abandoned/offered), ASA (average wait before answer), AHT (talk + hold + ACW + outbound dialing/contacting), ACW (keying activity codes, updating customer databases, filling forms after the interaction), talk segments, service level (% answered within target), answered.
- Flows: Architect executes flows per media type; auto-attendant ("business logic for building work flows to route, categorize, define, and prioritize interactions"; offload volume to self-service); call flow = caller's experience prior to agent assignment; prompts (.wav), DTMF, secure IVR.
- Outbound: campaign = "configuration approach to dialing a list of external numbers and delivering those calls to a queue or call flow" (dialing mode, contact list, DNC list, scheduled calling times, outbound flows, agent scripts); per-campaign dialing mode (some modes present info to agent before dial, some connect agent only after live party); agentless dialing mode (plays message, no agent); call analysis/AMD (CPA/CPD — live person / fax / answering machine); DNC lists (incl. FTC Telemarketing Sales Rule internal lists); zone sets (time-zone/day/time calling windows); call blending (coordinated delivery of inbound and outbound to the same agents); agent-owned callback (waits for owning agent; requires preferred-agent routing).
- Telephony: ANI (caller identification, matched to contact record for screen display), DNIS (number dialed), DID, E.164, BYOC Cloud / BYOC Premises (SIP trunks; on-prem Edge devices handle telephony events/media), ELIN/emergency dialing.
- QM: evaluation forms (scorecards), critical questions (yes/no, compliance-critical), calibration (evaluator consistency), annotations on recordings, PCI encryption keys.
- WFM: forecast methods (ensemble of ARIMA/Holt Winters/...; automatic best method), shrinkage ("time agents are not available... even though scheduled"), workforce planning across channels.
- Org structure: divisions (group configurable objects: queues, flows, campaigns, scripts, users, DNC lists...), management units, roles (employee role lowest; admin grants permissions).
- Licensing: named / concurrent / hourly models. **Genesys Cloud EX**: WEM-only license — "does not include voice, email, or digital interaction handling capabilities" — WFM/QM for interactions handled on external platforms. Strong boundary evidence: the workforce layer alone is not a call center.
- **Vendor's own glossary seam**: call center = "physical location where a high volume of customer and other telephone calls are handled... typically provide voice only inbound, outbound and limited self-service customer interactions"; contact center = "a modern call center. It manages inbound and outbound customer communications through a variety of channels" (e.g., email, website chat).
- UC pole: Collaborate/Communicate (chat, video, telephony for all employees) exist in the suite but are distinct from the contact center (Communicate's auto-attendant is an internal-telephony attendant).

### Five9 (evidence layer A for page content; marketing-leaning)

- Inbound: cloud contact center reachable via voice/SMS/webchat/social; IVA and visual IVR self-service; "route customers to the best-suited agents using skill or priority-based routing"; agents receive "a screen pop of customer info"; agent assist provides real-time guidance/checklists/transcriptions.
- Outbound: dialer technologies named predictive, power, progressive, preview, plus "Manual Touch Mode" (agent-initiated dialing); campaign & list management; compliance-relevant tools: DNC list management, time-zone rules dialing, Certified Caller (STIR/SHAKEN callernet validation), number reputation management, E911; agent efficiency: agent scripting, disposition timers and redials, answering-machine detection, automatic voicemail, vertical dialing mode, list-penetration mode; customer experience: web callback, CRM/CTI screen pop; local caller ID.
- Blended: agents move between inbound and outbound "based on inbound traffic flow with no disruption" (call blending).
- Global Voice: vendor-operated carrier network with Core Edges (full application stack regions) and Voice Edges (media POPs); BYOC or vendor telco; carrier redundancy, multi-carrier routing, route advance; recording data-residency options.
- Suite modules: Agent Desktop, Supervisor Desktop, engagement workflow, CRM integrations (Salesforce/ServiceNow/Microsoft/Oracle/Zendesk), UC integrations, APIs/SDKs, admin console, advanced campaign manager, AI stack (IVA, agent assist, summaries, insights, governance), Workforce Engagement (WFM, QM incl. "agentic QM", interaction analytics, performance management, gamification), reporting & analytics, marketplace.
- Market segments: healthcare, financial services, retail, higher-ed, government, sales & telemarketing, customer service, **outsourcing (BPO)**, **collections**; company sizes enterprise/mid/small.

### Talkdesk (evidence layer A for page content; marketing-leaning)

- Positioning: "cloud contact center platform"; "born in the cloud"; enterprise scale + consumer simplicity; AI agents + orchestration; no-code development.
- Named products: Studio (orchestration & routing), Navigator, Copilot (agent AI), Autopilot (self-service), Agentic Outbound, Omnichannel Engagement, Workforce Engagement, Quality Management, Interaction & Quality Analytics, Business Intelligence, Employee Collaboration, Automation Flows; AppConnect marketplace; 100+ out-of-box integrations (Salesforce, Zendesk).
- Global Communications Network for call distribution/voice quality; flexible deployment ("connect to any carrier and select your cloud region"); Talkdesk Embedded (embedded form); security certifications.
- FAQ defines cloud contact center: "manage customer support interactions... across various channels, including voice, chat, SMS, and email"; agents access remotely.

### Cross-product Comparison

| Structure | Amazon Connect | Genesys Cloud | Five9 | Talkdesk | Verdict |
|---|---|---|---|---|---|
| Telephony call as unit of contact | ✓ (voice channel) | ✓ (call center = voice) | ✓ (voice pole of suite) | ✓ (voice channel) | Defining |
| Queue as waiting line | ✓ queues + routing profiles | ✓ distribution queues (explicit definition) | ✓ skill/priority routing implies queues | ✓ Studio routing | Defining |
| ACD distribution to agents by rules | ✓ | ✓ (explicit ACD term) | ✓ | ✓ | Defining |
| Agent role + availability states | ✓ (agent workspace, login/logout reports, RTM) | ✓ (agent, employee role; agent states in metrics) | ✓ (agent desktop) | ✓ (agent workspace implied; WEM) | Defining |
| IVR/attendant intake layer | ✓ flows | ✓ Architect/auto-attendant | ✓ visual IVR/IVA | ✓ Studio/flows (implied by products) | Common mature |
| Skills/priority/preferred routing | ✓ | ✓ + bullseye + proficiency | ✓ skill or priority | ✓ (Studio) | Common mature |
| Agent per-call controls + screen pop + scripts + wrap-up | ✓ workspace, quick responses, ACW | ✓ scripts, wrap-up codes, ACW, ANI screen match | ✓ screen pop, scripting, disposition timers | ✓ Copilot/workspace (implied) | Common mature |
| Call recording | ✓ (recorded/analyzed, contact details) | ✓ QM recording | ✓ quality monitoring, data residency | ✓ QM | Common mature |
| Real-time + historical metrics | ✓ RTM/dashboards | ✓ service level/ASA/AHT/abandoned metrics | ✓ real-time & historical reporting | ✓ BI | Common mature |
| Supervisor monitor/whisper/barge | ✓ Monitor/Barge toggle | ✓ coaching/monitoring (glossary) | ✓ Supervisor Plus | ✓ (implied; not directly seen) | Common (Talkdesk weaker evidence) |
| Outbound campaigns + dialer modes | ✓ predictive + AMD | ✓ campaign/dialing modes/agentless/blending/callback | ✓ 5 dialer modes + compliance pack | ✓ Agentic Outbound | Common mature (outbound pole; some centers inbound-only) |
| Outbound compliance machinery (DNC, time-zone windows, callernet trust, E911) | — (campaigns page only) | ✓ DNC/zone sets/TSR internal lists | ✓ DNC/time-zone/STIR-SHAKEN/E911 | — | Common where outbound; precision varies |
| Telephony/carrier administration | ✓ claim numbers, managed telephony | ✓ BYOC Cloud/Premises, Edge, DID/E.164 | ✓ Global Voice, BYOC | ✓ any carrier, cloud region | Common mature; implementation varies widely |
| Callback offers | ✓ (outbound campaigns; task follow-up) | ✓ agent-owned callback | ✓ web callback | — | Common |
| CRM integration / screen pop | ✓ Customer Profiles | ✓ ANI→contact record; CX Cloud w/ Salesforce | ✓ CRM/CTI screen pop, 5 CRMs | ✓ 100+ integrations | Common mature |
| Case/profile mgmt inside platform | ✓ Cases + Profiles | — (external contacts; CRM-integrated) | — | ✓ (not directly seen) | Variant (platform-boundary dependent) |
| WFM (forecast/capacity/schedule) | ✓ | ✓ (forecast methods, shrinkage) | ✓ WFM module | ✓ WEM | Common as module; separable |
| QM (evaluations, calibration) | ✓ evaluations + screen recording | ✓ evaluation forms/critical questions/calibration | ✓ QM module | ✓ QM | Common as module; separable |
| Omnichannel expansion (chat/SMS/email/social/video/tasks) | ✓ native | ✓ digital channels | ✓ omnichannel menu | ✓ Omnichannel Engagement | Variant drift toward Contact Center |
| AI layer (bots, assist, summaries, analytics) | ✓ Lex/agent assist/summaries | ✓ Agent Copilot/Admin copilot/AI summarization | ✓ IVA/assist/summaries/insights | ✓ Autopilot/Copilot/Navigator | Common today, era-specific — not definitional |
| Delivery: cloud-native vs hybrid/on-prem components | cloud-only | cloud + BYOC Premises Edges (hybrid) | cloud (+ data residency) | cloud (+ embedded) | Variant |
| Multi-tenant BPO / vertical packs | — (not directly seen) | divisions (brand/business unit separation) | outsourcing & collections verticals | industries menu | Variant |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Call Center Platform is recognizable only if all of the following hold:

1. **Telephony call as the unit of customer contact** — the platform carries real-time voice telephone conversations with external parties (customers, prospects, citizens), inbound and/or outbound, over telephony (PSTN/SIP/VoIP). Remove the phone call and the product is an email/chat/ticket system — a different Type.
2. **System-managed distribution of calls to agents** — the platform holds calls awaiting service and matches each call to an agent according to configurable rules (the ACD function; for outbound, matching happens at dial/connect time under campaign rules). Remove distribution (calls handled ad hoc by individuals) and it is business telephony, not a call center.
3. **Agents as the platform's operating role with system-tracked availability** — staff whose job is handling calls; the platform tracks who is available/handling/idle and drives work to them. Remove the agent population and it is an IVR/self-service platform.

Historical check: this minimal triple deliberately excludes cloud delivery, omnichannel, skills-based routing, IVR, recording, screen pops, dialers, WFM, and AI. An on-prem ACD from the pre-cloud era, an open-source dialer, and a modern cloud suite all satisfy it. (Older products were not directly fetched in this pass — see Uncertainties — but the ACD definition Genesys publishes as a "standard contact center term" is itself the continuity proof; no current-market feature is load-bearing in the definition.)

### L1 — Common Mature Structure

- IVR / auto-attendant intake layer before agent assignment (menus, prompts, DTMF, self-service, data collection, routing decision) — present in all four sampled products.
- Configurable routing logic beyond simple assignment: skills (with proficiency), queue priority, preferred agents, expanding-agent-pool strategies.
- Agent workspace with per-call loop: caller identification (ANI/CLI → screen pop), call controls (answer/hold/mute/transfer/conference), scripts, disposition/wrap-up coding, after-call work gating availability.
- Call recording.
- Real-time operational view: queue/agent states, waits, service level, abandonment; supervisor monitor/whisper/barge and coaching.
- Historical reporting: handle time, answered, abandoned, service level.
- Outbound campaign machinery: campaign over contact list, dialing modes, answering-machine detection, DNC handling, time-zone calling windows, redial/disposition rules, callbacks (incl. web/agent-owned callbacks).
- Telephony administration: number provisioning (DID/toll-free), carrier connectivity (vendor telco and/or BYOC), call routing/number plans, emergency calling.
- CRM/CTI integration: customer record association and screen pop.
- API surface and admin console.

### L2 — Variant / Optional Structure

- Delivery form: cloud (CCaaS-style), hybrid (on-prem media edges), on-prem legacy; embedded form inside other products.
- Media scope: voice-only pole vs omnichannel expansion (chat/SMS/email/social/video/tasks) — the drift that produces "Contact Center Platform".
- Outbound orientation: inbound-only, outbound-only (dialer-farm style, incl. agentless campaigns), blended.
- AI layer: conversational IVR/bots, real-time agent assist, auto-summaries, sentiment/transcript analytics, AI-assisted evaluations — era-common, not definitional.
- Workforce engagement modules: WFM (forecasting/capacity/scheduling/shrinkage), QM (evaluation forms/calibration), gamification, performance management — separable (Genesys EX ships WEM without interaction handling).
- In-platform case/profile management vs CRM-external systems of record.
- Vertical/regulatory packs: collections, telemarketing, healthcare, government, BPO multi-tenancy (divisions/brands), data residency, recording-consent policies, PCI handling in IVR.
- Licensing: named/concurrent/hourly; usage-based.
- Resiliency: multi-region, active-active.

### L3 — Vendor-specific (kept out of final document)

- Genesys: Architect, Bullseye routing, distribution-queue tagging model, BYOC Premises Edge hardware, divisions/management units, critical questions, calibration, ensemble forecasting methods, agent-owned callback rules, Genesys Cloud EX/Digital/CX license split, "Connect Customer"-style product naming; glossary's call-center-vs-contact-center distinction (used as boundary evidence).
- Amazon Connect: Lex integration, CCP/agent workspace, step-by-step guides, Customer Profiles/Cases, task channel, "Connect Customer" rename (2026), 16 kHz softphone claim, email-address limits, region resiliency SKU.
- Five9: Core Edge/Voice Edge network, Agent Desktop Plus/Supervisor Plus, Manual Touch Mode, vertical/list-penetration dialing modes, Inference IVA studio, Pindrop fraud integration, "agentic QM", gamification.
- Talkdesk: Studio/Navigator/Copilot/Autopilot naming, AppConnect marketplace, Global Communications Network MOS claims, Talkdesk Embedded, CXA/Data Cloud.

## Rejected Findings (considered, not promoted)

- **"Cloud-delivered" as defining** — rejected: on-prem/hybrid poles still exist (Genesys BYOC Premises; legacy on-prem ACDs as market context); delivery is a variant.
- **"Omnichannel" as defining** — rejected: the vendor glossary itself defines call centers as voice-centric; omnichannel is the contact-center drift.
- **"IVR" as defining** — rejected: intake layer is common but a call center can route bare calls; IVR platforms exist standalone.
- **"Skills-based routing" as defining** — rejected: it is the dominant modern routing style, but simple/priority routing still satisfies the Type; skills are one rule vocabulary.
- **"Dialer" as defining** — rejected: many centers are inbound-only; outbound machinery is a pole, not the definition.
- **"WFM/QM" as defining** — rejected: modular and separable; Genesys EX explicitly excludes interaction handling.
- **"AI/bots" as defining** — rejected: era-common layer.
- **Precise numbers/thresholds** (softphone audio rates, country counts, abandon thresholds, license pricing) — rejected from final doc: single-source, plan/vendor-specific.

## Boundary Findings

- **Contact Center Platform**: same operational machinery, wider media scope. Genesys's own glossary: call center = "voice only inbound, outbound and limited self-service"; contact center = "a modern call center" across channels. Seam test: strip the voice/call machinery from a contact center and it can still be a contact center (email+chat); strip it from a call center and the Type collapses. Market reality: modern suites market themselves as contact centers while operating voice at their core — the two leaves risk being one Type with media scope variants. **Flagged for joint review.**
- **Cloud Contact Center / CCaaS**: deployment/packaging form of the same structure (Genesys glossary defines CCaaS as the cloud-based consumption model). Alias/variant risk vs Contact Center Platform. **Flagged for joint review.**
- **IVR Platform**: automates call handling without agent distribution as the core; inside call center platforms the IVR is the intake component. Standalone IVR = self-service/telecom-surface Type.
- **Contact Center Routing Platform / WFM for Contact Centers / Agent Scheduling / Contact Center Quality Management**: component/decommissioned layers of the same operation; each can exist standalone but lacks the call-distribution core (Genesys EX is the existence proof for WFM without interaction handling).
- **Sales Dialer**: individual-rep outbound calling embedded in sales workflow; overlaps with campaign dialing at small scale; call center outbound adds team-scale campaign machinery, compliance, and ACD blending.
- **Help Desk / Ticketing System**: system of record for cases/tickets with queues and SLAs but asynchronous, record-centric; call center is live-voice-and-distribution-centric. They integrate (screen pop, case creation) but neither contains the other.
- **Customer Support Chat / Omnichannel Customer Service**: chat or digital-media-primary surfaces.
- **Conference Calling Application**: multi-party meeting bridge among invited participants; no queueing/distribution/agent operation.
- **Softphone / UC / PBX**: general telephony for all employees; no ACD/queue/agent-operation semantics (Genesys ships Communicate separately from the contact center).
- **Government Contact Center (another leaf)**: domain variant of this Type, not a separate structure — candidate alias note for that leaf's pass.

## Uncertainties

- NICE CXone, VICIdial, Avaya Call Center Elite could not be fetched (404/JS-redirect/transport). The historical/on-prem/outbound-only poles are therefore argued structurally (via Genesys's ACD/CCaaS definitions and BYOC Premises hybrid mode), not from directly observed legacy docs. No precise claims about those products are made anywhere.
- Five9/Talkdesk evidence is product-page tier; their KB bodies were unreachable. Claims attributed to them are kept at the capability level visible on those pages.
- Talkdesk supervisor tooling (monitor/whisper/barge) and Studio routing details were not directly observed — kept out of strong claims.
- Whether the market still sustains a meaningful voice-only "call center platform" product distinct from "contact center" is uncertain: sampled vendors all position omnichannel suites with voice at the core. Treated as a boundary issue, not silently merged.
- Exact state names/numbers of agent states, queue priority semantics, and abandon-rate thresholds vary by product and were not cross-verified — no numeric claims made.

## Final Synthesis

A Call Center Platform is the operator-side platform for running a voice call center: it terminates and originates customer telephone calls, holds them in queues, distributes them to agents by configurable rules, equips agents with call handling and after-call work, and measures the operation in real time and historically. Its defining core is the triple **telephony call as unit of customer contact + system-managed call distribution (ACD) + agents as system-tracked operating role**. IVR intake, skills routing, recording, monitoring, reporting, outbound campaign/dialer machinery, telephony administration, and CRM integration are the common mature structure. Delivery form (cloud/hybrid/on-prem), omnichannel expansion, AI, WFM/QM modules, verticals, and licensing are variants. The strongest boundary is media scope against Contact Center Platform and delivery form against CCaaS — recorded as joint-review boundary issues.
