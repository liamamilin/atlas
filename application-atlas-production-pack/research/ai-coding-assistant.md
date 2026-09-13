# Research Notes — AI Coding Assistant

## Research Goal

Understand, from real products, what an **AI Coding Assistant** is as an Application Type: what its defining structure is, how the two canonical assistance loops (inline completion, code chat) actually work, what the human does at each step, how assistance is customized and governed, and where the boundary lies against the adjacent Types **AI Coding Agent** (sibling leaf, already processed), **Code Editor / IDE**, generic **AI chatbot / Enterprise AI Assistant**, and **Answer Engine**.

This leaf was processed **after** its sibling AI Coding Agent (2026-09-06), which flagged: "assistant = human performs each step; agent = AI performs the loop — an autonomy gradient, not a wall; vendors ship both structures inside one product line; flagged for joint review when AI Coding Assistant is processed." This research pass is that joint-review evidence pass from the assistant side.

## Initial Boundary

Preliminary hypothesis before research:

- An AI Coding Assistant is AI assistance **embedded in the developer's coding flow** — suggesting code completions as they type, answering questions about their code, generating snippets on request — where the **human performs each step** and applies or rejects each AI output.
- Nearest neighbors: AI Coding Agent (sibling — boundary flagged), Code Editor / IDE (assistants usually ship as editor plugins), generic AI chatbot / Enterprise AI Assistant (§13), Answer Engine / AI Research Assistant (§02.03), AI Software Engineering Agent (§12).
- Key suspected boundary: who holds the execution loop (see sibling research).
- Known unknowns: whether completion and chat are both definitional or one is enough; whether editor-embeddedness is definitional; how vendors partition assistant vs agent features inside one product; privacy/deployment variants; the effect of the 2025–2026 "everything is an agent" market drift on the Type.

## Research Questions

1. What are the canonical **assistance loops** — what does the human do, what does the assistant do?
2. What **context** does the assistant ground its output in (buffer, selection, workspace, attachments, conversation)?
3. What is the **unit of output** and who applies it?
4. How do **customization mechanisms** work (instructions, behaviors, tailored completions)?
5. How do **enterprise administration** surfaces work (policy, access, analytics, audit)?
6. How do vendors themselves **partition assistant vs agent** structure inside one product line?
7. What **surfaces** exist (IDE plugin, AI-native IDE, CLI, web, chat apps)?
8. What **privacy / deployment** variants exist (cloud vs self-hosted)?
9. What distinguishes an assistant from **editor autocomplete** (pre-AI) and from a **generic chatbot**?
10. What is drifting in the market (agent bundling, product repositioning), and does the assistant structure survive as a distinct Type?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / Position | Customer tier |
|---|---|---|---|
| GitHub Copilot | GitHub / Microsoft | the archetype assistant; editor-agnostic plugin + platform-embedded; officially partitions features into "Assistive" and "Agentic" | individual (free tier) → enterprise |
| JetBrains AI Assistant | JetBrains | IDE-vendor-native assistant inside traditional IDEs; documents Chat-vs-Agent modes explicitly | individual → enterprise |
| Tabnine | Tabnine | privacy-first, "fully private, organization-aware", runs entirely within the customer environment; completion+chat heritage | teams → enterprise |
| Amazon Q Developer | AWS | cloud-ecosystem conversational assistant; IDE plugins + console/chat-app surfaces; being sunset toward an agentic product (Kiro) | individual (free tier) → Pro/enterprise |

All four document both the assistant structure and a bundled agent structure — which is itself a finding (see Boundary Findings).

## Sources

Research date: **2026-09-06**. All sources fetched live on this date; **no fetch failures** (no source-access limitation applies this pass).

### GitHub Copilot (Tier 1 — official product documentation)

- What is GitHub Copilot: https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot
- GitHub Copilot features (Assistive vs Agentic partition): https://docs.github.com/en/copilot/get-started/features
- Getting code suggestions in your IDE (per-IDE how-to: JetBrains, Visual Studio, VS Code, Vim/Neovim, Azure Data Studio, Xcode, Eclipse): https://docs.github.com/en/copilot/how-tos/get-code-suggestions/get-ide-code-suggestions

### JetBrains AI Assistant (Tier 1 — official product documentation)

- AI Assistant in JetBrains IDEs (IDEA 2026.2 help): https://www.jetbrains.com/help/idea/ai-assistant.html
- AI Chat (modes, models, context, response processing): https://www.jetbrains.com/help/ai-assistant/ai-chat.html

