# Candidate Profile Platform

## Overview

A **Candidate Profile Platform** is the hiring organization's system of record for **people who might be hired**. Its defining core is the **candidate profile**: a persistent, structured, person-level record of a potential hire — identity and contact details, background (experience, education, skills), documents, and the recruiting team's own context (notes, tags, statuses) — that exists before, between, and after any specific job application.

This is deliberately distinct from the candidate record inside an Applicant Tracking System. An ATS profile is bound to a hiring pipeline: its center of gravity is applications, interview stages, scorecards, and offers for specific jobs. A Candidate Profile Platform holds the person-level layer that lives *outside* any pipeline: prospects who have not applied, past applicants who were not selected, passive talent being cultivated, event and community contacts, and (in some deployments) the employer's own employees considered for internal moves. The two interlock — profiles feed applications at the moment of apply, and application history flows back into profiles for rediscovery — but the managed object and the workflow spine differ.

The market realizes this Type under several names — talent CRM, candidate CRM, talent engagement platform, talent intelligence platform — and typically bundles it with search and outreach capabilities. What makes the Type recognizable is not any single bundled capability but the record layer itself: one maintained profile per person, kept over time, worked by the employer's recruiting side.

## Users & Context

Primary users are the hiring organization's talent acquisition roles:

- **Recruiters** — work profiles day-to-day: review a person's background, decide fit for a role, advance or park them, keep the record current.
- **Sourcers** — populate the platform: find people externally, import and enrich them, place them into pools for open or anticipated roles.
- **Recruiting coordinators and ops** — maintain data quality (duplicates, fields, tags), manage integrations and permissions.
- **Hiring managers** — mostly consumers: they receive shared pools of curated profiles and give feedback on them.

Secondary users and contexts:

- **Talent marketing / employer brand teams** — run signup forms and campaigns whose responses create and update profiles.
- **Staffing agencies** (variant) — maintain candidate profiles as reusable inventory across client assignments.
- **Candidates themselves** appear only as *subjects* of records and, in some products, as limited participants (filling a signup form, updating their own details) — they do not operate the platform.

The work context is a recruiter's desktop workflow, typically alongside an ATS and professional networks. The platform is usually a web application; browser extensions that capture profiles from other websites are a common companion surface.

## Core Model

### The candidate profile

The center of the system is one record per person. A profile carries, across the researched products:

- **Identity and contact** — name, email address(es), phone number(s), location, often a link to the person's public professional-network profile.
- **Background** — work experience, education, skills; in AI-forward products, inferred skills and potential derived from the raw history.
- **Documents** — the resume/CV and similar artifacts, stored as attachments to the profile.
- **Recruiter-added context** — private notes, shared comments, tags, and statuses (e.g., marking where the person stands with the employer).
- **History** — the accumulating trail of interactions: form submissions, message contacts, application history synced from the ATS, profile updates.

Two structural rules give the model its shape:

**One person, one record.** Because the same person arrives through many doors — a signup form, a CSV import, an external search, an ATS sync — mature products invest in deduplication and merge. Observed behaviors include collapsing same-person rows from different sources into one search result, cross-listing an existing person into a new pool instead of creating a second profile, and explicit merge-duplicate tooling. The profile, not the source event, is the durable unit.

**The profile is not the application.** A profile exists independently of any requisition. One person may be in several pools at once, may have applied to jobs in the past (or never), and may be active in a pipeline right now — the profile persists through all of it. Products that also sell an ATS make the distinction explicit inside their own interface: records sourced into the profile database are visually distinguished from records that exist only as ATS applications, and rediscovery over past applicants excludes people with active applications by default in the implementations that document this behavior — those in-process candidates belong to the pipeline's care, not the profile layer's.

### Pools, projects, and communities

Profiles are organized into named groupings — commonly called projects, talent pools, or talent communities. A grouping is typically created for a role ("one project per open role" is a documented best practice), a campaign, an event, or a standing community of people interested in the employer. One profile can belong to many groupings simultaneously; groupings are containers over the person layer, not subdivisions of it. Custom fields and tags attach recruiter-defined structure at the grouping or profile level.

### Where profiles come from

The profile layer is fed from several directions, and multi-source population is a standard capability:

- **External discovery** — searching a large index of public professional profiles and saving found people into the database.
- **Imports and uploads** — CSV/bulk upload of existing lists (conference lists, past sourcing output), with the platform enriching sparse seeds (name, employer, public professional-network profile URL) into fuller profiles (background, education, photo, contact information).
- **Professional-network exports** — importing selections exported from recruiter tools on public networks.
- **Candidate self-service** — signup forms on the career site ("talent community" forms) that create profiles directly from candidate-provided answers, with the resume stored as a profile attachment.
- **ATS and HCM sync** — indexing past applicants from the ATS for rediscovery, and (in some products) pulling employee records from the HR system so internal candidates can be considered alongside external ones.

