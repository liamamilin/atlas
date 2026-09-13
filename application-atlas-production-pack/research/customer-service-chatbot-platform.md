# Research Notes — Customer Service Chatbot Platform

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Customer Service Chatbot Platform really is as an Application Type: what exists inside it, who operates it, how the work flows, and where its boundaries sit against the dense §07 neighborhood (Customer Support Chat, Help Desk, Contact Center, IVR, Self-service Portal, Knowledge QA) and against the 2026-era agent-platform drift.

## Initial Boundary

Working hypothesis before research:

- Core use: businesses deploy automated conversational agents ("chatbots") that talk with customers on digital channels (website chat, in-app, messaging apps, email) to answer, resolve, and execute service actions without human agents.
- Primary users: service/support operations teams (bot builders, bot managers, CX ops) — customers are counterpart participants, not operators.
- Nearest neighbors suspected: Customer Support Chat (human live chat), Help Desk / Ticketing (record-centric), Contact Center Platform (live distribution), IVR Platform (voice twin), Knowledge Question Answering Application (answer deliverable), Self-service Support Portal (async), Agent Development Platform (dev-side drift), Customer-to-Business Messaging Application (channel substrate), Digital Concierge (hospitality variant — cross-reference from that pass).
- Prior passes already fixed seams to honor:
  - KQA pass: "vs customer-service-chatbot-platform (deliverable vs conversation business)"; "actions beyond answering — chatbot-platform drift zone".
  - IVR pass: "remove the voice medium → chatbot/web form"; "remove call anchoring and add agent orchestration → conversational AI platform".
  - Help Desk pass: "chat tools own one real-time channel; the desk owns the tracked record… Chat conversations become tickets".
  - Digital Concierge pass (STATUS Boundary Issues): hospitality guest-messaging/chatbot products could be claimed here; adopted discriminators are stay anchoring and physical-service fulfillment semantics.

## Research Questions

1. What is the "bot" as an object in these systems — how is it authored, versioned, published?
2. What is the unit of work — the conversation? What states does it carry?
3. How does the bot↔human seam work (handoff, escalation, push-back, no-human behavior)?
4. What does the bot converse from (knowledge, guidance, flows) and act on (integrations, actions)?
5. What surfaces exist for operators (build, test, deploy, monitor) and for customers (chat widget)?
6. How is automated performance measured (automation/resolution rate, CSAT/CX, topics)?
7. Where are the boundaries vs live chat, help desk, contact center, IVR, KQA, self-service portal, agent platforms?
8. Historical check: do pre-LLM dialog-tree/FAQ bots satisfy the same core?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Tier | Evidence |
|---|---|---|---|
| Intercom (Fin AI Agent) | messenger-native service suite, AI-agent-first | mid-market/enterprise | Tier-1 (help center articles fetched) |
| Zendesk (AI Agents) | ticket-centric service suite with embedded AI agents | enterprise | Tier-2 (product page; help center sign-in-walled) |
| LivePerson (Conversational Cloud) | enterprise conversational cloud; bot-as-agent-worker; BYOB | enterprise | Tier-1 (knowledge center articles fetched) |
| Chatwoot (Captain + AgentBot) | open-source shared-inbox suite; SMB | SMB / self-hosted | Tier-1 (user guide articles fetched) |

Dropped after failures (per source-access rules): Ada (help.ada.cx transport error; ada.cx/support 403 — 2 failures), Tidio (help.tidio.com, tidio.com/help — 2 transport errors), Freshchat (help.freshchat.com transport error ×1, not retried after sample filled). The SMB pure-play pole is covered indirectly by Chatwoot.

## Sources

- Intercom Help Center — https://www.intercom.com/help/ ; Fin AI Agent collection https://www.intercom.com/help/en/collections/6485365-fin-ai-agent ; "Fin AI Agent explained" https://www.intercom.com/help/en/articles/7120684-fin-ai-agent-explained (fetched 2026-09-08)
- Zendesk — AI Agents product page https://www.zendesk.com/service/ai-agents/ (fetched 2026-09-08); support.zendesk.com help center returns JS shell / sign-in wall (root and article URL both) — Tier-1 not reachable
- LivePerson Customer Success Center — https://community.liveperson.com/kb ; "How bots work in our Conversational Cloud" https://community.liveperson.com/kb/articles/1290 (fetched 2026-09-08)
- Chatwoot User Guide — https://www.chatwoot.com/hc/user-guide/en ; "Introduction to Captain" article 1738101283; "How to use Agent bots?" article 1677497472 (fetched 2026-09-08)
- Cross-referenced prior passes: research/help-desk.md, research/contact-center-platform.md, research/ivr-platform.md, research/knowledge-question-answering-application.md, research/self-service-support-portal.md, research/remote-customer-support-platform.md, research/customer-to-business-messaging-application.md

