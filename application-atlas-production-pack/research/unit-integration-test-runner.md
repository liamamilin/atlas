# Research Notes — Unit / Integration Test Runner

Research date: 2026-09-09
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a Unit / Integration Test Runner actually is as an Application Type: what exists inside it, who uses it, how a test run works end to end, what rules govern verdicts, and where its boundaries lie against neighboring developer-tooling Types (Test Automation Platform, End-to-end Testing Platform, Continuous Integration Platform, Software Test Management, Build Automation System).

## Initial Boundary (hypothesis before research)

Hypothesis: this Type is the code-level verification loop of software development. Developers write tests in the same language and codebase as the code under test; a runner discovers those tests, executes them, and reports pass/fail verdicts quickly enough to sit inside the developer's edit-run loop and inside the build.

Expected confusions (pre-registered):

- vs Test Automation Platform — sibling pass (processed 2026-09-09) pre-hung the seam: "code-layer tests living with the codebase and running with the build, no managed platform asset, no recorder/repository machinery — forward flag remains for that pass"
- vs End-to-end Testing Platform — sibling pass (processed 2026-09-08) pre-hung: "assembled app vs isolated components; Cypress/Playwright bundle component testing as capability overlap"
- vs Continuous Integration Platform — CI invokes the runner; the runner is a step, not the pipeline
- vs Software Test Management — verdicts are produced here; cases/runs/coverage-as-record live there

## Research Questions

1. What is the unit of verification (the "test") and how is a verdict produced?
2. Where does test code live relative to the code under test, and how is it bound to it?
3. How does the runner find tests (convention vs registration) and how does the user select a subset?
4. What does a run report, to whom, and through what surfaces (CLI, IDE, build tool, CI)?
5. What machinery surrounds the loop (watch mode, mocking, fixtures, coverage, snapshots, parallelism)?
6. What is invariant vs common-mature vs variant vs vendor-specific?
7. Does the older xUnit-style generation still satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different "customer layers" (JS consumer-grade batteries-included; modern Vite-era DX-first; Python minimal-core-plus-plugins; Java enterprise xUnit platform; language-toolchain-native):

- **Jest** (JavaScript/TypeScript) — batteries-included runner; OpenJS Foundation
- **Vitest** (JavaScript/TypeScript) — Vite-powered next-generation runner, Jest-compatible API
- **pytest** (Python) — minimal core, plugin-ecosystem philosophy
- **JUnit** (Java/JVM) — the canonical xUnit-family platform; enterprise build-tool integration
- **go test** (Go) — platform-native: the runner is part of the language toolchain itself

## Sources

All Tier 1 (official product documentation), fetched 2026-09-09:

- Jest Getting Started — https://jestjs.io/docs/getting-started
- Jest CLI Options — https://jestjs.io/docs/cli
- Vitest Getting Started / Guide — https://vitest.dev/guide/
- pytest Get Started — https://docs.pytest.org/en/stable/getting-started.html
- pytest Exit Codes — https://docs.pytest.org/en/stable/reference/exit-codes.html
- JUnit User Guide Overview — https://junit.org/junit5/docs/current/user-guide/index.html
- Go `testing` package documentation — https://pkg.go.dev/testing

Source-access limitations:

- JUnit writing-tests detail pages returned 404 on two attempts (junit.org and docs.junit.org paths); JUnit evidence rests on the user-guide overview page plus the user-guide section structure (directly observed), not full section text. JUnit-level claims are phrased accordingly.
- go.dev tutorial page (add-a-test) unreachable; substituted pkg.go.dev/testing (official standard-library reference).
- Component-testing overlap from the E2E side (Cypress/Playwright) not re-fetched this pass; overlap documented from the runner side (Vitest browser-mode/component-testing documentation) per the pre-hung flag.

## Product Observations

### Product A — Jest (JavaScript/TypeScript)

Evidence layer A (direct) unless noted.

Key observations:

- Test code lives in the project as ordinary files: `sum.test.js` imports/requires `./sum` — the code under test is the project's own module. Test file naming convention (`*.test.js`).
- The test is a named unit: `test('adds 1 + 2 to equal 3', () => { expect(sum(1, 2)).toBe(3); })`. Verdict produced by the expect/matcher API; grouping via `describe` blocks; globals (`describe`, `test`, `expect`, `beforeEach`) injectable, or importable from `@jest/globals`.
- Invocation is a CLI: `jest`, optionally with a pattern (`jest my-test`), `--config=config.json`, wired into `package.json` scripts (`"test": "jest"`).
- Output: per-file/per-test verdicts with timings — `PASS ./sum.test.js ✓ adds 1 + 2 to equal 3 (5ms)`.
- Developer-loop machinery on the CLI: `--watch` (rerun tests related to changed files), `--watchAll`, `-o/--onlyChanged` (based on git/hg), `--findRelatedTests` (run tests covering given source files), `--onlyFailures`, `-t/--testNamePattern` (filter by spec name), `--listTests`, `--shard=1/3` (split the suite), `--randomize --seed` (reproduce flaky ordering), `--passWithNoTests`.
- CI/automation surface: `--ci` flag ("will assume it is running in a CI environment" — changes snapshot behavior), `--json` results, `--outputFile`, pluggable `--reporters` (example given: `jest-junit`).
- Coverage built in: `--coverage`, `--collectCoverageFrom`, `--coverageProvider=babel|v8`.
- Mocking built in: Mock Functions doc section; `--clearMocks/--resetMocks/--restoreMocks` run-scope flags.
- Snapshot testing: dedicated guide (nav), `--updateSnapshot` flag; snapshot behavior changes under `--ci`.
- Environments: `--env=<environment>` (examples documented: `jsdom`, `node`) — the runner can execute tests in a DOM-like environment for component-level testing.
- Isolation/parallelism: worker pool (`--maxWorkers`, `--workerThreads` experimental), `--runInBand` serial mode; per-test timeout (`--testTimeout`, documented default 5000 ms — vendor fact, L3).
- Docs structure (nav): Using Matchers, Testing Asynchronous Code, Setup and Teardown, Mock Functions, Snapshot Testing — the surrounding machinery is first-class documentation.
- Ecosystem framing: Jest's own page names Vitest as "an API that is compatible with Jest" — cross-product recognition of a shared test-authoring API surface.

### Product B — Vitest (JavaScript/TypeScript)

Evidence layer A.

Key observations:

- Self-description: "a next generation testing framework powered by Vite."
- Same authoring shape as Jest: `sum.test.js` imports `sum` from `./sum.js`; `import { expect, test } from 'vitest'`; `test('adds 1 + 2 to equal 3', () => { expect(sum(1, 2)).toBe(3) })`.
- Discovery by convention: "By default, tests must contain `.test.` or `.spec.` in their file name."
- Invocation: `vitest` (watch mode by default — "To run tests once without watching for file changes, use `vitest run`"), wired as `"test": "vitest"` in package.json.
- Output: per-file and per-test checkmarks plus aggregate — `Test Files 1 passed (1) / Tests 1 passed (1) / Duration 311ms`.
- Run modes: watch default vs `vitest run`; flags like `--reporter`, `--coverage`; Test Filtering, Test Tags, Test Projects, Parallelism, Reporters, Coverage as first-class guide sections.
- IDE surface: official VS Code extension ("Vitest Explorer") for the in-editor test experience.
- Component/browser testing documented as a capability: Browser Mode section (Why Browser Mode, Component Testing, Visual Regression Testing, ARIA Snapshots) — the unit/integration runner extending into DOM/component territory. This is the documented capability-overlap point with the E2E seam.
- Broader authoring machinery (nav): Setup and Teardown, Mock Functions, Snapshot Testing, Mocking modules/timers/dates/file-system/requests/classes/globals, In-Source Testing, Testing Types, Benchmarking, Debugging Tests.
- Programmatic API: "Running Tests via API" section — the runner embeddable in other tooling.
- Generated-artifact directory (`.vitest/`) recommended for gitignore — run artifacts live in the workspace.

### Product C — pytest (Python)

Evidence layer A.

Key observations:

