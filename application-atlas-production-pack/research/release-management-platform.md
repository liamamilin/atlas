# Research Notes — Release Management Platform

Research date: 2026-09-09
Leaf: Release Management Platform (§12 Software Development & Product Engineering)
Slug: release-management-platform

## Research Goal

Understand what a "Release Management Platform" actually is as an Application Type: what the release object is in these products, what lifecycle it carries, what coordination machinery surrounds it, and where the Type ends relative to Continuous Delivery Platforms, IT Change Management, issue-tracker release versions, and feature-flag platforms.

## Initial Boundary (pre-research hypothesis)

- Core use: plan, coordinate, and govern software releases — grouping changes/deployments/work items into release vehicles, coordinating across teams, gating readiness, tracking the release lifecycle.
- Users: release managers, delivery managers, engineering/DevOps leads, PMO.
- Nearest neighbors: Continuous Delivery Platform (execution), IT Change Management (per-change governance), ITSM suites (module packaging), issue trackers' release/version features, Feature Flag platforms, PPM.
- Pre-hung seams from processed siblings:
  - **continuous-delivery-platform** (processed 2026-09-07): "release governance/planning (calendars, approvals policy, release notes, coordination across teams) vs deployment execution machinery"; test: executes deployments against environments → CD; coordinates/plans/governs releases as management objects → Release Management. Joint review flag recorded against this leaf.
  - **it-change-management** (processed 2026-09-08): "releases bundle changes/deployments into coordinated delivery vehicles; change management governs each modification individually. Expected seam: aggregation-and-coordination vs per-change authorization/record."

## Research Questions

1. What is a "release" as an object in these products? What does it contain and bind?
2. What lifecycle do releases move through, and what drives the transitions (gates, criteria, approvals, completion of constituents)?
3. How do releases relate to changes, deployments, applications/systems, environments?
4. What coordination machinery exists — calendars, schedules, blackout/freeze windows, dependencies, stakeholders, conflict detection?
5. How do these platforms relate to CI/CD tools — integration vs execution?
6. Who uses the product, and on what interfaces?
7. Where is the boundary vs CD platforms, IT change management, tracker release versions, feature flags, PPM?
8. Historical check: do pre-DevOps / ITIL-era release-management products fit the same definition?

## Representative Products

| Product | Pole | Evidence tier reached |
|---|---|---|
| Planview Release (formerly Plutora) | enterprise release management / VSM | Tier 1 (Success Center user guide) + Tier 2 (product page) |
| CloudBees CD/RO — Release module | release orchestration (execution-coupled) | Tier 1 (official docs) |
| Digital.ai Release (formerly XebiaLabs XL Release) | release orchestration | Tier 2 (product page + docs home one-liner); operational docs unreachable |
| Octopus Deploy | CD pole — boundary calibration | Tier 1 (official docs) |
| GitLab Releases | dev-platform/tracker pole — boundary calibration | Tier 1 (official docs) |

Selection rationale: two deep samples on opposite ends of the automation-depth axis (planning-centric enterprise pole vs execution-coupled orchestration pole), one Tier-2 orchestration sample, plus two thin poles that use the word "release" with different object semantics — exactly the anti-overfit calibration the Type needs.

## Sources

Fetched 2026-09-09:

- Planview Release product page — https://www.planview.com/products-solutions/products/planview-release/
- Planview acquisition page (Plutora → Planview Release) — https://www.planview.com/acquisitions/about-plutora/
- Planview Release & Verify user guide (Success Center):
  - Introduction to Release — https://success.planview.com/release-and-verify/Release/Introduction_to_Release
  - Manage Phases and Gates — https://success.planview.com/release-and-verify/Release/Manage_Phases_and_Gates
  - Introduction to Deployment — https://success.planview.com/release-and-verify/Deployment/Introduction_to_Deployment
  - (full section index captured: Release, Change, Deployment, Build, Blockout, Environment*, System, PIR, Dashboard, Reporting, Initiative Management, Organization Structure, CDP, Activities Kanban, TEBR/TECR, User Management)
- Digital.ai Release product page — https://digital.ai/products/release/
- Digital.ai docs home (via docs.xebialabs.com mirror) — https://docs.xebialabs.com/
- CloudBees CD/RO docs — https://docs.cloudbees.com/docs/cloudbees-cd/latest/releases/ ("Create and manage releases")
- Octopus Deploy docs — https://octopus.com/docs/releases
- GitLab docs — https://docs.gitlab.com/ee/user/project/releases/