## Product A — Intercom (Fin AI Agent)

### Key observations (Layer A — directly observed)

- Fin is positioned as an "AI agent for customer experience… ready to resolve your most complex queries on all your channels"; roles: Service, Sales, Ecommerce — one agent switching roles by conversation context.
- The operating loop is explicit: **Train → Test → Deploy → Analyze** ("The Fin Flywheel").
- **Train**: Content library (multi-source: Help Center articles, internal support content, PDFs, webpages); Audiences (content targeting by plan/location/brand); tone of voice + answer length; Guidance (custom instructions/policies); Data connectors (personalized answers, perform tasks on behalf of customers); Fin Tasks (multi-step processes, e.g. cancel an order, refund a subscription); Fin Procedures (document-style editor with code and data connectors in steps); multilingual (45+ languages claimed); Fin Vision (images).
- **Test**: Fin previews (real-time, per audience/brand/persona); Batch testing (import real conversations, evaluate accuracy); Simulations (scenario/edge-case testing of procedures); answer rating; answer inspection (see which sources/settings shaped an answer).
- **Deploy**: channels — chat (Messenger, WhatsApp, SMS, social), email, voice (Fin Voice), Slack, Discord; Workflows integration; Outbound/proactive triggering from behavioral signals (rage click, abandoned checkout); **human handoff** — "Fin will always automatically hand off when that is the safest option for the customer, including when it detects high-risk content such as self-harm… jailbreak attempts, or high-risk medical, legal, or financial advice"; escalation guidance and rules are operator-managed; behavior configurable when no human agents are available; audience targeting; usage limits with notifications when a defined resolution limit is reached.
- **Analyze**: Performance dashboard (resolution rate, involvement rate, CX score); Optimize dashboard (AI-generated improvement suggestions); Topics Explorer (AI-grouped conversation topics); conversation monitoring in the Inbox; holistic AI+human reporting; Fin CSAT reporting; answer debugging.
- Settings: Fin identity customization (name/avatar/branded identities), AI Agent **Disclosure** setting (transparency), multilingual setup, audiences.
- Integrations: "Fin integrates with any helpdesk" — Fin for platforms (Zendesk, Salesforce, HubSpot): uses existing channels/tickets, follows existing assignment rules, "escalates to agents in your preferred inbox"; hand-over of Fin conversations to another support tool.
- Intercom runs its own help center on Intercom ("We run on Fin") — the vendor dogfoods the Type.

## Product B — Zendesk (AI Agents)

### Key observations (Layer A where page-level, otherwise Tier-2 positioning)

- Product page (Tier-2): "Self-improving AI agents built for resolution… handle complex, multi-step workflows across channels and connect to the systems your business already runs on."
- Channels: messaging (web, mobile, social), email, voice; "any platform" — AI agents deployable into other service environments (Forethought acquisition).
- Capabilities named: ground answers in unified knowledge (help center + external sources like Google Drive, PDFs); autonomously reason through complex workflows ("describe workflows in natural language and generate procedures dynamically… without rigid scripts"); orchestrate actions across any system; built-in QA ("evaluate every interaction with automated QA controls to audit outcomes, enforce policies"); close the loop with self-improving AI (identify gaps, detect failing procedures, refine knowledge/workflows from outcomes).
- Escalation: "AI agents are seamlessly connected to your human teams. When escalation is needed, they intelligently route issues to the right team at the right time — with full context to ensure a smooth handoff."
- Governance: "set policies, review behavior, and evaluate every interaction with built-in QA."
- Pricing model: per-resolution ("Resolution Allowance", tiered outcomes, "pay for value") — automated resolutions are the billed unit.
- FAQ claims (marketing-tier, keep out of final doc): 80 languages, "up to 80%" automation.
- **Limitation**: support.zendesk.com help center is sign-in-walled (root and article URL both redirect to sign-in). No Tier-1 operational detail (flow builder mechanics, handoff configuration screens) observed for Zendesk. Assertions about Zendesk kept at product-page strength.

