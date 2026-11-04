# Support tickets versus ping records

## Conclusion

The two sources agree on the main symptoms and the broad timing. All 15 explicit rolling seven-day count claims filed within the covered ping dates match exactly. Two further count claims, filed 7 September, also match the available export but have incompletely covered windows. This is not proof that all tickets are exact, that all pings reached devices, or that the release caused the observed change.

## When the data moves and when reports arrive

- Before release: 29 June–11 August has 1,085 pings, 831 taken (76.6%), 25 missed (2.3%) and 40 total tickets over 44 calendar days (0.91/day).
- 10 August: 24/32 taken (75.0%), no missed; 11 August: 13/19 taken (68.4%), one missed (5.3%). Daily samples are small.
- 12 August: 11/25 taken (44.0%), seven missed (28.0%). The Drift ticket 3041, filed 15:41, reports an offer disappearing that morning. A missed ping for The Drift is recorded at 11:41 the same day. These are compatible records, not a proven event join. Exact deployment time is unavailable.
- 13 August: 10/25 taken (40.0%), 12 missed (48.0%). Ambrose files 3043 at 09:14 about Captain Vantage the previous evening; the log contains a missed ping at 19:03 on 12 August. The body explicitly says similar incidents occurred earlier in the year.
- 13–16 August together: 48/101 taken (47.5%), 30 missed (29.7%). The immediate acceptance/missed change persists beyond one day.
- 17 August: first explicit quiet-phone ticket, Farlight 3060. Last preceding logged ping: 14 August 21:22, taken; roughly three calendar days is consistent with that report.
- Week of 17 August: the four severely affected responders receive 16 combined pings, versus 49/week across the six complete pre-release weeks; in the mixed release week they still received 43. Their next weekly totals are 6 and 3. The sustained allocation collapse is clear after the mixed release week.
- 20 August: first quiet reports for Corporal Ashgrove (3070) and The Undertow (3073); 23 August: first for Halfmoon (3086). These are first observed filing dates, not proven issue-onset dates.

## Weekly comparison

Counts are Monday–Sunday. Week starting 10 August mixes pre-release, release-day and post-release dates. The 7 September ticket day is not comparable to a full week; ping data ends 6 September.

| Week starting | All tickets | Quiet reports | Vanishing reports | Pings | Taken | Missed | Acceptance |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-06-29 | 6 | 0 | 0 | 172 | 132 | 3 | 76.7% |
| 2026-07-06 | 6 | 0 | 0 | 170 | 131 | 4 | 77.1% |
| 2026-07-13 | 8 | 0 | 0 | 174 | 133 | 6 | 76.4% |
| 2026-07-20 | 5 | 0 | 0 | 176 | 132 | 5 | 75.0% |
| 2026-07-27 | 7 | 0 | 0 | 170 | 132 | 4 | 77.6% |
| 2026-08-03 | 7 | 0 | 0 | 172 | 134 | 2 | 77.9% |
| 2026-08-10 | 20 | 0 | 7 | 177 | 96 | 38 | 54.2% |
| 2026-08-17 | 27 | 8 | 3 | 158 | 104 | 28 | 65.8% |
| 2026-08-24 | 32 | 13 | 3 | 162 | 108 | 24 | 66.7% |
| 2026-08-31 | 25 | 9 | 2 | 165 | 120 | 21 | 72.7% |
| 2026-09-07 | 4 | 2 | 0 | Not covered | — | — | Not covered |

## Explicit seven-day claims

Window definition: same responder, sent_at >= filed_at minus seven days and sent_at < filed_at. Use timestamps as database local time; do not convert the connector’s UTC-looking serialization to another timezone. Every matching source event is preserved in ticket-ping-audit.json.