- Test code is ordinary Python: `test_sample.py` defines both `func(x)` and `test_answer()`; assertion is the plain language `assert` statement — "You can use the `assert` statement to verify test expectations. pytest's Advanced assertion introspection will intelligently report intermediate values of the assert expression."
- Discovery by convention: "pytest will run all files of the form `test_*.py` or `*_test.py` in the current directory and its subdirectories. More generally, it follows standard test discovery rules."
- The run is a collection→execution→report session: "collected 1 item", progress markers (`.`, `F`, `[100%]`), then a FAILURES section showing the source line, the assertion, and the computed intermediate values (`assert 4 == 5 + where 4 = func(3)`), then a short summary (`FAILED test_sample.py::test_answer - assert 4 == 5`) and timing (`1 failed in 0.12s`).
- Selection: `pytest -q test_class.py` (by file), `pytest -k TestClassDemoInstance` (substring expression over names).
- Exception verdicts: `with pytest.raises(SystemExit): f()`.
- Test organization: plain functions or `Test`-prefixed classes; "There is no need to subclass anything"; per-test class instances — "each test has a unique instance of the class… detrimental to test isolation" — isolation is an explicit documented concern.
- Fixture machinery: built-in fixtures requested via function signature (`tmp_path` — "pytest creates a unique-per-test-invocation temporary directory"); `pytest --fixtures` lists builtin and custom fixtures; fixtures reference + "About fixtures" explanation sections.
- Surrounding machinery (nav): marks, parametrize, subtests, monkeypatch (mocking), doctests, re-run failed tests + cache state, output management, log capture, stdout/stderr capture, skip and xfail ("tests that cannot succeed"), plugins (installing/writing), unittest integration, "xunit-style set-up" (the historical xUnit pattern is documented as a compatibility mode), CI Pipelines explanation, Flaky tests explanation.
- Exit codes as public API: documented seven codes — 0 all collected and passed; 1 collected and run but some failed; 2 interrupted by user; 3 internal error; 4 usage error; 5 no tests collected; 6 max warnings exceeded. `pytest.ExitCode` importable.
- Version sanity: `pytest --version` → `pytest 9.1.1` (from docs).

### Product D — JUnit (Java/JVM)

Evidence layer A for the overview/architecture; section content rests on the user-guide structure (fetch limitation recorded above) — phrasing kept at observed granularity.

Key observations:

- Architecture: "JUnit 6.1.3 = JUnit Platform + JUnit Jupiter + JUnit Vintage."
  - Platform: "serves as a foundation for launching testing frameworks on the JVM", defines the `TestEngine` API, provides a Console Launcher "to launch the platform from the command line" and a Suite Engine; first-class IDE support documented for IntelliJ IDEA, Eclipse, NetBeans, Visual Studio Code; build-tool support documented for Gradle, Maven, Ant, Bazel, sbt.
  - Jupiter: "the combination of the programming model and extension model for writing JUnit tests and extensions," ships its own TestEngine.
  - Vintage: a TestEngine "for running JUnit 3 and JUnit 4 based tests on the platform" (deprecated migration path) — direct evidence that the previous generation's test assets still execute on the current runner.
- Writing-tests surface (from user-guide section list, observed): Annotations; Test Classes and Methods; Display Names; Assertions; Assumptions; Exception Handling; Disabling Tests; Conditional Test Execution; Tagging and Filtering; Test Execution Order; Test Instance Lifecycle; Nested Tests; Dependency Injection for Constructors and Methods; Repeated Tests; Parameterized Classes and Tests; Test Templates; Dynamic Tests; Timeouts; Parallel Execution; Built-in Extensions.
- Running-tests surface (from section list, observed): IDE Support; Build Support; Console Launcher; Source Launcher; Discovery Selectors; Configuration Parameters; Tags; Capturing Standard Output/Error; Listeners and Interceptors; JUnit Platform Reporting (advanced topic); Launcher API; Test Engines.
- Reading: the same verification loop (discover via selectors, execute via engine, report via listeners/reporting), realized as a platform that other engines (including the Vintage engine for the older JUnit 3/4 generation) can plug into, and surfaced through IDEs and build tools rather than a proprietary console.

### Product E — go test (Go)

Evidence layer A (official standard-library reference for the `testing` package, which documents its contract with the `go test` command).

Key observations:

- Platform-native: "Package testing provides support for automated testing of Go packages. It is intended to be used in concert with the 'go test' command."
- Test = function: "automates execution of any function of the form `func TestXxx(*testing.T)` where Xxx does not start with a lowercase letter. The function name serves to identify the test routine."
- Test code bound to the codebase at package grain: "give that file a name ending in `_test.go`. The file will be excluded from regular package builds but will be included when the 'go test' command is run."
  - Two binding modes documented: same package ("may refer to unexported identifiers") vs a `foo_test` package ("the package being tested must be imported explicitly and only its exported identifiers may be used. This is known as 'black box' testing").