### How It Works

The platform's work moves through four recurring loops:

**Population loop.** A person is captured from some source → the platform resolves their identity (matching against existing records; merging or cross-listing rather than duplicating) → sparse data is enriched into a fuller profile → the profile lands in a default holding area or directly into a pool.

**Organization loop.** Recruiters create pools/projects for roles, campaigns, or communities → move or add profiles in bulk → tag, status, and annotate them → keep the structure current as roles open and close (pools can be duplicated or archived in observed implementations; deletion, where offered, is treated as permanent and unrecoverable).

**Consumption loop.** The recruiter searches or browses the profile database (by skills, experience, location, source, tags, past-application history) → opens a profile to review the person in full → acts on the record: add to another pool, share with a hiring manager, request contact information, export, or hand off to outreach. Sharing is a first-class act: pools are shared to teammates and hiring managers with view/comment-level control, and individual profiles can be exported to PDF or spreadsheets for people outside the platform.

**Handoff loop.** When a person becomes an applicant, the profile connects to the ATS (push, sync, or linked reference). When a person was an applicant and was not hired, the ATS history flows back: the profile layer indexes past applicants so they can be rediscovered for later roles — filtered by the jobs they applied to, the stages they reached, and how they were scored — subject to the active-application exclusion noted above.

A maintenance thread runs through all loops: keeping profiles current (public-source data drifts as people change or privatize their information — a drift products explicitly warn about), managing consent and retention for stored personal data, and (in metered products) tracking credits for contact retrieval and exports.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Profile detail page

The single most important surface — the employer's working view of one person.

- Typical information: identity and contact block, experience/education/skills, resume and documents, tags and status, notes and comments, interaction history, linked application history.
- Primary actions: edit details, add notes/tags/status, add to or remove from pools, share, request contact info, export, start outreach, hand off to the ATS.

### Database / search view

The recruiter's entry surface for finding people.

- Typical information: a filterable list of profiles with columns for key attributes; counts and saved searches.
- Primary actions: search and filter (including over past ATS applicants in products that index them), bulk-select profiles, add selections to pools or campaigns.

### Pools / projects

The organization surface.

- Typical information: list of member profiles, pool-level custom fields, owner and sharing state.
- Primary actions: create/rename/archive/delete pool, add or transfer profiles between pools, share with teammates and hiring managers, run pool-level actions (export, outreach, status changes).

### Sharing view for hiring managers

A reduced surface for consumers outside the recruiting team.

- Typical information: the curated pool of profiles shared with them.
- Primary actions: review profiles, comment or give feedback, advance or dismiss candidates — without broader database access.

### Signup forms (talent community)

The candidate-facing intake surface.

- Typical information: employer-branded form with standard identity fields (commonly required — a profile needs an identity anchor to exist), optional resume upload, and employer-defined questions.
- Primary actions: submit; the submission creates or updates a profile and places it in the community pool.

### Settings / administration

- Typical information: user and permission configuration, tag/status taxonomy, custom fields, integrations (ATS, HCM, email), data-privacy settings.
- Primary actions: configure the taxonomy and integrations that the other surfaces depend on.

## Important Rules / Behaviors

- **One person, one record.** Duplicate suppression and merge are structural: the same person arriving through different doors resolves to a single profile. This rule is what makes the profile a trustworthy long-term asset.
- **Profile ≠ application.** The record layer and the pipeline layer are kept distinct even inside products that sell both: sourced profiles are marked as distinct from ATS-only records, and rediscovery over past applicants excludes people with active applications by default. A person "in process" is the pipeline's record; a person "not selected" or "never applied" is the profile layer's.
- **Public-source data goes stale.** Profiles enriched from public professional data carry a freshness caveat that vendors state explicitly: people change jobs, privatize, or delete their public information, and the stored profile can drift from reality. Treating profile data as a cached view rather than live truth is a built-in behavior of the Type.
- **Consent and retention matter.** Storing personal data about people who were never hired is a regulated activity in many jurisdictions; mature products (especially enterprise-focused ones) provide consent management and compliance posture around the database. The specifics vary by product and region.
- **Sharing is scoped.** Hiring managers and teammates see what is shared with them — a pool or a profile — not the whole database. Confidential pools and role-scoped visibility exist in enterprise deployments.
- **Some actions are metered.** In some products, retrieving candidate contact information or exporting data consumes plan credits, and failed lookups may not consume them. Metering is product-dependent, not definitional.
- **The platform supports decisions; it does not make them.** Scores, rankings, and recommendations (where present) are decision support for the recruiting team; the advance/reject decisions remain human actions on the profile.

