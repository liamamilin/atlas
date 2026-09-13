# Internal Knowledge Search

## Overview

An **Internal Knowledge Search** application gives an organization's members one place to search and ask questions across the organization's own knowledge — documents, wiki pages, knowledge-base articles, policies, question-and-answer threads, and knowledge captured from work tools — and delivers what it finds as source-linked results or answers that cite where they came from, under the organization's access rules.

Its defining structure is small:

```text
Organization's knowledge corpus (authored in the product and/or gathered from its tools)
  → assembled into one searchable body
    → one member-facing query surface (search / ask)
      → grounded delivery: a result that opens the source, or an answer that cites its sources
```

Everything else commonly associated with current products — AI-generated answers, verification badges and trust signals, browser extensions and chat-tool delivery, agent interfaces, knowledge-gap analytics — is a widely expected capability of mature products, not part of what makes the product one of these. The earlier, pre-AI form of this software — workplace and intranet search products that connected several knowledge sources into one permission-aware search page — satisfies the same defining structure without any of those additions.

The boundary to watch: when the corpus widens from knowledge content to the organization's whole estate — email, business records, transactions, people — and the mission becomes everyday discovery of *anything*, the product becomes an **Enterprise Search Platform**. When the corpus shrinks to a single system's contents with its built-in search box, it is that system's feature, not this application.

## Users & Context

**Primary users — members of the organization as askers.** Any employee who needs an answer or a document to do their work: a support agent checking a policy before replying to a customer, an engineer looking for a runbook, a new hire trying to find how things work, a sales rep pulling together account context. Typical situations:

- asking a question in natural language ("what's our refund policy for annual plans?") instead of guessing which tool holds the answer
- re-finding a document seen before without remembering which system it lives in
- checking whether the answer they found is current and trustworthy
- getting answers where they already work — in the chat tool, in the browser — rather than visiting a portal

**Knowledge owners and subject-matter experts** are the second essential role: they author knowledge natively where the product offers authoring, and they are accountable for keeping knowledge items current — reviewing, verifying, correcting, and archiving. In several products this accountability is explicit: a named reviewer or team per knowledge item, with review reminders.

**Administrators (IT / knowledge operations)** connect sources, manage what enters the corpus and who may see it, configure the trust and quality machinery, and monitor usage and gaps.

**AI agents** are an emerging consumer class: current products commonly expose the same corpus to agents and custom integrations through APIs and agent protocols, with the same access rules applied.

The context is daily knowledge work. The query surface is deliberately brought to where members already are — a search box in a web app, a browser extension, a command inside the chat tool — because the value collapses if finding knowledge requires remembering where it lives.

## Core Model

### The defining core

```text
Knowledge sources        the organization's tools and systems, plus knowledge authored in the product
  → Corpus assembly      content, metadata, and access information gathered into one searchable body
    → Query surface      one search/ask entry point for members
      → Grounded delivery  source-linked results, or answers citing the sources behind them
```

Four properties. Removing any one changes the product into a different kind of software:

- **Internal knowledge corpus.** The searchable domain is the organization's own knowledge content — documents, wiki pages, KB articles, policies, procedures, Q&A threads, knowledge extracted from chat and work activity. Not the public web; and centered on knowledge rather than on transactional business records. Without this, the product is a web search engine or a generic app search.
- **Multi-source assembly.** The corpus is gathered from more than one source: authored and curated natively, ingested from connected tools, or both. This is what separates the application from any single wiki's or knowledge base's built-in search — a feature of that system rather than an application in its own right.
- **One member-facing query surface.** A single search/ask entry point through which members query the whole corpus at once, instead of running separate searches in each tool. Without it, the product is just a document store.
- **Grounded delivery.** What the member receives leads back into the corpus: a result that opens the source document in its home system, or an answer that cites the specific sources that shaped it. Without grounding, the product is an unanchored chatbot or a link dump, and its answers cannot be checked.

### Standard capabilities of mature products

These capabilities appear across the researched products. They make the application practical and trustworthy; a product remains recognizable as this Type without some of them.

