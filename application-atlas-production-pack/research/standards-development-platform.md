# Research Notes — Standards Development Platform

## Research Goal

Understand what a Standards Development Platform is, how it works, who uses it, and what distinguishes it from adjacent application types (committee management, document management, certification management).

## Initial Boundary

A Standards Development Platform is software used by Standards Development Organizations (SDOs) — such as ISO, IEEE, ASTM, IETF, W3C, ANSI-accredited bodies — to manage the full lifecycle of creating, reviewing, approving, and publishing technical standards.

Neighboring types:
- **Committee / Board Management** — governance of people and meetings, not the technical content lifecycle
- **Document Management / CMS** — generic document storage and versioning, without the standards-specific lifecycle and consensus machinery
- **Certification Management** — certifying people/products against standards, not creating the standards themselves
- **Policy Management** — internal organizational policies, not consensus-based technical standards

## Research Questions

1. What is a "standard" in this context? (document, specification, code, protocol)
2. What is the lifecycle of a standard? (proposal → draft → review → ballot/vote → approval → publication → revision/withdrawal)
3. Who participates? (technical committees, working groups, editors, voters, staff)
4. How does consensus work? (formal ballot, comment resolution, approval thresholds)
5. What are the key objects? (standard/project, committee, working group, member/organization, comment, ballot, document version)
6. How does collaboration work on drafts?
7. What happens after publication? (maintenance, revision, withdrawal)

## Representative Products

1. **ISO/IEC OSD (Online Standards Development)** — The platform used by ISO and IEC for collaborative standards development. Built on FontoXML. This is the largest and most documented platform, used by thousands of working groups worldwide.
2. **IEEE SA myProject/myBallot** — IEEE Standards Association's tools for standards development and balloting. Used by hundreds of IEEE standards committees.
3. **ASTM SpecBuilder** — ASTM's platform for collaborative document development and balloting, also offered as a white-label product to other SDOs.
4. **IETF Datatracker** — The IETF's tool for tracking Internet-Drafts and RFCs through the standards process. Open-source, publicly accessible.
5. **Stanza (InfoBeans)** — A commercial platform for SDOs, used by organizations like ICC (International Code Council). Adheres to ANSI guidelines.

## Sources

### ISO/IEC OSD
- ISO Helpdesk Knowledge Base: https://helpdesk-docs.iso.org/article/649-what-is-online-standards-development-osd
- ISO OSD Permissions: https://helpdesk-docs.iso.org/article/655-osd-permissions
- CEN OSD Guidance: https://boss.cen.eu/reference-material/guidancedoc/pages/drafting-in-osd/
- Fonto case study: https://www.fontoxml.com/case-study-online-standards-development/
- ANSI OSD page: https://www.ansi.org/osd/online-standards-development-platform

### IEEE SA
- IEEE SA eTools: https://standards.ieee.org/develop/etools/
- IEEE SA Balloting Process FAQs: https://standards.ieee.org/faqs/balloting-process/
- IEEE SA Standards Board Operations Manual: https://standards.ieee.org/about/policies/opman/sect5/
- IEEE SA Quick Reference Guide: https://standards.ieee.org/wp-content/uploads/import/documents/other/ieee_sa_toolkit.pdf

### ASTM SpecBuilder
- ASTM SpecBuilder page: https://www.astm.org/standards-and-solutions/enterprise-solutions/specbuilder

### IETF Datatracker
- IETF Datatracker: https://datatracker.ietf.org/
- IETF Datatracker About: https://datatracker.ietf.org/release/about
- RFC 6175 (WG Datatracker Requirements): https://www.rfc-editor.org/info/rfc6175/

### Stanza (InfoBeans)
- Stanza product page: https://infobeans.ai/stanza/
- InfoBeans SDO page: https://infobeans.ai/standards-developing-organizations/

### W3C Process
- W3C Process Document: https://www.w3.org/policies/process/
- W3C Recommendation Track: https://www.w3.org/2014/05/Process-20140506/tr

### Other
- NIST Sources Sought for Standards Development Platform: https://www.highergov.com/contract-opportunity/standards-development-licensed-platform-subscripti-nist-sco-25-ss01-r-b5c0d/
- Edaptive Technologies: https://www.edaptivetechnologies.com/
- Metanorma: https://www.metanorma.org/

## Product A: ISO/IEC OSD (Online Standards Development)

### Key observations

**Evidence Layer: A (Directly Observed)**

