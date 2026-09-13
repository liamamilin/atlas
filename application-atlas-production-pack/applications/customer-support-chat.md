# Customer Support Chat

## Overview

A **Customer Support Chat** application is the business-operated live conversation layer of customer service: the organization publishes a chat entry point on its own website or app, visitors and customers open real-time text conversations with the organization's human support agents, and a staffed agent console distributes those conversations across the team and retains each one as a transcript.

The defining core is small:

```text
Business-published conversation surface (widget / chat page / in-app SDK)
└── Visitor or customer
    └── Live support conversation (real-time, human-conducted, held as a transcript)
        └── Agent-side live operation (staffed console: availability, distribution, concurrent conversations, visitor context)
```

Everything else commonly associated with these products — visitor analytics, canned responses, proactive campaigns, satisfaction ratings, reports, knowledge bases, chatbots, extra messaging channels, ticketing, CRM — is standard capability or optional layering, not what makes the product a Customer Support Chat. When the automated participant, the live conversation, the owned surface, or the staffed operation is removed, the product becomes a neighboring Application Type (Chatbot Platform, Help Desk, C2B Messaging, Contact Center).

## Users & Context

The primary users are the organization's **support agents**: staff who sign into an agent console, set their availability, and conduct several customer conversations at once. Their work is time-pressured by design — the person on the other side is waiting live — so the console is built around switching between concurrent conversations quickly.

Secondary users:

- **team leads / supervisors** — monitor ongoing conversations, whisper guidance invisible to the customer, take over or transfer conversations, review agent performance
- **administrators** — configure the widget, working hours, departments or skills, routing rules, canned responses, and roles

The **customer** is a user of the product's other half without ever installing it: a visitor browsing the organization's website or app who clicks the chat button, asks a question, and expects an answer while the page is still open. Typical contexts are e-commerce stores, SaaS products, service businesses, and any organization that wants to answer pre-sale and post-sale questions in real time on its own properties.

## Core Model

### The Defining Core

```text
Business-published conversation surface
└── Visitor or customer
    └── Live support conversation
        └── Agent-side live operation
```

Three structures. If any one is removed, the product is no longer recognizable as a Customer Support Chat:

- **Business-published conversation surface** — a chat entry point the organization embeds on its own digital properties: a website widget or chat button, a hosted chat page or direct link, or an in-app SDK surface. Its live behavior is governed by the team's availability state: when agents are accepting conversations the surface offers live chat; when they are not it offers an offline form or an async message thread. Without an owned touchpoint surface, the product is a messenger operating over third-party networks, not a chat layer on the business's own properties.
- **Live support conversation** — a real-time text conversation between a visitor or customer and one of the organization's human agents, conducted while both parties are present, and retained as a transcript. The conversation — not a ticket, not an answer — is the unit of work and the unit of record. Without the live conversation, the product is a contact form or a FAQ page; without the human agent, it is a chatbot.
- **Agent-side live operation** — a staffed console in which agents handle multiple conversations concurrently, control their availability, receive incoming conversations through some distribution mechanism, and see context about the visitor next to each conversation. Without the staffed operation, the surface is a dead widget; without the owned surface, the console is just a team inbox.

### Standard Capabilities

Mature products carry most of the following. They make the live operation practical; they do not define the Type.

- **Visitor context panel** — who the visitor is and what they are doing: location, browser and device, the page they are on, the pages they visited before, and optionally custom data such as cart contents. This context is what lets an agent answer without asking the customer to re-describe everything.
- **Canned responses / macros** — pre-written reply blocks recalled by shortcut, often with per-language variants.
- **Private notes and whispers** — an internal-only message layer inside the conversation: notes for handovers, supervisor guidance invisible to the customer.
- **Transfer** — hand a conversation to another agent, department, or skill, usually with an internal note; some products return a refused transfer to the original agent.
- **Concurrent-capacity control** — a per-agent limit on simultaneous live conversations; when an agent is full, new conversations route elsewhere or wait in a queue.
- **Incoming distribution** — automatic assignment to available agents, a queue that agents pick up from, or routing rules that send conversations to the right department, skill, or page-specific team. Some products also route returning visitors back to the agent who served them before.
- **Availability states and working hours** — online/away/accepting-chats states per agent, plus scheduled hours that switch the widget between live chat and offline mode.
- **Pre-chat and offline forms** — short forms that collect contact details before or instead of a conversation.
- **Proactive engagement** — triggers and targeted messages that open or invite a conversation based on page, behavior, or audience.
- **Transcript archive** — every ended conversation stored, searchable, filterable, taggable, and exportable or emailable as a transcript.
- **Post-chat rating** — a satisfaction prompt at the end of a conversation, feeding agent-level and overall reports.
- **Reports and monitoring** — conversation volume, response times, missed chats, agent performance; real-time views of who is online and what is waiting.
- **Widget customization** — branding, position, language, chat button, attention-grabbing teasers; hosted chat pages, direct links, and QR codes as alternative surfaces.
- **Team structure and roles** — departments, groups, or skills; owner/administrator/agent roles; web, desktop, and mobile agent apps.
- **Conversation mechanics** — typing indicators, message sneak-peek (the agent sees what the visitor is typing), file sharing, emoji and reactions, inactivity timeouts, automatic messages (greetings, delay apologies), banning abusive visitors.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations vary:

