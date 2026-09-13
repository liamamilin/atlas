# Research Notes — Agent Tool / Computer-use Platform

Research date: 2026-09-06
Leaf: Agent Tool / Computer-use Platform (DIRECTORY §13 Data, Analytics & AI Systems)
Slug: agent-tool-computer-use-platform

## Research Goal

Understand what an "Agent Tool / Computer-use Platform" actually is as an Application Type, from real products:

- what the "tool" object is in each product's own documentation
- what the platform actually executes (browser sessions, code sandboxes, virtual desktops, tool APIs)
- how agents invoke tools and how observations return into the agent loop
- what the session/environment lifecycle looks like
- what security, credential, and oversight machinery surrounds agent execution
- where the Type's boundary sits against neighboring leaves — especially Agent Development Platform (which bundles tool services), Agent Orchestration Platform, RPA / Desktop Automation, browser-testing platforms, and AI Coding Agent

This leaf was explicitly flagged by two prior sibling passes:

- research/agent-development-platform.md Boundary Finding 4: "tools are L1 inside agent platforms; AgentCore ships Browser/Code Interpreter as optional tool services... A standalone tool/computer-use platform would center on providing executable environments rather than on agent definition."
- STATUS.md: "agent-development-platform vs agent-evaluation-platform / agent-observability-platform / agent-tool-computer-use-platform... all three appear as bundled standard capabilities in every sampled product... capability relationship; standalone products exist but the bundle dominates; flagged for joint review when those leaves are processed."

This pass is that joint-review input from the tool-platform side.

## Initial Boundary (pre-research hypothesis)

The leaf name contains a slash: "Agent Tool / Computer-use Platform". Working hypothesis: one Type with two framings — (a) platforms providing executable tools/environments that agents invoke, and (b) the "computer use" specialization where agents drive GUIs (screens, mice, keyboards). Expected neighbors:

- Agent Development Platform — defines and runs the agent loop; tools are inputs to that loop
- Agent Orchestration Platform — coordinates multiple agents
- Agent Evaluation / Observability Platforms — lifecycle slices
- RPA Platform (§10) / Desktop Automation Application (§03.16) — act on GUIs/computers but with human-designed scripts, not model-decided actions
- Browser Compatibility Testing Platform (§12) — same cloud-browser substrate, human test scripts
- AI Coding Agent (§12) — finished agent product; its research notes note "remove coding/development scope → general computer-use agent (different Type space, §13)"
- Cloud IDE / Dev Container (§12) — environments for humans, not for agents
- Model API Platform — provides tokens, not execution

## Research Questions

1. What is a "tool" in each product's documentation — an API endpoint, an SDK object, a managed resource, a configured component?
2. What execution environments does the platform operate (cloud browser, code sandbox, virtual desktop, customer machine)?
3. How does an agent invoke a tool, and how do results/observations return to the agent loop?
4. What is the session/environment lifecycle (create → interact → terminate/timeout/pause)?
5. What isolation and security machinery exists (containerization, ephemeral sessions, allowlists, credential storage)?
6. What human-oversight surfaces exist (live view, session replay, supervision escalation)?
7. How do developers/makers integrate (SDKs, frameworks, MCP, natural-language configuration)?
8. Who is the primary user, and at what tier (developer / low-code maker / enterprise)?
9. Where are the boundaries with Agent Development Platform, RPA, browser testing, and coding agents?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy | Customer tier | Docs fetched |
|---|---|---|---|
| Amazon Bedrock AgentCore (Browser + Code Interpreter + Gateway) | hyperscaler modular tool services inside an agent platform | enterprise cloud | docs.aws.amazon.com (what-is, browser-tool, code-interpreter-tool) |
| Microsoft Copilot Studio (computer use tool) | low-code agent platform with a natural-language computer-use tool | enterprise makers / business units | learn.microsoft.com (computer-use) |
| E2B | open-source sandbox substrate (code + desktop) for any agent | OSS/developer | e2b.dev/docs (index, sandbox lifecycle, computer use) |
| Browserbase | specialized browser-infrastructure platform (sessions + Functions + Stagehand) | developers/startups | docs.browserbase.com (introduction, create-session, getting-started, runtime/Functions) |