- Verdict by failure signaling, not assertion API: "use T.Error, T.Fail or related methods to signal failure" — failure is explicitly signaled (`t.Errorf`, `t.Fatal`, `t.FailNow`); `FailNow` stops the test and continues at the next test.
- Subtests: `t.Run(name, f)` "allow[s] defining subtests… without having to define separate functions for each. This enables uses like table-driven benchmarks and creating hierarchical tests"; each subtest has a hierarchical name (top-level name + slash-joined run names).
- Selection: `-run` flag is "an unanchored regular expression that matches the test's name", slash-separated for subtests (`go test -run Foo/A=1`).
- Skipping and modes: `t.Skip`; `testing.Short()` / `-test.short` mode; `testing.Verbose()` / `-test.v` verbose output flag.
- Run-scoped setup/teardown: `TestMain(m *testing.M)` wraps the whole test binary ("can do whatever setup and teardown is necessary around a call to m.Run"); `t.Cleanup` registers per-test cleanup; `t.TempDir`/`t.Setenv` managed test resources.
- Verdict reporting: per-test logging accumulated and dumped on failure (Log printed "only if the test fails or the -test.v flag is set"); the process outcome is an exit code — TestMain: "m.Run will return an exit code that may be passed to os.Exit."
- Parallelism: `t.Parallel()` marks tests to run in parallel; subtest grouping controls parallel scopes.
- Adjacent capabilities in the same command (documented as distinct function families): benchmarks (`func BenchmarkXxx(*testing.B)`, `-bench`), examples (`func ExampleHello()` verified against a comment "// Output: hello" — output comparison as verification), fuzzing (`func FuzzXxx(*testing.F)`, `-fuzz`, seed corpus), coverage (`Coverage()`, `CoverMode()`, "go test -cover" and "go tool cover").
- No built-in watch mode and no built-in assertion/matcher library in the fetched reference — the toolchain floor of the Type.

## Cross-product Comparison

| Dimension | Jest | Vitest | pytest | JUnit | go test |
|---|---|---|---|---|---|
| Test code location | in project, `*.test.js` | in project, `.test.`/`.spec.` (default) | in project, `test_*.py`/`*_test.py` | test classes in project source tree | `_test.go` files, excluded from normal builds |
| Binding to code under test | import/require modules | import modules | import / same-file definitions | same project class path | same package (incl. unexported) or `_test` package (black box) |
| Test unit | `test`/`it` in `describe` nesting | `test` in `describe` nesting | `test_*` functions, `Test*` classes | test classes and methods (annotated) | `TestXxx(*testing.T)` functions + `t.Run` subtests |
| Verdict mechanism | `expect().toBe()` matcher API | same expect API (Jest-compatible) | plain `assert` + introspection; `pytest.raises` | Assertions (+ Assumptions) doc sections | `t.Error/t.Fatal/t.Fail` signaling methods |
| Discovery | globs (`testMatch`), file-pattern regex arg | filename convention | filename + prefix conventions | Discovery Selectors / engine discovery | function-name + file-name convention |
| Selection | path pattern, `-t` name regex, `--shard` | filtering, tags, projects | file args, `-k` expressions | tags/filtering, discovery selectors | `-run` name regex (slash-aware) |
| Aggregate report | PASS/FAIL per file + test, `--json` | per-file/per-test + `Test Files n passed` | dots, short summary, FAILURES section | reporting via platform (listeners/reporting) | per-test log + summary; verbose flag |
| Machine outcome signal | exit via CLI; `--ci`, `--json`, `--outputFile`, reporters (`jest-junit`) | reporters; run via API | 7 documented exit codes (`pytest.ExitCode`) | first-class Gradle/Maven/Ant/Bazel/sbt integration | `m.Run()` exit code in TestMain |
| Watch mode | `--watch`/`--watchAll` (opt-in) | default (watch; `vitest run` for once) | not in core (plugin ecosystem) | not observed (IDE-driven loop instead) | absent |
| Mocking | built-in (mock functions, mock-state flags) | built-in (modules/timers/fs/requests…) | `monkeypatch` built-in; plugins | extension model | none built-in (interfaces/manual) |
| Coverage | built-in (`--coverage`) | built-in (guide section) | plugin ecosystem | not directly observed | built-in (`-cover`, Coverage()) |
| Parameterized tests | `test.each`/`describe.each` | documented | `parametrize` | "Parameterized Classes and Tests" | table-driven via subtests |
| Snapshot testing | yes (guide + `--updateSnapshot`) | yes (guide) | no | no | no (but Example output-checking is adjacent) |
| Parallelism | worker pool flags | parallelism guide/projects | plugin ecosystem | "Parallel Execution" section | `t.Parallel()` |
| Skips/conditional | skip/todo states (observed via `--collectTests` doc) | tags/annotations | skip/xfail doc | Disabling/Conditional sections | `t.Skip`, `-short` |
| IDE surface | ecosystem editors | official VS Code extension | editors/run integrations (nav: Good Integration Practices) | IntelliJ/Eclipse/NetBeans/VS Code "first-class" | editors/toolchain |

