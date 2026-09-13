# Research Notes — AI Coding Agent

## Research Goal

Understand, from real products, what an **AI Coding Agent** is as an Application Type: what its defining structure is, how the delegation-and-execution loop actually works, what humans do at each stage, which controls bound the agent's autonomy, and where the boundary lies against the adjacent Types **AI Coding Assistant**, **AI Software Engineering Agent**, **Code Editor / IDE**, and **Agent Development Platform**.

## Initial Boundary

Preliminary hypothesis before research:

- An AI Coding Agent is an application where a developer **delegates a software-engineering task** in natural language to an AI that **autonomously executes a multi-step tool loop** (read/edit files, run commands, run tests) over a **real codebase / execution environment**, producing **reviewable code changes**.
- Nearest neighbors: AI Coding Assistant (sibling leaf), AI Software Engineering Agent (sibling leaf — suspected alias), Code Editor / IDE, Agent Development Platform (§13), Code Review Platform, Issue Tracker.
- Key suspected boundary: the **assistant** helps a human who performs each step; the **agent** performs the steps itself while the human directs and reviews.
- Known unknowns: exact permission models, session lifecycles, local-vs-cloud execution split, how vendors position "agent" vs "assistant" modes inside one product.

## Research Questions

1. What is the primary **unit of input** — a task? a prompt? an issue assignment?
2. What **environment** does the agent operate in — local working tree, cloud sandbox, ephemeral CI machine?
3. What **tools** does the agent have, and how are they categorized?
4. What is the **execution loop** — how does the agent plan, act, observe, and adjust?
5. What is the **deliverable** — working-tree changes, commits, a branch, a pull request?
6. How does the **human control** the agent — approval modes, allowlists, sandboxing, take-over?
7. What **lifecycle / states** does a task or session have?
8. How is **project knowledge** supplied — instruction files, memory, rules, blueprints?
9. How does the agent **integrate with the development workflow** — git, issues, chat, CI, scheduling?
10. What **rules and limits** constrain the agent (time, scope, network, workflow gates)?
11. What distinguishes an **agent** from an **assistant** inside the same vendor's product line?
12. How do products support **parallel / multi-agent** work?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / Position | Customer tier |
|---|---|---|---|
| Claude Code | Anthropic | terminal-first agentic coding tool; local execution by default; multi-surface | individual → enterprise |
| GitHub Copilot coding agent ("Copilot cloud agent") | GitHub / Microsoft | platform-embedded, asynchronous, PR-centric agent running on GitHub infrastructure | mass-market → enterprise |
| Codex | OpenAI | coding agent delivered inside ChatGPT + IDE extension + CLI; cloud environments | consumer → enterprise |
| Cursor | Anysphere | IDE-native interactive agent (whole product now positioned as "a coding agent") | individual → enterprise |
| Devin | Cognition | autonomous cloud "AI software engineer"; session workspace with embedded IDE/browser | teams → enterprise |

## Sources

Research date: **2026-09-06**. All sources fetched live on this date.

### Claude Code (Tier 1 — official product documentation)

- Overview: https://code.claude.com/docs/en/overview
- Documentation index: https://code.claude.com/docs/llms.txt
- How Claude Code works (agentic loop, tools, environments, sessions, safety): https://code.claude.com/docs/en/how-claude-code-works

### GitHub Copilot coding agent (Tier 1 — official docs)

- About Copilot cloud agent: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- Using Copilot cloud agent on GitHub: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github

### Codex (Tier 2 — official product page only)

- Product page: https://openai.com/codex/
- **Source-access limitation**: the developer documentation at https://developers.openai.com/codex/ returned HTTP 403 on 2026-09-06 (one attempt; not retried further per network-restricted rule). Operational details for Codex are therefore **unverified**; only Tier-2 positioning statements are used, and no precise Codex workflow/rule claims are made.

### Cursor (Tier 1 — official product documentation)

- Docs home: https://docs.cursor.com/en/agent/overview (fetched; renders docs home page)
- Cursor Agent overview: https://cursor.com/docs/agent/overview
- Run Modes (approvals & sandboxing): https://cursor.com/docs/agent/security/run-modes
- Documentation index: https://cursor.com/docs/llms.txt

