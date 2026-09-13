# Research Notes — Project Scaffolding / Code Generator

## Research Goal

Understand what a Project Scaffolding / Code Generator application actually is as a Type: what objects exist inside it, what the user does, how generation works, and where its boundary lies against adjacent developer-tool Types (low-code builders, AI coding agents, internal developer portals, developer environment managers, build automation, code migration tools).

## Initial Boundary

Working hypothesis: this Type creates the *starting point* of a software project — a directory of files, configuration, and boilerplate — from a reusable template or generator program, driven by user-supplied parameters. It is a one-time (or per-new-project) creation act, not continuous maintenance of environments, not building/running code, not transforming existing code.

Nearest neighbors to check:
- Low-code / No-code Application Builder — also "creates applications", but the output is a running/configured app inside the platform, not a source codebase the developer owns.
- AI Coding Agent — can also generate project files, but interaction is conversational/open-ended, not template-driven.
- Internal Developer Portal — scaffolding appears as a capability inside portals (Backstage Scaffolder); is the portal a separate Type with scaffolding embedded?
- Developer Environment Manager — per-project environments vs one-time project creation.
- Build Automation — operates on existing code; scaffolding creates the code that build tools later operate on.
- Code Migration / Modernization — transforms existing codebases; scaffolding creates new ones.

## Research Questions

1. What is the unit of record — the template? the generator program? the generated project?
2. How does the user interact — CLI prompts, flags, web forms?
3. What does generation actually produce — files only, or also remote resources (repos, CI, catalog entries)?
4. Is there a lifecycle after generation (regeneration, updates to generated code)?
5. Where do templates/generators come from — bundled, community registries, org-authored?
6. What rules/constraints matter (naming, conflicts with existing files, dry-run, idempotency)?
7. Where is the boundary against low-code builders, AI agents, and portals?

## Representative Products

Selected for market representativeness, documentation quality, and different product philosophies:

1. **Yeoman** — ecosystem/generator-program philosophy; JS ecosystem; generators as Node modules with a run-loop; community registry.
2. **Cookiecutter** — template-file philosophy; language-agnostic (Jinja2 templates + JSON config); works directly from git repos/zip files.
3. **create-vite** (official scaffolder pattern: create-react-app / create-next-app / create-vite lineage) — official-tool philosophy; fixed template menu, minimal prompts, instant runnable project.
4. **Backstage Software Templates (Scaffolder)** — enterprise/IDP philosophy; web-form-driven, multi-step workflow, publishes to GitHub/GitLab, registers components in a catalog, task history and audit.

## Sources

Research date: 2026-09-10

- Yeoman — Writing Your Own Yeoman Generator: https://yeoman.io/authoring/ (fetched 2026-09-10)
- Vite — Getting Started (create-vite scaffolding section): https://vite.dev/guide/ (fetched 2026-09-10)
- Cookiecutter — docs index + Overview (input/output): https://cookiecutter.readthedocs.io/en/stable/ , https://cookiecutter.readthedocs.io/en/stable/overview.html (fetched 2026-09-10)
- Backstage — Software Templates overview: https://backstage.io/docs/features/software-templates/ (fetched 2026-09-10)

## Product A — Yeoman

### Key observations (Evidence layer A unless noted)

- Generators are the building blocks; they are plugins run by `yo` to generate files for end users. (A)
- A generator is a Node.js module, named `generator-name`; Yeoman discovers generators via the filesystem/npm. (A)
- Structure: a default `app` generator (`yo name`) plus sub-generators (`yo name:subcommand`) for adding pieces to an existing project. (A)
- Generators extend a base class; prototype methods run in sequence; a run-loop organizes initialization/prompting/writing phases. (A)
- User interaction: options/flags (`--babel`) and prompts; user answers are stored in a config file (`.yo-rc.json`), which also marks the project root. (A)
- Composability: generators can compose with other generators (documented "Composability" section). (A)
- Ecosystem: a public generators page indexes generators by keyword/description. (A)
- B-layer: the generator-as-program model (code decides what to write) vs Cookiecutter's template-as-files model — two real philosophies of the same Type.

## Product B — Cookiecutter

### Key observations

- "Cookiecutter creates projects from cookiecutters (project templates), e.g. Python package projects from Python package templates." (A)
- Input: a directory structure containing template files (paths and contents may contain Jinja2 placeholders, e.g. `{{ cookiecutter.project_name }}/`) plus a `cookiecutter.json` holding prompts and default values. (A)
- Flow: reads the settings file, prompts the user interactively to change settings, then generates an output directory structure. (A)
- Templates can come from the filesystem, a ZIP file, or a VCS server (Git/Hg); works with private repos. (A)
- Optional pre-generation and post-generation hooks (Python or shell scripts) run before/after generation. (A)
- Advanced structure: choice/boolean/dict variables, template inheritance, replay of a previous generation, user config (`~/.cookiecutterrc`), copy-without-render. (A)
- B-layer: template-as-files with a declarative prompt config is the dominant alternative philosophy; the generated output is a plain directory the user owns.

