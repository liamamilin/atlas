# Due Diligence Platform

## Overview

A **Due Diligence Platform** is the deal team's workbench for running a structured inquiry into a subject — a target company, asset, investment, or counterparty — ahead of a transaction decision. It organizes the diligence exercise into workstreams, manages the information request list as the unit of work, tracks every request from issue through response and review to closure, and accumulates the findings that feed the deal decision: the diligence report, the investment-committee memo, the closing conditions, the price adjustments.

The defining structure is small:

```text
Diligence exercise (bounded inquiry into a subject)
└── Workstreams / categories
    └── Information request list (the unit of work)
        └── Request → response → review (tracked lifecycle)
            └── Findings / issues accumulated
                └── Diligence output feeding the decision
```

Everything else commonly associated with these products — a built-in virtual data room, AI document analysis, dashboards, playbooks — is widespread in current products but is not what makes the product a due diligence platform. The document repository is a separable companion: some products host it, some link to an external room, some sync with it, and some work without one at all.

When the center of gravity shifts to hosting and controlling access to the document corpus itself, the product is a Virtual Data Room. When it shifts to the standing portfolio of third-party relationships, it is Third-party Risk Management. When it shifts to the deal pipeline and counterparty history, it is Deal Management.

## Users & Context

The primary users are the **inquiring side** of a transaction:

- **Corporate development / M&A deal teams** — run diligence on acquisition targets, coordinate internal workstreams, report to leadership
- **Private equity deal teams** — run buy-side diligence on investment targets, produce IC memos
- **M&A advisors, investment bankers, law firms, accountants** — run diligence workstreams on behalf of clients, manage request lists, draft reports

The **responding side** also works in the platform: sellers and their advisors respond to requests, upload documents, and answer questions — typically under restricted access that shows them only what they are meant to see.

Typical context: an M&A or investment transaction with a defined diligence window, multiple parallel workstreams (legal, financial, commercial, HR, IT, tax, regulatory, environmental), tight deadlines, and a decision at the end. The same machinery appears in adjacent bounded inquiries — real estate transactions, fundraising processes, and vendor-risk assessments run "like M&A diligence" — but the transaction-decision context is the center.

## Core Model

### The Defining Core

```text
Diligence exercise (bounded inquiry into a subject)
└── Workstreams / categories
    └── Information request list (the unit of work)
        └── Request → response → review (tracked lifecycle)
            └── Findings / issues accumulated
                └── Diligence output feeding the decision
```

Four structures. If any one is removed, the product is no longer recognizable as a due diligence platform:

- **The diligence exercise of record** — a bounded, identified inquiry into a specific subject, run by an inquiring party toward a decision. It has an owner team, a scope, and a place in a transaction. Without it, the product is generic project management.
- **The information request list as the unit of work** — structured items, each asking the subject or responding party for a document or an answer: "produce the last three years of financial statements", "explain this contract clause". Items are categorized by workstream, prioritized, assigned to owners, and tracked to completion. Without it, the product is a document repository or a static checklist nobody works.
- **The tracked request → response → review loop** — each request carries a lifecycle status; the response (a document, an answer, or both) is bound to the specific request it satisfies; the requesting and responding parties exchange through the platform; gaps and partial responses remain visible until resolved. Without it, the product is one-way file sharing.
- **Findings and issues accumulated against the exercise** — the risks, red flags, and open questions surfaced during review, logged with severity and an owner, linked back to the request or document that raised them, and carried into the diligence output. Without it, the product is a request tracker with no assessment behind it.

These four are jointly load-bearing. A request list without an exercise is a spreadsheet; a response loop without a request list is file sharing; findings without the inquiry machinery are an issues list nobody can trace.

### The Document Repository Is a Companion, Not the Core

The relationship to the data room varies by product, and this variation is the clearest evidence that the repository is not the defining structure:

- some products include a built-in virtual data room as one capability among several
- some products link each request to documents in a separate, external data room — the room stays authoritative, and the tracker is described as "two views of one state" with the room
- some products synchronize bidirectionally with external data rooms
- some products require no data room at all — documents are uploaded directly, or imported from a room export

In every case the workflow survives: what defines the Type is the inquiry loop, not where the documents live.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They make the workflow practical; they do not define the Type.

- **Q&A threading** — questions raised against specific requests, answered in threads, with a consolidated view of all open queries across the exercise
- **Templates and playbooks** — reusable request-list and folder structures per deal type; import of existing lists from spreadsheets or documents
- **Progress dashboards and status reporting** — completion rates, bottlenecks, exportable status updates for stakeholders
- **Granular permissions and party access** — buyers, sellers, advisors, and counterparties see only what they are meant to see; sensitive items can be restricted even within one team
- **Audit trail** — document access, task changes, and approvals timestamped, so the process is defensible after the fact
- **Reviewer assignment and notifications** — each request can carry a reviewer distinct from its owner; reminders chase outstanding items
- **Closing checklists built from live diligence state** — rather than rebuilt by hand at the end
- **AI assistance** — document classification, automatic matching of uploaded documents to open requests, key-term extraction, red-flag ranking, summary and memo drafting

