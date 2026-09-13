# Method Patch v1.1

Trigger:
First real production draft — `Instant Messaging Application`.

## Problem 1 — Modern implementation overfitted into Canonical definition

Observed pattern:

```text
phone number
+ address book
```

was promoted too aggressively into the definition of Instant Messaging.

Patch:

> Canonical Core must first identify the minimum stable invariant.
> Common current implementations belong one level below the definition.

New abstraction hierarchy:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

## Problem 2 — Assertion strength exceeded evidence strength

The draft transparently reported source-access limitations, but still contained several precise cross-product claims.

Patch:

> Evidence depth determines assertion depth.

New evidence layers:

```text
Direct Product Observation
→ Cross-product Commonality
→ Canonical Inference
```

Precise facts cannot be generalized without matching evidence.

## Problem 3 — Final document retained too much product detail

Patch:

```text
Must understand
→ final document

Helpful to understand
→ final document if useful

Product detail
→ Research Notes
```

## Result

Updated:

- `WORKFLOW_v1.1.md`
- `WRITING_GUIDE_v1.1.md`

Next validation step:

> Re-run / rewrite `Instant Messaging Application` under v1.1 and compare whether the Canonical Core becomes smaller, evidence discipline improves, and the final document becomes shorter without losing explanatory power.
