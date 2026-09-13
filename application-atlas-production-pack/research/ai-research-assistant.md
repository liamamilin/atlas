# Research Notes — AI Research Assistant

## Research Goal

Understand what an **AI Research Assistant** actually is as an Application Type — from real products, not from marketing abstraction:

- what the AI actually *does* for the user (which research work is delegated to it)
- what material it works over (the source substrate)
- what artifacts it produces and keeps
- how outputs are grounded and verified
- where the boundary lies against Answer Engine, Academic Search Engine, Academic Paper Reader, Reference Manager, and general AI chat products

Directory location: section 02.03 "Answering & Research", alongside Answer Engine, Expert Q&A Platform, Knowledge Question Answering Application.

## Initial Boundary (hypothesis before research)

- Core use hypothesis: AI-mediated support for research work — asking research questions, surveying literature, extracting and synthesizing findings across sources, producing cited research outputs.
- Likely users: academic researchers, students, industry analysts/scientists, knowledge workers digesting document sets.
- Nearest Types: Answer Engine (quick open-web answers), Academic Search Engine (ranked corpus lists), Academic Paper Reader (single-document reading), Reference Manager (bibliographic record management), Expert Q&A Platform (human answers), Enterprise Knowledge Assistant (org-internal knowledge substrate).
- Known unknowns at start:
  - Do all products share one substrate (paper corpus) or do substrates vary (user files)?
  - Is conversational Q&A defining, or is non-conversational analysis also part of the Type?
  - Are persistent research artifacts (libraries, reports, tables) defining or common?

## Research Questions

1. What does the user bring to the system (task entry), and what forms can a "research task" take?
2. What source substrate does the assistant work over — product-managed corpus, user-uploaded documents, or both?
3. Which analysis operations does the AI perform (retrieve / summarize / extract / compare / synthesize / screen)?
4. How are outputs attributed to sources, and how do users verify them?
5. What durable artifacts exist (threads, tables, flashcards, reports, libraries)?
6. What rules matter: grounding posture, metering/plan limits, upload limits, corpus coverage disclaimers?
7. Where do products straddle neighboring Types (answer engine vs search engine vs assistant)?
8. Is the Type definable without overfitting to the "LLM chatbot over a paper corpus" pattern?

## Representative Products

Selected for: market representation, documentation quality, distinct product philosophies, distinct customer tiers.

| Product | Philosophy | Audience tier | Evidence quality |
|---|---|---|---|
| Elicit | corpus-first research-workflow automation (search → table → extraction → report; systematic-review support) | professional/academic researchers, pharma, policy | strong (homepage + help center operational articles) |
| Consensus | corpus-grounded evidence Q&A (search-first, then AI summarize/synthesize; agreement metering) | students, researchers, professionals | strong (homepage + two help-center articles incl. limitations page) |
| Humata | user-file-grounded assistant ("ask questions across your files") | teams/enterprise + individual students/researchers | moderate (homepage + FAQ only; docs subdomain not fetched) |
| Scholarcy | per-document structured summarization (flashcards) + library/export pipeline | students, individual researchers | strong (homepage + official getting-started guide) |

Considered and dropped for source-access reasons: NotebookLM (Google support + product pages timed out twice), SciSpace (site returned empty twice), Scite (timed out twice). These are used below only as unverified boundary references; no operational details were taken from them.

## Sources

All fetched 2026-09-06.

- Elicit — https://elicit.com/ (product page; A)
- Elicit — https://support.elicit.com/ (help center root; A) and https://support.elicit.com/en/articles/14757543-getting-started-with-elicit-which-workflow-or-tool-should-i-use (workflow guide; A)
- Consensus — https://consensus.app/ (product page incl. feature schema; A)
- Consensus — https://help.consensus.app/en/articles/9922673-how-consensus-works (operational doc; A)
- Consensus — https://help.consensus.app/en/articles/10083353-responsible-ai-limitations (guardrails & limitations; A)
- Humata — https://humata.ai/ (product page + FAQ; A, homepage depth)
- Scholarcy — https://scholarcy.com/ (product page; A)
- Scholarcy — https://help.scholarcy.com/ (official getting-started guide; A)

