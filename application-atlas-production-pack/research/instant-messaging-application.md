# Research Notes — Instant Messaging Application

## Research Goal

Identify the smallest stable invariant that defines the **Instant Messaging Application** Type, and place every other observed feature at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

It also separates evidence into layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Instant Messaging Application

Nearest confusing Types:

- Team Messaging Application
- Group Messaging Application
- Community Chat Platform
- Social Live Streaming Platform
- Voice & Calling Applications (Internet Calling / Softphone)
- Dating Application

Working hypothesis:

> IM is private or small-group message exchange between individually addressable participants, retained as persistent conversation history.

The hypothesis is intentionally broader than "phone-number + address book + delivery receipts" — those are common modern implementations, not the defining invariant.

## Research Questions

- What makes a product recognizable as an Instant Messaging product at all, independent of era or platform?
- How is "who can talk to whom" addressed in this Type?
- What is the smallest unit of conversation?
- What survives across implementation variants: phone-number identity, username identity, platform-account identity?
- What does a long-lived IM look like that is not built around the phone-number pattern? (platform-native IM, regional IM, social-graph IM, old desktop IM)
- Where is the structural boundary with Team Messaging (workspace + persistent channel + member)?

## Representative Products

| Product | Why selected |
|---|---|
| WhatsApp | dominant modern mobile IM; phone-number identity |
| Signal | privacy-focused mobile IM; phone-number identity, later layered username |
| Telegram | username-layered identity; cloud-synced history; very large group variant |
| WeChat | regional super-app with IM core; multi-discovery (phone, ID, QR) |

Additional products used for **historical / market-sample breadth** (per `WORKFLOW_v1.1.md §24`), not for primary structural evidence:

- iMessage / Messages (Apple) — platform-native IM; identity is Apple ID / phone number; SMS/RCS fallback
- Facebook Messenger — IM built on top of a social-graph identity
- Older desktop IM (e.g. ICQ / MSN Messenger / early QQ) — historically username-based, no phone number

The older / platform-native / social-graph samples are precisely the reason phone-number identity should not be promoted into the defining invariant.

## Sources

Research date: **2026-09-05**

Direct fetch of `faq.whatsapp.com`, `support.signal.org`, `telegram.org/faq`, and `cs.help.wechat.com` was not possible from the research environment on 2026-09-05 due to network restrictions on those vendor domains.

Primary vendor surfaces used (root / about / support pages only):

- WhatsApp — https://www.whatsapp.com/ , https://faq.whatsapp.com/
- Signal — https://signal.org/ , https://support.signal.org/
- Telegram — https://telegram.org/tour , https://telegram.org/faq
- WeChat — https://www.wechat.com/en/ , https://weixin.qq.com/

Aggregator references used on the research date because vendor help-center articles were not reachable:

- Baidu Baike — WhatsApp Messenger: https://baike.baidu.com/item/WhatsApp%20Messenger/7592753
- Baidu Baike — Signal: https://baike.baidu.com/item/信号/65615862
- Baidu Baike — Telegram: https://baike.baidu.com/item/纸飞机/4015068

Per `WORKFLOW_v1.1.md §23 Source-access Limitation`:

> 1. record the limitation in Research Notes ✓
> 2. reduce assertion strength ✓
> 3. avoid precise workflow/rule claims that depend on inaccessible evidence ✓
> 4. do not compensate by silently filling detail from model memory ✓

The four-product sample was therefore used at the level of widely-attested public structural facts (identity model, conversation unit, persistence, call binding), not at the level of exact feature numbers, edit windows, or default settings.

## Product Observations

### WhatsApp

- Layer A: identity is the phone number; users are discovered via the device address book; 1:1 and small group chat are primary; messages persist; voice/video calls share the same identity.
- Layer A: a one-to-many broadcast primitive ("Channels") exists in the product; a Story-style ephemeral "Status" exists; WhatsApp Business is a separate product line.
- Layer B observation: phone-number identity with address-book-based reachability graph matches the dominant modern mobile IM pattern.

### Signal

- Layer A: identity is the phone number; address-book-based reachability; 1:1 and group chat with persistent history; voice/video calls on the same identity.
- Layer A: disappearing messages are a first-class primitive (timer attached to message lifecycle); minimal metadata collection is a defining product philosophy.
- Layer B observation: privacy posture (default E2EE, minimal metadata, disappearing messages) is a Common modern variant rather than a defining property of IM.

### Telegram

- Layer A: identity is the phone number for registration, plus an optional `@username` handle that is the primary discovery layer for non-contacts.
- Layer A: 1:1 chat, group chat, and a broadcast "Channel" primitive exist in the same product; cloud-synced history by default.
- Layer B observation: cloud-synced history is one common implementation of "persistent conversation history"; it is not the only one.

### WeChat

- Layer A: identity is the phone number plus an optional WeChat ID / QR-code identity; 1:1 and group chat at the core; voice/video calls on the same identity.
- Layer A: super-app surfaces (Moments, Mini Programs, WeChat Pay) exist in the same product but are structurally not IM.
- Layer B observation: QR-code-based and platform-account-based identity are common variants; they do not change the defining invariant.

