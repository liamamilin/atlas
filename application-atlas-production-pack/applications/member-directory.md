# Member Directory

## Overview

A **Member Directory** is a membership organization's searchable roster of its own members, held as individual member profiles and maintained so that specific members can be found, identified, and reached.

It answers a problem every membership organization has: once an organization grows beyond a handful of people, nobody can reliably find who belongs, how to reach them, or what each member does. The directory is the organization's deliberate publication of its own membership — selecting who appears, what information shows, and who is allowed to see it.

The defining core is small:

```text
The organization's member roster (population anchored in membership)
└── Standing member profile (identity, contact/reach, descriptive attributes)
    └── Lookup organization (search / filter / browse over profile attributes)
    └── Governed publication (which members, which fields, to which audience)
```

Everything else commonly seen — self-service profile editing, map views, public "find a member" sites, photo galleries, print output, featured listings — is standard capability in mature products but is not what makes a member directory a member directory. A printed congregational photo directory and a chamber of commerce's public business directory satisfy the same core.

## Users & Context

The setting is any organization whose value depends on its members being findable to each other or to the public: congregations, professional and trade associations, chambers of commerce, alumni bodies, clubs and societies.

**Primary users:**

- **Members** — look up fellow members to contact them (call, email, text, get directions), and maintain their own entry so others can find them. In members-only directories this is the whole audience.
- **Organization staff / administrators** — configure the directory (scope, fields, audience), manage the roster that feeds it, approve member-submitted changes, and produce outputs (web, app, print, exports).

**Secondary users:**

- **Volunteers/editors** — in many congregations and small associations, delegated staff help keep entries current and review member submissions.
- **Outside visitors** — when the organization runs a public-facing directory ("find a member business", "find a certified professional"), prospective customers and the general public search it and contact members, usually without seeing raw contact details.

The typical deployment is one organization's directory, either as a standalone service or as a named module inside a membership management system or association management system.

## Core Model

### The defining core

Three structures. Remove any one and the product stops being a member directory.

- **Membership-anchored population.** The population is the organization's own membership — people, families/households, and/or member organizations. Entries exist because of a membership relationship: inclusion is gated by the organization's membership records (application approval, standing, member type), and updates in the membership system flow into the directory. This is what separates a member directory from a general directory of businesses, places, or people in the open world: nobody "signs up" into a member directory from outside; they belong first.

- **Standing member profiles built for lookup and reach.** Each member carries a persistent structured profile. Its typical content:
  - *identity* — name (and family/household linkage where used), photo or logo
  - *reach attributes* — phone, email, address, website, social links
  - *descriptive attributes* — member type/category, areas of expertise, custom fields, bio/organization description
  - *standing markers* — member status or type, join/since date
  
  The reach attributes are the point: the directory exists so a specific member can be found **and contacted** — directly, or through a relayed contact form.

- **Lookup organization.** The directory organizes retrieval over profile attributes: search by name or keyword, filters by category, member type, custom field, or location, category-based browsing, alphabetical ordering, and commonly a map view. This is the "directory" in the name — the difference between a governed roster and a pile of member files.

- **Governed publication.** The organization decides which members appear, which attributes appear, and to whom: an entire directory may be public or members-only, contact fields may show or hide per audience, and individual members may hold consent rights over their own entry (stay listed but hide contact info, hide address, opt out entirely). Publication is an act the organization performs, not a data dump.

### Standard capabilities in mature products

Mature products commonly provide most of the following; none are definitional:

- **Member self-maintenance** — members update their own profile, either by direct editing through the member portal or by submitting changes that staff approve before they take effect. Photos are the most commonly submitted item.
- **Dual audience postures** — the same organization may run a members-only directory (a membership benefit for finding each other) and a public directory (a promotion channel for member businesses).
- **Multiple directories per organization** — scoped subsets: new members, a member type, a committee, a chapter, a church program group — each with its own audience and settings. Several products support such scoped sub-directories.
- **Contact protection** — in public postures, member email addresses are typically not shown directly; a contact form relays messages, and displayed emails may be shielded against harvesting.
- **Print and export companions** — printable PDF/booklet output (with photo layouts), and CSV import/export for mail-merge and labels.
- **Map view** — members geocoded and browsable by location with distance or area filters.
- **Featured or promoted listings** — paid or benefit-linked prominence, often a non-dues revenue source for the organization.
- **Admin roles and review queues** — administrator, editors/volunteers, approval of member submissions.