```text
Concept:   Business-published conversation surface
Forms:     website widget, chat button, hosted chat page / direct link / QR, in-app SDK

Concept:   Live support conversation
Postures:  strictly real-time chat; live-first with async overflow; async messaging mode
           (offline forms, unassigned threads) as the extension of the same surface

Concept:   Incoming distribution
Forms:     automatic assignment by availability, queue with manual pickup,
           rule-based routing by page / department / skill

Concept:   Visitor identity
Forms:     anonymous session (cookie-based), contact details from forms,
           identified customer from a connected CRM or login
```

A reader who has only seen one implementation — the corner widget on a retail site — should still recognize an in-app SDK chat or a hosted chat page as the same Type.

## How It Works

### Publish the surface and staff it

```text
Create an account
→ paste the snippet (or use a platform integration / SDK) on the site or app
→ customize the widget
→ invite agents, set departments and working hours
→ agents sign in and set their status to accepting conversations
→ the chat button goes live on the site
```

The visitor-facing surface and the staffed console are two halves of one state: an agent going offline changes what visitors see.

### Conduct a conversation

```text
Visitor opens the site → clicks the chat button
→ (optional pre-chat form)
→ the conversation enters distribution:
     automatic assignment to an available agent, or a queue for pickup
→ agent accepts and replies in the console; visitor sees the reply in the widget
→ both sides exchange messages in real time (typing indicators, sneak-peek, files)
→ agent may transfer, whisper internally, or consult canned responses
→ question resolved → agent ends the conversation
→ conversation is closed and archived as a transcript
→ (optional) rating prompt; (optional) follow-up as a ticket or email
```

This loop — publish, distribute, conduct live, archive — is the defining workflow of the Type. The agent typically handles several such conversations at once, switching between them from the conversation list.

### When the team is offline

```text
No agent accepting conversations
→ widget shows an offline form or an async message thread
→ the visitor's message is stored (offline form, unassigned thread, or email)
→ agents answer later from the same console
→ the reply reaches the visitor by email and/or in the widget on their next visit
```

Every sampled product extends the live surface with this asynchronous mode; the live conversation remains the product's center and its namesake.

### Reach out proactively

Rules or campaigns watch who is on the site and open or offer a conversation at the right moment — a greeting on a pricing page, an offer of help after some time on a page, a targeted announcement. The conversation that results flows through the same live loop.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Visitor-facing chat widget

The published surface on the organization's site or app.

- chat button or bubble; when opened: greeting, message history with the same visitor, message input, typing indicator, file attachment
- availability-dependent content: live chat invitation, queue/waiting notice, or offline form
- primary actions: start a conversation, send a message, share a file, rate the conversation

### Agent console — conversation list

The agent's queue of live work.

- lists the agent's own ongoing conversations, queued conversations waiting for pickup, and (in some products) conversations being supervised or left unassigned while the team was offline
- surfaces status (active vs waiting), waiting time, and which conversations still need an agent's reply
- primary actions: open a conversation, pick up from the queue, assign to yourself, transfer, end

### Agent console — conversation view

Where the conversation is conducted.

- message feed with visitor messages, agent replies, and system events; internal notes layer
- visitor context panel beside the feed (location, pages, contact details, custom data)
- reply tools: canned responses, emoji, file sharing, translation in some products
- primary actions: reply, whisper/note, transfer, tag, request rating, end conversation

### Archives

The transcript store.

- past conversations with filters (date, agent, department, tag, rating, channel), search, and transcript export or email
- primary actions: search, inspect, tag, export, resume a conversation

### Settings / administration

The configuration surface.

- widget customization, availability and working hours, departments/skills, routing and assignment rules, canned responses, forms, proactive campaigns, roles and agent accounts
- primary actions: configure, publish, invite agents

### Reports / monitoring

- conversation volume, response times, missed chats, agent performance, satisfaction; real-time views of agents online and queue state

## Important Rules / Behaviors

### Availability gates the surface

The team's availability state is not cosmetic: it decides whether a visitor sees a live chat, a queue notice, or an offline form. This coupling between the staffed side and the visitor side is a defining behavior of the Type.

### Conversations are owned and distributed

An incoming conversation is assigned through the product's distribution mechanism — automatically to an available agent, or into a queue for pickup. Ownership matters: in several products only the assigned agent can answer, and transfers exist precisely because ownership is exclusive. Some products route returning visitors back to the agent who helped them before.

### Live work is capacity-bounded

Agents handle a bounded number of live conversations at once. When an agent is full, new conversations route to other agents or wait; some products let the conversation continue asynchronously instead. The limit is a staffing instrument, and products commonly expose it per agent.

