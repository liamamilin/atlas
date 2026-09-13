# Golden Examples Audit — v1 → v2

## Overall conclusion

The four original Golden Examples are **conceptually useful but not yet ideal teaching examples** for the newly frozen `WORKFLOW.md` and `WRITING_GUIDE.md`.

They should not be discarded. Their research and canonicalization logic is largely sound.

The main issue is structural:

> They were written before the project decided that workflow should be fixed but document structure should remain adaptive.

The v1 examples therefore still look too much like one universal schema.

---

# Cross-example findings

## 1. Core Model was underdeveloped

v1 mostly used:

```text
Core Objects table
```

This is useful, but insufficient.

The new standard requires:

> explain the internal world of the Application and the relationships among its concepts.

v2 therefore adds explicit relational models such as:

```text
Account / Company
├── Contacts
├── Activities
└── Deals
      ↓
   Pipeline
```

and:

```text
Reservation
↔ Guest
↔ Room Assignment
↔ Stay
↔ Folio

Room
↔ Room Operational State
```

---

## 2. Too many fixed chapters

v1 used the same numbered structure:

```text
Overview
Users
Core Objects
Capabilities
IA
Pages
Flows
States
Rules
Permissions
Exceptions
...
```

for every application.

That conflicts with the new principle:

> fixed workflow, adaptive document structure.

v2 uses the common skeleton:

```text
Overview
Users & Context
Core Model
How It Works
Interfaces
Important Rules / Behaviors
Variants
Related Application Types
Representative Products
Sources
```

but expands each section differently according to the Application.

---

## 3. Capabilities were too prominent

The v1 documents were not feature dumps, but the dedicated `Capabilities` section still encouraged feature-list thinking.

v2 keeps Core/Common/Optional distinctions where useful, but places them inside the explanation of the Application model and operation.

The center of gravity becomes:

```text
structure
+
workflow
+
state
+
behavior
```

not feature inventory.

---

## 4. Sources were not sufficiently visible in final documents

v1 ended with statements such as:

> Derived from official Salesforce Trailhead...

This is not enough for a Golden Example.

v2 final documents include actual source references and research date.

Detailed evidence remains in Research Notes.

---

## 5. Research Notes were too compressed

The v1 research notes correctly included representative products and evidence matrices, but several did not explicitly contain:

- adaptive research questions
- source URLs
- uncertainty
- rejected/product-specific findings
- final boundary review

v2 adds those sections.

---

# Example-specific review

## Team Messaging

### Strong in v1
- clear boundary from consumer IM / project management / video conferencing
- strong workspace/channel/message model
- vendor-specific Slack extensions correctly rejected

### Improve
- distinguish channel membership/access from channel lifecycle
- make persistent shared-context model explicit
- final sources need URLs

### v2 focus
`Organizational container → conversation spaces → messages → contextual replies/history → membership/access`

---

## CRM

### Strong in v1
- good Lead / Contact / Account / Deal abstraction
- correct warning that Leads are not mandatory in every CRM
- Salesforce suite pollution was controlled

### Improve
- CRM is fundamentally a **relationship graph plus commercial workflow**, not merely a list of record types
- ownership and activity history should be integrated into model
- clarify that sales-oriented CRM is the canonical focus of this example

### v2 focus
`People + Organizations + Relationship History + Potential Business + Ownership + Pipeline`

---

## Restaurant POS

### Strong in v1
- strong distinction from Retail POS and Restaurant Management
- order/check/payment lifecycle well identified
- restaurant-specific modifiers/table/seat/course context correctly surfaced

### Improve
- show that `Order`, `Check`, and `Payment` are related but not always identical objects
- table-service and quick-service should be treated as two operational loops over the same transaction core
- separate restaurant transaction core from adjacent fulfillment modules

### v2 focus
`Menu configuration → Order construction → Service context → Check → Payment → Closure`

---

## Hotel PMS

### Strongest v1 example
The key insight was excellent:

> PMS contains interacting reservation/stay state and room operational state.

This is exactly the kind of model Application Atlas should extract.

### Improve
- make cross-object state dependency the center of the document, not a later subsection
- distinguish Reservation from Stay more carefully
- make front-desk, housekeeping and folio three coupled operational views of the same stay

### v2 focus
`Reservation/Stay lifecycle × Room resource state × Guest account/folio`

---

# Decision

All four examples remain Golden Examples after revision.

They now teach two things:

1. **how to research**
2. **how different Application Types produce different final structures**

They should be used as methodological references, not templates to copy mechanically.
