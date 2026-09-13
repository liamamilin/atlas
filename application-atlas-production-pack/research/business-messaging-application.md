# Research Notes — Business Messaging Application

## Research Goal

Understand what a "Business Messaging Application" is as an Application Type: the world model of messaging software where an **organization** is a conversation participant, how conversations enter and flow, how the organization side handles them at scale, and where the boundary lies with Instant Messaging, Team Messaging, Customer-to-Business Messaging, Customer Support Chat / Help Desk, and SMS Marketing.

## Initial Boundary

- Directory position: 01.01 Messaging & Chat, sibling of Instant Messaging, Group Messaging, Chat Room, Team Messaging, Community Chat, Customer-to-Business Messaging.
- The processed gold-standard sibling (`instant-messaging-application.md`) already commits to a distinction: Business Messaging = "identity is organizational; conversation is customer ↔ business; flows are CRM / support-shaped"; C2B Messaging = "customer-initiated contact with a business, often through a public profile or short code". This research must validate or refine that split, not silently rewrite it.
- Initial hypothesis: messaging applications in which one party is an organization acting in a business capacity — an identified business participant with org-held conversation records and (usually) multiple people/agents acting for the org — conversing with external individuals (customers, prospects, visitors).
- Risk flagged from the start: "Business Messaging" could be misread as internal business communication (= Team Messaging, already a separate leaf) or as business SMS bulk texting (= SMS Marketing Platform, separate leaf). Neither is the intended reading of this node in the Messaging & Chat family.

## Research Questions

1. What is the unit of the world — conversation? contact? inbox? channel?
2. What is identity here: who is the org-side participant, who is the external participant, and what substrate carries each (phone number, account, friend relationship, email, anonymous visitor)?
3. How do conversations enter (entry points) and how does a thread relate to the organization's other records (contact, order, ticket)?
4. How does the org side handle conversations at scale: shared inbox, assignment, states, automation, templates?
5. What can the org legitimately send (reply-only vs free push vs template-gated), and which rules constrain outbound messaging?
6. Where does this Type end and Help Desk / Customer Service Platform / Chatbot Platform / SMS Marketing begin?

## Representative Products

Chosen for market coverage + documentation depth + different product philosophies + different customer tiers:

| Product | Philosophy | Customer tier | Direct docs fetched? |
|---|---|---|---|
| LINE Messaging API / LINE Official Account | regional messaging network with official-account model | SMB → enterprise (API) | Yes (developers.line.biz) |
| Intercom (Messenger + Inbox + Channels) | in-product web/app messenger, customer-service-flavored platform | mid-market/enterprise SaaS | Yes (intercom.com/help) |
| Twilio Conversations | API/composable infrastructure for cross-channel conversation | developer/enterprise | Yes (twilio.com/docs) |
| Shopify Inbox | SMB storefront chat tied to commerce | SMB | App-listing page only (help center 403) |
| WhatsApp Business | consumer messenger extended for business | SMB app / enterprise platform | **No** (3 hosts failed; documented indirectly via Intercom's official WhatsApp-channel docs) |

## Sources

Fetched 2026-09-06:

- LINE Developers — Messaging API overview — https://developers.line.biz/en/docs/messaging-api/overview/ (Tier 1)
- Intercom Help — Home — https://www.intercom.com/help/en/ (Tier 1 index)
- Intercom Help — Channels collection — https://www.intercom.com/help/en/collections/10723236-channels (Tier 1)
- Intercom Help — Messenger explained — https://www.intercom.com/help/en/articles/6612588-messenger-explained (Tier 1)
- Intercom Help — The Inbox explained — https://www.intercom.com/help/en/articles/6258745-the-inbox-explained (Tier 1)
- Intercom Help — Using WhatsApp as a channel — https://www.intercom.com/help/en/articles/9881312-using-whatsapp-as-a-channel (Tier 1; official third-party documentation of WhatsApp business-channel behavior)
- Twilio Docs — Conversations — https://www.twilio.com/docs/conversations (Tier 1)
- Shopify App Store — Shopify Inbox listing — https://www.shopify.com/inbox (Tier 2 product listing)

Source-access limitations:

- WhatsApp Business vendor surfaces unreachable: `business.whatsapp.com` transport error, `faq.whatsapp.com` timeout, `www.whatsapp.com/business` timeout (3 distinct hosts). Per network rules, abandoned. WhatsApp channel facts below are only those documented by Intercom's official channel docs; WhatsApp SMB-app specifics (labels, catalogs, quick replies) were **not** verified this session and are deliberately excluded from precise claims.
- Freshworks/Freshchat unreachable (support.freshchat.com 404, freshworks.com timeout, help.freshchat.com transport error) — dropped as a sample.
- Shopify Help Center blocked (403); Shopify evidence is app-listing level.
- Zendesk messaging article URL guess returned 404; not pursued further.

## Product A — LINE Messaging API / LINE Official Account

Evidence layer: A (directly observed, official developer docs).

Key observations:

- The org-side participant is a **LINE Official Account** — an organizational account. Users (individuals) must **add the account as a friend**; the friend relationship gates the conversation.
- Flow: user sends a message to the Official Account → LINE Platform delivers a webhook event to the bot server → the bot server responds through the platform. The "agent" is whatever the org runs behind the API.
- Two outbound modes documented: **reply messages** (responding within the exchange) and **push messages** ("send messages directly to users at all times"), plus multicast/broadcast for lists.
- Rich message types including structured/template messages (text, sticker, image, video, audio, location, coupon, imagemap, template, Flex).
- A **rich menu** can be attached to the chat permanently; **LINE Beacon** can trigger interaction when a user enters a physical region; **account linking** ties the LINE user to the org's own user accounts.
- Profile retrieval of the user (display name, language, image, status message).
- Sending quotas are plan-metered; free monthly message count depends on the Official Account subscription plan.

Type-relevant reading: official-account model = org identity + friend-gated reachability + conversation thread + org-side automation. Outbound push to friends is free-form "at any time" (contrast with WhatsApp).

## Product B — Intercom (Messenger + Inbox + Channels)

Evidence layer: A (directly observed, official help center).

Customer side (Messenger):

- A messenger **embedded in the business's website or mobile app** (JavaScript install / iOS & Android SDKs), fully customizable (branding, welcome messages), mobile customization carried over.
- Messenger spaces: Home, Messages (inbound + outbound conversations), Tickets, Help (in-org help center), News (announcements feed), Tasks (checklists) — the messenger is a small app surface, conversation being the core space.
- Queue position display, expected reply times ("Show reply times during office hours"), file/image sharing, voice transcription.
- Channel switching: offer to continue the conversation in WhatsApp via QR code.

Org side (Inbox):

- The Inbox is "the workspace where your team manages and responds to customer conversations" — brings together all inboxes/conversations/customer context in one place.
- **Unassigned** queue; assign to teammate or team; conversation states **open / closed / snoozed** (snooze returns conversation at a due time); table layout with configurable conversation-data columns; custom filtered views in real time; search by keyword, tag, user, assignee, date range.
- Contact model: **user** (logged in to the product) vs **lead** (unidentified/anonymous visitor); duplicate detection matched on phone / WhatsApp number / email; merge with preview.
- Customer context sidebar: recent conversations, similar conversations, notes; custom conversation attributes; inbox apps.
- Workflows (rules-based automation), macros (canned responses), AI translations, AI summaries, Copilot, Fin AI agent.
- Mobile apps for teammates to reply on the go.

Channels: Messenger, Email, Phone, WhatsApp, SMS, Facebook, Instagram, Telegram, Discord, Slack — "Enabling the channels you use to communicate with customers, all from the Inbox."

WhatsApp-channel facts documented by Intercom (official third-party documentation of the WhatsApp business channel):

- Connection requires a **WhatsApp business number**; inbound + outbound both supported.
- **24-hour customer care window**: if the customer's last message is more than 24 hours old, the business can no longer reply with free text — only with pre-approved **message templates**; a customer reply re-opens the 24h window.
- Starting a new WhatsApp conversation from the inbox requires a pre-approved template.
- WhatsApp conversation exists as a **single thread**; the vendor lets the org define when a closed thread counts as a "new conversation".
- Inbound: text, images, attachments, gifs/videos, audio & voice notes, locations. Voice messages auto-transcribed to text for the team.
- New inbound WhatsApp contact creates a **lead** with WhatsApp profile name + number; optional merge by phone number.
- Bulk/triggered outbound WhatsApp messages available from Outbound (separately billed).

## Product C — Twilio Conversations

Evidence layer: A (directly observed, official docs).

- "Platform services, available as APIs or through a self-hosted SDK, for coordinating interactions across channels **while maintaining conversation history** and intelligence."
- Channels listed: Voice, SMS, WhatsApp, RCS, Chat.
- Two conversational patterns: **human agent augmentation** (real-time intelligence for human agents during live interactions) and **conversational AI agents** (agents that maintain context across channels, remember customer history, ground responses in business knowledge); plus **AI-to-human handoff** blueprints.
- Components: Conversation Intelligence (analyze signals, trigger actions), Conversation Relay (voice), Conversation Orchestrator ("track conversation state across channels and participants"), Conversation Memory ("persistent customer knowledge"), Enterprise Knowledge (ground responses in org policies/product info).
- Requires an existing channel implementation in production; conversation state and history are platform primitives the business composes its own agent surfaces on.

Type-relevant reading: the API-philosophy extreme — the Type's objects (conversation, participant, channel, history, state) exposed as primitives; org composes inbox/agent tooling itself. Confirms that conversation-as-managed-record-with-history is the center of gravity even when no GUI inbox exists.

## Product D — Shopify Inbox

Evidence layer: A- (Tier 2 official app listing; help center blocked).

- Storefront chat: "an AI-powered sales associate on your storefront. Buyers can ask questions and get help finding the right products from your catalog."
- Runs with or without the AI agent; agent grounded in the store's **catalog, policies, and order data**; merchant controls tone/style/rules; chats can be rated to train the agent.
- Feature set from the listing: real-time messaging, live chat, email-chat continuation, file upload, push notifications, customer insights; automated responses (discounts, FAQs, greetings, product recommendations, quick replies, order updates); customization (color/font, chat window, **business hours**, welcome messages, chat buttons, **chat assignment**, agent avatar); analytics (orders assisted, buyer satisfaction).
- Customer identification options (from vendor replies in the listing): require sign-in, require name+email, or **allow anonymous chats** — the identified-vs-anonymous customer is an explicit merchant decision.
- Deeply commerce-tied: messaging connects to products, inventory, orders.

## Product E — WhatsApp Business (indirect)

Evidence layer: A for channel behavior via Intercom's official docs (24h window, templates, business number, single-thread semantics, media types); positioning-level only for the rest. Direct vendor docs unreachable this session.

Type-relevant reading: a consumer messaging network exposing an organizational participation mode (business number, pre-approved templates, response-window policy enforced by the network). The org's outbound freedom is **constrained by the network's policy**, in contrast to LINE's free push. SMB-app specifics unverified — excluded from precise claims.

## Cross-product Comparison

| Aspect | LINE Official Account | Intercom | Twilio Conversations | Shopify Inbox | WhatsApp Business (via Intercom docs) |
|---|---|---|---|---|---|
| Org-side identity | Official Account | Workspace w/ business profile + agents | Org's own composed system (app/business) | Store/business | WhatsApp business number |
| External participant | LINE user (friend) | contact: user or lead/anonymous visitor | customer on any channel | shopper (sign-in / name+email / anonymous) | WhatsApp user (phone-based) |
| Entry point | friend-add / QR | website/app widget, WhatsApp, SMS, email, social DMs, phone | any channel the org wires | storefront chat widget | messaging network |
| Thread w/ persistent history | Yes | Yes (conversations; snooze/close states) | Yes ("maintaining conversation history") | Yes (chat thread; email continuation when offline) | Yes (single-thread semantics) |
| Org-side work handling | bot server + Official Account Manager | team Inbox: unassigned queue, assignment, open/snoozed/closed, views, search | conversation state + agent augmentation primitives | chat assignment, assignment + analytics | thread handling in org's tooling |
| Templates / canned responses | template & Flex messages | macros | org-defined | quick replies, FAQs, greetings | pre-approved templates (network-enforced) |
| Automation / AI | bots (API) | Workflows, Fin AI agent | conversational AI agents + handoff | AI sales agent grounded in catalog | via org's platform tools |
| Outbound policy | push at any time to friends | workflow/outbound rules | org-defined | order updates, recommendations | free text only within 24h window; templates otherwise |
| Commerce extensions | coupon messages | — (CRM-context) | — | catalog grounding, discounts, order analytics | — |
| Customer identity substrate | LINE account | email/ID or anonymous | channel address | Shop sign-in / email / anonymous | phone number |
| Plan-metered messaging | Yes (monthly quotas) | usage-based channels | usage-based | free app | per-conversation/network pricing |

### Abstraction result

Layer 0 — Defining Invariant (all five samples, all eras, all regional variants):

1. **Organizational identity as a conversation participant** — the conversation is attributed to an identified business/organization, not a private individual.
2. **Conversation thread with an external individual** (customer, prospect, or visitor) in chat form.
3. **Message exchange between the two sides** — genuinely two-way conversational messaging (not one-way broadcast).
4. **Organization-held persistent conversation history** — the thread and its history belong to the organization as a record, not to an individual's personal archive.

Layer 1 — Common mature structure (very common across samples, not definitional):

- Entry points: embedded website/app widget, messaging-network account (friend-add/QR/short code), business phone number, email, social DMs.
- Org-side inbox with shared handling: unassigned queue, assignment to agents/teams, conversation states (open / snoozed / closed), views and search.
- Customer context: contact record with attributes and past conversations visible to the agent.
- Templates / canned responses / quick replies.
- Automated greeting / away / expected-reply-time messaging; business hours.
- Tags/labels and internal notes on conversations and contacts.
- Media attachments (images, files, audio/voice notes, location).
- Automation and AI: rules, bots, AI agents grounded in business content, AI-to-human handoff.
- Reporting: volume, response performance, satisfaction.
- Multi-agent operation with roles/permissions on the org side.
- Channel consolidation: multiple external channels funneled into one inbox.

Layer 2 — Variant / optional structure (depends on segment, geography, business model):

- Outbound/bulk messaging to lists (broadcast, order updates, promotions) — network policies vary from free-form push (LINE) to template-gated (WhatsApp).
- Commerce extensions: product catalog in chat, discounts, order-status updates, payments-adjacent flows.
- Official-account model with friend-gating and plan-metered quotas (regional pattern).
- Anonymous vs identified customer policies (sign-in / email / anonymous chat).
- Delivery form: standalone SaaS inbox, in-product messenger SDK, composable API infrastructure, native app inside a consumer messaging network.
- Verification / approval regimes for org identity and message content.

Layer 3 — Vendor-specific (kept out of the final document):

- Intercom: Fin, Messenger "Spaces" (Home/Tickets/News/Tasks), Workflows, user-vs-lead contact model details, Command-K, table layout specifics.
- LINE: rich menus, LINE Beacon, coupon/imagemap message types, friend-add gate, plan quotas.
- WhatsApp: 24-hour customer care window, pre-approved template management (WhatsApp Manager), per-conversation pricing.
- Twilio: Conversation Relay / Orchestrator / Memory / Enterprise Knowledge component names, Agent Connect framework.
- Shopify: Shop sign-in personalization, catalog-grounded agent voice controls, orders-assisted analytics.

## Historical / Market-Sample Check

Would older, regional, platform-native or differently positioned products still fit the Layer 0?

- 2000s website live chat (operator console + visitor chat window): org identity (the company console), thread with a visitor, org-held history → fits, without team tooling, AI, or templates.
- Two-way business SMS on a short code: org identity (shortcode/number), thread with an individual, org-held history → fits; chat-form short messages.
- Regional official accounts (WeChat 公众号-style, LINE, KakaoTalk channels): org identity + friend-gated conversation → fits.
- Email-based customer conversations: envelope/letter model and mailbox-centric storage — better classified under Email-side Types; excluded by the chat-thread form in Layer 0.

The Layer 0 deliberately avoids: multi-agent teams, AI, templates, business hours, websites/apps as substrate, any specific identity substrate (phone vs account vs anonymous visitor). The WhatsApp phone-number identity is a common implementation, not the invariant (Intercom supports anonymous leads; Shopify supports anonymous chats).

## Vendor-specific Findings

See Layer 3 above. Notable for the boundary discussion: Intercom positions itself as "customer service" (its help center's tagline and Fin AI Agent collection are service-first) — evidence that the market overlaps this Type with Customer Service Platforms, while the conversation medium remains the defining surface.

## Boundary Findings

- **vs Instant Messaging Application**: identity is private-personal vs organizational; the conversation graph is the personal contact graph vs the org's customer relationships; history is a personal archive vs an organizational record. Remove the organizational participant and org-held records → it becomes IM.
- **vs Team Messaging Application**: audience is external customers/visitors vs internal employees; remove the external individual → it becomes Team Messaging.
- **vs Community Chat Platform**: 1:1 org↔individual threads vs many-to-many community spaces with discovery and moderation.
- **vs Customer-to-Business Messaging Application (sibling leaf)**: same underlying object model (org participant + thread + external individual). The researched distinction: C2B emphasizes the **customer-initiated entry** through a public entry point (official account, business profile, short code, QR), while Business Messaging covers the **organization-operated messaging application** as a whole — including org-initiated outbound within a relationship. These read as two sides of one conversation model rather than two disjoint Types; flag for joint review.
- **vs Customer Support Chat / Help Desk / Customer Service Platform**: those Types center on support intent and/or the ticket as the managed unit; Business Messaging centers on the conversation medium itself, agnostic to intent (sales, support, operations). Overlap is heavy: Intercom's marketing is support-first; Shopify's is sales-first — same Type, different intents. When conversations are fundamentally tickets → Help Desk.
- **vs Customer Service Chatbot Platform**: bot-first automation vs organization-staffed conversation (bots as an optional depth layer here).
- **vs SMS Marketing Platform**: broadcast/list-first campaign sending vs conversation-first exchange; bulk outbound exists inside Business Messaging (Layer 2) but campaign/list management is not the core.
- **vs Email Communication Types**: chat-thread short-message form vs envelope/letter form; email can appear as a channel into a business-messaging inbox (Intercom) without changing the Type.

## Uncertainties

- WhatsApp Business direct documentation unreachable; SMB-app behaviors (labels, catalogs, quick replies, business profile details) unverified this session — no precise claims made.
- Shopify evidence limited to the official app listing (help center 403); deep workflow details (assignment mechanics, state names) not verified.
- Regional official-account products beyond LINE (WeChat Work, KakaoTalk, Viber) not directly sampled; the official-account pattern rests on the LINE sample plus the LINE-documented friend-gating model.
- The directory's intended distinction between Business Messaging Application and Customer-to-Business Messaging Application is not settled by market evidence; recorded as a boundary issue rather than resolved unilaterally.

## Final Synthesis

A Business Messaging Application is messaging software in which an **organization is a conversation participant**: conversations between an identified business and external individuals are held as chat threads whose history belongs to the organization, and the organization side is equipped to receive, handle, and answer those conversations as work — commonly with a shared inbox, agent assignment, templates, automation, and multiple connected channels. Everything else (entry-point shape, identity substrate, AI, commerce, broadcast reach, plan models) is implementation or variant, not definition.
