# Research Notes — Knowledge Question Answering Application

Date: 2026-09-08
Leaf: Knowledge Question Answering Application (DIRECTORY §02.03 Answering & Research)
Slug: knowledge-question-answering-application

## Research Goal

Understand the population the directory leaf "Knowledge Question Answering Application" names, and test the provisional boundary recorded by the answer-engine pass (research/answer-engine.md §Boundary Findings #5): "answer engine spans open/general-purpose material for a general audience vs KQA bound to an organization-defined knowledge base serving that organization's users".

Deliver: a minimal defining core (L0), the standard capability layer (L1), variant axes (L2), and vendor-specific detail (L3); discharge or escalate the answer-engine joint-review flag; hold seams against Knowledge Base Application, Help Center, Internal Knowledge Search/ESP, Expert Q&A Platform, Customer Service Chatbot Platform (§07), AI Research Assistant, and unprocessed Enterprise Knowledge Assistant (§13).

## Initial Boundary

Working hypothesis from directory placement (§02.03, sibling of Answer Engine / AI Research Assistant / Expert Q&A Platform) and the answer-engine pass's provisional seam:

- The Type is question answering bound to a defined knowledge corpus owned by/for an organization — the market phrases this as "answers grounded in your data / your knowledge / your content".
- Nearest neighbors to hold: Answer Engine (open/curated general corpus, public audience), Knowledge Base Application (corpus authoring/governance machinery; article is the unit), Help Center (support publication), Internal Knowledge Search / ESP (multi-source discovery-first layer over the whole estate), Expert Q&A Platform (human-authored answers), Customer Service Chatbot Platform (conversation business with tickets/routing/handoff), AI Research Assistant (persisted research process/artifacts).

## Research Questions

1. What exactly is the "knowledge base" in KQA products — what source material, what assembly machinery, what currency guarantees?
2. How does asking work — surface, input form, conversational context?
3. How are answers produced — generation over retrieved content vs retrieval of Q&A pairs? What evidence of grounding (citations, confidence)?
4. What happens when the base cannot answer — refusal, uncertainty, fallback, escalation?
5. What is the improvement loop — how does asking feed back into the base?
6. Who operates the system and who is the asking audience; how is audience/access defined?
7. What delivery surfaces exist (widget, page, chat tools, API)?
8. Where does this Type end and Customer Service Chatbot Platform / agent platforms begin (the 2026 drift toward agentic products)?

## Representative Products

Selection principle: market representation + documentation completeness + different product philosophies + different customer tiers + different packaging poles.

| Product | Pole | Why sampled |
|---|---|---|
| kapa.ai | Enterprise, technical docs/community/support Q&A; knowledge-infrastructure packaging | Deepest operational docs in the population; documents the full loop (ingestion → retrieval → grounded answers → analytics → coverage gaps) |
| Microsoft Custom Question Answering (Azure AI Language / Foundry) | Developer cloud service / builder pole; pre-LLM-era machinery lineage (Q&A-pair KBs, ranking, confidence) | The clearest explicit "question answering over your data" service documentation; documents Q&A-pair extraction, multi-turn, metadata filtering, active learning, deploy-as-endpoint |
| Chatbase | Self-serve SMB builder pole | "Train an agent on your business data" in the purest self-serve form; documents the create→train→test→deploy→monitor loop end to end |
| Zendesk (AI agents) | Customer-service suite pole | Shows the same answering capability embedded in a service suite with escalation machinery; seam-vs-chatbot-platform specimen |
| Inkeep | Agent-platform drift pole | Current docs show a KQA-lineage product repurposed as a no-code/code agent builder; market-drift evidence |

Rejected/adjusted samples:
- DocsBot AI (self-serve pole candidate): docs.docsbot.ai unreachable (transport error ×2 on 2026-09-08) — dropped per network-limitation rule; Chatbase covers the pole.
- Zendesk Tier-1 help-center articles (e.g. "Getting started with AI agents") require sign-in — Zendesk evidence is product-page (Tier-2) strength only; claims calibrated accordingly.
- Internal-pole products (Guru, Glean-class) not re-sampled: covered by the knowledge-base-application and internal-knowledge-search passes; kapa's internal "company brain" use case provides internal-pole evidence within this sample.

## Sources

Tier-1 (operational docs, fetched 2026-09-08):
- kapa.ai docs — https://docs.kapa.ai/ (overview); /use-cases/documentation-assistant; /use-cases/internal-knowledge; /knowledge-sources/data-ingestion; /retrieval/; /analytics/coverage-gaps
- Microsoft Learn — Custom question answering overview — https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/overview
- Chatbase docs — https://docs.chatbase.co/ (welcome); /docs/user-guides/quick-start/your-first-agent

Tier-2 (product/positioning pages):
- Zendesk — AI Agents for Customer Service — https://www.zendesk.com/service/ai-agents/
- Inkeep docs — https://docs.inkeep.com/ (overview; open-source agent builder positioning)

Unreachable / limitations:
- Zendesk support article "Getting started with AI agents" (support.zendesk.com) → sign-in wall (Tier-1 blocked).
- DocsBot AI docs → transport error ×2 (dropped).
- help-center/knowledge-base-application/internal-knowledge-search passes' evidence reused for boundary reasoning only (no new product claims from them).

## Product Observations

### kapa.ai (evidence layer A — operational docs, 6 pages)

- Positions as an ingestion + "agentic retrieval" system: "it indexes your unstructured knowledge, documentation sites, PDFs, tickets, community threads, API specifications, and gives any agent the most relevant content from all of it" (docs root).
- **Knowledge base assembly**: "Ingestion assembles a unified knowledge base from 20+ types of sources … and keeps it up to date as that content changes." Sources include docs sites (web crawl), ticketing systems, community threads (Discourse, Stack Overflow), PDFs, API specs (OpenAPI), GitHub content, Google Drive, Confluence, Notion.
- **Currency machinery**: stateful per-source change sync (not wholesale re-index); different schedules for updates vs deletions ("deletions … a far more expensive check"); web crawling runs daily change-detection with new/modified/unchanged/deleted classification; **large-scale anomalies are gated for human review** ("If a large share of a site's pages changed or disappeared in a single crawl, nothing is applied and the crawl is routed to human review"); Sources view shows per-source last-checked state.
- **Retrieval & answering**: retrieval returns "the most relevant chunks … ranked and with their source URLs"; "It never generates text: your agent does the reasoning, Kapa provides the grounding"; Prebuilt Agents "generate an answer grounded in your own knowledge sources, with citations".
- **Answer states**: analytics FAQ documents **'uncertain' and 'off-topic' answer tagging**.
- **Use cases** (all rest on retrieval of the owner's knowledge): "Ask AI on your documentation" (users "ask in their own words, get an answer with citations into your pages"); support automation; community Q&A (Slack/Discord bots); **"Build a company brain"** — internal: "employees self-serve answers from it, with access restricted to authenticated employees"; public MCP server; competitor intel; RFP drafting.
- **Delivery surfaces**: Website Widget (chat on docs sites, "answering with citations back into your pages"), Slack Bot, Discord Bot, Support Form Deflector, Zendesk Agent, Internal Technical Assistant ("a private chat interface at chat.kapa.ai"), Chat SDK, Chat API, hosted MCP server, Agent SDK.
- **Improvement loop**: Coverage Gaps — analyzes **uncertain answers**, clusters recurring failure topics, produces Finding + AI-generated **Recommendation** "by updating your documentation"; "These suggestions require human review"; recommended workflow edits the documentation repository. Also Top Questions, Source Analytics, dashboards, email/Slack reports, Analytics API.
- **Customization**: "tune the agent's behavior and tone per deployment"; PII masking/security pages exist.

### Microsoft Custom Question Answering (evidence layer A — official service overview)

- Definition: "a cloud-based NLP service that creates conversational AI applications over your data. Build knowledge bases from FAQs, manuals, and documents to deliver accurate answers through chat bots, virtual assistants, and interactive interfaces."
- **KB creation**: "Import content from URLs, files, and documents. The service automatically extracts question-answer pairs from structured and semi-structured sources." Manual Q&A pair authoring supported (low-code authoring in Foundry classic).
- **Pipeline**: create project → test/refine → deploy → integrate; "Client applications send queries and receive JSON responses with answers, confidence scores, and follow-up prompts."
- **Capabilities**: multi-turn conversations with follow-up prompts; **metadata filtering** ("Tag answers by content type, domain, or freshness"); **active learning** ("Improve answer quality based on real-world usage patterns and user queries"); **deep learning ranking** ("Multi-stage ranking architecture combines Azure AI Search with NLP reranking for optimal **answer selection**" — i.e., selection, not necessarily generation); chit-chat integration; deploy to Azure Bot Service; SDKs (.NET/Python).
- Retirement notice (March 31, 2029) documents the lineage's lifecycle; successor guidance points to Foundry models.

### Chatbase (evidence layer A — operational docs, 2 pages)

- Positioning: "build intelligent agents trained on your business data"; "Train your AI Agent with your own documents, websites, or databases for accurate, relevant responses."
- **Training data**: Files ("Business documents, manuals, FAQs, product information"), text snippets, website crawl ("discover and learn from all your pages"), **Q&A pairs** ("Add your own Q&A … specific questions and answers that you want your agent to know"), Notion import.
- **Loop**: Create & Train → Test & Optimize (playground; **Instructions** define "tone … role … Set clear boundaries about what topics to discuss or avoid"; model choice; temperature) → Deploy (chat bubble, iframe, help page; Email, WhatsApp, Messenger, Instagram, Shopify, Slack, Zendesk, phone).
- **States**: agents are **disabled (workspace members only) vs enabled (public embed/link)** — audience/access is an owner decision.
- **Actions beyond answering** (pre-built): "human escalation, Slack, Stripe, Calendly, lead collection, and web search, plus custom actions" — the **web-search action is an explicit fallback/extension beyond the base**; escalation is a packaged action, not the core.
- **Analytics**: "Track conversations, monitor performance, and continuously improve your AI Agent."

### Zendesk (evidence layer B — product page only; Tier-1 help center sign-in-walled)

- "Ground answers in unified knowledge: Connect AI agents to your help center and external sources like Google Drive or PDFs to deliver accurate, on-brand answers. Keep guidance aligned as policies and product details evolve."
- Escalation: "When escalation is needed, they intelligently route issues to the right team … with full context to ensure a smooth handoff."
- Channels: messaging, email, voice, social; agentic workflows and system actions; built-in QA scoring; "Close the loop with self-improving AI: Identify gaps … refine knowledge and workflows based on outcomes."
- Pricing tied to resolutions; 80-language claim (marketing precision — not carried into final doc).
- Reading: the KB-grounded answer is one capability of an agentic service platform whose defining machinery (resolution, routing, actions, QA) belongs to the customer-service domain. Straddle specimen for the chatbot-platform seam.

### Inkeep (evidence layer A for its own product; used as drift evidence)

- Current docs define Inkeep as "a platform for building Agent Chat Assistants and AI Workflows" (no-code visual builder + TypeScript SDK) — a full agent-builder pivot.
- Residual KQA shape in its own use-case list: "a customer experience agent for help centers, technical docs, or in-app experiences" and "an internal copilot"; chat components, MCP/A2A delivery.
- Interpretation: a KQA-lineage product whose center of gravity moved to agent building; the KB-grounded chat assistant is now one use case. Evidence of market drift, recorded under Escalation Conditions (product-market mismatch of the current positioning vs leaf).

## Cross-product Comparison

| Dimension | kapa.ai | Microsoft CQA | Chatbase | Zendesk (Tier-2) | Inkeep |
|---|---|---|---|---|---|
| Bounded owner-defined corpus | unified KB from 20+ source types, synced | KB from FAQs/manuals/documents + auto-extracted Q&A pairs | files/text/crawl/Q&A pairs/Notion | help center + Drive/PDFs | indexed content for agent context |
| NL question input | widget/bots/API/MCP | client apps query endpoint (bots/assistants built on it) | widget/page/embeds | messaging/email/voice | chat components/API |
| Answer production | agent generates, grounded via retrieval | **answer selection** via multi-stage ranking (+confidence) | agent generation over trained data | grounded answers (machinery not directly observed) | agent generation |
| Grounding evidence to user | citations into pages, source URLs in retrieval | confidence scores in JSON | not directly observed | "accurate, on-brand" (positioning) | citations in examples |
| Out-of-coverage | 'uncertain' tagging + coverage-gap analytics | confidence scores; thresholding documented elsewhere (not fetched) | instructions set topic boundaries; **web-search fallback action** | escalation to humans | not observed |
| Improvement loop | coverage gaps → docs recommendations → human review | active learning from usage | analytics → "continuously improve" | self-improvement from outcomes | not observed |
| Audience/access | public deployments + authenticated-employee projects | audience-agnostic (developer decides) | disabled (internal) vs enabled (public) | customer-facing service | per-agent |
| Delivery | widget, Slack/Discord, SDK/API, MCP | REST endpoint + Bot Service | widget/iframe/page/many channels | suite channels | components/API/MCP/A2A |
| Packaging | enterprise platform + prebuilt agents | developer cloud service | self-serve SaaS | service-suite module | open-source agent builder |

Cross-product commonality (layer B): the owner-assembled bounded corpus as answer ground; NL question → direct answer as the deliverable; source grounding with references; currency maintenance of the corpus; an improve-the-base loop (in four of five at observed or positioning strength); multi-surface delivery incl. an API.

Notable divergences: answer production machinery (selection+confidence vs generation+citations — era/generation difference); out-of-coverage strictness (refusal/uncertainty vs web-search fallback); escalation presence (support-context pole only).

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The owner-defined knowledge base** — a bounded corpus assembled and kept current from the owner's own knowledge material (documentation pages, help articles, manuals/files, site content, community threads, curated Q&A pairs), held by the system as the answer source; the base defines what is answerable. Remove → open-web/general-purpose answer engine or a general chat assistant (no owning corpus).
2. **Question-anchored asking by the owner's audience** — the audience the owner defines (customers, community members, employees) asks natural-language questions about the base's domain. Remove → knowledge-base publication/search surfaces (KB Application / Help Center / internal search): users browse and read, they don't ask.
3. **The system-composed grounded answer as the deliverable** — at question time the system produces a direct answer from the base (generated from retrieved material, or a matched Q&A pair delivered as the answer), commonly with source references — not a ranked document list, not a human-written reply. Remove → KB search / discovery layer (results list) or Expert Q&A platform (human author).

Jointly-held is load-bearing:
- 2+3 without 1 → Answer Engine (open/curated general material, no owning organization or bounded accountable corpus).
- 1+3 without 2 → Help Center / KB publication with search (the article, not the answer, is the deliverable).
- 1+2 without 3 → KB search / internal knowledge search at its discovery-first pole (documents returned, not answers composed).

Triadic relation owner → corpus → audience is the discriminator that holds L0 minimal: the corpus is *the owner's*, the audience is *the owner's*, and the owner is accountable for the answers (hence the improve-the-base loop).

### L1 — Common Mature Structure

- Ingestion breadth + currency machinery: site crawl, file upload, connectors (ticketing, community, drive/wiki tools), Q&A-pair authoring; change-sync rather than wholesale reprocessing; per-source sync state.
- Grounded-answer presentation: citations/links into source pages; source URLs in retrieval results.
- Uncertainty handling: confidence scores (builder/service pole), uncertain-answer states; refusal/abstention instead of guessing.
- Conversational follow-up within a session (multi-turn prompts; chat continuations).
- Delivery surfaces: embeddable website widget, dedicated help/chat page, bots in chat tools, REST API/SDK.
- Owner console: sources/knowledge management, test playground, behavior instructions (tone/role/topic boundaries), deployment/channel configuration.
- Analytics & improvement loop: questions asked, uncertain/unanswered tracking, coverage-gap clusters with recommendations, active learning, feedback — feeding owner updates to the base.
- Access control: public vs authenticated audience (internal corpora gated; workspace-only preview states).

### L2 — Variant / Optional Structure

- **Audience pole**: external (customers/users of a product; docs/help-center/self-service) vs community (Slack/Discord members) vs internal (employees; "company brain").
- **Packaging**: standalone point product (enterprise, sales-led); self-serve SaaS builder; developer cloud service (endpoint-centric); module inside customer-service suites; knowledge layer beneath agent platforms (current drift).
- **Corpus composition emphasis**: product docs; help-center articles; internal drives/wikis; community threads; structured Q&A pairs; PDFs/manuals.
- **Answer-production era**: retrieval + LLM generation with citations (current dominant) vs Q&A-pair extraction/matching with ranking + confidence (documented, pre-generation generation of the Type).
- **Out-of-coverage posture**: strict confinement (refuse/flag) vs configured fallback (web-search action) vs human escalation (support contexts).
- **Escalation machinery**: none (pure docs QA) vs packaged handoff actions vs suite-grade routing with context.
- **Actions beyond answering**: lead capture, booking, transactions — chatbot-platform drift zone.
- Deployment (SaaS vs self-host/open-source), pricing (seats vs outcomes vs usage), multi-product/multi-brand corpora, PII/security machinery depth.

### L3 — Vendor-specific (kept out of final doc)

- kapa: crawl anomaly gates ("large share changed → human review"), Slack 7-day rolling re-scan, Internal Technical Assistant at chat.kapa.ai, Analytics "skills" workflow with a public GitHub skills repo, per-deployment customizations, hosted MCP server, Agent SDK.
- Microsoft CQA: chit-chat dataset integration, Azure AI Search + NLP rerank two-stage architecture, metadata-freshness tagging examples, Foundry-classic authoring portal, March 2029 retirement.
- Chatbase: plan storage limits, identity verification on widget, disabled/enabled toggle semantics, prebuilt action catalog (Stripe, Calendly), model/temperature comparison playground.
- Zendesk: resolution-based pricing tiers/allowance, 80-language claim, Forethought acquisition framing, "Resolution Learning Loop".
- Inkeep: visual builder/TS SDK two-way sync, fair-code license, self-hosting.

## Vendor-specific Findings

(See L3. Additional market-structure observations:)
- Products in this population self-describe with the same possessive construction: "your data" (CQA), "your business data" (Chatbase), "your own knowledge sources" (kapa), "your help center" (Zendesk) — cross-product textual convergence on owner-defined corpora (layer B).
- 2026 drift: KQA-lineage products are repositioning as "agentic retrieval" (kapa), agent builders (Inkeep), or resolution platforms (Zendesk). The KB-grounded answering capability persists as the knowledge layer; the leaf's center of gravity remains answer delivery from the owned base.

## Boundary Findings（"去掉什么就变成另一个 Type"判据）

1. **vs Answer Engine（§02.03, processed — JOINT REVIEW DISCHARGED from this side）**: seam = **corpus ownership & audience accountability**. Answer engine answers the world's questions over open/curated general material (no owning organization, no bounded corpus defining answerability); KQA answers a defined audience's questions about the owner's domain from the owner's maintained base, with the owner accountable for answer quality (improve-the-base loop). Removal tests: give the KQA product the open web as its ground and a general audience → Answer Engine (Chatbase's web-search fallback action shows the gradient edge; it remains KQA because the base is the primary ground and the fallback is optional); give an answer engine a single owner's bounded corpus, that owner's audience, and a KB-improvement loop → KQA. **Gradient risk acknowledged** (the answer-engine pass kept corpus scope as an L2 variant: a public answer product scoped to one corpus exists); resolution from this side: keep-both, with the owner-accountability triad (owner→corpus→audience) as the ratified seam, and the gradient zone (custom-scoped public answer engines) recorded for taxonomy maintainers. Verdict recorded in STATUS Boundary Issues.
2. **vs Knowledge Base Application（§02.06, processed）**: KB = the corpus and its authoring/ownership/review governance is the product's center (article is the unit); KQA = answering machinery is the center (the answer is the unit; the corpus is the input). Removal: strip system-composed answers → KB with search; strip corpus authoring/governance → KQA. Market blur: "AI knowledge base" labels; KB products adding AI answers realize the KQA function inside KB tooling (packaging, not identity). Consistent with the KB pass's own boundary #6 (Guru Answers straddle recorded there).
3. **vs Help Center（§02.07, processed）**: publication surface vs answering machinery. A help center publishes articles for self-serve retrieval; the KQA application composes answers from the (help-center or wider) corpus at question time. Consistent with help-center/KB ratified seams.
4. **vs Internal Knowledge Search / Enterprise Search Platform（§13/§10, processed）**: discovery-first layer over the multi-source estate (results-first delivery; whole-estate scope incl. records/people) vs answer-first delivery from an owner-defined, governed base. Softest seam at the internal pole (kapa's company brain indexes Drive/Confluence/Notion — multi-source): the retained discriminators are answer-vs-results delivery and the owner-accountability loop (coverage gaps → owner updates the base), which the ESP/IKS passes' discovery/trust framing does not center. Flagged for the EKA/ESP passes' awareness; no merge proposed.
5. **vs Customer Service Chatbot Platform（§07, unprocessed）**: the deliverable (grounded answer) vs the conversation business (tickets, routing, scripted flows, agent handoff, resolution). Escalation in KQA products is optional/packaged (Chatbase action; kapa form deflector hands to the support flow); in service suites it is defining. Zendesk AI agents straddle deliberately (suite module). Advance note for that pass.
6. **vs Expert Q&A Platform（§02.03, processed）/ Q&A Community（§01.06, unprocessed）**: answer author. Humans write answers on Q&A platforms/communities; the KQA system composes answers from the owned corpus at question time.
7. **vs AI Research Assistant（§02.03, processed）**: no persisted multi-step research process, no durable research artifacts (libraries/reports); single question→answer loop. Consistent with the answer-engine pass's boundary #3 removal test.
8. **vs Enterprise Knowledge Assistant（§13, unprocessed — advance flag）**: likely the internal-audience sibling. Proposed seam from this side: EKA = employee-facing conversational assistant (assistant framing; may span tools/actions); KQA = answering from the owner-defined base with the improvement loop as the accountability structure. Joint review recommended when that leaf is processed.
9. **vs Online Encyclopedia / Reference（§02.05）**: fixed curated entries consulted by reading vs question-time composition from the owner's corpus (follows the answer-engine pass's boundary #6 logic; the owner-corpus makes KQA further distinct).

## Historical / Market-Sample Check

Question: would older, differently positioned, or non-LLM products still fit the L0? Yes:

- **Pre-LLM documented anchor**: Microsoft CQA's own overview documents the Q&A-pair KB era — auto-extracted question-answer pairs from FAQs/manuals, multi-stage **ranking for answer selection**, confidence scores, active learning — no generation step required. L0's "generated or selected" wording keeps this inside the Type.
- **Audience-agnostic machinery**: CQA/Chatbase are "build anything on your data" services — audience (customers/community/employees) is a deployment choice, not a definitional property. L0 accordingly says "the audience the owner defines", not a specific audience kind.
- **Conceptual pre-software antecedent** (calibration only, not a product claim): a maintained policy binder/FAQ consulted through an attendant who answers questions from it — owner, bounded corpus, question-anchored asking, composed answer — the same triad without software.
- Nothing era-specific enters L0: no LLM, no RAG specifics, no chat widget, no embeddings, no cloud delivery, no MCP. The current LLM-grounded-with-citations realization is recorded as the dominant modern implementation (L1/L2), not the definition.

## Uncertainties

1. **Zendesk operational depth missing** (Tier-1 help center sign-in-walled): how its AI agents retrieve/ground answers operationally was not observed; all Zendesk statements in the final doc are positioning-strength ("connects to your help center and external sources…") and the suite pole's machinery is described only as far as the product page shows.
2. **Citation presentation not universally observed**: explicit citations (kapa) and confidence scores (CQA) are A-level; Chatbase/Inkeep citation UIs were not on fetched pages. Final doc says source references are *commonly* shown, not universally.
3. **Out-of-coverage strictness variance** is documented at the poles (kapa uncertain-tagging; Chatbase web-search fallback action) but the distribution across the market is unknown; phrased as variance, not norm.
4. **Internal-pole depth** rests on kapa's internal use case + prior passes' evidence (Guru/Slite/Glean class); no dedicated internal-only product re-sampled this pass.
5. **Regional forms** (e.g., Chinese-market 企业知识问答 products) not sampled; no regional claims made.
6. **Answer-engine L2 tension**: the answer-engine pass's own L0 admits "knowledge base" as a grounding substrate (corpus scope as L2 there). This pass resolves it operationally (owner-accountability triad as the seam) but a taxonomy-level convergence check between the two leaves' L0/L2 framings remains for maintainers — recorded in STATUS.

## Final Synthesis

A **Knowledge Question Answering Application** is the answering machinery an organization deploys over its own knowledge base: the owner assembles and keeps current a bounded corpus from its own knowledge material (docs, help articles, manuals/files, site content, community threads, Q&A pairs); the audience the owner defines asks natural-language questions about that domain; and the system composes a direct, grounded answer at question time — generated from retrieved material or delivered as a matched Q&A pair — rather than returning a document list or a human's reply. Mature products wrap this core in a standard layer: ingestion breadth with change-sync currency, citations, uncertainty/confidence handling, conversational follow-up, multi-surface delivery (widget/page/chat tools/API), owner consoles (sources, playground, instructions), and an analytics loop that turns uncertain answers into coverage gaps the owner fixes in the base. Variants run along audience (external/community/internal), packaging (standalone/self-serve builder/developer service/suite module/agent-platform drift), corpus composition, answering-machinery era (Q&A-pair ranking vs retrieval+generation), and out-of-coverage posture (refuse vs fallback vs escalate). The Type holds against all neighbors on the owner→corpus→audience triad: open-grounded answering is the Answer Engine, article publication is the Knowledge Base/Help Center, results-first estate discovery is Enterprise Search/Internal Knowledge Search, human answers are Expert Q&A, the conversation business is the Chatbot Platform, and durable research work is the AI Research Assistant.

STATUS 一句话（L0）: owner-bound question-answering application whose defining core is exactly three jointly-held structures: the owner-defined knowledge base (bounded corpus assembled and kept current from the owner's own knowledge material — docs/articles/files/site content/community threads/Q&A pairs — defining what is answerable; remove → answer engine or chat assistant) + natural-language question asking about the base's domain by the owner-defined audience (remove → KB/help-center publication & search) + the system-composed grounded answer as the deliverable (generated from retrieved base content or a matched Q&A pair, commonly with source references — not a results list, not a human reply; remove → KB search / Expert Q&A); jointly-held is load-bearing (2+3 without 1 = Answer Engine; 1+3 without 2 = KB publication; 1+2 without 3 = KB search); standard capabilities NOT definitional: ingestion breadth + change-sync currency machinery, citations, uncertainty/confidence handling, conversational follow-up, delivery surfaces (widget/page/chat tools/API), owner consoles (playground/instructions/persona), analytics with coverage-gap improvement loops, active learning, metadata filtering, access control, human escalation (support-context pole), actions beyond answering (chatbot-drift pole); variants: audience pole (external customer/docs vs community vs internal company brain), packaging (standalone enterprise vs self-serve builder vs developer cloud service vs customer-service-suite module vs agent-platform knowledge layer), corpus composition, answering-machinery era (Q&A-pair extraction+ranking+confidence vs retrieval+LLM generation with citations), out-of-coverage posture (refuse/flag vs web-search fallback vs escalate); historical check passed (documented pre-LLM anchor: auto-extracted Q&A-pair KB + multi-stage ranking + confidence + active learning satisfies the core without generation); joint review with answer-engine DISCHARGED from this side — keep-both on the owner-accountability triad (corpus ownership & audience accountability), gradient zone recorded.