### Devin (Tier 1 — official product documentation)

- Introducing Devin: https://docs.devin.ai/get-started/devin-intro
- Devin session tools: https://docs.devin.ai/work-with-devin/devin-session-tools

---

## Product A — Claude Code (Anthropic)

### Key observations (evidence layer A unless noted)

- Self-description: "an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser."
- **Agentic loop** (officially documented): when given a task, the agent works through *gather context → take action → verify results*, phases blending; it "chains dozens of actions together and course-correcting along the way." The user "can interrupt at any point to steer."
- The product calls itself an **agentic harness** around the model: it "provides the tools, context management, and execution environment that turn a language model into a capable coding agent."
- **Built-in tool categories** (official): file operations (read/edit/create/rename), search (file pattern, regex content), execution (shell commands, servers, tests, git), web (search, fetch docs), code intelligence (type errors, definitions/references via plugins). Plus subagent-spawning and question-asking tools.
- **What the agent accesses** when run in a directory: project files, the terminal ("any command you could run"), git state, CLAUDE.md (persistent project instructions), auto memory, configured extensions (MCP servers, skills, subagents, browser).
- Explicit contrast with assistants: "This is different from inline code assistants that only see the current file."
- **Execution environments** (official table): Local (your machine; default), Cloud (Anthropic-managed VMs or self-hosted environments), Remote Control (execution local, UI in browser).
- **Interfaces**: terminal CLI, desktop app, VS Code / JetBrains extensions, web (claude.ai/code), Slack, CI/CD (GitHub Actions, GitLab CI). "The interface determines how you see and interact with Claude, but the underlying agentic loop is identical."
- **Sessions**: conversation saved locally as JSONL; sessions are independent (fresh context); resumable (`--continue`, `--resume`) and forkable; tied to the current directory; parallel sessions via git worktrees.
- **Context management**: context window holds conversation, file contents, command output, CLAUDE.md, memory; auto-compaction when full.
- **Safety mechanisms** (official): (1) **checkpoints** — files snapshotted before edits, rewind with Esc Esc; separate from git; remote-system actions not checkpointable; (2) **permission modes** — Auto (classifier reviews actions in background, blocks risky ones), Manual (asks before edits and commands), Accept edits (edits + common filesystem commands without asking), Plan (explores and proposes a plan without editing source); plus allowlists in settings scoped from org policy to personal.
- **Work style guidance** (official): "Delegate, don't dictate" — give context and direction, trust the agent on details; iterate conversationally; interrupt and steer mid-run.
- **Automation surfaces**: headless/programmatic runs (`-p`), scheduled routines (cloud), scheduled desktop tasks, GitHub Actions integration (@claude mentions, issues → PRs), Slack routing, code review.
- **Extensibility**: CLAUDE.md memory, auto memory, skills, hooks (shell commands on events), MCP servers, subagents, plugins, Agent SDK (build custom agents on the same engine).
- Example task framing (official): `claude "write tests for the auth module, run them, and fix any failures"` — a single delegated task including its own verification loop.

## Product B — GitHub Copilot coding agent (Copilot cloud agent)

### Key observations (evidence layer A unless noted)