### Historical / market-sample breadth

- iMessage (Apple): identity is Apple ID / phone number; SMS / RCS fallback when recipient is not on iMessage.
- Facebook Messenger: identity is Facebook social-graph identity; IM is one surface of a larger social product.
- Older desktop IM (ICQ, MSN Messenger, early QQ): identity is a numeric or alphanumeric username; reachability is in-app, not address-book based.

These samples confirm the abstraction in the next section: identity can be phone-number, username, platform-account, or social-graph account; reachability can be address-book, in-app contacts, or platform contacts. The Type survives all of these.

## Cross-product Comparison

| Finding | WhatsApp | Signal | Telegram | WeChat | iMessage | Older IM | Abstraction level |
|---|---|---|---|---|---|---|---|
| individually addressable participant | yes | yes | yes | yes | yes | yes | L0 |
| private conversation between specific participants | yes | yes | yes | yes | yes | yes | L0 |
| persistent conversation history | yes | yes | yes (cloud) | yes | yes | yes | L0 |
| message as communication unit | yes | yes | yes | yes | yes | yes | L0 |
| reachability graph | address book | address book | address book + username | address book + ID + QR | Apple contacts | in-app contacts | L1 |
| group conversation (member-defined) | yes | yes | yes | yes | yes | yes (with limits) | L1 |
| delivery / read state | yes | yes | yes | yes | yes | varies | L1 |
| media messages (image / video / file / voice) | yes | yes | yes | yes | yes | yes (later) | L1 |
| profile (name, avatar) | yes | yes | yes | yes | yes | yes | L1 |
| presence / last-seen | yes | yes (configurable) | yes | yes | yes | yes (early IM) | L1 |
| voice / video call on same identity | yes | yes | yes | yes | yes | later | L1 |
| phone-number identity | yes | yes | yes (for registration) | yes | yes | no (historically) | L2 |
| username handle for discovery | added later | added later | yes (central) | yes (WeChat ID) | no | yes (historically) | L2 |
| platform-account identity | no | no | no | no | yes (Apple ID) | no | L2 |
| social-graph identity | no | no | no | no | no | yes (Messenger) | L2 |
| broadcast Channels | yes (later) | no | yes (central) | no | no | no | L2 / adjacent Type |
| Story-style ephemeral posts | yes (later) | no | no | yes (Moments) | no | no | L2 / adjacent Type |
| in-app payments | yes (limited) | yes (MobileCoin, some builds) | no | yes | yes (Apple Pay adjacent) | no | L2 / adjacent Type |
| bot / mini-app platform | no | no | yes (later) | yes (Mini Programs) | yes (iMessage Apps) | no | L2 / adjacent Type |
| default end-to-end encryption | yes (Signal Protocol) | yes (Signal Protocol) | no (Cloud Chat only) | partial | yes | no (historical) | L2 |
| disappearing messages | optional | first-class | optional | no | no | no | L2 |
| multi-device sync | yes (companion devices) | yes (linked devices) | yes (native multi-device) | yes | yes (Apple ecosystem) | no (historical) | L2 |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as Instant Messaging:

```text
Personal Addressable Identity
└── Reachability between specific known participants
    └── Conversation thread between identified participants
        └── Message as unit of communication
            └── Persistent conversation history
```

If any of these four properties were removed, the product would either become unrecognizable as IM, or become a different Application Type:

- remove *personal addressable identity* → it becomes a broadcast / channel product (Community Chat / Social Live Streaming)
- remove *reachability between specific known participants* → it becomes a public discovery surface (Community Chat / Social Network)
- remove *conversation thread between identified participants* → it becomes a transaction surface or a tool
- remove *persistent conversation history* → it becomes an ephemeral live surface (Live Social / Audio Room)

## L1 — Common Mature Structure

Capabilities and objects that are common in mature modern IM products but are not part of the strict definition. These make IM practical; they do not make it IM.

```text
Reachability graph (contact list / address book / in-app contacts)
Group conversation (member-defined, bounded membership)
Delivery / read state (sent / delivered / read)
Media messages (image / video / file / voice note)
Profile (display name, avatar, optional "about" text)
Presence (online / last-seen / typing indicator)
Voice / video call on the same identity
```

A product can still be IM without all of these (e.g. an older text-only IM with no calls), but a typical modern consumer IM will include most of them.

## L2 — Variant / Optional Structure

Common implementation choices and optional capabilities. Their presence or absence does not change the Type.

```text
Identity substrate
- phone-number identity
- username identity
- platform-account identity (Apple ID, Microsoft Account, etc.)
- social-graph identity
- email-based identity (rare today, common historically)

Reachability construction
- device address book auto-population
- in-app contacts
- username search
- QR-code contact card
- platform contacts

Encryption posture
- default end-to-end encryption
- optional end-to-end encryption
- no end-to-end encryption (transport-layer only)

Message lifecycle options
- disappearing messages / message timer
- edit window
- delete-for-everyone
- forward / reply / react

Multi-device behavior
- companion device (phone-primary)
- native multi-device
- single device

Adjacent surfaces (still allowed inside an IM product, but not part of IM as a Type)
- broadcast Channels
- ephemeral Story / Status posts
- in-app payments
- bot / mini-app platforms
```

