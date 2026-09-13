# Unit / Integration Test Runner

## Overview

A **Unit / Integration Test Runner** is the developer-side tool that executes the tests written against a codebase's own units and their direct combinations, and turns each test into a pass/fail verdict.

Its defining structure is small:

```text
Test code held in the codebase under test
└── Test = named, independently executable verification unit
    └── Assertion-driven verdict (pass / fail)
        └── The run: discover → select → execute → report
            └── Per-test verdicts + aggregate outcome + machine-usable signal
```

The runner is what makes the verification loop run: without it, tests are just files. It exists to answer one question quickly and repeatedly — *does the code still behave as the tests say it should?* — both while a developer is editing and when the build or CI pipeline invokes it automatically.

When the tested thing stops being the codebase's own units and becomes the whole assembled application driven through its real interface, the product has crossed into End-to-end Testing territory. When the test asset stops being code in the repository and becomes a record managed in a platform, that is Test Automation Platform territory. The runner holds the middle: code-level tests, living with the code, run with the build.

## Users & Context

**Primary user: the software developer working on a codebase.** The runner sits inside the edit–run loop — change code, run tests, read the failure, change again. Speed and failure clarity are the qualities that matter here; a runner that cannot report *which* test failed and *why* does not get used, regardless of its other features.

**Secondary user: the team.** A codebase's test suite is shared property. Tests define behavior collectively; a developer who breaks someone else's test sees the failure in their own run. Conventions (what files count as tests, how tests are named) are project-wide decisions encoded in configuration.

**Non-human invoker: the build and CI automation.** The same runner a developer uses interactively is invoked as one step of a build or pipeline. It is expected to return a machine-usable outcome — an exit code, a machine-readable report — so that the pipeline can pass or fail the change based on the verdicts. The runner produces the verdict; the pipeline reacts to it.

There is no end-user audience, no administrative console, and typically no multi-role permission model. Access control lives in the surrounding systems (repository, CI), not in the runner.

## Core Model

### The defining core

Three structures, all required:

**1. Test code held in the codebase under test.** Tests are ordinary code artifacts of the same project — normally written in the same language as the code they verify, living in the same repository/tree, and bound to the code under test by direct reference: importing the module, calling the class, or sharing the package. The tested things are the codebase's own units (functions, classes, modules) and their direct combinations — the "integration" half of the Type's name. Test code version-controls with the code it verifies; a test written for yesterday's interface is visible as broken today.

**2. The test: a named, independently executable verification unit.** A test is a small named routine — a function, a method in a test class, a block inside a file — that exercises one piece of behavior. Its outcome is binary and determined by assertions: checked expectations about what the code did (a returned value, a raised exception, a state change). Runners realize this in different styles — a matcher/expectation API, the language's plain assert statement with failure introspection, or explicit failure-signaling calls — but the model is the same: an expectation is checked, and a violated expectation fails the test. Each test is individually addressable and can be run on its own.

**3. The run: discover → select → execute → report.** The runner finds the tests (by naming conventions such as file or function prefixes, or by explicit registration), lets the user select a subset (by file, name, tag, or expression), executes them — normally with isolation between tests so one test's state cannot corrupt another's — and reports:

- a verdict per test (passed, failed, and usually skipped or errored)
- failure details: where the assertion failed, what was expected versus what happened
- an aggregate result (how many passed/failed/skipped, how long the run took)
- an outcome signal that automation can consume: the process exit status and/or machine-readable output

Remove any of the three and the Type dissolves: test files with no runner are dead code; verdicts with no tests-in-repo are a platform's records; a discover-execute-report loop with no assertion semantics is a generic script executor.

### Standard capabilities

Mature products commonly add the machinery below. These make the loop practical at scale but do not define the Type — older and minimal runners (including toolchain-native ones) lack several of them and remain clearly this Type.

