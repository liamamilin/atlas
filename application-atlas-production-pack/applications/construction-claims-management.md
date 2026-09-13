# Construction Claims Management

## Overview

A Construction Claims Management application is a system of record for contractual claims on a construction project: recorded assertions by one contracting party that events on the project entitle it to additional payment and/or an extension of time under the contract. It captures each claim with its event basis, contractual entitlement, and claimed impact; preserves the evidence trail that substantiates it; enforces the contractual procedure that governs it (notice deadlines, response periods, clause-referenced correspondence); and tracks every claim through a governed lifecycle from notice to agreement or escalation.

The defining core is fourfold: a **claim record** (event + entitlement + impact, tied to a specific contract and counterparty), **substantiation linkage** to the project record, a **governed lifecycle to resolution**, and a **claims register** that treats claims as a portfolio against the contract. Claims management exists for the *disagreement path* — the situation where the parties cannot agree on a change, and one party asserts its contractual right instead of executing an agreed change order.

## Users & Context

Primary users:

- **Contractors and subcontractors** (especially specialist trades): capture events, issue notices, build and substantiate claims for additional payment or time.
- **Commercial / contract managers**: run the claims register, monitor deadlines, draft responses, report commercial exposure.
- **Owners, PMO teams, and contract administrators** (engineers under FIDIC/NEC-style contracts): receive and review claims, respond, certify or determine outcomes.

Secondary users:

- **Claims consultants and delay analysts**: assemble chronologies, analyze programme impact, draft claim submissions.
- **Legal counsel**: consume the claim file when a dispute escalates to adjudication, arbitration, or litigation.

The work happens on live projects under standard contract families (FIDIC, NEC, and bespoke conditions), where contractual procedures impose strict notice windows and response obligations. Claims are typically formalized long after the triggering events, so the software's central value is preserving a defensible record while the project runs.

## Core Model

**Claim** — the central object. A discrete documented claim tied to a specific contract and counterparty, carrying:

- an **event basis**: what happened on the project (late information, unforeseen conditions, disruption, instructions, delays);
- an **entitlement basis**: the contractual right invoked — the clause or procedure under which payment or time is claimed;
- a **claimed impact**: additional money and/or extension of time, itemized and traceable to supporting records.

**Substantiation** — the evidence attached to or referenced by a claim: correspondence, notices, site diaries, meeting minutes, drawings, schedules, valuations, photographs. Mature products make this linkage first-class: every asserted fact and amount should trace back to a source document, because a claim's strength under scrutiny depends on its evidence trail.

**Notice / deadline** — the contractual time-bar machinery. Contracts typically require claims to be notified within defined windows after the triggering event; missing a window can extinguish entitlement. Products commonly extract these deadlines from the contract and track them against each claim.

**Claims register** — the portfolio view of all claims on a contract or project: status, claimed value, deadlines, and outcomes. Claims are managed as a set with a net commercial position, not as isolated documents.

**Response** — the counterparty side of the lifecycle: review, response, and (where the contract provides) determination or agreement. Mature products serve both parties, not only the claimant.

Conceptual lifecycle of a claim:

```text
Event on project
  ↓ noticed within contractual window
Claim (event + entitlement + impact)
  ↓ substantiated from project records
Response / review by counterparty
  ↓
Negotiation
  ↓
Agreement — or escalation to dispute resolution
```

## How It Works

The typical workflow runs in parallel with project execution:

1. **Event capture.** Site and commercial teams record events as they happen — delays, late design information, clashes, unforeseen conditions — often through structured event or daily-record forms. Each record captures cause, effect, the contractual clause invoked, mitigation taken, and whether notice was issued, with timestamps and an audit trail.
2. **Notice and deadline management.** The system tracks contractual notice windows extracted from the contract, alerts the team before deadlines expire, and generates contractually compliant notice correspondence.
3. **Claim assembly.** A claim is built from captured events plus referenced project records: correspondence, minutes, drawings, schedule updates, valuations. The claim itemizes money and time impact, each line traceable to its source.
4. **Submission and response.** The claim is submitted to the counterparty (or the claim is received and logged, from the respondent's perspective). The system generates clause-referenced correspondence, records the response, and advises the parties of their options under the contract's procedure.
5. **Negotiation and resolution.** Claims move through review, negotiation, and — if unresolved — escalation toward adjudication, arbitration, or litigation. Throughout, the register reports status, values, and deadlines; the full history of actions and correspondence is preserved for defense.

Two postures exist in the market. **Live-capture posture**: record events and build defensible positions while the project runs, so the claim never depends on reconstruction from memory. **Reconstruction posture**: after a dispute forms, assemble the factual timeline and evidence file from the accumulated project record — increasingly assisted by tools that index the corpus, build source-linked chronologies, and flag contradictions between documents.

## Interfaces

Common interfaces across the researched products:

- **Claims register / list** — all claims with status, claimed value, deadlines, and counterparty; filterable and exportable; the commercial cockpit.
- **Claim detail** — the claim's event basis, entitlement clause, itemized impact, substantiation links, correspondence history, and an automatically maintained timeline of actions.
- **Event / notice capture forms** — quick structured forms for recording events and issuing contractual notices, with required fields and document attachments.
- **Deadline / notice-compliance views** — upcoming and missed contractual windows, which notices were served and against which clause.
- **Document / evidence workspace** — consolidated reference lists of claim-related project records, searchable and filterable by party, trade, or period.
- **Reporting / dashboards** — claim status and progress reports, outstanding claims, claimed vs certified amounts, commercial exposure across the contract.

## Important Rules / Behaviors

- **Time-bars are the sharpest rule.** Contractual notice windows are hard constraints; products treat deadline tracking as a core obligation because a late notice can defeat an otherwise valid claim.
- **Procedure gates progression.** Claims move through the contract's own procedure — notice, substantiation, response, determination — and the software's value is keeping every step compliant and recorded. Actions performed late are typically flagged.
- **Evidence traceability is the defensibility standard.** Every assertion and amount in a claim is expected to trace to a dated, attributed source document; products increasingly check this automatically and flag gaps before submission.
- **Both parties' paths matter.** A claim that is asserted by one party must be reviewed and responded to by the other; mature products model the respondent's obligations, not just the claimant's.
- **Audit trail is non-negotiable.** Every action, communication, and document is time-stamped and attributed, because the record may later be scrutinized in a formal dispute.
- **Claims are prospective as well as live.** Registers commonly track potential claims (events that may ripen into claims) alongside current and closed ones.

## Variants

- **Contract-family-specific**: products configured around FIDIC (Red/Yellow/Silver books, Sub-Clause 20.1 claim procedures) or NEC (compensation events, early warnings), including regional modifications used in specific markets.
- **Constituency variants**: contractor-side event-capture products (specialist subcontractors under payment risk), owner/PMO-side claims processing embedded in the commercial contract lifecycle, and claims-consultant tooling for evidence assembly and delay analysis.
- **Module vs standalone**: claims management appears both as a dedicated product and as a module inside broader contract-administration or capital-program platforms.
- **AI-era evidence tooling**: a growing variant that ingests the full project record and produces source-linked chronologies, contradiction detection, notice-compliance matrices, and draft claim narratives — deliberately leaving fault judgment to human experts.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Change Order Management | the agreed path | change orders record changes the parties agreed to; claims assert entitlement when agreement is absent or contested |
| Construction Contract Administration | broader host | administers the contract's routine instruments (notices, instructions, variations, payment certificates); claims management is the specialized disagreement lane |
| Construction Document Management | adjacent | stores project documents; claims management links them into entitlement arguments and a claim lifecycle |
| Daily Log Application | evidence supply | site records feed claims; they carry no claim lifecycle or entitlement structure |
| Litigation / eDiscovery Platform | downstream | runs the formal legal case after escalation; claims management handles the project-level contractual claim before and up to that point |
| Insurance Claims Management | same word, different domain | adjudication of losses under insurance policies; unrelated object world |
| Progress Billing | same word, different sense | "payment claims" / "progress claims" in some markets mean payment certification, not contractual disputes |

## Representative Products

- **C-COM** — FIDIC/NEC contract administration platform with a dedicated claims module (time-bar monitoring, contractual correspondence, claims register).
- **Kahua Construction Claims & Dispute (SuperSet app)** — claims app on a construction management platform for contractors, consultants, and suppliers.
- **ClaimMaster.ai** — contractor-side live event capture with a structured cause/effect/entitlement record and defensibility scoring.
- **ClaimsBridgeHQ** — FIDIC/GCC-focused contract-aware monitoring with deadline alerts and an auto-maintained claims register.
- **WhiteHelmet Contract & Claim Management** — owner/PMO-side claims workflow within the commercial contract lifecycle.

## Sources

- C-COM — FIDIC Contract Management Software & Features pages — https://www.ccom.cloud/fidic-contract-management-software, https://www.ccom.cloud/features (researched 2026-09-10)
- Kahua kStore — Construction Claims & Dispute app listing — https://launch.kahua.com/kStore/Detail/971 (researched 2026-09-10)
- ClaimMaster.ai — product site — https://claimmaster.ai/ (researched 2026-09-10)
- ClaimsBridgeHQ — product site — https://claimsbridgehq.com/ (researched 2026-09-10)
- WhiteHelmet — Contract and Claim Management — https://www.whitehelmet.sa/products/contract-and-claim-management (researched 2026-09-10)
- Market context: Storia Technologies (storiatechnologies.com), Eviant (eviant.ai), Astora (astora.app), VitruAI (vitruai.com), Aurigo (aurigo.com), InEight learn site (payment-claims polysemy) — all researched 2026-09-10

Research limitation: no public Tier-1 operational help documentation was reachable for the sampled products; lifecycle stages and structures are described at the level the products themselves publish, and precise field lists, default statuses, and numeric deadlines are not asserted.
