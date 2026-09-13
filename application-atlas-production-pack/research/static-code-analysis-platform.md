# Research Notes — Static Code Analysis Platform

Research date: 2026-09-09
Leaf: Static Code Analysis Platform (§12 Software Development & Product Engineering)
Slug: static-code-analysis-platform

## Research Goal

Understand what a "Static Code Analysis Platform" is as an Application Type: what the analysis actually is (what is examined, how), what the product ships (detection knowledge), what it produces (findings), how findings reach developers, and where the Type's boundary sits — especially against the two sibling leaves that flagged this pass:

- **Code Quality Platform** (§12, processed 2026-09-07) — recorded: "bare analyzers (Checkstyle/ESLint-class) belong to the analyzer layer (Static Code Analysis), not this Type"; layer seam = analyzer (runs checks, reports findings for a run, no persistent state/standard/verdict) vs platform (system of record: recorded runs + persistent issues/metrics/history + configurable standard + pass/fail verdict).
- **SAST** (§15, processed 2026-09-09) — recorded: "heavy machinery overlap with SAST; recorded seam = detection orientation + consuming program (security weakness consumed by an AppSec workflow vs bug/smell/style consumed by a code-quality workflow); many products serve both."

This pass must discharge both flags (joint review) and write this leaf at its own layer.

## Initial Boundary (hypothesis before research)

- The Type is the **static-analysis machinery layer**: products whose center is the analysis itself — examining code without executing it, driven by packaged detection knowledge, producing located findings for developers.
- Persistent quality state + quality verdicts over time = Code Quality Platform territory (platform layer).
- Security-weakness orientation consumed by an AppSec program = SAST territory (capability layer, security orientation).
- The word "Platform" in the leaf name is market packaging, not the invariant: the market spans bare engines (cppcheck, ESLint) to platform-packaged suites (Klocwork Server/Validate, Coverity Connect). The bare-engine pole must stay in-type or the leaf collapses into Code Quality Platform.

## Research Questions

1. What exactly does the analysis examine, and what does "static" mean operationally?
2. What does the product ship as detection knowledge — rules/checkers/patterns — and how configurable is it?
3. What is a finding — what does it carry (location, explanation, severity, fix)?
4. How do findings reach developers (CLI, IDE, CI, web)?
5. How are false positives handled (suppression, baseline, triage)?
6. What is common mature structure vs defining structure?
7. Where is the boundary vs Code Quality Platform (layer), SAST (orientation), linters (pole), runtime testing (static/dynamic), SCA (first-party vs dependencies), IDE (embedded inspections), Code Review (human layer)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / pole | Tier |
|---|---|---|
| **Semgrep** | pattern-rule engine (OSS core + commercial platform); explicitly ships both security and quality orientations; polyglot | individual → org |
| **PVS-Studio** | classic commercial static analyzer (checker-catalog, engine-first, no own server platform; exports to quality services) | commercial team |
| **Coverity (Scan)** | enterprise deep static analysis, delivered here as a hosted service for OSS projects (build → upload → analysis → defect triage) | enterprise / OSS service |
| **ESLint** | pluggable linter pole: rule architecture, style/convention + bug-avoidance, no persistent state | OSS individual |
| **Cppcheck** | OSS bare engine pole for C/C++: located diagnostics, severities, suppressions, addons, no platform | OSS individual |

Supplementary market context (not a formal sample member — docs portal unreachable, product page only): **Klocwork** (Perforce) — enterprise/embedded static analysis with compliance packs (MISRA/AUTOSAR/CERT), server platform (Klocwork Server / Perforce Validate).

Deliberately not re-sampled: SonarQube/Codacy/Qlty/DeepSource (already deeply documented by the code-quality-platform pass; referenced here only for the layer seam).

## Sources

Fetched 2026-09-09 (Tier 1 unless noted):

- Semgrep — https://semgrep.dev/docs/ ; https://semgrep.dev/docs/writing-rules/overview/ ; https://semgrep.dev/docs/semgrep-code/triage-remediation/
- ESLint — https://eslint.org/docs/latest/ ; https://eslint.org/docs/latest/use/core-concepts/
- PVS-Studio — https://pvs-studio.com/en/docs/ (manual index + section structure)
- Coverity Scan — https://scan.coverity.com/
- Cppcheck — https://cppcheck.sourceforge.io/manual.html (full manual)
- Klocwork — https://www.perforce.com/products/klocwork (Tier 2 product page)