Reading of the table: every row above "Watch mode" is filled in all five columns (cross-product commonality, Layer B→L0/L1 candidates). Watch mode, snapshot testing, and mocking machinery vary substantially (variant-level). The five products also span the substrate axis: three are installed packages (Jest, Vitest, pytest), one is a platform with pluggable engines (JUnit), one is inside the language toolchain (go test) — substrate is not the invariant.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The Type is recognizable when all three of these hold:

1. **Test code held in the codebase under test.** Tests are code artifacts of the same project, written (normally) in the same language, exercising the project's own units — functions, classes, modules — and their direct combinations (integration). The binding to the code under test is direct reference/import/package membership, and the test code lives in the same repository/tree as the code it verifies. Remove → Test Automation Platform / E2E Testing Platform territory (assets managed in a platform, or a detached assembled app), or an unbound script collection.
2. **The test as an independently executable verification unit with an assertion-driven verdict.** A test is a named, individually addressable routine whose pass/fail outcome is determined by assertions/expectations or explicit failure signaling about the behavior of the exercised code. Remove → a coverage/profiling tool, or an assertion library with no execution.
3. **The run: discover → select → execute → report verdicts, with a machine-usable outcome.** The runner finds tests by convention or registration, allows selection of subsets, executes them (individually isolated), and reports per-test verdicts plus an aggregate result, exiting/signaling an outcome that automation (build tools, CI) can consume. Remove → an assertion library nobody runs; a generic script executor with no verification semantics; a results dashboard with no execution.

Jointly load-bearing:

- 1 alone = test files nobody executes (dead code / assertion library)
- 2 alone = assertion library / scripting
- 3 alone = generic script/task runner or CI pipeline over non-verification scripts
- 1+2 without 3 = manually-run verification (no loop)
- 1+3 without 2 = build steps that run scripts but establish no per-test behavior verdicts
- 2+3 without 1 = a platform executing detached/recorded tests = Test Automation Platform / E2E territory

### L1 — Common Mature Structure

Very common in mature modern runners; not required for the Type to be recognizable:

- test organization/grouping (nesting constructs, classes, suites, subtests)
- lifecycle hooks (setup/teardown at run/file/test scope)
- selection by name/path/tag and sharding for large suites
- mocking/test-double machinery or ecosystem equivalents
- coverage collection
- parameterized/data-driven tests
- skip/conditional/expected-failure states
- parallel execution
- machine-readable report formats (XML/JSON) consumed by build/CI tooling
- IDE integration surfaces (test explorers, gutter run controls)
- failure diagnostics engineered for the developer (assertion introspection, diffs, source context)

### L2 — Variant / Optional Structure

- substrate: installed package vs platform-with-engines vs language-toolchain-native
- assertion style: matcher API vs native assert vs failure-signaling methods
- watch mode (opt-in, default-on, plugin, or absent — absent at the toolchain-native pole)
- snapshot testing (strong in the JS-runner family; absent elsewhere sampled)
- component/DOM/browser testing capability (Vitest browser mode; Jest `--env jsdom`) — capability overlap toward E2E/component territory
- benchmarks/fuzzing/examples-as-verification riding the same command (go test; Vitest benchmarking)
- in-source testing, doctest integration, type-testing (product-specific authoring placements)
- isolation model details (process-per-file vs in-process; fresh instances per test)