## How It Works

### Set up the exercise

```text
Create the diligence exercise (bound to the deal/subject)
→ define workstreams (legal, financial, commercial, HR, IT, …)
→ build the request list: from a template/playbook, or by importing
   an existing list from a spreadsheet or document
→ assign owners and priorities
→ invite the responding party (seller / target / counterparty) with
   restricted access
```

### Run the request loop

```text
Issue requests to the responding party
→ responding party attaches documents and/or answers to each request
   (uploaded directly, or linked from the data room)
→ requesting side reviews each response
→ follow-up questions asked and answered in the request's thread
→ request moves through its lifecycle:
   open → responded → reviewed → closed
   with flagged items held open for resolution
→ gaps and partial responses stay visible until resolved
```

The request is the persistent unit: every document produced, every answer given, and every question asked stays attached to the request it belongs to, so the state of the inquiry is always answerable from the list.

### Accumulate findings

```text
Review surfaces an issue (a litigation matter, a customer-concentration
concern, a contract gap)
→ log it as a finding/issue: description, severity, owner,
   linked to the request or document that raised it
→ track resolution or acceptance
→ findings roll up into the diligence output
```

The findings register is built from the diligence process itself rather than maintained as a separate document — each flagged item traces back to the request that surfaced it.

### Produce the output and close

```text
Compile the diligence output: report, IC memo, risk summary
→ findings feed closing conditions and price adjustments
→ closing checklists draw on live diligence state
→ the exercise closes with a complete, auditable record
```

### Core vs Common vs Optional

**Defining core** — without these, not a due diligence platform:

- diligence exercise of record bound to a subject
- information request list as the unit of work
- tracked request → response → review loop with responses bound to requests
- findings/issues accumulated and feeding the diligence output

**Common mature structure** — present in most modern products:

- Q&A threading, templates/playbooks, list import
- dashboards, permissions, audit trail, reviewer assignment, notifications
- data-room integration in some posture
- closing checklists from live state
- AI assistance

**Variant / optional** — depends on product philosophy, packaging, and context:

- built-in data room vs external room (linked, synced, or absent)
- standalone workbench vs module of a wider M&A suite
- buy-side vs sell-side operation
- AI depth (matching → analysis → memo drafting)
- non-M&A subject contexts (real estate, fundraising, vendor assessments)

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Request list / tracker

The primary working surface — the structured queue of the whole exercise.

- every request with its number, workstream/category, description, status, owner, due date
- progress at a glance (e.g. "14 / 22 complete"), filterable by category, priority, assignee
- primary actions: create/import requests, assign owners and reviewers, set priorities and due dates, update status, flag items

### Request detail

The unit-of-work surface for one request.

- the request text, its status history, the response (documents and/or answer), the Q&A thread, linked findings
- primary actions: attach/link documents, answer, comment, re-assign, change status, flag as risk

### Document / data room view

The corpus surface — hosted in-product, or an index of an external room.

- folder structure, document metadata, access controls, activity logs
- primary actions: upload, organize, link a document to a request, control access

### Findings / issues register

The assessment surface of the exercise.

- each finding with description, severity, owner, source link, resolution state
- primary actions: log a finding, assign an owner, set target resolution, link evidence, close or escalate

### Dashboards and reporting

The oversight surface for deal leadership and stakeholders.

- completion and coverage across workstreams, bottlenecks, aging open items
- primary actions: filter, export status updates, generate the diligence report

### Administration / permissions

- party and role configuration, access grants per workstream or document, audit trail review

## Important Rules / Behaviors

### The request is the unit of accountability

Every request carries a status, an owner, and (commonly) a due date. The status model is conceptual — open, responded, reviewed, closed, flagged — but the exact labels vary by product. What is structural is that the state of the whole inquiry is readable from the list, without status calls.

### Responses bind to their requests

A document or answer satisfies a specific request, not a folder. Resolving requests by pointing at documents — rather than emailing attachments — keeps the repository authoritative and leaves a record of exactly what was produced to whom. This binding is what makes the exercise auditable.

### Findings trace back to their source

Each finding links to the request or document that raised it. The traceability is the point: a flagged item that later becomes a closing condition or a price adjustment must be defensible back to its source.

### Cross-party visibility is governed

The requesting and responding sides see different things. Sellers commonly see only their own queue; sensitive findings may be invisible to the responding party; within the buying side, workstream teams may be walled from each other. Permissions are a structural surface, not an afterthought.

### The exercise is bounded and leaves a record