- **Test organization** — grouping constructs (describe blocks, test classes, suites, nested or sub-tests) that mirror the structure of the code under test and give failures readable names.
- **Lifecycle hooks** — setup and teardown routines at run, file, or per-test scope; fixture mechanisms that provide managed test resources (temporary directories, fresh instances, controlled environment).
- **Selection at scale** — filtering by name pattern, tag, or expression; splitting large suites into shards.
- **Mocking and test doubles** — replacing parts of the system (functions, modules, timers, network, file system) with controlled stand-ins so units can be tested in isolation.
- **Coverage collection** — reporting which lines/branches of the codebase the executed tests actually touched.
- **Parameterized tests** — running one test body over many data cases (each case reported as its own verdict).
- **Skip and expected-failure states** — marking tests as skipped, conditionally disabled, or expected-to-fail, as first-class verdict categories alongside pass/fail.
- **Parallel execution** — running tests concurrently across processes or workers.
- **Machine-readable reports** — output formats (XML/JSON families) that build and CI tooling import.
- **IDE integration** — test explorers and in-editor run controls that invoke the same runner and display the same verdicts inside the editor.
- **Developer-shaped failure diagnostics** — assertion introspection (showing intermediate values), diffs, and source context, engineered so the failure report itself explains the bug.

### One structure, many implementations

The core model is conceptual; each ecosystem realizes it differently:

```text
Concept:            binding tests to code
Implementations:    same-package access (including private members),
                    explicit import of a public interface ("black box"),
                    same-file or sibling-file definitions

Concept:            the test unit
Implementations:    annotated methods in test classes,
                    plain functions matched by name prefix,
                    blocks registered inside grouping constructs,
                    sub-tests spawned within a parent test

Concept:            verdict mechanism
Implementations:    expectation/matcher API, language-native assert
                    with introspection, explicit failure-signaling calls

Concept:            the runner's substrate
Implementations:    installed package in the project,
                    platform with pluggable test engines,
                    part of the language toolchain itself
```

A reader who has only seen one ecosystem's style should be able to recognize any other as the same Type.

## How It Works

### The authoring step

