# DAST / IAST

## Overview

A **DAST / IAST application** is a security testing application for running software. It places a specific, identified running application under security test, deliberately exercises that application, detects vulnerabilities from the application's actual runtime behavior, and records the results as evidenced vulnerability findings that drive remediation.

The defining core is small:

```text
Running target application under test
└── Exercise-and-observe test act
    │   ├── from outside — generated test requests, analyzed against the
    │   │   application's responses (dynamic / black-box mode, "DAST")
    │   └── from inside — an instrumentation agent observing exercised
    │       traffic as it flows through the running code (interactive mode, "IAST")
    └── Findings with runtime evidence
        (what weakness, where, proof, severity, remediation guidance)
```

The two abbreviations in the Type name mark the two observation vantages: testing a running application **from outside** (dynamic application security testing) and testing it **from within** an instrumented application (interactive application security testing). They are one family: both require a running target, both rely on deliberate exercise of the application, and both produce findings whose proof is the application's real behavior rather than an abstraction of its source code.

Everything else commonly associated with the category — crawlers, login automation, check libraries, CI/CD integration, dashboards, team features — is standard capability that mature products add. A tool that analyzes source code without running it is a static analyzer; a tool that blocks traffic in production is a firewall; a tool that only aggregates other tools' findings is a vulnerability management system. The running-application test act with runtime evidence is the boundary.

## Users & Context

Primary users:

- **Application security engineers** — own the testing program: register targets and scope, define scan policies, launch or schedule tests, triage findings, and drive them to the teams that own the code.
- **Security testers / penetration testers** — use the tooling interactively during manual testing: exploring the application through a proxy, replaying and modifying requests, and letting the scanner handle systematic coverage.
- **Developers** — consume findings about their own code, fix, and see fixes verified; in the instrumented mode, findings can surface in the developer's IDE.
- **QA / test engineers** — in the instrumented mode, their normal functional testing is the exercise that produces security findings; no security expertise is required of them.

Secondary users: security leadership and compliance stakeholders (reports, weakness-class coverage), and DevOps engineers who wire testing into build pipelines.

The work context is the software development lifecycle. Active testing that sends attack-grade traffic is normally run against test, QA, or staging environments, or otherwise gated by explicit authorization, because the testing itself can damage an application. Instrumented agents are likewise deployed in test/QA/staging environments (and developer workstations), not as production monitoring.

## Core Model

### The Defining Core

**The target.** The central subject is a running application identified for testing — a web application, API, or service addressed by URL/endpoint, or an application instrumented with an agent. The target is the deployed, executing thing: not a source repository, not a network segment, not an infrastructure component. In management-console products the target is a persistent record (a registered site or API with its configuration, credentials, and scan history); in desktop tools it is the session's explicit subject; in instrumented products it is the application instance carrying the agent.

**The test act.** The defining action is *exercise and observe*: the application is made to run through its behavior under test conditions, and security conclusions are drawn from what it actually does. Two vantages realize this:

- *Outside (dynamic mode).* The tool discovers the application's surface (crawling links and forms, driving a browser for script-heavy apps, or importing API definitions), then sends test traffic: passively observing normal traffic, and/or actively sending modified or malicious requests to see how the application handles unexpected input. Active probing is graded from mild to attack-grade.
- *Inside (instrumented mode).* An agent embedded in the application's runtime observes how exercised requests flow through the code — where untrusted input travels, where it reaches dangerous operations — while the application is used normally by QA tests, by a scanner, or by a human tester. The agent does not need its own attack engine; the exercise comes from the application's ordinary use.

**Findings.** The output is a structured vulnerability record, not a log line. A finding states what weakness class was detected, where it lives (the URL and request that triggered it, or the route and code location inside the instrumented application), the evidence that proves it (the request/response pair, the data-flow trace), a severity or risk rating, and remediation guidance. Findings are managed objects: triaged, assigned to owners, verified, and retested after fixes.