Source-access limitation: NotebookLM (support.google.com/notebooklm, notebooklm.google.com), SciSpace (scispace.com), Scite (scite.ai) could not be fetched after 2 attempts each. Their existence and rough market position were used only for boundary triangulation; no specific feature or behavioral claims about them are made anywhere in this research or the final document.

## Product Observations

### Elicit (evidence layer A)

Positioning: "AI for scientific research" — search, summarize, extract data from, and chat with a large corpus of papers (homepage states 125M+; the help article states 138M+ from Semantic Scholar and other sources). Used by researchers in academia and industry.

Key observations:

- **Task entry is a research question with a chosen workflow.** Home page offers: Research Report, Systematic Review, Find Papers, Chat with Papers, Extract Data, Research Agent. The help-center guide explicitly frames choice by research stage, desired control, and desired output.
- **Find Papers**: natural-language question → summary of most relevant papers + a **table of papers**; add suggested or custom **columns** (AI-filled analysis per paper), filter results, load more, save papers to library.
- **Research Report**: question → auto-generated structured report with references to the papers used; exportable PDF/Word; can be customized (which papers, which information is covered).
- **Systematic Review**: guided multi-step flow — enter question, include uploaded PDFs and/or corpus search results, **screen papers for include/exclude**, extract data, generate report. Marketing states PRISMA 2020 support, reproducibility/traceability; plan-tiered paper-count capacity.
- **Extract Data**: upload/choose PDFs → table of those papers; add columns; chat with them.
- **Chat with Papers**: select up to a plan-dependent number of uploaded/library papers → chat prompt over them.
- **Research Agent sessions**: agentic workflow — draws on sources "well beyond academic publications" (clinical trial data, regulatory documents, press releases, product labels), flexible outputs (tables, narrative summaries, multiple artifacts), and **iteration within a session** (follow-ups, new analyses, reshaping outputs). Up to 20 uploaded resources per session (plan-dependent).
- **Library**: store and organize found sources for reuse across projects. **Alerts**: notifications on new research. **Session history** is a documented surface.
- **Grounding posture (homepage)**: "supports all AI-generated claims with sentence-level citations from the underlying sources"; "more than chat — rich, interactive tables and multi-step workflows"; accuracy claims backed by published evals (vendor-run).
- **Metering**: all workflows subject to plan usage limits; recent move to a monthly usage pool.
- **Other**: Zotero import; API and MCP server; multiplayer collaboration (blog, Aug 2026).

### Consensus (evidence layer A)

Positioning: "AI-powered academic search engine built on a database of over 220 million peer-reviewed research papers"; explicitly contrasts itself with general AI tools: "every response is tied back to a real research paper."

Key observations:

- **Search pipeline (documented in detail)**: hybrid semantic (embeddings) + keyword (BM25) search over the corpus → re-rank top ~1,500 by quality signals (recency, citation count, journal impact/reputation) → final high-precision re-rank of top ~20 with a larger AI model. (Numbers are vendor-published pipeline detail — research notes only.)
- **AI is used only after search**: two modes — analyze individual papers in depth (Ask Paper, Study Snapshot) and synthesize across papers (Pro Analysis messages, Consensus Meter).
- **Consensus Meter**: AI analysis/visualization of agreement vs disagreement in the literature for yes/no questions.
- **Research Agent**: "handles complex, multi-step research questions by planning searches, chaining together tools, and applying academic filters."
- **Chat with Full Text / Ask Paper**: ask questions across the full text of specific papers, Collections, **or uploaded documents**.
- **My Library**: save/organize papers into collections; save searches.
- **Filters**: advanced AI-powered search filters (paper details); study types & research methods section in help center suggests study-design filtering is a documented concern.
- **Citation export** in RIS/BibTeX/CSV; **Citation Graph** for paper relationships.
- **Guardrails (Responsible AI page)**: "search before synthesis"; "summarization, not speculation" (models limited to retrieved paper content); "transparent sourcing and attribution — every claim is cited, every citation is clickable"; separate **checker models verify source relevance** before summarizing; user reporting (flag button).
- **Limitations acknowledged**: does not have access to all research; summaries are "a snapshot"; of the three hallucination categories (fake sources / wrong facts / misread sources), only misreading is claimed possible; misreads can still occur.
- Corpus: Semantic Scholar, OpenAlex, own crawl; updated weekly (vendor-stated).

