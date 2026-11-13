# Dispatch · Offer recovery pilot spec

[Director brief](dispatch-4.2-product-brief.md) · [Clickable prototype](dispatch-recovery-prototype.html)

## Pilot scope

Give eligible responders with low offer exposure a way to return toward ordinary ranking and show responders and handlers the state of each offer. Offer scoring and status are the pilot scope. Delivery-aware penalties and offer-recency tie-breaking remain options for later evaluation.

### Ranking

- Apply decay only to acceptance history. At ranking time, calculate `0.50 + (last_score − 0.50) × 2^(−elapsed_days / half_life_days)`. Start the replay at a 14-day half-life. For example, 0.20 becomes 0.35 after 14 days, and 0.80 becomes 0.65.
- When an offer resolves, compute the current effective score, apply the existing outcome adjustment (+0.08 for taken, −0.12 for declined or expired), clamp to [0, 1], and record the result and outcome timestamp once. Preserve a neutral default for responders with no history. Seed existing scores from the verified last outcome where available. For scores without a trustworthy timestamp, propose using pilot activation as the starting timestamp and validate this cohort separately in replay. Wen confirms where production history is stored and how to preserve rollback state before pilot launch.
- Use existing production eligibility and 4.2 weights. Wen verifies capability and availability rules before launch. Recovery can change an eligible responder’s rank, with no guaranteed offer.

### Offer and assignment

| Scenario | Responder app | Handler console and routing |
| --- | --- | --- |
| Offer is sent | Show incident, time remaining and **Accept** / **Decline**. Calculate remaining time from the server deadline using server time. | Show **Offer sent** and the recipient. Advance after a decline or expiry. |
| Notification arrives at +45 seconds | Show **15 seconds left**. A notification arriving after expiry opens the expired state with no actions. | Deadline remains send +60 seconds. |
| Accept reaches the server before expiry | Show **Assigned** after confirmation. | Atomically assign once, mark the responder engaged and end routing. Preserve the existing availability update that Supply consumes. |
| Responder declines or server clock reaches expiry | Show **Offer declined** or **Offer expired**. Disable both actions once terminal. | Record the reason and offer to the next eligible responder. Show **No responder assigned** if the list is exhausted. |
| Accept reaches the server at expiry or later | Show **Offer expired**, even if a delayed or offline tap was queued. | Reject the stale action. Retried messages and races between answer and expiry must produce one terminal outcome, at most one assignment and one score update per offer. |

Log offer sent, displayed where available, server answer received, terminal outcome and assignment timestamps. Capture candidate eligibility and rank at routing time for pilot analysis. Keep delivery confirmation separate from responder intent. Limit handler-visible status to the callout and offer flow.

## Pilot and release decision

- **Before launch.** Wen verifies telemetry, routing and score initialization. Ravi replays ranking with comparable callouts and checks how sensitive results are to the proposed half-life. Marcus verifies the terminal-state tests, Supply availability updates and a feature-flag rollback to current ranking with current scores. Nadia verifies the wording against real ticket scenarios.
- **Comparison.** Start with two weeks. Use comparable routing pools that do not share responders, with both groups on the same timer and ranking weights. Ravi checks feasibility, predefines the low-offer cohort by baseline offers per eligible callout and sets the minimum sample and review date before launch. If independent pools or sufficient volume are unavailable, use replay and a limited operational check while deferring an expansion decision.
- **Primary metric.** For the frozen low-offer cohort, divide the number of responder–callout pairs that received an offer by the number of pairs eligible at ranking time. Compare improvement from baseline with the concurrent comparison group. Proposed target is at least 20% relative improvement over the rate expected from the comparison group’s change. Ravi confirms a usable baseline and denominator before applying the target.
- **Guardrails.** Measure p90 seconds from callout creation to assignment among assigned callouts, alongside unassigned callouts as a share of routed callouts. Proposed limits are +5 seconds and +1 percentage point respectively versus comparison. Also review acceptance, time between offers and expired-offer tickets. Marcus pauses the pilot if a guardrail is breached and rolls back on a confirmed assignment or availability defect. Helen reviews the result before expansion.

## Prototype walkthrough

Start with the current flow to see why Kip can see an assignment while Meteor Mite’s phone stays quiet. Then run the proposed flow with an on-time or 45-second-late notification. Try accepting before expiry, declining, or advancing to the deadline and attempting a late accept. The sample ranking, incident and simulated times are illustrative. The prototype has no connection to Dispatch, responder records or live timers.