Unreachable (recorded limitations):

- docs.digitalai.com — transport errors ×2 (operational docs of Digital.ai Release not reachable; docs.xebialabs.com mirror serves only the docs home)
- ibm.com/docs (IBM UrbanCode Release) — 403 ×2
- servicenow.com — timeout ×2
- docs.opentext.com (OpenText/Micro Focus Release Control) — transport error
- support.atlassian.com (Jira releases doc) — 404 on guessed URL; not retried further

## Product A — Planview Release (formerly Plutora)

### Key observations (Tier 1, Success Center user guide)

- Positioning: "The Release & Verify Release Management module enables you to define, manage and visualize your Release Management process across your Software Delivery Lifecycle (SDLC)... able to model your Release Process irrespective of your development methodology or level of automation... a flexible framework that enables you to bake governance and auditability into your process." (Layer A)
- Stated problem space: "Difficult to determine accurate release statuses; limited collaboration between delivery teams, operations, and the business; governance and compliance are difficult to audit, enforce & automate; difficulty in the coordination of resources & stakeholders notifications." (Layer A)
- Benefits list: visibility into release progress (role-based visualizations, real-time status); integrated governance & compliance ("Automated and manual gates incorporated into every delivery process eliminate out-of-band efforts. Audit history available on demand"); decreased business risks/production incidents; environment/data/resource optimization ("Planning, orchestration, and arbitration avoid resource collisions, project delays, and bottlenecks"); improved service transition; continuous improvement. (Layer A)
- **Release types**: "There are three core types of Release: Enterprise, Project and Independent. An Enterprise Release is used to group multiple Project Releases and Independent Releases together under one Release (for example, a release that affects systems across multiple portfolios that have dependencies). Changes cannot be assigned to the Enterprise Releases, only to the child releases. Project Releases are intended to be child release of an Enterprise Release, although they can also stand alone. Independent Releases are used to represent independent, normally low impact, releases that have no dependencies." (Layer A)
- **Phases and Gates**: "Phases are periods in a Release where Activities need to be completed, e.g. design, development, testing, deployment, etc. Whereas, Gates are milestone points in time where a Criterion or approval needs to be met for the Release to remain on schedule." Phases/gates can be pushed from Enterprise Release to child releases; gates have associated Criteria; changing phase/gate dates affects associated Activities/Criteria and Environment Bookings. Release Templates also carry phases/gates. (Layer A)
- **Release Manager page**: search/open a Release by Release ID or Release Name; tabs include Phases & gates, Release Manifest, Release Changes, Release Environments, Release Stakeholders, Release Activities, Impact Systems, Events, Release Analytics; Release Calendar and Release Schedule surfaces exist. (Layer A — section index + page structure)
- **Deployment Management**: "automated run-book capabilities to define, manage and report on go-live implementations into your Production estate. Deployment Management includes built-in approval workflows to ensure that run-books can be tested in a pre-Production or Staging environment and that any issues or feedback captured during the go-live is captured. Complex deployments consisting of multiple run-books can be managed simultaneously and can be viewed holistically in a Command Centre. The run-books can be used to orchestrate automated activities, as well as manage any manual tasks." Master Deployment Plan vs stand-alone Deployment Plan; Deployment Plan Activities, Checkpoints, Issues, RACI. (Layer A)
- **Object estate** (section index): Release, Change (with workflow, status, priority, type customization; linked items; delivery release management), Build, Blockout (blackout periods with types), Environment machinery (Environment, Environment Booking, Environment Group, Environment Schedule, Environment Stack, Environment Request, TEBR — Test Environment Booking Request, TECR — Test Environment Change Request, Environment Impact Matrix, Environment Map), System (System Impact Matrix), PIR (Post-Implementation Review items/activities), Dashboard (Release Management KPIs, Insights, Value Stream Flow Metrics, IM Dashboard), Health Check Dashboard, Reporting, Initiative Management, Organization Structure, CDP (Continuous Delivery Pipeline), Activities Kanban, User Management. (Layer A — structure; depth not fetched for all)
- Product page (Tier 2): release calendar "including blackout periods"; "Streamline workflows and accelerate releases with automation"; "Minimize risks by identifying and resolving conflicts early"; "Ensure consistent governance and simplify approval processes"; "Access a comprehensive view of release progress, status, quality, automation and overall health". Customer quotes name roles: "Quality and Release Services" manager, "Release and Environment Manager", "Projects and Portfolio Release Manager". (Layer A for quotes, Tier 2 for capability claims)