## L3 — Vendor-specific Structure

Modules, names and limits that belong to individual products and should not be promoted into the canonical core:

- WhatsApp Channels, WhatsApp Status (Story), WhatsApp Business, WhatsApp Pay
- Telegram Channels (broadcast), Telegram Secret Chat, Telegram Voice Chat Rooms
- WeChat Moments, WeChat Mini Programs, WeChat Pay
- Signal's MobileCoin integration
- Specific encryption protocols (Signal Protocol, MTProto)
- Specific numeric limits (group-size caps, edit windows, device counts, history-retention rules)
- Branded workflow names and bundled suite modules

These remain in Research Notes as evidence and examples; they do not enter the Application Document.

## Canonical Model (v1.1)

```text
L0
Personal Addressable Identity
└── Reachability between specific known participants
    └── Conversation thread (1:1 or member-defined small group)
        └── Message
            └── Persistent conversation history
```

This is the entire Core Model. Everything else is L1 or lower.

## Boundary Findings

### vs Team Messaging Application

The Team Messaging Golden Example (`examples/application-docs/team-messaging.md`) defines its Type as:

- **Organizational container** (workspace / team) provides identity context.
- **Channel** is a persistent shared conversation space organized around a topic, project, or department.
- **Direct conversation** is a private surface inside the same identity context.
- Conversation is *persistent and discoverable inside an organizational collaboration context*.

IM differs structurally on every one of these axes:

- IM has no organizational container. Identity is personal, not workspace-based.
- IM has no persistent shared conversation spaces belonging to an organization. Conversations are between personal contacts.
- IM does not make conversation "discoverable" inside an organizational context; reachability is via the personal contact graph.
- IM does not have a `Channel` object; the 1:1 chat and the member-defined small group are the only conversation shapes.

The cleanest boundary test:

> Removing workspace + channel + topic from a Team Messaging product leaves an IM.
> Removing personal-identity + personal-contact-graph from an IM does not yield a Team Messaging product.

This is consistent with the boundary note in `examples/application-docs/team-messaging.md:262`:
> "Instant Messaging Application — more centered on contacts and private conversations; organizational channels are not necessarily primary."

### vs Group Messaging Application

Group Messaging is largely a focused variant of IM Group Chat. It does not currently present a structurally distinct model; the boundary may deserve review in a later pass.

### vs Community Chat Platform

- Community Chat is organized around public / semi-public servers or topics with discovery and moderation.
- IM reachability is the personal contact graph, not a discoverable community space.

### vs Social Live Streaming / Audio Room

- Live Social is broadcast-shaped with many simultaneous listeners; IM is bidirectional, 1-to-1 or small-group, and persistent.

### vs Voice & Calling Applications

- Softphone / Internet Calling centers on a call log and dialer; messaging is secondary.
- IM includes voice / video calls as L1 capability on the same identity; messaging is primary.

### vs Business Messaging / Customer-to-Business Messaging

- Business Messaging is organization-to-customer; IM is person-to-person by default.
- WhatsApp Business is a separate product line, not a feature of WhatsApp personal IM.

## Uncertainties

- Live vendor help-center pages were not fetchable on the research date. The structural claims above are derived from widely-attested public facts about the four products; precise operational details (numeric limits, default settings, encryption modes, edit windows) are not stated in the final document.
- "Personal Addressable Identity" was chosen as the L0 abstraction because it survives the historical / regional / platform-native samples. Whether this is the strongest possible L0 abstraction, or whether it should be split further (e.g. *identity* vs *reachability graph* as two L0 objects), is an open refinement question.
- The boundary with Group Messaging Application is not yet crisp; the canonical model of Group Messaging should be checked against IM Group Chat in a separate research pass.
- Dating Application and Business Messaging are listed as Related Types but were not researched as primary samples for this leaf.

## Final Synthesis

Canonical Instant Messaging, v1.1:

```text
L0 (defining invariant)
- Personal Addressable Identity
- Reachability between specific known participants
- Conversation thread between identified participants
- Message as unit of communication
- Persistent conversation history

L1 (common mature structure)
- Reachability graph (contact list)
- Group conversation (member-defined)
- Delivery / read state
- Media messages
- Profile
- Presence
- Voice / video call on the same identity

L2 (variant / optional)
- Identity substrate: phone number / username / platform account / social-graph account
- Reachability construction: address book / in-app contacts / username search / QR
- Encryption posture, disappearing messages, multi-device behavior
- Adjacent surfaces (Channels, Stories, payments, bots) — allowed in product, not in IM Type
```

The Application Document will present only L0 and L1, with a Variants section that names L2 options. L3 stays in Research Notes.
