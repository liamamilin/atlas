# Internal Talent Marketplace

## Overview

An **Internal Talent Marketplace** is an organization-operated application that connects the organization's own employees to internal opportunities — open roles, short-term projects or gigs, and commonly mentorships — and manages the path from expressed interest to completed internal movement.

It exists because workforce capability is normally invisible outside its own department: projects stall while qualified employees sit elsewhere, managers hold on to their best people, and employees who cannot see a future inside the organization leave to find one outside. The marketplace answers this with a two-sided structure: the organization publishes opportunities, each employee presents capability and interests, the application brokers between the two, and a governed process turns a match into an actual move.

Its boundary: the candidate population is the organization's own workforce. Planning *how* a career should grow is the work of career development tools; hiring people from outside is the work of recruiting systems. The marketplace transacts movement of the people the organization already has.

## Users & Context

**Primary users:**

- **Employees** — the demand side. They browse or receive recommendations for internal opportunities, express interest, and work toward an internal move. Every member of the workforce is a potential participant; profile quality determines what they are shown.
- **People managers** — a dual-sided role. They post or sponsor opportunities (a role opening on their team, a project needing help), and they also act as the gate on the other side: when one of their team members pursues an opportunity, manager review or release is typically part of the path. Manager reluctance to lose good people ("talent hoarding") is the recognized tension of the category, addressed by policy and culture as much as by software.
- **Opportunity owners / hiring managers** — review the candidates the system surfaces, invite people into projects, and select the eventual placement.

**Secondary users:**

- **Recruiters / talent acquisition** — participate when internal roles run through the recruiting process; the marketplace supplies internal candidates to that process.
- **HR and talent-management leadership** — configure what counts as an opportunity, who may see and apply for what, which approvals are required, and how mobility policy is enforced; monitor mobility and adoption analytics.

The typical context is an enterprise workforce deployment connected to the organization's HR system: employee data flows in, placements flow back. Employees usually meet the product both in a dedicated web experience and inside the tools they already use (chat platforms, email, HR portals).

## Core Model

The defining core is four structures. If any one is removed, the product is no longer this Type:

```text
Organization-posted internal opportunities
        +
Employee talent representation
        ↔  two-sided connection (matching)
        →  governed resolution into internal movement
```

### Internal opportunity population

The supply side: openings and engagements created and maintained by the organization and open **only to its own workforce**. The population commonly mixes several kinds of opportunity with different commitment shapes:

- **internal roles** — permanent moves into open positions elsewhere in the organization;
- **projects and gigs** — time-bounded participation alongside the employee's regular job (stretch assignments, cross-functional initiatives);
- **mentorships** — developmental pairings between employees;
- **adjacent development actions** — some products include learning or shadowing opportunities in the same catalog.

An opportunity carries what a candidate needs to judge it: description, required skills, time commitment, duration, and the team or owner behind it. Opportunity owners are managers or talent teams inside the organization — there is no external advertiser.

### Employee talent representation

The demand side: each employee carries a profile of capability and intent — skills, experience, interests, aspirations, and sometimes availability. This representation is assembled from several sources: what the employee declares, what the HR system of record holds, and (in mature products) what is inferred from work and performance data. It is not a static résumé: it participates directly in matching, and products actively prompt employees to keep it current because match quality depends on it.

### Two-sided connection

The brokering mechanism, running in both directions:

- **toward employees** — the system recommends opportunities aligned with the person's skills, interests, and goals; employees can also browse and search the catalog themselves;
- **toward opportunity owners** — the system surfaces qualified internal candidates for an open role or project, so owners can find and invite people rather than waiting for applications.

How the connection is realized varies: scored matching by AI, rule- or ontology-based filtering, or simple self-identified application against a listing. The two-sided visibility is what distinguishes a marketplace from a plain internal job-posting list, where the only signal is an employee choosing to apply.

### Governed resolution

Expressed interest does not directly change anything. It enters a managed process: review by the opportunity owner, and — the pivotal gate — involvement of the employee's current manager, whose release or approval is commonly required before a move can proceed. Organizational mobility and eligibility policies shape the path throughout. The process ends in a recorded outcome: a transfer into the new role, participation in the project or gig, or a mentorship pairing. In integrated deployments, the placement is handed to the HR system of record; the marketplace brokers the move, it does not own employment records.

### Standard capabilities

A typical mature marketplace adds a consistent layer around this core:

