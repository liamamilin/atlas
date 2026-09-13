# Static Code Analysis Platform

## Overview

A **Static Code Analysis Platform** is software that examines a program's own code **without executing it**, driven by a packaged catalog of detection rules, and reports **located, actionable findings** — each pointing at a specific place in the code with an explanation of the problem — to the developers who can fix it.

It answers a question no runtime tool can ask: *what is wrong with this code as written, before anyone runs it?* Compilers reject what the language forbids; tests observe only the paths their cases exercise; profilers measure only what actually ran. A static analysis product reads the code the way a careful reviewer would — but systematically, against a written catalog of what counts as wrong, on every file and (in deeper products) across potential execution paths.

The defining core is small:

```text
The program's own code
  └── examined statically (without executing it)
      └── against a packaged, configurable catalog of detection rules
          └── producing located, actionable findings
              └── delivered where developers work
```

Everything else commonly associated with the category — servers, dashboards, quality scores, merge gates, compliance packs, AI-suggested fixes — is widespread market structure layered on that core, not what makes the product a static analysis product. The category spans a packaging spectrum from bare engines (a command-line tool with a rule catalog) to platform-backed suites; a product remains squarely in this Type with none of the platform machinery.

## Users & Context

**Primary users: developers** — the people whose code is analyzed. They meet the findings where they already work: in the editor while writing, in the terminal while building, or as comments on a proposed change. Their typical actions are: read the finding, understand the problem from the explanation, fix the code, or suppress the finding with a reason when it is a false positive or an acceptable risk.

**Secondary users:**

- **team / engineering leads** — configure which rules apply to which code, tune noise (suppressions, baselines), and read reports about what the analysis is finding;
- **security and compliance engineers** — when the product carries a security or compliance axis, they select the relevant rule packs (security standards, coding standards) and consume the same findings in their review processes.

The working context is the development workflow itself: code being written and changed, checked into version control, built, and merged. The analysis runs against that code — on demand from a developer's machine, inside the editor, or as a step in the build/CI pipeline. It is a complement to testing, not a substitute: the product category itself is explicit that static analysis does not replace careful design, testing, dynamic analysis, or fuzzing.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being a static analysis product:

**1. Static examination of the program's own code, without executing it.**
The object of analysis is the code under development — typically the source, parsed into a syntax tree the rules can reason over; in some products, a form captured from the build. "Static" is the operative word: the code is never run as part of the analysis. The product reasons about what the code *would* do — which paths could execute, which values could reach which operations — rather than observing what it *did* do. This is the seam against every runtime tool: tests, profilers, and debuggers all need the program to run; this Type does not.

**2. Packaged detection knowledge.**
The product ships its own judgment about what counts as wrong, in the form of a catalog of rules, checkers, or bug patterns — commonly a large one, organized by category (correctness bugs, resource handling, style, security, coding standards). This is what separates the Type from ad-hoc grep or a manual checklist: the knowledge is packaged, maintained by the vendor or community, and — critically — **configurable**. Teams turn rules on and off, adjust their strictness, and write their own. The catalog is the product's opinion, made inspectable and adjustable.

**3. Located, actionable findings.**
The output is not a score or a summary but a stream of individual findings, each bound to a location in the code (file and line, commonly a symbol) and carrying an explanation: what the problem is, why it matters, and — in mature products — how to fix it. A typical finding reads like: *file, line, severity, message* ("array index out of bounds"). Deeper products enrich the location with an evidence trail: the sequence of assignments and calls that led the analysis to its conclusion, so the developer can verify the reasoning rather than take it on faith.

### Standard Capabilities

Mature products across the spectrum carry most of the following. They make the analysis practical; they do not define the Type.