- Official concept: "Copilot can research a repository, create an implementation plan, and make code changes on a branch. You can review the diff, iterate, and create a pull request when you're ready." It "can work independently in the background to complete tasks, just like a human developer."
- **Task types** (official list): research a repository, create implementation plans, fix bugs, implement incremental features, improve test coverage, update documentation, address technical debt, resolve merge conflicts.
- **Execution environment**: "its own ephemeral development environment, powered by GitHub Actions, where it can explore your code, make changes, execute automated tests and linters and more."
- **Entry points** (official): agents panel/tab on GitHub.com; dashboard prompt; Copilot Chat `/task`; **assigning an issue to Copilot** (assignee); `@copilot` mention on any PR; "Fix with Copilot" buttons (failing workflow runs, merge conflicts); new-repository seeding prompt; Slack/Teams integrations; automations (schedule or event-triggered, e.g. issue opened).
- **Output convention**: works on a branch; pushes commits; opens a pull request; "add you as a reviewer when it has finished, triggering a notification." Iteration happens via PR comments (`@copilot` follow-ups); "Copilot remembers context from previous sessions on the same pull request."
- **Explicit contrast with IDE agent mode** (official): "Copilot cloud agent works autonomously in a GitHub Actions-powered environment… In contrast, agent mode in your IDE makes autonomous edits directly in your local development environment." Also an explicit contrast with IDE assistants: with IDE assistants coding is local, synchronous, untracked, with manual steps (branch, commit, push, PR); with the cloud agent, coding happens on GitHub, steps are automated and transparent ("every step happening in a commit and being viewable in logs").
- **Customization**: repository custom instructions (files in repo, or org settings), Copilot Memory (product stores learned repo details; preview), custom agents (specialized profiles with own prompts/tools), MCP servers (GitHub and Playwright MCP enabled by default per docs), hooks (shell commands at key points), skills.
- **Rules / limits** (official): one repository per run; by default only context within that repository (broadenable via MCP config); one branch at a time; exactly one PR per task; a maximum session execution time exists (documented as 59 minutes, hard limit — precise figure kept here in Research Notes); GitHub-hosted repositories only; repository rulesets/branch-protection rules can block the agent unless bypass is granted.
- **Governance**: must be enabled; admin policy for Business/Enterprise; repository owners can opt out repositories; **GitHub Actions workflows do not run automatically on the agent's PRs by default** — a human must click "Approve and run workflows" (configurable).
- **Session management**: sessions listed and trackable; progress visible in session logs; follow-up prompts steer a running session.
- Usage metrics (PRs created/merged by the agent, time-to-merge) exposed to admins.

## Product C — Codex (OpenAI)

### Key observations (evidence layer A for positioning; operational details unverified — see source-access limitation)

- Official product page positions Codex as "the same powerful coding agent—now in ChatGPT" and "the best way to build with agents."
- Positioning statements (Tier 2): "reliably completes tasks end to end, like building features, complex refactors, migrations"; "a command center for agentic coding. With built-in worktrees and cloud environments, agents work in parallel across projects"; Skills to "teach Codex your team's standards, workflows, and ways of working"; scheduling for "routine but important work like issue triage, alert monitoring, CI/CD"; code review ("high-signal code review").
- Surfaces (official): Codex in ChatGPT (app), Codex IDE extension, Codex CLI — "The same agent everywhere you code… all connected by your ChatGPT account."
- **Not verified** (developer docs returned 403): session model, permission model, sandbox details, exact tool set, PR/branch behavior. No precise claims about these are made anywhere in the Atlas documents.

## Product D — Cursor

### Key observations (evidence layer A unless noted)

- Docs home positions the whole product: "Cursor is a coding agent for building ambitious software. Use it to understand your codebase, plan and build features, fix bugs, review changes, and work with the tools you already use."
- **Agent definition** (official): "Agent is Cursor's assistant that can complete complex coding tasks independently, run terminal commands, and edit code."
- **Agent = three components** (official): Instructions (system prompt + rules), Tools, Model; the product "orchestrates these components for each model."
- **Tools** (official list): search files/folders, web search, fetch rules, read files (including images), edit files, run shell commands, control a browser (screenshots, test applications, verify visual changes), image generation, ask clarifying questions (agent keeps working while awaiting the answer). "There is no limit on the number of tool calls Agent can make during a task."
- **Checkpoints**: automatic snapshots of modified files before significant changes; restore reverts files (not conversation); "stored locally and separate from Git."
- **Steering**: queued messages (processed in order after the current task) and immediate follow-ups ("delivered at the agent's next tool call… preserves in-flight work"); `/goal` gives "a long-lived objective to work toward until it's fully complete."
- **Run Modes** (local agents; official table): **Auto-review** (allowlisted calls run immediately; other shell commands run in a sandbox when possible; the rest go to a classifier that can allow, redirect, or ask the user), **Allowlist** (deterministic; listed actions run without approval), **Run Everything** (zero prompts). Plus **sandboxing** (OS-level: Seatbelt on macOS, Landlock/seccomp on Linux; workspace-scoped file access; network blocked by default with allowlist modes) and hard **protections** (browser tool, file deletion, files outside workspace always require approval). Team admins can override available modes and sandbox network rules.
- **Cloud Agents**: "run inside their own dedicated machine, so the agent never asks you to approve an action" — autonomy posture differs by substrate; self-hosted machine pools supported.
- **Other structure**: Agents Window (dispatch/manage many agents from one screen), worktrees for parallel isolation, Plan Mode, debug/design modes, background/cloud agents, automations, Bugbot (review), integrations (GitHub, GitLab, Slack, Linear, Jira…), CLI, SDK, rules/skills/MCP/hooks/subagents/plugins.

