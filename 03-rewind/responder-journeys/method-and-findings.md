# All responder journeys: actual pings and modeled history scores

Coverage: 29 June-6 September 2026; 1,696 pings, 1,222 taken, 16 responders. Database coverage and roster checked during this analysis.

Actual weekly counts match all 160 saved responder-week rows. Six complete pre-release weeks are compared with three complete post-release weeks; 10-16 August is excluded from averages.

Scores are simulations, not observed database values. No recorded history score, rank, availability or outcome timestamp exists in the retrieved tables. Start at 0.50 on 29 June; apply code rules in sent-time order, immediately after each modeled outcome. Clamp every event to 0-1. These are not full ranking scores and cannot establish causation or production deployment. Lines use send time as an approximation; actual score updates happen after answers/timeouts. No timezone conversion is applied.

Starting-value sensitivity: replay separately from 0 and 1 and report the ending interval. Convergence only removes this particular starting-value uncertainty under the model; it does not validate production behavior.

| Responder | Pings/week before | After | Change | Model score 9 Aug | Model 6 Sep | Post offers: accepted / declined / missed |
|---|---:|---:|---:|---:|---:|---|
| Captain Vantage | 12.0 | 16.7 | +38.9% | 0.84 | 0.92 | 37 / 8 / 5 |
| Cindermark | 9.0 | 11.7 | +29.6% | 1.00 | 0.96 | 25 / 6 / 4 |
| Corporal Ashgrove | 10.0 | 7.3 | -26.7% | 1.00 | 1.00 | 15 / 4 / 3 |
| Farlight | 12.0 | 1.3 | -88.9% | 0.80 | 0.00 | 0 / 1 / 3 |
| Halfmoon | 11.0 | 8.3 | -24.2% | 0.96 | 1.00 | 17 / 5 / 3 |
| Ironvale | 8.0 | 11.0 | +37.5% | 0.96 | 0.72 | 23 / 4 / 6 |
| Meteor Mite | 11.2 | 2.3 | -79.1% | 1.00 | 0.00 | 1 / 2 / 4 |
| Nightwell | 15.0 | 19.7 | +31.1% | 0.96 | 0.88 | 42 / 11 / 6 |
| Sgt. Bulwark | 9.0 | 10.7 | +18.5% | 0.76 | 1.00 | 23 / 4 / 5 |
| Sgt. Falkirk | 10.0 | 14.7 | +46.7% | 1.00 | 0.76 | 31 / 7 / 6 |
| Stormwrack | 13.0 | 17.7 | +35.9% | 0.96 | 0.76 | 40 / 7 / 6 |
| The Drift | 6.2 | 7.7 | +24.3% | 1.00 | 0.84 | 16 / 4 / 3 |
| The Gale | 13.0 | 19.3 | +48.7% | 1.00 | 0.96 | 42 / 10 / 6 |
| The Longcast | 7.2 | 8.7 | +20.9% | 1.00 | 0.96 | 18 / 4 / 4 |
| The Undertow | 12.0 | 2.0 | -83.3% | 1.00 | 0.00 | 1 / 1 / 4 |
| Vesper | 13.8 | 2.7 | -80.7% | 0.96 | 0.00 | 1 / 2 / 5 |

Source files: ../dispatch-4.2-analysis/all-pings.csv and responder-week-rows.csv; ../../00-rook/code/dispatch-routing/{history,config,offer,routing}.py. Roster: SELECT name, handler, area FROM rook.responders ORDER BY name. Coverage: SELECT COUNT(*), MIN(sent_at), MAX(sent_at) FROM rook.pings.
