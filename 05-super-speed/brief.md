# Dispatch 4.2 · Farlight’s next ping

**To Helen Achebe, Director of Product**

**Owner: Dispatch Product Manager** — accountable for the replay and pilot, coordinating validation and bringing the expansion recommendation to Helen.

**Decision requested.** Approve a replay and limited pilot, with the target Dispatch release subject to feasibility and roadmap review. Give responders like Farlight a way to recover in the rankings and make the **60-second offer window** clear on the phone and handler console.

### What 4.2 left unresolved

Farlight averaged 12 pings a week before 4.2 and 1.3 afterward, with zero in the final week studied. Uptown callouts fell about 5%. Farlight’s handler also reported a rare ping disappearing before Farlight could answer. A miss lowers the history score, and Dispatch stops at the first acceptance. A responder who drops in rank can therefore go quiet with few chances to recover. The export lacks historical eligibility, rank and phone display times, so the team still needs to verify what caused Farlight’s decline.
[Module 3 analysis](../03-rewind/dispatch-4.2-analysis/deeper-analysis.md) · [Ticket and ping timeline](../03-rewind/dispatch-4.2-analysis/ticket-ping-comparison.md)

### What we’d build for the pilot

**Give Farlight a path back.** Let older outcomes gradually count less. With the proposed 14-day half-life, a history score of 0.20 returns toward neutral (0.50), reaching 0.35 after 14 days without a new outcome. At that point, Farlight would rank ahead of an eligible responder whose effective history score is 0.30 if all other ranking inputs are equal. This illustrates a possible recovery, not Farlight’s observed production score or a guaranteed offer. Wen and Ravi should validate the recovery rate in replay.

**Show the time Farlight actually has.** A ping displayed 45 seconds after send shows **15 seconds left**. The handler sees **Offer sent**. An acceptance received before the deadline shows **Assigned** on both screens. A decline advances routing immediately. At 60 seconds from send, the app shows **Offer expired**, the server rejects late accepts, and the handler sees Dispatch move to the next eligible responder.

**Capture enough evidence to improve scoring.** Log eligibility, rank, send, display where available, and outcome. The first pilot applies the existing 0.12 history deduction to both expiry and explicit decline. Nadia and Wen can use the timing data to evaluate a follow-up scoring change for late or unconfirmed delivery.

### How we’d decide whether to expand

Ravi defines and freezes the low-offer cohort before launch. Using candidate eligibility and offer logs, measure offers received divided by eligible responder–callout pairs for that cohort. Aim for a **20% relative improvement** over the rate expected from a concurrent comparison group’s change from baseline, using the same deadline and proximity weights. Pause if p90 callout-to-assignment time among assigned callouts rises by more than 5 seconds or unassigned callouts as a share of routed callouts rises by more than 1 percentage point versus comparison. These thresholds await validation before launch.
[Pilot spec](dispatch-recovery-spec.md) · [Clickable prototype](dispatch-recovery-prototype.html)

### Release approach and roadmap

**Proposed sequence: validate → pilot → review → staged expansion.** Wen and Ravi first validate routing, telemetry and the recovery rate in replay; Marcus confirms feasibility, rollback and preservation of the availability update that Supply consumes. The Dispatch Product Manager brings the release proposal to Helen, who confirms priority against existing roadmap commitments and approves any changes to them. Proposed experience validation: Sofia and Nadia check with handlers and responders that the prototype makes the deadline and offer states understandable, and bring any blocking findings to the launch review. The target release remains unassigned pending that review.

Start with a two-week limited pilot in comparable routing pools that do not share responders. If independent pools, reliable telemetry or sufficient volume are unavailable, continue replay and a limited operational check, deferring expansion. Ravi sets the minimum sample and review date before launch and reports results against the target and guardrails above. Marcus pauses the pilot if a guardrail is breached and rolls back on a confirmed assignment or availability defect. If the evidence supports expansion, Helen approves staged rollout to additional pools, with the same monitoring and pause rules; the team agrees each stage and review date before expanding. Insufficient evidence defers expansion.

Delivery-aware penalties and offer-recency tie-breaking remain future discovery, with no committed release. Nadia, Wen and Ravi use pilot timing and exposure evidence to assess whether either warrants a separate proposal before Helen considers roadmap priority.
