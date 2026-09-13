# AI Coding Assistant

## Overview

An **AI Coding Assistant** is AI assistance embedded in a developer's coding flow: it suggests code as the developer types, answers questions about the developer's code and project, and generates snippets or edits on request — while the **developer performs each step of the coding work** and applies or rejects every AI output.

The defining structure is small:

```text
Human-driven coding flow (the developer performs each step)
└── AI assistance embedded in that flow
    ├── responding to the developer's in-flight coding activity or an explicit request
    ├── grounded in the developer's coding context
    │   (the code being written, the project around it, the ongoing conversation)
    └── producing a suggestion / answer / snippet
        └── which the developer reviews and applies (or rejects) themselves
```

Everything commonly associated with current products — inline completion mechanics, chat panels, model selection, enterprise governance, self-hosted deployment — is standard in the market but is not what makes a product an assistant. The defining property is the assistance relationship itself: the assistant reacts to the human's work and never pushes work to completion on its own. When a product instead takes a delegated task and executes it end to end — editing files, running commands, iterating until done — it is exercising a different Type, the AI Coding Agent. Most current products implement both structures side by side; see Related Application Types.

## Users & Context

The primary user is a **software developer** who is actively writing or maintaining code and wants help without giving up control of the keyboard: completing boilerplate or unfamiliar APIs, understanding code they did not write, generating a first draft of a function or a test, getting a fix for a small error, or drafting commit messages and descriptions.

The relationship between developer and assistant has a characteristic shape:

- **The developer initiates.** Assistance arrives in response to the developer's own activity (typing triggers completions) or an explicit request (a question, an instruction, a quick action).
- **The developer decides.** Every output — a completion, a snippet, a suggested edit — is accepted, edited, partially accepted, or discarded by the developer.
- **The developer stays in the loop.** Even when the assistant generates a whole function, the developer reads it, adjusts it, and owns the result.

Secondary users appear in organizational settings: **team administrators** who govern what the assistant may see and suggest (content exclusions, access, policies) and who review usage analytics; and **platform owners** who configure context sources and model access.

Typical context of use is a developer's IDE or editor during day-to-day coding, with the assistant present continuously but acting only on request or on in-flight coding activity. Some products extend to adjacent surfaces — terminal chat, web console, mobile, team chat applications — sharing the same underlying assistance.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as an AI Coding Assistant:

- **Human holds the execution loop.** The developer performs the coding work; the assistant responds within the human's flow. The unit of work is a suggestion or an answer — never a delegated task. Remove this and the product becomes an AI Coding Agent.
- **AI model as the assistance mechanism.** Output is model-generated and context-adapted — anything from a single line to a whole function, or a natural-language explanation. Remove this and the product is classic deterministic editor autocomplete or snippet expansion, an editor capability rather than this Type.
- **Grounding in the developer's coding context.** Responses are shaped by the code being written and the project around it: the current file and selection, comments and filenames, attached files or symbols, the workspace, and the conversation history. Remove this and the product is a generic AI chatbot.
- **Human-applied output, step by step.** Nothing changes in the project until the developer accepts, edits, or rejects the output in their own editing flow. Remove this and the product becomes an agent.

Both canonical assistance loops rest on this core:

- **Completion loop** — the assistant watches the developer's in-flight typing and offers inline suggestions that continue or fulfill the code being written, including code implied by a natural-language comment the developer just wrote.
- **Chat loop** — the developer asks a question or gives an instruction in natural language; the assistant answers, explains, or generates code, using the developer's selected or automatic context.

Older or narrower products satisfy the core with only one of the two loops (completion-only assistants with no chat were the founding form; chat-only assistants exist), which is why neither loop alone is part of the definition.

### Standard Capabilities

A typical modern assistant carries most of these capabilities. They make the assistance practical; they are not what makes the product an assistant.