- The OSD is a web-based XML editor (built on FontoXML) that replaces Word-based standards development.
- It covers the full lifecycle: authoring → member commenting → editing for publication.
- Roles are defined in the Global Directory: Officer (LEADER), Committee member/WG expert (OSD COMMENTER), Liaison representative, Partner, Document monitor, Voter (OSD VOTER).
- Permissions change based on the project stage:
  - **Authoring/drafting stages (00.00–20.99)**: Officers can write content, accept/reject changes, run quality checks. WG experts can comment.
  - **Ballot stages (10.20, 30.20, 40.20, 50.20)**: Voters can view national comments, edit/delete their comments, resolve comments.
  - **Enquiry/Approval stages**: Leaders can export to PDF.
- Comments can be added anywhere in the text, typed as General, Editorial, or Technical, and can include a proposed change.
- Every comment gets a unique identifier that persists across stages.
- Content quality checks are built in (validates against ISO/IEC Directives Part 2).
- The platform is harmonized between ISO and IEC, with CEN/CENELEC also adopting it.
- As of 2025, OSD is the default tool for all new ISO/IEC projects.
- National Standards Bodies (NSBs) can use Option A (direct commenting in OSD) or Option B (upload national comments from a template).
- The platform supports real-time collaboration, version control, and track changes.

**Lifecycle stages observed:**
- Preliminary (00.xx): New work item proposal
- Preparatory (20.xx): Working draft
- Committee (30.xx): Committee draft
- Enquiry (40.xx): Draft International Standard (DIS)
- Approval (50.xx): Final Draft International Standard (FDIS)
- Publication (60.xx): International Standard

## Product B: IEEE SA myProject/myBallot

### Key observations

**Evidence Layer: A (Directly Observed)**

- myProject is the central system for managing IEEE standards projects.
- Key functions: manage activity profile, submit PARs (Project Authorization Requests), join ballot groups, vote and comment.
- The standards development process:
  1. **PAR submission**: A new project is proposed and authorized by NesCom (New Standards Committee).
  2. **Working Group development**: WG members collaborate on the draft using iMeet Central, WebEx, Listserv, etc.
  3. **SA Ballot invitation**: When the draft is ready, a ballot invitation is opened (minimum 15 days, typically 30 days) to form the ballot group.
  4. **MEC (Mandatory Editorial Coordination)**: IEEE staff review the draft for editorial compliance.
  5. **SA Ballot**: The ballot group votes (minimum 30 days). Requires 75% response rate and 75% approval rate.
  6. **Recirculation ballot(s)**: If substantive changes are made, a recirculation ballot (minimum 10 days) is required.
  7. **RevCom review**: The Standards Review Committee verifies procedures were followed.
  8. **SASB approval**: The Standards Board approves the standard.
  9. **Publication**: The standard is published on IEEE Xplore.
- Ballot groups must be balanced: no single interest category can comprise more than 1/3 of the group.
- Votes: Approve, Do Not Approve (with comment), Abstain.
- Comment Resolution Group (CRG) reviews all comments and provides disposition (Accepted, Revised, Rejected).
- Public Review runs simultaneously with the initial SA Ballot (60 days).

**eTools ecosystem:**
- myProject: Project management and balloting
- iMeet Central: Collaboration workspace
- Mentor: Secure document repository
- IEEE SA Open: Open source development platform
- Attendance Tool: Meeting attendance tracking
- Standards Dictionary: Database of terms
- WebEx, Listserv, WordPress: Supporting tools

## Product C: ASTM SpecBuilder

### Key observations

**Evidence Layer: A (Directly Observed from product page)**

- SpecBuilder is a collaboration and balloting platform for developing internal specifications, codes, and regulations.
- Key features:
  - Single platform for drafts, comments, voting, and supporting documents
  - Task groups and subgroups with discussion tracking
  - Customizable ballot and voting parameters
  - Automated ballot progress tracking and alerts
  - Document history and archive
  - Reference linking to ASTM standards
  - Publishing and sharing of final documents
- Used by organizations like PPI (Plastics Pipe Institute) and API (American Petroleum Institute).
- Built on the same platform ASTM uses for its own standards development.
- Offered as a white-label product for other SDOs and organizations.

## Product D: IETF Datatracker

### Key observations

**Evidence Layer: A (Directly Observed)**

- The Datatracker is the primary day-to-day front-end to the IETF database.
- It tracks: Internet-Drafts (I-Ds), RFCs, working groups, meetings, agendas, minutes, presentations.
- Key objects:
  - **Internet-Draft**: A document under development, with states (Active, Expired, Replaced, Withdrawn).
  - **Working Group**: A group developing standards, with chairs, secretaries, and members.
  - **RFC**: A published standard, with a number and status.