### One structure, several implementations

The core is conceptual; products realize it differently:

```text
Concept:  Membership-anchored population
Realizations:  roster maintained directly by staff · derived from the
               membership database (updates flow in automatically) ·
               member accounts created at join time

Concept:  Member access to the directory
Realizations:  email listed in the directory + secure sign-in link ·
               member-portal login · mobile-app registration

Concept:  Lookup organization
Realizations:  alphabetical/category listings · keyword + faceted search ·
               geocoded map views · print booklet order

Concept:  Governed publication
Realizations:  per-directory public vs members-only setting · tiered access
               by membership level · per-member hide/opt-out settings ·
               staff approval of member-submitted changes
```

## How It Works

### Population flows from membership

Members enter the directory through the organization's membership machinery, not through a public submission form: staff add or import them, they join and are approved, or they are auto-included by member type or group. Where the directory derives from an approval-gated roster, unapproved members are not displayed; members can also be hidden or removed individually, and some products treat membership standing as a listing prerequisite. In products where the directory derives from the membership database, a change to the roster (new member, type change) is reflected in the directory without separate work.

### Configure and publish

An administrator scopes the directory (which members — all, a type, a group), chooses the audience (public, members-only, or restricted to specific member groups), selects which profile fields render, sets ordering (alphabetical, category-based, or randomized fairness ordering in some products), and can generate print or PDF output. The same organization commonly maintains several directories with different audiences from the same roster.

### The lookup loop

```text
Visitor (member or public) opens the directory
→ searches by name/keyword, applies filters (category, type, location)
→ scans result cards (photo/logo, name, member type, location)
→ opens a member's profile page
→ acts on reach attributes: call, email, text, directions,
  website link — or submits a contact form that relays the
  message without exposing the member's email address
```

This loop is the directory's reason to exist: find a specific member and reach them.

### The maintenance loop

```text
Member life event (new address, new photo, name change)
→ member edits own profile in the portal/app, or submits a change
→ staff review (in moderated setups) and approve or reject
→ change propagates to the directory's surfaces: web listing, member
  apps, print output where one is maintained
```

Staff also maintain directly: bulk import of member data with field mapping, exports for mailing labels, and corrections at the record level. A directory that cannot be kept current fails at its one job, so the maintenance loop is as central as the lookup loop.

## Interfaces

### Directory search / list surface

The public or member-facing entry surface.

- Purpose: find members by what you know (name, what they do, where they are).
- Typical information: result cards with photo/logo, name, member type/category, location; view toggles (list/map, category views).
- Primary actions: search, filter, open a profile, toggle views.

### Member profile page

The unit of the directory.

- Typical information: photo/logo, name and family/organization linkage, contact details (shown per audience rules), address (full or city/state only), member type, description/bio, custom fields, links, sometimes join/since date, gallery, and related people (e.g., company staff).
- Primary actions: contact the member (direct or relayed form), directions, website link; for the member themselves: edit/submit updates.

### Map view

A location-organized alternative to the list: members as pins, area/distance filters, pin → profile.

### Directory administration

The staff surface.

- Purpose: control scope, audience, fields, ordering, and outputs; manage the roster feeding the directory.
- Typical information: directory settings, member record list with status/type/join-date attributes, approval queue of member-submitted changes.
- Primary actions: create/configure directories, add/import members, approve/reject submissions, hide/exclude records, export, generate print/PDF.

### Member's own profile

Where subject participation happens: the member edits or submits updates to their own entry and, in many products, sets their own visibility preferences (hide contact info, hide address).

## Important Rules / Behaviors

- **Inclusion follows membership standing.** Being listed is a consequence of belonging: members appear once they are approved or in good standing, and records can be hidden or removed at the member level. Where the directory derives from an approval-gated roster, unapproved records are not displayed; some products also reflect standing in ordering itself (dues-paying or benefit-holding members listed ahead of others).
- **Per-member consent overrides directory defaults.** A member's own hide-contact/hide-address/opt-out setting typically wins over what the directory or member type would otherwise show. The organization may allow members to set these preferences themselves.
- **Audience gating is structural.** A members-only directory is invisible to the public; a public directory may still hide contact fields so that only logged-in members can actually reach the member — turning the directory into a member benefit.
- **Email is the most protected attribute.** Public postures commonly replace displayed email with a relayed contact form, and displayed addresses may be shielded from automated harvesting; several products explicitly frame this as anti-spam compliance.
- **Moderation preserves accuracy.** Where members submit their own changes, submissions route to administrators/editors for approval rather than publishing immediately.
- **The directory mirrors the roster, not the other way around.** The authoritative membership record lives in the membership system; the directory is the published, lookup-organized view of it. Fix membership data at its source.

