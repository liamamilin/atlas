# Conversation Intelligence Platform

## Overview

A **Conversation Intelligence Platform** captures an organization's customer-facing conversations — sales calls, video meetings, and in several products email — as recordings, converts them into machine-readable transcripts, and turns the accumulated corpus into searchable, analyzable, org-scale insight.

Its purpose is to make what was actually said in customer conversations visible and usable at the level of the team and the organization: for reviewing individual conversations, for understanding how the team talks to customers, and for reading market signals out of the collective voice of customers. The corpus assembles itself as a byproduct of normal selling — conversations are captured automatically through integrations with the telephony, web-conferencing, and calendar tools the organization already uses — so the platform becomes the system of record for the organization's conversations while the CRM remains the system of record for customers and deals.

The defining core is deliberately small: **a captured conversation of record, a machine transcript, derived conversation signals computed over the corpus, and org-scale access to and aggregation of that corpus.** Everything else commonly associated with these products — CRM sync, AI summaries, scorecards, deal-risk alerts, live in-call guidance — is standard machinery that mature products add, not what makes the Type.

## Users & Context

The platform serves a selling organization rather than an individual:

- **Sales representatives** review their own calls to prepare for the next conversation, study what worked, share moments with colleagues, and let the platform handle logging and follow-up drafting.
- **Sales managers** work the corpus at team scale: inspecting how reps handle objections and discovery, finding coachable moments, and comparing individuals against team patterns.
- **Enablement and onboarding teams** build libraries of exemplary calls — objection handling, demos, best practices — from real conversations.
- **Revenue operations and leadership** use aggregate dashboards to understand conversation patterns, adoption of new messaging or methodologies, and deal risks surfaced from what buyers said.
- **Product and marketing stakeholders** read recurring themes — competitor mentions, pricing pushback, feature requests — out of the customer voice the corpus aggregates.

The work context is a B2B sales or revenue organization whose conversations happen on phone systems and web-conferencing platforms. The platform is not where conversations happen; it is where they are captured, understood, and revisited afterward.

## Core Model

### The conversation of record

The central object is the **captured conversation** — a specific recorded interaction with external parties, held as a persistent record with participants, timing, the communication channel it came from, and (in most implementations) an association to the CRM account, deal, or contact it concerns. Conversations enter without manual authorship: the platform integrates with phone systems and conferencing tools, and in typical implementations also reads the calendar to know which meetings to join or record. Conversations that could not be recorded still appear as records with metadata in most products — a meeting without a recording is a known state, not an absence.

### The transcript

Every captured conversation becomes a **speaker-attributed machine transcript**. The transcript is the substrate on which everything else rests: it is synced to the audio so a reader can jump from any line to that moment, it is searchable, and it feeds the analysis layer. Transcription quality tooling — custom vocabularies for product and company terms, language detection, translation for cross-language teams — is a standard part of mature products.

### Conversation signals

On top of the transcript, the platform computes **derived signals** configured to the organization's priorities:

- **Tracked words and concepts** — lists of terms, and increasingly AI-defined concepts that match meaning rather than literal phrasing ("asks for a discount" matching "is that the best you can do?"). Organizations define trackers around what matters to them: competitor names, pricing objections, required disclosures, new-message adoption. A conversation mentioning a tracked concept is findable as such, and its occurrences can be counted across the corpus.
- **Conversation metrics** — structural properties of how people talked: talk-time balance between rep and customer, question rate, longest monologue, call volume and duration. These are computed per conversation and aggregated per person and team.
- **Topics and themes** — recurring subject areas detected or defined across many conversations, with prevalence and time-spent views.
- **AI summaries and extractions** — per-conversation summaries, action items, and follow-up drafts generated from the transcript.

Signals are organization-configured rather than fixed: two companies on the same product track different things, because trackers encode each business's strategy, messaging, and compliance obligations.

### The corpus and its access surfaces

The whole collection of conversations is a **queryable corpus**. Search spans participants, accounts, words spoken, tracked concepts, and meeting attributes, and searches can be saved and turned into standing collections that notify when new matching conversations arrive. Alongside search sit **libraries and folders** — personal and organization-wide — where exemplary calls and snippets are curated for training and reuse. Access to the corpus is permission-scoped; a rep normally sees their own conversations, a manager their team's, with organization-wide visibility governed by configuration.

### Aggregate insight

The corpus is aggregated into views that no single conversation can provide: team dashboards over conversation patterns, rep-versus-peer comparisons, adoption tracking for strategic initiatives, trend lines for tracked concepts (including market-level concerns surfacing in customer conversations), and deal- or account-level roll-ups of what was said across every conversation touching that opportunity.