| Ticket | Filed | Responder | Reported | Recorded | Coverage |
|---|---|---|---:|---:|---|
| 3071 | 2026-08-20 | Farlight | 4 | 4 | within covered dates |
| 3073 | 2026-08-20 | The Undertow | 6 | 6 | within covered dates |
| 3080 | 2026-08-22 | The Undertow | 5 | 5 | within covered dates |
| 3081 | 2026-08-22 | Farlight | 2 | 2 | within covered dates |
| 3083 | 2026-08-23 | Corporal Ashgrove | 6 | 6 | within covered dates |
| 3086 | 2026-08-23 | Halfmoon | 8 | 8 | within covered dates |
| 3089 | 2026-08-24 | Farlight | 3 | 3 | within covered dates |
| 3097 | 2026-08-26 | Corporal Ashgrove | 7 | 7 | within covered dates |
| 3098 | 2026-08-26 | Halfmoon | 8 | 8 | within covered dates |
| 3104 | 2026-08-28 | The Undertow | 2 | 2 | within covered dates |
| 3108 | 2026-08-29 | Halfmoon | 7 | 7 | within covered dates |
| 3114 | 2026-08-30 | Farlight | 2 | 2 | within covered dates |
| 3118 | 2026-08-30 | Corporal Ashgrove | 7 | 7 | within covered dates |
| 3129 | 2026-09-03 | Halfmoon | 7 | 7 | within covered dates |
| 3135 | 2026-09-04 | Corporal Ashgrove | 7 | 7 | within covered dates |
| 3145 | 2026-09-07 | The Undertow | 1 | 1 | partial: ticket filed after final covered date |
| 3147 | 2026-09-07 | Halfmoon | 8 | 8 | partial: ticket filed after final covered date |

## Two rare-offer examples

- Ticket 3110, filed 29 August: Farlight received an offer the previous night after five days, but it disappeared. The log has missed pings on 23 August 13:51 and 28 August 19:28, roughly 5.2 days apart.
- Ticket 3140, filed 5 September 18:17: The Undertow received an offer that afternoon after nine days and missed it. The log has missed pings on 27 August 23:18 and 5 September 15:17, roughly 8.7 days apart.
- Agreement on sent time and missed outcome supports the account, but pings has no delivery, display, response or withdrawal timestamps and tickets have no callout_number. These cannot prove the exact device experience or response window.

## Where the sources differ or leave gaps

- Quiet reports cover Farlight (11), The Undertow (11), Corporal Ashgrove (5), and Halfmoon (5): 32 reports from four handlers. Farlight and The Undertow have severe allocation declines. Ashgrove and Halfmoon have smaller declines broadly similar to home-area demand changes.
- No support tickets in this dataset are about Meteor Mite or Vesper, despite severe recorded ping declines. Their symptoms appear in September interviews, a separate source. Support alone misses some affected responders.
- Vanishing reports are broader: 14 post-release tickets from ten handlers. Ironvale, Sgt. Falkirk and Nightwell report disappearing offers despite receiving more pings per complete week after release. Fewer pings and missed offers are related hypotheses, not interchangeable symptoms.
- Two tickets (3110, 3140) describe both quiet stretches and disappearing offers. Therefore 32 + 14 means 44 distinct post-release tickets, not 46 independent incidents or customers.
- There are 105 total tickets after 12 August across 26 days through 7 September: 4.04/day, about 4.4 times the earlier rate. This includes filters, sign-in, equipment and other issues, and cannot all be attributed to routing. Through the shared 6 September end date, the post period has 101 tickets over 25 days, also 4.04/day.
- Earlier issues existed: ticket 3014 (14 July) describes a missed offer while out of signal; 3034 (4 August) describes unreliable notifications on an older phone; 3043 recalls earlier disappearing offers. The absence of earlier tickets in the strict post-release theme categories does not mean the symptoms were new.
- By the week of 31 August, aggregate acceptance improves to 72.7%, still below all complete pre-release weeks. Ticket volume remains 25 and quiet reports nine, consistent with continued individual problems despite aggregate improvement.

## Reproduction files

- support-ticket-rows.json: all 147 tickets, full text.
- daily-ping-rows.json: 70 daily totals freshly queried from the database, checked against all-pings.csv.
- ticket-ping-audit.json: every classified ticket, classification rules, seven-day claim windows and matching individual events.
- ticket-ping-timeline.csv: weekly ticket themes and ping totals.
- ticket-ping-queries.sql: exact database reads and a direct SQL reproduction of the rolling count checks.

Theme flags are a transparent manual reading supported by subject matching. They are not a causal classifier, and earlier related signal/device issues are explicitly listed separately. Multiple tickets may refer to the same incident.