- WG Chairs can input and update the status of WG I-Ds using defined states and annotation tags.
- Document shepherds track documents through the IESG evaluation process.
- The Datatracker is open-source (Django-based), publicly accessible.
- IETF process is more informal than ISO/IEEE: consensus is reached through mailing list discussion and "rough consensus" rather than formal balloting.

## Product E: Stanza (InfoBeans)

### Key observations

**Evidence Layer: A (Directly Observed from product page)**

- Stanza is a comprehensive solution for committee management, standards development, voting, and balloting.
- Adheres to ANSI guidelines.
- Key capabilities:
  - **Committee Management**: Attendance & participation tracking, calendar, events & meeting management
  - **Comments Management**: Status tracking, real-time conflict resolution
  - **Membership Management**: Approvals & tenure limits, expiration & reappointments, roles & access management
  - **Standards Management**: New requests & revisions, withdrawal & merges, reinstatements & splits, publishing
  - **Balloting**: Criteria definition, circulation & approval, weighted balloting, procedural review, secret ballot
  - **Document Management**: Real-time collaboration & co-authoring, shared repositories, flexible workspaces
- Used by ICC (International Code Council) and other ANSI-accredited SDOs.
- Supports weighted balloting (deriving consensus from a variety of sources).
- Integration with any document management platform.

## Cross-product Comparison

| Feature | ISO/IEC OSD | IEEE SA myProject | ASTM SpecBuilder | IETF Datatracker | Stanza |
|---|---|---|---|---|---|
| **Primary user** | WG members, committee managers, voters | WG chairs, ballot groups | Standards developers, committee members | WG chairs, authors, IESG | Committee members, staff |
| **Document format** | XML (NISO STS) | PDF/Word | Word/PDF | Plain text (I-D format) | Word/PDF |
| **Collaborative editing** | Yes (real-time) | No (external tools) | Yes | No (external tools) | Yes |
| **Commenting** | In-document, typed (General/Editorial/Technical) | Via ballot system | In-document | Mailing list + tracker | In-document |
| **Balloting/Voting** | Via separate ballot system | Integrated (myBallot) | Integrated | Informal (rough consensus) | Integrated |
| **Lifecycle stages** | 6 stages (Preliminary → Publication) | PAR → WG → Ballot → RevCom → Publish | Configurable | I-D → RFC | Configurable |
| **Role-based permissions** | Yes (Officer, Commenter, Voter, Reader) | Yes (Chair, Member, Voter) | Yes | Yes (Chair, Author, Shepherd) | Yes |
| **Content quality checks** | Yes (ISO Directives) | MEC review | No | No | No |
| **Public access** | No (members only) | Partial (public review) | No | Yes (fully public) | No |
| **Open source** | No | No | No | Yes | No |

## Canonical Model

### L0 — Defining Invariant

The smallest stable structure without which the Application Type would stop being recognizable:

1. **Standard/Project of record** — A persistent identified record of a standards development effort, carrying scope, owner, and a lifecycle from proposal to publication.
2. **Committee/Working Group** — A group of identified participants (experts, members, organizations) authorized to develop the standard.
3. **Draft document with version history** — The evolving technical content, with tracked changes and versions.
4. **Comment/Feedback mechanism** — A structured way for participants to provide feedback on the draft, with disposition tracking.
5. **Consensus mechanism (ballot/vote)** — A formal or informal process to determine whether the draft has achieved consensus and can advance.

If any one is removed:
- Remove 1 → generic document collaboration
- Remove 2 → individual authoring tool
- Remove 3 → meeting minutes or task tracker
- Remove 4 → document approval without feedback
- Remove 5 → document repository without consensus

### L1 — Common Mature Structure

Capabilities that are very common in mature products but not required to define the Type:

- **Lifecycle stage progression** — Defined stages (proposal, draft, review, ballot, approval, publication) with gates.
- **Role-based permissions** — Different roles (officer, editor, member, voter) with different capabilities at different stages.
- **Comment resolution workflow** — Comments are reviewed, accepted/rejected, and incorporated into the draft.
- **Meeting management** — Scheduling, attendance, agendas, minutes.
- **Document templates and formatting rules** — Ensuring drafts conform to the SDO's style guide.
- **Integration with publication systems** — Handoff to the publishing/distribution platform.

### L2 — Variant / Optional Structure

Features that depend on market segment, geography, or SDO-specific rules:

- **Weighted balloting** — Some SDOs use weighted voting (e.g., by organization size or interest category).
- **Public review** — Some SDOs (IEEE, ISO) have a public review period where non-members can comment.
- **National mirror committees** — ISO members have national committees that consolidate national positions.
- **Patent policy compliance** — Some SDOs require patent disclosures and licensing commitments.
- **Open source development** — Some SDOs (IETF, IEEE SA Open) use open source tools and processes.
- **XML-based structured authoring** — ISO/IEC use XML (NISO STS); others use Word/PDF.