## Product E — Devin (Cognition)

### Key observations (evidence layer A unless noted)

- Official positioning: "Devin is the AI software engineer… an autonomous AI software engineer that can write, run and test code." Task-scale rule of thumb (official): "if you can do it in three hours, Devin can most likely do it."
- **Task types** (official): Linear/Jira tickets, features from scratch, bug repro & fix, app testing, migrations/refactors/modernization (language/framework upgrades, monorepo splits, feature-flag removal), PR review, codebase Q&A, unit tests, documentation, integrations/internal tools/demos/prototypes.
- **Session workspace** (official): conversational session UI; developer tools = **Shell** (full command-line access; command history with outputs; user can take over and run own commands), **IDE** (interactive VSCode environment with the repos; watch edits in real time; take over by stopping the session, then resume and inform Devin), **Browser/Desktop** (interactive browser for testing local apps, visual verification, auth flows/CAPTCHAs; browser state persistable into the environment "blueprint"). **Progress tab** unifies all shell commands, code edits, browser activity into one log.
- **Side chats**: ask questions about the session without interrupting the main work; read-only (can read/search code but not edit or run).
- **Human role** (official best practices): monitor progress, intervene early ("stop and redirect"), take over when needed, communicate manual changes back to the agent when resuming.
- **Task framing guidance** (official): "Write clear prompts with explicit completion criteria"; "Make tasks easy to verify — e.g. checking that CI passes"; break hard tasks into well-scoped steps.
- **Surfaces**: web app (app.devin.ai), Slack/Teams tagging, Devin CLI for local work with `/handoff` to cloud Devin, API.
- Environment provisioning via **blueprints** (environment configuration referenced by sessions).

---

## Cross-product Comparison

| Dimension | Claude Code | Copilot cloud agent | Codex | Cursor | Devin |
|---|---|---|---|---|---|
| Unit of input | natural-language task (CLI arg or interactive message) | prompt / issue assignment / `@mention` / button | prompt (ChatGPT / IDE / CLI) — positioning only | prompt in agent chat; `/goal` for long objectives | prompt / ticket / chat tag |
| Execution environment | local machine (default), cloud VMs, self-hosted | ephemeral GitHub Actions environment | cloud environments (+ CLI locally) — positioning only | local machine (sandboxed) or dedicated cloud machine | vendor-managed cloud machine (blueprint-provisioned) |
| Tool set | file ops, search, shell, web, code intelligence | repo tools, tests/linters, MCP | unverified | search, read/edit files, shell, browser, web, ask-user | shell, IDE edits, browser/desktop |
| Verification behavior | runs tests/builds, fixes failures | runs tests/linters | unverified | runs commands; browser visual verification | writes, runs, tests code; CI-passing criteria |
| Deliverable | working-tree changes → commits/PRs on request | branch + PR, review requested | changes/PRs (positioning) | working-tree changes + checkpoints; PRs via integrations | PR from session |
| Human control | permission modes (ask/accept/plan/auto-classifier), allowlists, sandbox | admin policy, repo opt-out, workflow-approval gate | unverified | run modes (auto-review classifier / allowlist / everything), sandbox, hard protections | monitor, take-over, resume; no per-action approval in cloud |
| Steering mid-run | interrupt (Esc) or queue messages | follow-up prompts to running session | unverified | queue or send-now at next tool call | stop/redirect; side chats for questions |
| Undo | checkpoints (file snapshots) | git/PR revert semantics | unverified | checkpoints (separate from git) | git semantics; take-over |
| Session model | persistent, resumable, forkable, per-directory | listed sessions, trackable logs | sessions in ChatGPT (positioning) | agent sessions; Agents Window | sessions with unified progress log |
| Project knowledge | instruction file + auto memory | repo custom instructions + learned memory | skills (positioning) | rules + skills | blueprints + persisted browser state |
| VCS integration | git operations, PRs, CI | native (GitHub) | positioning: PR workflows | GitHub/GitLab/Bitbucket/Azure DevOps | PRs; repo hosting integrations |
| Parallelism | subagents, worktrees, agent view, agent teams | multiple sessions | parallel agents + worktrees (positioning) | background/cloud agents, Agents Window, worktrees | parallel sessions |
| Extensibility | MCP, skills, hooks, plugins, subagents, SDK | MCP, custom agents, hooks, skills | skills (positioning) | MCP, rules, skills, hooks, subagents, plugins, SDK | API, blueprints |
| Automation / triggers | headless mode, schedules, CI, chat routing | automations (schedule/event), issue assignment, buttons | scheduling (positioning) | automations, CLI, SDK | Slack/Teams tags, API, CLI handoff |
| Primary surface | terminal (plus IDE/desktop/web) | GitHub web (plus IDE/chat/chat-tools) | ChatGPT app / IDE / CLI | desktop IDE (plus cloud/CLI) | web workspace (plus chat/CLI) |