### Tabnine (Tier 1 — official product documentation)

- Overview: https://docs.tabnine.com/
- Tabnine Chat: https://docs.tabnine.com/main/getting-started/tabnine-chat.md
- Tabnine Agent (explicit assistant-vs-agent contrast): https://docs.tabnine.com/main/getting-started/tabnine-agent.md

### Amazon Q Developer (Tier 1 — official product documentation)

- What is Amazon Q Developer: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html
- Using Amazon Q Developer in the IDE (feature availability table): https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html
- Generating inline suggestions: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/inline-suggestions.md

---

## Product A — GitHub Copilot

### Key observations (evidence layer A unless noted)

- Self-description: "GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort."
- **Official feature partition** (features page, verbatim categories):
  - **"Assistive features"** — "These tools are used **synchronously**, providing advice or suggestions **as people work on a task**": Copilot Chat (ask coding questions; available on website, Mobile, IDEs, Windows Terminal); **Inline suggestions** (autocomplete-style, in supported IDEs; plus **next edit suggestions** in VS Code/Xcode/Eclipse that "predict the location of the next edit you are likely to make"); PR summaries; commit-message generation in GitHub Desktop.
  - **"Agentic features"** — "These features can **work autonomously without direct human supervision**. However, they typically need human approval to perform sensitive actions": Copilot CLI, GitHub Copilot app (desktop, parallel agent sessions, automations), Copilot cloud agent, third-party agents, code review, **agent mode in IDEs** ("Copilot will determine which files to make changes to, offer code changes and terminal commands for the user's approval, and iterate to remediate issues until the original task is complete").
- **Completion mechanics** (per-IDE how-to): suggestions appear as grayed text while typing; natural-language comments in code trigger code suggestions; **Tab accepts, Esc rejects**; alternatives cycleable (prev/next) and viewable in a multi-suggestion tab; **partial acceptance** (accept next word / next line); "Copilot will attempt to match the context and style of your code. You can always edit the suggested code."; duplication-detection policy can suppress suggestions matching public code; the completion model itself is user-switchable.
- **Surfaces**: IDEs (VS Code, full JetBrains suite, Visual Studio, Xcode, Eclipse, Vim/Neovim, Azure Data Studio), GitHub website, GitHub Mobile, Windows Terminal, GitHub CLI, GitHub Copilot desktop app.
- **Customization**: Copilot Spaces (organize code/docs/specs as grounding context for a task), custom instructions, prompt files (reusable Markdown prompts in the workspace), Copilot Memory, MCP servers, agent skills, custom agents.
- **Administration** (Business/Enterprise): policy management, access management (who gets Copilot), usage data, audit logs, **file exclusions** (content Copilot must ignore).
- **Access tiers**: Copilot Free; Pro / Pro+ / Max; Business / Enterprise; free for students, teachers, OSS maintainers; org/enterprise enablement flows.

## Product B — JetBrains AI Assistant

### Key observations (evidence layer A unless noted)

- Positioning: "AI Assistant brings AI-powered coding agents and AI features directly into IntelliJ IDEA"; compatible with almost all JetBrains IDEs.
- **AI Chat interaction pattern** (official, four steps): select how to interact (chat vs agent) → select model (JetBrains AI service, third-party provider with own key (BYOK), or locally hosted) → add context (files, folders, images, symbols, commits) → process the response (review; apply changes as needed).
- **Chat mode defined against the agent** (official, verbatim): "In this mode, the AI provides responses and suggestions **but does not apply changes to your project automatically**. Any generated code needs to be **reviewed and applied manually**." vs Agents: "perform **multi-step actions** in your project, **modify multiple files**, and report progress during execution. You can review the results and **keep or roll back** the changes."
- **In-editor code assistance**: "autocomplete single lines and entire blocks of code following your coding style and naming conventions. **Next edit suggestions** then recommend your next edits and move you to the following place that might need a change."
- Conversations: persistent chat history, new chats per topic, chat can open in an editor tab.
- Setup flexibility: JetBrains AI subscription, BYOK, agent authorization with provider accounts, local models.

## Product C — Tabnine

### Key observations (evidence layer A unless noted)