## Product B — CloudBees CD/RO (Release module)

### Key observations (Tier 1, official docs)

- "The Release module captures, executes, visualizes, and controls the life cycle of multiple application or microservice enterprise releases. Using the Release capability, outputs from multiple teams can be coordinated to produce a final release to be pushed to production." (Layer A)
- "You can use the Release feature to deliver software releases through traditional methods where changes from multiple applications or microservices are bulked up and are released together as a unit through a pipeline on a regular cadence (schedule) such as weekly, monthly, quarterly, or other frequency. In such traditional scenarios, the Release capability allows you to manage dependencies between multiple applications or microservices. In addition, you can even use the Release feature to cater to Continuous Delivery-style releases where code check-in from a developer can traverse all the way to production through various pipeline stages and approval gates. The Release feature allows CloudBees CD/RO to manage all the releases in one platform, regardless of the release methodologies used by the release team." (Layer A)
- **Release Dashboard / Release List**: "bird's eye view of all the releases that are planned, active, or completed. For a specific release, you can easily see its status, what the milestones are, if the release is blocked for some human intervention, and the Release's progress." (Layer A)
- **Path to Production view**: "For each stage in the Release pipeline, the Path-to-Production view shows the applications or microservices deployed in the release, the deployed versions, and the environments to which they are deployed... including... the snapshots, and the environments that are not in compliance with the bill of materials throughout the Release." (Layer A)
- **Control**: "CloudBees CD/RO keeps track of the data from the multiple teams involved in the release. The Release feature captures, validates, coordinates, and tracks all the details in one place, where everyone can access the Release definition, bill of materials (which applications or microservices to release), the pipeline controlling the release process, and environment to use across stages, approval conditions, release configurations, and so on." (Layer A)
- **Release manifest / Release definition** specifies: the pipeline controlling the process; the applications or microservices in the pipeline; how to deploy tasks/processes; where versioned objects will be deployed (multiple-tiered environments); "The approvers for manual process steps, manual tasks, and pipeline gates." (Layer A)
- **Immutability**: "Once a release is ended, the release becomes immutable, and options to modify properties of the release run, and its pipelines, become inactive. This ensures an accurate record of the release for auditing and archiving purposes." (Layer A)
- Multiple pipeline runs in a release (launch multiple instances, pass parameters, select stages). **Release scheduling**: "You can create schedules for releases... each team can set up their own independent schedules that run on a particular stage. They can set a start date and can also make a release recurring (for example, daily or weekly)." Release and environment reservations calendar exists as a surface. (Layer A)
- Pipelines have stages and entry/exit gates, manual tasks, approval conditions; native CI integration. (Layer A — pipeline section index)

## Product C — Digital.ai Release (Tier 2 only)

### Key observations

- Docs home one-liner: "Release: Empower developer teams to seamlessly release and deploy software on a large scale across hybrid environments, all while ensuring that compliance and security requirements are effectively in place." (Layer A, docs home)
- Product page: "Digital.ai Release serves as the foundation of DevSecOps, enabling you to create a self-service catalog with predefined workflows to release and deploy applications reliably at scale. Create simple software release templates that developers can reuse, automate application deployment, and weave in security protocols and governance..." (Layer A, marketing-tier)
- Capability claims: "Optimize software release with automated quality checks, change approvals and release notes"; "Manage complex release dependencies across many teams to proactively remediate issues"; "Help different teams transition to continuous delivery by offering release templates based on their maturity level"; "Ensure thorough audits with a simple one-click access to detailed audit and traceability reports"; "Achieve compliance with industry regulations by incorporating mandatory reviews and approvals into your process"; "Seamlessly integrate with your existing DevOps tools and systems". (Tier 2 — capability claims, not operational detail)
- Operational docs unreachable (transport errors). Lifecycle/phase machinery asserted at Tier 2 strength only. No numeric claims drawn from this product.

## Product D — Octopus Deploy (boundary pole, CD)

### Key observations (Tier 1)

- "A release is a snapshot of the deployment process and the associated assets that existed when you created the release. These assets include scripts, references to package versions, and variables... Each release gets assigned a version number. You can deploy releases as often as necessary..." (Layer A)
- Surrounding concepts: lifecycles, channels, guided failures, prevent release progression, issue tracking (Jira/GitHub/Azure DevOps), release versioning, deployment changes, environment timeline, release notes. (Layer A — section index)
- Interpretation: in the CD pole, "release" = versioned deployment snapshot bound to one project's deployment process. No cross-team coordination machinery, no release calendar, no gates/readiness lifecycle at the release level (progression rules exist but are deployment-environment rules). This is the CD pass's documented territory ("executes deployments against environments → CD").