Coverage check: hyperscaler suite vs low-code maker platform vs OSS substrate vs specialist infra. Two products center on browsers (AgentCore Browser, Browserbase), two on sandboxes/desktops (AgentCore Code Interpreter, E2B), one on full desktop GUI control (Copilot Studio computer use). Historical check performed against RPA/browser-testing/cloud-IDE neighbors (conceptually; see Boundary Findings).

Anthropic and OpenAI were considered as model-vendor samples (computer-use tool APIs) but their documentation hosts were unreachable from the research environment (see Sources). Their existence and shape are nonetheless evidenced indirectly: Copilot Studio's own doc lists OpenAI's "Computer-Using Agent (CUA)" and Anthropic Claude models as selectable execution models for its computer-use tool, and E2B's computer-use guide references the "OpenAI Computer Use API" — both Layer A observations from fetched pages.

## Sources

All fetched 2026-09-06 (Layer A unless noted):

1. Amazon Bedrock AgentCore overview — https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html (full service table: Harness, Runtime, Memory, Gateway, Identity, Code Interpreter, Browser, Observability, Payments, Evaluations, Optimization, Policy, Registry)
2. Amazon Bedrock AgentCore Browser — https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html (workflow, session model, Live View, session recording, security features)
3. Amazon Bedrock AgentCore Code Interpreter — https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html (sandbox model, runtimes, file support, best practices)
4. Microsoft Copilot Studio computer use — https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use (tool definition, CUA models, machine configuration, credentials, supervision, access control, testing, billing)
5. E2B docs index — https://e2b.dev/docs (What is E2B; Sandbox/Template/Persistence building blocks)
6. E2B sandbox lifecycle — https://e2b.dev/docs/sandbox (create/timeout/pause/resume/kill)
7. E2B computer use — https://e2b.dev/docs/use-cases/computer-use (Desktop sandboxes, VNC, agent loop, Desktop SDK actions)
8. Browserbase introduction — https://docs.browserbase.com/introduction (platform components: Browser API, Agents, Search API, Fetch API, Runtime; Stagehand; use cases)
9. Browserbase create session — https://docs.browserbase.com/platform/browser/getting-started/create-browser-session (session model, configuration options)
10. Browserbase getting started — https://docs.browserbase.com/welcome/getting-started (dashboard, playground, Session Inspector, framework choices, Functions)
11. Browserbase Functions (runtime) — https://docs.browserbase.com/platform/runtime/overview (serverless browser agents, invocation model, monitoring)

Not fetched / unreachable (recorded per source-access limitation rules):

- Anthropic documentation (docs.claude.com and platform.claude.com) — region-blocked ("App unavailable in region") on both attempts; no Anthropic-doc claims made.
- OpenAI platform docs (platform.openai.com/docs/guides/tools-computer-use) — HTTP 403 on single attempt; not retried; no OpenAI-doc claims made.
- AgentCore browser page at agent-core-browser.html returned title-only twice; correct URL (browser-tool.html) found via the service table and fetched successfully.

## Product Observations

### Amazon Bedrock AgentCore — Browser, Code Interpreter, Gateway (Layer A)

Positioning: AgentCore is "an agentic platform for building, deploying, and operating highly effective agents securely at scale using any framework and foundation model"; its services "work together or independently". The tool services are three of thirteen modular services — direct evidence that tool provision is a separable layer from agent definition (Harness) and runtime (Runtime).

