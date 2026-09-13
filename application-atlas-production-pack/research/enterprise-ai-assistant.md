# Research Notes — Enterprise AI Assistant

## Research Goal

Understand what an Enterprise AI Assistant actually is as an Application Type: what the organization buys and operates, what employees do with it, what structures exist inside it, how work flows through it, and where its boundaries sit against the dense cluster of neighboring AI Types in §13 (Enterprise Knowledge Assistant, agent platforms, gateways, governance) and against adjacent Types in other sections (enterprise search, knowledge QA, customer-service chatbots, coding assistants, BI).

## Initial Boundary

Working hypothesis at start:

- It is an organization-operated, workforce-facing, conversational AI assistant — the "front door" product employees use, not the infrastructure underneath it.
- Nearest neighbors: Enterprise Knowledge Assistant (§13 sibling, unprocessed), Enterprise Search Platform / Internal Knowledge Search (§10, processed — noted as "grounding substrate" for assistant leaves), Knowledge Question Answering Application (§02.03, processed), Customer Service Chatbot Platform (§07, processed), AI Coding Assistant/Agent (§12, processed), Agent Development Platform (§13, processed), Business Intelligence Platform (§13, processed — its pass flagged this leaf with a "light flag": in-BI AI features are capabilities of BI).
- Known risk: the market straddles this leaf heavily with Enterprise Knowledge Assistant (same products, e.g. Glean, serve both readings). The seam must be center-of-gravity, not feature presence.

## Research Questions

1. What is the minimal structure that makes a product an Enterprise AI Assistant (vs consumer AI chat, vs a scripted chatbot, vs a search tool)?
2. Who operates it and who uses it? What roles exist (end user, admin, agent builder, knowledge manager, program owner)?
3. What does the assistant draw on (company knowledge, web, model knowledge) and how are permissions enforced?
4. What can it do beyond answering (drafting, summarizing, actions in connected systems, agents, proactive nudges)?
5. How is it governed (admin console, policies, model management, usage analytics, audit)?
6. Where does it sit relative to: enterprise search (substrate?), knowledge QA (narrower?), agent platforms (builder vs user?), BI (capability vs product?), customer-service chatbots (audience?), coding assistants (domain scope?)?
7. Historical check: do pre-LLM enterprise assistants (NLU-era virtual agents, platform-native productivity assistants) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Microsoft 365 Copilot | platform-native, suite-embedded | largest enterprise distribution; assistant embedded in productivity apps; rich IT-pro docs |
| Glean | standalone "work AI" platform | the pure-play enterprise-assistant platform; excellent Tier-1 user + admin docs |
| Amazon Q Business | cloud-provider assistant | AWS-hosted assistant with explicit admin/user/system workflow docs; also a market-exit data point |
| Moveworks | service-automation-first / agentic | IT/HR-support heritage grown into a workforce-wide assistant platform; now ServiceNow-owned |
| ChatGPT Enterprise | model-vendor general-purpose tier | boundary specimen (general assistant + enterprise admin); NOT directly documented this pass |

## Sources

Fetched 2026-09-08 (all successful unless noted):

- Microsoft Learn — Microsoft Copilot documentation hub: https://learn.microsoft.com/en-us/microsoft-365-copilot/
- Microsoft Learn — "What is Microsoft Copilot?": https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
- Glean — "What is Glean?" (user guide): https://docs.glean.com/user-guide/about/what-is-glean
- Glean — "How Glean accesses information": https://docs.glean.com/user-guide/assistant/how-glean-accesses-info
- Glean — "About the Admin Console": https://docs.glean.com/administration/about
- Glean — docs home (structure): https://docs.glean.com/ ; marketing home: https://www.glean.com/
- AWS docs — "What is Amazon Q Business?": https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html
- AWS docs — "How Amazon Q Business works": https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/how-it-works.html
- Moveworks — home: https://www.moveworks.com/ ; AI Assistant product page: https://www.moveworks.com/us/en/platform/ai-assistant
- FAILED: https://openai.com/chatgpt/enterprise/ (timeout ×2 on 2026-09-08) — ChatGPT Enterprise kept as market anchor only; no operational claims drawn from it.