## Product E — GitLab Releases (boundary pole, dev platform)

### Key observations (Tier 1)

- "Create a release to package your project at critical milestones. Releases combine code, binaries, documentation, and release notes into a complete snapshot of your project. When a release is created, GitLab automatically tags your code, archives a snapshot, and generates audit-ready evidence." (Layer A)
- Release = Git tag + title + release notes + associated milestones + asset links; created via CI/CD job, UI, or API; upcoming/historical release badges; deploy freeze windows ("Prevent unintended production releases during a period of time you specify"); release permissions; group-level release metrics. (Layer A)
- Interpretation: release-as-version-snapshot inside a dev platform. Single-project scope; no cross-team coordination, no phases/gates/readiness machinery, no release calendar (deploy freeze is a CI safety window, not a release plan). A capability of the dev platform, not the Type.

## Cross-product Comparison

| Dimension | Planview Release | CloudBees CD/RO Release | Digital.ai Release (T2) | Octopus (boundary) | GitLab (boundary) |
|---|---|---|---|---|---|
| Release object | persistent release record (Enterprise/Project/Independent) with ID, dates, status, stakeholders | release definition/manifest + bill of materials + pipeline binding | release templates → releases | versioned snapshot of deployment process+assets | Git tag + notes + assets + milestones |
| Binds constituent items | changes, deployments, environments, systems, activities | applications/microservices + versions + pipeline runs | changes/approvals/release notes (claimed) | package references, scripts, variables | milestones (issues), assets |
| Lifecycle machinery | phases + gates + criteria + approvals; status | planned/active/completed; run/end; gates in pipeline | mandatory reviews/approvals (claimed) | progression rules per environment | released date only |
| Coordination machinery | release calendar, blockouts, environment booking, stakeholders, conflict identification, child-release push | multi-team coordination, dependencies between applications, release scheduling, environment reservations calendar | dependencies across many teams (claimed) | none | none |
| Execution posture | deployment plans/runbooks with approval workflows; orchestrate automated + manual activities; CDP module | executes deployments via its own automation; release pipeline runs | automates deployment (claimed) | executes deployments | CI job creates release; deployment separate |
| Audit/record | audit history on demand | ended release immutable for audit/archiving | audit/traceability reports (claimed) | release notes/history | release evidence snapshot |
| Post-release | PIR (post-implementation review) | release summary | — | — | — |
| Templates | release templates with phases/gates | reusable pipelines | release templates by maturity | — | — |

**Layer B findings (cross-product commonality, Planview + CloudBees + Digital.ai Tier-2):**

1. The release is a persistent, individually identified record that binds the delivery's constituent items (changes, applications/deployments, environments) and carries its own status/progress. (A: Planview, CloudBees; B: + Digital.ai claims)
2. The release advances through a managed lifecycle driven by gates/criteria/approvals and completion of constituents. (A: Planview phases/gates/criteria, CloudBees planned/active/completed + pipeline gates; B: + Digital.ai "mandatory reviews and approvals")
3. The release is coordinated against a schedule: calendars, start dates, recurring cadences, blackout/freeze windows, dependencies between contributing applications/teams, stakeholder notification. (A: Planview calendar/blockouts, CloudBees scheduling/reservations calendar; B: + Digital.ai "complex release dependencies across many teams")
4. Release templates / reusable release process definitions are standard. (A: Planview Release Templates, CloudBees reusable pipelines; B: Digital.ai release templates)
5. Audit/traceability of the release is a first-class outcome; ended/completed releases become a fixed record. (A: Planview audit history, CloudBees immutability; B: Digital.ai audit reports)
6. Integration with the surrounding toolchain (issue trackers, CI, ITSM) rather than replacement. (A: Planview Integration Hub/API, CloudBees native CI integration + issue tracking; B: Digital.ai "integrate with your existing DevOps tools")

**Layer C (canonical inference):** the Type's defining structure is the release as a governed coordination vehicle — not the deployment, not the change, not the version tag.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (three jointly-held structures)

