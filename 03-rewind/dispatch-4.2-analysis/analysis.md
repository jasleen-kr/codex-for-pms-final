# Dispatch 4.2: weekly ping and acceptance analysis

Source: Rook database, rook.pings and rook.responders. Query window: sent_at >= 2026-06-01, no upper bound. Available data: 29 June–6 September 2026; no earlier June or later September pings were returned. All 1,696 pings are included across 16 responders and 10 Monday–Sunday weeks.

Acceptance = total taken / total pings, including turned down and missed. Rates are weighted by pings, not averages of responder percentages. Dates use database local time; UTC-looking dates in the connector output are not converted to another timezone.

## Findings

Before 12 August: 831/1,085 accepted (76.6%). After 12 August (13 August–6 September): 380/586 (64.8%), a decline of 11.7 percentage points. On release day itself: 11/25 (44.0%). The deployment time is unknown, so release day is separate. Including 12 August in the post period gives 391/611 (64.0%).

The six complete pre-release weeks average 172.3 pings and 132.3 taken per week; the three complete post-release weeks average 161.7 pings and 110.7 taken, declines of 6.2% and 16.4%. Full-week acceptance declines from 76.8% to 68.5%. The post-release weekly rate improves from 65.8% to 72.7%, still below every complete pre-release week.

Ping allocation changes sharply. Farlight, Meteor Mite, The Undertow and Vesper together receive 294 pings in six pre-release weeks (49/week), versus 25 in three post-release weeks (8.3/week), down 83.0%. Their share falls from 28.4% to 5.2%. Their acceptance also falls from 223/294 (75.9%) to 3/25 (12.0%). The remaining 12 responders receive 123.3 -> 153.3 pings/week (+24.3%), while acceptance falls from 571/740 (77.2%) to 329/460 (71.5%). These are descriptive groups identified from this dataset.

Missed pings rise from 25/1,085 (2.3%) before to 103/586 (17.6%) after, excluding release day. Turned-down pings fall from 229/1,085 (21.1%) to 103/586 (17.6%).

The timing is consistent with a release-related problem, but this observational comparison does not establish causation. Pings do not establish delivery, responder availability, demand, ranking decisions or the reason for a missed offer. Validate routing and the 60-second timeout with Wen and Ravi, including whether missed offers reduce subsequent ranking. No September recovery beyond 6 September can be assessed.

## Weekly totals

| Week starting | Period | Pings | Taken | Acceptance |
|---|---|---:|---:|---:|
| 2026-06-29 | Before | 172 | 132 | 76.7% |
| 2026-07-06 | Before | 170 | 131 | 77.1% |
| 2026-07-13 | Before | 174 | 133 | 76.4% |
| 2026-07-20 | Before | 176 | 132 | 75.0% |
| 2026-07-27 | Before | 170 | 132 | 77.6% |
| 2026-08-03 | Before | 172 | 134 | 77.9% |
| 2026-08-10 | Mixed release week | 177 | 96 | 54.2% |
| 2026-08-17 | After | 158 | 104 | 65.8% |
| 2026-08-24 | After | 162 | 108 | 66.7% |
| 2026-08-31 | After | 165 | 120 | 72.7% |

## Release-week split

| Dates | Period | Pings | Taken | Acceptance |
|---|---|---:|---:|---:|
| 10–11 August | Before | 51 | 37 | 72.5% |
| 12 August | Release day | 25 | 11 | 44.0% |
| 13–16 August | After | 101 | 48 | 47.5% |

## Responder comparison using complete weeks

Pre: six weeks starting 29 June–3 August. Post: three weeks starting 17–31 August. Each cell shows average weekly pings / average weekly taken; rates use unrounded totals.