## Variants

- **CRM-first** — the profile database and pool management are the product's heart, with search and outreach attached (the classic talent CRM).
- **Search-first** — a large external profile index with saved-search machinery is the entry point, with profile management built around what search finds.
- **AI-intelligence-first** — deep inferred profiles (skills, potential, career trajectories) power matching and rediscovery across hiring and internal mobility.
- **ATS-embedded module** — the same record layer shipped as the CRM/database module of an ATS suite rather than a standalone product.
- **Agency mode** — staffing firms run candidate profiles as reusable inventory across client assignments, with submission flows replacing (or alongside) application flows.
- **Internal-talent extension** — employee records from the HCM join external candidate profiles so internal and external talent are considered together.
- **Scale and sourcing posture** — from employer-owned databases only, to platforms operating very large public-profile indexes.
- **Regional/compliance depth** — consent campaigns, data residency, and retention tooling vary with the regulatory environments customers operate in.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Applicant Tracking System / ATS | interlocking neighbor | ATS owns the hiring pipeline (requisitions, applications, stages, offers); its candidate profile is the pipeline record. This Type owns the person-level record layer outside the pipeline. The sharpest seam: bind the profile to a requisition's stages and it becomes the ATS record. |
| Candidate Search Platform | capability overlap | Search is a core capability here, but the managed object is the maintained profile record, not the query. A search platform answers "who matches?" over a corpus; a profile platform keeps the people it found. Market products straddle; boundary deserves joint review. |
| Talent Sourcing Platform | upstream activity vs record layer | Sourcing is the identification-and-outreach activity; this platform is the record layer those activities deposit into and draw from. |
| Recruitment Marketing Platform | upstream neighbor | Marketing owns pre-application audience attraction (campaigns, career site, distribution); this platform owns the records that attraction converts into. The signup form is the seam. |
| Resume Builder | opposite side of the artifact | Candidate-side document authoring vs employer-side record management; the resume is one input artifact to the profile. |
| Professional Social Network | data source, not the same surface | The social network hosts the person's public self-presentation on a shared graph; this platform holds the employer's private working record about the person. Public profiles feed the record; the surfaces, ownership, and rules differ. |
| Customer Relationship Management / CRM | structural analog | Same record-relationship pattern (person records, pools, notes, activity, dedup) applied to a different domain object — the candidate rather than the customer/deal. |
| Job matching marketplaces (candidate-authored profiles) | different Type | There the platform operates a two-sided marketplace and the candidate owns the profile employers browse; here the employer owns the record about the person. |

## Representative Products

- **Beamery** — enterprise talent CRM; profile-centric database with talent pools, consent management, and ATS/HCM integration.
- **Gem** — talent engagement platform; People (CRM) product with projects, talent-community forms, and search across its own database plus indexed ATS candidates.
- **Eightfold AI** — AI talent intelligence; deep inferred profiles powering matching, rediscovery, and internal mobility across a talent suite.
- **SeekOut** — search-first talent platform; large external profile index plus profile management (uploads, enrichment, notes/tags/statuses, projects, exports).

The ATS-side contrast (the candidate profile as pipeline record) was checked against Greenhouse Recruiting's documentation to keep the boundary honest.

## Sources

Research date: **2026-09-07**

- Gem Help Center — People directory; Projects overview; Gem Talent Community; ATS candidate rediscovery (ATS search) — https://help.gem.com/
- SeekOut Help Center — Candidate Profiles collection (profile management, uploads & enrichment, contact information, exports); Projects collection (how to use projects, sharing) — https://support.seekout.com/
- Greenhouse Support — Candidate profile redesign overview; Candidate profiles section — https://support.greenhouse.io/
- Beamery — homepage and Talent CRM product page — https://beamery.com/
- Eightfold AI — homepage and Talent Acquisition product page — https://eightfold.ai/

> Sourcing limitations: Beamery's helpdesk and Eightfold's product documentation portal could not be reached from the research environment (connection failures and login gating, respectively); evidence for those two products is product-page level, and no internal mechanics are claimed for them. Ashby's help center was unreachable after repeated attempts and was dropped from the sample. Precise numeric limits, plan-level behaviors, and vendor-specific mechanics are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