### Humata (evidence layer A, homepage depth)

Positioning: "Ask questions across all of your files"; FAQ answers "Humata is built to work with files… generates answers based on the content of your documents. Each answer… will cite relevant sections from your uploaded documents." Vendor self-compares: "like ChatGPT for PDFs."

Key observations:

- **Substrate is user files only** (no product-managed paper corpus claimed on the homepage): upload documents (PDF emphasis); "unlimited files, unlimited questions."
- **AI work**: summarize findings, **compare documents**, search for answers across files; iterate — "order the AI to rewrite your summary until you're satisfied."
- **Attribution**: answers come with **cited links into the source files** ("trace where your insight came from").
- **Team/enterprise surface**: shared team files/data rooms, user access control, role-based security, folder/department-level permissions, OCR for scanned text, SSO (stated as coming soon on the page), embedding the assistant in webpages.
- **Metering**: plan tiers defined by page counts and answer counts (page-based pay-as-you-go above plan allowances).
- No corpus search, no literature-discovery features, no reference-manager integration observed.

### Scholarcy (evidence layer A)

Positioning: "Summarize, analyze and organize your research"; built "specifically for academic papers"; audience pages for students and researchers.

Key observations:

- **Import from anywhere**: PDFs, book chapters, articles, plain text, Zotero, Google Drive, YouTube, browser extension. The guide's first section is "Easy import".
- **Core AI output is a structured summary artifact**: "interactive summary Flashcards" that "highlight key information"; consistent structured format whether reading one article or twenty.
- **Analysis features**: Spotlight (jump to key findings, key concepts, contributions); "Enhance" rewrites the summary at different depths ("single sentence to a researcher level overview"); comparisons to earlier work; exploration of concepts/terms with further reading; analysis of data and figures from a paper.
- **Reading-adjacent layer**: highlights, annotations, notes attached to flashcards.
- **Library**: save flashcards, organize in folders; store references, figures, tables; refresh before lectures/meetings.
- **Synthesize/export**: export flashcards to Excel, PKMS and other formats; generate bibliographies; hand off to citation managers; import Zotero libraries for screening.
- **Collaboration** is a documented guide section (lighter detail).
- Notably **not conversation-first**: the primary interaction is import → structured summary → annotate/export; Q&A/chat is not the homepage's primary frame.

## Cross-product Comparison