- Overview: "Tabnine is a **fully private, organization-aware** AI coding agent designed to **run entirely within your environment**… to deliver real-time, secure code assistance and automated workflows."
- **The assistive base is named explicitly** (Agent page, verbatim): "Tabnine Agent extends the capabilities of Tabnine **beyond inline code completion and conversational chat**…" — i.e., the two assistant capabilities are **inline code completion** and **conversational chat**, and the agent is defined as the thing beyond them.
- **Agent vs chat contrast** (official): Tabnine Chat = "on-demand natural language conversations" (explaining code, generating snippets, answering documentation queries); Tabnine Agent = "**operates autonomously to achieve the user's specified goal**… codebase-wide refactoring, automated test generation, documentation synthesis, policy validation", while "maintain[ing] a tight feedback loop with the developer… independently determines when to check in for input or approval."
- **Chat loop** (official): launch in IDE → ask questions / give instructions → "**read, review, and apply**" the response within the code. Supports **quick actions** (predefined prompts for specific use cases), custom chat behaviors and response length, separate conversations per task, chat context selection ("make sure you've selected the relevant code before you ask a question").
- **Administration**: analytics, team management, user management, **Context Engine** (admin-managed context), settings, APIs.
- SaaS fair-use token consumption limit per user per day (EMT customers) — operational figure, L3.

## Product D — Amazon Q Developer

### Key observations (evidence layer A unless noted)

- Positioning: "a **generative artificial intelligence (AI) powered conversational assistant** that can help you understand, build, extend, and operate AWS applications… When used in an integrated development environment (IDE), Amazon Q provides **software development assistance**: chat about code, provide **inline code completions**, generate net new code, scan your code for security vulnerabilities, and make code upgrades and improvements."
- **Surfaces**: AWS Management Console / docs website / AWS website / console mobile app (chat); IDEs — VS Code, JetBrains, Visual Studio, Eclipse (+ AWS coding environments: Cloud9, Lambda console, SageMaker Studio, JupyterLab, Glue Studio); chat applications (Microsoft Teams, Slack).
- **IDE feature availability table** (official): rows = Chat, **Agentic coding**, MCP servers, Context in chat, **Inline chat**, Workspace context in chat, **Inline suggestions**, Transformations (Java language upgrades) — chat and agentic coding listed as distinct capabilities per IDE.
- **Inline suggestions** (official): "code recommendations in real time… based on your existing code and comments. Filenames are also taken into consideration… ranging from a single line comment to fully formed functions"; pause/resume auto-suggestions per IDE; suggestions customizable "to your software development team's internal libraries, proprietary algorithmic techniques, and enterprise code style"; **code references** (attribution of suggestions to open-source-adjacent training data surfaced to the user); walkthrough shows comment→suggestion→Tab-accept loop and arrow-key cycling through multiple suggestions.
- **Sunset notice** (official): "On April 30, 2027, AWS will discontinue support for Amazon Q Developer IDE plugins. For capabilities similar to… explore **Kiro** to access the latest models and features, including **agentic coding**, chat and MCP support." — a sampled assistant product being steered toward an agentic successor while chat + completions carry over.
- Access: AWS Builder ID (no AWS account) for free IDE use; Free tier + Pro subscription; powered by Amazon Bedrock (single augmented model; no user-facing model picker observed in sampled pages).

---

## Cross-product Comparison