**Browser** ("Interact with web applications using Amazon Bedrock AgentCore Browser"):
- "A fast and secure cloud-based browser runtime environment to enable AI agents to interact with web applications, fill forms, navigate websites, and extract information in a fully managed environment."
- Runs in a containerized environment, "keeping web activity separate from your system."
- Four-step workflow: (1) create a Browser Tool — AWS-managed browser (aws.browser.v1) or custom browser with session recording, custom network settings, IAM execution roles; (2) start a browser session — isolated, configurable timeouts, multiple simultaneous sessions; (3) interact — WebSocket-based streaming APIs; an Automation endpoint performs browser actions (navigate, click, fill forms, screenshots) via libraries like Strands, Nova Act, or Playwright; a Live View endpoint lets an end user watch the session in real time and interact with it directly; (4) monitor and record — Live View, session recording (captures DOM changes, user actions, console logs, network events; stored in the customer's S3 bucket; replayed in the AWS console with video playback, timeline navigation, action tracking), CloudWatch metrics.
- "Why use remote browsers for agent development?": agents interact with the web as humans do; serverless scaling; visual understanding through screenshots; human intervention with live interactive view; session isolation; audit capabilities.
- Security features: isolation (containerized), ephemeral sessions ("temporary sessions that reset after each use"), automatic termination when time-to-live expires.
- Integrations: "Any foundation model or popular browser automation frameworks including Playwright and BrowserUse."

**Code Interpreter**:
- "A capability that allows AI agents to write, execute, and debug code securely in sandbox environments... a bridge between natural language understanding and computational execution."
- Runs in a containerized environment within AgentCore; pre-built runtimes for Python, JavaScript, TypeScript with common libraries pre-installed; large-file support (inline upload up to 100 MB; up to 5 GB via S3 through terminal commands); internet access; CloudTrail logging; customizable session properties and network modes; default execution time 15 minutes, extendable up to eight hours; results returned and processed as streams.
- Framing of value: agents "may execute arbitrary code that can lead to data compromise or security risks" — the sandbox exists to make arbitrary agent code safe.

**Gateway** (adjacent evidence): "convert your APIs, Lambda functions, and existing services into Model Context Protocol (MCP)-compatible tools... making them available to AI agents" — the tool-catalog side of the same layer.

**Policy** (adjacent evidence): "deterministic control... intercept[s] every tool call before execution" — governance attached to the tool layer.

### Microsoft Copilot Studio — computer use tool (Layer A)

- Definition: "Computer use is a tool in Copilot Studio that lets your agent interact with and automate tasks on a Windows computer. It works with websites and desktop apps by selecting buttons, choosing menus, and entering text into fields on the screen. Describe in natural language what you want computer use to do, and it performs the task on a computer you set up by using a virtual mouse and keyboard."
- Key positioning sentence: "agents can complete tasks even when there's no API to connect directly to the system. If a person can use an app or website, computer use can too."
- Engine: "powered by Computer-Using Agents (CUA), an AI model that combines vision capabilities with advanced reasoning to interact with graphical user interfaces (GUIs). Because it's AI-powered, it adapts to interface changes" (buttons/screens can change without breaking the flow).
- Authoring: added as a tool to an agent (Tools page → Add tool → Computer use); configured with Name, Description, Model, Instructions (natural-language steps, with instruction templates and best practices); requires generative orchestration.
- Model selection is multi-vendor: OpenAI Computer-Using Agent (CUA), Anthropic Claude Sonnet 4.5/4.6, Claude Opus 4.6 — the tool platform is model-agnostic at the tool level.
- Inputs: dynamic values combined with instructions at execution time.
- **Machine**: "Select the target machine that the agent uses to run computer use" — machine management lives in Power Automate; the execution environment can be a customer-designated Windows machine, not only a vendor cloud runtime.
- **Credentials**: maker-provided (default, for autonomous agents) or end-user credentials; stored credentials for website/desktop sign-ins held in Power Platform internal storage or customer-provided Azure Key Vault; credential types scoped by website domain (wildcards supported) or desktop app name.
- **Human supervision**: designate an email reviewer contacted "if the computer-use agent detects potentially harmful instructions"; response-time limit after which the request expires and the run stops.
- **Access control**: allowlists of websites and desktop applications; note that allowlists "only prevent[] the model from taking actions on websites or applications that aren't in the allow list. It doesn't stop the model from opening them."
- **Enforce HTTPS** option.
- Testing: test experience with a left panel showing "a step-by-step log of the tool's reasoning and actions" and a right panel showing "a preview of the actions on the machine"; Stop testing halts all actions immediately.
- Publishing: autonomous agents (background tasks) or conversational (Teams etc.); in conversation the tool "shares reasoning messages and screenshots of the machine's activity in the chat."
- Billing: per-step Copilot Credits (5 standard / 15 premium model) — precise vendor numbers, kept out of the canonical document.
- Security best practices: dedicated/isolated machines, least-privilege accounts, web allowlists via browser policy, application control limiting executable apps.

### E2B (Layer A)

- Definition: "E2B provides isolated sandboxes that let agents safely execute code, process data, and run tools. Our SDKs make it easy to start and manage these environments."
- Building blocks: **Sandbox** — "a fast, secure Linux VM created on demand for your agent, which you can pause and resume as needed"; **Template** — "defines what environment a sandbox starts with"; **Persistence** — "pausing a sandbox saves both its filesystem and its memory, and paused sandboxes are kept indefinitely until you kill them."
- Lifecycle: create (with timeout) → running → timeout expiry can auto-pause (preserving full state) → resume → kill; timeout extendable at runtime; sandbox info retrievable (ID, template, metadata, start/end times). Continuous-run ceilings exist per plan (24 h Pro / 1 h Base) — precise numbers, research notes only.
- SDKs: Python and JavaScript/TypeScript; `Sandbox.create()`, `sandbox.commands.run(...)`.
- **Computer use** (Desktop): "Build AI agents that see, understand, and control virtual Linux desktops using E2B Desktop sandboxes." Desktop sandbox = Ubuntu 22.04 + XFCE with pre-installed applications; VNC streaming "for real-time visual feedback" viewable in a browser.
- Documented agent loop: (1) user sends a command; (2) agent creates a desktop sandbox; (3) agent takes a screenshot; (4) LLM (e.g., "OpenAI Computer Use API", Anthropic Claude) analyzes the screenshot and decides the action; (5) action executed via Desktop SDK (left/right/double/middle click, move, drag, write text, press keys, scroll, screenshot, terminal commands); (6) repeat until task complete.
- E2B positions itself as the environment, not the brain: the LLM integration is the developer's choice ("Connect LLMs to E2B" guide; the loop code calls `getNextActionFromLLM`).
- Other use cases: GitHub Actions CI/CD (testing, validation, AI code reviews in sandboxes).
- Meta-observation: E2B's docs are served via a public MCP server and llms.txt for coding agents — the product's own audience includes agents.

### Browserbase (Layer A)

- Definition: "Browserbase is the complete platform to build and deploy agents that browse and interact with the web like humans. One API key gives your agent access to cloud browsers, web search, page fetching, sandbox runtime, and access to every major LLM."
- Platform components: **Browser API** ("create, control, and observe browser sessions programmatically"), **Agents** ("a single API to extract structured data and interact with the whole web"), **Search API** ("fast, token-efficient web search results for your agents"), **Fetch API** ("retrieve page content as clean markdown through a proxy network"), **Runtime/Functions** ("deploy and run browser agents on Browserbase, on a schedule or on demand").
- Session model: "A browser session represents a single browser instance running in the cloud. It's the fundamental building block of Browserbase, providing an isolated environment for your web automation tasks." Created via Sessions API → returns a connection URL → connect any automation framework (Playwright, Puppeteer, Selenium) or Stagehand ("the SDK for browser agents. Natural language selectors, self-healing actions... LLM-powered browser control").
- Session configuration: region, viewport, keep-alive, recording (enabled by default), logging (enabled by default), agent identity (automatic fingerprinting, Verified tier, proxies, captcha solving, allowed domains), extensions, browser contexts ("persist authentication and session state"), user metadata.
- Escalation ladder the vendor itself teaches: Search → Fetch → Browsers ("Log in to portals with agent identity, navigate complex pages, and extract the hard-to-reach data") — capability tools (search/fetch) and environment tools (browser sessions) sold as one graded surface.
- Functions: "deploy browser agents or automation scripts directly onto Browserbase's infrastructure... as cloud functions invokable as APIs"; zero infrastructure; sessions automatically created and configured; async invocation with polling; invocation logs; session replays via Session Inspector; browser sessions automatically close when the function completes. Limitations: max execution 15 minutes, no persistent storage between invocations, TypeScript only (beta-era facts — research notes only).
- Observability: Session Inspector ("watch sessions in real time, view recordings, or inspect logs"); sessions list; playground with Live View; network activity and performance metrics per invocation.
- Framework integrations: Mastra, LangChain, CrewAI; skills files for coding agents (Claude Code, Cursor).
- Use cases: agents, web data retrieval, browser automation (logins, multi-step forms), automated testing.

## Cross-product Comparison

| Dimension | AgentCore Browser / CI | Copilot Studio computer use | E2B | Browserbase |
|---|---|---|---|---|
| Tool surface addressed to agents | Browser Tool resource; Code Interpreter tool; Gateway MCP tools | "Computer use" tool added to an agent | SDK objects (Sandbox, Desktop Sandbox) | Sessions API; Search/Fetch APIs; Functions |
| Platform executes the action | Yes — managed cloud browser / sandbox containers | Yes — virtual mouse/keyboard on a configured Windows machine (customer-designated or managed) | Yes — on-demand Linux VMs / desktops | Yes — cloud browser instances; serverless Functions |
| Invocation style | Streaming APIs (WebSocket automation endpoint); framework libraries (Playwright, Strands, BrowserUse) | Natural-language instructions configured in a low-code tool form | SDK methods (commands.run, click, type, screenshot) | REST/SDK; CDP/framework connection; Stagehand natural-language selectors |
| Observation returned to loop | Screenshots, DOM, streams of execution results | Screenshots + reasoning log (chat or test panel) | Screenshot → LLM → action loop; command stdout | Page state via framework; session replays; logs |
| Session/environment lifecycle | Create tool → session (timeout, TTL auto-termination, ephemeral) | Configure tool → run on machine → stop | Create → run → pause/resume → kill; timeout auto-pause | Create session → connect → keep-alive/timeout; auto-close on Function completion |
| Isolation | Containerized; ephemeral sessions; session isolation | Dedicated-machine guidance; allowlists; least-privilege accounts | Isolated VMs per sandbox | Isolated browser instances; contexts; allowed domains |
| Human oversight | Live View (watch + interact); session replay in console | Test panel (reasoning log + live preview); human supervision email gate; Stop testing | VNC stream (watch in browser) | Session Inspector (live view, recordings, logs); Live View in playground |
| Security/credential machinery | IAM execution roles; network settings; CloudTrail logging | Stored credentials (internal vault or Azure Key Vault); maker vs end-user credentials; access-control allowlists; enforce HTTPS | (Isolation-first posture; network access configurable) | Agent identity (fingerprinting, proxies, captcha solving); allowed domains; proxies |
| Model posture | Any foundation model | Multi-vendor model choice (OpenAI CUA, Anthropic Claude) | Any LLM (developer-wired) | "Access to every major LLM"; Stagehand LLM-powered |
| Integration with agent frameworks | CrewAI, LangGraph, LlamaIndex, Strands; MCP | Copilot Studio agents/agent flows (generative orchestration) | Any (SDK-first); docs served over MCP | Mastra, LangChain, CrewAI; Stagehand; skills for coding agents |
| Primary audience | Developers (enterprise) | Low-code makers / business units | Developers (OSS) | Developers / startups |
| Delivery | Managed cloud service (modular, inside agent platform) | Tool inside a low-code agent platform | Open-source SDK + hosted service | Managed cloud platform (specialist) |

## Abstraction Levels

### L0 — Defining Invariant

An Agent Tool / Computer-use Platform is a product whose primary job is to provide **executable tools and managed execution environments that AI agents invoke at runtime**: the platform performs (or orchestrates) the agent's action outside the model — in a cloud browser, code sandbox, virtual desktop, or managed tool service — and returns the observations that drive the agent's next step.

Three properties; remove any one and the product stops being this Type:

1. **Agent-invocable tool surface** — capabilities exposed as callable interfaces (tool schemas, SDK methods, API endpoints, or natural-language tool configurations) that a model-driven agent invokes at runtime, with the model deciding each action from observations. Without it: generic cloud infrastructure (browser/VM hosting) or human-scripted automation (RPA, browser test grids).
2. **Platform-executed action in a managed environment** — the platform, not the model and not the end user's hands, performs the action in an environment it operates or designates (isolated browser session, sandbox VM, virtual desktop, managed API). Without it: an SDK/library inside the agent dev platform, or a model API alone.
3. **Observation returned into the agent loop** — the result (page state, screenshot, code output, extracted data) flows back so the agent can decide its next step. Without it: a fire-and-forget actuator/trigger system, not a tool.

Historical/era check: this Type is young (its sampled products date from the mid-2020s agent era); the definition is deliberately written so it does not overfit to any one substrate. "Computer use" (pixel/screen-level GUI control) is the flagship variant, not the definition — search/fetch tools, code sandboxes, and MCP tool gateways satisfy the same three properties without any screen. Conversely, older same-substrate products (Selenium-style cloud browser grids, RPA bots, cloud IDEs) fail property 1 (invocation is by human-written scripts or human operation, not by a model deciding at runtime) — they are different Types, not older instances of this one.

### L1 — Common Mature Structure

Present across the sampled products; not required for the definition:

- session-based environments with a lifecycle (create → interact → terminate; timeouts/TTL; ephemeral-by-default posture)
- isolation of execution (containerized/microVM/VM/browser-instance separation from the caller's systems)
- execution observability (live view/streaming, session recording/replay, logs of actions, DOM/network/console events, audit logging)
- human-oversight surfaces (watch-only live view, interactive takeover, supervision/review escalation, stop controls)
- security controls on what tools may touch (network restrictions, domain/app allowlists, HTTPS enforcement)
- credential machinery separated from the agent's reasoning (stored credentials, vaults, maker vs end-user identity)
- SDK/API integration with agent frameworks and protocols (Playwright/Puppeteer/Selenium, LangChain/CrewAI/Mastra, MCP compatibility)
- concurrency/scale management (concurrent session limits, regions, serverless invocation)
- built-in tool catalogs alongside environments (search, fetch, code interpreter)

### L2 — Variant / Optional Structure

- tool scope: browser-only (Browserbase core) vs sandbox-only (E2B core) vs desktop GUI control (computer use) vs multi-tool suites (AgentCore Browser + CI + Gateway) vs capability tools (search/fetch)
- execution locus: vendor-managed cloud runtime vs customer-designated machine (Copilot Studio machine management) vs self-hosted open-source substrate
- delivery form: standalone infrastructure platform vs bundled tool services inside an agent development platform vs model-vendor built-in tools
- control interface: framework-native APIs vs SDK primitives vs natural-language instructions in a low-code form
- human-in-the-loop depth: watch-only vs interactive live takeover vs email supervision gates
- credential custody: platform-internal vault vs customer key vault vs per-user credentials
- audience: developer (SDK-first) vs low-code maker (tool configuration forms)
- commercial posture: consumption-based billing (per session/step/credit — vendor-specific numbers)
- persistence: ephemeral-only vs pause/resume state preservation vs persistent browser contexts

### L3 — Vendor-specific (Research Notes only)

- AgentCore: aws.browser.v1 managed-browser resource vs custom browsers; session recording to customer S3 with console replay; CloudTrail; WebSocket automation + Live View endpoints; Gateway MCP conversion; Cedar/natural-language Policy intercepting every tool call; microVM Harness; 15-min default / 8-h max session and execution windows; 100 MB inline / 5 GB S3 file limits
- Copilot Studio: Copilot Credits per-step billing (5/15); Power Automate machine management; Azure Key Vault credential option; generative-orchestration requirement; instruction templates; allowlist caveat (blocks actions, not navigation); CUA/Claude model table
- E2B: pause/resume persistence model (filesystem + memory preserved indefinitely); templates; Desktop SDK action vocabulary; E2B Surf reference agent; docs served via public MCP server; 24 h/1 h plan ceilings
- Browserbase: Stagehand (natural-language selectors, self-healing); Functions serverless browser agents (15-min cap, TypeScript-only beta); Verified identity/captcha solving; Search→Fetch→Browsers escalation ladder; Session Inspector; playground

## Vendor-specific Findings

See L3. None entered the canonical model. Notable: the Copilot Studio allowlist caveat (blocks actions on non-allowlisted surfaces but not navigation to them) is a precise vendor behavior — kept out of the canonical document. AgentCore's session-recording-to-S3 and Browserbase's Functions beta limits are likewise vendor facts.

## Rejected Findings

- "This Type = screen-pixel computer use" — rejected: search/fetch tools, code sandboxes, and MCP tool gateways satisfy the same core without any GUI; computer use is the flagship variant. The leaf name's "computer-use" half names the most visible variant, not the boundary.
- "The platform must own cloud infrastructure" — rejected: Copilot Studio's computer use runs on customer-designated Windows machines; E2B is open-source and self-hostable. What is invariant is platform-executed/orchestrated action, not vendor-owned data centers.
- "Tools must be invoked via function-calling APIs" — rejected: Copilot Studio configures tools through natural-language instructions in a low-code form; Browserbase sessions are driven through automation frameworks. The invariant is agent-invocability at runtime, not a specific calling convention.
- "Isolation is definitional" — rejected as L0: capability tools (search/fetch) have no session isolation in the environment sense; isolation is the mature security posture of environment tools (L1).
- "This is just RPA with a new name" — rejected: RPA's action sequences are human-designed at build time and deterministic; here the model decides each action at runtime from observations. Copilot Studio itself carries both structures (Power Automate-style flows vs the computer-use tool), showing they are distinct mechanisms inside one platform.
- "Model-vendor built-in tools are a separate Type" — rejected: they satisfy the same three properties (Copilot Studio's model table and E2B's docs evidence OpenAI CUA / computer-use APIs as selectable engines); delivery form (built-in vs standalone) is L2.

## Boundary Findings

1. **vs Agent Development Platform (sibling; the flagged joint review)** — confirmed complementary centers of gravity. The dev platform defines and runs the agent loop; this Type provides the executable capabilities that loop calls. Evidence from both directions: AgentCore ships Browser/Code Interpreter as optional tool services beside its Harness/Runtime (dev platform bundling tools); E2B and Browserbase have no agent builder at all (standalone tool substrate); Copilot Studio is a dev platform whose computer use is one tool among connectors. Structural test: remove agent definition/runtime → the tool platform survives (E2B, Browserbase); remove tool environments → the dev platform survives (LangGraph, OpenAI Agents SDK ship none). The bundle dominance noted by the dev-platform pass stands: in platform suites, tools are bundled L1; standalone products and model-vendor built-ins coexist. Both leaves remain defensible as separate Types; joint review should record the capability/bundle relationship.
2. **vs Agent Orchestration Platform (sibling)** — clean: orchestration coordinates multiple agents; this Type executes single actions/environments for agents. No sampled product conflates them (AgentCore's multi-agent support lives in Runtime, not in Browser/CI).
3. **vs RPA Platform (§10) / Desktop Automation Application (§03.16)** — sharpest conceptual boundary. Both act on GUIs and computers. Discriminator: who decides each action at runtime — RPA executes human-designed deterministic scripts triggered by schedules/events; here a model decides each action from live observations. Substrate overlap is real (both drive virtual mice/keyboards), and Copilot Studio ships both mechanisms in one platform (agent flows vs computer use), so the boundary is mechanism-level, not vendor-level. Test: remove model-driven runtime decisions → RPA remains.
4. **vs Browser Compatibility Testing Platform / Device Testing (§12)** — same substrate (cloud browser farms), different invoker and job: human-written test suites asserting expected behavior vs agent-driven sessions accomplishing tasks. Browserbase lists automated testing as a use case — the substrate is shared infrastructure; the Type boundary is the model-driven invocation.
5. **vs AI Coding Agent (§12)** — a coding agent is a finished agent product; this Type is the tool substrate agents call. The ai-coding-agent pass already noted the generalization direction ("remove coding/development scope → general computer-use agent"). Sandboxes also serve coding agents directly (E2B's CI/CD use case; Browserbase skills for Claude Code/Cursor) — the substrate is consumed by both.
6. **vs Cloud IDE / Dev Container (§12)** — same "managed environment" shape, different principal: environments operated for human developers vs environments invoked by agents. E2B's sandbox is agent-first (created on demand "for your agent"); a dev container is human-entered.
7. **vs Model API Platform / LLM Application Development Platform** — model APIs provide inference; this Type provides execution. The connective tissue is function/tool calling; Copilot Studio's multi-vendor model table and E2B's "connect any LLM" pattern show the tool layer is deliberately model-agnostic.
8. **vs MCP (protocol; no directory leaf)** — MCP is the protocol connecting agents to tools; several sampled products expose or consume MCP (AgentCore Gateway converts APIs to MCP tools; E2B serves its docs over MCP). Protocol vs platform: no conflict, but a joint-review note if a protocol/standard leaf is ever added.
9. **Leaf-name observation** — "Agent Tool / Computer-use Platform" embeds model-vendor-era terminology ("computer use" as popularized by model-vendor tool APIs). The researched Type is broader: managed agent-execution tooling of which computer use is the flagship variant. No rename made unilaterally; recorded for taxonomy review.

## Uncertainties

- Anthropic and OpenAI official documentation were unreachable (region block / 403). Their computer-use tool APIs are evidenced only indirectly (Copilot Studio's model table; E2B's guide). No claims about their internal tool schemas, pricing, or defaults are made.
- AgentCore Browser/Code Interpreter sub-pages beyond the three fetched pages (quickstart, observability, filesystem configurations) were not fetched; session/timeout numbers are from the fetched pages only and kept out of the canonical document.
- Browserbase Functions is explicitly beta-era (region-limited, TypeScript-only, secrets "coming soon"); its limits may change; kept out of the canonical document.
- Copilot Studio computer-use details come from one concept article; the FAQ and standalone-tools preview pages were not fetched. Billing numbers are vendor-published and may change; excluded from the canonical document.
- The market is moving quickly (this Type is ~2 years old as a distinct category); the sample reflects the mid-2026 state. The definition is written substrate-agnostic to survive further tool-scope expansion (e.g., new environment kinds).
- No pure "model-vendor built-in tools" product was directly documented (unreachable docs); the L2 "delivery form" variant rests on indirect evidence plus the sampled platforms' own bundling behavior.

## Final Synthesis

The Type's center of gravity is an **invocation → execution → observation** triangle operated by the platform on the agent's behalf:

```text
Agent (model-driven loop, owned elsewhere — dev platform or custom code)
   ↓ invokes
Tool surface (callable capability: browser session, code sandbox, virtual desktop, search/fetch, MCP tool)
   ↓ executed by
Platform-operated environment (managed, isolated, session-based)
   ↓ returns
Observation (page state / screenshot / code output / extracted data)
   ↓ feeds back into
Agent's next decision … (loop repeats until task completes)
```

Around this triangle, mature products add: session lifecycle management (timeouts, TTL, pause/resume), execution observability (live view, replay, logs), security machinery (isolation, allowlists, credential vaults), human-oversight surfaces, framework/protocol integrations, and scale management.

The defining core is deliberately small and substrate-agnostic: agent-invocable tools, platform-executed action, observations returned. "Computer use" — the model driving a GUI with virtual mouse/keyboard — is the most visible variant of the execution environment, not the boundary of the Type. Everything about where the environment runs (vendor cloud, customer machine, self-hosted), how the tool is invoked (SDK, streaming API, natural-language configuration), and how delivery is packaged (standalone, bundled in agent platforms, model-vendor built-in) is variation.