1. **The release as managed record of record** — a persistent, individually identified release (named, commonly versioned) that acts as the coordination container: the changes, deployments, and/or work items intended to go out together attach to it, and it carries the release's own status, dates, and ownership. Remove → version labels/milestones in a tracker, or change tickets and deployment records with no vehicle.
2. **The managed release progression** — the release advances through a defined lifecycle (planned → in progress → released/deployed → completed/closed) driven by gates/criteria/approvals and by the completion of its constituent items; the progression machinery is what makes it "managed" rather than a label. Remove → a static version tag with a released date.
3. **The coordination surface across contributing streams** — the release is planned and scheduled against the organization's delivery constraints: calendar placement, dependencies/sequencing between contributing teams/applications/systems, blackout/freeze windows, stakeholders to inform. Remove → single-pipeline deployment automation (CD territory) or a shared calendar (PPM territory).

Jointly-held load-bearing tests:
- 1 alone = tracker milestone / version label (GitLab pole).
- 2 without 1 = generic workflow with no release identity.
- 3 without 1+2 = a delivery calendar with no managed vehicle.
- 1+2 without 3 = single-team release tracking (tracker fix-versions with status).
- 1+3 without 2 = a release schedule nobody advances.
- 2+3 without 1 = coordination process with no record.

### L1 — Common Mature Structure

- Release templates / reusable release process definitions
- Phases & gates with criteria/approval checkpoints
- Release calendar & scheduling (start dates, recurring cadence, blackout/freeze windows)
- Changes/work items linked to the release
- Deployment plans / runbooks attached to the release (activities, checkpoints, issues)
- Environment dimension (reservations/bookings against the release schedule)
- Stakeholders, ownership, notifications
- Status/progress dashboards (release list, planned-vs-actual, path-to-production)
- Audit/traceability; ended-release immutability
- Post-release review (PIR / release summary)
- Toolchain integration (issue trackers, CI, ITSM) rather than replacement

### L2 — Variant / Optional Structure

- Automation depth: planning-centric (delegates execution to CD tools) ↔ execution-coupled orchestration (runs deployment activities itself). Variant axis, not a Type split — both poles hold all three L0 legs.
- Release hierarchy shapes: parent/child release trees (Planview Enterprise→Project→Independent) vs single release with multiple pipeline runs (CloudBees).
- Environment-management depth: full test-environment booking machinery (TEBR/TECR-class) vs light environment reservations.
- ITSM-embedded form: release management as a module inside an ITSM suite, release records tied to change requests (ServiceNow-class; documented second-hand via the it-change-management pass).
- Methodology framing: cadence/trained releases vs continuous-delivery releases (CloudBees explicitly supports both in one platform).
- Value-stream analytics / flow metrics dashboards (Planview-class module).

### L3 — Vendor-specific (research notes only)

- Planview: TEBR/TECR, System/Environment Impact Matrices, Activities Kanban, Initiative Management, Blockout types, Deployment Plan RACI, Command Centre, Health Check Dashboard.
- CloudBees: bill of materials, path-to-production view, release manifest terminology, Groovy DSL process-as-code, personas, per-stage team schedules.
- Digital.ai: Intelligent Change Risk Prediction, self-service catalog, guided workflows, DevSecOps framing, fast-lane for low-risk changes.
- GitLab: release evidence, permanent links, RSS feed, protected tags, deploy-freeze crontab windows.
- Octopus: channels, tenants, guided failures, lifecycle/channel progression rules.

## Boundary Findings

