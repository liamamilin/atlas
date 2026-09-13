# Application Atlas — Production Pack

This is the simplified production package.

The project has now moved beyond taxonomy design.

## What matters now

```text
DIRECTORY
+
WORKFLOW
+
WRITING GUIDE
+
GOLDEN EXAMPLES
=
APPLICATION DOCUMENT PRODUCTION
```

## Files

### Core

- `DIRECTORY.md` — production navigation tree
- `WORKFLOW.md` — how the Agent researches an Application
- `WRITING_GUIDE.md` — how the final document should be written
- `AGENT_HANDOFF.md` — execution instructions

### Examples

```text
examples/
├── AUDIT.md
├── research-notes/
│   ├── team-messaging.md
│   ├── crm.md
│   ├── restaurant-pos.md
│   └── hotel-pms.md
└── application-docs/
    ├── team-messaging.md
    ├── crm.md
    ├── restaurant-pos.md
    └── hotel-pms.md
```

### Production output

```text
research/
applications/
```

## Simplified philosophy

The Atlas is primarily a **directory of Application Types plus a library of researched documents**.

Structured registries, graph databases, YAML schemas and advanced search infrastructure may be added later if the document corpus creates a real need.

They are not prerequisites for production.

## Core rule

> Workflow is standardized. The internal model of each Application is not.

## Production loop

```text
Take next leaf from DIRECTORY.md
→ Research using WORKFLOW.md
→ Write using WRITING_GUIDE.md
→ Compare against Golden Examples
→ Save Research Notes
→ Save Application Document
→ Continue
```