| Dimension | GitHub Copilot | JetBrains AI Assistant | Tabnine | Amazon Q Developer |
|---|---|---|---|---|
| Self-description | "AI coding assistant" | "AI-powered coding agents and AI features" in IDEs | "fully private, organization-aware AI coding agent… real-time, secure code assistance" | "generative AI powered conversational assistant" |
| Inline completion as you type | yes (grayed text; Tab accept / Esc reject; word/line partial accept; alternatives) | yes (single lines and blocks "following your coding style") | yes (named as base capability: "beyond inline code completion") | yes ("in real time… single line comment to fully formed functions") |
| Code chat | Copilot Chat (IDE/web/mobile/terminal) | AI Chat (tool window / editor tab) | Tabnine Chat (in IDE; quick actions) | Chat (IDE, console, chat apps) |
| Context grounding | open code + Spaces (curated code/docs/specs) + custom instructions | attachments: files, folders, images, symbols, commits | chat context selection; admin Context Engine | existing code, comments, filenames; workspace context; context in chat |
| Response application | human accepts (Tab) / edits; "you can always edit the suggested code" | "reviewed and applied manually" (Chat mode) | "read, review, and apply" | Tab accept; arrow-key cycling |
| Next-edit suggestions | yes (VS Code, Xcode, Eclipse) | yes ("recommend your next edits") | not observed in sampled pages | not observed in sampled pages |
| Model selection | yes (user-switchable completion model; multiple models) | yes (JetBrains service / BYOK / local models) | AI models page (multi-model; details not sampled) | not observed (Bedrock-augmented single model) |
| Customization | custom instructions, prompt files, Spaces, Memory, skills | behavior via prompts; setup flexibility (subscription/BYOK) | custom chat behaviors; suggestions tailored to internal libraries/style | suggestions tailored to internal libraries / enterprise style |
| Attribution / public-code posture | duplication detection policy (can suppress public-code matches) | not observed | not observed | code references (attribution) |
| Enterprise administration | policy mgmt, access mgmt, usage data, audit logs, file exclusions | subscription/activation management (sampled) | analytics, team/user mgmt, Context Engine, APIs | IAM permissions; Pro tier (sampled) |
| Bundled agent structure | agent mode in IDEs, CLI, cloud agent, Copilot app, code review | Junie + external agents (ACP), agent mode | Tabnine Agent (CLI/IDE) | Agentic coding row; Kiro successor |
| Deployment posture | cloud (data residency option for enterprises) | cloud service / BYOK / local models | "runs entirely within your environment" (self-hosted posture) | cloud (AWS-native) |

### Cross-product commonalities (evidence layer B)

Observed across all four sampled products (or noted where fewer):

1. **AI assistance delivered inside the coding environment** — all four operate where the developer writes code (IDE plugin, AI-native IDE, editor-embedded chat), optionally extending to adjacent surfaces.
2. **Inline completion as you type** — all four document it (Copilot, JetBrains, Q explicitly; Tabnine names it as its base capability). Triggered by coding activity; human accepts/rejects.
3. **Chat about the code/project** — all four. Natural-language Q&A, explanations, snippet generation, with conversation history (documented for JetBrains; Tabnine conversations; Copilot/Q chat surfaces).
4. **Grounding in the developer's context** — all four shape responses from code context: buffer/selection/comments/filenames at completion time; attachments (files/folders/symbols/commits), workspace context, or curated context collections at chat time.
5. **The human applies each output** — all four: Tab accept / Esc reject (Copilot, Q), "reviewed and applied manually" (JetBrains chat mode), "read, review, and apply" (Tabnine).
6. **A bundled agent structure** — all four ship an autonomous mode/product alongside the assistant (agent mode/CLI/cloud agent; Junie + external agents; Tabnine Agent; Agentic coding/Kiro), and **all four vendors document the assistant-vs-agent contrast themselves** — the strongest available evidence for the Type boundary.
7. **Customization of assistance** — three of four directly observed (Copilot instructions/prompt files; Tabnine behaviors + tailored completions; Q tailored completions); JetBrains offers model/setup customization.
8. **Enterprise administration surfaces** — observed in Copilot (policy/access/usage/audit/exclusions) and Tabnine (analytics/team/user mgmt/Context Engine); common in team/enterprise offerings generally, treated here as common mature structure for org deployments.
9. **Next-edit suggestions** — two of four directly observed (Copilot, JetBrains) → common but not universal; keep out of the core.
10. **Attribution / public-code posture** — two of four (Copilot duplication detection; Q code references) → optional.

### What varies (candidate L2)

- **Surface form**: editor-agnostic plugin (Copilot, Q) vs IDE-vendor-native assistant (JetBrains) vs privacy/self-hosted deployment (Tabnine) vs multi-surface beyond the IDE (web console, chat apps, mobile, terminal).
- **Assistance posture**: completion-first heritage vs chat-first packaging.
- **Domain focus**: general-purpose vs ecosystem-specialized (Q/AWS: architecture, resources, AWS SDKs; Java transformations).
- **Model strategy**: single augmented model (Q) vs user-selectable multi-model (Copilot, JetBrains) vs enterprise-governed models (Tabnine).
- **Deployment/privacy posture**: cloud SaaS (with data-residency options) vs "run entirely within your environment".
- **Customer packaging**: free individual tiers → org/enterprise plans with governance.
- **Bundled agent depth**: from a mode inside the chat to standalone agent products; actively drifting (see below).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Human-driven coding flow (the developer performs each step of the coding work)
└── AI assistance embedded in that flow
    ├── responding to the developer's in-flight coding activity or an explicit request
    ├── grounded in the developer's coding context
    │   (the code being written — buffer/selection — and the project around it,
    │    plus the ongoing conversation)
    └── producing a suggestion / answer / snippet
        └── which the developer reviews and applies (or rejects) themselves