## Product C — LivePerson (Conversational Cloud)

### Key observations (Layer A — directly observed)

- "How bots work in our Conversational Cloud": bots "can carry out a variety of automatic tasks and communicate with consumers to help take the load off of your agents"; bots positioned as replacements for IVR/websites/apps "with conversations".
- **Bots are handled just like human agents**: "bots are handled just like human agents. Bots can perform tasks that a human agent can, and both are measured with the same KPIs in the same agent workspace. This enables a conversation to be easily passed between a bot and a human agent."
- **"Human-bot tango"**: human agents can intervene or pick up conversations where needed; "Conversations can be passed back and forth between human and bot agents without a hitch."
- Building: LivePerson **Conversation Builder** — "interactive dialog builder" + library of industry-specific templates (retail, telco) "tuned for the top intents"; aimed at non-technical team members.
- Bot management: agents become **bot managers** who "manage and train the bots… tweaking conversations for better outcomes, bots are automatically made better too."
- **BYOB (bring your own bot)**: third-party bots integrated via connectors/APIs; "LivePerson offers a comprehensive set of management and reporting capabilities that you can use to manage both LivePerson native bots and third-party bots."
- Bot measurement: "A bot's performance is measured against your KPIs, are monitored in real-time by agent managers, and are included in centralized reporting."
- Voice bots exist as a separate surface ("Voice bots", "Transfer voicebot calls to contact center") — voice twin seam.
- Broader platform context: agent workspace, routing/skills, campaigns, proactive messaging, Conversation Orchestrator, Meaningful Conversation Score, Generative Insights, bring-your-own-LLM — the bot sits inside a full conversational operations platform.

## Product D — Chatwoot (Captain + AgentBot)

### Key observations (Layer A — directly observed)

- Open-source, self-hostable customer support suite ("An alternative to Intercom and Zendesk"); SMB-shaped shared inbox.
- **Captain Assistant**: "talks to your customers, learns from your help docs and past conversations, and gives quick, accurate responses. When enabled, the assistant would take the initial questions before transferring to an agent."
- Captain family: Copilot (agent-side drafting/translation — agent assist, not the customer bot), FAQs (spots common questions missing from the knowledge base — gap detection), Memories (conversation-derived memory), Custom Tools, audience/schedule control ("Control who Captain replies to and when"), AI credits (usage metering), self-hosted enablement.
- **AgentBot** (bring-your-own-bot at SMB scale): "connect external AI agents and custom bot logic directly to your Chatwoot inbox… your bot to listen to customer conversations, process incoming queries, and respond through Chatwoot in real time."
  - Mechanics: once connected to an inbox, new conversations get **pending** status; conversation events (widget_triggered, message_created, message_updated) are sent to the bot's webhook URL; the bot processes events, may call external system APIs ("order status or booking triggers") and AI models (OpenAI, Claude, Gemini, Amazon Lex), posts responses via Chatwoot APIs.
  - **Handoff**: "If the bot determines that a human agent's assistance is needed or if the customer explicitly asked for human help, it can use the conversation update API to change the status to 'open' which would make the conversation available to a human." Agents can **push back** a handed-off conversation into the bot queue (open → pending).
  - Bot identity: name + avatar + webhook URL; bots are account objects created in Settings → Bots and attached to inboxes (Bot Configuration).
- **Bot Reports** exist as a first-class report category (alongside conversations/agents/CSAT/SLA reports).
- Dialogflow integration guide ("bring your Dialogflow chatbot to Chatwoot") + Rasa demo — pre-LLM-era intent/dialog machinery still first-class.
- Channels: website live chat widget, WhatsApp, Facebook, Instagram, Telegram, SMS, email, API channel, voice calling (Twilio) — bot sits over the shared-inbox channel fabric.

## Cross-product Comparison