| Responder | Before: pings / taken per week | After: pings / taken per week | Acceptance before | Acceptance after |
|---|---:|---:|---:|---:|
| Captain Vantage | 12.0 / 8.8 | 16.7 / 12.3 | 73.6% | 74.0% |
| Cindermark | 9.0 / 7.2 | 11.7 / 8.3 | 79.6% | 71.4% |
| Corporal Ashgrove | 10.0 / 7.8 | 7.3 / 5.0 | 78.3% | 68.2% |
| Farlight | 12.0 / 8.8 | 1.3 / 0.0 | 73.6% | 0.0% |
| Halfmoon | 11.0 / 8.0 | 8.3 / 5.7 | 72.7% | 68.0% |
| Ironvale | 8.0 / 6.2 | 11.0 / 7.7 | 77.1% | 69.7% |
| Meteor Mite | 11.2 / 7.7 | 2.3 / 0.3 | 68.7% | 14.3% |
| Nightwell | 15.0 / 11.3 | 19.7 / 14.0 | 75.6% | 71.2% |
| Sgt. Bulwark | 9.0 / 6.8 | 10.7 / 7.7 | 75.9% | 71.9% |
| Sgt. Falkirk | 10.0 / 8.0 | 14.7 / 10.3 | 80.0% | 70.5% |
| Stormwrack | 13.0 / 10.3 | 17.7 / 13.3 | 79.5% | 75.5% |
| The Drift | 6.2 / 5.2 | 7.7 / 5.3 | 83.8% | 69.6% |
| The Gale | 13.0 / 10.2 | 19.3 / 14.0 | 78.2% | 72.4% |
| The Longcast | 7.2 / 5.3 | 8.7 / 6.0 | 74.4% | 69.2% |
| The Undertow | 12.0 / 9.3 | 2.0 / 0.3 | 77.8% | 16.7% |
| Vesper | 13.8 / 11.3 | 2.7 / 0.3 | 81.9% | 12.5% |

## All responder-week rows

160 rows, each one responder in one Monday–Sunday week. The zero row for Farlight in the week of 31 August is explicitly filled from the responder roster; the other 159 rows have pings. A zero-ping week has no measurable acceptance rate. Pings and taken reconcile exactly to all 1,696 underlying ping records (1,222 taken). All 160 rows were independently checked against those ping records.