- **Source connections.** Prebuilt integrations for common knowledge sources (wikis, cloud drives, docs tools, chat, ticketing) plus a path to connect custom systems. Administrators scope what is synced (spaces, folders, channels), monitor sync status, and re-authorize connections; content, metadata, and access information flow into the corpus together, and sources are re-checked continuously or on a schedule.
- **Native knowledge authoring** (in corpus-owning products). A knowledge base inside the product — articles, cards, Q&A, organized into collections, spaces, or boards — so part of the corpus is authored and curated directly rather than only indexed from elsewhere.
- **AI answers with citations.** The current flagship delivery: the member asks a question, and the product composes an answer grounded in the corpus, citing the specific documents it drew from. Mature products commonly keep the plain results list as a parallel form — some automatically choose between the two based on whether the query looks like a question or a document hunt.
- **Knowledge-trust machinery.** Trust states on knowledge items (verified / unverified / unreviewed), an accountable reviewer or owner per item, optional review cadences, and trust signals displayed next to results and inside answers — so the member can see at a glance whether knowledge is current, who stands behind it, and how recently it was confirmed. In several products this extends to automated quality agents that review content against usage feedback and content analysis, flag or retire stale knowledge, and log their decisions for human oversight.
- **Trust-ranked delivery.** Verified and recently confirmed knowledge commonly ranks ahead of unverified or stale material; some products also let administrators restrict what the answer engine may use (for example, verified content only).
- **Access control over the corpus.** What a member can find is governed by configured access rules — either inherited from the source systems (a document visible in search only to those who could open it at the source) or managed in the product itself through groups, roles, and scoped spaces. Current products commonly extend the same rules to third-party agents querying on a member's behalf.
- **In-workflow surfaces.** The query capability travels: a browser extension that answers from all connected sources (sometimes reading the page being viewed), a command in the team chat tool, alongside the web app.
- **Knowledge-gap detection.** The question stream is itself an instrument: unanswered and repeatedly asked questions, stale-content flags, and usage analytics show owners where the corpus is thin or drifting out of date, feeding the maintenance loop.
- **Agent and API supply.** The same corpus is exposed programmatically — APIs and agent-protocol servers — so coding assistants and custom agents can search and read the organization's knowledge under the same access rules.
- **Search mechanics.** Filtering by source, time, author, and tags; semantic and hybrid retrieval; autocomplete and query suggestions.

### One structure, many implementations

The core model is written in conceptual terms; concrete products realize each concept differently:

```text
Concept:  corpus assembly
Realized as:  native authoring + connectors (corpus-owning products)  /  connectors alone (search-native products)  /  native Q&A + connectors (Q&A-native products)

Concept:  delivery form
Realized as:  cited AI answer  /  source-labeled results list  /  both, auto-selected by query intent

Concept:  access model
Realized as:  permissions inherited from source systems  /  product-scoped groups and roles  /  scoped workspaces — products commonly support more than one

Concept:  trust machinery
Realized as:  trust signals on delivery only  /  verification states with accountable reviewers  /  plus automated quality agents with decision logs
```

A reader who has only seen one implementation — say, a team knowledge base with an AI answer bar — should still be able to recognize a connector-only search product or a Q&A-native knowledge layer as the same Type.

## How It Works

### 1. Assemble the corpus

An administrator connects the organization's knowledge sources: selecting a system, authenticating (in some products via a dedicated service account, so the connection survives personnel changes), scoping what will be synced — particular spaces, folders, channels, or sites — and choosing who may access the connected content. In parallel, teams author knowledge natively where the product offers it: articles, cards, answers to recurring questions, organized into collections or spaces with named owners. The corpus is therefore partly a mirror of the organization's tools and partly a curated body in its own right.

### 2. Keep it current

Connected sources are re-checked continuously or on a schedule; new, changed, and removed content flows into the searchable copy, together with the access information needed to decide who may see it. Sync status and indexing progress are visible to administrators, and failures raise notifications. The searchable copy always lags the sources by the sync interval — freshness is a configuration outcome, not an absolute.

