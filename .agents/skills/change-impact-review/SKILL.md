---
name: change-impact-review
description: Assess a proposed product or behavior change for affected users, system dependencies, feedback loops and unintended outcomes. Use when planning changes with cross-user or cross-product effects.
---

# Change impact review

Read the proposed change and available implementation, workflow and data references. Describe current and proposed behavior first. Separate observed facts, code-snapshot behavior, hypotheses and proposals.

Trace relevant paths:
- Users and workflows: who benefits, who might lose exposure, access or time, and what users see in delayed, failed or unusual cases.
- Feedback loops: how ranking, penalties or incentives affect later opportunities, including repeated effects and recovery. Aggregate averages can conceal concentrated harm.
- System and data dependencies: producers, consumers, shared state, interfaces and events, including migration and rollback where affected.
- Failure and timing boundaries: delayed delivery, stale actions, retries, concurrency, missing data and fallback behavior where relevant.
- Measurement: cohort-level effects, leading signals, guardrails and validation needed to detect unintended consequences.

For Dispatch, trace the Responder Availability Record through to Supply when affected. Separate coverage gaps, no offer, delivery failure, decline and expiry. Verify production eligibility separately from ranking points. Do not infer responder identities. Read Security Policy 4.1 before designing responder-record changes; if unavailable, flag that prerequisite and continue unaffected analysis.

Return a concise impact table: affected group/dependency, behavior change, evidence reference, possible consequence and smallest mitigation or validation step. Rate coverage of each relevant path **Pass / Needs clarification / Missing**: Pass means adequately assessed, not risk-free; Needs clarification means ambiguous or unverified; Missing means absent analysis. Explain excluded paths. Label uncertain risks as hypotheses and prioritize by plausible consequence and evidence rather than invented likelihood scores.

Review only unless edits are requested. Document questions and proposed validation without modifying production behavior, expanding scope or treating hypothetical harms as established incidents.
