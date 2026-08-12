# HISTORICAL TERMINOLOGY QUARANTINE

> **Do not use this file as naming authority.** It preserves an earlier state and may redirect to an obsolete naming record. The sole active headword is `impressed-force`, governed by `08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`. Historical wording does not reopen the decision.

---
# NML3 Entry Sequence Decision — 2026-08-02

Status: current steering decision for NML3 and for the active Design 2.1 ledger
after E12.

## Decision

1. There is no standalone force-sum chimney at E13.
2. E9, `net-force-material-object`, is both its Newton-II triplet entry and the
   already-installed chimney for the force-sum law.
3. E12 remains reserved for the deferred outward inertial-mass wall. Skipping it
   now does not renumber it or block NML3 work.
4. The force-sum triplet begins at E13 and its two walls end at E17.
5. The meta-typing block moves to the end of the active ledger, after the
   action-reaction, acting-object, and closure blocks.

## Active sequence from the seam

| Entry | Role |
|---|---|
| E9 | Newton-II triplet entry for `net-force-material-object`; force-sum chimney |
| E10 | Newton-II triplet entry for `inertial-mass-material-object` |
| E11 | Newton-II wall for `net-force-material-object` |
| E12 | Reserved deferred inertial-mass wall |
| E13-E15 | Force-sum triplet |
| E16-E17 | Force-sum walls: IFS generator and closer |
| E18-E23 | Action-reaction block |
| E24-E29 | Acting-object block |
| E30-E35 | Mechanical-closure block |
| E36-E41 | Meta-typing block |

## Renumbering map

| Previous active-ledger position | Current position |
|---|---|
| E13 standalone force-sum chimney | removed; role carried by E9 |
| E14-E18 force-sum remainder | E13-E17 |
| E25-E30 action-reaction | E18-E23 |
| E31-E36 acting-object | E24-E29 |
| E37-E42 closure | E30-E35 |
| E19-E24 meta-typing | E36-E41 |

Historical Design 2, Design 3, trace, and first-pass note numbers are not
silently rewritten. Their E-numbers identify the architectures they recorded.
This decision governs the active Design 2.1/NML3 surface.

The active force-member headword is governed separately by
`NML3_CONTRIBUTING_FORCE_TERMINOLOGY_DECISION_2026-08-02.md`.
