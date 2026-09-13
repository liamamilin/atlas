# Household Staff Management

## Overview

A **Household Staff Management** application is the employer-side system of record for the people a household employs — nannies, housekeepers, house and estate managers, personal assistants, private chefs, drivers, gardeners, and in-home caregivers. The household itself (a family, principal, estate, or family office, personally or through a manager) uses it to hold each staff member as an individually identified employment record and to run that employment over time: bringing the person on, recording duties, worked time, and leave, administering pay and pay-related records, meeting the obligations that attach to household employment, and retaining the record with controlled access.

The defining structure is small:

```text
Household-employer staff roster of record
└── employment administration loop over each staff member
    (bring on → record work and leave → pay and meet obligations → keep the record)
    anchored in the household-employment regime
```

Everything else commonly associated with the category — automated payroll and tax filings, employee self-service portals, house manuals, insurance, background checks, multi-property estates — is standard capability or variant, not what makes the software this Type. Historically the same job was done with a household book: a page per servant, duty rosters, wage entries, employment agreements, and the house rules, kept by the household itself. A paper household book and a modern one-employee payroll app are the same Type.

When the employer stops being a household and becomes a business serving customers, the software drifts into payroll and HR territory; when the work is done by family members rather than employees, it becomes home management; when the software's job is matching families with workers rather than administering employment, it belongs to the marketplace Types.

## Users & Context

**Primary users — the household as employer:**

- **Principals and family members** — the legal employer. In the common one-employee case (a nanny, a housekeeper), the parent or homeowner is the account holder, does the hiring, and approves time and pay.
- **Estate managers / house managers / chiefs of staff** — in staffed households, the employer's delegate. Runs the roster day to day: assigns duties, tracks onboarding, logs HR interactions, controls what each staff member can see.
- **Family offices and fractional estate managers** — operate staff administration across multiple employers, properties, or client households.

**Participants — the staff themselves:**

- Staff members interact with the system in most modern products, but deliberately narrowly: a scoped login that shows only their assigned tasks or permitted categories, self-service access to their own paystubs and account details, or a member area with employment documents and benefits. The employer remains the operator; the staff member is a participant with limited standing.

**Service layer:** on the employment-administration side, products ship with a human service layer — household-employment specialists who execute registrations, filings, and corrections behind the employer's account. The specialist team is part of how these products work, not optional support.

**Typical contexts:** a family employing a single nanny or housekeeper; a household employing senior care at home; a staffed estate with housekeepers, groundskeepers, a chef, and a house manager across several properties; a family office or fractional estate manager running staff administration for multiple households; a family that engaged an agency to place the staff and now manages the employment itself.

## Core Model

### The Defining Core

Three structures. If any one is removed, the software stops being recognizable as Household Staff Management:

- **The staff roster of record.** Every person employed to work in the home is held as an individually identified employment record in the household's own system: who they are, their job title and role, their employment status (full-time, part-time, contractor), typically the property or place they serve, their start date, and personal details an employer needs on file — emergency contact, birthday, preferences, allergies. Records persist and accumulate history; a promotion (housekeeper to executive housekeeper) or a status change is recorded on the person, not lost to turnover. Remove this and the software is about houses or tasks, not staff.
- **The employment administration loop.** The household runs each employment through its lifecycle inside the system: bringing the person on (records, contract, employer registrations, new-hire steps), recording their work and absence (duties and tasks, time entries, time-off requests, leave balances), administering pay or pay-related records (pay runs and payslips, or the records handed to and from a payroll service), and retaining the employment record — documents, history, access — after events change or end the employment. Remove this and what remains is a contact list or a filing cabinet; the "management" is gone.
- **The household-employer regime.** The obligations the system manages attach to a private household employing domestic staff, not to a business serving customers. This regime is what the whole category is built around: the employer is a family or individual; the work happens in the employer's home under the employer's direction; classification, employment taxes or their national equivalents, insurance, and in-home service standards all follow from that shape. Products state it explicitly — household payroll is "a different world from business payroll." Remove it and the same skeleton becomes business payroll or HR software.

```text
Household (the employer)
└── Staff roster of record
      └── Employee record (identity · role · status · place of service · start date)
            ├── Documents (contract · job description · NDA · credentials)
            ├── Work & leave (duties/tasks · time entries · approvals · PTO/sick/holiday balances)
            ├── Pay records (pay runs · payslips · withholdings)      [employment-administration realizations]
            ├── Compliance records (registrations · filings · insurance)
            └── Interaction log (time-off requests · HR updates · milestones)
Household standards layer (manual/protocols · reporting structure · per-staff permissions)   [operations realizations]
```

### Standard Capabilities Around the Core