- **Rule configuration** — enable/disable rules, per project, per path, per language; configuration files checked into the repository so the standard travels with the code.
- **Suppression** — a first-class act, not an afterthought. Findings can be silenced inline (a comment on the offending line), in suppression files, or by baselining: recording the findings that exist in already-written code so the team focuses on what new changes introduce. Suppressions commonly carry a reason, making the "we decided this is fine" decision explicit and reviewable.
- **Severity and classification** — findings are graded (error / warning / style, or richer scales) and grouped into categories or diagnostic families, so teams can triage what to fix first.
- **Fix guidance** — from prose remediation advice to automatically applicable fixes (the product rewrites the offending code on request) to AI-generated proposed changes opened for human review.
- **Editor delivery** — findings surfaced inside the IDE as the developer writes, so problems are met at writing time rather than at build time.
- **Build and CI delivery** — the analysis runs as a pipeline step; findings appear as build output, annotations, or comments on the proposed change.
- **Incremental / differential analysis** — re-analyzing only what changed, or reporting changed-code results with full-system context, because whole-code analysis of large codebases is expensive.
- **Output formats and reports** — machine-readable result formats (XML/JSON-class), human-readable reports, and templates that render findings in the format of other tools.

### One Structure, Many Implementations

The core model is conceptual. Specific products realize each piece differently:

```text
Concept:            Static examination without execution
Implementations:    source parsed to a syntax tree; compiled form captured
                    from the build; pattern matching over code structure;
                    dataflow tracking; inter-procedural path analysis

Concept:            Packaged detection knowledge
Implementations:    built-in rule catalogs; community rule registries;
                    custom rule languages; compliance/coding-standard
                    packs (MISRA-class, CERT-class, OWASP-class);
                    graphical or DSL-based custom checkers

Concept:            Located, actionable findings
Implementations:    console diagnostics; structured result files;
                    IDE problem markers; PR/MR review comments;
                    web defect lists with evidence trails

Concept:            Delivery surface
Implementations:    CLI; IDE plugins; CI pipeline steps; hosted or
                    self-hosted web dashboards
```

A reader who has only seen one implementation — say, a linter in an editor — should still be able to recognize an enterprise analysis suite, and vice versa, from the core model.

## How It Works

### The analysis loop

```text
Configure the rule catalog
  → run the analysis over the code (parse; apply checks; reason)
  → findings reported with location + explanation
  → developer disposes of each finding:
        fix the code, or
        suppress with a reason
  → re-run; fixed findings disappear, suppressed findings stay silent
```

This loop is the Type's fundamental interaction. Two properties of it matter:

- **The analysis is advisory.** It reports; it does not change the code. Even when a product can generate a fix, the fix is a proposal the developer reviews and applies — the code changes through the developer, not through the analyzer.
- **Every finding demands a human decision.** Fix it, or suppress it with a justification. A finding that is neither fixed nor suppressed stays open. This decision stream — not the raw analysis — is what actually improves the code.

### The continuous loop

In team settings the same loop runs continuously against the stream of changes:

```text
code change proposed (commit / pull request)
  → analysis runs (often only on the changed code, with full-context results)
  → findings on the change surfaced in the delivery workflow
      (build output, review comments)
  → developer fixes or suppresses before merge
  → existing-code findings held in a baseline, addressed separately
```

The baseline is the structural answer to a real problem: a codebase that has accumulated years of findings cannot fix them all at once. Mature products let teams record the pre-existing findings and hold new work to the standard of *not adding new ones* — the analysis still sees the old findings, but the team's attention goes to the delta.

### What the analysis can and cannot do

The category is candid about its limits, and the limits shape behavior. Static analysis reasons without running, so it cannot know the program's intent: output that is wrong but well-formed, logic that compiles and runs and produces the wrong answer, are mostly invisible to it. What it finds well is what can be reasoned about from the code's structure and data flow: undefined behavior, dangerous patterns, resource mishandling, violations of written standards. Because the reasoning is mechanical, **false positives are a structural fact of the Type** — every product's documentation treats suppression and tuning as first-class workflow, not as an edge case. And because deep reasoning is expensive, products offer depth/speed trade-offs: faster shallower modes for the editing loop, exhaustive modes for scheduled full runs.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Command-line interface