### Cross-product commonalities (evidence layer B)

Observed across **all five** sampled products (or four of five where noted):

1. **Task-shaped input** — every product's primary input is a natural-language task/goal, optionally enriched with an issue, screenshot, error log, or chat thread. (All five.)
2. **Autonomous multi-step execution** — every product documents the agent working through multiple self-directed steps (search → read → edit → run → verify) without a human action per step. (All five; Codex at positioning level.)
3. **Real project + execution environment** — every product operates on an actual codebase inside an environment where actions have real effects (local directory, ephemeral CI machine, or managed cloud machine). (All five.)
4. **Reviewable change output** — the work culminates in project changes the human inspects (diff/PR/checkpoints) and accepts, modifies, or rejects. (All five.)
5. **Command execution + verification** — running shell commands and tests/builds is part of every product's documented loop. (All five; Codex positioning-level.)
6. **Steering without restarting** — every product lets the human inject direction while the agent works (interrupt, queued messages, follow-ups, take-over). (All five.)
7. **Session as unit of work** — every product structures work as sessions that are listed, monitorable, and (where local) resumable. (All five.)
8. **Persistent project instructions** — every product has a mechanism for repo/team-level instructions or learned memory. (All five.)
9. **Git / PR integration** — every product integrates with version control; cloud-positioned products make the PR the deliverable, local-first products treat commits/PRs as optional final steps. (All five.)
10. **Permission / autonomy controls** — every product has an explicit control layer (approval modes, allowlists, classifiers, sandboxes, admin policy, or take-over). (All five.)
11. **Parallel agents** — every product supports running multiple agent sessions/agents. (All five.)
12. **Extensibility via external tools/protocols** — MCP or equivalent, plus skills/rules/hooks. (Four of five directly observed; Codex skills at positioning level.)

### What varies (candidate L2)

- **Execution substrate**: local machine vs vendor cloud machine vs ephemeral CI environment vs self-hosted runners.
- **Output convention**: working-tree-centric (local agents; commit/PR on request) vs PR-centric (cloud/async agents; PR is the deliverable).
- **Trigger model**: interactive (user at keyboard) vs asynchronous delegation (issue assignment, @mention, buttons) vs automated (schedules, events, CI).
- **Autonomy posture**: ask-by-default vs classifier-mediated auto vs cloud-full-autonomy (no per-action prompts).
- **Take-over interaction**: embedded IDE inside the agent's workspace (Devin) vs agent inside the human's IDE (Cursor) vs terminal (Claude Code).
- **Environment provisioning**: setup scripts, dev containers, blueprints.
- **Governance depth**: admin policies, model access control, audit/metrics, workflow-approval gates.
- **Model strategy**: single-vendor model vs multi-model router.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Developer-issued Task (natural-language goal, optionally with attached context)
└── Autonomous multi-step execution loop
    (the agent plans, acts through tools, observes results, adjusts — no human action per step)
    └── acting on a Real Project Environment
        (an actual codebase inside an execution environment where actions have real effects)
        └── culminating in Reviewable Changes
            (project changes the human can inspect as diffs and accept / modify / reject)