Mature products commonly add the following. They make the core loop workable — or sell the employment-administration pole — but they do not define the Type:

- **Payroll machinery** — pay schedules, gross-to-net calculation, withholdings, direct deposit or employer-issued checks/transfers, payslips and paystubs. Dominant on the employment-administration side; notably absent from operations-side platforms, which is why it is not definitional.
- **Employment tax and filings, executed or orchestrated** — household employment taxes (Social Security/Medicare contributions, federal and state unemployment) with W-2s and the household-employer schedule filed with the personal return in the US form; income-tax withholding, national insurance, workplace pensions, and employer's liability insurance in the UK form; deadline tracking and agency correspondence handled by the provider.
- **Time and leave records** — time entry with approvals, leave policies, and running balances surfaced on pay documents.
- **Employment documents and HR support** — contract generation, job descriptions, NDAs, employer checklists, HR consultations.
- **Onboarding support** — employer registrations (tax accounts, PAYE scheme), new-hire reporting, onboarding progress tracking with check-ins and milestones.
- **Worker-classification guidance** — whether a worker is an employee or an independent contractor, decided by who controls the work, embedded in setup flows and product content; misclassification correction is a recognized service.
- **Employee self-service** — scoped staff logins, 24/7 paystub and account access for the employee, member areas, employee-facing support.
- **Insurance and background checks** — workers' compensation or employer's liability coverage, and periodic checks, attached directly or through partners; typically tier- or partner-dependent.
- **Duty and standards machinery** (operations side) — task and list assignment per staff member with completion tracking, a house manual or protocols with chapters for staff conduct and procedures, and an expressed reporting structure.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:   Staff roster of record
Shapes:    employee profiles in a household platform (role, status, property, connected documents) ·
           employees on a payroll account · employer- and employee-side member areas

Concept:   Employment administration
Shapes:    provider-executed payroll and filings behind the employer's account ·
           self-serve payroll run by the employer ·
           administration without pay at all (duties, standards, records)

Concept:   Pay
Realizations:   in-product payroll with deposit · payslip generation with self-payment by
                check or transfer · provider pays the worker and the authorities ·
                none (operations platforms stop before pay)

Concept:   Staff access
Realizations:   scoped logins with layered permissions · self-service paystubs ·
                employee member areas · no staff access (employer-only records)
