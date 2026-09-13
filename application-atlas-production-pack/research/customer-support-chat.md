# Research Notes — Customer Support Chat

## Research Goal

Understand what a Customer Support Chat (website live chat) Application really is as an Application Type: what exists inside it, who operates it, how the work flows, and where its boundaries sit in the dense §07 neighborhood (Help Desk, Ticketing System, Customer Service Platform, Customer Service Chatbot Platform, Omnichannel Customer Service Platform, Contact Center, C2B Messaging, Business Messaging) and against adjacent Types documented by earlier passes (Chat Room, Remote Customer Support, Digital Concierge).

## Initial Boundary

Working hypothesis before research:

- Core use: a business publishes a chat entry point (widget/button/page/SDK) on its own website or app; visitors and customers start real-time text conversations with the business's human support agents; agents conduct those conversations from a shared operator console.
- Nearest neighbors suspected: Customer Service Chatbot Platform (automation conducts vs humans conduct), Help Desk / Ticketing (record-centric), Customer Service Platform (whole-function suite), Omnichannel Customer Service Platform (channel-unification-first), Contact Center (live-interaction distribution machinery), C2B / Business Messaging (third-party messaging networks, intent-agnostic), Chat Room Application (shared room vs 1:1 agent chat), Remote Customer Support Platform (device control), Digital Concierge (stay anchoring).
- Prior passes already fixed seams this pass must honor:
  - Chatbot-platform pass: "Chat = human agents conduct real-time conversations; chatbot platform = automation conducts conversations first, humans enter through the seam. Remove the automated participant → Customer Support Chat." Advance flag: LivePerson-class products span bot+agent operations — check whether automation-first vs human-first holds as the keep-both discriminator.
  - Help-desk pass: "chat tools own one real-time channel; the desk owns the tracked record… Chat conversations *become* tickets in the desk."
  - Chat-room pass: "Visitor-to-agent 1:1 conversations are Customer Support Chat. The widget is a delivery form, not a different Type."
  - Remote-customer-support pass: "conversation-first; no device visibility or control. Remove device control → chat."
  - C2B-messaging pass: "vs Customer Support Chat (intent-agnostic vs support-scoped)."
  - Digital-concierge pass: "generic support lacks stay anchoring and physical-service fulfillment semantics."
  - Contact-center pass: "Customer Support Chat: a single digital medium; contact center is the multi-channel distribution platform over which chat may be one intake surface."
- Unknowns: is "real-time" definitional given the market's async-messaging drift? Is the website widget definitional or just the dominant implementation? Where exactly does the Type end against the omnichannel sibling (still unprocessed)?

## Research Questions

1. What is the visitor-facing surface, and how does the team's availability control it?
2. What is the central object (chat session / conversation) and what does it hold?
3. How do incoming conversations get distributed to agents (queue, automatic assignment, manual pickup, skills)?
4. What does the agent console look like: concurrent conversations, visitor context, internal collaboration?
5. What happens when the team is offline (offline form, async messaging, unassigned chats)?
6. What surrounds the conversation: pre-chat forms, proactive triggers, transcripts, ratings, reports?
7. Where does the Type end vs Help Desk (ticket), Chatbot Platform (automation), Omnichannel CSP (channel unification), C2B Messaging (messaging networks), Contact Center (distribution machinery)?

## Representative Products

Chosen for market coverage, documentation depth, different product philosophies, different customer tiers:

| Product | Philosophy | Customer tier | Direct docs fetched? |
|---|---|---|---|
| LiveChat | archetypal premium live-chat pure-play (Text, Inc.) | mid-market / enterprise | Yes — help center index + Chats section + Chat assignment articles (layer A) |
| Tawk.to | free-forever live chat, SMB | SMB / free | Yes — product page (Tier 2) + help center index (layer A/B) |
| Lime Connect (formerly Userlike) | EU/privacy posture, unified messaging over own widget + channels | mid-market | Yes — Message Center guide (layer A) |
| Crisp | all-in-one SMB shared inbox around a chatbox | SMB | Yes — knowledge base index + Inbox category (layer A/B) |
| LivePerson | enterprise conversational cloud; spans bot + agent operations | enterprise | Yes — Agent Workspace for live chat + Automatic Conversation Distribution (layer A) |

Rejected/abandoned samples: Olark (help.olark.com transport error ×2 — abandoned per network rule), Comm100 (documentationcenter 404), Zendesk Chat (help center sign-in-walled per earlier passes).