### The CRM seam

Conversations are auto-associated with CRM accounts, deals, and contacts, and call outcomes are logged back to the CRM. The direction of ownership matters: the CRM remains the record of the customer relationship and the deal; the platform owns the conversation corpus itself. Several products extend from conversation analysis into deal-inspection and forecasting territory, but those are expansions beyond the conversation layer.

## How It Works

### Configure capture

An administrator connects the organization's telephony, web-conferencing, and calendar/email systems, and defines the capture scope: whose conversations are recorded, which meeting types are eligible, and how recording consent is obtained and announced. Consent configuration is region-sensitive; products support modes from simple announcement to requiring agreement before recording starts.

### Capture as a byproduct of selling

Once configured, capture is automatic: eligible meetings are identified from the calendar and recorded either natively through the conferencing platform or by a recording participant that joins the meeting; phone conversations are recorded on the telephony side. Nothing is manually authored. Capture can and does fail in operationally visible ways — a recording participant not admitted to the meeting, a participant declining consent, recording disabled mid-call — and mature products record these outcomes so managers can see why a conversation is missing, not just that it is.

### Process into a record

After a conversation ends, the platform transcribes it, attributes speakers, runs its analysis — tracked concepts, metrics, topics, summaries — and places the resulting conversation record in the corpus, associated with the right accounts, deals, and people.

### Work a single conversation

A rep or manager opens the conversation record: plays the recording with the transcript beside it, jumps to moments by clicking transcript lines, highlights and comments on specific moments, cuts snippets to share, reads the AI summary and action items, and drafts follow-up. This is the review-and-feedback loop that made the category — the conversation becomes a durable, shareable artifact instead of a memory.

### Work the corpus

Across conversations, users search and filter to answer questions ("all calls last quarter where a competitor was named", "discovery calls by this rep"), save those searches, organize exemplars into libraries, and receive notifications when new conversations match standing criteria.

### Aggregate and act

Managers and leaders read the aggregate surfaces: team conversation patterns, tracker adoption against goals, emerging themes, market-level trend lines, and deal-risk signals. These views feed coaching priorities, enablement content, messaging decisions, and deal intervention — the reason the organization captures conversations at all.

## Interfaces

### Conversation library / search

The corpus entry surface: lists and filters conversations by participant, account, spoken words, tracked concepts, and time. Saved searches and standing collections live here. Primary actions: search, save criteria, open a conversation, curate into folders or libraries.

### Conversation detail page

The single-conversation surface and the heart of the product: recording player with synced, clickable transcript; speaker attribution; summary, action items, and topics; tracked-concept occurrences; per-moment comments, snippets, and sharing; privacy and deletion controls. This is where reps self-review and managers leave feedback.

### Dashboards

Team- and rep-level aggregate views: conversation volume and duration, talk-time and question-rate patterns, topic and tracker prevalence, score distributions where scoring is used, and platform-engagement metrics (what the team listens to and comments on). Primary actions: filter, compare individuals, drill from an aggregate into the underlying conversations.

### Initiative and market views

Where offered: boards tracking adoption of a messaging or methodology initiative via tracked concepts against goals, and trend views showing how often concepts appear in customer conversations over time, linked back to the underlying calls.

### Deal and account views

Conversation-derived signals arranged around the CRM entities: what was said across every conversation on a deal, risk and staleness alerts, and roll-ups of stakeholder sentiment where the product provides it.

### Capture administration

Admin surfaces for integrations, who and what is recorded, consent modes and announcements, retention, and privacy. Capture-outcome reporting (why conversations were not recorded) commonly lives near these or near team dashboards.

## Important Rules / Behaviors

- **Capture is governed, not automatic in the unqualified sense.** An admin defines the scope of recording; consent requirements gate whether a recording starts; a required consent that is refused prevents capture even when a recording participant is manually invited.
- **Capture failure is a first-class state.** Conversations that failed to record appear as records with a reason — participant declined consent, recording participant not admitted, recording disabled — because a manager's first question about a missing call is "why".
- **The transcript is the substrate.** Analysis features (trackers, topics, summaries, search) operate on the transcript; custom vocabularies exist to improve recognition of company-specific terms.
- **Signals encode strategy.** Tracked words and concepts are defined per organization; the same product implementation tracks different things at different companies. Insight surfaces are therefore always relative to what the organization chose to track.
- **Two systems of record, clearly split.** The platform owns the conversation corpus; the CRM owns customer and deal data. Conversations link to CRM entities and log activity back, but the platform does not become the deal record system unless it expands into revenue-intelligence territory.
- **Access follows role and configuration.** Reps see their own conversations; managers see their teams; organization-wide libraries and permissions are configured. Conversations can be marked private, and deletion and retention controls exist because the corpus contains sensitive customer speech.
- **Privacy machinery is structural.** Consent modes, recording announcements, and (in some products, particularly regulated industries) automatic removal of sensitive information from recordings or transcripts are part of the core operating model, not add-ons.