- **AI-based matching** scoring employee↔opportunity fit;
- **career path exploration** — which roles a person's skills unlock and what steps get them there;
- **readiness and gap signals** — what a person is missing for a target role;
- **profile building** with data imported from HR systems and prompted completion;
- **push delivery** — proactive recommendations and alerts into chat, email, and existing workflows rather than waiting for a visit;
- **owner and manager consoles** — posting opportunities, reviewing matches and applicants, releasing team members;
- **mobility analytics** — application, matching, and movement metrics for HR leadership;
- **integration spine** into HRIS, ATS, and learning systems (or being the HR suite itself);
- **linkage to succession and talent-pipeline processes**;
- **AI governance posture** — bias auditing and explainability of recommendations, since algorithmic suggestion of people is the sensitive core of the product.

## How It Works

The operational loop runs supply → connection → resolution → placement, and then feeds the result back:

```text
1. Publish
   manager / talent team posts an internal role, project, or mentorship
   (in suite-integrated deployments, open requisitions can be flagged as internal-eligible)

2. Represent
   employees maintain career profiles — skills, experience, interests, aspirations;
   the system imports HR data, infers where it can, and nudges for gaps

3. Connect
   the system recommends opportunities to employees,
   and surfaces matching employees to opportunity owners;
   employees may also browse and search the catalog themselves

4. Express interest
   the employee applies, raises their hand, or accepts an owner's invitation
   (mechanics differ by opportunity type and product)

5. Resolve
   owner reviews candidates;
   the employee's current manager is consulted or approves the release;
   mobility and eligibility policies shape who can go where and when

6. Place
   selected employee moves into the role (processed as a transfer in the HR system),
   joins the project for its duration, or enters the mentorship pairing;
   outcome recorded, analytics updated,
   and the employee's refreshed profile feeds the next round of matching
```

Two flows deserve emphasis because they carry the product's value:

- **The employee growth flow**: profile → recommendations → interest → manager conversation → placement. Here the marketplace functions as an internal career engine — every recommendation is simultaneously a development signal and a staffing option.
- **The owner staffing flow**: need → post → matched candidates → invite/select → participation. Here it functions as an internal sourcing channel — faster than an external requisition, and with candidates who already know the organization.

## Interfaces

Described conceptually; exact layout and naming vary by product.

### Opportunity feed / marketplace home

The employee's entry surface.

- Purpose: show relevant internal opportunities and make the catalog explorable.
- Typical information: recommended roles, projects, and mentorships; why each was suggested; new opportunities in watched areas.
- Primary actions: open an opportunity, browse/search the catalog, filter by type, skill, or location.

### Opportunity detail

- Purpose: everything a candidate needs to judge and pursue one opportunity.
- Typical information: description, required skills, time commitment and duration, owning team, how the person's profile compares.
- Primary actions: express interest / apply / join, ask a question, save.

### Career profile

- Purpose: the employee-side representation that powers matching.
- Typical information: skills, experience, education, interests, career aspirations, availability.
- Primary actions: add or confirm skills, set aspirations, complete prompted gaps.

### Career path explorer

- Purpose: orientation before opportunity — where can this career go from here.
- Typical information: possible next roles from the current one, skill gaps for each, steps to close them.
- Primary actions: explore paths, target a role, see related opportunities.

### Manager / opportunity-owner console

- Purpose: run the supply side.
- Typical information: posted opportunities, matched or interested candidates, team members' interests and development activity.
- Primary actions: post and manage opportunities, invite candidates, review applicants, approve or release a team member.

### HR administration

- Purpose: govern the marketplace as a program.
- Typical information: opportunity types, eligibility and mobility policy, approval workflows, adoption and mobility metrics.
- Primary actions: configure rules and workflows, curate the catalog, monitor analytics.

### Embedded surfaces

Recommendations, alerts, and increasingly conversational assistants delivered inside collaboration tools and email, so the marketplace is encountered in the flow of work rather than only in a portal.

## Important Rules / Behaviors

### The population is internal

Only the organization's own employees participate as candidates. This single rule separates the Type from every external hiring surface and is why employee data can flow freely into matching.

### Manager consent is the pivotal gate

An interested employee is not a movable employee. The current manager's review or approval sits in the path of most role moves, and marketplace programs treat manager cooperation as the make-or-break adoption factor — the "talent hoarding" problem is a named failure mode of this Type, not an edge case.

### Matching is policy-aware