## Sources

Research date: **2026-09-08**

- LiveChat — https://www.livechat.com/help/ , https://www.livechat.com/help/use-livechat/ , https://www.livechat.com/help/how-to-chat-section/ , https://www.livechat.com/help/chat-assignment/
- Tawk.to — https://www.tawk.to/ , https://help.tawk.to/
- Lime Connect (formerly Userlike) — https://docs.userlike.com/ , https://docs.userlike.com/features/message-center
- Crisp — https://help.crisp.chat/ , https://help.crisp.chat/en/category/inbox-15ctwet/
- LivePerson — https://knowledge.liveperson.com/ , https://community.liveperson.com/kb/articles/1135-agent-workspace-for-live-chat , https://community.liveperson.com/kb/articles/1156-automatic-conversation-distribution

Access limitations: Olark unreachable (transport error ×2, abandoned); Comm100 docs 404; Tawk.to category pages intermittently errored (product page + help index used instead); LivePerson article pages are nav-heavy (article bodies recovered from saved fetches). No precise numeric limits are asserted in the final document beyond what sampled vendors document.

## Product A — LiveChat (evidence layer A)

- Positioning: "AI live chat software for business… connect with customers, provide real-time support" (footer positioning; product family: LiveChat + ChatBot.com + HelpDesk.com + KnowledgeBase — the live chat product is one layer of a suite).
- Install: code snippet or platform integrations (Shopify, WordPress, Wix, …) put the widget on the site.
- Chats section (agent app): "where the communication between agents and customers happens". Chat list divided into **my chats** (ongoing), **queued chats** (waiting for an available agent), **supervised chats** (handled by other agents, supervisable), **unassigned chats** (messages submitted while the team is offline, or when widget availability is set to "always" — an asynchronous mode; replies go to the visitor's email and the chat window).
- Chat statuses: **active** (recent message either side) vs **inactive** (customer hasn't responded for a configurable time; greyed out; don't count toward the concurrent-chats limit).
- Chat feed: history (current + previous conversations "providing the person hasn't cleared cookies"), text area with typing indicator shown to visitors, **message sneak-peek** (agent sees what the visitor types before sending), canned responses recalled with `#` shortcuts, emoji + emoji reactions, file sharing, tags.
- Transfer: to another agent or group; optional **private note** visible to agents only. Supervision: a supervisor can watch and whisper invisibly to the customer.
- End chat: "Close and archive" — chats move to Archives (filter, sort, tag past conversations); transcripts obtainable.
- Tickets: native ticketing existed but was **sunsetted** (schedule documented per plan); LiveChat now points to HelpDesk.com (sibling ticketing product) — direct market evidence that the chat tool and the ticket record are separable layers.
- Ban customers (spam/abuse) for a chosen number of days; unbannable.
- Assignment: **automatic** (each new chat goes to the first available agent with "Accept chats" status; rounds continue until all agents hit their concurrent-chat limit; returning customers go to the agent who served them before; auto-transfer if the assignee doesn't respond within a timeout) or **manual selection** (chats queue; all accepting agents get notified; first to pick up wins). Group-scoped; URL rules and routing rules route chats to selected groups/teams.
- Settings: widget customization, widget visibility, chat button, eye-catcher, campaigns (targeted pop-ups), chat forms / customer data collection surveys, queue configuration, inactivity timeouts, working hours (work scheduler), groups, agent accounts, roles (owner/administrator/agent), multiple websites.
- Reports: chat volume, missed chats, agent rankings, team management; Sales Tracker (value of chats); goals.
- Customers: customer details panel; outbound messages; Traffic/Engage section (site visitors).

## Product B — Tawk.to (evidence layer A/B)

- Positioning: "Free Live Chat Software for Your Website"; "100% Free"; one JavaScript snippet, "live in minutes", no developer needed.
- Product surfaces: Live Chat, Omnichannel Inbox, Chat Pages (hosted landing pages that "turn links into conversations"), Knowledge Base, CRM, Pipeline, Activities (bookings), Feedback (ideas portal), Automation (AI answers), Add-ons (white label etc.).
- Dashboard ("customer command center"): shared inbox across channels (web widget, Messenger, Twilio SMS, WhatsApp, Telegram, Gmail/Outlook email, forms, voice), contacts/CRM auto-built from conversations, ticketing ("when an enquiry is a problem, not a sale, it becomes a ticket on the same contact"), knowledge base, AI Assist add-on (AI answers routine questions; "when a conversation actually needs a person, a person takes it, with full history and full context").
- Help center categories: Getting Started (create account, add widget, invite colleagues to a shared property), Chat Widget Customization (brand, scheduler, widget content/behavior), Dashboard 101, Ticketing, Knowledge Base, Contacts, Advanced features (triggers, departments, white label), Add-ons, channel connectors (Messenger/SMS/WhatsApp/Telegram/Email), shopping-cart integrations.
- Agent-side imagery: shared inbox with per-channel badges, typing indicator, whisper/smart-reply affordances, agent online count, response-time and satisfaction stats.

## Product C — Lime Connect, formerly Userlike (evidence layer A)

- Rebrand note: "Userlike is now Lime Connect" (Lime Technologies); docs domain unchanged. Product lineage: Userlike live chat → unified-messaging platform.
- Message Center: "where all your customer messaging comes together… your collection of conversations with your contacts – ongoing or ended."
- Inbox: conversations assigned to you (**Mine**) vs **Unassigned**; "A conversation can only be answered by the operator it's assigned to."
- Conversation statuses: **NEW** (started while all operators unavailable), **OPEN** (requires operator reply), **PENDING** (operator last replied, awaiting contact), **ENDED** (manually ended, or auto-ended after contact inactivity — vendor documents 30 days), plus a **LIVE** label: "A conversation will be marked live if there is activity and contact and operator are online and operator has a slot free… The live label suggests a higher priority."
- Live vs async is explicit: "A conversation is live, or synchronous, when both you and the contact are online at the same time. Because in this situation there is a time pressure on answering, you can set a maximum capacity [chat slots] in your profile… If you have reached your maximum capacity, the conversation switches into asynchronous mode. The contact can still send messages, but it is clear to her that the answer will come later. There is no limit on the number of asynchronous conversations."
- Online/Away switch: "Online: live conversations are automatically routed to you. Away: you can only engage in asynchronous messaging."
- Routing: "When one or more operators are available: new incoming conversations are automatically routed to the available operators. When no operators are available: newly started conversations appear under unassigned" (assignable via "Assign to me").
- Operator Infos: which colleagues are online and how busy.
- Conversation input: text, notes (message/note switch), chat macros (shortcut-triggered text blocks, locale variants), chat commands (`$assign`, `$forward`, `$topic`, `$status`, `$rating`, `$block`, `$send` transcript…), file uploads, audio/video calls (contact must be online in the Website Messenger and grant permission; unanswered calls expire — vendor documents 180 s), voice messages, Live Translation.
- Action bar: subject, assign/unassign operator or group, status, topic, add-ons, send transcript, end conversation.
- Contact details: name/email, custom fields, latest location (IP/browser geolocation), custom API data (e.g., shopping basket), visited URLs (chronological); operator-initiated email verification (`$verify`).
- Conversation details: subject, assigned operator, language, status, topic, widget, page impressions/visits/messages, privacy mode; notes (multiple, editable, visible to all operators); message channel info (browser/OS/device for widget messages); session states LIVE/OFFLINE per session.
- All conversations archive: filters (date, operator, status, topic, rating, group, widget, locale, channel, feedback, chats with bots), bulk actions, export, delete; search.
- Contact list: second pillar; multiple ongoing conversations per contact; GDPR-compliant contact deletion (removes conversations too).
- Widget: Widget Editor (Chat > Behavior: supported media, calls; Chat > Advanced: conversation timeout); channels beyond the Website Messenger (WhatsApp, Telegram, SMS, Email, WebChat, custom).

## Product D — Crisp (evidence layer A/B)

- Positioning: chatbox + shared inbox for SMB; knowledge base index categories: Getting Started, Installing Crisp, Customization, Inbox, Campaigns, Knowledge Base, Analytics, Hugo AI Agent & Chatbot, Automations, Contacts & CRM, Legal & Security.
- Install: "How to Install Crisp Live Chat Software on a Custom Website"; chatbox script; Website ID identifies the workspace; multiple Website IDs for separate chatboxes; sub-inboxes for teams/departments/brands inside one workspace.
- Inbox (agent side): "where all your customer conversations come together… whether you are answering live chat, email, or social messages."
  - Routing/assignment: manual assign, agents pick unassigned conversations, or automatic routing rules; Operator Teams group operators by department/role for routing and notifications.
  - Ordering: "status comes first, then recency within each status bucket."
  - Canned responses ("message shortcuts") with CSV import/export; private notes with @mentions; reminders (schedule follow-up; fires the conversation back out of resolved); resolve state; bulk actions; custom filters; automatic triage rules (segments, custom data, spam drop).
  - Transcripts: sent automatically after inactivity or manually; email conversations alongside chat; outbound email from the inbox; CC participants.
  - Message editing (last sent message), Markdown formatting, keyboard shortcuts.
  - Audio/video calls from a conversation "when the visitor is online" (from Essentials tier).
- Widget: customizable chatbox (custom button), 60+ languages; campaigns (targeted); automations; knowledge base with in-inbox article preview; analytics (real-time support performance); Hugo AI agent (message triggers, quick replies).
- File limits documented (default 10 MB etc.) — vendor-specific precision, kept here only.

## Product E — LivePerson (evidence layer A)

- Positioning: enterprise "Conversational Cloud"; spans live chat, async messaging, bots, voice; knowledge center separates "Agent Workspace for live chat" from "Agent Workspace for messaging" and documents "Moving from chat to messaging" — the enterprise pole has migrated the same conversation surface from real-time chat to async messaging.
- Agent Workspace for live chat: "centralized location for agents to manage all of their chat conversations simultaneously."
  - Setup: tag on every page; agent users; agent sets status to online → "automatically enable[s] the chat button on the website".
  - Web Visitors list: all visitors currently on the website with geolocation, browser, IP, current page; sortable (score, country, skill, agent, current page); detailed visit info (campaign, goal, target audience, behavioral targeting, city/country/organization/OS/browser) and page navigation (current + previously visited pages).
  - Conversation start: "visitor initiates a conversation from your website by clicking on the chat button and completing any necessary pre-chat surveys; a notification is displayed on the relevant agent's desktop"; agent accepts.
  - Chat handling: text entry + send; default delay-apology automatic message if the agent is silent; either side can end ("End engagement"; visitor can terminate by closing the chat window).
  - Widgets/tools: visit info, predefined content (library of ready-made responses), page navigation (offer help by journey), agent survey (input to managers about outcome), conversation history (previous transcripts); copy as plain text; private message to another agent; transfer to another agent or skill group with an agent-visible note (refusal returns the chat); end engagement.
  - CoBrowse: view-only or joint browsing of the visitor's page with masked password/credit-card fields; visitor can end the session.
- Automatic Conversation Distribution (ACD): "intelligently routing conversation requests and balancing the workload among the pool of available agents"; basic vs advanced queue options; if the agent doesn't answer within a set interval, the visitor returns to the queue for the next most-available agent. Related machinery: skills-based connection, queue prioritization, queue backlog management, dynamic capacity per skill, agent groups workload distribution.
- Bots: "How bots work in our Conversational Cloud" — bots participate in the same conversation pipeline (bot → human handoff), i.e., automation is a participant layer over the same conversation infrastructure.

## Cross-product Comparison

| Structure | LiveChat | Tawk.to | Lime Connect | Crisp | LivePerson | Evidence |
|---|---|---|---|---|---|---|
| Business-published chat surface on own site/app (widget/button/page/SDK) | ✓ (code snippet, integrations, chat button, chat page + QR) | ✓ (one snippet; chat pages) | ✓ (Website Messenger widget; widget editor) | ✓ (chatbox script; Website ID) | ✓ (tag on every page; chat button; mobile SDK) | A×5 |
| Availability state gates the visitor surface | ✓ (accepting/not accepting; widget availability; working hours) | ✓ (scheduler; agent online count) | ✓ (Online/Away switch; "no operators available → unassigned") | ✓ (implied by routing/unassigned; agent presence) | ✓ (status online "automatically enables the chat button") | A×4 + B |
| Real-time conversation visitor ↔ human agent as the unit | ✓ ("communication between agents and customers happens"; sneak-peek; typing) | ✓ (live chat core; typing; whisper) | ✓ (LIVE label; "time pressure on answering"; chat slots) | ✓ (live chat + inbox) | ✓ (chat button → accept → chat display area) | A×5 |
| Conversation held as transcript / archive | ✓ (Archives; transcripts; tags) | ✓ (history on contact; transcripts) | ✓ (All conversations archive; transcripts; filters) | ✓ (history kept; transcripts; deletion explicit) | ✓ (conversation history widget; transcripts; web history) | A×5 |
| Agent console with concurrent conversations | ✓ (my chats list; concurrent limit; active/inactive) | ✓ (shared inbox) | ✓ (chat slots; Mine/Unassigned) | ✓ (inbox; status-first ordering) | ✓ ("manage all of their chat conversations simultaneously") | A×5 |
| Incoming distribution (auto-assign / queue / manual pickup) | ✓ (automatic vs manual selection; queue; returning-customer rule) | ✓ (departments; assignment) | ✓ (auto-routing to available operators; unassigned) | ✓ (manual / pick-up / automatic routing rules) | ✓ (ACD; queue; skills) | A×5 |
| Visitor context panel | ✓ (customer details; Traffic) | ✓ (contact record auto-built) | ✓ (location, visited URLs, custom data) | ✓ (contact/CRM data) | ✓ (Web Visitors list; visit info; page navigation) | A×5 |
| Canned responses / macros | ✓ (# shortcuts) | ✓ (smart replies/whisper; shortcuts) | ✓ (chat macros, locale variants) | ✓ (message shortcuts) | ✓ (predefined content) | A×5 |
| Private notes / internal-only messages | ✓ (private note on transfer; supervisor whisper) | ✓ (whisper) | ✓ (message/note switch; notes) | ✓ (private notes + @mentions) | ✓ (private message to agent) | A×5 |
| Transfer to agent/group/skill | ✓ | ✓ (departments) | ✓ ($assign/$forward; groups) | ✓ (routing; teams) | ✓ (agent or skill group; refusal returns) | A×5 |
| Concurrent-capacity control | ✓ (per-agent concurrent limit) | (not directly observed) | ✓ (chat slots; async overflow) | (not directly observed) | ✓ (dynamic capacity per skill) | A×3 |
| Pre-chat / offline forms | ✓ (chat forms, data-collection surveys; offline → unassigned) | ✓ (forms; pre-chat) | ✓ (offline conversations NEW; email notification) | ✓ (forms; email channel) | ✓ (pre-chat surveys) | A×5 |
| Proactive engagement (triggers/campaigns) | ✓ (campaigns, eye-catcher, targeted messages) | ✓ (triggers) | (workflows/campaigns exist; WhatsApp campaigns) | ✓ (campaigns; automations) | ✓ (proactive engagements; campaigns) | A×4 |
| Post-chat rating / CSAT | ✓ (reviews; ratings reports) | ✓ (satisfaction stat) | ✓ ($rating; rating filter) | (satisfaction in analytics) | ✓ (agent survey; survey dashboards) | A×4 |
| Reports / monitoring | ✓ (volume, missed chats, agent rankings) | ✓ (dashboard stats) | ✓ (analytics) | ✓ (analytics) | ✓ (dashboards; report center) | A×5 |
| Async messaging mode | ✓ (widget availability "always"; unassigned chats) | ✓ (channels; offline messages) | ✓ (explicit async mode) | ✓ (email + resolved/reminders) | ✓ (messaging products; "moving from chat to messaging") | A×5 |
| Extra messaging channels beyond own widget | ✓ (Messenger, WhatsApp, Apple, Twilio integrations) | ✓ (Messenger, SMS, WhatsApp, Telegram, email) | ✓ (WhatsApp, Telegram, SMS, email, custom) | ✓ (email; social) | ✓ (Apple, WhatsApp, SMS, social, voice) | A×5 |
| Ticketing layer | ✓ (native tickets sunsetted → sibling HelpDesk) | ✓ (ticketing category) | ✗ (not observed) | ✓ (resolved state; reminders; not a ticket desk) | ✓ (case management support) | A×4 |
| Knowledge base / self-service | ✓ (KnowledgeBase sibling) | ✓ (KB product) | (help section; not observed as product pillar) | ✓ (KB product; article preview in inbox) | ✓ (knowledge articles for bots/agents) | A×4 |
| Chatbot / AI layer | ✓ (ChatBot.com sibling; reply suggestions) | ✓ (AI Assist add-on) | ✓ (AI Automation Hub; Connect AI) | ✓ (Hugo AI agent) | ✓ (bots; Conversation Copilot) | A×5 |
| Audio/video calls or co-browse from chat | (not observed in fetched pages) | (voice channel observed) | ✓ (calls, voice messages) | ✓ (audio/video calls) | ✓ (CoBrowse; voice/video calls) | A×3 |
| Ban/block abusive visitors | ✓ (ban for N days) | (not directly observed) | ✓ ($block/$unblock) | ✓ (spam triage) | (not directly observed) | A×3 |

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures:

1. **The business-published conversation surface at the customer touchpoint.** The organization embeds a chat entry point (widget, chat button, hosted chat page, in-app SDK) on its own digital properties; the surface's live behavior is governed by the team's availability state. Remove → a generic messenger or C2B messaging over third-party networks (no owned touchpoint surface), or a contact form (no conversation).
2. **The live support conversation as the unit of work and record.** A visitor or customer and one of the organization's human agents exchange real-time text messages in a single conversation, conducted while both parties are present, and the conversation is retained as a transcript. Remove → async ticket/email correspondence (Help Desk territory) or a static FAQ (no conversation).
3. **The agent-side live operation.** A staffed console in which agents handle multiple conversations concurrently, control their availability, receive incoming conversations through some distribution mechanism (automatic assignment, queue pickup, or routing rules), and see context about the visitor. Remove → peer-to-peer chat with no staffed operation, or a bot-only surface (Chatbot Platform).

Jointly-held is load-bearing:

- 1+2 without 3 = a chat window with no staffed operation behind it (dead widget / unstaffed C2B channel).
- 2+3 without 1 = a generic team inbox or messenger with no business-published touchpoint surface (Team Messaging / shared-inbox territory).
- 1+3 without 2 = visitor analytics plus a chat UI with no conversations (not a realizable product shape — supports that leg 2 is load-bearing).

Notes on the boundary of each leg:

- "Human agents conduct" is load-bearing: in every sampled product the conversation is answered by a person; automation appears only as an assist layer (canned responses, reply suggestions, AI agents with handoff). When automation is the primary conversationalist, the product is the Customer Service Chatbot Platform (seam fixed by that pass; LivePerson confirms both shapes coexist in one vendor under different products/modes).
- "Real-time while both parties are present" is the defining posture; every sampled product also supports an offline/async extension (offline forms, unassigned chats, messaging mode), which is documented as common structure, not as the definition. Lime Connect makes the live/async distinction explicit (LIVE label, chat slots, async overflow); LivePerson documents the enterprise migration path ("moving from chat to messaging") — the live posture remains the Type's namesake and entry mode.
- "Support-scoped, customer-facing" is load-bearing: the conversation is between the business's staff and its (prospective) customers on the business's own properties. Sales/lead-generation use of the same surface is a common secondary posture, not a different Type.

### L1 — Common Mature Structure (not definitional)

- Visitor context panel: geolocation, browser/OS/device, current page, visited-page history, IP; custom/API data (e.g., cart contents).
- Canned responses / macros / predefined content, often with shortcuts and locale variants.
- Private notes / internal-only messages / whisper; supervisor monitoring.
- Transfer to another agent, group, or skill; returning-visitor routing to the previous agent.
- Concurrent-capacity control (per-agent concurrent chat limits / chat slots / dynamic capacity).
- Incoming distribution: automatic assignment by availability, queue with pickup, routing rules (URL/page rules, departments, skills).
- Availability states (online/away/accepting chats) + working hours / scheduler.
- Pre-chat forms and offline/data-collection forms; automatic messages (greetings, delay apologies, away messages).
- Proactive engagement: triggers, targeted messages/campaigns, eye-catchers.
- Transcript archive with search, filters, tags; transcript emailing/export.
- Post-chat rating / CSAT / agent surveys.
- Reports: volume, response times, missed chats, agent performance; real-time monitoring.
- Widget customization: branding, position, language, chat button, hosted chat page / direct link / QR.
- Team structure: groups / departments / skills / teams; roles (owner/admin/agent); multi-device agent apps (web/desktop/mobile).
- Inactivity timeouts; ban/block abusive visitors; file sharing; emoji/reactions; typing indicators; sneak-peek.
- Knowledge-base integration and article suggestions; AI assistance (reply suggestions, AI agents with human handoff) — era-current.

### L2 — Variant / Optional Structure

- Async messaging mode as a first-class posture (widget availability "always"; unassigned chats; messaging products at the enterprise pole).
- Additional messaging channels beyond the owned widget (WhatsApp, Messenger, Telegram, SMS, email, social) — the omnichannel drift.
- Ticketing layer (native or sibling product).
- CRM / contacts layer built from conversations.
- Knowledge base / self-service product layer.
- Chatbot layer (native or sibling product).
- Co-browsing; audio/video calls from the conversation.
- E-commerce integrations (cart data, shopping-cart platforms, sales tracking, goals).
- Privacy/compliance tooling (GDPR deletion, data masking, PII redaction at the enterprise pole).
- White-labeling; self-hosting (thin in this sample; open-source shared-inbox pole documented by the chatbot pass).
- Sales/lead-generation posture (proactive sales chat, conversion goals) — same surface, different emphasis.

### L3 — Vendor-specific (research notes only)

- LiveChat: native Tickets sunsetted (per-plan schedule documented) in favor of sibling HelpDesk.com; "eye-catcher"; Sales Tracker; supervised chats; Starter-plan 3-minute fixed auto-transfer timeout; active/inactive chat statuses and their interaction with the concurrent limit.
- Lime Connect: "chat slots" terminology; LIVE/NEW/OPEN/PENDING/ENDED status machine with documented 30-day auto-end; `$verify` operator-initiated email verification; Live Translation; 180-second call expiry; 100 MB upload limit; GDPR-compliant contact deletion including conversations; rebrand Userlike → Lime Connect (Lime Technologies).
- LivePerson: ACD basic/advanced queue options with return-to-queue interval; "Night Vision" overlay for ACD settings; Meaningful Conversation Score (MCS); CoBrowse orange frame + field masking; Tenfold (partner telephony layer); separate live-chat vs messaging agent workspaces.
- Tawk.to: free-forever model ("Why Free"); Chat Pages; AI Assist as paid add-on; white-label add-on.
- Crisp: Website ID / multiple workspaces vs sub-inboxes; Hugo AI agent; automatic triage; reminders; 10 MB default upload limit; last-message editing.

## Historical / Market-Sample Check

- 1990s–2000s anchor: LivePerson's own live-chat documentation (chat button enabled by agent status, visitor list, pre-chat survey, accept, chat display area, predefined content, transfer) describes the same core that late-1990s/early-2000s "live help" products sold; LiveChat (2002) and the Zopim/Olark/Tawk.to generation (2008–2013) satisfy the core with no AI, no omnichannel, no CRM, no knowledge base. ✓
- Thin ancestor: the contact form / "leave a message" box — fails leg 2 (no live conversation) and leg 3 (no staffed live operation); correctly excluded.
- Adjacent-shape check: website widgets delivering open visitor *rooms* are a delivery form of the Chat Room Application Type (fixed by that pass); visitor-to-agent 1:1 conversations are this Type. ✓
- Platform-native/regional: in-app SDK chat (mobile apps), hosted chat pages, QR-code chat links, and messaging-network channels all realize leg 1's "business-published conversation surface"; the widget is the dominant implementation, not the definition. ✓
- Async drift check: the enterprise pole (LivePerson) has migrated its flagship surface from live chat to async messaging while keeping the same conversation infrastructure; the live posture nevertheless remains the recognizable core of the Type (product names, LIVE labels, "real-time support" positioning across the sample). Async is documented as common extension, not definition. ✓

## Vendor-specific Findings

See L3 above. Cross-vendor observation worth recording: LiveChat's ticket sunset is direct market evidence that the live-chat conversation layer and the ticket-record layer are separable products that vendors split and recombine — supporting the Help Desk boundary rather than weakening it.

## Boundary Findings

- **vs Customer Service Chatbot Platform** (closest sibling; seam fixed by that pass, confirmed from this side): chat = human agents conduct real-time conversations; chatbot platform = automation conducts first, humans enter through a governed seam. Remove the automated participant → this Type. LivePerson ships both shapes (Conversation Builder bots vs live-chat agent workspace) — automation-first vs human-first holds as the keep-both discriminator. The chatbot pass's advance flag is discharged: no joint review needed for the bot seam; the flag's other half (Omnichannel CSP) remains open below.
- **vs Help Desk / Ticketing System** (help-desk pass seam, confirmed): chat tools own one real-time channel and the conversation is the central object; the desk owns the persistent tracked request record with lifecycle and SLAs. Chat conversations *become* tickets in the desk (LiveChat's own ticket-from-chat flow, later sunsetted; Tawk.to's "when an enquiry is a problem, not a sale, it becomes a ticket"). Remove the live conversation → shared inbox / help desk.
- **vs Customer Service Platform** (processed): the platform of record operates the whole service function (case of record + agent operation + integrated span: multi-channel intake, self-service, automation, operation management). This Type is the conversation channel layer; it does not hold the service case of record. LiveChat's product family (LiveChat + HelpDesk + KnowledgeBase + ChatBot) is the market's own decomposition of the suite into this Type plus siblings.
- **vs Omnichannel Customer Service Platform (unprocessed sibling)** — OPEN SEAM for joint review: every sampled live-chat product now connects extra messaging channels (WhatsApp, Messenger, SMS, email…), so "single channel vs many channels" is a posture gradient, not a clean binary. This pass holds the Type on the owned-surface center of gravity (the business-published chat on the organization's own properties is the product's heart; other channels are connectors), and flags for joint review when omnichannel-customer-service-platform is processed: whether channel-posture (chat-first vs channel-unification-first) holds as the keep-both discriminator.
- **vs Contact Center Platform** (contact-center pass seam, confirmed): the contact center is the multi-channel live-interaction distribution machinery (voice heritage, ACD/queues/WFM); this Type is the chat conversation surface itself. At the enterprise pole the machinery converges (LivePerson's ACD/skills/capacity are contact-center machinery applied to chat) — the seam is the center of gravity, not a wall.
- **vs C2B / Business Messaging Application** (those passes' seams, confirmed and refined): C2B/Business Messaging runs over third-party messaging networks through public business points and is intent-agnostic; this Type runs over the business's own embedded surface and is support/service-scoped with a staffed agent operation. LiveChat's Messenger/WhatsApp/Apple connectors show the same product bridging both — the owned widget remains the defining surface.
- **vs Chat Room Application** (that pass's seam, confirmed): 1:1 visitor-to-agent conversations are this Type; shared visitor rooms are a chat-room delivery form.
- **vs Remote Customer Support Platform** (that pass's seam, confirmed): conversation-first, no device visibility or control; remote-support products embed chat as an in-session tool. Remove device control → this Type.
- **vs Digital Concierge** (that pass's seam, confirmed): generic support lacks stay anchoring and physical-service fulfillment semantics.
- **vs Team Messaging / Instant Messaging**: audience (external customers vs internal team / personal contacts) and the business-published availability-gated surface separate both.
- **"去掉什么就变成另一个 Type" summary**: remove the staffed human operation → chatbot platform; remove the live conversation (keep the record) → help desk; remove the owned touchpoint surface (keep conversations over messaging networks) → C2B/business messaging; remove the conversation (keep distribution machinery) → contact center; remove the business context (keep the room) → chat room; remove support scoping → business messaging.

## Uncertainties

- The exact visitor-side behavior when all agents are busy (queue position display, estimated wait) varies by product and was not directly observed in fetched pages for every sample; no precise queue-depth or wait-time claims are made.
- Whether "concurrent chat limit" is universal or merely common: directly documented at LiveChat (per-agent limit), Lime Connect (chat slots), LivePerson (dynamic capacity); not directly observed at Tawk.to/Crisp. Held as common structure, not definitional.
- The SMB free pole (Tawk.to) documents its ticketing/CRM/KB layers only at index level in this pass (category pages errored); layer-A depth for those layers is thinner than for LiveChat/Lime Connect. Assertions about them are kept at "common optional layer" strength.
- Olark and Comm100 could not be fetched; the minimalist-human-chat and enterprise-on-prem poles are covered indirectly (LivePerson for enterprise; LiveChat's simplicity articles for the minimal pole). No claims rest on those two vendors.
- The boundary with Omnichannel Customer Service Platform cannot be fully settled until that leaf is processed (flagged for joint review).

## Final Synthesis

A Customer Support Chat application is the business-operated live conversation layer of customer service: the organization publishes an availability-gated chat surface on its own website or app; visitors and customers open real-time text conversations with the organization's human support agents; a staffed agent console distributes incoming conversations across the team, carries visitor context next to each conversation, and retains every conversation as a transcript. Everything else the sampled products ship — visitor analytics, canned responses, proactive campaigns, ratings, reports, knowledge bases, bots, extra messaging channels, ticketing, CRM — is common mature structure or optional layering around that core. The Type's identity is held by three jointly-held structures (owned touchpoint surface + live human-conducted conversation as unit of record + staffed agent-side live operation); removing any one of them turns the product into a neighboring Type.
