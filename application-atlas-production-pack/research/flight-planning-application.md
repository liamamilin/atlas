# Research Notes — Flight Planning Application

Research date: **2026-09-08**

## Research Goal

Understand what a Flight Planning Application actually is as a software Type: who plans flights with it, what objects exist inside it, what it computes, what it produces, how it connects to ATC and to the crew, and where its boundary lies against neighboring aviation Types (airline operations, EFB, tracking, booking).

## Initial Boundary Hypothesis

- Hypothesis entering research: a flight planning application computes and organizes the technical plan for a flight — route, altitude, time, fuel — from aircraft performance, weather and airspace data, and produces the documents/file transmissions that let the flight be operated and cleared by ATC.
- Confusable neighbors: Airline Operations Platform (day-of-operation control), Electronic Flight Bag (in-cockpit reference), Flight Search / Booking Platform (consumer acquisition, name collision), Route Optimization Platform (road logistics), Aircraft Maintenance Management, Air Cargo Management.

## Research Questions

1. What is the unit of record — the plan? a trip? a leg? What does a plan bind together?
2. How is a route constructed, and over what data (airports, waypoints, airways, procedures, airspace)?
3. What does the application compute, and from what inputs (aircraft performance data, forecast winds/temps, weights)?
4. How do weather and NOTAMs integrate — overlays, briefings, tailored packages, alerts?
5. What is filed, to whom, in what format, and what lifecycle states does a filed plan have (amend/activate/close/cancel)?
6. How does the plan reach the crew (navlog / operational flight plan / briefing package / crew app)?
7. Who uses it — pilot self-planning vs flight department/dispatch vs airline OCC vs trip-support service providers?
8. What varies across segments (GA / business aviation / airline / cargo / government)?
9. Where are the boundaries with day-of-operations platforms, EFBs, flight tracking, and booking platforms?

## Representative Products

Selected for market representation + documentation reachability + different customer tiers + different product philosophies:

| Product | Vendor family | Segment / tier | Philosophy |
|---|---|---|---|
| ForeFlight Mobile | ForeFlight (Jeppesen/Boeing) | GA pilots → business aviation (mobile EFB) | consumer-grade EFB with planning at its center |
| ForeFlight Dispatch | ForeFlight (Jeppesen/Boeing) | business aviation operators (Part 91/135-class) | dispatcher-side planning hub, planner↔pilot sync |
| RocketRoute FlightPlan | RocketRoute | private pilots + business aviation | plan-file-manage service with vendor marketplace |
| PPS Flight Planning | Air Support A/S (Denmark) | airlines, cargo, charter, governments, trip-support providers | airline-grade, customization-heavy, integration-spine OCC tool |
| FltPlan.com (+ FltPlan Go) | Garmin (founded 1999, web-era) | US pilots, ad-supported free | web-form planning + filing with companion EFB app |

Attempted but unreachable (abandoned per network rules): SkyDemon (403 ×2), Garmin Pilot manual portal (JS shell), Lufthansa Systems Lido (transport errors ×2), SITA OptiFlight (404), FalconView (transport error), Wikipedia FliteStar (timeout).

## Sources

All fetched 2026-09-08. All Layer A (direct observation) unless marked.

- ForeFlight Mobile product page — https://www.foreflight.com/products/foreflight-mobile/
- ForeFlight Flight Plan Filing page — https://foreflight.com/products/foreflight-mobile/flight-plans/
- ForeFlight Graphical Briefing page — https://foreflight.com/products/foreflight-mobile/weather/briefing/
- ForeFlight Dispatch page + FAQ — https://www.foreflight.com/products/dispatch/
- RocketRoute Flight Planning page — https://www.rocketroute.com/flight-planning
- Air Support (root) — https://www.air-support.aero/
- PPS Flight Planning product page — https://air-support.aero/pps-flight-planning/
- FltPlan.com — https://www.fltplan.com/

