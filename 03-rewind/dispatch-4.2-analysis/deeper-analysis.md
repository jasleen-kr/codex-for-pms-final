# Why four responders received fewer pings after 4.2

## Finding and confidence

The strongest explanation to investigate is a ranking feedback loop involving the shorter offer timeout, persistent acceptance-history penalties, and the change in proximity weighting. The repository demonstrates that this mechanism is possible; database counts and customer reports are consistent with it. The available evidence does not establish the actual ranking decisions or why these four responders were initially affected. Confirm that the repository snapshot matches production before treating code behavior as deployed behavior.

Six responders received fewer pings per complete week. Four show severe declines: Farlight, Meteor Mite, The Undertow and Vesper. Corporal Ashgrove (-26.7%) and Halfmoon (-24.2%) show smaller declines, broadly similar to their home-area callout-demand declines (-30.6% and -29.6% respectively); that does not prove demand explains their individual change.

## Comparable periods

Before: six full Monday–Sunday weeks, 29 June–9 August 2026.
Release week: 10–16 August, includes two pre-release days.
After: three full weeks, 17 August–6 September.
Normalize volume to pings per week because the windows have different lengths. These windows differ deliberately from the earlier exact-date comparison excluding 12 August.

| Responder | Before pings/week | After pings/week | Ping decline | Home area | Home-area callout decline/week |
|---|---:|---:|---:|---|---:|
| Farlight | 12.0 | 1.3 | 88.9% | Uptown | 5.3% |
| Meteor Mite | 11.2 | 2.3 | 79.1% | Eastgate | 14.3% |
| The Undertow | 12.0 | 2.0 | 83.3% | Harborside | 8.2% |
| Vesper | 13.8 | 2.7 | 80.7% | Old Town | 1.4% |

Home area is the responder roster's usual area, not verified eligibility for every callout. Demand comparisons are context, not a controlled estimate.

## The sequence

| Responder | Baseline pings/week (6 weeks) | 10 Aug week (mixed) | 17 Aug week | 24 Aug week | 31 Aug week |
|---|---:|---:|---:|---:|---:|
| Farlight | 12.0 | 10 | 3 | 1 | 0 |
| Meteor Mite | 11.2 | 10 | 4 | 2 | 1 |
| The Undertow | 12.0 | 11 | 4 | 1 | 1 |
| Vesper | 13.8 | 12 | 5 | 2 | 1 |

For the four combined:
- Before: 294 pings, 223 taken, 62 turned down, 9 missed. Missed share 3.1%; acceptance 75.9%.
- Mixed release week: 43 pings, 18 taken, 8 turned down, 17 missed. Missed share 39.5%; acceptance 41.9%.
- After: 25 pings, 3 taken, 6 turned down, 16 missed. Missed share 64.0%; acceptance 12.0%.
- Weekly pings decline 49.0 -> 8.3 (-83.0%).

The rise in missed share is already visible in the mixed release week, before the largest subsequent weekly ping declines. Weekly data does not establish the exact within-week sequence or causality. The 64% post-period missed rate has a small denominator (25 pings).

## Why a quiet phone may reflect ranking

Repository code:
- config.py:9: timeout 90 -> 60 seconds in 4.2.
- config.py:13–15: proximity weight 0.45 -> 0.60; acceptance-history weight 0.40 -> 0.25; capability weight unchanged at 0.15.
- offer.py:25–30: iterate the ranked list, return immediately when somebody accepts; both turned down and missed trigger record_declined.
- history.py:25–39 and config.py:18–19: taken adds 0.08, nonacceptance subtracts 0.12, score capped between 0 and 1.
- history.py:30–34: no time-based recovery toward neutral is implemented.
- routing.py:24–27 and 38–42: lower history contributes to lower rank; all available candidates stay on the ranked list.
- availability.py: available_for is a placeholder; comments say responder/handler availability is not changed by routing.

Plausible chain: shorter answer window -> more misses -> lower history score -> lower rank on future callouts -> earlier-ranked responder accepts -> affected responder gets no ping -> fewer chances to earn score back. This is a hypothesis about these responders, not an observed execution trace.

History penalties themselves were not newly introduced or increased by 4.2 according to this snapshot. The history weight actually decreased. More heavily weighted proximity can independently alter ranking. We cannot infer the four responders' travel times or capabilities from names or usual areas.

## Evidence against a simple demand-only explanation

Their home-area callouts per week fell only 1.4–14.3%, versus their individual ping declines of 79.1–88.9%.

Meteor Mite and The Gale share both Eastgate and handler Kip. Mite: 11.2 -> 2.3 pings/week (-79.1%). Gale: 13.0 -> 19.3 (+48.7%). Eastgate demand: 18.7 -> 16.0 callouts/week (-14.3%). This is a useful within-area comparison, not a matched control for availability, capabilities or travel time.

Kip's 4 September interview describes Mite being quiet while Gale is exhausted:
https://app.notion.com/p/3eac8516f501815f9b0bc8b80e97d20a

Vesper's 3 September interview describes both offers disappearing before he can answer and quiet stretches:
https://app.notion.com/p/3eac8516f50181a0bf04dd3b61063feb

Support tickets 3071 (Farlight) and 3073 (The Undertow), both 20 August, report reduced pings despite availability and tags appearing correct. These are handler reports, not verified historical availability. Ticket 3110 (29 August, Farlight) and 3140 (5 September, The Undertow) report a rare offer disappearing before acceptance. Ticket text/timing is not assumed to match exact database event counts. Earlier signal problems also existed (3014, 14 July).

The targeted ticket query returned 40 tickets, all about Farlight or The Undertow; interview evidence supplies context for Meteor Mite and Vesper. Tickets are repeated reports, not independent affected customers.

Release page and comments confirm the simultaneous changes, rising support reports, and an unresolved engineering question about ranking:
https://app.notion.com/p/3eac8516f50181499fc4c5cf15c1ace7

## What would establish the cause

With Wen and Ravi, retrieve historical availability, eligibility/capabilities, travel-time estimates, candidate rankings, score components and actual configuration for matched callouts around 12 August. Compare whether each responder was eligible, their rank, and whether dispatch stopped before reaching them.

With Nadia and engineering, trace specific disappearing-offer reports through sent, delivered/displayed, answered and withdrawn timestamps. The pings table has sent_at and outcome only; no delivery or response-duration fields. Check whether pre-release acceptances often occurred at 60–90 seconds.

Replay rankings under old/new weights on the same historical candidate inputs to isolate allocation effects; assess timeout separately. Restoring 90 seconds alone would not implement recovery of accumulated score penalties, so evaluate both mechanisms before choosing a remedy. Any production change should go through Marcus; commitment changes through Helen.

## Reproduction

deeper-source-rows.json contains all returned rows: 48 responder/period outcome rows, 45 area/period demand rows, 49 observed affected/comparator weekly rows (Farlight's final zero week is omitted by GROUP BY), and 40 support tickets.
deeper-queries.sql contains exact read-only SQL queries.
The earlier all-pings.csv provides individual events and responder-week-rows.csv includes the explicit zero week.