## Product C — create-vite (official scaffolder pattern)

### Key observations

- Vite's docs have a dedicated "Scaffolding Your First Vite Project" section: `npm create vite@latest`, "Then follow the prompts!" (A)
- Templates are a fixed menu of framework presets (vanilla, vue, react, preact, lit, svelte, solid, qwik — each with a TS variant). (A)
- Non-interactive mode: project name and template can be passed as CLI options (`--template vue`); `.` scaffolds into the current directory; `--no-interactive` flag exists. (A)
- Output is a runnable project: scaffolded `package.json` with dev/build/preview scripts; user then `npm install` and runs. (A)
- Community templates exist; the docs also point to tools like tiged for scaffolding from arbitrary GitHub repos. (A)
- B-layer: the "create-X" official scaffolder is now the standard onboarding surface for frameworks (create-react-app, create-next-app, create-vite, cargo new, npm init, etc.); minimal prompts, opinionated defaults, zero-config runnable result.

## Product D — Backstage Software Templates (Scaffolder)

### Key observations

- "The Software Templates part of Backstage is a tool that can help you create Components inside Backstage. By default, it has the ability to load skeletons of code, template in some variables, and then publish the template to some locations like GitHub or GitLab." (A)
- Templates live under `/create`; user picks a template, fills per-step input variables (e.g. GitHub repo info), reviews a summary, then runs. (A)
- A template run is a task with a unique ID; there is a Task List of previous executions; failed runs expose per-step logs; runs can be cancelled; "Start Over" re-runs with pre-filled editable parameters. (A)
- Templates are defined as YAML with steps invoking actions (fetch skeleton, template variables, publish, register); custom actions and custom field extensions are supported; dry-run testing exists. (A)
- Output goes beyond local files: publish to a git host and register the result as a Component in the Software Catalog. (A)
- Authorization of scaffolder tasks/parameters/steps/actions and audit events are documented features. (A)
- B-layer: in the enterprise variant, generation is a governed workflow (form → review → run → publish → register), and scaffolding is one capability inside a portal/platform — but the scaffolder itself is a separable machinery.

## Cross-product Comparison

| Dimension | Yeoman | Cookiecutter | create-vite | Backstage Scaffolder |
|---|---|---|---|---|
| Unit of record | generator program (Node module) | template directory + JSON config | fixed built-in template set | YAML template definition + actions |
| Interaction | CLI prompts + flags | interactive prompts from JSON | CLI prompts or flags | web form, multi-step, review page |
| Template source | npm/registry, filesystem | git/hg/zip/local | bundled presets + community repos | imported into the Backstage instance (org-authored) |
| Output | files in project dir (+ config file) | local output directory | runnable project dir | files + publish to git host + catalog registration |
| Post-generation | sub-generators add pieces later | pre/post hooks (scripts) | none (hand off to package manager) | register component; task history/audit |
| Re-run/update | re-run generators; config persisted | replay feature | one-shot | task re-run ("Start Over") |
| Governance | none | user config only | none | authorization, audit events |
| Audience | JS ecosystem developers | polyglot developers | framework users | enterprise engineering orgs |

### Stable commonalities (B-layer)

1. A reusable starting-point definition exists as a first-class artifact (template or generator program) that is separate from any single generated project.
2. The user supplies parameters (project name, options) that shape the output; collection is interactive prompts and/or flags/forms.
3. Generation produces a concrete starting project — a directory of files (code, config, docs, tooling) — that the developer then owns and continues to develop.
4. The act is creation of a NEW project (or addition of a new piece to an existing one), not modification of substantial existing code.
5. Templates/generators are distributable and reusable across many projects and users.

### Differences (implementation/variant, not identity)

- Program vs template: generator code (Yeoman) vs declarative template files + prompt config (Cookiecutter) vs fixed presets (create-vite) vs YAML workflow (Backstage).
- Surface: CLI vs web form.
- Output scope: local files only vs publish-to-remote + registration.
- Ecosystem: public registry vs org-internal library.
- Lifecycle: one-shot vs re-runnable tasks with history.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **A reusable starting-point definition** — a template or generator that encodes a project's starting structure (files, configuration, boilerplate), held separately from any single generated result. Remove → ad-hoc copy-paste of someone's repo, not a generator application.
2. **Parameterized generation** — the user supplies inputs (name, options) that are resolved into the output; the same template yields different projects. Remove → static file copy / `git clone` of a sample.
3. **Emission of a starting project** — the act writes a concrete, coherent starting codebase (files/directories) that the developer takes ownership of and continues to build. Remove → a preview/lint/report tool, or a hosted app builder.