### Standard Capabilities

Mature products commonly add the following around the core. Each is widespread, but a product lacking one can still be recognized as this Type:

- **Surface discovery** — crawlers/spiders (including browser-driven exploration for script-heavy applications) in the outside mode; route discovery derived from observed requests in the instrumented mode.
- **Authenticated testing** — stored credentials, recorded login sequences, and session maintenance (including handling single-use tokens) so tests can exercise the application as a logged-in user.
- **Check libraries and scan policies** — collections of security checks mapped to recognized weakness classes (CWE, OWASP Top 10, web-testing guides), configurable per target, with support for custom checks.
- **Test-intensity tiers** — a graded spectrum from safe observation to intrusive attack simulation, with warnings and per-check enablement.
- **False-positive management** — confidence ratings on findings, dynamic confirmation of suspected issues, active retesting/verification of results, and triage states.
- **Test lifecycle machinery** — on-demand, scheduled, or pipeline-triggered runs; error handling and resumability; re-testing of fixed issues.
- **Results management** — issue queues with assignment, consolidation of duplicate findings, dashboards, and reporting including compliance/weakness-class coverage mapping.
- **Integration spine** — CI/CD hooks, ticketing systems, notifications, and APIs.
- **Organizational layer** — team/role management and organization-wide policies in the console-based shapes; distributed scan agents to reach internal networks.

### One Structure, Many Implementations

The core model is conceptual. Products differ in how they realize each part:

```text
Concept:      Observation vantage
Implementations:  external scanner (discovery + test-traffic engine),
                  in-app instrumentation agent,
                  both modes shipped in one product

Concept:      Who exercises the application
Implementations:  the tool's own generated test traffic,
                  a human tester browsing/probing through the tool,
                  existing QA/functional-test traffic flowing through
                  an instrumented application

Concept:      Finding evidence
Implementations:  request/response proof captured by the scanner,
                  data-flow and code-location traces captured by the agent

Concept:      Where the tool lives
Implementations:  desktop workbench, web management console,
                  CLI/daemon/API, build-pipeline step
```

A reader who has only seen one shape — say, a desktop proxy used by a penetration tester, or an agent deployed by a build pipeline — should still be able to recognize the other shapes from the core model.

## How It Works

### The outside-in loop (dynamic scanning)

```text
Define the target (URL/endpoint, scope, credentials)
→ discover the application surface
  (crawl links and forms, drive a browser, or import API definitions)
→ observe traffic passively (safe)
  and/or send modified test requests (active, graded intensity)
→ maintain sessions and logins throughout the run
→ analyze responses against weakness-class checks
→ record findings with request/response evidence
→ re-test after fixes are deployed
```

The two discovery-and-audit phases inform each other: the map of the application determines where test input can be placed, and new discoveries re-prioritize what gets tested first. Because active testing sends real attack-grade requests, the tool must also handle what a real attack session handles — authentication state, session expiry, application errors — and degrade gracefully (skipping, retrying, pausing) rather than producing garbage results.

### The inside-out loop (instrumented testing)

```text
Deploy an agent for the application's runtime into the target environment
→ exercise the application normally (QA tests, scanner traffic, manual use)
→ the agent observes data flow and security-relevant behavior from within
→ when exercised input reaches dangerous behavior, record a finding
   with the route and code location that produced it
→ fix the code; the same exercise verifies the fix
```

The characteristic property of this mode is that the exercise is not the tool's own attack: it rides whatever traffic the application already receives during testing. This is why the mode is popular with development teams — security testing happens as a by-product of testing the application anyway — and why its findings can point to the exact code location and route involved.

### The remediation loop

Both modes converge on the same closing loop:

```text
Finding raised → triage (confirm / dismiss / accept risk)
→ assign to an owner
→ fix happens outside the tool (code, configuration)
→ verify: re-scan the target, or re-run the exercise, until the
   finding no longer reproduces
→ report (trends, weakness-class coverage, compliance)
```

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Desktop testing workbench