### Two layers inside one conversation

Every conversation carries a customer-visible layer (messages) and an internal-only layer (notes, whispers, transfer notes). The internal layer never reaches the visitor; it is the collaboration and supervision surface.

### The conversation is the record

The transcript is retained after the conversation ends and is searchable and exportable. Where a request outgrows the conversation — a refund to process, a bug to fix — products bridge to a ticket or email, but the bridge is an extension: the chat product's own record is the conversation.

### Real-time expectations shape behavior

Because the customer is waiting live, products build in time-sensitive machinery: typing indicators, sneak-peek, inactivity timeouts, automatic delay apologies, and auto-transfer when an agent does not respond. Abusive visitors can be banned; satisfaction is measured at the conversation's end.

## Variants

Common forms of the same Type:

- **classic live chat** — real-time website widget as the whole product; minimal surrounding machinery
- **live chat + async messaging mode** — the same widget offering offline threads and unassigned messages when the team is away
- **unified-messaging posture** — the owned widget plus connected messaging channels (WhatsApp, Messenger, Telegram, SMS, email) answered from one console; the owned surface remains the center
- **suite-embedded live chat** — the chat layer as one product inside a vendor's service suite alongside ticketing, knowledge base, and chatbot products
- **enterprise conversational platform** — the chat surface operated with contact-center machinery (skills, capacity, queue management) and bot participation with human handoff
- **all-in-one SMB inbox** — chat plus CRM, ticketing, knowledge base, and campaigns in one free or low-cost product
- **sales/lead-generation posture** — the same surface aimed at converting visitors rather than resolving issues; proactive engagement emphasized
- **in-app SDK chat** — the surface embedded in a mobile or desktop app rather than a website

A variant remains a variant unless it changes the core users, objects, or workflow: once automation becomes the primary conversationalist, the product is a Customer Service Chatbot Platform; once the tracked request record becomes the center, it is a Help Desk.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Customer Service Chatbot Platform | automation conducts the conversation first, humans enter through a governed handoff seam; here humans conduct and automation only assists. Remove the automated participant → this Type |
| Help Desk / Ticketing System | owns the persistent tracked request record with lifecycle and SLAs; chat is one intake channel and conversations *become* tickets there. Here the live conversation itself is the unit of record |
| Customer Service Platform | operates the whole service function (case of record, multi-channel intake, self-service, automation, operation management); this Type is the conversation channel layer within that span |
| Omnichannel Customer Service Platform | channel-unification-first: many channels as first-class equals; here the business-published chat surface is the center and other channels are connectors |
| Contact Center Platform | multi-channel live-interaction distribution machinery (voice heritage, queues, workforce management); this Type is the chat conversation surface itself, though enterprise products apply contact-center machinery to it |
| Customer-to-Business / Business Messaging | conversations over third-party messaging networks through public business points, intent-agnostic; here the surface is the business's own property and the scope is support |
| Chat Room Application | shared visitor rooms with self-service join; here conversations are 1:1 between a visitor and the staffed team |
| Remote Customer Support Platform | live sessions into the customer's device with control; here conversation only, no device visibility or control |
| Digital Concierge | hospitality guest messaging anchored to a stay with physical-service fulfillment; generic support lacks both |
| Team Messaging Application | internal employees in organizational channels; here external customers on a business-published surface |
| Self-service Support Portal | async content and request forms; here live human conversation |

The two most important boundaries: with the **Chatbot Platform** (who conducts the conversation) and with the **Help Desk** (what the record is). Both seams are confirmed by market behavior — vendors split the chat layer and the ticket layer into separate products, and bots hand off into human chat rather than replacing it.

## Representative Products

- LiveChat — archetypal premium live-chat pure-play
- Tawk.to — free-forever live chat for SMB
- Lime Connect (formerly Userlike) — unified-messaging live chat with a privacy/EU posture
- Crisp — all-in-one SMB chatbox and shared inbox
- LivePerson — enterprise conversational platform spanning live chat, messaging, and bots

The defining core was checked against the market's history (late-1990s/early-2000s live-help products) and against the async-messaging drift at the enterprise pole, so that the definition is not over-fitted to today's dominant packaging.

## Sources

Research date: **2026-09-08**

- LiveChat — Help Center: https://www.livechat.com/help/ (incl. Chats section overview, Understanding chat assignment)
- Tawk.to — product page and Help Center: https://www.tawk.to/ , https://help.tawk.to/
- Lime Connect (formerly Userlike) — product guide: https://docs.userlike.com/ (Message Center)
- Crisp — Knowledge Base: https://help.crisp.chat/ (Inbox category)
- LivePerson — Customer Success Center: https://knowledge.liveperson.com/ (Agent Workspace for live chat; Automatic Conversation Distribution)

> Sourcing limitation: Olark (transport errors) and Comm100 (404) could not be fetched and are not cited; no claim in this document rests on them. Precise vendor-specific numbers (timeouts, limits, status names) are intentionally not stated here; they remain in the Research Notes.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