- **Inline suggestions with fine-grained control** — suggestions rendered as ghost text in the editor; accept or reject the whole suggestion, cycle through alternatives, or accept partially (next word, next line); suggestions matched to the file's context and style.
- **Code chat with history** — a chat surface (sidebar or inline in the editor) for questions, explanations, and snippet generation; conversations persisted and organized by topic so work can continue later.
- **Context control** — automatic grounding (current file, selection, open files, workspace, filenames) plus explicit attachment (files, folders, symbols, images, commits) and curated context collections for specific tasks; in organizations, admin-managed context sources.
- **Quick actions** — predefined one-click prompts for recurring jobs such as explaining code, fixing a problem, generating tests or documentation, or drafting a commit message.
- **Customization** — persistent custom instructions or behavior settings; completions and chat tailored to the team's internal libraries and house style.
- **Apply mechanics for generated code** — reviewing chat-generated code and applying it to files, presented as a reviewable change rather than a silent write.

Several further capabilities are widespread but product- or deployment-dependent — model selection (including third-party or locally hosted models), enterprise administration, self-hosted deployment, and attribution of suggestions — and are listed under Variants below.

### One Structure, Many Implementations

The core model is written conceptually. Common implementations differ:

```text
Concept:      Embedded in the developer's flow
Realizations: plugin in an existing editor, assistant built into an IDE by its vendor,
              assistant inside an AI-native editor, terminal or web chat over the same project

Concept:      Coding-context grounding
Realizations: current buffer/selection at completion time; attached files/symbols/commits
              or workspace indexing at chat time; curated context collections

Concept:      AI mechanism
Realizations: vendor-hosted models, third-party models, locally hosted models

Concept:      Human-applied output
Realizations: keyboard accept/reject on inline text; explicit "apply" on chat-generated code
```

A reader who has only seen one delivery form (for example, a plugin in a mainstream editor) should be able to recognize the others — including self-hosted or terminal-based forms — from the defining core.

## How It Works

### The completion loop

```text
Developer types code (or a natural-language comment describing intent)
→ the assistant generates an inline suggestion from that context
→ the developer accepts it (whole or partially), cycles through alternatives, or rejects it
→ the accepted code becomes part of the file and the context for the next suggestion
```

The loop is silent by default: it runs continuously as the developer works, costs no explicit action, and interrupts nothing. Suggestions are advisory — nothing enters the file unless the developer accepts it.

### The chat loop

```text
Developer asks a question or gives an instruction in the chat surface
→ optionally attaches or selects context (files, symbols, folders, the current selection)
→ the assistant answers, explains, or generates code using that context
→ the developer reviews the response
→ generated code is applied to the file(s) manually (or discarded)
→ the conversation persists for follow-ups
```

Compared with the completion loop, the chat loop is deliberate and stateful: it consumes explicitly provided context and produces reviewable output that the human explicitly applies. In mature products this boundary is explicit: the chat mode itself is documented as not applying changes automatically.

### Grounding and customization

Two standing activities shape the quality of both loops:

- **Context management** — the developer (or the product automatically) supplies the code context each request needs; better-selected context yields focused answers, and products commonly advise selecting the relevant code before asking.
- **Customization** — persistent instructions and tailored suggestions align the assistant with the team's conventions, internal libraries, and preferred response style, so the assistance improves without per-request effort.

### Governance (organizational deployments)

Administrators control the perimeter around the assistance: who may use the assistant, which content is excluded from its reach, which policies apply, and what usage and audit data is collected. Governance changes what the assistant can see and suggest — it does not change who applies the output.

### Tiers of capability

**Defining core** — without these, not an AI Coding Assistant:

- human holds the execution loop
- AI model as the assistance mechanism
- grounding in the developer's coding context
- human-applied output, step by step

**Standard capabilities** — present in most modern products:

- inline completion with fine-grained accept/reject control
- code chat with persistent conversations
- context control (automatic + explicit)
- quick actions
- apply mechanics for chat-generated code
- customization (instructions, tailored behavior)

**Common variants / optional** — depends on product, segment, and posture:

