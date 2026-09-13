# Project Scaffolding / Code Generator

## Overview

A **Project Scaffolding / Code Generator** is a developer-facing creation tool that produces the starting point of a new software project: it holds a reusable starting-point definition — a template or generator program encoding a project's initial files, configuration, and boilerplate — collects a few inputs from the user, and emits a concrete, coherent starting codebase that the developer then owns and continues to build with their normal tools.

The defining structure is small:

```text
Reusable starting-point definition (template or generator)
└── Parameterized generation (user inputs shape the output)
    └── Emission of a starting project (files/directories the developer owns)
```

Everything else commonly associated with the category — public template registries, post-generation hooks, sub-generators, web-form workflows, publishing to git hosts, task history and audit — is widespread in mature products but not part of the defining core. The act is fundamentally a **one-time creation of a new project** (or of a new piece added to an existing one), not continuous maintenance, building, or transformation of existing code.

## Users & Context

The primary user is a software developer starting a new project — a service, library, package, frontend app, or infrastructure module — who wants a correct, convention-following starting structure in seconds instead of assembling it by hand.

Typical moments of use:

- starting a brand-new project ("give me a working skeleton with the right tooling wired up")
- adding a new piece to an existing codebase (a new module, component, or package generated from a sub-template)
- an engineering organization standardizing how every new service begins life (same structure, same lint/CI/docs setup, every time)

Secondary users include platform/engineering-productivity teams who author and maintain the organization's templates, and automation (CI scripts) that runs generation non-interactively.

The work environment is the developer's own machine and terminal in most products; enterprise variants add a web surface where developers pick a template from a form-driven catalog.

## Core Model

### The Defining Core

Three properties. If any one is removed, the product is no longer recognizable as this Type:

- **A reusable starting-point definition** — a template or generator that encodes a project's starting structure: source files, configuration, manifests, docs, and tooling wiring. It exists as a first-class artifact held separately from any generated result, so it can be reused across many projects and improved over time. Without it, there is only ad-hoc copying of someone's repository.
- **Parameterized generation** — the user supplies inputs (project name, options, choices) that are resolved into the output; the same definition yields different projects. Without this, it is a static file copy or a sample repo.
- **Emission of a starting project** — the act writes a concrete starting codebase to disk (or, in enterprise variants, creates it in a remote system). The output is source code the developer takes ownership of and continues to develop with their own editor, build tools, and version control. Without this, it is a preview tool or a hosted app builder.

The binding across all three is *software-project creation semantics*: the output is a codebase, not a running hosted application and not a document.

### Capabilities Shared by Mature Products

These make the Type practical; they do not define it:

- **Interactive parameter collection** — prompts, CLI flags, or web forms with sensible defaults; the project name is nearly always the first input.
- **Template distribution** — a channel through which starting-point definitions reach users: a public registry or index, a package manager, a git URL, or an organization-internal catalog.
- **Post-generation steps** — hooks or follow-up actions such as installing dependencies, initializing git, or printing "next steps" instructions.
- **Sub-generators / add-ons** — smaller templates that generate additional pieces into an existing project after the initial creation.
- **Non-interactive mode** — all inputs passable via flags or a config file so generation can run in scripts and CI.
- **Conflict handling** — refusing or warning when the target directory is non-empty or files would be overwritten.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:   Reusable starting-point definition
Realized as:  generator program (executable code decides what to write)
              template directory (files with placeholders + a prompt config)
              fixed built-in template menu
              YAML workflow definition (steps invoking actions)

Concept:   Parameter collection
Realized as:  terminal prompts, CLI flags, web forms with review step

Concept:   Emission
Realized as:  local directory of files
              local directory + publish to a git host + registration in a catalog