Sibling-pass evidence (Tier 1, prior passes): research/code-quality-platform.md, research/sast.md, research/profiler.md, research/code-review-platform.md, research/code-migration-platform.md, research/integrated-development-environment-ide.md.

**Source-access limitations:**

- Coverity commercial product documentation (documentation.blackduck.com) is a JavaScript application — content not fetchable. Coverity evidence is limited to the Coverity Scan service site (which documents the analysis flow, defect classes, and triage). Deep-analysis technique claims about the commercial Coverity engine are NOT asserted.
- Klocwork docs (docs.perforce.com) — transport error on first fetch; per the retry rule the product page (perforce.com, Tier 2) was used instead. Klocwork is held as market context only; no operational claim depends on it.
- blackduck.com Coverity product page — 404.

## Product Observations

### Semgrep (evidence layer A unless noted)

- Self-description (docs home): "Find bugs and reachable dependency vulnerabilities in code. Enforce your code standards on every commit." Deploys "static application security testing (SAST), software composition analysis (SCA), and secrets scans from one platform."
- Rules (writing-rules overview): "Semgrep uses rules, which encapsulate pattern matching logic and data flow analysis, to scan your code for security issues, style violations, bugs, and more." Rules available in the Semgrep Registry; custom rules writable (YAML rule files, pattern composition with Boolean operators, rule-defined fixes, output messages). Pattern syntax page + rule syntax page.
- Languages: GA list spans C/C++, C#, Go, Java, JavaScript/TypeScript, Kotlin, Python, Ruby, Rust, Scala, Swift, PHP, Terraform, plus beta/experimental tiers; a Generic mode exists.
- Findings & triage (triage-remediation page): findings have triage statuses — Open (default; "a match between the code and a rule enabled in the repository"), Reviewing, Provisionally ignored (AI autotriage), To fix, Fixed ("detected in a previous scan but no longer detected in the most recent scan"), Ignored (with reasons: False positive, Acceptable risk, No time, No triage reason, Duplicate, Ignored via nosemgrep). Removed findings (rule disabled/changed, file deleted/ignored, PR closed unmerged) tracked separately.
- Inline suppression: `nosemgrep` code comments.
- Fixing: manual refactor per suggestions, or Autofix (AI-generated proposed changes, draft PR, human reviews/merges). Multimodal adds remediation advice, suggested fix, autotriage, noise filtering.
- Scan modes: full scans vs diff-aware scans (triage behavior differs across branches/refs; findings tracked across refs).
- Policies page: enable/disable rules and rulesets per repository; disabling a rule keeps existing findings open until re-scan.
- PR/MR integration: findings posted as comments; triage via comment commands (/fp, /ar, /other, /open); bulk triage API (issue_type sast/sca).
- Cross-product note: Semgrep explicitly ships BOTH orientations (Code = security+quality rules; Supply Chain = dependencies) — the living proof that machinery is shared and orientation is a seam, not a wall. (layer B)

### ESLint (evidence layer A)

- Self-description (core concepts): "ESLint is a configurable JavaScript linter. It helps you find and fix problems in your JavaScript code. Problems can be anything from potential runtime bugs, to not following best practices, to styling issues."
- Rules: "the core building block"; a rule "validates if your code meets a certain expectation, and what to do if it does not"; "hundreds of built-in rules"; custom rules via plugins.
- Rule fixes: optional fixes "safely correct the violation without changing application logic", applied via `--fix` and editor extensions; rule suggestions may change logic, editor-only.
- Configuration: config files (rules, enforcement level, plugins, shareable configs, file globs); shareable configurations distributed via npm (e.g. style guides); plugins = npm modules containing rules/configurations/processors/languages; parsers convert code to an AST (default Espree; custom parsers e.g. TypeScript); custom processors extract JS from other file types; formatters control CLI output appearance; bulk suppressions documented.
- Delivery: CLI + Node.js API; editor integrations "show you the ESLint results of your code in the file as you work".
- No server, no persistent cross-run state in the core product — the platform layer is absent by design. (layer A)

### PVS-Studio (evidence layer A)