All three are jointly held: 1 alone = a repo of example files; 2 alone = a config form; 3 without 1+2 = a one-off script. The binding is *software-project creation semantics*: the output is source code a developer will continue to work on with their own tools.

### L1 — Common Mature Structure

- Interactive parameter collection (prompts, flags, or forms) with defaults
- Template/generator distribution (registry, package manager, git URL, org catalog)
- Post-generation hooks / follow-up steps (install dependencies, git init, print next steps)
- Sub-generators / add-ons that generate additional pieces into an existing project
- Non-interactive mode (flags / config file) for automation and CI
- Conflict handling: refuse or warn when target directory is non-empty / files exist

### L2 — Variant / Optional Structure

- Publishing outputs to remote systems (create repo, push, register in a catalog) — enterprise/IDP variant
- Task history, re-run, audit, authorization — governed enterprise variant
- Template inheritance, choice variables, replay — advanced template-engine features
- Monorepo/workspace generators generating multiple packages at once
- AI-assisted generation (describe what you want → generated scaffold) — emerging variant
- Language/ecosystem specialization (frontend frameworks, Python packages, Terraform modules, etc.)

### L3 — Vendor-specific (Research Notes only)

- Yeoman's `.yo-rc.json` project-root marker and run-loop phase names
- Cookiecutter's `~/.cookiecutterrc`, `_copy_without_render`, Jinja environment customization
- create-vite's specific template list and `--no-interactive` flag
- Backstage's camelCase action-ID constraint, dry-run testing, `scaffolder.registerComponent` route binding

## Vendor-specific Findings

- Yeoman: filesystem-based generator discovery; `generator-` naming prefix required for registry indexing.
- Cookiecutter: works directly against git/hg URLs and zip files without a registry.
- create-vite: `.` to scaffold into current directory; StackBlitz online variants (`vite.new/{template}`).
- Backstage: each template execution is a uniquely identified task; per-step failure logs; cancel sends an abort signal; "Start Over" pre-fills previous parameters.

## Boundary Findings

- **vs Low-code / No-code Application Builder**: both "create applications". Decisive test: the output. A scaffolder emits a source codebase the developer owns and continues in their own toolchain; a low-code builder hosts and runs the app inside the platform. Remove the codebase-emission and host the result → low-code builder territory.
- **vs AI Coding Agent**: an agent can produce a scaffold conversationally, but the defining structure here is a *reusable, versioned starting-point definition* applied deterministically; the agent has no such reusable unit and is open-ended. Remove the reusable template and drive by conversation → AI coding agent.
- **vs Internal Developer Portal**: portals embed a scaffolder as one self-service action (Backstage itself is the proof). The portal's core is the catalog + self-service surface; scaffolding is a capability. Remove the catalog/portal surface and keep template→generate→publish → this Type.
- **vs Developer Environment Manager**: environment managers assemble and activate the *tooling around* a project continuously (per-project runtimes); scaffolders create the project once. Remove the reusable template and generate-once act, keep environment assembly → environment manager.
- **vs Build Automation / CI**: build tools operate on existing code repeatedly; scaffolding is a one-time creation of the code that build tools later consume.
- **vs Code Migration / Modernization Platform**: migration transforms an existing codebase; scaffolding creates a new one. Both may share template/rewrite machinery, but the object of record differs (existing system vs new starting point).
- **Removal test**: remove the reusable starting-point definition → one-off code generation (scripting, not a Type-defining product category); remove parameterization → static template repo; remove codebase emission → form builder or preview tool.

## Uncertainties

- Precise registry sizes / generator counts not verified (avoided).
- Whether "code generator" in the directory name also intends *continuous* code generation (e.g. OpenAPI codegen, protobuf codegen). Evidence sampled leans to project-creation; API-client generators from specs are a plausible adjacent variant but were not deeply researched — recorded as an open question rather than asserted.
- AI-era scaffolding products evolve quickly; treated as emerging variant only.

## Final Synthesis

A Project Scaffolding / Code Generator application is a developer-facing creation tool whose defining core is: a reusable starting-point definition (template or generator program), parameterized by user input, that emits a concrete starting codebase the developer owns and continues to build. Mature products add interactive parameter collection with defaults, template distribution channels, post-generation steps, sub-generators, non-interactive modes, and conflict handling. Enterprise variants extend the output beyond local files to repo creation, catalog registration, governed task runs, and audit. The Type is defined by creation-of-new-project semantics, not by any particular template format, surface (CLI vs web), or ecosystem.