Source-access limitation: no vendor Help Center article interiors were directly reachable this pass (ForeFlight support center is a separate portal; PPS help center is login-gated; Garmin's documentation portal renders empty without JS; SkyDemon, Lido, SITA, FalconView unreachable). All capability claims below rest on official product/detail pages, which are vendor-authored and partly marketing-framed. Accordingly, the final document states no precise numeric limits, defaults, time windows, or country-coverage exhaustiveness.

## Product Observations

### ForeFlight Mobile (Layer A — official product/detail pages)

- Self-described as an Electronic Flight Bag used "for flight planning, charts, weather, airport information, document management, flight logging, synthetic vision, and more". Planning is the headline use.
- Two planning modes: graphical "Touch Planning" on the Maps view (drag route onto the map) and a "full-featured form-based planner" in the Flights view.
- Aircraft profile with performance data → "better fuel consumption and wind-adjusted flight time".
- Altitude Advisor: re-computed total time and fuel burn per altitude (wind strength/direction shown).
- Procedure Advisor: add SIDs / STARs / traffic-pattern entries to the route.
- Graphical Route Advisor: wind-optimized routes, official preferred routes, recently-cleared ATC routes (with clearance recency, aircraft type, altitude range), EUROCONTROL-validated autorouted IFR routes "within a matter of seconds".
- Flight plan filing in ICAO format to ATC; plan form auto-populated from planning details (route, departure time, ETE, ICAO codes, performance data from aircraft profile); filing described as delivered "directly to ATC" via dual AFTN connections on two continents.
- Post-filing lifecycle: amend or cancel IFR plans; activate and close VFR flight plans; email copy of each request kept for records.
- Flight Notifications: push/email when plan is acknowledged by ATC, when ATC issues a revised expected route, when adverse weather arises along the route, when delays due to traffic-management initiatives (EDCT/CTOT) occur — i.e., conditions changing between filing and departure.
- Pre-Departure Clearance (PDC) delivered by email/SMS at participating airports, plus digital ATIS.
- Graphical Briefing: derived from approved government sources — adverse conditions, synopsis, current conditions, enroute and destination forecasts, NOTAMs; translated + raw text options; timestamped and stored in app/cloud, positioned as recording that the pilot obtained weather/NOTAMs per preflight-action requirements (14 CFR 91.103(a)); syncs across devices, stored locally for offline in-flight use.
- Navlog with selectable templates (incl. "International" layout).
- Adjacent EFB surfaces: VFR/IFR charts from multiple sources, global vector aeronautical map, weather overlays (radar, AIR/SIGMET, winds aloft, icing/turbulence), terrain profile/hazard advisor, synthetic vision, checklists, logbook, weight & balance (integrateable into flight plans), "Pack" downloads for planned trips, runway analysis products, Jeppesen charts option, Military Flight Bag variant.

### ForeFlight Dispatch (Layer A — official product page + FAQ)

- Positioned as the business-aviation operator's "unified flight planning and collaboration hub" — "bridging the gap between flight planners and pilots".
- "Surfaces optimized options based on the latest weather and your organizational rules" — organizational constraints enter planning.
- Automations for repetitive tasks; customization "to suit your workflow and your organization's operational constraints".
- Keeps "the whole operation in sync with the flight status and when the plan changes" — plan-change propagation to crew/pilots.
- Filing: uses Jeppesen's global AFTN addressing database; ACK/REJ acknowledgment shown for USA, Canada, EUROCONTROL airspace; elsewhere "pilots should verify with the local ATC facility" — acknowledgment states are product-surfaced.
- Integrates with scheduling systems via built-in API (customer quote: scheduling → Dispatch → crews review performance data per flight; operations see flights with warnings).
- Sibling modules: Trip Support, Fuel (JetFuelX contract fuel + Fuel Advisor tankering), Runway Analysis + W&B, Flight Tracking, "Active Navlog".
- FAQ: not only for licensed dispatchers; optimized for operators flying under FAA Part 91/135 or equivalent; worldwide filing to any destination in Jeppesen's global AFTN address database, manual AFTN addresses addable.

### RocketRoute FlightPlan (Layer A — official product page)

- "FlightPlan EFB": "online flight planning, trip support, flight tracking, concierge services"; "prepare, organise, manage, and follow flights".
- Includes "charts, route generation, weather, airport information, flight tracking, and 3rd party integrations for runway performance, maintenance, and scheduling software".
- iOS/Android/Web; "File & Go" — 24/7 worldwide filing and management ("built its reputation in Flight Plan Filing and Management").
- Audience: "pilot and dispatcher in complete control of their flight".
- Connected Vendor Marketplace: connect flights to fuel, handling and other airport vendors — permits, slots, hotels, taxis coordinated "seamlessly with your flights".
- Membership packages; positions itself on speed/simplicity ("fastest way to the runway").

### PPS Flight Planning — Air Support (Layer A — official product pages)

- Airline/operations-grade: "founded on transparency and flexibility... perfect choice for the integrated OCC"; used by airlines, cargo, general/business aviation, trip-support service providers, and governments; "trusted by airlines and flight operators since 1989", 500+ operations, users in 75+ countries.
- Route generator + automation: AutoDispatch, AutoFiling via "fully automated internet-based AMEXSY flight plan filing system"; "Runway-2-Runway planning when searching and selecting SIDs/STARs for routes".
- Dynamic calculations: "fully automatic optimization and selection of the minimum production cost routing and best economical FL profile for all flights in relation to actual weight and forecasted en-route winds and temperatures"; performance data from OEM sources (Boeing BPS, Airbus PEP, or other original manufacturer data); speed configurations for climb/cruise/descent "including the dynamic cost index".
- Cost optimization: "costs calculated per leg... different objectives or constraints require different approaches"; criteria "may also change mid-flight" — data supplied for re-decisions.
- Briefing/distribution: CrewBriefing web + app — crew access "the latest briefing packages for the flight, including the operational flight plan/flight log along with updated winds and temperatures, ATC flight plan, trip-tailored NOTAM briefing, surface weather, wind charts, cross-sectional wind chart, significant weather charts as well as company messages and company NOTAMs"; offline mode; print/mail.
- Weather Watch: real-time TAF/METAR status for departure, destination and alternate airports.
- Integration spine: scheduling systems, booking systems, crew/rostering, maintenance systems, loading systems, EFB systems, runway analysis applications, performance programs, in-house custom systems (API/SOAP); "50+ systems providers" in its business network.
- Sibling product OpsControl (Flight Watch): flight tracking + weather/NOTAM monitoring for dispatchers; PPS "integrates with multiple flight tracking systems"; tracking positions "start planning based on facts rather than theoretical data models".
- Service-provider mode: "Generate and distribute complete flight plans on a commercial basis to third-party aircraft operators".
- Deployment: locally installed or hosted cloud; hosting with backups/roll-back.
- Filing-regime note: FF-ICE (ICAO initiative via EUROCONTROL/SESAR) replacing FPL 2012 from 2026 in Europe — the filing format layer is actively evolving (evidence that plan-filing machinery is a live, regime-dependent layer, not static).

### FltPlan.com / FltPlan Go (Layer A — official site)

- Web-based flight planning & filing (US-centric; site founded web-era, now a Garmin company, integrated into Garmin Connext).
- FltPlan Manager: fleet-level administrative account — "flight plans and related information are centralized by aircraft for easy management, record keeping, and control of aircraft profiles, ICAO data, and Weight & Balance".
- FltPlan Go: free companion EFB app — "powerful route and mapping features... for inflight and offline use"; displays ADS-B traffic/weather/GPS from compatible receivers; transfers flight plans directly to the Garmin Pilot app and select Garmin avionics.
- Site tools: weather, FBO & airport info, area fuel prices, nearby airports, quick trip info, digital charts.
- Philosophy: free, advertising-supported, backup site, video/manual support pages.

## Cross-product Comparison

| Structure | ForeFlight Mobile | ForeFlight Dispatch | RocketRoute | PPS | FltPlan |
|---|---|---|---|---|---|
| Persistent plan/flight record | yes (Flights view, sync mobile/web) | yes (hub, centralized) | yes (organize/manage flights) | yes (per-leg plans, data reports) | yes (plans centralized by aircraft) |
| Route built over aviation data on map/chart canvas | Touch Planning on charts | map-based planning + ATC route options | charts + route generation | interactive map, ATC route options | route/mapping features (web + Go app) |
| Aircraft profile w/ performance | yes (fuel + wind-adjusted time) | yes (performance data per flight) | 3rd-party performance integration | OEM data (BPS/PEP-class) | aircraft profiles + ICAO data |
| Computation: time/fuel/altitude | Altitude Advisor re-computes | optimized options | computed (route generation) | full climb/cruise/descent + FL profile + cost index | computed (planning + filing) |
| Weather integration | overlays + graphical briefing | "latest weather" in optimization | weather module | TAF/METAR watch (dep/dest/alt), winds/temps in briefing | weather tools |
| NOTAMs | in briefing + notifications | warning flags on flights | airport info / trip support | trip-tailored NOTAM briefing + company NOTAMs | (not evidenced) |
| Filing ICAO plan to ATC | yes, AFTN, ACK/REJ, amend/cancel/activate/close | yes, global AFTN DB, ACK/REJ | "File & Go" 24/7 worldwide | AutoFiling (AMEXSY), FF-ICE-ready | yes (web filing) |
| Briefing package / OFP to crew | graphical briefing + navlog | Active Navlog, crew sync | briefing part of service | CrewBriefing package (OFP, charts, NOTAMs) | FltPlan Go companion |
| Organizational/multi-user posture | subscriptions per pilot | planner↔pilot hub, scheduling API | membership + marketplace | OCC customization, integrations, service-provider mode | FltPlan Manager fleet account |
| Optimization depth | per-altitude re-computation, autoroutes | optimized options under org rules | (marketing-level) | min-cost routing + FL profile, cost index | basic |
| Adjacent modules sold alongside | EFB suite (charts/logbook/checklist/W&B/runway) | trip support, fuel, tracking, runway analysis | trip support marketplace, tracking, concierge | OpsControl tracking, CrewBriefing, data reports | tracking, FltPlan Go EFB |

Reading of the matrix:

- The **plan of record** (a specific flight, aircraft-bound, route-bearing, editable) is present in all five — cross-product commonality (Layer B).
- **Aviation-domain route construction** (airports/waypoints/airways/procedures/airspace on an aeronautical chart surface) is present in all five (Layer B).
- **Operational computation** (time, fuel, altitude economics driven by aircraft performance + forecast winds) is present in all five, with depth scaling from "wind-adjusted time and fuel per altitude" (GA) to "min-cost routing + optimal flight level + dynamic cost index on OEM performance data" (airline) (Layer B).
- **The briefing/OFP output and crew distribution** appear in all five in some form (briefing, navlog, CrewBriefing, companion app) (Layer B).
- **Filing to ATC in the ICAO plan format** is present in all five; acknowledgment states surfaced where the regime provides them; lifecycle verbs (amend, cancel, activate, close) evidenced in the GA/mobile product (Layer B for presence; exact per-region behavior varies).
- **NOTAM/weather tailoring** is universal in mature products but its depth varies (Layer B).
- **Organizational/posture features** (dispatch hub, scheduling integration, service-provider mode, fleet manager accounts) vary sharply by tier — clearly not definitional (Layer A per product).
- **Optimization sophistication** (cost index, min-cost routing, tankering) is a depth dimension, not an identity dimension (Layer B for direction).

## Canonical Model

### L0 — Defining Invariant (smallest stable structure)

```text
The flight plan of record
  (persistent, identified plan for a specific flight:
   aircraft + origin/destination + route + timing + load)
  └── Route constructed over aviation navigation data
      (airports, waypoints/navaids, airways, procedures, airspace — on a chart surface)
      └── Operational computation of the flight
          (distance, wind-corrected times, fuel requirement with reserve margins,
           altitude choice — from aircraft performance + forecast conditions)
```

Three jointly-held structures:

1. **The flight plan of record.** Remove → a performance calculator or a briefing reader with nothing planned; the "planning" disappears.
2. **Route construction over aeronautical data.** Remove → a generic map/route planner (roads instead of airways) or a chart viewer.
3. **Operational computation of the flight from performance + conditions.** Remove → route drawing; a line on a map is not a planned flight.

Joint-load-bearing checks:

- 1 alone = a form/record with no aviation computation (logbook row).
- 2 alone = aeronautical chart/map viewer.
- 3 alone = an E6B-class performance calculator.
- 1+2 without 3 = route sketcher.
- 1+3 without 2 = abstract flight estimator unbound to the aviation world.
- 2+3 without 1 = one-shot route/fuel calculator, no plan kept, nothing to refine/file.

### L1 — Common Mature Structure

- Weather integration (METAR/TAF, winds aloft/temps, SIGWX, adverse-condition alerts) — 5/5 sample in some form.
- NOTAM integration (route/airport-tailored NOTAM briefings, company NOTAMs) — evidenced in 4/5.
- Briefing package / operational flight plan / navlog as the plan's document form, distributed to crew (print, app, offline) — 5/5.
- Filing of the ICAO-format flight plan to ATC with lifecycle management (amend, cancel, and in some regimes activate/close; acknowledgment states) — 5/5.
- Aircraft profiles carrying performance/ICO data — 5/5.
- Autorouting / route generation (validated routes, preferred/ATC-cleared routes) — 4/5 evidenced.
- Altitude/flight-level evaluation and optimization — 4/5 evidenced (Altitude Advisor; FL profile optimization; per-altitude re-computation).
- SIDs/STARs/procedures attachable to routes — 2/5 explicit + implied in airline-grade.
- Map/chart surface as the planning canvas — 5/5.
- Weight & balance — 3/5 explicit.
- Multi-device/mobile companion surfaces — 5/5.
- Alternates in the weather picture — 1/5 explicit (departure/destination/alternate TAF/METAR), implicit in ICAO planning elsewhere.

### L2 — Variant / Optional Structure

- Trip-support layer: permits, slots, handling, fuel vendors, concierge (RocketRoute marketplace; ForeFlight Trip Support) — bizav/service-provider realization.
- Fuel economics: contract fuel programs, tankering strategy (ForeFlight JetFuelX/Fuel Advisor).
- Cost-index and minimum-cost optimization on OEM performance data (PPS).
- Deep integration spine: scheduling, booking, crew/rostering, maintenance, loading, EFB, runway analysis (PPS, ForeFlight Dispatch API).
- Fleet/organizational management accounts (FltPlan Manager; Dispatch hub).
- Flight-watch/tracking companions (PPS OpsControl; RocketRoute tracking; ForeFlight tracking; FltPlan tracking) — adjacent sibling capability.
- Deployment: local install vs hosted vs SaaS/web (PPS both poles; FltPlan web; ForeFlight cloud).
- Segment realizations: GA pilot self-planning; business-aviation flight departments; airline OCC dispatch; cargo; government/state operators (PPS operations pages; ForeFlight Military Flight Bag; Air Support government page).
- Service-provider mode: generating flight plans commercially for third-party operators (PPS explicit; trip-support firms generally).
- Filing-regime machinery and its evolution (EUROCONTROL validation; FF-ICE/FIXM transition; ACK/REJ surfacing) — regime- and era-dependent.
- Military flight bag / mission-planning posture (ForeFlight Military Flight Bag exists as a variant; deeper military mission planning was not reachable — see Uncertainties).

### L3 — Vendor-specific (research notes only)

- ForeFlight: Touch Planning, Altitude/Procedure/Route Advisors, Graphical Briefing, PDC via Satcom Direct partnership, dual-AFTN filing, FFL call sign privacy feature, Pack, Jeppesen chart bundling, 14 CFR 91.103(a) briefing-record framing.
- Air Support: PPS X, AMEXSY filing, Runway-2-Runway, AutoDispatch/AutoFiling, CrewBriefing app, Weather Watch, OpsControl Flight Watch, "500+ operations since 1989, 75+ countries" (marketing figures).
- RocketRoute: FlightPlan EFB naming, Vendor Marketplace, concierge, "7 years" service claims, 4.5/5 satisfaction (marketing).
- FltPlan: FltPlan Manager, FltPlan Go, backup sites, Garmin Connext/avionics transfer, advertising-supported model.

## Vendor-specific Findings

- Acknowledgment states for filed plans (ACK/REJ) are surfaced only where the regime provides them (ForeFlight FAQ: US/Canada/EUROCONTROL; elsewhere verify locally) — regime-dependent, not universal machinery.
- Organizational-rule-aware planning ("optimized options based on the latest weather and your organizational rules") is operator-tier positioning, not GA reality.
- The FF-ICE/FIXM transition (from FPL 2012, Europe, from 2026) shows the filing layer is actively changing — any claim about filing formats must stay abstract.
- Briefing-as-compliance-record (timestamped briefing storage per 14 CFR 91.103(a)) is a US-regulatory framing from one product — product+regime specific.

## Boundary Findings

- **vs Airline Operations Platform** (airline-ops pass pre-hung a cross-check, now discharged from this side): the ops platform owns the day-of-operation — legs instantiated from the schedule, live state, aircraft rotation, disruption control. The flight planning application owns the per-flight technical plan (route/alt/fuel) that feeds that operation. Evidence: Air Support sells PPS (planning) and OpsControl (flight watch) as separate products integrated with each other; ForeFlight positions Dispatch as planning while status/plan-change sync is "connecting" language; PPS integrates with scheduling/rostering/maintenance rather than containing them. Remove the plan computation → ops platform; remove the day-of-operation leg state → flight planning. Boundaries held on object sets: plan of record vs live operational state.
- **vs Electronic Flight Bag**: no directory leaf exists for the EFB, yet it is the dominant market category adjacent to (and bundled with) flight planning. ForeFlight Mobile self-describes as an EFB whose planning core sits next to charts/documents/logbook/checklist; FltPlan Go is a "companion EFB"; PPS lists EFB systems among the systems it integrates with. Center-of-gravity seam: constructing the plan before the flight (this Type) vs carrying charts/documents/reference during the flight (EFB). Same product frequently spans both — the Type boundary follows the center of gravity, not the product label.
- **vs Flight Search / Booking Platform** (that pass noted the name collision): booking platforms serve traveler acquisition of a seat on someone's flight (inventory of flights-as-products); flight planning serves the operator computing how a flight they will fly is actually flown. Different users, objects, and rules. Discharged from this side — keep separate.
- **vs Airport Operations Platform** (that pass recorded "adjacent, pre-operational"): airport ops owns airport-scoped resources/stand/gate allocation against the operational flight picture; flight planning computes the flight for the operator. Echo — boundaries held.
- **vs Airline Crew Management**: crew demand comes from the schedule, not from the flight plan; the plan's briefing is distributed to crew but crew legality/rosters belong to crew management.
- **vs Aircraft Maintenance Management**: maintenance status constrains which aircraft may be planned (integration spine evidence); airworthiness records themselves are another Type.
- **vs Air Cargo Management**: cargo management books shipments onto flights (capacity as the sold resource); flight planning computes the flight itself.
- **vs Route Optimization Platform** (road logistics) and **Travel Itinerary Planner**: different domain worlds (roads/vehicles; consumer trips) — same word "route/plan", different Types.
- **Trip support services** (no directory leaf): the service layer (permits, handling, concierge) is a service business wrapped around this tooling Type; the tool part belongs here. Recorded as a possible taxonomy gap only if the directory later wants a services leaf.
- **"What would make it another Type":** remove route construction over aeronautical data → generic route optimization; remove the plan of record → chart/briefing viewer (EFB territory); remove the operational computation → booking/tracking surfaces; add day-of-operation leg state + rotation control → airline operations platform.

## Historical / Market-Sample Check

- FltPlan.com (web-era, founded 1999, still operating) exhibits the same three L0 structures as modern mobile products — plan records, route over aviation data, computation with filing — without any modern EFB packaging. Historical leg satisfied by a directly observed older-generation product.
- Conceptual inference (Layer C): the paper-era practice this Type digitizes — a navigation log computed by hand from forecast winds, an ICAO flight plan form filed by phone/fax, a briefing collected from a weather office — satisfies the same core (plan of record on paper; route over published enroute charts; manual computation). No specific vintage product was directly sourced this pass (FliteStar/FalconView unreachable), so no named historical desktop product is asserted anywhere in the final document.
- Conclusion: the minimal core survives across eras and segments; mobile-first packaging, EFB bundling, cost-index optimization, and marketplace add-ons are era/market additions, not definitional.

## Uncertainties

1. Help-center interiors were not reachable; all claims are product-page level. Numeric limits, exact state names, default fuel policies, country coverage lists — deliberately absent from both documents.
2. Military mission planning systems and UAS/drone flight planning were not directly evidenced. The GA→airline span is well-evidenced; the military/UAS edges are noted as unverified adjacencies only.
3. Regional products outside the US/EUROCONTROL sphere (e.g., Asia-Pacific VFR planners) unsampled; regime-dependence of filing behavior is asserted only at the abstract level.
4. ForeFlight evidence includes one vendor family in two products (Mobile + Dispatch); they are treated as two tier poles of one vendor, balanced by RocketRoute and FltPlan at the pilot/planner tier and PPS at the airline tier.
5. Exact relationships between autorouting and official route validation differ per regime (EUROCONTROL validation vs FAA preferred routes vs recently-cleared routes); described abstractly.

## Final Synthesis

A Flight Planning Application is the aviation-operations planning system whose unit of record is the flight plan for a specific flight. Around that plan it integrates three things no neighboring system combines: route construction over aeronautical navigation data, operational computation of the flight (time, fuel, altitude) from aircraft performance and forecast conditions, and the regulated interface outward — the plan as briefing/OFP for the crew and, commonly, as a filed flight plan toward ATC with a manageable lifecycle. Everything else — EFB surfaces, trip-support marketplaces, cost-index optimization, tracking companions, fleet manager accounts, service-provider mode — is mature packaging that varies by segment (pilot / flight department / airline OCC) but does not define the Type.