| Week starting | Responder | Pings | Taken |
|---|---|---:|---:|
| 2026-06-29 | Captain Vantage | 12 | 10 |
| 2026-06-29 | Cindermark | 9 | 7 |
| 2026-06-29 | Corporal Ashgrove | 10 | 8 |
| 2026-06-29 | Farlight | 12 | 9 |
| 2026-06-29 | Halfmoon | 11 | 8 |
| 2026-06-29 | Ironvale | 8 | 6 |
| 2026-06-29 | Meteor Mite | 11 | 7 |
| 2026-06-29 | Nightwell | 15 | 11 |
| 2026-06-29 | Sgt. Bulwark | 9 | 7 |
| 2026-06-29 | Sgt. Falkirk | 10 | 9 |
| 2026-06-29 | Stormwrack | 13 | 10 |
| 2026-06-29 | The Drift | 6 | 5 |
| 2026-06-29 | The Gale | 13 | 10 |
| 2026-06-29 | The Longcast | 7 | 5 |
| 2026-06-29 | The Undertow | 12 | 9 |
| 2026-06-29 | Vesper | 14 | 11 |
| 2026-07-06 | Captain Vantage | 13 | 10 |
| 2026-07-06 | Cindermark | 9 | 8 |
| 2026-07-06 | Corporal Ashgrove | 11 | 9 |
| 2026-07-06 | Farlight | 12 | 9 |
| 2026-07-06 | Halfmoon | 10 | 7 |
| 2026-07-06 | Ironvale | 8 | 5 |
| 2026-07-06 | Meteor Mite | 12 | 9 |
| 2026-07-06 | Nightwell | 14 | 10 |
| 2026-07-06 | Sgt. Bulwark | 9 | 7 |
| 2026-07-06 | Sgt. Falkirk | 10 | 8 |
| 2026-07-06 | Stormwrack | 13 | 11 |
| 2026-07-06 | The Drift | 6 | 5 |
| 2026-07-06 | The Gale | 12 | 9 |
| 2026-07-06 | The Longcast | 7 | 5 |
| 2026-07-06 | The Undertow | 11 | 9 |
| 2026-07-06 | Vesper | 13 | 10 |
| 2026-07-13 | Captain Vantage | 12 | 8 |
| 2026-07-13 | Cindermark | 8 | 6 |
| 2026-07-13 | Corporal Ashgrove | 10 | 7 |
| 2026-07-13 | Farlight | 11 | 8 |
| 2026-07-13 | Halfmoon | 11 | 8 |
| 2026-07-13 | Ironvale | 9 | 8 |
| 2026-07-13 | Meteor Mite | 10 | 6 |
| 2026-07-13 | Nightwell | 15 | 12 |
| 2026-07-13 | Sgt. Bulwark | 10 | 8 |
| 2026-07-13 | Sgt. Falkirk | 11 | 8 |
| 2026-07-13 | Stormwrack | 12 | 9 |
| 2026-07-13 | The Drift | 7 | 6 |
| 2026-07-13 | The Gale | 13 | 10 |
| 2026-07-13 | The Longcast | 8 | 7 |
| 2026-07-13 | The Undertow | 12 | 9 |
| 2026-07-13 | Vesper | 15 | 13 |
| 2026-07-20 | Captain Vantage | 11 | 7 |
| 2026-07-20 | Cindermark | 10 | 7 |
| 2026-07-20 | Corporal Ashgrove | 9 | 7 |
| 2026-07-20 | Farlight | 12 | 9 |
| 2026-07-20 | Halfmoon | 12 | 8 |
| 2026-07-20 | Ironvale | 8 | 6 |
| 2026-07-20 | Meteor Mite | 11 | 7 |
| 2026-07-20 | Nightwell | 16 | 12 |
| 2026-07-20 | Sgt. Bulwark | 9 | 7 |
| 2026-07-20 | Sgt. Falkirk | 10 | 8 |
| 2026-07-20 | Stormwrack | 14 | 12 |
| 2026-07-20 | The Drift | 6 | 5 |
| 2026-07-20 | The Gale | 14 | 11 |
| 2026-07-20 | The Longcast | 7 | 5 |
| 2026-07-20 | The Undertow | 13 | 10 |
| 2026-07-20 | Vesper | 14 | 11 |
| 2026-07-27 | Captain Vantage | 12 | 9 |
| 2026-07-27 | Cindermark | 9 | 7 |
| 2026-07-27 | Corporal Ashgrove | 10 | 8 |
| 2026-07-27 | Farlight | 13 | 10 |
| 2026-07-27 | Halfmoon | 11 | 9 |
| 2026-07-27 | Ironvale | 7 | 5 |
| 2026-07-27 | Meteor Mite | 12 | 9 |
| 2026-07-27 | Nightwell | 15 | 11 |
| 2026-07-27 | Sgt. Bulwark | 8 | 5 |
| 2026-07-27 | Sgt. Falkirk | 9 | 7 |
| 2026-07-27 | Stormwrack | 13 | 10 |
| 2026-07-27 | The Drift | 6 | 5 |
| 2026-07-27 | The Gale | 13 | 11 |
| 2026-07-27 | The Longcast | 7 | 5 |
| 2026-07-27 | The Undertow | 12 | 10 |
| 2026-07-27 | Vesper | 13 | 11 |
| 2026-08-03 | Captain Vantage | 12 | 9 |
| 2026-08-03 | Cindermark | 9 | 8 |
| 2026-08-03 | Corporal Ashgrove | 10 | 8 |
| 2026-08-03 | Farlight | 12 | 8 |
| 2026-08-03 | Halfmoon | 11 | 8 |
| 2026-08-03 | Ironvale | 8 | 7 |
| 2026-08-03 | Meteor Mite | 11 | 8 |
| 2026-08-03 | Nightwell | 15 | 12 |
| 2026-08-03 | Sgt. Bulwark | 9 | 7 |
| 2026-08-03 | Sgt. Falkirk | 10 | 8 |
| 2026-08-03 | Stormwrack | 13 | 10 |
| 2026-08-03 | The Drift | 6 | 5 |
| 2026-08-03 | The Gale | 13 | 10 |
| 2026-08-03 | The Longcast | 7 | 5 |
| 2026-08-03 | The Undertow | 12 | 9 |
| 2026-08-03 | Vesper | 14 | 12 |
| 2026-08-10 | Captain Vantage | 13 | 8 |
| 2026-08-10 | Cindermark | 10 | 6 |
| 2026-08-10 | Corporal Ashgrove | 10 | 6 |
| 2026-08-10 | Farlight | 10 | 4 |
| 2026-08-10 | Halfmoon | 11 | 6 |
| 2026-08-10 | Ironvale | 9 | 5 |
| 2026-08-10 | Meteor Mite | 10 | 4 |
| 2026-08-10 | Nightwell | 16 | 9 |
| 2026-08-10 | Sgt. Bulwark | 10 | 5 |
| 2026-08-10 | Sgt. Falkirk | 11 | 7 |
| 2026-08-10 | Stormwrack | 14 | 8 |
| 2026-08-10 | The Drift | 7 | 4 |
| 2026-08-10 | The Gale | 15 | 9 |
| 2026-08-10 | The Longcast | 8 | 5 |
| 2026-08-10 | The Undertow | 11 | 4 |
| 2026-08-10 | Vesper | 12 | 6 |
| 2026-08-17 | Captain Vantage | 15 | 11 |
| 2026-08-17 | Cindermark | 11 | 8 |
| 2026-08-17 | Corporal Ashgrove | 8 | 5 |
| 2026-08-17 | Farlight | 3 | 0 |
| 2026-08-17 | Halfmoon | 9 | 5 |
| 2026-08-17 | Ironvale | 10 | 6 |
| 2026-08-17 | Meteor Mite | 4 | 1 |
| 2026-08-17 | Nightwell | 18 | 14 |
| 2026-08-17 | Sgt. Bulwark | 10 | 8 |
| 2026-08-17 | Sgt. Falkirk | 13 | 9 |
| 2026-08-17 | Stormwrack | 16 | 12 |
| 2026-08-17 | The Drift | 7 | 5 |
| 2026-08-17 | The Gale | 17 | 12 |
| 2026-08-17 | The Longcast | 8 | 6 |
| 2026-08-17 | The Undertow | 4 | 1 |
| 2026-08-17 | Vesper | 5 | 1 |
| 2026-08-24 | Captain Vantage | 17 | 13 |
| 2026-08-24 | Cindermark | 12 | 8 |
| 2026-08-24 | Corporal Ashgrove | 7 | 5 |
| 2026-08-24 | Farlight | 1 | 0 |
| 2026-08-24 | Halfmoon | 8 | 5 |
| 2026-08-24 | Ironvale | 11 | 8 |
| 2026-08-24 | Meteor Mite | 2 | 0 |
| 2026-08-24 | Nightwell | 20 | 13 |
| 2026-08-24 | Sgt. Bulwark | 11 | 7 |
| 2026-08-24 | Sgt. Falkirk | 15 | 11 |
| 2026-08-24 | Stormwrack | 18 | 13 |
| 2026-08-24 | The Drift | 8 | 6 |
| 2026-08-24 | The Gale | 20 | 14 |
| 2026-08-24 | The Longcast | 9 | 5 |
| 2026-08-24 | The Undertow | 1 | 0 |
| 2026-08-24 | Vesper | 2 | 0 |
| 2026-08-31 | Captain Vantage | 18 | 13 |
| 2026-08-31 | Cindermark | 12 | 9 |
| 2026-08-31 | Corporal Ashgrove | 7 | 5 |
| 2026-08-31 | Farlight | 0 | 0 |
| 2026-08-31 | Halfmoon | 8 | 7 |
| 2026-08-31 | Ironvale | 12 | 9 |
| 2026-08-31 | Meteor Mite | 1 | 0 |
| 2026-08-31 | Nightwell | 21 | 15 |
| 2026-08-31 | Sgt. Bulwark | 11 | 8 |
| 2026-08-31 | Sgt. Falkirk | 16 | 11 |
| 2026-08-31 | Stormwrack | 19 | 15 |
| 2026-08-31 | The Drift | 8 | 5 |
| 2026-08-31 | The Gale | 21 | 16 |
| 2026-08-31 | The Longcast | 9 | 7 |
| 2026-08-31 | The Undertow | 1 | 0 |
| 2026-08-31 | Vesper | 1 | 0 |

## Reproduction files

- responder-week-rows.csv: all 160 rows above.
- release-split-rows.csv: 188 observed responder/week/period rows used to split the release week exactly; absent zero-count combinations are omitted.
- all-pings.csv: all 1,696 underlying ping records, retrieved in two ordered batches of 900 and 796; neither batch was truncated.
- queries.sql: exact database queries.

The six complete pre-release weeks total 1,034 pings / 794 taken. The three complete post-release weeks total 485 / 332. The mixed week totals 177 / 96. Together: 1,696 / 1,222.