| Dimension | Elicit | Consensus | Humata | Scholarcy | Reading |
|---|---|---|---|---|---|
| User-posed research task | question → chosen workflow | natural-language question | questions over uploaded files | import a document to understand | **invariant** |
| Substrate | corpus (~138M papers) + uploads + agent web/document sources | corpus (220M+) + uploads | user files only | user-imported documents | **invariant: identified research material, corpus and/or user-supplied** |
| AI performs analysis | summarize, extract-to-columns, screen, report, agentic | per-paper analysis + cross-paper synthesis + agreement analysis | summarize, compare, Q&A, rewrite | structured summary, key-findings extraction, comparison | **invariant** |
| Source attribution | sentence-level citations; report references | every claim cited, clickable; checker models | cited links into source files | flashcards trace to the document (spotlight/jump points) | **invariant (strength of guarantee varies; Elicit/Consensus state it most explicitly)** |
| Persistent artifacts + library | tables, reports, library, alerts, sessions | threads, collections, saved searches | files + chats + team rooms | flashcards, folders, notes | **common (all 4)** |
| Iterative refinement | follow-ups in agent sessions; columns/filters; load more | follow-up chat; filters; saved searches | re-ask; rewrite summaries | enhance depth; annotate | **common (all 4)** |
| Conversational Q&A | yes (chat, agent) | yes (core) | yes (core) | weakly (not primary) | common, **not defining** |
| Corpus search/discovery | yes | yes (core identity) | no | no | variant |
| Upload own documents | yes | yes | yes (only substrate) | yes (import-centric) | common |
| Structured extraction tables/columns | yes (central) | per-paper snapshots; no table-first claim observed | no | flashcard = structured per-doc summary (table-less) | common pattern, forms vary |
| Synthesis across sources | reports, agent outputs | Pro Analysis, Consensus Meter | compare documents | cross-study comparison, references | common |
| Credibility/quality signals | accuracy evals, source ranking | recency/citations/journal-impact re-ranking; study types | not observed | comparison-to-earlier-work | common in corpus-backed products |
| Export/handoff | PDF/Word reports; Zotero in | RIS/BibTeX/CSV | not observed | Excel/Word/bibliographies/citation managers | common |
| Agentic multi-step research | Research Agent (core, new) | Research Agent (newer) | no | no | emerging common (2/4) |
| Collaboration/team | multiplayer (new) | not observed | roles, folders, teams | light | variant |
| Metering/plan limits | usage pool | plan tiers | pages/answers metered | subscription | common; exact mechanics vendor-specific |
| Audience framing | pharma/academia/policy/industry researchers | researchers, students, professionals | teams, students, analysts | students, researchers | varies (audience is not defining) |

## Canonical Abstraction

### Level 0 — Defining Invariant

Minimal structure without which the product stops being recognizable as an AI Research Assistant:

```text
User-posed research task
  (a question, topic, or a body of material to understand)
    └── Source substrate: identified research material
        (product-managed corpus of papers and/or user-supplied documents)
          └── AI-performed research work
              (the assistant itself retrieves and analyzes:
               summarize / extract / compare / synthesize / screen)
                └── Source-attributed output
                    (statements traceable to specific sources)
```

Four invariants:

1. **User-posed research task** — the user brings an inquiry or a document set, not just a keyword or a blank canvas.
2. **Identified research-material substrate** — the AI works over specific, identifiable research material: a scholarly-paper corpus, the user's own uploaded documents, or both. Without a substrate, the product is a general chatbot.
3. **AI-performed research work** — the assistant, not the user, performs substantive analysis steps (retrieval, summarization, extraction, comparison, synthesis, screening). Without this, the product is an Academic Search Engine (the user reads the results).
4. **Source attribution on outputs** — AI-generated statements carry traceable references to the specific source material they derive from. Without this, the product leaves the grounded-research family entirely and becomes a general chatbot.