### 3. Ask and search

A member types a question or keywords into the search bar — in the web app, the browser extension, or the chat tool. The product interprets the query, retrieves across the assembled corpus, and delivers: a composed answer with citations to the documents that shaped it, a ranked list of source-labeled results, or both. Each result identifies its source system and opens there; the corpus copy stays read-only for connected content. The member filters (by source, time, author, tag), opens the underlying documents, and — where the trust layer is present — sees a trust signal telling them how reliable each item is considered to be.

### 4. Keep the knowledge trustworthy

This is the loop that distinguishes the population's current discipline from plain search. Knowledge items carry trust states and accountable reviewers. Reviewers confirm or correct items on a cadence or on demand; any member can flag a problem. Where automated quality machinery exists, agents review content on a recurring schedule against usage signals (feedback, views) and content analysis (dates, time-sensitive claims), automatically confirming healthy content, flagging or retiring stale content, and logging each decision with its reasoning for human oversight. Gap detection closes the loop from the demand side: unanswered and repeated questions, and stale-content flags, tell owners exactly where to write or fix knowledge next. Some products go further and watch the organization's tools for changes that make existing knowledge wrong, draft the correction, and route it to the right expert for approval.

### 5. Supply the agents

The same corpus, access rules, and trust signals are exposed to AI agents through APIs and agent-protocol servers, so an assistant inside a code editor or chat tool can answer from the organization's knowledge — citing sources and respecting permissions — instead of from general training data.

```text
The operating loop:

connect sources + author knowledge → corpus assembles and stays in sync
        ↓                                   ↑
members ask and search → grounded, trust-signaled answers/results
        ↓                                   ↑
gaps and staleness detected → owners verify, fix, archive → corpus improves
```

## Interfaces

### Search / ask bar

The primary entry surface, in the web app and replicated in work tools.

- Purpose: capture a question or query from any work context.
- Typical information: suggested questions and recent items while typing.
- Primary actions: ask a question, run a keyword search, pick a suggestion.

### Answer surface

The cited-answer experience.

- Purpose: deliver a grounded answer, not just links.
- Typical information: the answer text, citations linking to the specific source documents, trust signals on the cited knowledge, follow-up suggestions.
- Primary actions: open a cited source, verify the answer's basis, ask a follow-up, rate the answer.

### Results list

The document-hunting experience.

- Purpose: present ranked, source-labeled results across the corpus.
- Typical information: title, snippet, source system, owner/author, last-modified, trust state where present; filter panel (source, time, author, tags).
- Primary actions: open the result in its source system, refine with filters, share.

### Knowledge base / content browse

The corpus-owning surface, where the product is also the home of curated knowledge.

- Purpose: browse and maintain the native knowledge body — collections, spaces, boards, Q&A.
- Typical information: organized knowledge items with owners, trust states, review dates, related items.
- Primary actions: read, author or edit (for entitled roles), verify or flag, comment.

### Content detail

A single knowledge item, wherever it lives.

- Purpose: show the knowledge with its full context.
- Typical information: content body, author, owner/reviewer, verification state and history, source-system origin for connected items, usage feedback.
- Primary actions: open at source, verify/unverify (reviewers), flag a problem, comment.

### Admin console

The operational surface.

- Purpose: connect and govern the corpus.
- Typical information: connected sources with sync status and indexing progress, access configuration per source, verification/quality settings and decision logs, gap and usage analytics, audit logs.
- Primary actions: add or re-authorize a source, scope content and access, configure trust and quality automation, review gaps and analytics.

### Agent / API surface

The programmatic face of the same corpus.

- Purpose: let custom applications and AI agents query the organization's knowledge.
- Typical information: search and retrieval endpoints; agent-protocol servers exposing search, read, and sometimes verification actions.
- Primary actions: authenticate, query, receive cited results under the caller's access rules.

## Important Rules / Behaviors

### Access is governed by configuration, and the mechanism varies

