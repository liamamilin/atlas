# AGENT HANDOFF

## Mission

Walk through `DIRECTORY.md` and produce a researched Application Document for each leaf.

Do not treat the directory as a database schema.

Do not attempt to normalize all Applications into one universal object model.

The invariant is the **research workflow**, not the internal structure of the software.

## Required reading order

1. `DIRECTORY.md`
2. `WORKFLOW.md`
3. `WRITING_GUIDE.md`
4. `examples/AUDIT.md`
5. the paired Golden Examples

## Production unit

For one directory leaf:

```text
<Application Type>
↓
research/<domain>/<slug>.md
↓
applications/<domain>/<slug>.md
```

Research file first.
Application document second.

## Mandatory process

Follow:

```text
Understand
→ Plan
→ Sample
→ Research
→ Model
→ Compare
→ Synthesize
→ Write
→ Review
→ Cite
```

## Adaptive rule

For every Application, create its own research questions.

Examples:

```text
CRM
→ records / relationships / commercial lifecycle

Video Editor
→ media / timeline / editing interaction

Hotel PMS
→ reservation/stay × room state × folio

IAM
→ identity / authentication / authorization / policy
```

Do not copy the Golden Example structure mechanically.

## Research requirement

Use real products.

Default:
- 2–5 representative products
- official docs/help/user guides first
- external walkthroughs only when needed

Do not produce complex operational claims from memory alone.

## Canonicalization behavior

If research suggests the directory leaf is actually:
- duplicate
- alias
- variant
- capability
- overly broad family

record:

```text
## Taxonomy / Boundary Issue
```

inside Research Notes.

Continue producing the best useful document unless the Type is genuinely incoherent.

Do not silently restructure the entire directory.

## Output standard

The final document should let a reader answer:

```text
What is this Application?
Who uses it?
What is its internal product model?
How does it actually work?
What interfaces matter?
What states/rules/behaviors matter?
What nearby Types are different?
What real products demonstrate it?
```

## Golden Examples

Study all four:

- Team Messaging
- CRM
- Restaurant POS
- Hotel PMS

They intentionally model different kinds of software.

## Anti-patterns

Do not produce:

- marketing summaries
- generic “improves efficiency” prose
- flat feature dumps
- one-vendor manuals
- unnecessary implementation architecture
- invented business rules
- identical section content for every Application