### L3 — Vendor-specific Structure

(stays in these notes; not in the final document)

- Jest: `NODE_ENV=test` default; watchman file-crawling; `--detectOpenHandles`/`--forceExit` diagnostics; babel-based transform infra; injectable globals vs `@jest/globals`; documented default per-test timeout of 5000 ms; seed-based randomization machinery
- Vitest: Vite config/plugin reuse; UI mode; `.vitest/` artifact directory convention; in-source testing; test annotations
- pytest: fixture system as dependency-injection mechanism (`tmp_path`, `monkeypatch` as builtin fixtures); pluggy hook/plugin architecture; seven-code public exit-code enum (incl. code 6 for max warnings); unittest/xunit-style compatibility layers; doctest collection
- JUnit: Platform/Jupiter/Vintage three-module architecture; `TestEngine` SPI; Console Launcher and Launcher API; extension model with lifecycle callbacks; Vintage engine for JUnit 3/4 migration; requires Java 17+ at runtime (version-dated fact)
- go test: `TestMain(m *testing.M)` whole-binary hook; `foo_test` black-box package mode; Example functions verified against `// Output:` comments; built-in fuzzing engine with seed corpus and `testdata/fuzz` layout; `testing.Short()` mode; `-artifacts` directories (recent toolchain additions)

## Rejected Findings (anti-overfit)

- **Watch mode is NOT definitional.** Opt-in at Jest, default at Vitest, plugin territory at pytest, absent in the go toolchain reference. The invariant is the cheap re-runnable loop, not file-watching.
- **A matcher/expect API is NOT definitional.** pytest uses the plain language `assert` with introspection; go test signals failure via methods and plain comparisons. The invariant is an assertion-driven verdict, not any particular assertion API.
- **Snapshot testing is NOT definitional** (2/5, JS-family). Variant.
- **Mocking is NOT definitional.** go test ships none built-in. Common machinery, not the Type.
- **Coverage is NOT definitional** (built into 3/5 sampled, plugin elsewhere). Common.
- **Parallel execution is NOT definitional** (realized via workers/flags/plugins/annotations; absence still leaves the Type). Common.
- **The "framework/package" substrate is NOT definitional** — go test is part of the toolchain; JUnit is a platform others launch. The invariant is the loop, not the packaging.
- **Per-test timing numbers, default timeouts, worker defaults** — vendor facts (L3), excluded from the canonical document.
- **Shared Jest/Vitest API shape does not imply one product** — the authoring API surface (describe/test/expect) is a family convention of the JS ecosystem, not a Type requirement (the §22 anti-overfitting rule applied to API surface).

## Boundary Findings