- Self-label: "static code analyzer" (manual: "Getting acquainted with the PVS-Studio static code analyzer on Windows").
- Analysis targets: C, C++, C#, Java, JavaScript/TypeScript, Go; integration paths per language (MSBuild, CMake module, Gradle/Maven, JSON Compilation Database, command-line drivers).
- IDE plugins: Visual Studio, JetBrains Rider/CLion, Qt Creator, VS Code, IntelliJ IDEA/Android Studio, WebStorm/PhpStorm, GoLand.
- Continuous use: Docker, Jenkins, TeamCity, "PVS-Studio and continuous integration", "incremental analysis mode", "Analyzing commits and pull requests", unattended deployment, distributed builds (Incredibuild); cloud CI guides (Travis, CircleCI, GitLab, GitHub Actions, Azure DevOps, AppVeyor, Buddy).
- Results handling: "How to view and convert analyzer's results" (log files, converters), "Baselining analysis results (suppressing warnings for existing code)", "Suppression of false-positive warnings", filtering via .pvsconfig, excluding files/directories, blame-notifier utility ("Notifying the developer teams").
- Results export to quality services: "Integration of PVS-Studio analysis results into DefectDojo / SonarQube / CodeChecker" — the analyzer deliberately has NO own web platform; the platform layer is delegated. (layer A — strongest structural pole for the layer seam)
- Diagnostic catalog ("PVS-Studio Messages"): General Analysis (C++/C#/Java), Micro-Optimizations, Viva64 (64-bit error diagnosis), MISRA, AUTOSAR, OWASP groups (C++/C#/Java) — detection knowledge packaged as named diagnostic groups including compliance packs.

### Coverity (Scan service) (evidence layer A for the service; commercial platform docs unreachable)

- Positioning: "Coverity Scan — Static Analysis. Find and fix defects in your Java, C/C++, C#, JavaScript, Ruby, or Python open source project for free."
- Analysis claim: "Test every line of code and potential execution path." "The root cause of each defect is clearly explained, making it easy to fix bugs."
- Flow ("Get Started in 3 Easy Steps"): sign up and register your project → upload your build for analysis → view and fix your defects. Build capture is part of the flow (build package downloaded, uploaded for analysis).
- Defect classes surfaced in project testimonials: resource leaks, NULL dereference, uninitialized values, buffer overflow/overrun, missing return-code checks, mutex lock problems in conditionals, injection (OGNL) — correctness + security classes.
- Triage exists as a first-class activity ("locking registration and triage" during upgrade windows); weekly build limits by project size; project-level defect views.
- Community testimonials frame the value: finding defects "invisible even to Valgrind" (i.e., beyond dynamic analysis), weekly whole-source analysis, faster fix of newly introduced defects.

### Cppcheck (evidence layer A)

- Self-description (manual): "Cppcheck is an analysis tool for C/C++ code. It provides unique code analysis to detect bugs and focuses on detecting undefined behaviour and dangerous coding constructs. The goal is to detect only real errors in the code, and generate as few false positives as possible."
- "About static analysis" section: bugs findable = undefined behavior, dangerous code patterns, coding style; static analysis "does not replace any of: careful design, testing, dynamic analysis, fuzzing" — the product itself frames the static/dynamic boundary.
- Findings: `[file1.c:4]: (error) Array 'a[10]' index 10 out of bounds` — file:line + severity + message. Severities: error / warning / style / performance / portability / information. XML output carries id, severity, msg, verbose text, inconclusive flag, CWE id when known, and MULTIPLE locations (primary + evidence locations: "Assignment 'p=0'" → "Calling function 'f'" → "Null pointer dereference") — the analysis shows its reasoning path.
- Suppression machinery: command-line suppressions, suppressions files (plain text/XML), inline comments (`// cppcheck-suppress aaaa`, block begin/end, file-level, macro-level, per-symbol), remark comments justifying a warning in the report.
- Incremental analysis: build dir (`--cppcheck-build-dir`) — "Only changed files are analyzed when you recheck"; old warnings re-reported from cache.
- Project import: Visual Studio solutions, compilation databases (CMake), Borland; file filters; ignore patterns; optional Clang parser; preprocessor define-combination exploration (--force/--max-configs); platform configuration (type sizes); C/C++ standard selection.
- Extensibility: addons = scripts analyzing Cppcheck dump files (misra.py for MISRA C 2012 compliance, namingng.py naming conventions, threadsafety.py, y2038.py); library configuration .cfg files for external libraries; custom output templates (VS/GCC-compatible); HTML report generator.
- Check levels: reduced / normal / exhaustive (speed vs depth trade).
- No server, no accounts, no persistent cross-run store beyond the local build dir — bare engine pole. (layer A)

### Klocwork (market context; Tier 2 product page only — docs portal unreachable)

- Self-label: "Static Code Analysis and SAST for Secure Embedded Development"; "The static application security testing (SAST) tool provides early defense for developers by alerting them to potentially costly defects and compliance violations as soon as the code is written."
- Languages: C, C++, C#, Rust, Java, JavaScript, Python, Kotlin.
- Machinery evidence: "deep, inter-procedural dataflow analysis"; differential analysis of changed files "as if the entire system had been analyzed"; Klocwork Server holds system context; command-line + REST API; XML/JSON/PDF outputs; containerized/cloud builds; IDE plugins with "connected desktop" immediate differential results; graphical custom checker creation tool; architectural analysis integration.
- Compliance packs: Security (CERT, CWE, CWE Top 25, OWASP, DISA STIG, PCI DSS, ISO/IEC TS 17961), Safety (MISRA C 2004/2012/2023, HKMC, MISRA C++ 2008, AUTOSAR C++ 14, JSF AV C++), Quality (NASA 10 rules), custom standards/rules.
- Platform layer: Perforce Validate — "a centralized store of analysis results from Perforce Static Analysis solutions... analysis data, trends, and configurations... accessed through a web browser"; Project Streams manage multi-branch/variant codebases (shared rule config, issue sync across variants, cite-once); Smart Rank risk prioritization; AI-assisted code remediation.
- Reading: Klocwork instantiates BOTH layers (analysis machinery + Validate platform layer) — consistent with the "many products are both" note from the code-quality pass. (layer A for the page's claims; held as market context because operational docs were unreachable)

## Cross-product Comparison

| Dimension | Semgrep | ESLint | PVS-Studio | Coverity Scan | Cppcheck | Klocwork (context) |
|---|---|---|---|---|---|---|
| Static examination without execution | yes (pattern + dataflow) | yes (AST rules) | yes | yes ("potential execution path") | yes | yes (inter-procedural dataflow) |
| Packaged detection knowledge | rules + Registry + custom rules | hundreds of built-in rules + plugins | diagnostic groups (General/Viva64/MISRA/AUTOSAR/OWASP) | checkers (defect classes) | checkers + addons | compliance packs + custom checkers |
| Located findings | yes (rule match locations, dataflow) | yes (file/line messages) | yes (warnings, log files) | yes (defects with root cause) | yes (file:line, multi-location evidence) | yes (cause + remediation guidance) |
| Severity/classification | yes | yes (error/warn/off) | yes (diagnostic groups) | yes (defect classes) | yes (6 severities) | yes (risk severity, Smart Rank) |
| Suppression | nosemgrep comments, ignore reasons | bulk suppressions, config | false-positive suppression, baselining | triage | inline/file/XML suppressions, remarks | filters, suppressions, baselines |
| Auto-fix | Autofix (AI draft PR) | --fix + suggestions | — (not observed) | — (not observed) | — (not observed) | AI-assisted remediation |
| IDE delivery | editor (Semgrep Editor for rules) | editor integrations | 7+ IDE plugins | web UI | GUI + editor templates | IDE plugins, connected desktop |
| CI/build delivery | CI scans, PR comments | CLI in CI | Jenkins/TeamCity/cloud CI guides | build upload service | CLI in CI, build-dir cache | CI/CD, differential analysis |
| Incremental/diff-aware | diff-aware scans | — | incremental mode | weekly full builds | build dir (changed files) | differential analysis |
| Own server/platform layer | AppSec Platform (commercial) | none | none (exports to SonarQube/DefectDojo/CodeChecker) | hosted service (Scan) | none | Klocwork Server + Validate |
| Persistent quality state + verdicts | platform-side (commercial) | none | none | service-side | none | Validate-side |
| Security orientation | explicit (SAST product) | incidental | OWASP group | defects incl. security classes | incidental | explicit (self-labels SAST) |
| Compliance packs | — | — | MISRA/AUTOSAR/OWASP | — | misra.py addon | MISRA/AUTOSAR/CERT/... |
| Business model | OSS core + commercial platform | OSS | commercial license | free hosted service for OSS | OSS | commercial license |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **Static examination of the program's own code without executing it.** The analysis object is the code under development — source parsed into an AST (ESLint parsers, Semgrep patterns, cppcheck's parser or its optional Clang parser), or the code's compiled form captured from the build (Coverity build upload) — examined by reasoning over it rather than by running it. Coverity's own framing: "test every line of code and potential execution path"; cppcheck's manual explicitly frames static analysis as distinct from testing/dynamic analysis/fuzzing. Remove → runtime testing (Test Automation / Unit Test Runner), Profiler, Debugger territory.
2. **Packaged detection knowledge.** The product ships a catalog of rules/checkers/patterns encoding what counts as wrong — ESLint "hundreds of built-in rules"; Semgrep rules ("pattern matching logic and data flow analysis") + Registry; PVS-Studio diagnostic groups; cppcheck checkers + addons; Coverity checkers; Klocwork compliance packs. The catalog is the product's judgment, and it is configurable (enable/disable, custom rules). Remove → ad-hoc grep or manual code review (no packaged judgment).
3. **Located, actionable findings.** Each result identifies where in the code (file/line, commonly symbol/function) with an explanation of the problem — cppcheck `[file1.c:4]: (error) Array 'a[10]' index 10 out of bounds`; Coverity "root cause of each defect is clearly explained"; Klocwork "detailed information of cause with... guidance on remediation"; ESLint messages with optional fixes/suggestions; Semgrep findings with messages and fixes. Remove → aggregate metrics/scores without locations (metrics tooling), or a manual review report.

Jointly-held load-bearing:

- 1 alone = a parser/AST tool or code search (no judgment about wrongness)
- 2 alone = a standards document / checklist (nothing analyzed)
- 3 alone = manual code-review report
- 1+2 without 3 = analysis machinery with no developer-consumable output (e.g., a metrics collector)
- 1+3 without 2 = ad-hoc inspection (grep/manual notes), no packaged judgment
- 2+3 without 1 = runtime testing or manual review findings (the code ran, or a human read it)

### L1 — Common Mature Structure

- Rule/checker configuration (enable/disable per rule, per file/path/glob; config files: ESLint config, cppcheck suppressions/settings, PVS settings files, Semgrep policies)
- Suppression of findings as a first-class act (inline comments: `cppcheck-suppress`, `nosemgrep`; suppression files; baselining existing code: PVS "suppressing warnings for existing code", Klocwork baselines; ignore reasons in triage UIs)
- Severity / classification of findings (cppcheck's six severities; ESLint error/warn/off; PVS diagnostic groups; Semgrep severity + triage statuses)
- Fix guidance (auto-applicable fixes: ESLint `--fix`, Semgrep Autofix; suggestions; remediation guidance: Klocwork, Coverity root-cause explanations)
- IDE delivery (PVS 7+ plugins; Klocwork plugins + connected desktop; ESLint editor integrations "results in the file as you work")
- CI/build delivery (PVS CI guides; Klocwork CI/CD; Coverity build upload; Semgrep CI scans + PR comments; ESLint CLI in CI)
- Incremental / differential analysis (PVS incremental mode; Klocwork differential; cppcheck build dir; Semgrep diff-aware scans)
- Output formats & reports (cppcheck XML/templates/HTML; Klocwork XML/JSON/PDF; ESLint formatters; PVS converters)
- Multi-location evidence trails (cppcheck template-location showing the reasoning path; Semgrep dataflow traces; Coverity root-cause explanation)

### L2 — Variant / Optional Structure

- **Packaging spectrum**: bare engine (cppcheck, ESLint) ↔ engine + IDE plugins (PVS-Studio) ↔ server-backed suite (Klocwork Server/Validate, Coverity Connect) ↔ hosted service (Coverity Scan, Semgrep AppSec Platform). The platform layer itself — persistent issues/metrics/history + configurable standard + pass/fail verdict on changes — is Code Quality Platform territory; a static-analysis product remains in-type without any of it.
- **Detection orientation**: quality/bug-first (cppcheck, PVS-Studio General Analysis, ESLint) ↔ security-first (SAST seam: Klocwork self-labels SAST; Semgrep ships a SAST product; PVS-Studio ships an OWASP group) ↔ compliance-pack-driven (MISRA/AUTOSAR/CERT: Klocwork packs, PVS MISRA/AUTOSAR groups, cppcheck misra.py addon).
- **Technique depth**: syntactic pattern matching (ESLint rules, Semgrep patterns) ↔ local dataflow (Semgrep dataflow, cppcheck ValueFlow) ↔ inter-procedural/path-sensitive deep analysis (Coverity "potential execution path", Klocwork inter-procedural dataflow). Depth trades against speed (cppcheck check levels reduced/normal/exhaustive).
- **Language scope**: single-language (ESLint: JS/TS) ↔ language family (cppcheck, PVS-Studio core: C/C++ roots) ↔ polyglot (Semgrep, Klocwork).
- **Build integration depth**: parse-only (ESLint) ↔ build-capture (Coverity build upload; PVS compiler monitoring; Klocwork compiler support "hundreds of compilers and cross-compilers").
- **Provenance / business model**: OSS (ESLint, cppcheck) ↔ free hosted service for OSS (Coverity Scan) ↔ commercial license (PVS-Studio, Klocwork) ↔ OSS core + commercial platform (Semgrep).

### L3 — Vendor-specific (research notes only)

- Semgrep: YAML rule syntax with Boolean pattern composition; Registry; Multimodal autotriage/noise filtering; /fp //ar comment triage; issue_type sast/sca API.
- PVS-Studio: Viva64 64-bit diagnostics; blame-notifier; .pvsconfig; PVS_STUDIO macro; JSON entity annotation.
- Coverity Scan: weekly build limits tiered by lines of code; build package download/upload mechanics.
- Klocwork: Project Streams (variant sync, cite-once); Smart Rank; Perforce Validate platform; TÜV-SÜD certification materials.
- cppcheck: dump-file addon architecture; .cfg library files; template/template-location output DSL; preprocessor define-combination exploration.
- ESLint: plugin/parser/processor architecture; shareable configs via npm; bulk suppressions file.

## Boundary Findings

1. **vs Code Quality Platform (§12, processed) — LAYER seam. RATIFIED, keep-both.** This Type = the analysis machinery: runs checks, produces located findings for a run; persistent cross-run state, quality standards-as-verdict, and quality ledgers are NOT required (cppcheck/ESLint/PVS-Studio poles all in-type with none). Code Quality Platform = the system-of-record layer above: recorded runs + persistent issues/metrics/history + configurable standard + pass/fail verdict attached to changes. Many products instantiate both layers (SonarQube-class; Klocwork+Validate), which is why the two leaves must be written at different layers — exactly as the code-quality pass recorded. Remove-test: remove persistent state + standard + verdict from a product → still this Type (bare analyzer pole); add them as the center → Code Quality Platform territory. **DISCHARGES the code-quality-platform pass's heavy-overlap flag from this side.**
2. **vs SAST (§15, processed) — ORIENTATION + CONSUMING-PROGRAM seam. RATIFIED, keep-both.** Same machinery (static examination + packaged knowledge + located findings); the seam is what the detection knowledge is oriented at and who consumes the findings: SAST = security weaknesses consumed by an AppSec program; this Type = bugs/smells/style/quality consumed by the development workflow. Many products serve both (Semgrep explicitly ships both orientations on one engine; Klocwork self-labels SAST; PVS-Studio ships an OWASP group beside General Analysis; Coverity finds both defect and security classes). Remove-test: reorient the catalog at security weaknesses and hand findings to an AppSec workflow → SAST; keep the defect/quality orientation and the developer workflow → this Type. **DISCHARGES the sast pass's forward flag from this side.**
3. **vs Linter — no separate leaf; linters are the style/convention POLE of this Type.** ESLint self-labels "linter" and covers "potential runtime bugs, to not following best practices, to styling issues"; cppcheck lists "coding style" among findable bug kinds. The directory has no separate Linter leaf; the pole is documented as a variant, consistent with the code-quality pass's "bare analyzers (Checkstyle/ESLint-class)" framing.
4. **vs Debugger / Profiler (§12, processed) — static/dynamic seam.** The profiler pass recorded: "remove execution observation and it becomes static analysis." Confirmed: nothing in this Type observes execution; cppcheck's own manual names dynamic analysis and fuzzing as complements it does not replace.
5. **vs Test Automation / Unit & Integration Test Runner (§12) — execution seam.** Tests execute the code and assert behavior; static analysis reasons without executing. cppcheck's manual: static analysis "does not replace... testing."
6. **vs SCA / Dependency Management (§15) — first-party vs dependency seam.** The sast pass recorded the seam as vendor-documented; confirmed here: Semgrep ships Code (first-party) and Supply Chain (dependencies) as separate products; Coverity Scan's pitch is defects in your project's code.
7. **vs Code Editor / IDE (§12, processed) — center-of-gravity seam.** The IDE pass recorded "inspections (built-in static analysis)" as an IDE capability; the IDE's center is authoring, this Type's center is the analysis. IDE integration is a delivery surface of this Type, not identity.
8. **vs Code Review Platform (§12, processed) — human layer above.** The code-review pass recorded: "this Type is the human layer above the analyzer layer." Automated analysis may post comments into review, but the review conversation and human verdict define that Type.
9. **vs Code Migration Platform (§12, processed) — recommend vs transform.** The code-migration pass recorded: "remove the transformation (recommend only) → static analysis." Confirmed: this Type reports; it does not rewrite the codebase (auto-fixes are per-finding suggestions the developer applies, not migration programs).
10. **vs Compiler — conceptual boundary, no directory leaf.** Compilers also examine code without running it and emit located diagnostics; the difference is purpose: a compiler's diagnostics are a byproduct of translation, while the static analyzer's findings ARE the product, drawn from a configurable detection catalog aimed at defects the compiler does not target. cppcheck even offers the Clang parser as an option, showing the machinery can be shared while the purpose differs. Held as a research note; no taxonomy action.

## Historical / Market-Sample Check (§24)

- The lint lineage (1970s C `lint` and its descendants: PC-lint, FindBugs, PVS-Studio 2008, cppcheck) satisfies all three L0 legs with NO platform, NO CI, NO cloud, NO IDE: static examination + rule catalog + located diagnostics. The Type predates the platform era.
- Compiler warnings are a conceptual ancestor (located diagnostics from static examination), distinguished by purpose (see Boundary 10).
- The "platform" packaging (servers, dashboards, trends, verdicts) is era-current market structure, not definitional — the bare-engine poles prove it. The leaf name's "Platform" word is market packaging, not the invariant.
- Historical check PASSES: older, regional, platform-free products fit the definition.

## Uncertainties

- Commercial Coverity platform documentation unreachable (JS app) — deep-analysis technique claims about the commercial engine are not asserted; Coverity evidence limited to the Scan service site.
- Klocwork operational docs unreachable (transport error) — held as market context from a Tier 2 product page; no operational claim depends on it.
- Exact checker/rule counts are version- and language-dependent; no numeric counts asserted anywhere.
- The exact triage-status vocabularies (Semgrep's Open/Reviewing/... set) are product-specific; the final document describes the lifecycle conceptually without importing vendor state names.
- Whether "platform-packaged" static analysis should eventually merge with Code Quality Platform is a taxonomy question for a future joint review if the market consolidates further; current evidence supports three distinct layers (SAST capability / this machinery layer / quality platform layer).

## Final Synthesis

A Static Code Analysis Platform is a product whose center is the static analysis of the program's own code: it examines code without executing it, driven by a packaged, configurable catalog of detection knowledge, and produces located, actionable findings — each pointing at a place in the code with an explanation — delivered to developers where they work (CLI, IDE, CI, or web). Everything else is mature market structure layered on that core: rule configuration, suppression/baselining, severities, fix guidance, IDE/CI delivery, incremental analysis, output formats. The Type spans a packaging spectrum from bare engines to platform-backed suites; the platform layer (persistent quality state + verdicts) belongs to Code Quality Platform territory, and the security-weakness orientation consumed by an AppSec program belongs to SAST territory — same machinery, different layer and orientation. The Type is the machinery layer between them, and the lint lineage proves the core needs none of the modern packaging.