A developer writes a test into the codebase: create a test file (named per the project's convention), import the code under test, and write a named routine that exercises a behavior and checks the result.

```text
create test file (convention-compliant name)
→ import / reference the code under test
→ write the test: exercise a behavior, assert the expected outcome
→ done — no separate registration step in convention-driven runners
```

### The run

Invoking the runner starts the same loop whether it comes from a terminal, an IDE button, a build script, or CI:

```text
invoke runner (bare, or with a file pattern / name filter / tags)
→ discover: find test files and test units by convention or registration
→ select: keep the tests matching the request (default: all)
→ execute: run the selected tests, isolated, one by one or in parallel
→ report: print per-test verdicts and failure details, then the aggregate
→ exit with an outcome signal (nonzero when something failed)
```

### Reacting to failure

A failed run produces targeted diagnostics — the failing test's name and location, the violated expectation, the actual versus expected values. The developer fixes the code (or the test), then re-runs. Mature products accelerate the re-run: watch mode re-executes affected tests as files change; related-test selection runs only the tests that cover a changed source file; failure-only re-runs repeat just the tests that failed last time; seeded randomization helps reproduce order-dependent (flaky) failures. None of these accelerators is required for the Type; the loop itself is.

### In the build

The same invocation is scripted into the project's build and CI: the pipeline calls the runner in its non-interactive mode, and the runner answers with an exit status and a machine-readable report. CI products treat this as the verification step: the change passes only if the runner's verdicts pass. Runners commonly detect a CI context and adjust behavior accordingly (for example, treating a new output snapshot as a failure to be confirmed rather than silently recorded).

### Capability tiers

- **Defining core** — test code in the codebase; named assertion-driven tests; discover/select/execute/report with a machine-usable outcome.
- **Standard capabilities** — grouping, hooks, selection, mocking, coverage, parameterization, skips, parallelism, reports, IDE integration, failure diagnostics.
- **Common variants / optional** — watch mode posture (absent, opt-in, default), snapshot testing, component/DOM execution environments, benchmarks/fuzzing/doctests riding the same command, in-source test authoring.

## Interfaces

The runner is CLI-first. Its surfaces, described conceptually:

### Command line

The primary interface.

- Purpose: invoke runs on demand with precise control.
- Typical information: command name; positional patterns (files or name filters); flags for selection (name pattern, tags), execution (parallelism, shards, bail-on-failure), output (verbosity, reporters, coverage), and mode (watch, CI detection).
- Primary actions: run all tests; run a subset; watch; re-run failures; list discovered tests without running them.

### Test output

What the user actually reads.

- Purpose: communicate verdicts and failures.
- Typical information: per-test verdicts (often with durations); grouped by file/suite; failure sections with assertion details and source context; a final aggregate (passed/failed/skipped counts, total time).
- Primary actions: none — this is a read surface; its quality is the product.

### Configuration

Where project conventions are encoded.

- Purpose: bind the runner to the project's conventions (which files are tests, how to transform or load them, execution settings, reporter setup).
- Typical information: test-file patterns, environment settings, coverage scope, reporter list; often placed in a dedicated config file or the project's manifest, with build-tool equivalents.
- Primary actions: define conventions; override per invocation (command-line flags commonly take precedence).

### IDE test surface

The editor-embedded face of the same runner.

- Purpose: run and inspect tests without leaving the code.
- Typical information: a tree of discovered tests; verdict icons next to tests; failure detail panes; gutter controls beside test definitions.
- Primary actions: run a test, a file, or all; re-run on change; jump to failure.

### Machine output

The automation face.

- Purpose: let build/CI tooling consume results.
- Typical information: structured result formats (XML/JSON families) and the process exit status; some runners document distinct exit codes for outcomes such as all-passed, failures, or no tests collected.
- Primary actions: consumed, not acted on; CI systems branch on the outcome.

## Important Rules / Behaviors

### A failed assertion means a failed test — and nothing else runs away with the verdict

The verdict is local: one violated expectation fails the test containing it; the runner continues with the remaining tests (optionally stopping early after a configurable number of failures). A test that errors — throws, crashes, or signals a fatal failure — is a failure of that test, not of the run; the run's aggregate simply includes it. A small number of products offer fatal failure modes that abort the current test only, keeping the rest of the run intact.

### Tests are isolated by default expectation

The working contract is that each test starts fresh: products go to real lengths to enforce or encourage it (fresh instances per test, per-test temporary directories, per-test environment and mock state). State that leaks between tests is treated as a defect of the tests, and some products expose order randomization specifically to expose hidden dependencies.

### Discovery conventions are strict

What counts as a test is convention-defined: file name patterns and function/class name prefixes decide whether code is collected at all. Misname a test and it silently never runs — which is why runners expose a "list what would run" action, and why "no tests collected" is often a distinct, reported outcome (some products treat it as its own exit status, others offer a flag to pass in that case for pipelines where emptiness is legitimate).

### Selection changes the run, not the suite

Filters, tags, and patterns choose which discovered tests execute; they never modify the population. Skipping is different: a skipped test is part of the suite with a recorded non-execution state, reported as its own verdict category.

### Flakiness is a managed phenomenon

Runs are expected to be repeatable: same code, same verdicts. Products acknowledge order- and environment-dependence with machinery — seeded ordering, failure re-runs, cache of last results — but the canonical contract remains deterministic verdicts on deterministic code.

### The outcome signal is a contract

The exit status means what the documentation says it means. Pipelines are built on it; a runner that exits zero on failure breaks the build's trust. This is why the machine-facing behavior (exit codes, report formats, CI-mode detection) is documented with the same care as the authoring API.

## Variants

- **Language-ecosystem families** — the Type exists per language ecosystem, with the same loop realized in each: the JavaScript family (expectation-API style, snapshot testing, component environments), the Python style (plain assert with introspection, fixture system), the JVM platform style (annotated test classes, pluggable engine architecture, deep build-tool integration), the toolchain-native style (testing built into the language's own command, minimal by design).
- **Substrate variants** — installed as a project package; shipped as part of the language toolchain; architected as a platform on which multiple test engines run (including engines for older test generations).
- **Assertion philosophy** — rich matcher/expectation APIs versus minimal language-native assertions with diagnostic introspection versus explicit failure-signaling calls. A family convention, not a Type requirement.
- **Interaction posture** — watch-mode-first runners oriented entirely around the editing loop; invocation-first runners with watch as an option; toolchain runners with no watch at all (loop closed by editors or external tools).
- **Scope extensions** — component/DOM/browser execution environments bring UI-level component testing under the runner's loop; benchmark, fuzzing, and doctest modes ride the same command. These extend the Type without changing it; the center of gravity stays at code-level verification.
- **Suite-scale machinery** — sharding, parallel worker pools, caching, and failure-only re-runs appear as suites grow large; minimal runners lack them without losing Type identity.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Test Automation Platform | closest sibling | the platform's center is a managed multi-surface test asset (recorded/maintained in a platform repository) plus execution and maintenance machinery; the runner's test asset is plain code in the repository, with no recorder, no platform asset store, no results database |
| End-to-end Testing Platform | sibling, scope seam | E2E exercises the whole assembled application through its real interface and produces pre-release journey verdicts; the runner exercises code units and their direct combinations. Capability overlap is real (unit runners can execute DOM/component tests), so the seam is center of gravity |
| Continuous Integration Platform | consumer | CI owns the pipeline (checkout, build orchestration, scheduling, artifacts, notifications) and invokes the runner as the verification step; the runner produces verdicts, CI reacts to them |
| Software Test Management | record-keeping sibling | test management holds test cases, runs, and coverage as managed records with traceability; the runner produces verdicts as run output. Run output is commonly imported into such systems; the runner holds no case repository |
| Build Automation System | interlocked neighbor | builds produce artifacts; runners verify behavior. They interlock at the invocation surface (build tasks call the runner); a build script with inline assertions is the Type's minimal ancestor, not a build system |
| Static Code Analysis / Code Quality Platform | different mechanism | inspects code without executing it; the runner executes code and checks behavior against expectations |
| Debugger | complementary developer tool | inspects one execution interactively; the runner verifies many tests in batch. Debuggers commonly attach to a failing test run |

## Representative Products

- **Jest** — JavaScript/TypeScript; batteries-included runner (matchers, mocking, snapshots, coverage built in)
- **Vitest** — JavaScript/TypeScript; Vite-powered runner with a Jest-compatible authoring API, watch-mode-first workflow, and browser-mode component testing
- **pytest** — Python; minimal core (plain assert + discovery conventions) with a large plugin/fixture ecosystem
- **JUnit** — Java/JVM; the canonical xUnit-family platform with a pluggable test-engine architecture and first-class IDE/build-tool integration
- **go test** — Go; the runner as part of the language toolchain itself (test functions in `_test.go` files, failure-signaling methods, benchmarks/fuzzing/examples in the same command)

The definition was checked against the older xUnit-style generation (still executable on modern platforms — e.g., engines that run the previous Java test generations unchanged) and against the toolchain-native pole, so the defining core does not depend on any modern machinery (watch mode, parallelism, coverage, mocking, snapshots).

## Sources

Research date: **2026-09-09**

- Jest — Getting Started: https://jestjs.io/docs/getting-started ; CLI Options: https://jestjs.io/docs/cli
- Vitest — Getting Started / Guide: https://vitest.dev/guide/
- pytest — Get Started: https://docs.pytest.org/en/stable/getting-started.html ; Exit Codes: https://docs.pytest.org/en/stable/reference/exit-codes.html
- JUnit — User Guide (Overview): https://junit.org/junit5/docs/current/user-guide/index.html
- Go — `testing` package (standard library reference): https://pkg.go.dev/testing

> Sourcing limitation: JUnit's writing-tests section pages were unreachable (404) at research time; JUnit-level statements are kept to what its user-guide overview and section structure directly document. Detailed per-product evidence, cross-product comparison, and abstraction levels are recorded in the paired Research Notes.