```

A reader who has only seen one style (say, a CLI that asks a few questions and prints a project) should still be able to recognize the form-driven enterprise variant from this model.

## How It Works

### The generation loop

```text
Choose a template or generator
→ supply parameters (name, options) — via prompts, flags, or a form
→ the tool resolves the parameters against the starting-point definition
→ files are written: source, config, manifests, docs, tooling wiring
→ optional post-generation steps (install dependencies, git init, print next steps)
→ the developer owns the output and continues building it
```

There is no long-lived object inside the application afterwards: the generated project lives in the developer's own repository and toolchain. The application's persistent state is the starting-point definitions themselves, plus (in some products) records of past runs.

### Authoring a template or generator

A second, equally defining workflow: someone must create the reusable starting-point definition.

```text
Create the template/generator artifact
→ define the parameters users will be asked for (with defaults)
→ mark the variable parts of files and paths
→ optionally add pre/post-generation logic
→ distribute it (registry, package manager, git URL, org catalog)
```

Organizations use this loop to encode their standards: one maintained template means every new service starts with the same structure, linting, CI, and documentation setup.

### Adding to an existing project

Many products support generating a *piece* into an existing codebase — a new module, component, or package — using a sub-template. This is the same core act (definition + parameters + emission) applied at sub-project scale.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- reusable starting-point definition
- parameterized generation
- emission of a starting codebase

**Common mature structure** — present in most modern products:

- interactive parameter collection with defaults
- template distribution channel
- post-generation steps / hooks
- sub-generators for adding pieces later
- non-interactive mode for automation
- conflict handling on non-empty targets

**Variant / optional** — depends on segment and deployment:

- publishing outputs to remote systems (create repo, push, register in a service catalog)
- governed runs: task history, re-run with pre-filled parameters, audit, authorization
- advanced template features (inheritance, choice variables, replay)
- monorepo/workspace generation
- AI-assisted generation (describe the project → generated scaffold)

## Interfaces

### Command-line interface

The dominant surface. The user invokes the tool with a template/generator name; the tool asks questions in the terminal (or accepts flags), streams progress, and reports what was written.

- typical information: template name, parameter prompts with defaults, file-writing progress, next-step instructions
- primary actions: run a generation, pass flags for non-interactive use, list available templates/generators

### Template/generator listing

A discoverable catalog of available starting points — a public registry page, a package-manager search, or an in-product list.

- typical information: name, description, maintainer, ecosystem
- primary actions: browse, search, select for use

### Web form / wizard (enterprise variant)

A multi-step form surface: pick a template, fill per-step inputs, review a summary, run.

- typical information: template description, grouped input fields, review page, run progress with per-step status
- primary actions: choose template, fill inputs, review, run, view results or per-step failure logs, re-run

### Authoring surface

Where maintainers define templates/generators: a project layout with a prompt/parameter configuration, template files with placeholders, and optional hook scripts. Usually authored as ordinary code in a repository.

## Important Rules / Behaviors

### The output leaves the application

The generated project is not managed inside the tool afterwards. Once emitted, it belongs to the developer's repository and evolves through normal development. This is the structural contrast with hosted app builders, where the application remains the runtime home of what was created.

### One-time creation, not continuous transformation

The defining act creates a new project (or a new piece). Products do not treat substantial existing code as their object of record; tools that rewrite or migrate existing codebases belong to a different Type.

### Parameters shape the output deterministically

Given the same template and the same inputs, the output is reproducible. This determinism — a versioned starting-point definition applied to explicit inputs — is what separates the Type from open-ended conversational code generation.

### Conflicts are guarded

Generation into a non-empty directory or over existing files is typically refused or explicitly warned about, protecting the developer's existing work.

### The template is the standard

In organizations, the maintained template functions as an enforceable starting convention: what every new project contains is decided by the template's author, not by each developer.

## Variants

- **Ecosystem official scaffolders** — a framework or language ships its own scaffolder with a fixed menu of opinionated presets; minimal prompts; the result runs immediately (the "create-X" pattern).
- **Generator-program ecosystems** — generators are small programs in a shared runtime, discoverable through a public registry; composable and extensible (JS-ecosystem style).
- **Template-file engines** — templates are plain directory trees with placeholders plus a declarative prompt configuration; language-agnostic and usable directly from git URLs or archives.
- **Enterprise / platform scaffolding** — web-form-driven, org-authored templates; generation publishes to a git host and registers the result in a software catalog; runs are tracked tasks with history, re-run, audit, and authorization.
- **Monorepo/workspace generators** — generate multi-package workspaces and new packages inside them.
- **AI-assisted scaffolding** — an emerging variant where the starting point is produced from a natural-language description, layered over the same template/generation machinery.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Low-code / No-code Application Builder | also "creates applications", but the result is a running app hosted inside the platform; a scaffolder emits a source codebase the developer owns |
| AI Coding Agent | can generate project files conversationally, but has no reusable, versioned starting-point definition applied deterministically; scaffolding is template-driven |
| Internal Developer Portal | portals embed scaffolding as one self-service action; the portal's core is the software catalog and self-service surface, not the generation machinery |
| Developer Environment Manager | assembles and activates the per-project tooling environment continuously; scaffolding creates the project once |
| Build Automation / CI | operates repeatedly on existing code; scaffolding creates the code that build tools later consume |
| Code Migration / Modernization Platform | transforms an existing codebase; scaffolding creates a new one |
| Dependency Management Application | manages a project's library dependencies over time; scaffolding only wires the initial dependency setup |

The most important boundary is with hosted application builders: both promise "an application in minutes". The decisive test is the output — a codebase the developer takes away, versus an application that lives inside the platform.

## Representative Products

- Yeoman — generator-program ecosystem with a public registry
- Cookiecutter — language-agnostic template-file engine usable directly from git/zip sources
- create-vite (and the create-react-app / create-next-app lineage) — official framework scaffolders
- Backstage Software Templates (Scaffolder) — enterprise, form-driven scaffolding with publish-to-git and catalog registration

## Sources

Research date: **2026-09-10**

- Yeoman — Writing Your Own Yeoman Generator: https://yeoman.io/authoring/
- Vite — Getting Started (Scaffolding Your First Vite Project): https://vite.dev/guide/
- Cookiecutter — documentation index and Overview: https://cookiecutter.readthedocs.io/en/stable/ , https://cookiecutter.readthedocs.io/en/stable/overview.html
- Backstage — Software Templates overview: https://backstage.io/docs/features/software-templates/

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
