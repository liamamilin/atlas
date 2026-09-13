# Research Notes — Enterprise Knowledge Assistant

## Research Goal

Understand the **Enterprise Knowledge Assistant** (§13, directory leaf `Enterprise Knowledge Assistant`) as an Application Type: what the product grounds on, what it delivers, how organizations trust and govern its answers, who uses it, and where its boundaries lie against the closest siblings — Enterprise AI Assistant (§13 sibling), Knowledge Question Answering Application (§02.03), Enterprise Search Platform / Internal Knowledge Search (§10/§13), RAG Development Platform (§13), and Knowledge Base Application / Enterprise Wiki (§02.06).

This pass must **discharge the forward joint-review flag** left by the enterprise-ai-assistant pass (2026-09-08): closest sibling — same market products serve both readings; seam = center of gravity (grounded answering from the organization's knowledge as the defining center vs general work assistance with answering as one capability); removal tests recorded both directions in research/enterprise-ai-assistant.md §Boundary Findings.

## Initial Boundary

Hypothesis before research: an Enterprise Knowledge Assistant is an organization-operated, employee-facing AI assistant whose defining job is answering questions from the organization's own knowledge — connected applications and/or its own curated content — with answers scoped by the organization's access rules and attributed to their sources. Nearest neighbors: Enterprise AI Assistant (general work assistance), Knowledge QA Application (owner-defined base), Enterprise/Internal Knowledge Search (results-first discovery), RAG Development Platform (developer machinery), KB Application (authoring center).

## Research Questions

1. What is the grounding corpus — one curated base, or the org's federated connected estate, or both?
2. What is the deliverable — a composed answer, a results list, or a human reply?
3. How does the organization trust the answers — permissions, citations, verification, gap-fixing?
4. What surfaces does the assistant appear on, and who operates it?
5. What does the assistant do beyond answering, and when does that drift toward the sibling Type?
6. Would pre-LLM or differently positioned products still fit the definition?

## Representative Products

Five poles, chosen for market representation, documentation quality, product philosophy, and customer tier:

| Product | Pole | Customer tier | Evidence tier |
|---|---|---|---|
| Glean | standalone work-AI platform, knowledge-grounding-centered | enterprise | Tier 1 (user guide, help.glean.com) |
| Guru | governed-knowledge-layer / KB-first trust | mid-market → enterprise | Tier 2 (product pages, getguru.com) |
| Atlassian Rovo | suite-embedded (knowledge-management vendor's estate) | enterprise | Tier 1 (support docs, support.atlassian.com) |
| Moveworks | service-desk heritage; knowledge-gap → article loop | large enterprise | Tier 2 (product pages, moveworks.com) |
| Slite (Ask) | SMB, KB-native assistant | SMB / small-mid | Tier 2 (product page, slite.com/ask) |

## Sources

Fetched 2026-09-10:

- Glean — https://help.glean.com/en/ (help center root), https://help.glean.com/user-guide/about/what-is-glean , https://help.glean.com/user-guide/assistant/how-glean-accesses-info , https://help.glean.com/user-guide/knowledge/verification/how-verification-works (Tier 1)
- Guru — https://www.getguru.com/ , https://www.getguru.com/product/how-it-works (Tier 2; help center help.getguru.com not fetched this pass)
- Atlassian Rovo — https://support.atlassian.com/rovo/ , https://support.atlassian.com/rovo/resources/ , https://support.atlassian.com/rovo/docs/what-is-rovo/ (Tier 1)
- Moveworks — https://www.moveworks.com/ , https://www.moveworks.com/us/en/platform/ai-knowledge-management (Tier 2; help.moveworks.com not fetched)
- Slite — https://slite.com/ask (Tier 2)

Cross-pass evidence re-used (marked as such where relied on):

- enterprise-ai-assistant.md (2026-09-08): Moveworks AI Assistant positioning ("individual permissions", surfaces, role model); Amazon Q Business / M365 Copilot / ChatGPT Enterprise observations for sibling-seam context.
- enterprise-search-platform.md (§Boundary Findings): "assistants ground in the search index; remove the index/ingestion layer → assistant with no enterprise grounding."
- internal-knowledge-search.md (§Boundary Findings): "Answers-first conversational product grounded in an index; remove the corpus assembly/permission layer → a chat product."
- knowledge-question-answering-application.md (§Boundary Findings #8 + historical anchor): KQA's proposed seam and the documented pre-LLM Q&A-pair anchor (Microsoft CQA).
- rag-development-platform.md (§Boundary Findings): "end-user product (chat over company knowledge for non-developers)."

## Product A — Glean (standalone work-AI platform)

### Key observations (Layer A unless noted)

- Self-definition (user guide): "Glean is your enterprise AI coworker. It connects to the apps and documents your company already uses. It understands who knows what, and helps you find answers, draft work, and move tasks forward without hunting across tools. Search is one of the jobs Glean is good at, but it's just one of many."
- Core help verbs: find information across connected apps ("results limited to what you already have permission to see"); **"Get grounded answers with citations. Ask in plain language and follow the sources, so you can verify what Glean used before you act on it"**; turn company knowledge into work product; find people/teams; work from tools you already use (browser, desktop, extension, Slack, MCP).
- "Think of Glean as a coworker who has read your company's documents and followed the conversations you can access."
- When to use: "when the answer depends on your company's knowledge or connected systems."
- Knowledge sources (Info access page): three combined per response — **company knowledge** (connected apps, permission-scoped, plus the user's own past chats/agent runs), **web knowledge** (real-time), **LLM knowledge** (pre-trained). Default "All Knowledge mode" auto-selects; per-query toggles (search the web / use company sources); both off = LLM-only, **no citations because no sources are retrieved**. Web search only if the administrator enabled it.
- Permission mirroring: "Glean respects the permissions set in your company's connectors... If your coworker has different permissions, they might see different results." Permission changes in connectors "reflected quickly." Personalization from the user's own activity.
- User-side corpus influence: collections (group related documents), **document verification** ("mark documents as verified to signal that they're authoritative and up to date"), attach documents (@-mentions/URLs).
- Verification machinery (dedicated docs section): verified = "personally approved by one of your users that it's accurate and up to date"; green badge on results with who-verified-and-when on hover; **verification tasks** queue (documents users requested verification on + re-verify reminders); "Your Content" view (all content you own across apps, filter unverified/verified/deprecated); request verification from a teammate; deprecate out-of-date documents.
- Knowledge-management layer: authored **Answers** (Q&A), collections, go links, pins, announcements, projects, home page.
- Assistant surface breadth (docs TOC): chat, real-time voice, deep research, file upload, canvas & artifacts, code, meeting notes, data connections (query BigQuery), memory & skills, library.
- Admin side (from EAA pass, corroborated by help-center structure): Admin Console — RBAC, SSO, connector management, search management (check a user's access to a document, hide content), GenAI setup, insights, audit logs, model management.
- Scope warning: "designed to support, not replace, human decision-makers" — high-risk operations excluded.
- Audience: "Anyone who works across multiple apps and needs company context to do their job."

## Product B — Guru (governed knowledge layer)

### Key observations (Layer A for positioning/structure claims; marketing figures excluded)

- Positioning: "The Governed Knowledge Layer for Enterprise AI." "Guru structures, governs, and continuously improves your company's knowledge—so every AI tool and every person gets answers they can trust."
- How-it-works, three phases:
  1. **Structure & strengthen knowledge** — "Guru indexes and transforms raw content into organized, verified, usable knowledge — automatically." Listed machinery: 100+ connectors, unified knowledge index, permission-aware ingestion, DLP masking, agent-generated documentation, deduplication & reconciliation, gap detection & auto-generation, key info extraction, AI-assisted authoring.
  2. **Govern & continuously improve** — "Knowledge decays the moment it's published. Stale content doesn't just produce bad answers — it produces confidently wrong answers at scale." Machinery: automated verification & maintenance, expert review workflows, auto-archival & cleanup, AI Training Center, "correct once, right everywhere", **citation enforcement**, answer transparency & reasoning, audit logs & lineage.
  3. **Power every workflow** — Knowledge Agent chat, guided conversations, deep research, MCP for AI tools & agents, Slack/Teams integrations, browser extension, Team Hubs, targeted announcements.
- Documented answer flow (product-page walkthrough): question ("What's our refund policy for enterprise customers?") → "Permissions checked · scoped to employee role" → "Pulling 3 relevant sources" → "Primary source identified · Enterprise Refund Policy · Verified by Sarah" → composed answer → "3 sources · View reasoning details".
- Trust framing as the product's center: "Your AI is quoting documents nobody verified" (homepage problem statement); security strip: permission-aware AI, full audit trails, citations on every answer, enterprise SSO, DLP built in, configurable guardrails.
- Knowledge Agents (2026 positioning): "Knowledge Agents now improve your info, not just find it" — agents that verify/unverify, flag stale content, draft updates, route to experts. Marketing stats (adoption %, accuracy %) observed but excluded from all claims.
- Solutions taxonomy: Knowledge Management Automation, Enterprise AI Governance, Workplace AI Chat & Research, Enterprise AI search, Agentic Knowledge Base, Team Hubs — the vendor itself straddles KB/search/assistant vocabulary.

## Product C — Atlassian Rovo (suite-embedded)

### Key observations (Layer A)

- Definition (support docs): "Rovo is a new app that helps you turn information into action... features that accelerate finding, learning, and acting on information across your Atlassian and third-party apps." Three pillars: **Find** (Search across data, tools, platforms incl. third-party apps), **Learn** ("Explore your company's data more deeply through AI-driven insights, knowledge cards, and Chat"), **Act** (specialized agents).
- Org-operated evidence: "To turn on Rovo, your organization admin must be on a verified business domain"; credits included in paid Jira/Confluence/Service Collection/Teamwork Collection subscriptions; org-admin manages connectors.
- Rovo Search: "combines results from your Atlassian apps (like Jira and Confluence) with connected third-party apps (like Google Drive and Slack). **Rovo respects your user permissions, so users can only see what they already have access to.**"
- Rovo Chat: "engage in interactive conversations to ask questions, generate new ideas, get helpful feedback... **Chat is based on your company's data (from both Atlassian and connected third-party apps), but only uses content you have access to.**" Accessible within Jira, Jira Service Management, Jira Product Discovery, Confluence, plus browser extension; also Slack app, Teams app, mobile app, desktop.
- **Definitions** (knowledge-card surface): "When you've come across some company jargon or a project you've never heard of, Rovo can help you find out what it means. Rovo searches across your company knowledge to find the right definition specific to your context." Users can add/edit definitions.
- Agents: AI-powered virtual teammates; knowledge sources configurable for subagents; agent permissions and governance; verified agents; Rovo Studio as the builder home.
- Family boundary stated by the vendor: **Rovo Dev** (coding agent: CLI, IDE, code reviews) is documented as a separate product line under the Rovo brand — domain-scoped specialization consistent with the AI Coding Assistant seam.
- Chat modes: Think deeper, Deep research, memory management — assistant-depth variants.

## Product D — Moveworks (service-desk heritage)

### Key observations (Layer A for product-page claims; operational detail not asserted)

- Positioning: "The AI Assistant platform for your entire workforce to search and act across business applications." ServiceNow acquisition closed (vendor announcement).
- Estate: "Instantly find user-generated content across systems (Slack, OneDrive, Google Drive, SharePoint, Confluence, Outlook, and 50+ others)"; surfaces: "chat, web, intranet, portals, and mobile"; 100+ languages claim (marketing figure).
- **Knowledge Studio** (the knowledge-center module): "Supercharge your employees' ability to self-serve answers to common questions by generating knowledge articles based on your unique enterprise context and data." Machinery: generate content (mines support tickets, extracts agent notes → "grounded articles"); **find knowledge gaps** ("AI article recommendations based on real employee demand"); pinpoint knowledge updates (overlap detection with existing articles); **citations** ("Generated articles include full citations to the source material"); article-level analytics; enterprise grounding; content library.
- The loop: employee demand → gap detection → AI-generated grounded articles with citations → self-serve answering → article analytics. Knowledge maintenance is part of the product, not just ingestion.
- Related modules: Enterprise Search ("search for knowledge, files, and data across all of your business applications — all from one place"), AI Assistant, Agent Studio, Employee Experience Insights.
- From EAA pass (re-used, marked): AI Assistant "personalizes responses with business context and individual permissions"; role model includes **Knowledge Managers** (Knowledge Studio) as a first-class admin audience; FedRAMP; ITSM/HR tier-1-resolution heritage.

## Product E — Slite (Ask) (SMB, KB-native)

### Key observations (Layer A for product-page claims)

- Positioning: "Stop searching, start asking. Get instant answers from trusted company info and all the connected apps, right where you need them."
- Corpus: native knowledge base + "connects your knowledge base with the external sources of your choice."
- Trust: "Trust without second-guessing. Filter the sources to make sure that you can trust the answers with verified docs." "Ask works only with your data, securely separated from everyone else's." "Based on your access only: Just like a regular search, Ask accesses only those docs you can view, filtering team workspace content by your permissions."
- Answer-first framing: "'No result matches your search' is not an answer. Yet, the info lives somewhere in your knowledge base. Our AI-powered assistant will surface the info and cross-check your sources to give the accurate answer, in an instant."
- Gap loop: "Identifies the gap: Ask not only answers questions but also highlights knowledge gaps. If an answer seems wrong or outdated, check the sources to update any missing information."
- Proactive answering: "Slite listens to the conversations in your Slack channels and automatically answers them straightaway, even without being triggered."
- Surfaces: web app, Chrome extension, Slack. Hints (suggested questions from team content); multi-language ask/answer.
- Broader positioning: "The self-maintaining knowledge base your team and agents can trust" — Slite Agent (self-maintaining KB); MCP listed in footer.
- Customer quotes frame value as onboarding speed and fewer repeated questions (SMB-scale concerns).

## Cross-product Comparison

| Dimension | Glean | Guru | Rovo | Moveworks | Slite Ask |
|---|---|---|---|---|---|
| Operator | the organization (tenant, admin console) | the organization | the organization (verified business domain, org admin) | the organization (platform deployment) | the organization (team workspace) |
| Served population | workforce ("anyone who works across multiple apps") | workforce (teams: support, HR, IT, sales...) | workforce (Atlassian cloud users) | "your entire workforce" | team members (SMB) |
| Grounding corpus | connected apps, permission-scoped + own chats | connected sources transformed into verified knowledge + native cards | Atlassian apps + connected third-party apps | 50+ systems + generated KB articles | native KB + connected apps |
| Deliverable | grounded answers with citations | composed answers, citations enforced, reasoning shown | conversational answers, knowledge cards, definitions | self-serve answers; grounded cited articles | composed answers referencing sources |
| Permission scoping | explicit ("results limited to what you already have permission to see") | permission-aware ingestion; "scoped to employee role" | "only uses content you have access to" | "individual permissions" (EAA pass) | "accesses only those docs you can view" |
| Trust machinery | verification badges, verification tasks, deprecation | verification workflows, citation enforcement, audit logs & lineage | definitions editable, agent verification | citations on generated articles, gap analysis | verified docs, source filtering, gap highlighting |
| Gap → corpus loop | verification tasks, answers (authored Q&A) | gap detection & auto-generation, agent-drafted updates | definitions add/edit | Knowledge Studio (demand-driven article generation) | gap identification → update sources |
| Surfaces | web, desktop, extension, Slack, MCP | chat, extension, Slack/Teams, MCP, Team Hubs | in-suite (Jira/Confluence/JSM), extension, Slack/Teams, mobile, desktop | chat, web, intranet, portals, mobile | web, extension, Slack |
| Beyond answering | drafting, agents, canvas, deep research, voice | guided conversations, deep research, announcements | agents, Studio, Act pillar | agents/plugins, actions, comms broadcast | proactive Slack answering, Slite Agent |
| Admin/governance | Admin Console (RBAC, connectors, insights, audit) | governance automations, audit logs | org admin, agent governance, credits | Moveworks Setup, EX Insights | workspace permissions |
| Distinct flavor | widest assistant surface; knowledge layer beside it | trust/governance as the product's center | suite-embedded; definitions surface | service-desk heritage; demand-driven article generation | SMB simplicity; proactive answering |

### Cross-product commonalities (Layer B)

1. **Organization-operated, workforce-facing**: every product is bought/provisioned/administered by the organization and served to its own employees. No consumer or external-customer mode at the center.
2. **The org's own knowledge as the grounding corpus**: connected application estate and/or native/curated content, assembled into one answerable body. All five.
3. **Composed grounded answers as the deliverable**: natural-language question in → direct answer composed from retrieved org knowledge, with source references. All five. None centers on returning a results list (search exists as a companion capability).
4. **Permission-scoped grounding**: answers draw only on content the asking employee may access; permission changes mirrored. All five (Moveworks via EAA-pass evidence).
5. **Answer-trust machinery**: citations/source attribution universal; verification states (Glean, Guru, Slite), audit/lineage (Guru), editable knowledge cards (Rovo).
6. **Knowledge-gap → corpus-improvement loop**: unanswered/demand signals drive content creation or updates (Guru gap detection, Moveworks Knowledge Studio, Slite gap identification, Glean verification tasks/answers).
7. **Multi-surface delivery**: web app + browser extension + chat tools (Slack/Teams) at minimum; desktop/mobile common; API/MCP supply of the same knowledge to other AI tools (Glean, Guru, Slite, Rovo ecosystem).
8. **Admin & governance layer**: connectors, policies, analytics, audit — all five at some depth.
9. **Capabilities beyond answering exist in most** (drafting, agents, actions) — but their weight varies widely; the knowledge-answer center is the constant.

### Where products differ (variant axes)

- Corpus composition: federated connected estate (Glean, Moveworks, Rovo) vs native KB (Slite, Guru partially) vs hybrid — a spectrum, not a split.
- Corpus governance depth: passive index (index the mess as-is — Guru's own critique of "enterprise search alone") vs active transformation (dedupe, reconcile, verify, generate).
- Trust machinery depth: badges (Glean) → enforced citations + lineage (Guru) → simple verified-docs filter (Slite).
- Deployment substrate: standalone platform vs suite-embedded vs KB-native.
- Beyond-answering weight: minimal (Slite) ↔ wide assistant (Glean, Moveworks, Rovo).
- Grounding posture: enterprise-only vs +web vs +model knowledge (admin-configurable where documented — Glean toggles/admin gate).
- Proactivity: reactive Q&A vs proactive answering in channels (Slite) vs nudges (Moveworks, EAA pass).
- Answer-machinery era: LLM retrieval+generation is the current norm; pre-LLM extractive/Q&A-pair forms are the historical anchor (see Historical Check).

## Canonical Abstraction

### L0 — Defining Invariant

An Enterprise Knowledge Assistant is **an organization-operated, workforce-facing AI assistant whose defining job is composing grounded answers from the organization's own knowledge**.

Three jointly-held structures; remove any one and it is a different thing:

1. **Organization-operated, workforce-facing** — the organization provisions its people, administers the assistant, and governs its use; the served population is its own employees acting in their work context. Remove → consumer AI chat (outside the atlas) or a customer-facing knowledge bot (KQA external pole / Customer Service Chatbot territory).
2. **The organization's own knowledge as the grounding corpus** — what the organization knows (its connected application estate and/or its own authored/curated content), assembled into one answerable body; the corpus defines what is answerable. Remove → a general AI assistant with thin grounding (Enterprise AI Assistant) or ungrounded chat.
3. **The composed grounded answer as the deliverable** — employees ask in natural language; the system composes a direct answer from retrieved organization knowledge — not a results list, not a human reply — commonly with source references. Remove → Enterprise Search / Internal Knowledge Search (results-first discovery).

Jointly-held load-bearing:

- 1 alone = the Enterprise AI Assistant core (general work assistance).
- 2 alone = the enterprise-search/knowledge-index substrate (ESP/IKS territory).
- 3 without 1+2 = an answer engine / generic QA surface.
- 1+3 without 2 = a chatbot with no enterprise grounding.
- 2+3 without 1 = the Knowledge Question Answering Application core (owner-defined base, owner-defined audience).

Note on the "AI" leg: the current market realization is LLM retrieval+generation, but the L0 deliberately does not require LLMs, connectors, chat widgets, or embeddings — see Historical Check.

### L1 — Common Mature Structure

Present in essentially all mature current products; not required to recognize the Type:

- **Permission-scoped grounding** — answers draw only on content the asking employee may access; permission changes in source systems mirrored into the assistant.
- **Source attribution** — answers carry citations/references so employees can verify before acting.
- **Knowledge-trust layer** — verification states (verified/unverified/deprecated), accountable content owners, review/re-verify cadence, audit trails.
- **Knowledge-gap loop** — unanswered questions and demand signals surface as gaps; content creation/update machinery (authored answers, generated articles, verification tasks) closes them.
- **Multi-surface delivery** — web app, browser extension, chat tools (Slack/Teams), desktop/mobile; API/MCP supply of the same grounded knowledge to other AI tools.
- **Conversation history & personalization** — persistent threads; results personalized by the employee's own activity and access.
- **Admin & governance console** — connector management, policies, usage/adoption analytics, audit logs.
- **Search as companion capability** — results-list search over the same corpus beside the answer surface.

### L2 — Variant / Optional Structure

- Corpus composition: federated connected estate ↔ native KB ↔ hybrid (KB-ownership pole).
- Corpus governance depth: passive indexing ↔ active transformation (dedupe/reconcile/verify/generate).
- Grounding posture: enterprise-only ↔ +web ↔ +model knowledge (admin-configurable).
- Beyond-answering weight: answering-only ↔ drafting/agents/actions (drift toward Enterprise AI Assistant).
- Native authoring/KB tooling (drift toward Knowledge Base Application).
- Proactive answering (listening in channels, auto-answering, nudges).
- Deployment substrate: standalone platform / suite-embedded / KB-native / service-suite module.
- Compliance posture: data residency, regulated-industry authorization.
- Answer-machinery era: retrieval+generation ↔ extractive/Q&A-pair (pre-LLM).

### L3 — Vendor-specific (research notes only)

- Glean: All Knowledge mode + per-query toggles; verification tasks / Your Content; go links; collections; authored Answers; Gleaniverse/Academy; BigQuery data connections; memory & skills.
- Guru: Knowledge Agents (verify/unverify, draft updates, route to experts); quality automations; "correct once, right everywhere"; AI Training Center; guided conversations; Team Hubs; DLP masking; deduplication & reconciliation.
- Rovo: Definitions (AI-generated company jargon/project definitions, user-editable); knowledge cards; Find/Learn/Act pillar framing; credits; Rovo Dev as a separate product line; Studio; verified agents.
- Moveworks: Knowledge Studio (ticket-mined article generation with citations); Reasoning Engine; Agent Studio; Employee Experience Insights; Knowledge Managers as an admin role; ServiceNow acquisition; FedRAMP.
- Slite: Slite Agent (self-maintaining KB); Ask hints (suggested questions); proactive Slack answering without being triggered; verified-docs source filter.

## Vendor-specific Findings

(See L3; none promoted to the canonical model. Closest calls: permission-scoped grounding and citations are universal in the sample but kept in L1 — a minimally-configured deployment without formal verification workflows is still recognizable as this Type, consistent with the IKS pass's treatment of trust machinery; the knowledge-gap loop is universal in the sample but a deployment can run without it.)

## Rejected Findings

- "Knowledge assistant = a RAG pipeline product" — rejected: the RAG machinery is the developer-facing substrate (RAG Development Platform); the assistant is the end-user product built on such machinery.
- "Knowledge assistant = enterprise search with a chat box" — rejected: the deliverable differs (composed answer vs results list); search is a companion capability, and the ESP pass itself recorded the assistants-ground-in-the-index relationship.
- "Corpus must be a single curated base" — rejected: the federated connected estate is the dominant modern composition; the curated base is one pole (and the KQA seam, not a requirement).
- "Verification workflows are definitional" — rejected: universal in the mature sample but a minimal deployment without them remains recognizable; kept in L1.
- "Suite-embedded vs standalone is a Type boundary" — rejected: deployment substrate is a variant axis (Rovo vs Glean serve the same core).

## Boundary Findings

1. **vs Enterprise AI Assistant (§13 sibling — JOINT REVIEW DISCHARGED from this side).** The sibling's proposed seam holds: center of gravity, not feature presence. The knowledge assistant is centered on grounded answering from the organization's knowledge — the corpus and the composed answer are the defining center; the enterprise AI assistant is centered on general work assistance — answering is one capability beside drafting, summarizing, analysis, and actions in systems. Removal tests confirmed both directions: strip drafting/actions/general chat → the knowledge assistant remains (Guru, Slite are nearly answering-only); strip the knowledge-corpus center (keep general assistance with thin grounding) → the enterprise AI assistant remains. **Refinement ratified from this side**: the sibling's phrase "corpus + answer trust as the product" is realized as — corpus in L0, answer trust (permissions, citations, verification) as the universal L1 trust layer rather than a definitional invariant, consistent with the IKS pass's treatment. Glean is the convergence pole: one product carrying both centers; the seam stays a center-of-gravity judgment. The EAA pass's removal tests are hereby discharged.
2. **vs Knowledge Question Answering Application (§02.03 — discharges KQA pass advance flag #8).** KQA's proposed seam ("EKA = employee-facing conversational assistant; KQA = answering from the owner-defined base with the improvement loop as the accountability structure") is **confirmed with refinement**. The retained discriminators: (a) corpus structure & accountability — KQA's owner assembles and keeps current one bounded base and is accountable for answerability via the improvement loop; EKA grounds on the org's live federated estate (and/or native content) with trust bound to the org's own access governance rather than a single owner's curation loop; (b) audience — KQA's audience is owner-defined (external customers/community/internal pole); EKA's audience is the workforce by definition; (c) surface framing — KQA is a QA application (the answer about a domain is the product); EKA is a persistent personal work surface (conversation history, personalization, multi-surface). Removal tests: give the EKA product a single owner-curated base with an owner improvement loop and an owner-defined external audience → KQA; give the KQA internal deployment the org's federated estate with permission mirroring and a persistent assistant surface → EKA. Overlap zone recorded: internal-audience KQA deployments (company-brain class) and KB-native EKA products share the corpus-composition axis; the seam above is what keeps them distinct.
3. **vs Enterprise Search Platform / Internal Knowledge Search (§10/§13 — corroborates both passes).** Search returns results-first discovery over the estate; the assistant composes answers conversationally. The ESP pass's sentence is ratified from this side: assistants ground in the search index — ESP/IKS are the grounding substrate; remove the index/ingestion layer → an assistant with no enterprise grounding; remove answer composition → the substrate. The IKS pass's "convergence watch" is answered: the corpus layer is shared machinery, the delivery model is the seam.
4. **vs RAG Development Platform (§13 — corroborates that pass).** End users vs developers: the RAG platform is the developer-facing machinery (corpus of record, retrieval, generation binding, build surface); the assistant is the ready-made product employees use. No build surface is exposed to the EKA's end user.
5. **vs Knowledge Base Application / Enterprise Wiki (§02.06).** The KB/wiki's center is content authoring/publishing/ownership governance; the assistant's center is question-time answering over the (wider) corpus. KB-native EKA products (Slite, Guru) bundle authoring — packaging, not identity; consistent with the KQA pass's boundary #2 and the KB pass's Guru straddle note.
6. **vs AI Coding Assistant / AI Coding Agent (§12).** Domain-scoped specialization: the coding assistant is centered on the development workflow. Vendor-internal evidence this pass: Atlassian documents Rovo Dev (CLI/IDE/code reviews) as a separate product line beside Rovo Chat/Search — the same vendor splits the domain-scoped assistant from the knowledge assistant.
7. **vs Customer Service Chatbot Platform (§07).** Audience test: external customers vs internal workforce. No sampled EKA product centers on external customers; external-facing deployments of the same machinery belong to the KQA/chatbot Types.
8. **vs Business Intelligence Platform (§13).** Discharged from the EAA pass: in-BI AI features are BI capabilities; assistants may consume BI/warehouses as data connections (Glean BigQuery connection observed this pass), but governed analytics content remains BI's center.
9. **vs Intranet Platform (§10).** Publishing/communication surface with search embedded vs answering center; remove publishing/communication, keep grounded answering → this Type.
10. **Consumer AI chat** — no directory leaf; fails the org-operated leg.

## Historical / Market-Sample Check

Question: would older, regional, platform-native, or differently positioned products still fit the L0? Yes:

- **Pre-LLM anchor (cross-pass, documented)**: the KQA pass's documented Microsoft CQA anchor shows the Q&A-pair era — auto-extracted question-answer pairs from the organization's own material, multi-stage ranking for answer selection, confidence scores, active learning — no generation step required. An internal deployment of that machinery (org-operated, employee-facing, org knowledge as the base, composed/selected answer as the deliverable) satisfies the EKA L0 without LLMs.
- **Pre-LLM extractive-answer form**: enterprise search products of the late-2010s shipped natural-language answer surfaces (extractive answers with source links) over the corporate index — the IKS pass's pre-AI workplace-search calibration supports keeping generation out of the L0.
- **Platform-native form**: a suite-embedded assistant grounded in the vendor's own productivity/knowledge estate (Rovo in Atlassian; the M365 Copilot pattern from the EAA pass) satisfies the core without any standalone-platform machinery.
- **SMB form**: a small team's knowledge base with an ask surface, verified docs, and permission filtering (Slite) satisfies the core without enterprise admin machinery.
- Nothing era-specific enters L0: no LLM, no RAG specifics, no connectors count, no chat widget, no embeddings, no MCP, no cloud delivery. The current LLM-grounded-with-citations realization is recorded as the dominant modern implementation (L1/L2), not the definition.

## Uncertainties

1. **Guru and Moveworks evidence is product-page tier** (help centers not fetched this pass): operational workflow depth (exact verification flows, exact article-generation pipeline) not asserted; all Guru/Moveworks statements in the final doc are positioning/structure strength.
2. **Slite evidence is product-page tier**: verification mechanics and permission-filtering depth kept at positioning strength.
3. **Grounding-posture distribution** (enterprise-only vs +web vs +model knowledge) documented at Glean (admin-gated web, toggles) and via the EAA pass (Q Business admin setting, Copilot policy); distribution across the market unknown; phrased as variance.
4. **Regional forms** (e.g., Chinese-market enterprise knowledge assistants) not sampled; no regional claims made.
5. **The KQA seam is now held from both sides** (KQA pass advance flag + this pass) — the refinement (corpus accountability + audience + surface framing) should be visible to taxonomy maintainers; recorded in STATUS.
6. **Marketing figures** (connector counts, adoption %, accuracy %, language counts) observed but excluded from all claims.

## Final Synthesis

The Enterprise Knowledge Assistant is the organization's own answering assistant: bought and operated by the organization, served to its workforce, grounded in what the organization knows, and delivering composed answers — not result lists, not human replies — to employees' natural-language questions. The defining core is the triad **organization-operated × workforce-facing × grounded answering from the organization's knowledge**. Everything that makes modern products trustworthy and useful — permission-scoped retrieval, citations, verification states, gap-detection loops, multi-surface delivery, admin governance — is the mature market's standard equipment (the trust layer), not the definition. The Type sits between its siblings: the Enterprise AI Assistant shares the org-operated/workforce-facing base but centers on general work assistance; the Knowledge QA Application shares the grounded-answer deliverable but centers on an owner-defined bounded base with owner accountability; Enterprise Search/Internal Knowledge Search supply the grounding substrate but deliver results, not answers; the RAG Development Platform is the developer machinery such assistants are built on. The seam with the Enterprise AI Assistant — the closest sibling — is center of gravity, and the market's convergence pole (one product carrying both centers) is acknowledged rather than resolved away.