Recommendations and eligibility reflect the organization's mobility rules — who may apply, when, for what — not raw skill similarity alone. The marketplace operationalizes the organization's mobility policy as much as its skills data.

### Opportunity types carry different outcome semantics

A role move ends a reporting relationship and begins a new one; a gig adds time-bounded participation without ending the current job; a mentorship creates a pairing with no staffing change at all. The same catalog can contain all three, and the resolution workflow differs accordingly.

### Profile quality drives match quality

The system's recommendations are only as good as the talent-side representation, which is why mature products continuously import HR data, infer skills where possible, and prompt employees to complete their profiles.

### Recommendations are auditable

Suggesting people algorithmically is high-stakes; mature products expose explainability and undergo bias auditing of their matching models. This is a structural expectation of the category rather than a decorative feature.

## Variants

- **Opportunity-type emphasis** — role-first deployments centered on internal mobility and retention; gig/project-first deployments centered on workforce agility and cross-functional staffing; balanced portfolios.
- **Delivery pole** — standalone specialist platforms vs modules inside an HCM suite, where the marketplace sits on the same data core as the org chart, employment records, and recruiting.
- **Matching philosophy** — deep-learning matching over broad talent data vs matching grounded in a vendor-curated skills ontology; the choice is a product philosophy, not a capability difference.
- **Surface posture** — dedicated portal vs delivery embedded in chat, email, and collaboration tools; most mature products do both.
- **Scope** — single-organization deployments vs enterprise talent sharing across affiliated entities or divisions.
- **Program posture** — opt-in development marketplace (employees explore growth) vs redeployment-driven operation (the marketplace as the mechanism for moving people during reorganization); most deployments blend the two.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Career Development Platform | plans growth: employee-owned development plans anchored to career paths and competencies; the marketplace transacts actual movement into actual opportunities. Career pathing appears in both — as the record's anchor in one, as navigation in the other |
| Skills Management Platform | maintains the skills data (ontologies, inventories, assessments) that feeds marketplace matching; has no opportunity population and no placement workflow |
| Applicant Tracking System / Recruiting Management Platform | manages external hiring and requisitions; the marketplace's candidates are internal and often feed into the same requisition process from the inside |
| Job Board | public advertising surface; anyone can be a candidate, and application capture is the end of its involvement — no managed mobility path |
| Succession Planning Platform | governance over critical roles with curated, management-nominated slates; the marketplace is open access where any employee may express interest. Products link the two but the participation models are opposites |
| Resource Management / Professional Services Automation | matches people to work for delivery and billing execution; the marketplace matches people to opportunities for mobility and development. Some vendors ship both as separate products |
| Employee Onboarding Platform | begins after a placement is made; the marketplace ends at the placement |

The sharpest seam is with the Career Development Platform: vendors bundle both (career paths beside opportunity catalogs), and both speak the language of growth. The structural difference is the object of record — a development plan versus a managed opportunity population with a placement workflow.

## Representative Products

- Gloat
- Fuel50
- SAP SuccessFactors (Opportunity Marketplace / Career and Talent Development)
- Workday (AI for Talent Mobility)
- Eightfold AI

## Sources

Research date: **2026-09-07**

- Gloat — Talent marketplace explained: https://gloat.com/platform/talent-marketplace/ ; Platform: https://gloat.com/platform/ ; Intelligent Tools: https://gloat.com/ai-technology/intelligent-tools/
- Fuel50 — Talent Marketplace: https://fuel50.com/products/talent-marketplace ; product navigation: https://fuel50.com/
- Workday — AI for Talent Mobility: https://www.workday.com/en-us/products/talent-management/ai-talent-mobility.html ; Talent Management: https://www.workday.com/en-us/products/talent-management.html
- SAP — Career and Talent Development: https://www.sap.com/products/hcm/career-talent-development.html ; Talent Management: https://www.sap.com/products/hcm/talent-management.html
- Eightfold AI — Talent Intelligence Platform: https://eightfold.ai/products/talent-intelligence-platform/ ; Project Marketplace: https://eightfold.ai/capabilities/project-marketplace/

> Sourcing limitation: vendor help-center and product-documentation surfaces were not reachable from the research environment on 2026-09-07 (SAP's help portal renders as a JavaScript shell, and one vendor's documentation site requires customer login). Evidence is therefore strongest at the official product-page level and does not extend to click-path-level operational detail. Accordingly, this document deliberately states no precise eligibility rules, approval chains, time windows, or numeric limits; where operational behavior varies by product it is described in general terms.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