The manual-tester shape.

- site tree of the explored application, request/response viewers and editors, proxy/interception controls, findings list
- primary actions: explore the target, inspect and replay requests, launch scans, review findings and evidence

### Web management console

The enterprise shape.

- target registry, scan configuration and scheduling, issue queues with assignment, dashboards, policy and report sections, team/role administration
- primary actions: register a target, launch/schedule a scan, triage and assign findings, generate reports

### Browser overlay (some products)

Security tooling surfaced inside the browser while the tester browses the target, blurring the line between manual exploration and automated analysis.

### Pipeline / CLI / API surfaces

Non-interactive operation for automation: headless scans in CI, agent deployment via infrastructure tooling, programmatic retrieval of findings.

### IDE surfaces (instrumented mode)

Findings pushed into the developer's editor with code locations and remediation guidance, so fixes happen where the code lives.

## Important Rules / Behaviors

- **Active testing is treated as a real attack.** Products gate attack-grade testing with authorization warnings, safe modes, and intensity tiers, and recommend staging/test environments. Sending malicious input can damage data or availability, and the tools say so explicitly.
- **Observation is safe; probing is not.** The passive/active distinction is structural: passive analysis of observed traffic does not alter the application, while active checks inject input and carry risk. Products keep the two separable.
- **Evidence quality is explicit.** Findings confirmed by observing actual exploit behavior carry higher confidence than findings inferred from static suspicion alone; products encode this in confidence ratings or verification passes rather than pretending all findings are equal.
- **Findings belong to a specific target and location.** Every finding anchors to the tested application and the precise request, route, or code location involved; identical issues across many locations are consolidated rather than duplicated endlessly.
- **Authenticated testing is a first-class mechanism.** Credentialed coverage requires machinery for logins and session upkeep (recorded login sequences, token handling), because most of an application's attack surface sits behind authentication.
- **Fixes are verified at runtime.** A finding closes not on assertion but on re-test: the same exercise that surfaced the vulnerability is repeated, and the issue closes only when it no longer reproduces.
- **Runs are engineered for failure.** Long test runs meet timeouts, outages, and defensive controls; products track errors granularly, skip or retry failed actions, and can pause or abort rather than report misleading results.

## Variants

The Type is implemented in several recognizable shapes. These differ in operating philosophy and audience, not in core structure:

- **Desktop manual-first toolkit** — a workbench for security testers in which automated scanning augments interactive human testing (e.g. Burp Suite Professional, OWASP ZAP).
- **Free open-source scanner** — proxy-first tooling with community extension ecosystems, spanning individual testers to security teams (e.g. OWASP ZAP).
- **Enterprise scan-management platform** — console-centered operation at organization scale: target registries, scheduled and distributed scanning (including agents inside internal networks), team roles, policies, and reporting (e.g. Invicti Enterprise).
- **Pipeline-native instrumented testing** — agent-based testing that rides normal QA/functional testing in CI/CD workflows, optimized for developer consumption of findings (e.g. Contrast Assess, Black Duck Seeker).
- **Hybrid products** — vendors shipping both vantages in one portfolio or product: an external scanner accompanied by per-runtime instrumentation agents, or one agent platform claiming to combine static, dynamic, and interactive approaches.
- **Target-type specializations** — API-oriented scanning (including machine-readable API definitions as input), script-heavy single-page application handling via browser-driven crawling.