Evidence layers used below: **A** = directly observed on the cited official page of a specific product; **B** = cross-product commonality across the sampled set; **C** = canonical inference from comparison + boundary reasoning.

## Product A — Microsoft 365 Copilot (platform-native, suite-embedded)

### Key observations (Layer A unless noted)

- Positioning (IT-pro docs): "Plan, implement, and manage Microsoft Copilot Chat and Microsoft Copilot in your organization." The doc is written for admins, not consumers.
- All experiences powered by: LLMs for natural-language understanding/generation; grounding in web and/or organizational data (Microsoft Graph, Work IQ); **access scoped by user permissions** ("security and compliance enforced").
- Three license experiences on one assistant: Copilot Chat (Basic) — enterprise AI chat grounded in web data, org content only when explicitly provided (upload, open content in Teams/Outlook, or pay-as-you-go agents); Microsoft 365 Copilot (Basic) — standard access to in-app Copilot; Microsoft 365 Copilot (Premium) — full experience with automatic organizational grounding via Microsoft Graph + Work IQ (emails, files, meetings, calendars, teams, organizational relationships), Copilot Search, semantic indexing.
- In-app assistance enumerated per app: Word (draft/rewrite/summarize), Excel (analyze data, insights, formulas, visuals), PowerPoint (create/summarize/edit presentations), Outlook (draft emails, summarize threads, tone coaching), OneNote (draft plans/ideas/lists), Teams (summarize and transcribe meetings, capture action items), Forms (draft questions).
- Agents: "scoped or focused versions of Microsoft Copilot that act as AI assistants and can automate business processes"; agent lifecycle managed by admins; Copilot Studio is the separate low-code builder ("Agents let you customize your organization's Copilot experience").
- Cowork (Premium, usage-billed): "carries out tasks across your Microsoft 365 environment on your behalf."
- Admin layer: Copilot Control System — pin Copilot Chat across experiences, control image generation, manage agent creation/use, web-search grounding policy, remove user access entirely; dedicated AI Administrator role (least-privilege, no Global Admin needed).
- Governance/compliance: Enterprise Data Protection (EDP) for prompts and responses "by the same contractual terms... as their emails in Exchange and files in SharePoint"; EU Data Boundary; Microsoft Purview classification/labels/leak prevention/prompt-response review; SharePoint Advanced Management + restricted content discovery to reduce oversharing into Copilot's data sources.
- Usage reports: total/daily active users, prompts submitted, per-user engagement (7/30/90/180-day views); "organizational messages" to drive adoption.
- Model selection: Auto / Quick response / Think deeper via a real-time router; Anthropic available as an opt-in subprocessor in applicable licensed experiences.
- Family boundary stated by the vendor itself: GitHub Copilot ("an AI coding assistant... licensed by your work organization") and Microsoft Security Copilot are **independently licensed separate products** — i.e., the vendor treats domain-scoped assistants as separate products from the general enterprise assistant.
- Entry points require **work identity**: "instruct them to sign in with their Microsoft Entra account"; personal-account (MSA) entry points listed separately as the consumer surface; tenant restrictions control personal sign-in.

## Product B — Glean (standalone work-AI platform)

### Key observations (Layer A unless noted)