| Structure | Intercom Fin | Zendesk AI Agents | LivePerson | Chatwoot | Strength |
|---|---|---|---|---|---|
| Bot as business-authored, publishable asset | Fin (content+guidance+persona+audiences) | AI agents (knowledge grounding + natural-language procedures) | Conversation Builder dialogs + templates; BYOB | Captain Assistant config; AgentBot (name/avatar/webhook) | 4/4 — Core |
| Customer conversations as tracked unit in an operator surface | conversations in Inbox, viewable/monitorable | interactions under QA; tickets | conversations in agent workspace; bots measured with same KPIs | conversations in shared inbox; Bot Reports | 4/4 — Core |
| Bot↔human seam (handoff with context; push-back; no-human behavior) | automatic escalation guidance/rules; high-risk auto-handoff; no-agents-available behavior | "intelligently route… with full context… smooth handoff" | human-bot tango; pass back and forth; human intervention | pending→open toggle; agent push-back open→pending; explicit-ask trigger | 4/4 — Core |
| Knowledge grounding (help center/docs/past conversations) | Content library multi-source | help center + external sources | knowledge/intent-driven | help docs + past conversations | 4/4 — Common mature |
| Operator guidance/instructions layer | Guidance | policies | bot manager training | (Captain config; custom tools) | 4/4 — Common mature |
| Actions on business systems | Tasks/Procedures + data connectors | actions across systems | bot integrations/functions | external APIs via bot logic | 4/4 — Common mature |
| Multi-channel deployment | Messenger/WhatsApp/SMS/social/email/voice/Slack/Discord | messaging/email/voice/social | web/app/WhatsApp/Apple/SMS/voice | widget/WhatsApp/FB/IG/Telegram/SMS/email/API | 4/4 — Common mature |
| Pre-deploy testing | previews, batch tests, simulations | (QA built-in; not detailed) | (not observed) | (not observed) | 1/4 detailed — Common (thin evidence) |
| Performance analytics on automation | resolution/automation rate, CX score, topics, CSAT | automation rate; QA scoring | same KPIs as agents; real-time monitoring; centralized reporting | Bot Reports | 4/4 — Common mature |
| Content-gap improvement loop | Suggestions (AI content recommendations) | self-improving loop (refine knowledge/procedures) | bot manager training | Captain FAQs (gap detection) | 4/4 — Common mature |
| Usage metering of automated resolutions | resolution limits + notifications | per-resolution pricing | (billing not observed) | AI credits | 3/4 — Common mature |
| AI disclosure/transparency setting | AI Agent Disclosure | trust-center posture | trustworthy-GenAI article | (not observed) | 3/4 — Common (thin) |
| Audience/targeting controls | audiences (plan/location/brand) | (not observed) | target audience article | audience/schedule control | 3/4 — Common |
| Proactive/outbound conversations | Outbound Fin (behavioral triggers) | (not observed) | proactive messaging | campaigns (visitor messages) | 3/4 — Optional |
| Voice channel | Fin Voice | voice AI agents | voice bots | voice calling (channel only) | 4/4 present, 1/4 bot-voice deep — Optional/variant |
| BYOB / external-bot architecture | hand-over to another support tool (reverse direction) | "any platform" (Forethought) | BYOB native concept | AgentBot native concept | 3/4 — Variant |
| Agent-side AI (copilot) | (Copilot exists in Intercom, not observed here) | Copilot product | Conversation Copilot | Captain Copilot | 3/4 — Optional, adjacent |
| Sales/ecommerce roles | Fin for Sales/Ecommerce | (not observed) | (not observed) | (not observed) | 1/4 — Optional (drift zone) |
| Employee/internal audience | (not observed) | Employee Service product | (not observed) | (not observed) | 1/4 — Variant |
| Self-hosted deployment | no | no | no | yes | 1/4 — Variant |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The business-operated service bot** — an automated conversational agent that the organization authors, configures, and publishes as a standing asset: it carries the business's knowledge, instructions/policies, persona, and (in mature products) actions. The bot is an object the business owns and edits over time — not a one-off script, not a consumer toy. Remove → generic chatbot builder / demo bot / consumer assistant.
2. **The customer service conversation as the unit of work** — real conversations with the organization's customers (service seekers) on the organization's service channels, conducted primarily by the bot, held as recorded, observable sessions in an operator surface. The conversation — not a document, not a ticket, not an answer — is what the system produces and manages. Remove → FAQ page / knowledge-QA answer tool / static self-service.
3. **The managed bot↔human service seam** — the platform holds an explicit, governed boundary between automated and human service: conversations the bot cannot (or should not) resolve are handed to human agents or captured for human follow-up, with context carried across the seam; humans can intervene, take over, and push conversations back; the split between automated resolution and human service is measured. Remove → pure answer bot with no service operation behind it (KQA/self-service drift), or a scripted demo bot.