Adjacent add-ons often travel with the Type from the same vendor — runtime attack protection, software composition analysis, asset discovery — but they are neighboring capabilities, not part of this Type's definition.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Static Code Analysis Platform (SAST) | closest testing sibling | analyzes source code without executing it; this Type tests a running application and derives evidence from runtime behavior. Removing the running-application exercise turns this Type into SAST. |
| Software Composition Analysis (SCA) | sibling technique | inventories third-party components and their known vulnerabilities; this Type finds weaknesses in the application's own behavior. |
| Vulnerability Management | consumer / aggregate | aggregates, prioritizes, and tracks remediation of findings from many scanners across asset classes; it does not exercise applications itself. Removing the test act, keeping aggregation, yields Vulnerability Management. |
| Web Application Firewall (WAF) | opposite side of the same traffic | sits in traffic continuously and blocks/enforces in production; this Type tests deliberately and reports, normally outside production. Changing the act from test-and-report to enforce-and-block yields a WAF (or runtime application protection). |
| Penetration Testing Management | process around the act | organizes human-led engagements (scoping, authorization, reporting); this Type is the tool that performs systematic testing. |
| Breach & Attack Simulation | sibling "attack" family | validates whether security controls detect and respond to simulated attacks across infrastructure; this Type hunts vulnerabilities in the application itself. |
| End-to-end Testing Platform | functional-testing neighbor | both exercise running applications; E2E testing verifies functional correctness, this Type verifies security properties with weakness-class vocabulary and findings. |
| API Security Platform | adjacent, wider horizon | maintains a continuous inventory of the whole API estate, observes production traffic, and can enforce; this Type runs bounded tests against identified targets and produces findings. API-security products embed this Type's testing as one module. |
| Software Test Management | process neighbor | organizes functional test cases/suites/runs for QA; this Type produces vulnerability findings with security semantics. |

The most important boundaries are the two that share an object with this Type: SAST shares the *software under test* (but never runs it), and the WAF shares the *HTTP traffic* (but enforces instead of tests). Both distinctions come back to the defining act: exercising a running application and proving vulnerabilities from what it actually does.

## Representative Products

- OWASP ZAP — free open-source proxy-first testing tool (outside-in mode)
- Burp Suite (PortSwigger) — manual-first professional toolkit with an embedded automated scanner (outside-in mode)
- Contrast Security (Contrast Assess) — agent-based instrumented testing platform (inside-out mode)
- Invicti (Invicti Enterprise) — enterprise scan-management platform that also offers instrumented testing via per-runtime agents (both modes)
- Black Duck Seeker — pipeline-oriented instrumented testing product (inside-out mode)

The core model was checked across these five shapes — open-source desktop, manual-first toolkit, agent-based platform, enterprise scan management, and pipeline IAST — to avoid over-fitting the definition to any one operating philosophy or customer tier.

## Sources

Research date: **2026-09-07**

- OWASP ZAP — documentation index and Getting Started Guide: https://www.zaproxy.org/docs/ , https://www.zaproxy.org/getting-started/ ; Alert Details catalog: https://www.zaproxy.org/docs/alerts/
- PortSwigger Burp Suite — Burp Scanner and Auditing documentation: https://portswigger.net/burp/documentation/scanner , https://portswigger.net/burp/documentation/scanner/auditing
- Contrast Security — documentation (Welcome, Assess, AST technology): https://docs.contrastsecurity.com/ (en/welcome-to-contrast.html, en/assess.html, en/ast-technology.html)
- Invicti — documentation portal and Invicti Enterprise and Standard docs: https://www.invicti.com/support/ , https://docs.invicti.com/ie-is/category/invicti-enterprise-and-standard (incl. Scans and Invicti Shark sections)
- Black Duck — Seeker Interactive product page: https://www.blackduck.com/interactive-application-security-testing.html

> Sourcing limitation: Black Duck Seeker evidence rests on official product pages only (operational documentation was not retrieved), so Seeker observations were used to corroborate the instrumented-testing pattern, not for precise operational claims; Invicti evidence is strongest at the documented module-structure level. Vendor accuracy claims (e.g., false-positive rates) are marketing statements and are intentionally not repeated as facts in this document. Precise vendor parameters (priority weightings, agent language lists, check counts) are recorded, where observed, in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