- next-edit suggestions
- model selection (multi-model, bring-your-own-key, local models)
- enterprise administration (analytics, audit, exclusions, policies)
- next-edit suggestions (predictions of where the developer will likely edit next)
- self-hosted / fully-private deployment
- attribution or public-code-matching posture
- adjacent assistive outputs (commit messages, change descriptions, AI review suggestions, security scanning)
- a bundled agent structure (see Related Application Types)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Inline suggestion surface

Lives inside the code editor itself.

- ghost-text suggestion following the cursor; a small affordance for cycling alternatives and partial acceptance
- primary actions: accept (typically one key), reject, accept next word/line, open alternatives

### Chat panel

A persistent sidebar (or inline prompt) inside the editor.

- conversation history organized by topic; model and mode selectors where offered
- typical information: the question/instruction, the attached or referenced context, the response with code blocks
- primary actions: send a question or instruction, attach context, insert or apply generated code into a file, start a new conversation, open the chat in a larger view

### Context controls

The surfaces through which the developer manages what the assistant sees.

- selection awareness (the highlighted code is the context), file/folder/symbol attachments, workspace or repository indexing, curated context collections
- primary actions: add or remove context, restrict scope

### Settings

Per-developer configuration.

- enable/disable assistance features, pause suggestions (per editor or globally), choose models, set custom instructions and response behavior

### Administration console (organizational)

- member access and policies, content exclusions, usage analytics, audit logs, context-source configuration

## Important Rules / Behaviors

### The assistant is reactive, never autonomous

It acts only on the developer's activity or request, and its output remains inert until the developer applies it. This is the Type's core contract and the dividing line against agent behavior: an assistant that starts changing the project on its own initiative has crossed into the agent structure.

### Acceptance is granular

The developer controls adoption at multiple grains — accept the whole suggestion, a line, a word, or nothing — and can always edit accepted code afterward. The suggestion is a proposal at every grain.

### Context determines relevance

Responses are only as grounded as the context provided. Mature products let developers steer this explicitly (select code, attach files, reference symbols) and commonly document that poor answers usually mean poor context.

### Governance can restrict what the assistant sees and proposes

Organizations can exclude files from the assistant's reach, govern access, and set policies for suggestion behavior (for example, suppressing suggestions that closely match public code). These controls operate upstream of the assistance loop; they do not change who applies the output.

### The assistant is continuously present but opt-in per action

Presence is ambient (the completion loop runs as the developer types); consumption is voluntary (every suggestion, answer, and quick action can be ignored). Products accordingly provide pause/resume controls for the ambient loop.

### Conversation state is persistent and personal

Chat conversations persist and are organized per topic, so a question asked yesterday can be continued today. History is private to the developer unless sharing is explicitly offered.

## Variants

The Type is implemented in several recognizable forms. Common variants:

- **Editor plugin assistant** — delivered as an extension across many editors and IDEs; the dominant delivery form; often completion-first with chat added.
- **IDE-vendor-native assistant** — built into an IDE by its vendor, integrated with the IDE's own project model (symbols, inspections, navigation).
- **AI-native editor bundle** — an editor product built around AI assistance (and usually a bundled agent structure) rather than a plugin.
- **Self-hosted / fully-private assistant** — runs entirely within the customer's environment for security-sensitive organizations; assistance mechanics unchanged, deployment posture different.
- **Ecosystem-specialized assistant** — grounded in a particular cloud or platform ecosystem (its APIs, services, architecture guidance), alongside general coding assistance.
- **Multi-surface assistant** — the same assistance extended to terminal chat, web console, mobile, or team chat applications.
- **Assistant with bundled agent structure** — the current dominant packaging: the assistive loops remain, alongside an agent mode or agent product in the same line (one sampled vendor has announced steering customers from its assistant plugins toward an agentic successor product, while chat and completions carry over).

