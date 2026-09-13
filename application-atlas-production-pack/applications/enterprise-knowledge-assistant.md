# Enterprise Knowledge Assistant

## Overview

An **Enterprise Knowledge Assistant** is an AI assistant operated by an organization for its own workforce, whose defining job is answering employees' questions with answers composed from the organization's own knowledge — the applications it uses and the content it has authored — rather than returning a list of documents or a human's reply.

The defining core is small:

```text
Organization-operated, workforce-facing assistant
└── The organization's own knowledge as the grounding corpus
    └── Natural-language question from an employee
        └── Composed grounded answer (commonly with source references)
```

Everything that makes modern products trustworthy and useful — permission-scoped retrieval, citations, verification states, knowledge-gap detection, multi-surface delivery, admin governance — is standard equipment in mature products, not part of the definition. A minimally configured deployment (a team's knowledge base with an ask surface and permission filtering) is still recognizably this Type.

When the center of gravity shifts to general work assistance — drafting, summarizing, analysis, and actions in systems, with answering as one capability among many — the product is drifting toward a different Application Type (Enterprise AI Assistant). When the deliverable becomes a results list over the estate, it is Enterprise Search territory.

## Users & Context

The primary user is an **employee** who needs an answer that depends on what their organization knows: a policy, a process, a decision, a document, a person to ask. Typical moments:

- "What's our refund policy for enterprise customers?"
- "How do I set up X in the system we use?"
- "What did we decide about this project, and where is it written down?"
- "Who owns this process, and where is the current procedure?"

The assistant is used across the workday — in a web app, inside the browser, in chat tools, on mobile — wherever the question arises. It is especially load-bearing for onboarding, cross-team questions, and anything where the answer lives in a tool the employee doesn't open every day.

Secondary users operate the system:

- **Administrators** connect knowledge sources, set policies, manage access, and monitor usage.
- **Knowledge owners / managers** maintain the corpus: verify content, answer verification requests, close knowledge gaps, and keep the answerable body current.

The organization itself is the customer: it provisions its people, administers the assistant, and governs what it may say and on what grounds.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being this Type:

- **Organization-operated, workforce-facing assistant.** The organization buys, provisions, and governs the assistant; the served population is its own employees acting in their work context. Without this, the product is consumer AI chat or a customer-facing bot.
- **The organization's own knowledge as the grounding corpus.** What the organization knows — its connected application estate (documents, messages, tickets, wikis) and/or its own authored and curated content — is assembled into one answerable body. The corpus defines what is answerable. Without this, the product is a general assistant with no enterprise grounding.
- **The composed grounded answer as the deliverable.** An employee asks in natural language; the system composes a direct answer from retrieved organization knowledge — not a results list, not a human reply. Without this, the product is enterprise search.

### Standard Capabilities of Mature Products

These make the assistant trustworthy and practical in real organizations. They are not what makes the product this Type, but mature products commonly carry most of them:

- **Permission-scoped grounding.** Answers draw only on content the asking employee may already access. A coworker with different permissions may get a different answer to the same question. Permission changes in the source systems are reflected in the assistant.
- **Source attribution.** Answers carry citations or references so the employee can verify what the assistant used before acting on it. When no sources are retrieved (for example, model-knowledge-only responses), citations are absent — which is exactly why organizations restrict that posture.
- **A knowledge-trust layer.** Content carries verification states — verified, unverified, deprecated — with accountable owners, review reminders, and audit trails. Employees can see who verified a document and when, before trusting an answer built on it.
- **A knowledge-gap loop.** Unanswered questions and demand signals surface as gaps; the organization closes them by authoring answers, generating or updating articles, and routing content to owners for review. The corpus improves because the assistant reveals where it is thin.
- **Multi-surface delivery.** A web app, a browser extension, integration into chat tools (team messaging), desktop and mobile apps; and increasingly an API or protocol supply of the same grounded knowledge to other AI tools the organization uses.
- **Conversation history and personalization.** Threads persist; results are shaped by the employee's own activity and access.
- **Admin and governance console.** Connector management, grounding policies, usage and adoption analytics, audit logs.
- **Search as a companion capability.** Results-list search over the same corpus lives beside the answer surface; the answer is the center, the lookup is the companion.

### One Structure, Many Implementations

The core is written conceptually. Common implementations vary:

```text
Concept:            The organization's knowledge as the grounding corpus
Implementations:    federated connectors over the application estate;
                    a native knowledge base; a hybrid of both

Concept:            Answer trust
Implementations:    permission mirroring from source systems; citations;
                    human verification states; audit trails

Concept:            The gap loop
Implementations:    authored Q&A entries; AI-drafted articles from
                    support tickets; verification task queues;
                    gap highlighting for owners
```

## How It Works

### Ground the assistant in the organization's knowledge

```text
Administrator connects knowledge sources (applications, drives, wikis,
ticketing systems) and/or enables the native knowledge base
→ content is indexed into one answerable body
→ access rules from the source systems carry over
→ administrators set the grounding posture
   (organization knowledge only, or additionally web / model knowledge)
```

The corpus is live: new and changed content flows in from the connected systems, and the organization's own access rules govern who can be answered from what.

### Ask and receive a grounded answer

```text
Employee asks a question in natural language
→ the assistant retrieves relevant content from the corpus,
   scoped to the employee's permissions
→ it composes a direct answer
→ it shows the sources used (and often who verified them)
→ the employee verifies, then acts — or asks a follow-up in the same thread
```

If the corpus cannot answer the question, the assistant says so — or, where the organization allows it, falls back to web or model knowledge, typically marked as such.

### Keep the corpus trustworthy

```text
Content owners verify documents (or answer verification requests)
→ verified content is badged and preferred
→ stale content is flagged, re-verified, or deprecated
→ unanswered questions and repeated asks surface as knowledge gaps
→ the organization closes the gaps: author answers,
   generate or update articles, route drafts to experts
→ the next question gets a better answer
```

This loop is what separates a maintained assistant from a chat box over a stale index: the product's own usage reveals where the organization's knowledge is missing or wrong, and the organization repairs it in place.

### Beyond answering

Most mature products extend the assistant with drafting, summarization, agents, and actions in connected systems. These capabilities vary widely in weight; the grounded answer remains the center that makes the product what it is.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Ask / chat surface

The primary entry surface.

- conversation thread with the assistant; suggested questions; grounding-source indicators
- primary actions: ask a question, attach or reference a document, filter which sources may be used, inspect the cited sources, continue the thread

### Answer detail / sources

The trust surface behind an answer.

- the composed answer, the source documents it drew from, verification badges, who verified and when
- primary actions: open a source, check verification status, report a wrong or outdated answer

### Search results

The companion lookup surface over the same corpus.

- results limited to the employee's permissions, verification badges on results
- primary actions: open a result, ask the assistant about it, save or share

### Knowledge management surface

The owner-side surface for corpus health.

- owned content across sources with verification states, verification task queues, gap reports
- primary actions: verify, request verification, deprecate, author or update content, review generated drafts

### Admin console

The operator-side surface.

- connected sources and their sync state, grounding policies, user and access administration, usage and adoption analytics, audit logs
- primary actions: add or remove connectors, set policies, manage models, inspect usage

### Embedded surfaces

The assistant inside the tools where work happens: browser extension, chat-tool integration (including proactive answering in channels in some products), mobile and desktop apps, and API/protocol access for other AI tools.

## Important Rules / Behaviors

### Permission scoping is the trust substrate

The assistant answers only from content the asking employee may access, mirroring the organization's own access rules. This makes the employee's permissions both a relevance filter and an access-control surface — and it means two employees can receive different answers to the same question, correctly.

### Citations are the verification mechanism

Answers are attributed to sources so employees can verify before acting. Organizations commonly restrict or flag ungrounded (model-knowledge-only) responses precisely because they cannot be checked this way.

### The corpus decays; the product fights the decay

Knowledge goes stale, duplicates, and contradicts itself. Mature products treat this as a first-class problem: verification states with owners and review cadence, staleness flagging, deprecation, and gap detection that turns unanswered questions into content work. An assistant over an unmaintained corpus produces confidently wrong answers — the failure mode these mechanisms exist to prevent.

### The assistant supports, not replaces, judgment

Products in this Type typically frame themselves as support for human decisions, with high-stakes operations (hiring, termination, compliance determinations) explicitly out of scope and governance machinery (guardrails, audit, policies) around everything else.

### Out-of-corpus behavior is a policy decision

What the assistant does when the organization's knowledge cannot answer — refuse, flag uncertainty, or fall back to web/model knowledge — is configured by the organization, not fixed by the Type.

## Variants

Common forms of the Type:

- **Standalone platform** — a dedicated product that connects the organization's application estate and serves the whole workforce (the enterprise-tier norm).
- **Suite-embedded** — the assistant ships inside a productivity or knowledge-management suite, grounded in that suite's estate plus connected third-party apps.
- **Knowledge-base-native** — the assistant grows out of a team knowledge base; the corpus is primarily authored content, with external sources connected around it (common in the SMB and mid-market tier).
- **Service-desk heritage** — deployments grown out of IT/HR self-service, where the knowledge corpus is fed by support-ticket mining and the gap loop is the operational center.
- **Grounding-posture variants** — organization-knowledge-only deployments (regulated or high-trust contexts) versus deployments that also allow web and model knowledge under admin policy.
- **Proactive variants** — assistants that listen in team channels and answer without being asked, alongside the reactive ask-and-answer loop.

A variant remains a variant unless it changes the served population or the deliverable: an external-customer deployment of the same machinery is a Knowledge Question Answering Application or a customer-service bot, not this Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Enterprise AI Assistant | closest sibling; shares the organization-operated, workforce-facing base. Seam is center of gravity: here, grounded answering from the organization's knowledge is the defining center; there, answering is one capability beside drafting, analysis, and actions. The same market products can carry both centers. |
| Knowledge Question Answering Application | shares the grounded-answer deliverable. Seam: there, an owner assembles and keeps current one bounded base and is accountable for answerability, for an owner-defined audience; here, the assistant grounds on the organization's live knowledge estate with trust bound to the organization's own access governance, for the workforce. |
| Enterprise Search Platform / Internal Knowledge Search | the grounding substrate. Search delivers results-first discovery over the estate; the assistant composes answers conversationally. Remove answer composition → search; remove the index → an assistant with no grounding. |
| RAG Development Platform | the developer-facing machinery (corpus of record, retrieval, generation binding, build surface) such assistants are built on. Here the user is an employee using a ready-made product; there, a developer building one. |
| Knowledge Base Application / Enterprise Wiki | the corpus and its authoring/ownership governance is the product's center there; question-time answering over the wider corpus is the center here. Knowledge-base-native assistants bundle authoring — packaging, not identity. |
| Customer Service Chatbot Platform | audience flip: external customers and conversation business (tickets, routing, handoff) vs internal workforce and knowledge answering. |
| AI Coding Assistant / Agent | domain-scoped specialization centered on the development workflow; vendors typically ship it as a separate product beside the knowledge assistant. |
| Business Intelligence Platform | governed analytics content is BI's center; assistants may consume BI as a data connection, but do not own the analytical model of record. |
| Intranet Platform | publishing and communication surface with search embedded; remove publishing, keep grounded answering → this Type. |

## Representative Products

- **Glean** — standalone work-AI platform; grounded answers with citations over a permission-scoped connected estate, with a verification and knowledge-management layer (enterprise tier)
- **Guru** — governed knowledge layer; structured, verified, continuously improved knowledge delivered as cited answers to people and AI tools (mid-market to enterprise)
- **Atlassian Rovo** — suite-embedded assistant grounded in the Atlassian estate plus connected apps, with search, chat, knowledge cards, and definitions
- **Moveworks** — workforce assistant with service-desk heritage; knowledge-gap detection and AI-generated, cited knowledge articles feeding self-serve answers (large-enterprise tier)
- **Slite (Ask)** — knowledge-base-native assistant for teams; verified docs, permission-filtered answers, gap highlighting (SMB tier)

## Sources

Research date: **2026-09-10**

- Glean — What is Glean?; How Glean accesses information; How Verification Works; Glean Documentation (help center) — https://help.glean.com/user-guide/about/what-is-glean , https://help.glean.com/user-guide/assistant/how-glean-accesses-info , https://help.glean.com/user-guide/knowledge/verification/how-verification-works , https://help.glean.com/en/
- Guru — How Guru Works; homepage — https://www.getguru.com/product/how-it-works , https://www.getguru.com/
- Atlassian Rovo — What is Rovo?; Rovo support resources — https://support.atlassian.com/rovo/docs/what-is-rovo/ , https://support.atlassian.com/rovo/resources/
- Moveworks — Knowledge Studio; homepage — https://www.moveworks.com/us/en/platform/ai-knowledge-management , https://www.moveworks.com/
- Slite — Ask product page — https://slite.com/ask

> Sourcing limitation: Guru, Moveworks, and Slite evidence is product-page tier (their help centers were not fetched on this date); statements drawn from them are positioning- and structure-strength, and no precise operational details (exact limits, defaults, pipeline internals) are asserted. Cross-pass corroboration (enterprise AI assistant, enterprise search, internal knowledge search, knowledge QA, and RAG development platform research notes, 2026-09-06 to 2026-09-08) was used for sibling boundaries and the pre-LLM historical anchor. Detailed evidence, product-by-product observations, and the cross-product comparison matrix are recorded in the paired Research Notes.