## Variants

- **Congregation photo directory** — families/households as units, photo-forward, print/booklet heritage, closed member audience, moderated member submissions. The most product-specialized variant.
- **Chamber / business member directory** — member organizations as entries with logos, descriptions, categories ("find a member business"), often public-facing with featured listings, deals, and lead routing for members.
- **Association members-only directory** — member-to-member networking: find colleagues by expertise, section, or location; access strictly a member benefit.
- **Alumni directory** — population anchored in the institution's graduate register rather than dues-paying membership.
- **Standalone vs embedded packaging** — dedicated directory products exist, but the most common realization is a named module inside a membership management or association management system, or a directory widget embedded in the organization's website.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Directory Application | parent structure | organizes entries of any defined entity class (businesses, places, people of the open world) curated by an operator; a member directory's population is bound to an organization's membership, its subjects participate in maintaining entries, and publication is membership-aware (audience gating, standing-driven prominence, consent) |
| Listings Platform | family neighbor | a listing is a current, expiring offer (job, rental, item); a directory entry is a standing record of a member that persists while membership holds |
| Member Community Platform | sibling | an interaction container (discussions, participatory spaces) that *includes* a profile directory as one capability; strip the participation and the directory remains complete |
| Member Portal | sibling | the member's own self-service surface (account, payments, preferences); the directory is the organization-facing lookup surface over the roster — they meet where members edit their profiles |
| Membership Management System / AMS | containing system | owns the member registry, dues, and renewal lifecycle; the directory is one published surface over that registry, either built in or standalone |
| Congregation Membership Management | sibling | holds and administers the membership roll (status, households, milestones); the directory is one of its outputs — a standalone member directory does not administer the roll |
| Social Profile Network | adjacent | profile networks center on self-authored presentation, follow graphs, and feeds; member directory prominence comes from membership standing and organization settings, not from a social graph |
| CRM / Contact Discovery tools | different object | CRM holds relationship and workflow records; contact-discovery platforms prospect the open market — a member directory neither manages relationships nor finds prospects, it publishes the org's own people |

The most consequential boundary is with the general Directory Application: the lookup machinery is shared, and the difference is the population's provenance (membership relationship vs operator curation) together with the governance and participation wrapped around it.

## Representative Products

- **Instant Church Directory** — standalone congregational photo directory: family/individual records, print/PDF companion, member mobile apps, moderated member submissions
- **MembershipWorks** — all-in-one membership software whose member directory module covers tiered access, keyword/geo/faceted search, and contact-relay protection
- **Brilliant Directories** — directory-website platform combining member accounts, membership plans, and public directory publishing
- **Novi AMS** — association management system whose member directory module derives directories from member groups, with standing-based ordering and per-member privacy overrides

Together these span the standalone/module packaging split, the closed-members/public-audience postures, and the congregation/association/chamber customer segments.

## Sources

Research date: **2026-09-08**

- Instant Church Directory — https://www.instantchurchdirectory.com/ ; https://www.instantchurchdirectory.com/church-directory-features
- MembershipWorks — https://membershipworks.com/ ; https://membershipworks.com/member-directory/
- Brilliant Directories — https://support.brilliantdirectories.com/support/solutions/articles/12000045147-my-members-search-members-overview ; https://support.brilliantdirectories.com/support/solutions (knowledge base)
- Novi AMS — https://help.noviams.com/articles/6957821970-a-guide-to-the-member-directory ; https://help.noviams.com/articles/5302661912-cheat-sheet-member-directory-privacy-and-data-protection ; https://help.noviams.com/articles/2120182893-add-remove-or-rearrange-custom-field-values-on-directory-profile-pages ; https://help.noviams.com/collections/5740287562-member-directory

> Sourcing limitation: two widely cited vendors could not be reached during research (Wild Apricot's help and feature pages returned errors; the alumni-platform pole was unreachable). Claims about field-level visibility controls rest on the three products whose documentation was directly verified, and the alumni variant is described only as a market structure, not from product documentation. Precise numeric limits and vendor-specific defaults are intentionally not asserted.