The analysis engine's native surface, and the integration point for build systems.

- input: files/directories/projects to analyze, plus configuration (rules, severity thresholds, exclusions, target platform/standard)
- output: located diagnostics in human- or machine-readable formats; exit status usable by build tooling
- primary actions: run an analysis, apply automatic fixes, emit reports

### Editor / IDE surface

Where developers meet findings while writing.

- problem markers on the offending lines, with the explanation and (where available) a one-action fix
- primary actions: read finding, apply fix, suppress with reason

### Findings list / report surface

The triage view over a run's results — a web dashboard in platform-packaged products, a generated report in engine-only products.

- typical information: findings grouped by rule or by file, with severity, location, explanation, evidence trail, and current disposition (open / fixed / suppressed)
- primary actions: filter and sort, inspect the evidence for a finding, mark dispositions (fix / ignore with reason), export

### Configuration surface

The rule catalog made adjustable — configuration files in the repository (the dominant form), project settings, or policy pages in platform products.

- typical information: which rules are active, at what strictness, for which files
- primary actions: enable/disable rules, set severities, define exclusions, manage suppressions and baselines

### CI / code-review surface

Not a surface of the product itself but the place its output lands in team workflows: build annotations, review comments carrying findings, and reply-style commands that let a reviewer dispose of a finding from the conversation.

## Important Rules / Behaviors

- **Findings are advisory until a human disposes of them.** The analysis never silently changes the code. Auto-fixes and AI-suggested fixes are proposals requiring review.
- **Suppression is explicit and reasoned.** Silencing a finding is a recorded act — an inline comment, a suppression entry, a triage decision with a reason — not a silent disappearance. This keeps the "we decided this is acceptable" decision visible and revisitable.
- **Finding identity persists across runs.** A finding is tracked as the same finding while the code that triggered it remains (across re-runs, and in mature products across branches); it becomes "fixed" when the code no longer triggers it, and "removed" when the rule changed or the code disappeared. This persistence is what makes dispositions meaningful over time.
- **Baselines partition old debt from new work.** Pre-existing findings are recorded and held; the operative standard is applied to what changes introduce. Without this, adoption fails on legacy codebases.
- **The catalog is opinionated and tunable.** What the product calls "wrong" is its packaged judgment; teams adjust it. Two teams running the same product can enforce materially different standards.
- **Static analysis complements, never replaces, runtime verification.** The category's own framing: it finds what can be reasoned from the code; testing, dynamic analysis, and fuzzing find what only execution reveals.

## Variants