A variant remains a **Variant** as long as the defining core holds — the human performs the work, the AI responds within the flow, output is grounded and human-applied.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| AI Coding Agent | closest sibling | the assistant helps a human who performs each step (suggestions, answers, single-shot edits the human applies); the agent takes a delegated task and performs the multi-step loop itself, handing back changes for review. Boundary test: who holds the execution loop. Vendors ship both structures in one product line and document the contrast themselves; the two Types are adjacent points on an autonomy gradient |
| AI Software Engineering Agent | probable alias/variant of the agent Type | "AI software engineer" describes positioning (ticket-level delegation, team-member framing) of the agent structure, not a distinct structure from the assistant side |
| Code Editor / IDE | host / bundle | the editor's primary object is the file the human edits, with historically deterministic assistance (autocomplete, snippets, inspections); the assistant's primary object is the assistance relationship over the developer's context. An "editor with AI features" is a bundle of two Types |
| Enterprise AI Assistant | adjacent (different domain) | assists general organizational knowledge work with no grounding in the developer's coding context or editing flow; an assistant product's non-coding chat surfaces behave like this Type |
| Answer Engine / AI Research Assistant | adjacent (different job) | answers general technical questions without anchoring to the developer's code; the assistant's chat is anchored to the project and its output is meant to be applied |
| Code Review Platform | adjacent (different primary object) | the review platform's object is the review workflow over changes from anyone; assistive review suggestions and change descriptions, when embedded in the coding flow, are optional assistant capabilities |

The boundary with the **AI Coding Agent** is the most important one, because every researched product bundles both structures and the market is actively converging their packaging. The structural test — does the product stop at a suggestion the human applies, or does it apply project changes itself and iterate to completion? — separates exercising the assistant structure from exercising the agent structure, regardless of what the product is called.

## Representative Products

- **GitHub Copilot** (GitHub / Microsoft) — the archetype AI coding assistant; editor-agnostic plugin plus platform-embedded surfaces; documents its own feature set as "assistive" (synchronous suggestions while people work) versus "agentic" (autonomous).
- **JetBrains AI Assistant** (JetBrains) — assistant built into JetBrains IDEs; documents chat mode ("does not apply changes… reviewed and applied manually") versus agents explicitly.
- **Tabnine** (Tabnine) — privacy-focused assistant that runs entirely within the customer's environment; describes its base as inline code completion and conversational chat, with an autonomous agent beyond them.
- **Amazon Q Developer** (AWS) — ecosystem-specialized conversational assistant with IDE chat and inline completions; lists chat and agentic coding as distinct capabilities and is steering toward an agentic successor product.

The defining core was checked across completion-first, chat-first, IDE-native, self-hosted, and ecosystem-specialized forms — and against the founding completion-only generation of the Type — to avoid defining the Type by any single current packaging.

## Sources

Research date: **2026-09-06**

Primary official documentation:

- GitHub Copilot — What is GitHub Copilot; GitHub Copilot features; Getting code suggestions in your IDE — https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot , https://docs.github.com/en/copilot/get-started/features , https://docs.github.com/en/copilot/how-tos/get-code-suggestions/get-ide-code-suggestions
- JetBrains AI Assistant — AI Assistant in JetBrains IDEs; AI Chat — https://www.jetbrains.com/help/idea/ai-assistant.html , https://www.jetbrains.com/help/ai-assistant/ai-chat.html
- Tabnine — Overview; Tabnine Chat; Tabnine Agent — https://docs.tabnine.com/ , https://docs.tabnine.com/main/getting-started/tabnine-chat.md , https://docs.tabnine.com/main/getting-started/tabnine-agent.md
- Amazon Q Developer — What is Amazon Q Developer; Using Amazon Q Developer in the IDE; Generating inline suggestions — https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html , https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html , https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/inline-suggestions.md

> Evidence calibration: all sources above were fetched successfully on the research date; no source-access limitation applied. Claims about product-specific mechanics (key bindings, plan names, limits, dates) are kept in the paired Research Notes; this document states assistant-vs-agent contrasts only at the level the vendors themselves document. Commonality claims are calibrated to the four-product sample: capabilities observed in all four are stated generally; those observed in fewer are qualified ("many", "some", "where offered").

Detailed evidence, product-by-product observations, the cross-product comparison matrix, rejected findings, and the boundary analysis toward the AI Coding Agent Type are recorded in the paired Research Notes.