Access to results follows rules the organization configures — but this population implements that principle in more than one way. Commonly a product supports permissions inherited from the source systems (search shows a document only to those who could open it at the source, and source-side changes propagate back) alongside product-scoped access (groups, roles, or scoped workspaces managed inside the product, independent of source-system permissions). The practical consequence: in some deployments the search layer can expose content more broadly than the source tool's seat structure would — a deliberate choice organizations make, not an accident. Because of this variance, the access model of a specific deployment is a governance decision to check, not an assumption to make.

### The searchable copy lags the sources

Connected content is reflected as of the last sync. Brand-new or just-deleted material may not yet be consistently represented; removal in particular can take effect only after the next sync cycle. Freshness depends on the cadence configured per source.

### Trust states inform — and sometimes gate — delivery

By default, unverified or unreviewed knowledge remains searchable; trust signals tell the member what to rely on. But trust state can also affect what the answer engine uses: some products let administrators restrict answering to verified content, and verified knowledge commonly ranks ahead of stale or unreviewed material. Trust machinery changes ranking and (optionally) availability — it does not change access permissions.

### Editing knowledge can reset its trust

In products with verification workflows, an edit by someone other than the accountable reviewer may flip the item to unverified pending review — a deliberate safeguard, where present, so that changes to knowledge re-enter the trust loop rather than silently inheriting the old endorsement.

### The source system stays authoritative for connected content

For ingested material, the home system remains the system of record: editing, deleting, and re-sharing happen there and flow back through sync. For natively authored knowledge, the product itself is the record. A deployment therefore mixes two authorities, and which parts of the corpus fall on which side is a consequence of the corpus-ownership model the organization chose.

### Provenance is always shown

Whether the delivery is a result or a composed answer, the member can see where the knowledge came from — the source system and document for results, the cited documents for answers. This is the property that makes the answers checkable, and it holds even when the consumer is an AI agent.

## Variants

- **Corpus-owning (knowledge-base-native) products** — the product is also the home of curated knowledge: native authoring, owners, verification workflows, with connected sources extending the corpus around that core. Team and mid-market deployments commonly take this shape.
- **Search-native products** — a pure lens over the organization's existing tools; no native authoring; value lies in connector breadth, retrieval quality, and the answer layer. Enterprise deployments commonly take this shape.
- **Q&A-native products** — the corpus grows out of question-and-answer practice: questions with accepted answers as the primary knowledge unit, extended with capture from chat and docs and trust signals inherited from community curation.
- **Team-scale vs enterprise-scale** — team products emphasize simplicity and per-user pricing; enterprise products add SSO, granular role-based access, audit, compliance certifications, data residency, and AI guardrails.
- **SaaS vs self-hosted** — most products are cloud services; open-source products offer self-hosting for data-control-sensitive organizations, with the AI model pluggable.
- **Trust-machinery depth** — from trust signals on delivery only, through verification states with accountable reviewers, to automated quality agents with decision logs and drift detection that drafts corrections for expert approval.
- **Scope breadth** — centered on knowledge content, but commonly extending into connected business applications (tickets, deals, tables); the broader the scope, the closer the product sits to the enterprise-search family.

