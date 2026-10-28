# Rook Industries: course working file

## Session scope, Product School lab

This directory is coursework for Product School's "Codex for PMs"
certification. Everything in it is a fictional teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.
  Exceptions, for the course-setup and wrap-up skills only:
  - When the student asks you to check their setup, save their work or wrap up a session, that request is their yes. You may run the GitHub command-line program installed at ~/.codex-for-pms/gh for those checks and saves, and look in that folder to find it.
  - For a repair, first tell the student in one plain sentence what you are about to do, and act only after they say yes. Repairs may: run that GitHub program (including setting this folder's own git sign-in setting and changing this repo's visibility back to Public); copy the student's own course files into this directory from another folder on their computer (copy only; never move, edit or delete the originals); rename something outside this directory that blocks setup, by adding "-old" to its name (never delete it); and, only if the student once said no to trusting this folder, change that one trust setting for this folder in Codex's settings file, keeping a copy of the file first.
  Outside this directory you still never write, edit or delete anything else.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

### Business and products

Rook sells subscription software per active responder to independent masked responders and their handlers; it does not employ responders. Public positioning: emergency-services logistics/workforce coordination.

- **Dispatch (your product, flagship):** handler web console and responder phone app. Incident → rank available responders → ping highest-ranked → taken assigns incident and marks responder engaged; turned down/missed advances to next responder. Routing config ships with releases.
- **Supply:** gear requisitions, approvals, fulfillment and maintenance; field failure reports can bring maintenance forward. Dispatch writes the shared **Responder Availability Record**; Supply reads it for maintenance scheduling. Dispatch changes can affect Supply scheduling.
- Monthly release train, 4.x numbering. Active-callout support tickets bypass the queue. Never infer responder identities: production stores capability tags, availability and callout history, not cover identities or legal-identity mappings. Read Security Policy 4.1 before designing responder-record changes.

### People to work with

- **Helen Achebe, Director of Product:** your director; roadmap, commitments and deferred scope. Commitment changes go through Product.
- **Marcus Oyelaran, Dispatch engineering manager:** engineering partner; first stop for technical uncertainty and rough numbers.
- **Wen Li, staff engineer:** built routing; source for ranking behavior. Detailed documentation is missing.
- **Ravi Menon, data analyst:** weekly acceptance reporting; source for numbers.
- **Nadia Hoffmann, support lead:** tickets and handler concerns; Priya recommends a standing 15-minute check-in.
- **Sofia Marino, designer:** console and phone app; ran September interviews.
- **Priya Raghunathan, predecessor:** predecessor for 14 months; left 21 August 2026.

### Vocabulary and measures

Handler manages responder readiness; quartermaster owns equipment/approvals. Callout = request to attend an incident; ping = offer to one responder. Taken = yes; turned down = explicit no; missed = no response within **ping wait**.

**Acceptance rate** = taken / all pings (including turned down and missed), reported weekly in aggregate. **Time-to-accept** = median seconds from ping sent to taken. **Coverage gap** = no available responder with required capability tags; distinct from rejection. **Routing priority** uses travel-time proximity, availability, capability match and recent acceptance history. Turning down or missing lowers the history component and future ranking. **Mutual aid/shared cover** = responders covering one another across city areas; not supported today.

### Inherited situation and open questions

- **4.1 (16 June 2026):** travel-time proximity, bulk callout, push reliability. Priya describes console/mobile as stable; routing is the risk.
- **4.2 (12 August):** proximity weighted up relative to acceptance history; ping wait cut **90 → 60 seconds**; persistent console filters and three fixes. 
- By 18 August, support reported callout tickets about **3× normal**. On 26 August they remained elevated: roughly **two-thirds “phone never goes off,” one-third “gone before I could answer.”** Marcus asked whether the ranking change intentionally applied to responders turning jobs down; no resolution is recorded in Company comments.
- Priya attributed much of the acceptance decline to August seasonality, expected September recovery and opposed rollback. Treat these as unverified hypotheses/preferences. Validate trends, routing behavior and timeout effects with Ravi, Wen and Nadia. Validate her dismissal of filter tickets as cosmetic too.
- Roadmap last reviewed **30 June** still labels 4.2 items committed and owned by Priya. Availability Confidence (score beside stated availability) is absent from release notes; confirm delivery and remaining commitments with Helen. Supply approval chains target 4.3; handler app and shared cover are Q4 explorations. Document routing with Wen.

Sources: Company wiki, directory, roadmap, releases/comments; `00-rook/company/notes/handoff-from-priya.docx` (21 August 2026). Sources describe June–September 2026; verify subsequent outcomes.

Ask Priya why routing and timeout changes shipped together and what evidence justified 60 seconds.
Her “couple” of deferred 4.2 items are unnamed; request the full list and customer promises.
The handover omits Ravi’s reporting role and the Supply dependency; ask which data informed decisions and whether Supply was consulted.