- **vs Continuous Delivery Platform** (processed 2026-09-07): CD executes deployments against named environments and keeps the deployment record; Release Management coordinates/plans/governs releases as management objects. Octopus's "release" (deployment-process snapshot, no coordination machinery) demonstrates the CD-side meaning of the word. CloudBees CD/RO contains both deployment automation and a Release module — suite packaging, not Type fusion. Joint review DISCHARGED from this side: the CD pass's test ("executes deployments against environments → CD; coordinates/plans/governs releases as management objects → Release Management") holds; the two Types interlock (release management plans and gates what CD executes) but neither subsumes the other. "Release orchestration" vocabulary straddles both — Octopus/CloudBees/Digital.ai all use it; vocabulary alone does not merge the Types.
- **vs IT Change Management** (processed 2026-09-08): change management governs each modification individually (assess→authorize→schedule→implement→review per change); release management aggregates changes/deployments into release vehicles and coordinates them. Planview Release carries a Change object linked to releases (the change's authorization lives in change/ITSM systems; the release coordinates them). The it-change-management pass's expected seam (aggregation-and-coordination vs per-change authorization/record) is confirmed from this side. ServiceNow documents release stages inside change workflows — module packaging inside ITSM, recorded as variant.
- **vs Issue Tracker / dev-platform release versions** (GitLab/Jira-class): release-as-version-snapshot with notes/assets/milestones; single-project scope; no gates/readiness lifecycle, no cross-team coordination, no calendar. A capability of another Type, not this Type. The word "release" is shared; the object is not.
- **vs Feature Flag Management Platform** (processed 2026-09-08): flags decouple feature release from code deployment; object of record = flag. Release management's object of record = the release vehicle. Complementary (a release may ship flag-gated features), not overlapping.
- **vs Project Portfolio Management**: PPM manages projects/portfolios of work; release management manages release vehicles of software delivery with delivery-specific bindings (changes, deployments, environments). Planview Release lives inside Planview's portfolio platform and has an Initiative Management module — packaging adjacency, not identity.
- **vs Software Delivery Governance Platform** (§12 sibling, unprocessed): governance policy enforcement across the delivery toolchain vs the release vehicle as center. Flag for that pass; expected seam: policy/rules layer vs release-object coordination layer.
- **vs Test Environment Management**: Planview bundles deep environment booking machinery (TEBR/TECR) beside release management; environment management is a sibling concern (its own record base and booking loop), bundled in the same product here.
- **"去掉什么就变成另一个 Type" 判据**: remove the release container → change tickets + deployment records with no vehicle (IT change + CD); remove the managed progression → version label in a tracker (dev-platform capability); remove the coordination surface → single-pipeline deployment automation (CD); remove the software-delivery binding → generic milestone management (PPM).

## Historical / Market-Sample Check (§24)

- Would older products fit L0? ITIL-era release management (2000s) and the first release-orchestration generation (XL Release 2010s, UrbanCode Release 2010s, Plutora 2010s): release records bundling changes, release calendars, CAB-style approval gates, release notes, post-release review — all three L0 legs present with no cloud/AI/K8s machinery. Even the paper-era practice (release schedule board + change list + sign-off gates + typed release notes) satisfies the legs. Check passed.
- Era-sensitive risk handled: "release = big-bang version deployed to production" is NOT in L0; the abstraction is "delivery vehicle for changes/deployments", which covers cadence releases, release trains, and continuous releases (CloudBees explicitly supports both in one platform).
- Regional/platform-native check: sample spans US-commercial SaaS (Planview), US enterprise automation (CloudBees), and open-source/dev-platform poles (GitLab, Octopus); no region-specific structure entered L0.

## Uncertainties

- Digital.ai Release operational docs unreachable (transport errors ×2 on docs.digitalai.com; xebialabs mirror serves only the docs home). Its lifecycle/phase machinery is asserted at Tier 2 strength only; no operational detail drawn from it.
- IBM UrbanCode Release (403×2), ServiceNow (timeout×2), OpenText Release Control (transport error) unreachable — the traditional-enterprise pole and the ITSM-embedded pole are under-sampled. The ITSM-embedded form is documented second-hand via the it-change-management pass's ServiceNow evidence (release stages inside change workflows; releases as change associations).
- Whether "release orchestration" and "enterprise release management" are one Type or two: evidence supports ONE Type with an automation-depth variant axis (both sampled poles hold all three L0 legs; the difference is how much execution the platform performs vs delegates). Recorded as variant axis, not a Type split.
- Planview's environment machinery (TEBR/TECR) depth not fetched page-by-page; treated as bundled sibling capability, not part of the release core.
- No numeric limits, default values, or timing figures from any product were promoted to the final document.

## Final Synthesis

A Release Management Platform is the software-delivery coordination system of record whose defining spine is: a **release** — a persistent, identified delivery vehicle — binds the changes, deployments, and work items intended to go out together; the release advances through a **managed lifecycle** driven by gates/criteria/approvals and constituent completion; and the release is **coordinated** against the organization's delivery constraints (calendar, dependencies between contributing teams/applications, blackout/freeze windows, stakeholders). Around that spine, mature products add templates, phases/gates machinery, deployment plans/runbooks, environment reservations, dashboards, audit/immutability, post-release review, and toolchain integration. The Type ends where deployment execution begins (CD), where per-change authorization begins (IT change management), where the version snapshot begins (tracker/dev-platform release features), and where feature-level release control begins (feature flags). The market realizes the Type on an automation-depth axis from planning-centric enterprise release management to execution-coupled release orchestration — one Type, two postures.