```

Four properties. Remove any one and the product stops being recognizable as an AI Coding Assistant:

- **Human holds the execution loop.** The developer performs the coding work; the assistant reacts — to typing (completions) or to a question/instruction (chat). The unit of work is a suggestion or an answer, never a delegated task. Without this, the product is an AI Coding Agent.
- **AI model as the assistance mechanism.** Output is model-generated and context-adapted (whole lines to whole functions, natural-language explanations), not rule-based templates. Without this, the product is classic editor autocomplete / IntelliSense / snippet expansion — an editor capability, not this Type.
- **Grounding in the developer's coding context.** The response is shaped by the code being written and the project around it (buffer, selection, comments, filenames, attachments, workspace, conversation). Without this, the product is a generic AI chatbot / answer engine.
- **Suggestion applied by the human, step by step.** Nothing changes in the project until the developer accepts, edits, or rejects the output in their own editing flow. Without this, the product is an agent.

Historical/market-sample check (§24): the definition is satisfied by completion-only assistants with no chat (the founding form), by chat-only assistants with no completion, by IDE-vendor-native and editor-agnostic plugin forms, and by cloud and self-hosted deployments. Neither chat, nor completion, nor a particular IDE, nor cloud delivery is required — the two assistance loops are both *typical* but the invariant is the assistance relationship itself (context-grounded, human-applied). Precursors to the AI era (deterministic autocomplete, snippet libraries) are excluded by the AI-mechanism property; the Type's history begins with model-based completion and quickly added chat.

### L1 — Common Mature Structure

Present in most mature products; expected by the market but not definitional:

- **Inline completion as you type** — grayed inline text triggered by coding activity; accept (Tab) / reject (Esc) / cycle alternatives / partial acceptance (word or line); suggestions matched to the file's context and style.
- **Code chat with history** — a chat surface (sidebar or inline) for questions, explanations, snippet generation; conversations persisted and organized per topic.
- **Context control** — automatic context (current file, selection, open files, workspace, filenames) plus explicit context attachment (files, folders, symbols, images, commits) and curated context collections; admin-managed context in enterprise deployments.
- **Quick actions / predefined prompts** — one-click explain / fix / generate-tests / document / commit-message actions.
- **Next-edit suggestions** — predicting the next place the developer is likely to edit (observed in two of four; increasingly common).
- **Model selection** — choosing among models (vendor service, third-party keys, local models) where offered.
- **Customization** — custom instructions / behavior settings; completions and chat tailored to internal libraries and house style.
- **Apply mechanics for generated code** — reviewing chat-generated code and applying it to files (with diff presentation) without autonomous execution.
- **Enterprise administration** — policy management, access assignment, usage analytics, audit logs, content exclusions (for org/enterprise deployments).
- **Attribution / public-code posture** — duplication detection or code-reference surfacing (observed in two of four; optional).

### L2 — Variant / Optional Structure

- **Surface**: editor-agnostic plugin, IDE-vendor-native assistant, AI-native editor bundle, terminal/CLI chat, web/console surfaces, chat-app integrations, mobile.
- **Assistance posture**: completion-first vs chat-first packaging.
- **Deployment/privacy posture**: cloud SaaS (with data-residency options) vs self-hosted / "runs entirely within your environment"; security-sensitive governance (content exclusions, private model operation).
- **Domain focus**: general-purpose vs ecosystem-specialized (cloud provider APIs, architecture, specific languages/frameworks).
- **Model strategy**: single augmented model vs multi-model selection vs BYOK/local models.
- **Customer packaging**: free individual tiers → org/enterprise subscriptions with governance.
- **Bundled agent structure**: the agent mode/product shipped alongside the assistant (the dominant 2025–2026 market pattern).
- **Adjacent assistive outputs**: commit messages, PR summaries/descriptions, code review suggestions, security scanning, language-transformations (observed in one or two products each; optional).

### L3 — Vendor-specific Structure (Research Notes only)

- Copilot: "Assistive vs Agentic" feature taxonomy; Copilot Spaces / Memory / prompt files / custom agents; duplication detection policy; per-IDE keyboard mappings (Tab/Esc, Alt+], Ctrl+Enter multi-suggestion tab, Accept Word); plan names (Free/Pro/Pro+/Max/Business/Enterprise); GitHub Copilot desktop app; next-edit gutter arrow; data residency for Enterprise Cloud.
- JetBrains: Junie; Agent Client Protocol (ACP) for external agents; DPAIA open benchmark + "JetBrains Pick" default-agent recommendation; BYOK and local-model connection; chat-in-editor-tab layout; 2026.2 help vintage.
- Tabnine: Context Engine (admin-managed); quick actions naming; custom chat behaviors/response length; EMT SaaS fair-use per-user daily token limit; "run entirely within your environment" deployment.
- Amazon Q Developer: Kiro transition and the 2027-04-30 IDE-plugin end-of-support date; AWS Builder ID sign-in; Bedrock augmentation ("high quality AWS content"); code references; transformations (Java); AWS coding-environment surfaces (Cloud9, Lambda, SageMaker Studio, JupyterLab, Glue Studio); Teams/Slack channels.

## Vendor-specific Findings

- **Copilot's "Assistive vs Agentic" page taxonomy** is the most explicit vendor statement of the Type boundary found anywhere in the sample: assistive = "used synchronously, providing advice or suggestions as people work on a task"; agentic = "can work autonomously without direct human supervision… typically need human approval to perform sensitive actions."
- **JetBrains' Chat-mode definition** is equally explicit: chat "does not apply changes to your project automatically… reviewed and applied manually"; agents "perform multi-step actions… modify multiple files."
- **Tabnine defines itself through the same contrast**: its base is "inline code completion and conversational chat"; its Agent "operates autonomously to achieve the user's specified goal" while checking in for approval.
- **Amazon Q Developer's feature table** lists "Chat" and "Agentic coding" as separate rows; the product is being sunset toward Kiro, an agentic successor, while chat and completions carry over.
- Vendor positioning drift: three of four sampled products now lead their marketing with the word "agent" (Tabnine, JetBrains, Q/Kiro) even though the assistant structure remains their base. The word has drifted; the structure has not (assistant loops remain documented and central in all four).

## Rejected Findings

- **"IDE plugin" is NOT definitional.** Assistants appear as IDE-vendor-native features, in terminal/chat surfaces, and in AI-native editors; the plugin is the dominant *delivery form*, not the invariant.
- **"Inline completion is the definition" is NOT accepted.** Completion is the founding loop and present in all four samples, but chat-only assistants satisfy the Type; the invariant is the assistance relationship (context-grounded, human-applied), not a specific loop.
- **"Chat is the definition" is NOT accepted** for the symmetric reason.
- **"Suggestions must be code-only" is NOT accepted.** Sampled assistants also explain, answer documentation questions, generate commit messages, and summarize PRs; the object is *assistance around the coding work*, with code application as the center of gravity.
- **"Cloud delivery" is NOT definitional** (Tabnine's self-hosted posture satisfies the Type).
- **"Free tier"** and other pricing shapes are market packaging, not Type structure.
- **"The AI Coding Assistant is dead / absorbed by agents"** is NOT supported: every sampled product still documents the assistive structure as a working, first-class part of the product (synchronous loops, manual apply), even when marketing leads with agents.

## Boundary Findings

### vs AI Coding Agent (sibling leaf — most important boundary)

The structural difference is **who holds the execution loop**:

- **Assistant**: the human performs each step of the coding work; the AI responds within the human's flow (completion as they type, answers when asked); the unit of work is a suggestion/answer; initiative stays with the human; each output is applied or rejected by the human.
- **Agent**: the human delegates a task; the AI performs a multi-step loop (search → edit → run → verify) and the human reviews the outcome; the unit of work is the delegated task; initiative passes to the AI for the duration of the run.

Evidence that the boundary is real and vendor-recognized: **all four sampled vendors partition the two structures inside one product line** (Copilot "Assistive features" vs "Agentic features"; JetBrains Chat mode vs Agents; Tabnine Chat vs Tabnine Agent, including "beyond inline code completion and conversational chat"; Amazon Q "Chat" vs "Agentic coding" table rows).

Boundary test: hand the product a goal — does it stop at a suggestion/answer the human applies (assistant), or does it apply project changes itself and iterate to completion, with the human reviewing the result (agent)?

Convergence facts, recorded for the joint review already flagged by the sibling research: every sampled product bundles both structures; single products increasingly blur packaging (agent modes inside assistants, assistant modes inside agents); one sampled assistant product (Amazon Q Developer IDE plugins) is being discontinued in favor of an agentic successor. The two leaves are best understood as adjacent points on an **autonomy gradient**: the Type describes structures (assistive loops vs agentic loop), and a given product may implement both. No taxonomy change made unilaterally.

### vs Code Editor / IDE

The editor's primary object is the file the human edits, and its assistance was historically deterministic (autocomplete, snippets, refactoring inspections). The AI Coding Assistant is a distinct Type that (a) uses model-generated output and (b) exists to be embedded in the editor's flow. Most delivery today is *inside* editors — plugin or native — so "editor with AI features" is a bundle of two Types (editor + assistant). Distinction test: remove the editor UI — an assistant's value proposition (context-grounded suggestions/answers, human-applied) survives in a terminal/web chat over the same project; an editor's does not.

### vs generic AI chatbot / Enterprise AI Assistant (§13)

A chat that answers questions with no grounding in the developer's code or workflow is a generic assistant/answer surface. The AI Coding Assistant is defined by grounding in the coding context and by application mechanics inside the developer's flow. Products that serve both (e.g., cloud-console chat surfaces of an assistant product) exercise the adjacent Type on those surfaces.

### vs Answer Engine / AI Research Assistant (§02.03)

Asking general technical questions without code context drifts toward the answer-engine Type; the assistant's chat is anchored to the developer's code and project.

### vs Code Review Platform / assistive add-ons

Commit-message generation, PR summaries, and AI review suggestions (observed in one sampled product as packaged features) are assistance applied to *adjacent artifacts* of the coding workflow. They are optional assistant capabilities when embedded in the flow; a product whose primary object is the review workflow itself is a Code Review Platform.

### 去掉什么就变成另一个 Type 判据

- Remove **human-holds-the-loop** (the AI applies changes and iterates toward a goal) → **AI Coding Agent**.
- Remove **AI model as mechanism** (deterministic rule-based completion/snippets) → editor autocomplete / snippet feature of a **Code Editor**.
- Remove **coding-context grounding** (answers arbitrary questions) → generic **AI chatbot / Enterprise AI Assistant**; research-flavored variants → **Answer Engine**.
- Remove **coding scope** (assists arbitrary knowledge work in the org) → **Enterprise AI Assistant** (§13).
- Remove **human-applies-each-output** while keeping code scope → **AI Coding Agent** (same as first test).

## Uncertainties

1. **Tabnine completion details** — Tabnine's sampled pages name "inline code completion" as its base capability but do not document its mechanics (accept/reject controls). Treated as present-but-not-detailed; no precise claims made.
2. **Next-edit suggestions coverage** — directly observed in two of four; market prevalence likely higher; kept as common-but-not-universal.
3. **Model selection** — observed in two of four (Copilot, JetBrains); Q samples show a single augmented model. Whether model selection becomes universal is a moving target.
4. **Market drift velocity** — vendors are actively repositioning assistants as agents (three of four lead with "agent" in self-description; Q IDE plugins sunset 2027). The assistant structure is documented and first-class in all four today, but packaging may shift faster than this document's shelf life. The joint-review framing ("autonomy gradient; both structures in one product line") is robust to that drift; a strict two-leaf split may need revisiting as products converge further.
5. **AI Software Engineering Agent leaf (§12 sibling)** — not sampled this pass; per the sibling research it is a probable alias/variant of AI Coding Agent. Untouched here; joint-review item.
6. **Non-English/regional assistant products and open-source assistants** (e.g., editor plugins for local models) were not deeply sampled; the historical check covers them structurally (completion-only, chat-only, self-hosted all satisfy the definition), not with product-specific evidence.

## Final Synthesis

The AI Coding Assistant is defined by an **assistance contract**: the developer keeps the execution loop, and the AI supplies context-grounded suggestions and answers *inside* the developer's flow, each of which the developer applies or rejects. Its two canonical loops — inline completion responding to typing, and chat responding to questions/instructions — are the mature realization of that contract; context control, customization, apply mechanics, and enterprise governance make it practical; surfaces, deployment posture, domain focus, and model strategy are variants. Everything agentic — delegated tasks, autonomous loops, reviewable multi-file changes — belongs to the neighboring AI Coding Agent Type, with which this Type forms an autonomy gradient that vendors themselves recognize, document, and bundle inside single product lines.