**vs Test Automation Platform** (flag pre-hung by that pass — DISCHARGED here, keep-both RATIFIED):
The seam held exactly as pre-hung. The runner's test asset is test code in the codebase: ordinary files/classes in the repository, executed by CLI/build tool, with no managed platform asset, no recorder, no repository machinery, no results database. The Test Automation Platform's center is the managed multi-surface test asset + execution + maintenance (its own pass's center). Products on the runner side (this pass's five) carry none of the platform machinery; products on the platform side (its pass's Ranorex/Leapwork/Tosca sample) hold test assets in platform repositories with recorders/maintenance layers. Keep both; the runner is where code-level tests live, the platform is where managed automation assets live.

**vs End-to-end Testing Platform** (flag pre-hung by that pass — DISCHARGED here, keep-both RATIFIED):
The seam is the size of the exercised thing and the loop it serves. The runner exercises the codebase's own units and their direct combinations, feeding the developer's edit-run loop and the build's verdict. The E2E platform exercises the whole assembled application through its real interface, producing pre-release journey verdicts. Capability overlap is real and documented from this side: Vitest documents browser-mode component testing; Jest documents jsdom environments — a unit runner can reach component/DOM scope without changing Types. The drift test: when the center of gravity moves from code units to whole-app user journeys (recording, cross-browser grids, pre-release gates), the product has crossed into the E2E Type.

**vs Continuous Integration Platform:**
The runner is invoked by CI as a step; the CI platform owns the pipeline (checkout, build orchestration, job scheduling, artifacts, notifications). Evidence of the interlock from this side: Jest `--ci` (behavior changes when it detects CI), pytest's CI Pipelines guidance, JUnit's build-tool first-class support, go test's exit code for `os.Exit`-style pipeline consumption. The runner produces the verdict; CI reacts to it. Remove the pipeline → still a runner; remove the runner → a pipeline with no verification step.

**vs Software Test Management:**
Executable-vs-record seam, consistent with the test-automation pass's ratification. The runner produces verdicts as run output; test management holds cases/runs/coverage as managed records with traceability. The runner's output is consumed by (or imported into) such systems; the runner itself holds no case repository.

**vs Build Automation System:**
Build produces artifacts; the runner verifies behavior. They interlock at the invocation surface (npm scripts, `go test` as a toolchain command, Gradle/Maven test tasks). A build system that runs tests delegates the verification semantics to a runner (or bakes a minimal one in — the boundary case is a build script with inline assertions, which is the Type's minimal ancestor, not a build system).

**vs Code Quality / Static Analysis Platform:**
Static analysis inspects code without executing it; the runner executes code and checks behavior against expectations. (Not re-researched this pass; kept as a conceptual seam.)

**vs Debugger:**
Both are developer-facing code tools. The debugger inspects one execution interactively; the runner verifies many tests in batch and reports verdicts. Debuggers can attach to a failing test run — complementary, not overlapping Types.

## Historical / Market-Sample Check

- The xUnit generation predates all sampled products' current shapes, and the evidence is visible inside this pass's own sources: pytest documents "xunit-style set-up" as a compatibility mode and its assertion introspection as avoiding "the many names of JUnit legacy methods"; JUnit's Vintage engine executes "JUnit 3 and JUnit 4 based tests" on the modern platform. A JUnit-3-era suite — test classes in the project, assert-based methods, run from IDE/Ant with pass/fail counts — satisfies all three L0 legs with no watch mode, no parallelism, no coverage, no snapshots.
- The toolchain-native pole (go test) shows the Type does not require a separately installed product; a minimal per-language test convention executed by a build command is the Type's floor.
- The conceptual ancestor — make/scripts running test binaries that exit nonzero on failure — satisfies legs 1–3 in minimal form (tests in tree, assertion-driven verdict, run+report with machine signal). The Type is therefore not an artifact of the modern framework era.
- Conclusion: the L0 definition survives the historical check; nothing modern (watch, parallelism, coverage, mocking, snapshots) is load-bearing in the definition.

## Uncertainties

- pytest's coverage story (pytest-cov) and parallel story (xdist) were not directly fetched; coverage/parallelism are held at "common via built-in or ecosystem" strength, not per-product detail.
- JUnit writing-tests section text unreachable (404 ×2); JUnit's assertion/annotation specifics rest on the overview page and section titles, so JUnit-specific capability wording is kept coarse.
- The "integration" half of the leaf name: no sampled product maintains a separate "integration test runner" market; integration scope appears as the same loop run over larger combinations of units (pytest fixture wiring, Go subtest hierarchy, component environments). Recorded as an observation, not a claim about dedicated integration tooling.
- IDE test-explorer behavior beyond the documented integration lists (e.g., gutter-run UX details) not researched.
- Component-testing drift boundary (how far a runner can go before it becomes an E2E product) is drawn as center-of-gravity, not a bright line; the sibling E2E pass holds the other side.

## Final Synthesis

The Unit / Integration Test Runner is the code-level verification loop of software development. Its defining structure is three jointly-held invariants: test code held in the codebase under test (exercising the project's own units and their direct combinations); the test as an independently executable, assertion-driven verification unit with a pass/fail verdict; and the run itself — discover, select, execute, report per-test verdicts plus an aggregate with a machine-usable outcome signal. Everything else commonly associated with modern runners — watch mode, mocking, coverage, parallelism, snapshots, IDE explorers, reporter ecosystems — is mature common structure or variant machinery, absent in older or toolchain-native generations without loss of Type identity. The Type's neighbors are distinguished by what they hold instead: the Test Automation Platform holds managed test assets, the E2E platform holds the assembled application's journeys, CI holds the pipeline, test management holds the records, the build system holds artifact production. The runner holds the verdict loop for the codebase's own units.