- **Bare engine** — a command-line tool (often open source) with a rule catalog and diagnostics output; no server, no accounts, no cross-run store. The structural floor of the Type.
- **Engine + IDE plugins** — the analyzer packaged with editor integrations so findings meet developers at writing time.
- **Platform-backed suite** — the analyzer plus a server holding analysis results, trends, and configurations across projects and teams; commonly paired with compliance reporting for regulated domains (automotive, aerospace, medical), where coding-standard packs (MISRA-class, AUTOSAR-class) and certification evidence are the point.
- **Hosted analysis service** — the analysis offered as a service: register a project, submit builds, view defects in a web UI.
- **Security-oriented packaging** — the same machinery with the catalog oriented at vulnerability classes and the findings consumed by security workflows (see Related Types: this shades into SAST territory).
- **Linter pole** — style/convention-focused analyzers with pluggable rule architectures; the shallow-but-broad end of the same spectrum, sharing every defining structure.
- **Depth spectrum** — syntactic pattern matching (fast, shallow) through local dataflow to inter-procedural, path-sensitive analysis (slow, deep); products expose the trade-off as analysis levels or separate scan modes.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Code Quality Platform | adjacent layer above | the quality platform is the **system of record** for code health: persistent issues, metrics, history, a configurable quality standard, and a pass/fail verdict attached to each change. This Type is the machinery that *produces* the findings; it needs none of that state (bare engines are fully in-type). Many products instantiate both layers. |
| SAST (Static Application Security Testing) | same machinery, different orientation | SAST orients the detection catalog at security weaknesses and feeds an application-security program; this Type orients at bugs, smells, style, and standards and feeds the development workflow. Many products serve both orientations on one engine. |
| Linter | variant pole, not a separate Type | linters are the style/convention end of this Type's spectrum; they share all three defining structures. |
| Code Review Platform | adjacent, human layer | the review platform's system of record is the human review conversation and verdict on a change; automated analysis may post comments into that conversation, but the human loop defines that Type. |
| Test Automation / Unit & Integration Test Runner | execution seam | tests execute the code and assert behavior; static analysis reasons without executing. Complementary, not competing. |
| Profiler / Debugger | execution seam | profilers and debuggers observe measured execution; this Type observes nothing that runs. |
| SCA / Dependency Management | object seam | SCA analyzes the third-party components the code depends on; this Type analyzes the code itself. Suites commonly ship both as separate products. |
| Code Editor / IDE | embedding seam | IDEs embed inspections as an authoring aid; the IDE's center is writing code, this Type's center is the analysis. IDE integration is a delivery surface here. |
| Code Migration Platform | recommend vs transform | migration platforms transform codebases; this Type reports on them. Auto-fixes here are per-finding proposals, not migration programs. |

The two most important boundaries are the **layer seam** with Code Quality Platform (machinery vs system of record) and the **orientation seam** with SAST (development-workflow defects vs AppSec security weaknesses). The market's products frequently straddle both seams — which is why the seams are documented as layers and orientations of one machinery, not as walls.

## Representative Products

- **Semgrep** — pattern-rule engine (open-source core, commercial platform); rules encode pattern matching and dataflow; ships both quality and security orientations.
- **PVS-Studio** — classic commercial static analyzer (C/C++, C#, Java, and more); checker-catalog philosophy; deliberately delegates the platform layer by exporting results to external quality services.
- **Coverity (Scan)** — enterprise-grade deep static analysis, examined here through its hosted service for open-source projects (build submission → analysis → defect triage).
- **ESLint** — the pluggable linter pole for JavaScript/TypeScript: rule architecture, configuration files, auto-fix, editor integrations; no platform layer by design.
- **Cppcheck** — open-source bare engine for C/C++: located diagnostics with severities, layered suppression machinery, incremental analysis, addon extensibility.

The core model was checked against the packaging spectrum (bare engine → hosted service → platform suite) and against the lint lineage, so the definition does not over-fit to any one era or packaging.

## Sources

Research date: **2026-09-09**

- Semgrep — documentation home, "Write rules" overview, "Triage and remediate findings": https://semgrep.dev/docs/ , https://semgrep.dev/docs/writing-rules/overview/ , https://semgrep.dev/docs/semgrep-code/triage-remediation/
- ESLint — documentation and Core Concepts: https://eslint.org/docs/latest/ , https://eslint.org/docs/latest/use/core-concepts/
- PVS-Studio — documentation index / user manual: https://pvs-studio.com/en/docs/
- Coverity Scan — service site: https://scan.coverity.com/
- Cppcheck — full user manual: https://cppcheck.sourceforge.io/manual.html
- Klocwork (market context only) — product page: https://www.perforce.com/products/klocwork

> Sourcing limitation: the commercial Coverity product documentation portal (documentation.blackduck.com) renders only via JavaScript and could not be fetched; Coverity evidence is limited to the Coverity Scan service site, and no claim depends on the commercial engine's internal techniques. Klocwork's documentation portal was unreachable (transport error); Klocwork is cited from its product page as market context only, and no operational claim depends on it. Precise numeric details (rule counts, build limits, checker inventories) are intentionally not stated, as they are version- and tier-dependent.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against sibling Types are recorded in the paired Research Notes.