Jointly-held is load-bearing:
- 1 alone = chatbot builder / demo bot (no service operation)
- 2+3 without 1 = human live chat / customer support chat (Customer Support Chat Type)
- 1+2 without 3 = scripted bot with no path into human service (toy/answer bot)
- 1+3 without 2 = routing/orchestration shell with no customer conversations (not a realizable product shape — supports that leg 2 is load-bearing)

### L1 — Common Mature Structure (not definitional)

- knowledge grounding (help center, docs, PDFs, past conversations) + content management
- operator guidance/instruction layer (policies, tone, persona)
- multi-channel deployment (web widget, in-app SDK, WhatsApp/social/SMS/email; voice as extension)
- pre-deploy testing (previews, batch tests, simulations)
- conversation monitoring/debugging (answer inspection, live view)
- automation performance analytics (automation/resolution rate, CSAT/CX, topic analysis)
- content-gap improvement loop (suggestions, FAQ generation, bot training)
- usage metering of automated resolutions (limits, credits, per-resolution pricing)
- AI disclosure/transparency controls
- audience/targeting controls
- integrations with help desks/CRMs (hand-over both directions)

### L2 — Variant / Optional

- voice channel (voice bots / AI voice agents) — the IVR twin seam
- BYOB / external-bot architecture vs native bot (LivePerson BYOB, Chatwoot AgentBot, Zendesk "any platform")
- agent-side AI (copilot/agent assist) — adjacent capability often bundled
- proactive/outbound conversations (behavioral triggers, campaigns)
- sales/ecommerce roles (drift toward sales chat)
- internal/employee service audience (drift toward ESM)
- industry templates (retail, telco)
- deployment: SaaS vs self-hosted/open-source
- commercial model: per-resolution vs seats vs credits

### L3 — Vendor-specific (Research Notes only)

- Fin Guarantee, Fin Operator, Fin Vision, CX Score, Fin AI Engine™, Fin Identities, "45+ languages"
- Zendesk Resolution Learning Loop, Resolution Platform, Forethought acquisition, "80 languages", "up to 80%" claims, Resolution Allowance tiers
- LivePerson "human-bot tango" branding, Meaningful Conversation Score, Conversation Orchestrator, Generative Insights, bring-your-own-LLM, aiStudio/Gemini migration
- Chatwoot Captain Memories, AI credits mechanics, robots.txt crawling for the assistant, specific webhook event names

## Rejected Findings (anti-overfitting)

- **"AI/LLM" as definitional** — rejected. Pre-LLM dialog-tree/FAQ bots (LivePerson Conversation Builder dialogs; Chatwoot+Dialogflow/Rasa) satisfy the core. The LLM era changed the authoring surface (write guidance instead of drawing trees) and answer machinery, not the Type's structure.
- **"Handoff to live agents" as the literal invariant** — too narrow. The invariant is the managed automated/human boundary; live-agent handoff is the dominant implementation, async capture/ticket creation is another. Phrased abstractly in L0 leg 3.
- **"Website chat widget" as definitional** — rejected. Channels span messaging apps, email, social, voice; the widget is one implementation.
- **"Automation rate / resolution-based pricing" as definitional** — rejected; commercial-model variant (L2), though per-resolution billing is a strong current-market signal.
- **"Multi-intent agentic reasoning" as definitional** — rejected; era-current capability (Zendesk marketing), not required by the core.
- **"Suite membership" (inbox + knowledge + reports in one product)** — rejected as definitional; standalone bot layers over third-party desks exist (Fin for platforms; Chatwoot AgentBot over any inbox). The platform's own operator surface is what matters.

## Boundary Findings

