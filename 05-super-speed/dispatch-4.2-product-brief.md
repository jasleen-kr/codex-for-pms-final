# Dispatch 4.2 · Farlight’s next ping

**To Helen Achebe, Director of Product**

**Decision requested.** Approve a replay and limited pilot for the next Dispatch release. Give responders like Farlight a way to recover in the rankings and make the **60-second offer window** clear on the phone and handler console.

### What 4.2 left unresolved

Farlight averaged 12 pings a week before 4.2 and 1.3 afterward, with zero in the final week studied. Uptown callouts fell about 5%. Farlight’s handler also reported a rare ping disappearing before Farlight could answer. A miss lowers the history score, and Dispatch stops at the first acceptance. A responder who drops in rank can therefore go quiet with few chances to recover. The export lacks historical eligibility, rank and phone display times, so the team still needs to verify what caused Farlight’s decline.
[Module 3 analysis](../03-rewind/dispatch-4.2-analysis/deeper-analysis.md) · [Ticket and ping timeline](../03-rewind/dispatch-4.2-analysis/ticket-ping-comparison.md)

### What we’d build for the next release

**Give Farlight a path back.** Let older outcomes gradually count less. Take two qualified, available responders with equal travel times. Today, a responder with a fresh history score of 0.30 gets the ping ahead of Farlight at 0.20. If that responder accepts, Farlight’s phone stays quiet. With the proposed 14-day half-life, Farlight’s score reaches 0.35 after 14 days without a new outcome and Farlight gets the first ping in this example. Wen and Ravi should validate the recovery rate in replay.

**Show the time Farlight actually has.** A ping displayed 45 seconds after send shows **15 seconds left**. The handler sees **Offer sent**. An acceptance received before the deadline shows **Assigned** on both screens. A decline advances routing immediately. At 60 seconds from send, the app shows **Offer expired**, the server rejects late accepts, and the handler sees Dispatch move to the next eligible responder.

**Capture enough evidence to improve scoring.** Log eligibility, rank, send, display where available, and outcome. The first pilot applies the existing 0.12 history deduction to both expiry and explicit decline. Nadia and Wen can use the timing data to evaluate a follow-up scoring change for late or unconfirmed delivery.

### How we’d decide whether to expand

Compare the pilot with comparable routing pools using the same deadline and proximity weights. Aim for a **20% relative increase** in the share of eligible callouts that reach responders who rarely get offers. Check whether nearby responders still get timely offers. Pause if p90 time to assignment rises by more than 5 seconds or the unassigned share rises by more than 1 percentage point versus the comparison group. These thresholds are proposed for pilot planning.
[Pilot spec](dispatch-recovery-spec.md)