A diligence exercise has a beginning (setup, request list) and an end (report, close). The complete record — requests, responses, Q&A, findings, access logs — persists after closing and is commonly exportable as a package.

### Findings carry forward

In mature products the findings register is not discarded at close: it feeds closing conditions, price adjustments, and — where the product is part of a wider M&A platform — post-close integration planning.

## Variants

- **Standalone diligence workbench** — the diligence exercise is the whole product; documents come from uploads or external rooms
- **Module of an M&A lifecycle suite** — diligence sits beside pipeline (deal sourcing) and integration (post-close execution) modules in one platform; findings flow into integration planning
- **Data-room-first product with embedded workflow** — a virtual data room whose request lists, Q&A, and task management live inside the room; the room is the starting point
- **Workflow module of a transaction platform** — a thin tracker that links to a separate data room index rather than hosting documents
- **Buy-side vs sell-side operation** — the same machinery serves sellers preparing for exit (vendor due diligence reports, readiness assessments, objection registers) and buyers investigating targets
- **Subject extensions** — real estate transactions, fundraising processes, and vendor-risk assessments run with the same request-list machinery against different subjects
- **AI-era depth** — from simple tracking, through automatic document-to-request matching, to cross-document analysis and drafted reports with authorship attribution

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Virtual Data Room | closest sibling; market bundles both | VDR is the disclosure repository of record (document corpus, party access, disclosure record); this Type is the inquiry workflow of record (requests, responses, review, findings). A traditional VDR stores files but tracks nothing else; a diligence platform can run without hosting any room |
| Deal Management for Private Equity / VC | upstream sibling | that Type is the firm's deal-flow CRM (pipeline stages, counterparties, deal history) where "due diligence" is a pipeline stage; this Type is the execution workbench for the diligence exercise itself |
| Third-party Risk Management | adjacent; convergence zone real | TPRM is the standing relationship program (inventory, evaluation, governed decisions across the relationship lifecycle); this Type is a bounded exercise toward a transaction decision. Vendor assessments can be run with this machinery, but the standing program remains TPRM's center |
| KYC / KYB Platform | same word, different object | customer-onboarding compliance program (accumulated due-diligence case file, regulator-facing record) vs transaction-decision inquiry |
| Transaction Legal Management | broader host | whole-deal execution is the center there; diligence is one workstream inside it |
| Investment Research Platform | different information world | public-domain issuer material vs deal-confidential document sets; research interrogation vs inquiry workflow |
| eDiscovery Platform | same word family, different object | evidentiary review with legal hold and production machinery vs deal inquiry |
| Corporate Investigation Management | different subject | internal wrongdoing cases vs transaction subjects |
| Environmental Site Assessment | closest assessment sibling | a bounded engagement with evidence and a report, but scoped to a property's environmental condition under practice standards, not a multi-workstream transaction inquiry |
| Contract Analytics Platform | analysis vs process | contract legibility machinery over documents vs the request/response workflow of the deal |

The boundary with the Virtual Data Room is the most important one, because the market deliberately straddles it: several products bundle a data room and the diligence workflow in one platform, and some data rooms embed request lists. The structural test is the center of gravity — repository of record vs workflow of record.

## Representative Products

- **DealRoom** — M&A platform whose diligence module centers requests, files, findings, and collaboration; explicitly positions itself beyond traditional data rooms
- **Midaxo** — enterprise M&A platform whose diligence phase combines request lists, document review, Q&A, and a risk/issue register that carries into integration
- **InvestmentBank.com Diligence Tracker** — a thin workflow module managing the full request cycle against a separate data room index
- **Dillien** — a next-generation data room with the diligence workflow (request lists, Q&A, tasks, report generator) embedded in the room
- **DD Navigator** — an AI-native diligence workbench producing cited findings and IC-memo first drafts, working with or without a data room

The core model was checked across standalone workbenches, lifecycle suites, data-room-first products, and thin workflow modules to avoid over-fitting to any one packaging pattern.

## Sources

Research date: **2026-09-10**

- DealRoom — M&A Diligence Management Software — https://dealroom.net/product/diligence
- Midaxo — M&A Due Diligence Software — https://www.midaxo.com/platform/m-a-due-diligence
- InvestmentBank.com — Diligence Tracker — https://investmentbank.com/transaction-desk/diligence-tracker
- Dillien — https://dillien.com/
- DD Navigator — https://ddnavigator.com/

> Sourcing limitations: one additional sampled product (go-diligence) could not be fetched directly (JavaScript-rendered site); its observations are held at existence level from search snapshots. Help-center-level operational documentation was not crawled, so no status vocabulary, permission scheme, or numeric limit is claimed as industry-standard — documented status models are product-specific realizations of one conceptual lifecycle. Vendor marketing figures (savings claims, line-item counts, pricing) are excluded from this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the joint review with the Virtual Data Room pass) are recorded in the paired Research Notes.