Historical/market-sample check: the Type is LLM-era, so there are no "older regional" instances; the overfitting risk is defining it by the current dominant pattern (chat over a paper corpus). The sample breaks each candidate over-fit: conversation is not required (Scholarcy), a paper corpus is not required (Humata, Scholarcy), "academic papers only" is not required (Humata handles arbitrary documents; Elicit's agent pulls institutional/web document sources), and chat-style interaction is not required. The four invariants above survive all samples.

### Level 1 — Common Mature Structure

Very common in the sampled products, but not required to recognize the Type:

- persistent research artifacts: threads, extraction tables, summaries, reports, and a **library/collection** where saved sources and outputs accumulate
- iterative refinement loop: follow-up questions, re-asking, adjusting scope/columns/filters, regenerating outputs
- document upload / import with AI analysis of user-supplied files
- synthesis across multiple sources (cross-paper answers, comparisons, reports)
- export and downstream handoff (documents, spreadsheets, citation formats, reference-manager interop)
- structured per-source analysis artifacts (summary cards/snapshots/flashcards; extraction columns)
- conversational Q&A over the substrate
- credibility/relevance machinery in corpus-backed products (quality-signal re-ranking, relevance checks, study-type filters)
- plan-based usage metering shaping how much AI work can be performed

### Level 2 — Variant / Optional Structure

Depends on segment, substrate, and business model:

- **substrate posture**: product-managed scholarly corpus (Elicit, Consensus) vs user-file grounding only (Humata, Scholarcy) vs corpus + uploads + broader document sources (Elicit agent)
- **workflow posture**: Q&A-first (Consensus, Humata), table/extraction-first (Elicit), summary-artifact-first (Scholarcy), report-first, agent-session-first
- **audience**: professional/industry research teams vs students vs individual knowledge workers
- **domain scope**: general science, biomedicine-heavy, or any-document
- **collaboration**: individual tool vs team workspaces/roles/permissions vs multiplayer sessions
- **business model**: freemium subscription, usage-metered (pages/answers/credits), enterprise
- **integration**: reference managers (Zotero import/export), citation formats, APIs/MCP, embeds
- **notification/monitoring** (alerts on new research) — present in one sampled product (product-specific-leaning optional)

### Level 3 — Vendor-specific (research notes only)

- Elicit: named workflow set (Find Papers / Research Report / Systematic Review / Extract Data / Chat with Papers / Research Agent), PRISMA 2020 framing, sentence-level citation guarantee, alerts, API + MCP server, monthly usage pool, multiplayer.
- Consensus: Consensus Meter (yes/no agreement visualization), Study Snapshot, three-stage search pipeline (semantic+BM25 → quality re-rank → top-20 high-precision re-rank), checker models, flag/reporting loop, "search engine, not a chatbot" self-positioning, RIS/BibTeX/CSV export, Citation Graph.
- Humata: page-count pricing, embed-in-webpage widget, OCR of scanned documents, SSO roadmap, department/folder permissions.
- Scholarcy: Flashcard Summary artifact, Spotlight, Enhance depth control, browser extension, YouTube/Drive import, Excel/PKMS export, bibliography generator.

## Vendor-specific Findings

See Level 3. None of these may be promoted to the canonical core: each is one product's design language for the same underlying invariants. Notably, two vendors have independently converged on an agentic "Research Agent" surface (Elicit, Consensus) — recorded as an emerging common structure (Level 1), not a defining one.

## Rejected Findings

- "An AI Research Assistant searches academic papers" — rejected as defining: two of four sampled products have no corpus and work purely over user files. Kept as the canonical "source substrate (corpus and/or user documents)".
- "It is a chatbot" — rejected: Scholarcy's primary surface is import → structured summary → export, with no conversational core. Conversation recorded as common, not defining.
- "It produces citations to peer-reviewed papers" (as *the* substrate definition) — narrowed: attribution is invariant, but the substrate ranges from peer-reviewed corpora to the user's own uploaded documents.
- "Multi-step autonomous agent" is part of the definition — rejected: only 2 of 4 sampled products expose agentic sessions, and both position them as newer additions.
- "Agreement/consensus visualization" — rejected: single-product design (Consensus Meter).
- Corpus-size numbers, search-pipeline stage counts, upload limits, and plan mechanics — rejected from the canonical layer (vendor-published operational detail; metering mechanics vary and change).

## Boundary Findings

- **vs Answer Engine**: answer engines respond quickly to general questions, typically from open-web sources, as one-shot Q&A. The AI Research Assistant works over a bounded research-material substrate, sustains an iterative research process, and accumulates persistent research artifacts (libraries, tables, reports). Market straddling exists: general AI answer products are adding "deep research"/project-workspace features that drift toward this Type; conversely, this Type's products answer questions. The discriminator retained: **research-material substrate + delegated multi-step analysis + persisted artifacts**.
- **vs Academic Search Engine**: search engines return ranked, refinable record lists for the user to evaluate; the assistant performs analysis on the material itself. Note: Consensus *self-describes* as an "AI-powered academic search engine" while being assistant-shaped — market language straddles this boundary; the functional discriminator is **who does the reading and synthesis**. Recorded as a soft taxonomy note, not an alias.
- **vs Academic Paper Reader**: readers center on presenting a single paper's full published content for reading/annotation; assistants operate across documents and delegate analysis. A reading surface can exist inside an assistant (and did not dominate any sample), but when single-document reading is the primary job, it is the other Type.
- **vs Reference Manager**: reference managers manage bibliographic records and citation workflows; they do not analyze content. The two interoperate heavily (import/export, bibliography generation) but neither subsumes the other in the sample.
- **vs Expert Q&A Platform / Knowledge Question Answering Application**: answers there come from humans (expert communities) or fixed knowledge bases; here analysis is performed by the AI at question time, grounded in sources.
- **vs Enterprise Knowledge Assistant / Enterprise AI Assistant**: those are organization-scoped assistants over internal company knowledge and systems; AI Research Assistants center on external research material and the individual researcher's own document set. Different substrate ownership and audience.
- **vs AI Coding Agent**: same "delegated AI work" pattern, but substrate and deliverable are code/project changes, not research material and cited findings.
- **Removal tests ("去掉什么就变成另一个 Type")**: remove AI-performed analysis → Academic Search Engine; remove research-material substrate → general chatbot (outside this family); remove attribution/grounding → general chatbot; reduce to single-document presentation → Academic Paper Reader; remove AI entirely, keep bibliographic management → Reference Manager; remove persistence entirely and answer from the open web → Answer Engine.

## Uncertainties

- **NotebookLM, SciSpace, Scite could not be documented** (fetch failures). NotebookLM is widely known to represent a user-document-grounded notebook philosophy; if true, it would strengthen the "substrate varies" invariant rather than change it — but no claim about it is made in the final document.
- Whether "agentic multi-step research sessions" will consolidate into a standard expectation (currently emerging common, 2/4 products, both recent).
- The strength of the attribution guarantee varies (explicit sentence-level claims vs link-into-source claims vs implicit traceability). The canonical layer says "outputs carry traceable references"; how strictly each product guarantees this is vendor-specific.
- Non-English/regional markets were not sampled; the corpus-backed products' coverage claims are English-literature-centric by vendor admission (major journals, PubMed etc.). No regional exception is expected to affect L0, but this is unverified.
- Collaboration depth varies and is recently evolving (Elicit multiplayer is new); the canonical treatment (variant) may need revisiting if team-based research assistance becomes dominant.

## Final Synthesis

An **AI Research Assistant** is an application in which the user poses a research task — a question, a topic, or a body of documents to understand — and the system itself performs substantive research work over identified source material: it retrieves, summarizes, extracts, compares, and synthesizes, and it delivers its outputs with traceable references to the specific sources behind each claim. Around this core, mature products add persistent artifacts (extraction tables, structured summaries, reports, libraries), iterative refinement (follow-ups, re-analysis, scope changes), document import, export/handoff to writing and citation tools, and credibility machinery. Products differ primarily in substrate (product-managed scholarly corpus vs user-supplied files vs both), workflow posture (Q&A-first, table-first, summary-artifact-first, report-first, agent-first), and audience (students to enterprise research teams). The Type is distinct from an Answer Engine (one-shot open-web answers, no sustained research process), from an Academic Search Engine (the user, not the AI, does the reading), from an Academic Paper Reader (single-document presentation rather than cross-document delegated analysis), and from a Reference Manager (bibliographic records without content analysis).