### L3 — Vendor-specific Structure

Product-specific modules, terminology, or branded workflows:

- ISO/IEC: OSD, Global Directory, Projex-Online, NISO STS, FontoXML
- IEEE: myProject, myBallot, PAR, NesCom, RevCom, SASB, MEC
- ASTM: SpecBuilder, Compass
- IETF: Datatracker, Internet-Draft, RFC, IESG, IAB
- Stanza: weighted balloting, ANSI guidelines compliance

## Vendor-specific Findings

### ISO/IEC OSD
- The OSD is built on FontoXML, a commercial XML editor.
- It is being rolled out as the default tool for all new ISO/IEC projects (as of 2025).
- CEN and CENELEC are also adopting the OSD, with some customization for EU directives.
- The platform is harmonized between ISO and IEC, but each organization has its own templates and integrations.

### IEEE SA
- IEEE uses a suite of tools (myProject, iMeet Central, Mentor, etc.) rather than a single integrated platform.
- The balloting process is highly formalized, with specific rules for ballot group balance, response rates, and approval thresholds.
- IEEE SA Open is a separate platform for open source development.

### ASTM SpecBuilder
- SpecBuilder is offered as a white-label product, allowing other SDOs to use the same platform ASTM uses.
- It is simpler than ISO/IEC OSD, focusing on collaboration and balloting without structured XML authoring.

### IETF Datatracker
- The IETF process is more informal than ISO/IEEE, relying on "rough consensus" rather than formal balloting.
- The Datatracker is open-source and publicly accessible.
- It tracks Internet-Drafts and RFCs, but the actual drafting happens in external tools (email, GitHub, etc.).

### Stanza
- Stanza is a commercial platform designed for ANSI-accredited SDOs.
- It supports weighted balloting, which is specific to certain SDO governance models.
- It integrates with external document management platforms.

## Boundary Findings

### vs. Committee / Board Management
- Committee management focuses on governance of people (rosters, attendance, meetings).
- Standards development platforms include committee management but add the technical content lifecycle (drafting, commenting, balloting, publication).
- **Boundary test**: Remove the draft document and consensus mechanism → committee management.

### vs. Document Management / CMS
- Document management focuses on storage, versioning, and access control.
- Standards development platforms include document management but add the standards-specific lifecycle and consensus machinery.
- **Boundary test**: Remove the committee, commenting, and balloting → document management.

### vs. Certification Management
- Certification management focuses on certifying people/products against existing standards.
- Standards development platforms focus on creating the standards themselves.
- **Boundary test**: If the system certifies people/products rather than developing standards → certification management.

### vs. Policy Management
- Policy management focuses on internal organizational policies.
- Standards development platforms focus on consensus-based technical standards developed by external stakeholders.
- **Boundary test**: If the system manages internal policies rather than external consensus standards → policy management.

## Uncertainties

1. **W3C process**: W3C uses GitHub and other tools rather than a single integrated platform. It is unclear whether W3C's tooling constitutes a "Standards Development Platform" or a collection of tools.
2. **Informal vs. formal processes**: Some SDOs (IETF) use informal consensus (rough consensus, running code) while others (ISO, IEEE) use formal balloting. The boundary between "standards development platform" and "collaboration tools" is less clear for informal processes.
3. **National vs. international**: National SDOs may use different tools than international SDOs. The ISOlutions OSD project is adapting the ISO OSD for national use.
4. **Open source vs. proprietary**: Some SDOs use open source tools (IETF Datatracker, IEEE SA Open) while others use proprietary platforms (ISO OSD, Stanza).

## Final Synthesis

A Standards Development Platform is a collaborative platform used by Standards Development Organizations (SDOs) to manage the full lifecycle of creating, reviewing, approving, and publishing technical standards.

The defining core is:
1. A **standard/project** with a lifecycle from proposal to publication
2. A **committee/working group** of identified participants
3. A **draft document** with version history
4. A **comment/feedback mechanism** with disposition tracking
5. A **consensus mechanism** (ballot/vote) to determine approval

The platform supports multiple roles (officers, editors, members, voters) with different permissions at different lifecycle stages. It may include collaborative editing, meeting management, and integration with publication systems.

The key distinction from adjacent types is the combination of technical content lifecycle management and consensus-building machinery. Committee management alone is governance of people; document management alone is storage and versioning; standards development platforms add the structured process of developing consensus-based technical content.