A variant stops being this Type when it loses the defining core: a search scoped to one system's contents is that system's built-in search; an answering chatbot with no corpus behind it is a chat product; a corpus with no query surface is just a knowledge base.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Enterprise Search Platform | The closest sibling, and the most consequential boundary. Both assemble multiple internal sources into one searchable body behind one query surface. The difference is center of gravity: this Type centers on the organization's knowledge content and on answering knowledge questions, and carries the knowledge-trust discipline (verification, owners, trust-ranked delivery) as a central structure; an Enterprise Search Platform centers on the whole organizational estate — including email, business records, and people — and on everyday discovery of any content, with curation as an optional layer rather than a discipline. The same product can legitimately serve both roles; the populations overlap heavily. |
| Knowledge Base Application | Authors and publishes knowledge content for later use; its built-in search covers its own contents. This Type is the discovery-and-answer layer over a multi-source corpus. A knowledge base with an answer bar that also searches other tools has become this Type. |
| Enterprise Wiki | Collaborative authoring and publishing surface; search is a feature of the wiki. Same separator as the knowledge base: single-system contents vs multi-source corpus. |
| Intranet Platform | Communication and content publishing for the organization, with search embedded in it; this Type is the knowledge-discovery layer, not the communication layer. |
| Enterprise Knowledge Assistant | An answers-first conversational product; when grounded in an assembled, permission-aware corpus it is essentially this Type's answer surface (or sits directly on top of it). Without the corpus and access layer it is a chat product. The two are converging in the current market. |
| Search Platform (developer infrastructure) | Search technology for developers building search into arbitrary applications; no organizational knowledge corpus implied. Swap the org-knowledge corpus for arbitrary applications and this Type becomes that one. |
| Help Center | Knowledge published for external customers; this Type serves internal members over internal knowledge. Audience flip. |
| eDiscovery | Legal investigation over organizational content with holds, exports, and chain of custody for a legal team; this Type is everyday knowledge discovery for everyone. Purpose and user flip. |
| General Web Search Engine | Searches the public web under an ad model with no organizational access rules. Scope and audience flip. |

The boundary with **Enterprise Search Platform** deserves emphasis because the two describe overlapping products: every product researched for this Type also satisfies the enterprise-search structure. The honest reading is that this leaf names the knowledge-centered emphasis of the same family — knowledge content, question-answering, and knowledge trust — rather than a structurally separate kind of software. Organizations choosing between them are choosing scope and emphasis, not category.

## Representative Products

- **Guru** — corpus-owning, governance-first pole: native knowledge cards plus connected sources, verification with accountable reviewers and automated quality agents, answers delivered in chat tools and the browser.
- **Glean** — search-native, enterprise pole: connects the organization's SaaS estate into one searchable body with a combined search-and-assistant bar and a curation layer.
- **Onyx** — open-source, self-hosted pole: connectors assemble the corpus, with parallel search and chat surfaces and pluggable AI models.
- **Slite** — team knowledge-base pole: an AI knowledge base that owns verified docs, ranks verified knowledge first in its answers, and drafts maintenance fixes for expert approval.
- **Stack Internal (formerly Stack Overflow for Teams)** — Q&A-native pole: trusted knowledge built on question-and-answer practice, with trust signals on every answer and expert-validation workflows.

The defining core was deliberately checked against the pre-AI form of this software — workplace and intranet search products that connected several knowledge sources into one permission-aware search page — to avoid defining the Type by the current AI-answer implementation.

## Sources

Research date: **2026-09-07**

- Guru — product page: https://www.getguru.com/ ; Help Center: https://help.getguru.com/ ; "How Sources Work in Guru": https://help.getguru.com/docs/linking-sources-for-guru-answers ; "How Content is Verified in Guru": https://help.getguru.com/docs/verifying-and-unverifying-cards
- Onyx — documentation: https://docs.onyx.app/ ; "RAG and Search": https://docs.onyx.app/overview/core_features/internal_search
- Slite — product page: https://slite.com/ ; AI Search: https://slite.com/ai-search
- Stack Internal — overview: https://stackoverflow.co/teams/ ; features: https://stackoverflow.co/internal/features/
- Glean — connectors, search, and security documentation: https://docs.glean.com/connectors/about ; https://docs.glean.com/user-guide/search/how-to-search-in-glean ; https://docs.glean.com/security (fetched 2026-09-06 during the Enterprise Search Platform research pass and re-used for this leaf)

> Sourcing limitations: Slite and Stack Internal evidence is limited to official product and feature pages (their help centers were not fetched), so product-specific operational details for those two are kept at positioning strength. Glean evidence was fetched one day earlier during the sibling Enterprise Search Platform pass and is reused rather than re-fetched. Precise operational parameters that vary by product and configuration (sync cadences, file-size limits, review-interval options, edition gating of permission features) are intentionally not stated in this document; they are recorded, where documented, in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis — including the relationship to the Enterprise Search Platform research — are recorded in the paired Research Notes.