```

Four properties. Remove any one and the product stops being recognizable as an AI Coding Agent:

- **Task delegation as the unit of input** — the human hands over a goal, not a sequence of editing steps. Without this, the product is an assistant (human performs each step) or a build tool.
- **Autonomous multi-step execution** — the agent itself decides and performs the sequence of actions, course-correcting from observed results. Without this, the product is a suggestion engine or a scripted pipeline.
- **Real project environment** — the agent acts on an actual software project (files, dependencies, runnable toolchain), not on a chat abstraction. Without this, it is a chatbot or a code generator with no ground truth.
- **Reviewable changes as the deliverable** — the output is a changed project state that the human can inspect and accept/reject; the human remains the reviewer and merger. Without this, it is an autonomous system with no human checkpoint — not a developer tool.

### L1 — Common Mature Structure

Present in essentially all mature products; expected by the market but not definitional:

- **Tool set**: file read/edit/create, codebase search (by name and content), shell/command execution, web search / documentation fetch.
- **Verification behavior**: running tests/builds/linters and iterating on failures until they pass.
- **Sessions**: named, monitorable units of work with a progress log/transcript; resumable where local.
- **Steering**: interrupt, queued messages, or follow-up prompts delivered mid-run without restarting.
- **Checkpoints / undo**: snapshots of the project before changes, restorable independently of git.
- **Persistent project instructions**: instruction/rules files and/or learned memory that shape every session.
- **VCS integration**: branches, commits, pull requests; PR-centric products add review-request and comment-iteration flows.
- **Extensibility**: external tool connections (MCP or equivalent), reusable skills/playbooks, lifecycle hooks, sub-agents.
- **Parallel execution**: multiple concurrent agent sessions/agents, isolated via worktrees or separate machines.
- **Permission / autonomy controls**: approval modes, allowlists, classifier review, sandboxing, admin policy — the layer that bounds what the agent may do without asking.
- **Multiple entry surfaces**: the same agent reachable from CLI, IDE, web, chat, issue tracker, or CI.

### L2 — Variant / Optional Structure

- **Execution substrate**: local machine / vendor cloud sandbox / ephemeral CI environment / self-hosted runners.
- **Output convention**: working-tree-centric vs PR-centric deliverables.
- **Trigger model**: interactive vs async delegation (issue assignment, @mention, buttons) vs scheduled/event automation.
- **Autonomy posture**: ask-by-default vs classifier-mediated auto-run vs cloud full-autonomy (no per-action approval).
- **Environment provisioning**: setup scripts, dev containers, environment blueprints, persisted browser state.
- **Take-over interaction**: embedded IDE inside the agent workspace vs agent embedded in the human's IDE vs terminal-only.
- **Enterprise governance**: admin enablement, model access control, audit logs, usage/PR-outcome metrics, workflow-approval gates.
- **Model strategy**: single-vendor model vs multi-model selection/routing.
- **Adjacent roles bundled by some products**: code review, issue triage, seeding new repositories.

### L3 — Vendor-specific Structure (Research Notes only)

- Claude Code: permission mode names (Auto / Manual / Accept edits / Plan), CLAUDE.md + auto memory, Agent SDK, routines, Remote Control, ultrareview.
- Copilot cloud agent: 59-minute hard session limit (documented figure), Copilot Memory (preview), custom agents, "Approve and run workflows" gate, agents panel, usage-metrics APIs.
- Codex: ChatGPT-app delivery, worktrees + cloud environments marketing framing.
- Cursor: Run Modes (Auto-review / Allowlist / Run Everything), permissions.json / sandbox.json schemas, Agents Window, Bugbot, Composer models.
- Devin: ACU-based commercial model (referenced by vendor materials), blueprints, side chats (`/btw`), Interactive Browser/Desktop tab, `/handoff` CLI→cloud.

## Vendor-specific Findings

- The **59-minute session limit** (Copilot cloud agent) is a single-product operational figure — kept out of the canonical document.
- **Permission-mode naming** differs per product (Claude Code modes vs Cursor Run Modes vs Copilot admin policy vs Devin take-over) — the canonical concept is "an autonomy-control layer," not any specific mode set.
- **Devin's embedded IDE + interactive browser** is the most elaborate take-over surface in the sample; other products achieve take-over differently (local editor, terminal). Treat as a variant of "human take-over," not a defining structure.
- **Copilot's issue-assignment trigger** (assign the agent as an issue assignee) is the clearest "agent as team member" framing; other products reach the same delegation via chat tags or CLI. Concept: async task delegation.

## Rejected Findings

- **"Runs in a cloud sandbox" is NOT definitional.** Local-first agents (Claude Code CLI, Cursor local agent, Devin CLI) satisfy the Type on the developer's own machine. Cloud/ephemeral execution is an L2 substrate.
- **"Opens pull requests" is NOT definitional.** Local agents can complete tasks in a working tree without any PR. PR-centricity is an output-convention variant tied to async/platform-embedded products.
- **"Uses git" is NOT definitional.** Agents can act on a plain directory; git integration is common mature structure, not the invariant.
- **"Multi-repo / cross-repo operation" is NOT part of the Type.** The sampled cloud agent explicitly restricts itself to one repository per run; scope rules are product policy, not Type structure.
- **"The agent is an IDE feature" is NOT definitional.** Several sampled agents run with no editor at all (terminal, web, CI). IDE-embedded agents are a surface variant.
- **"Always asks for approval before each action" is NOT definitional** — and neither is "never asks." The invariant is that an autonomy-control layer exists; its default posture varies by product and substrate (L2).
- **"AI Software Engineer" as a distinct structure** — rejected as a separate Type on current evidence; see Boundary Findings.

## Boundary Findings

### vs AI Coding Assistant (sibling leaf — most important boundary)

The structural difference is **who holds the execution loop**:

- **Assistant**: the human performs each step (writes, edits, runs); the AI suggests completions, answers questions, or produces single-shot edits the human applies. Unit of work = suggestion/answer. Initiative stays with the human.
- **Agent**: the human delegates a task; the AI performs the multi-step loop and the human reviews the outcome. Unit of work = delegated task. Initiative passes to the agent for the duration of the run.

The same vendor frequently ships both in one product line (chat/autocomplete vs agent mode/cloud agent), and vendors themselves document the contrast (the cloud-agent docs explicitly contrast "AI assistants in IDEs" with the agent; the Claude Code docs explicitly contrast itself with "inline code assistants that only see the current file"). **Boundary test**: if the product can complete an end-to-end task unattended and hand back a diff, it is exercising the agent structure; if it only responds inside a human-driven editing flow, it is exercising the assistant structure. The two leaves are adjacent points on an autonomy gradient, and single products increasingly bundle both — flagged for joint review.

### vs AI Software Engineering Agent (sibling leaf)

The sampled product marketed as an "AI software engineer" (Devin) has exactly the L0 structure of the AI Coding Agent: task delegation → autonomous tool loop over a provisioned environment → reviewable PR. "AI software engineer" is a **positioning variant** (emphasizing end-to-end autonomy, ticket-level delegation, team-member framing), not a different structure. Evidence supports treating the leaf as a probable **Alias/Variant** of AI Coding Agent. Flagged for joint review; no taxonomy change made unilaterally.

### vs Code Editor / IDE

The editor's primary object is the file the human is editing; its loop is human-driven. The agent's primary object is the **task** executed against the project; it can run with no editor present (terminal, cloud, CI). IDE-embedded agent modes are a surface variant of the agent, and "IDE with agent features" is a bundle of two Types. Distinction test: does the product's core value survive if no editor UI is present? For an agent, yes (CLI/cloud agents); for an editor, no.

### vs Agent Development Platform (§13)

The Agent Development Platform's user **builds agent software** (SDKs, orchestration, tool wiring); the AI Coding Agent's user **delegates coding work** to a finished agent. They meet in products that expose an SDK on top of a coding agent (one sampled product does exactly this), but the primary jobs, users, and objects differ (agent-building vs software-building).

### vs Code Review Platform

Review is the downstream human gate on the agent's output; some agents also perform review tasks. But a review platform's core object is the review/finding workflow on changes produced by anyone; the coding agent's core object is the delegated task loop that produces changes. Overlap (agent-as-reviewer) is a task variant, not a Type identity.

### vs Issue Tracker

Issue assignment is a **trigger surface** for async delegation. The tracker's object is the issue and its workflow; the agent's object is the executed task. Assigning an issue to an agent does not make the agent an issue-tracking application.

### "去掉什么就变成另一个 Type" 判据

- Remove **autonomous multi-step execution** (agent only suggests, human applies) → AI Coding Assistant.
- Remove **task delegation** (input is a keystroke/selection, not a goal) → AI Coding Assistant / autocomplete.
- Remove **real project environment** (acts on chat text only) → generic AI chatbot / code generator, not a coding agent.
- Remove **reviewable-changes deliverable** (no human checkpoint on output) → autonomous automation/ops system, not a developer's coding tool.
- Remove **coding/development scope** (delegated tasks over arbitrary digital work) → general computer-use agent (different Type space, §13).

## Historical / Market-Sample Check (§24)

AI coding agents are a young Type (market emergence mid-2020s); there is no "older generation" of the same Type to test against. The check was applied instead to **structural breadth within the current market**:

- **Local-first agents** (terminal CLI on the developer's own machine, working-tree output, optional git) satisfy L0 without cloud sandboxes or PRs → the definition must not require cloud execution or PR deliverables.
- **Cloud/async agents** (ephemeral environments, PR-centric output, issue/mention triggers) satisfy L0 without any local presence → the definition must not require local execution or an IDE.
- **IDE-embedded agents** satisfy L0 inside the editor → the definition must not require a standalone surface.
- Open-source terminal agents and research prototypes (not sampled in depth) share the same task→loop→diff shape, supporting the abstraction beyond the five commercial products.

The L0 above holds across all of these forms; no property of the current dominant implementation (cloud sandbox, PR-centricity, subscription billing) was promoted into the definition.

## Uncertainties

1. **Codex operational structure unverified** — developer docs returned 403; only Tier-2 positioning was used. If Codex's session/permission model differs structurally from the sample, L1 wording might need adjustment (low risk: positioning statements align with the sampled pattern).
2. **AI Software Engineering Agent leaf** — evidence strongly suggests alias/variant, but the decision belongs to a joint review pass, not this document.
3. **Assistant/agent convergence** — vendors are shipping agent modes inside assistant products and assistant modes inside agents; over time the two sibling leaves may need a shared "autonomy gradient" framing. Recorded for joint review.
4. **Permission defaults change quickly** — default autonomy postures (ask-first vs auto) are actively evolving vendor behavior; the canonical document deliberately describes the control layer conceptually, not per-product defaults.
5. **Non-commercial agents** (open-source terminal agents, research frameworks) were not deeply sampled; the §24 check covers them only structurally, not with product-specific evidence.

## Final Synthesis

The AI Coding Agent is defined by a **delegation contract**: the developer states a task; the agent autonomously executes a multi-step tool loop against a real project environment; the work culminates in changes the developer reviews. Everything else — where the loop runs (local/cloud/CI), what the deliverable looks like (working tree vs PR), how the agent is triggered (interactive/issue/mention/schedule), how strictly actions are gated (ask-first/classifier/full-auto), and how the human watches or takes over — is mature structure or variant, not definition.

The Type's nearest neighbor is the AI Coding Assistant; the boundary is **who holds the execution loop**. The Type's most likely alias is AI Software Engineering Agent (positioning variant of the same structure). The Type is distinct from Code Editor/IDE (object = task vs file), Agent Development Platform (build agents vs delegate work), Code Review Platform (produce changes vs adjudicate changes), and Issue Tracker (trigger surface vs execution engine).