## Variants

- **Standalone conversation-intelligence product** — the corpus and its insight surfaces as the whole product, typically for sales organizations.
- **Module of a revenue or engagement suite** — the same conversation layer embedded alongside dialing, sequencing, deal management, and forecasting; commercially bundled, structurally the same corpus machinery.
- **Real-time emphasis** — extends the analysis into the live call: guidance cards, objection help, and knowledge answers surfaced during the conversation, strongest in inside-sales and contact-center settings.
- **Contact-center tuning** — the same capture-and-analysis machinery aimed at service populations, typically alongside quality-management scoring of agent interactions; adjacent to the contact-center Types listed below.
- **Notetaker-adjacent products** — capture-first products aimed at individual meeting records that add analytics layers and drift toward this Type; the distinguishing question is whether the product centers one meeting or the organization's corpus.

## Related Application Types

| Application Type | Distinction |
|---|---|
| AI Meeting Assistant | Serves the individual participant's single meeting — record, summary, notes, action items for immediate use. This Type centers the organization's corpus of many conversations and the aggregate insight drawn from it. Products span the gradient; the primary object differs. |
| Meeting Recording & Transcription Application | Provides the recording and verbatim transcript for later human use. This Type computes derived, organization-configured signals over the transcript corpus and aggregates it. |
| Sales Call Coaching Platform | Same capture-and-analysis machinery, different end product: the managed seller-development loop (evaluations, feedback routing, tracked coaching progress). Conversation intelligence's end product is org-scale understanding of conversations and market; coaching modules exist inside it, and analytics exist inside coaching products — the boundary is the primary job. |
| Revenue Intelligence Platform | Consumes conversation signals as inputs to a revenue model over deals (inspection, projection). This Type's end product is the conversation corpus's meaning; the revenue platform's is the revenue picture. |
| Sales Dialer | Places record-bound outbound calls; conversation intelligence analyzes the recordings those calls produce. Suites bundle both, but placing and analyzing are different jobs. |
| Call Center Platform / Cloud Contact Center | Operates the calling itself — routing, queues, agent states. Conversation intelligence may ingest its recordings but does not run the operation. |
| Contact Center Quality Management | Evaluates support-agent interactions against service-quality and compliance criteria with calibration workflows. Shares evaluation machinery; different population and purpose. |
| Support Conversation Analytics | The conversation-analytics family applied to support/service conversations and service-operations questions; this Type's canonical center is the sales/revenue conversation corpus. |
| Sales Intelligence Platform | External data about companies, contacts, and intent for prospecting; conversation intelligence captures what happens inside the organization's own conversations. |
| Business Intelligence Platform | Generic dashboards over arbitrary data sources; this Type is conversation-native — it captures, transcribes, and analyzes the corpus it reports on. |

## Representative Products

- Gong — the category archetype; conversation intelligence expanded into a broader revenue platform
- Jiminny — standalone conversation and revenue intelligence for mid-market revenue teams
- Salesloft (Conversation Intelligence) — the conversation layer embedded in a sales engagement and revenue platform
- Balto — the same conversation machinery tuned to contact centers with real-time guidance emphasis

## Sources

Research date: **2026-09-07**

- Gong Help Center — https://help.gong.io/ (Understanding call recording; View a call transcript; Understanding trackers; Find and organize conversations; Get started with team insights and initiatives; Market)
- Jiminny — https://www.jiminny.com/ , https://www.jiminny.com/product/conversation-intelligence , https://help.jiminny.com/en/ (platform collections; Understand why meetings and calls are not recorded)
- Salesloft — https://salesloft.com/platform/conversation-intelligence-software
- Balto — https://balto.ai/

> Sourcing limitation: ZoomInfo Chorus (a major category product) could not be fetched from the research environment (product pages returned access errors) and contributed no structural evidence. Salesloft was evidenced at product-page level only; its help center was not machine-readable. Claims resting on those sources were excluded or kept generic. Precise vendor-specific details (filter counts, package names, consent-mode labels) are kept in the Research Notes rather than stated here.