- **vs Customer Support Chat** — closest sibling. Chat = human agents conduct real-time conversations; chatbot platform = automation conducts conversations first, humans enter through the seam. Remove the automated participant → Customer Support Chat. (Help-desk pass already fixed: chat conversations become tickets in the desk.)
- **vs Help Desk / Ticketing System** — record-centric (tickets, queues, SLAs, lifecycle) vs conversation-centric automation. Bots hand off INTO desks; desks may embed bots as a channel feature. Remove the automation-first conversation loop → help desk.
- **vs Contact Center Platform** — live-interaction distribution machinery to human agents across media vs the automated self-service layer. Contact centers embed bots (LivePerson spans both — bot-as-agent-worker is the bridge shape). Remove automation, keep live distribution → contact center.
- **vs IVR Platform** — voice twin (IVR pass: "remove the voice medium → chatbot/web form"). Text/digital conversational automation here; designed voice flows + DTMF/speech there. Voice bots sit on the seam (Fin Voice, LP voice bots, Zendesk voice agents).
- **vs Knowledge Question Answering Application** — KQA's deliverable is the grounded answer; this Type's business is the conversation (session lifecycle, handoff seam, service metrics). KQA's "actions beyond answering" pole drifts here (KQA pass already flagged).
- **vs Self-service Support Portal** — async content + requests + own-request view vs live automated conversation. Bots may live inside portals as a variant (self-service pass already noted).
- **vs Agent Development Platform / LLM Application Development Platform** — developer-facing general agent building vs service-operation-facing bot operation (bot is a service worker measured in service KPIs, deployed on service channels, with a human seam). Chatwoot AgentBot's webhook contract shows the boundary: the platform hosts/operates the bot in a service operation; the agent platform builds the brain.
- **vs Customer-to-Business Messaging Application** — C2B messaging is the channel/relationship substrate (business↔customer messaging over WhatsApp/Messenger); the chatbot platform automates the business side of such conversations. Channel substrate vs automation layer.
- **vs Digital Concierge (hospitality)** — per the digital-concierge pass cross-reference: hospitality guest-messaging/chatbot products with **stay anchoring** and **physical-service fulfillment semantics** belong to Digital Concierge; this Type covers the generic service-chatbot machinery without stay anchoring. Adopted here as the discriminator.
- **"Remove what to become another Type" summary**: remove the bot (automation) → Customer Support Chat; remove the conversation-as-unit (keep corpus+answer) → Knowledge QA; remove the seam (keep bot+conversations) → demo/answer bot; remove text medium → IVR/voice-bot territory; remove service anchoring (keep conversation automation) → general agent/chatbot builder.

## Historical / Market-Sample Check

- Pre-LLM anchor: dialog-tree bot builders (LivePerson Conversation Builder — interactive dialog builder, still documented; Chatwoot's Dialogflow/Rasa integrations — intent machinery) + FAQ bots in live-chat widgets with "connect me to an agent" fallback. All satisfy the three L0 legs without LLM/RAG/AI analytics. ✓
- Thinner ancestor: live-chat auto-responder (single canned reply) — fails leg 1 (no authored conversational asset beyond one message) and leg 3; correctly excluded as too thin.
- Platform-native/regional: WhatsApp Business API bots, WeChat service accounts with automated replies — same core over different channel substrates. ✓
- Voice-era: IVR trees are the voice twin, not this Type (medium differs); voice bots are the modern seam. ✓
- The check passes: the definition does not depend on LLMs, RAG, agentic reasoning, per-resolution pricing, or any specific channel.

## Uncertainties

- Zendesk Tier-1 operational detail unobserved (sign-in wall): flow-builder mechanics, handoff configuration, bot-versioning behavior for Zendesk are inferred only from the product page — kept at Tier-2 strength.
- Ada / Tidio / Freshchat unreachable: the standalone SMB pure-play pole (bot-only product, no inbox) is under-evidenced directly. Chatwoot (SMB suite) partially covers the tier. Assertion "standalone bot-only platforms exist as a variant" is held at moderate confidence.
- Pre-deploy testing observed in depth only at Intercom; held as common-mature with thin evidence (Zendesk QA implies evaluation; LivePerson bot-manager training implies iteration).
- Exact default behaviors (default escalation thresholds, default disclosure on/off, default no-human behavior) not researched — no precise defaults asserted anywhere.
- Whether the no-human-available behavior (defer/capture) is universal or Intercom-emphasized: observed explicitly at Intercom; implied elsewhere; held as common-mature, not core.

## Final Synthesis

A Customer Service Chatbot Platform is the business-side system for operating automated conversational agents on the business's customer service channels. Its world has three jointly-held structures: (1) the service bot as a business-authored, publishable automation asset; (2) the customer service conversation as the tracked unit of work; (3) the managed seam between automated and human service (handoff with context, intervention, push-back, measured split). The operator's loop is configure → test → deploy → converse → hand off → analyze → improve. The Type is distinct from human live chat (no automation), help desks (record-centric), contact centers (live distribution), IVR (voice medium), KQA (answer deliverable), and agent development platforms (dev-side brain-building). The LLM era changed the authoring surface and answer machinery, not the structure; pre-LLM dialog-tree bots satisfy the same core.