- User-guide self-definition: "Glean is your enterprise AI coworker. It connects to the apps and documents your company already uses. It understands who knows what, and helps you find answers, draft work, and move tasks forward without hunting across tools. **Search is one of the jobs Glean is good at, but it's just one of many.**" — the vendor itself demotes search to a capability.
- What it helps do: find information across connected apps (results limited to what you already have permission to see); grounded answers with citations; turn company knowledge into work product (draft updates, summaries, plans, follow-ups); find the right people/teams; work from tools you already use (browser, desktop app, extension, Slack, MCP).
- Explicit scope warning: "Glean is designed to support, not replace, human decision-makers. Our systems are not intended to perform high-risk operations, such as evaluating learning outcomes, or performing employment activities (for example, hiring, promotion, or termination)."
- Audience: "Anyone who works across multiple apps and needs company context to do their job" — support, sales, operations, product, engineering, people teams.
- Knowledge model (Info access page): three sources combined per response — **company knowledge** (connected apps, permission-scoped, plus the user's own past chats/agent runs), **web knowledge** (real-time), **LLM knowledge** (pre-trained). Default "All Knowledge mode" auto-selects sources; per-query toggles (search the web / use company sources); both off = LLM-only, no citations. Web search only if the administrator enabled it.
- Permission mirroring: "Glean respects the permissions set in your company's connectors... If your coworker has different permissions, they might see different results." Permission changes in connectors "reflected quickly." Personalization from the user's own activity.
- User can improve results: collections, document verification ("mark documents as verified to signal that they're authoritative"), attach documents (@-mentions/URLs).
- Assistant surface breadth (docs TOC): chat, real-time voice/audio, deep research, file upload, canvas & artifacts, code, meeting notes, data connections (query BigQuery in the assistant), memory & skills, library.
- Knowledge-management layer: answers (authored Q&A), collections, verification, go links, pins, announcements, projects, home page.
- Agents: first-class docs section — how agents work, templates, create agents; admin side: manage agent library, access & governance, agent identity.
- Admin Console (self-serve "central hub"): RBAC (Full Admin / Setup Admin / content-moderation permissions), SSO via IdP, search management (check a user's access to a document, hide content), connector management (add/remove/adjust permissions), GenAI setup (chat/answers/summarization), adoption tracking (invited vs active), insights (assistant/LLM/agents/MCP), audit logs, Protect (sensitive findings, AI security), model management (supported LLMs, configure, default model, exclude/restrict models, region-scoped open models, deprecation), tools/MCP servers/A2A, API tokens, branding, maintenance windows.
- Platform claims on marketing home (Layer A as *claims*, not verified facts — excluded from final doc): 40+ LLMs, 275+ connectors, uptime, adoption/hours-saved figures.
- MCP posture: Glean exposes itself as an MCP server so other AI clients can use company context; also consumes remote MCP servers as tools.

## Product C — Amazon Q Business (cloud-provider assistant)

### Key observations (Layer A unless noted)

- Definition: "a fully managed, generative-AI powered assistant that you can configure to answer questions, provide summaries, generate content, and complete tasks based on your enterprise data... end users receive immediate, **permissions-aware responses from enterprise data sources with citations**, for use cases such as IT, HR, and benefits help desks."
- Also: "create and share task automation applications, or perform routine actions like submitting time-off requests and sending meeting invites."
- Admin workflow (documented step-by-step): connect workforce identity (IAM Identity Center / identity federation) → create the application (auto-generates the web experience) → add users/groups and **provision user subscriptions** ("Only an admin can create and upgrade user subscriptions") → enhance (data sources, admin-level controls, chat relevance tuning, plugins, chat features incl. Amazon Q Apps) → customize web experience (title, subtitle, welcome message, quick prompts) → share the web-experience URL with subscribed users.
- User workflow: sign in at the organization's web-experience URL → ask questions (answers generated from enterprise data the user has access to) → verify cited sources → conversation history (retained 30 days, resumable) → summarize email threads → create outlines/drafts → **plugin actions** ("ask Amazon Q Business to perform actions on your behalf, like creating a ticket in a supported third party app") → guardrails/chat controls → Amazon Q Apps (task-focused apps created from a conversation).
- Out-of-scope behavior: "Sometimes your question requires information that's beyond the scope of your enterprise data. Then, Amazon Q Business responds that it couldn't find an answer in your documents, **unless your admin has allowed** Amazon Q Business to generate responses using model knowledge." — grounding posture is an admin configuration.
- System workflow: retriever (admin-chosen) selects/retrieves relevant documents "following authorization and access control" → generation from enterprise data only or enterprise data + model knowledge (admin-configured) → response returned with a unique message ID for tracking.
- Hallucination mitigation: checks supported chat responses for inconsistencies and corrects in real time.
- Delivery surfaces: web experience, browser extensions, apps for Slack/Teams/Office, embed API into custom apps/websites; **anonymous applications** for public-facing scenarios (explicitly a different audience — boundary pole).
- Pricing model: user subscriptions + index capacity (structure observed; numbers not asserted).
- Market note: "Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick." — the product is being superseded; evidence remains valid for the Type's structure.

## Product D — Moveworks (service-automation-first / agentic)

### Key observations (Layer A unless noted)

- Positioning: "The AI Assistant platform for your entire workforce to search and act across business applications." / "Search and action in one. Most assistants stop at search."
- AI Assistant: "personalizes responses with business context and **individual permissions**, routing requests to the right applications and learning continuously from each interaction"; powered by a "Reasoning Engine" that "understands intent, nuance, and your organization's unique workflows"; "autonomously understands, plans, executes, and adapts to complete any request."
- Action layer: "Linked to thousands of action plugins that turn intent into results"; unifies "hundreds of enterprise systems under one intelligent layer" (Workday, Coupa, ServiceNow, Salesforce named); proactive nudges for recurring/time-sensitive tasks.
- Surfaces: "chat, web, intranet, portals, and mobile"; Conversations API; 100+ languages.
- Role model (explicit, five audiences): Program Owners (Employee Experience Insights — track metrics, governance/analytics), Developers (Agent Studio — build agents), Admins (Moveworks Setup — centralized self-service admin console: configure, secure, monitor), Knowledge Managers (Knowledge Studio — generate grounded knowledge articles to fill content gaps), Internal Communications (broadcast targeted comms through the assistant).
- Specialized Assistants: employees build task/domain-specific assistants ("Tailor assistants by content sources and tools, specify a user list"), vetted by the organization; AI Agent Marketplace (1000+ prebuilt agents claim — marketing figure).
- Heritage: solutions pages for IT (resolve issues, reset access, provision tools), HR (instant answers/self-service "from hire to retire"), finance, sales — the ITSM/HR tier-1-resolution origin is still visible; customer quotes frame it as tier-1 deflection (reduced support calls, ticket volume).
- Security posture: data minimization, zero-trust, auditable logging; FedRAMP authorization; ISO 27001/SOC 2/HIPAA/GDPR claims.
- Market note: ServiceNow acquisition closed (vendor's own announcement page).

## Product E — ChatGPT Enterprise (model-vendor tier) — NOT directly documented

- openai.com/chatgpt/enterprise/ timed out twice on 2026-09-08; abandoned per network rules. Kept as a market anchor: a general-purpose assistant sold to organizations with enterprise administrative controls. No operational claims drawn from it anywhere in this pass. Its existence supports the deployment-substrate variant (model-vendor enterprise tier) at positioning level only.

## Cross-product Comparison

| Dimension | M365 Copilot | Glean | Amazon Q Business | Moveworks |
|---|---|---|---|---|
| Operator/customer | the organization (tenant/licensing) | the organization (tenant) | the organization (AWS account, subscriptions) | the organization (platform deployment) |
| Served population | workforce (Entra work accounts; personal accounts = separate consumer surface) | workforce ("anyone who works across multiple apps") | workforce users via IAM Identity Center; anonymous apps = explicit exception | workforce ("your entire workforce") |
| Interaction | conversational chat + in-app assistance | conversational chat + search + voice + canvas | conversational web-experience chat | conversational across chat/web/portals/mobile |
| Company grounding | Graph/Work IQ (Premium), upload/open-content (lower tiers) | connectors, permission-scoped | connectors/retrievers, permission-aware, cited | integrations, individual permissions |
| Web/model knowledge | web grounding + model knowledge; admin policy on web search | three-source model with per-query toggles; admin-gated web | admin-configured: enterprise-only vs +model knowledge | business context + model knowledge |
| Actions | in-app actions; agents; Cowork (on your behalf) | agents, tools, MCP | plugins (create a ticket), Q Apps, routine actions | action plugins, agents, proactive nudges |
| Admin console | Copilot Control System + AI Administrator role | Admin Console (RBAC, connectors, insights, audit, models) | AWS console (application, subscriptions, plugins, guardrails) | Moveworks Setup |
| Usage analytics | usage reports (active users, prompts) | insights dashboards | — (not fetched at that depth) | Employee Experience Insights |
| Builder layer | Copilot Studio (separate product) | agent builder + templates | Q Apps (from conversation) | Agent Studio + marketplace |
| Distinct flavor | deepest productivity-app embedding; licensing tiers | knowledge-management layer (verification, answers, collections) | cleanest RAG pipeline documentation; anonymous-app pole | service-desk heritage; omnichannel; comms broadcast |

### Cross-product commonalities (Layer B)

1. **Organization as operator**: every product is bought, provisioned, and administered by the organization — identity integration (Entra / IdP-SSO / IAM Identity Center), admin consoles, user subscriptions/licenses.
2. **Workforce as served population**: all four frame the user as the employee at work; external-audience modes are either absent or explicitly separate (Q Business anonymous apps; Copilot's personal-account entry points listed as the consumer surface).
3. **Conversational NL assistance with model-generated responses**: chat is the universal primary surface; in-app/embedded assistance is the common second surface.
4. **Permission-scoped grounding**: responses draw on company content the asking user may already access; citations as the verification mechanism (Copilot: "access scoped by user permissions"; Glean: "results limited to what you already have permission to see"; Q Business: "permissions-aware responses... with citations"; Moveworks: "individual permissions").
5. **Admin-configurable grounding posture**: whether the assistant may use web/model knowledge vs enterprise data only is an admin decision (Copilot web-search policy; Glean toggles + admin gate; Q Business explicit admin setting).
6. **Actions beyond answering**: every product executes work in connected systems (plugins/agents/Cowork/Q Apps) — the "search and action" pairing is industry vocabulary (Moveworks' own headline).
7. **Admin governance layer**: policies, model management, agent governance, usage/adoption analytics, audit logging.
8. **Multi-surface delivery**: web app + embedding into productivity/chat tools + extension/API; MCP/API supply of the same assistant to other tools (Glean MCP, Moveworks Conversations API, Q Business embed).
9. **Builder/extension layer beside the assistant**: agents (all four), agent builders (Copilot Studio, Glean agents, Agent Studio, Q Apps) — the assistant is extensible into scoped agents.
10. **Human-accountability framing**: Glean states it outright ("support, not replace, human decision-makers"; high-risk operations excluded); the others express it via guardrails/governance machinery.

### Where products differ (variant axes)

- Deployment substrate: suite-embedded (Copilot) vs standalone platform (Glean, Moveworks) vs cloud-provider service (Q Business) vs model-vendor tier (ChatGPT Enterprise, positioning only).
- Center of gravity: productivity-app assistance (Copilot) vs knowledge+agents platform (Glean) vs configurable RAG assistant (Q Business) vs service automation grown wide (Moveworks).
- Autonomy depth: single-turn assistance ↔ multi-step agentic execution (Moveworks Reasoning Engine, Cowork, agents).
- Grounding breadth: enterprise-only ↔ enterprise+web+model knowledge.
- Knowledge-management layer depth (Glean deepest: verification, answers, collections).
- Audience exceptions: anonymous/public-facing applications (Q Business) — a boundary pole, not the center.

## Canonical Abstraction

### L0 — Defining Invariant

An Enterprise AI Assistant is **an AI assistant operated by an organization for its own workforce, interacted with in natural language, whose responses and assistance are generated by AI models**.

Three jointly-held properties; remove any one and it is a different thing:

1. **Organization-operated** — the organization is the customer and operator: it provisions its people (workforce identity), administers the assistant, and governs its use. Remove → consumer AI chat (no directory leaf; outside the atlas).
2. **Workforce-facing** — the served population is the organization's own employees/members acting in their work context. Remove → customer-facing chatbot / service bot (Customer Service Chatbot Platform) or guest-facing concierge (Digital Concierge).
3. **AI-driven conversational assistance** — employees request in natural language; the assistant's responses/assistance are model-generated, not fixed scripted flows. Remove → scripted decision-tree bot or a search UI.

Note on the "AI" leg: the modern category is LLM-era. NLU-era enterprise virtual assistants and platform-native productivity assistants (Cortana-in-M365 class) satisfy the org-operated + workforce-facing + conversational core and are the thin ancestors; fully scripted FAQ bots fail the AI leg and are excluded. "LLM" specifically is era-current implementation, not the invariant — the abstraction is "AI model-generated assistance."

### L1 — Common Mature Structure

Present in essentially all mature current products; not required to recognize the Type:

- **Organization grounding**: connectors/index over company knowledge; permission-scoped retrieval; cited answers.
- **Work actions**: plugins/actions in connected systems; task automation; agents; proactive nudges.
- **Productivity embedding**: assistance inside docs/email/meetings/chat tools; browser extension.
- **Admin & governance console**: identity/SSO provisioning, policies, model management, agent governance, usage/adoption analytics, audit logs.
- **Conversation history** with bounded retention; multi-surface delivery; API/MCP supply of the assistant to other tools.
- **Knowledge-management layer** (verified answers, collections) — strongest at the knowledge-platform pole.
- **Builder/extension layer** (agents, agent builders) beside the assistant.

### L2 — Variant / Optional Structure

- Deployment substrate (suite-embedded / standalone / cloud-provider / model-vendor tier).
- Scope: general-purpose vs domain-scoped (IT/HR service pole — Moveworks heritage).
- Autonomy depth: assistance-first ↔ agentic-first.
- Grounding posture: enterprise-only ↔ +web ↔ +model knowledge (admin-configurable).
- Anonymous/public-facing applications (Q Business pole — drifts out of the Type).
- Model posture: vendor-hosted vs multi-model selection vs BYO.
- Compliance posture: data residency/boundaries, regulated-industry authorization (FedRAMP), regional model availability.
- Specialized/secondary assistants built by employees and vetted by the org.

### L3 — Vendor-specific (research notes only)

- Microsoft: Copilot Chat (Basic) / M365 Copilot (Basic/Premium) license ladder; pay-as-you-go agents; Copilot credits/usage-based billing; Cowork; Work IQ; Copilot Search; semantic indexing; EDP; EU Data Boundary; Purview integration; AI Administrator role; organizational messages; model router (Auto/Quick/Think deeper); Anthropic subprocessor opt-in.
- Glean: "enterprise AI coworker" framing; All Knowledge mode + per-query toggles; tenant ID/BE domain; Admin Chat; Protect/Protect+; insights families; A2A server; go links; Gleaniverse/Academy; marketing figures (40+ LLMs, 275+ connectors, adoption/hours stats — excluded from final doc).
- Amazon Q Business: IAM Identity Center application model; web-experience URL; quick prompts; Q Apps; anonymous applications; user-subscription + index-capacity pricing; hallucination mitigation; message IDs; 30-day conversation history; end-of-sale → Amazon Quick.
- Moveworks: Reasoning Engine; Agent Studio; Knowledge Studio; Employee Experience Insights; Quick GPT; Brief Me; AI Agent Marketplace; Conversations API; specialized assistants; ServiceNow acquisition; FedRAMP.

## Vendor-specific Findings

(See L3; none promoted to the canonical model. The closest calls: permission mirroring and admin-configurable grounding are near-universal in the sample but were kept in L1 because the L0 stands without them — a minimally-configured org assistant is still recognizable; and the knowledge-management layer is Glean-signature though the *function* (trusted answers) appears elsewhere in weaker forms.)

## Boundary Findings

1. **vs Enterprise Knowledge Assistant (§13 sibling, unprocessed) — closest sibling, joint review required.** Same products serve both readings (Glean, Copilot). Proposed seam (center of gravity): the knowledge assistant is centered on grounded answering from the organization's knowledge — the knowledge corpus and answer trust are the defining center; the enterprise AI assistant is centered on general work assistance — answering is one capability beside drafting, summarizing, analysis, and actions in systems. Removal tests: strip drafting/actions/general chat → knowledge assistant remains; strip the knowledge-corpus center (keep general assistance with thin grounding) → enterprise AI assistant remains. The ESP pass already recorded "enterprise search is the grounding substrate for Enterprise Knowledge Assistant leaves"; this pass extends: it is the substrate for both assistant leaves.
2. **vs Enterprise Search Platform / Internal Knowledge Search (§10, processed)** — search returns result lists over the org estate; the assistant converses, composes, and acts. Glean's own docs demote search ("Search is one of the jobs Glean is good at, but it's just one of many"). ESP/IKS inherit as grounding substrates (index + permission layer). The assistant's built-in search is a capability, not the Type.
3. **vs Knowledge Question Answering Application (§02.03, processed)** — KQA: owner-defined KB defines what is answerable; the grounded answer is the deliverable. The enterprise assistant's scope is broader (drafting, actions, general work chat) and its grounding is the live connected estate rather than a curated KB. KQA's internal-audience pole is the overlap zone; the KQA pass's "agent-platform knowledge layer" drift note is consistent.
4. **vs Customer Service Chatbot Platform (§07, processed)** — audience test: external customers vs internal workforce. Q Business's anonymous applications are the explicit exception pole (public-facing deployments of assistant machinery) — recorded as a variant drifting out of the Type.
5. **vs AI Coding Assistant / AI Coding Agent (§12, processed)** — domain-scoped specialization: the coding assistant is centered on the development workflow (IDE-embedded, code context); the enterprise assistant is general-purpose. Vendor-internal evidence: Microsoft lists GitHub Copilot as an independently licensed separate product from M365 Copilot. The org-operated property is shared; the center differs. Consistent with the coding passes' autonomy-gradient framing (assistant vs agent) — orthogonal axis.
6. **vs Agent Development Platform (§13, processed)** — builders vs end users: agent platforms build/run custom agents; the enterprise assistant is the ready-made assistant employees use. Vendor-internal evidence: Copilot Studio (builder) vs Microsoft 365 Copilot (assistant) as separate products; Moveworks Agent Studio beside Moveworks AI Assistant. Assistants embed agent capability (agents as a capability of the assistant), which is the convergence zone.
7. **vs Business Intelligence Platform (§13, processed)** — the BI pass held: in-BI AI features are capabilities of BI. This pass confirms the mirror side: assistants may consume BI/warehouses as data connections (Glean BigQuery connection; Q Business ↔ Quick Sight integration), but governed analytics content remains BI's center.
8. **vs AI Gateway / AI Governance / AI Safety Guardrail / LLM Observability (§13, processed)** — infrastructure and governance layers around AI usage; the assistant is the end-user product those layers govern. No structural overlap; integration-coupled.
9. **vs Digital Concierge (§29, processed)** — external guest-facing service assistant in hospitality; audience test separates it (same test as #4).
10. **vs AI Meeting Assistant (§03.10, processed)** — meeting-scoped assistant; the enterprise assistant may include meeting help as one capability.
11. **Consumer AI chat** — no directory leaf; fails the org-operated leg. Copilot's own docs separate personal-account (MSA) entry points from work-account (Entra) entry points — vendor-internal confirmation that the consumer surface is a different thing.
12. **Historical check (§24)**: pre-LLM NLU-era enterprise virtual assistants (ITSM virtual agents, Amelia-class) and platform-native productivity assistants (Cortana-in-M365 class) satisfy org-operated + workforce-facing + conversational with AI-driven (NLU) responses — thin ancestors that fit the abstract core; fully scripted decision-tree bots fail the AI leg. The L0 deliberately does not require LLMs, connectors, agents, or admin analytics.

## Uncertainties

- ChatGPT Enterprise (and Google Gemini enterprise tiers) not directly documented — the model-vendor-enterprise-tier variant rests on positioning-level knowledge only; no operational claims made.
- Amazon Q Business is end-of-sale (→ Amazon Quick); its documentation remains the cleanest workflow evidence this pass, but the product's future shape is unknown.
- Moveworks evidence is product-page tier (help.moveworks.com not fetched); operational workflow detail (e.g., exact resolution flows) not asserted.
- Pricing/licensing specifics (Copilot tiers, Q Business subscription+index structure) observed as structures, not asserted as numbers.
- The Enterprise Knowledge Assistant seam is one-sided (sibling unprocessed); joint review pending.
- Marketing figures (adoption %, hours saved, connector/LLM counts) observed but excluded from all claims.

## Final Synthesis

The Enterprise AI Assistant is the organization's own AI assistant: bought and operated by the organization, served to its workforce, interacted with in natural language, and powered by AI models. Everything that makes modern products impressive — company-knowledge grounding with citations, actions in connected systems, agents, productivity embedding, admin governance, usage analytics — is the mature market's standard equipment, not the definition. The definition is the triangle: **organization-operated × workforce-facing × AI-driven conversational assistance**. The Type sits at the top of the §13 stack: enterprise search and data platforms are its substrate, gateways/guardrails/governance its plumbing, agent platforms its extension mechanism, BI and domain assistants its neighbors — and its closest sibling (Enterprise Knowledge Assistant) differs by center of gravity, not by structure.