```

A reader who has only seen a self-serve payroll app should still be able to recognize a staffed-estate platform that never touches pay, or a UK service that pays the nanny and the tax authority on the employer's behalf, as the same Type.

## How It Works

### 1. Bring a staff member on

```text
Add the person to the roster (identity, role, status, place of service, start date)
→ collect and attach documents (contract, job description, NDA, credentials)
→ set up the employer side (tax accounts / PAYE scheme; new-hire reporting where required)
→ settle classification (employee vs contractor) and pay arrangement
→ grant the staff member any access (scoped login, member area)
```

On employment-administration products, the service performs the registrations and files the new-hire paperwork as part of setup. Operations-side products track the onboarding itself: check-ins on a schedule, milestone notes, training and protocols to hand over.

### 2. Run the working relationship

```text
Assign duties — single tasks or recurring lists, assigned to a named staff member
→ staff complete work; completion visible to the employer
→ time and leave recorded (time entries with approvals; time-off requests; balances accrue)
→ HR interactions logged on the person's record
```

On the operations side this is the daily loop: the tasks dashboard filtered by employee shows what is on each person's plate, and the house manual's staff chapter expresses who reports to whom. On the employment-administration side the loop is lighter — hours and absence reach the pay run — because duties remain the employer's conversational work.

### 3. Pay and meet the obligations

```text
Pay period closes
→ gross-to-net calculated (wages, withholdings, employer contributions)
→ worker paid (direct deposit, or employer pays by check/transfer and the service files)
→ taxes withheld and filed on schedule (quarterly and annual; year-end forms produced)
→ deadlines tracked; agency correspondence handled by the service
```

This is the heart of the employment-administration pole and the reason households adopt it: the obligations are real (a missed filing means penalties), recurring, and unfamiliar to first-time employers. Products frame their promise around it — accuracy and on-time filing, automatic deposit and filing, specialists who answer the phone.

### 4. Keep the record

```text
Documents, pay records, filings, and interaction logs accumulate on the person's record
→ retained for years (audit and reference protection)
→ corrections and retroactive cleanup supported (catching up after months of off-record pay)
→ access stays controlled: the household decides what each person can see, and can revoke it
```

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- household-employer staff roster of record
- employment administration loop over each employment
- household-employment regime as the frame of obligations

**Standard capabilities** — present in most modern products:

- payroll machinery (on the administration pole)
- employment tax filings executed or orchestrated
- time and leave records
- employment documents and HR support
- onboarding support and classification guidance
- employee self-service
- duties/tasks and standards machinery (on the operations pole)

**Optional / variant** — depends on segment, country, and scale:

- insurance attachment, background checks
- multi-property and multi-employer operation
- benefits, rewards and wellbeing programs for staff
- placement adjacency (agency provenance, agency portals)
- AI assistance

## Interfaces

### Employer dashboard (roster view)

The household's home surface.

- all staff as cards or list entries: photo, name, role, status, place of service
- primary actions: add/edit a staff member, open a person's record, filter by property or role, search

### Employee record

The per-person workspace and the system's center of gravity.

- identity, role, status, start date, emergency contact, personal notes
- connected documents (contract, job description, NDA), time-off and HR log, pay records where applicable
- primary actions: update status, attach documents, log an interaction, connect records elsewhere in the system

### Payroll run surface

Where the employment-administration loop is executed.

- pay schedule and runs, hours and leave feeding in, gross-to-net preview, payment method
- filings and their deadlines, year-end forms, paystubs and reports
- primary actions: run or approve payroll, check filing status, download documents

### Duty and standards surfaces (operations-side realizations)

- tasks dashboard: assignments per staff member with completion state; list templates for recurring duties
- house manual / protocols: chapters for staff conduct, procedures, and reporting structure with links to staff records
- permission settings: what each staff member can see, add, edit, delete — by category and by property

### Staff-facing surfaces

Deliberately narrow.

- the staff member's own tasks or permitted categories (operations side)
- own paystubs, account details, employment documents (self-service / member areas)
- primary actions: view, confirm, and keep personal details current

### Knowledge and support layer

- employer obligation guides, checklists, and calculators (pay, leave, salary)
- access to household-employment specialists by phone or consultation — a structural surface on service-backed products, not a help afterthought

## Important Rules / Behaviors

- **The household is the employer, and control defines it.** Who sets the schedule, directs the work, and pays the wages determines that a household worker is an employee — regardless of what the arrangement is called or how payment has been made. Paying cash does not change the classification; calling a housekeeper self-employed does not either. Products embed this test because getting it wrong — treating an employee as a contractor — is a failure they describe as among the most common they are hired to correct.
- **Obligations do not scale down to zero.** Even one part-time employee puts the household inside the regime once wages cross the statutory threshold; the number of employees does not change the employer's responsibilities. Products frame their value around carrying obligations the employer did not anticipate when they hired.
- **The record exists for accountability.** Wages, hours, filings, contracts, and correspondence are kept for years because household employment is auditable and reference-checked; retroactive reconstruction after off-record payment is an established, service-shaped behavior.
- **Pay accuracy and timeliness are the trust anchor.** On the administration side, products state accuracy and on-time filing guarantees and treat a missed deadline as the named catastrophe. Precise statutory thresholds and rates vary by jurisdiction and year and are configured per account rather than fixed by the software.
- **Access is asymmetric and revocable.** Staff members see only what the household grants — their tasks, their category, their own pay records. Sensitive household information (gate codes, family details, other staff) stays behind employer-controlled permissions; a departing or dubious device does not walk away with the household's data.
- **The regime is jurisdiction-shaped.** Pay-schedule options, leave rules, filing cadence, and insurance requirements follow the employer's state or country; the same product behaves differently across jurisdictions and some are explicitly single-regime.
- **Placement is upstream and out of scope.** The system may record which agency helped find a staff member, and agencies may be partners — but hiring, matching, and placement happen before and outside this Type.

## Variants

Common shapes of the same Type:

- **Employment-administration service (payroll-centered)** — the dominant shape: the household's staff administration realized as payroll, filings, insurance, and HR support, with human specialists executing behind the employer's account. Gradients run from self-serve tools to white-glove concierge.
- **Household-operations platform (duties-centered)** — staff administration inside the household's wider operating system: roster, duties, standards, onboarding, and permissions across properties, with pay left to external services. Typical of staffed estates and family offices.
- **Single-employee mass market** — one nanny or housekeeper; one-employee plans, mobile-first payroll, employee self-service; the highest-volume segment.
- **Staffed-estate / multi-property** — many employees across residences; per-employee pricing, property-scoped access, multi-state or multi-household operation.
- **Senior-care employment at home** — families employing caregivers, companions, and aides for aging or disabled family members; the same employment loop with care-context content.
- **Nanny-share co-employment** — two families sharing one nanny; resource-level support observed, mechanics vary.
- **UK / regional regime variants** — PAYE, workplace pensions, and employer's liability insurance replace the US federal/state machinery; the same products often publish salary and leave guidance for their market.
- **Agency-partnered operation** — staffing agencies as referral, portal, or white-label partners of the administration service.

A variant remains a variant while the employer is a household administering its own employees. If the operator becomes a business serving many families, or the record center becomes enrollment rather than employment, the software is a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Payroll System | nearest relative on the money side | generic payroll serves businesses; here the household-employer regime, the classification test, and the in-home context define the system. "Household payroll" is the market's name for this Type's administration pole |
| HRIS / Employee Record System | same skeleton, different employer | business HR carries org units, benefits administration, and corporate compliance; the household carries personal service, in-home standards, and individual-employer obligations |
| Time & Attendance System / Employee Scheduling | overlapping records, different frame | org workforce management runs shifts and coverage at scale; household time and leave are embedded in each employment, with no shift-planning apparatus observed |
| Staffing Agency Management System | different side of the same hire | the agency places staff and runs its own business records; the household manages the placed person as its employee afterward. Agencies appear here only as partners or provenance |
| Babysitting Marketplace | handoff boundary | marketplaces explicitly disclaim the employer role — once the family hires, the employer-side administration that begins is this Type |
| Childcare Management System | sibling in care, opposite record center | a care operator runs a licensed business serving many families (enrollment, custody, tuition); here a family employs its own staff (employment, pay, obligations) |
| Home Management Application / Family Organizer | no employment | those coordinate household work among family members — tasks, calendars, lists with no employer, no pay, no obligations. Remove the employment relationship from this Type and you get them |
| Household Chore Application | looks similar on the operations pole | chore lists for household members vs duty assignment to employed staff; the record exists to run an employment, not to divide family chores |
| Family Care Coordination | care vs employment | coordinating care for dependents vs employing the people who provide it; a family employing an in-home caregiver is this Type |
| Estate / property management platforms | different center | estate platforms center properties, assets, vendors, and projects; staff appear as one record type or as users. Suites may carry both shapes |
| Personal Concierge Platform | service delivery vs employment | delivering services to members vs administering the employment of the people who serve the home |

The most important boundary is with **Payroll System**: the employment-administration pole is payroll-shaped, and the distinction rests not on the payroll engine but on the household-employer regime and the staff subject. The second is with the **family/home Types** — the entire category exists because household staff are employees, and the moment the employment relationship disappears, every obligation, record, and loop in this document loses its reason to exist.

## Representative Products

- **NINES** — household/estate management platform for staffed households and family offices; the operations pole: employee profiles, duties, house manual, and layered permissions (pay does not appear in its documented staff toolset)
- **HomeWork Solutions** — specialist household payroll and compliance service (US, since 1993); tiered from guided self-service to white-glove, including classification correction and background checks
- **Poppins Payroll** — self-serve household payroll for everyday employers (US); employer registration, pay runs, leave tracking, and filings behind a flat subscription
- **SurePayroll (by Paychex)** — large payroll brand with household employers as a named solutions segment; automation-first nanny, caregiver, and housekeeper payroll with employee self-service
- **Nannytax** — the longest-running UK nanny PAYE service; payroll, pensions, employer's liability insurance, contracts, HR support, and a nanny-facing member area

The definition was checked against the operations pole (staff administration without pay) and against the UK regime to avoid defining the Type by the US household-payroll pattern alone.

## Sources

Research date: **2026-09-08**

Primary vendor sources (product, solution, and official content pages):

- NINES — https://ninesliving.com/ ; "Manage your household staff with Nines" (https://ninesliving.com/manage-household-employees-with-nines/) ; "Are you setting your household employees up for success?" (https://ninesliving.com/onboarding-household-staff/)
- HomeWork Solutions — https://www.homeworksolutions.com/ ; "Hiring Other Household Staff" (https://www.homeworksolutions.com/hiring-other-household-staff/)
- Poppins Payroll — https://www.poppinspayroll.com/
- SurePayroll — https://www.surepayroll.com/household-payroll ; https://www.surepayroll.com/solutions/household
- Nannytax — https://www.nannytax.co.uk/
- EstateSpace — https://estatespace.com/ (examined as a boundary case only)

> Sourcing limitations: no dedicated help centers or member areas were fetchable in this pass (login- and JS-gated); evidence is product-page and vendor-content level, so precise operational details (exact plan mechanics, exact status vocabularies, statutory thresholds and rates) are deliberately not stated. GTM (gtm.com) and Breedlove returned access denials and were abandoned after repeated attempts; Care.com's HomePay was not directly reachable (its domain family blocks fetching, and the similar-named gethomepay.com is an unrelated product). Claims in this document are therefore calibrated to the five observed products, with UK/US regime statements kept at the level those products' own pages support.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
