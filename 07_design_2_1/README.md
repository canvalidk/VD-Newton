# VD Newton Design 2.1 Workspace

Status: working branch space, started 2026-05-14; proposal ledger updated
2026-11-17.

Design 2.1 is a scoped fork from the Design 3 work. It keeps the useful
structural progress from Design 3 while avoiding the full object/witness-sheet
implementation burden.

## Fast Reading Order

Start with [CURRENT_STATE.md](CURRENT_STATE.md) and the **proposed
continuation** in [DESIGN_2_1_ENTRY_STRUCTURE.md](DESIGN_2_1_ENTRY_STRUCTURE.md).
The ledger uses the user's 17 November names: **Force-Sum** for
net-force / contribution / haze, and **Interaction** for the single conditional
recursion over impressed forces and the interaction set. It also adds a proposed
**Action–Reaction** house and the **orientation-based evaluation alternative**,
each with explicit corner and wall rows. Their recipient, convention, and
grounding questions remain visible. Sources are pinned and entry labels remain
provisional.
The August material below supplies the earlier naming and abstraction
boundary; it does not describe the whole current proposal. Final entry
wording remains in `DESIGN_2_1_DRAFT_1_ENTRIES.md`.

The first seven candidate packets are linked in the ledger's
[entry-packet index](DESIGN_2_1_ENTRY_STRUCTURE.md#entry-packets--2026-11-17).
Start with P-FS2 and P-I1 together, then P-FS1, P-FS3, and P-I3. P-O1/P-O2 are
separate alternative-house candidates. They include provisional entry wording
and semantic checks; they are not installed in the active draft or engine.

Before using the entry ledger, read
`DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md`. It records a
confirmed structural bug in the E13-and-later force-accounting design: an
aggregate constraint cannot supply the individual membership predicate for the
collection being aggregated. The affected structure remains under correction.
Then read
`../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`,
which historically fixed `net-force / impressed-force / interaction-set`
while leaving the rest of the cut open. Use the 17 November naming correction
in the ledger for the current two-law continuation. The older
`FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` supplies the underlying
identity/value and construction/aggregation reasoning; translate its `IFS` and
`V(f)` notation under the naming decision. Finally read
[VD-docs: Canonical-force orientation](https://github.com/canvalidk/VD-docs/blob/90383f7dfa8225e8b5496d7b3d795e13cbff3151/Newton-analysis/criticism_history/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14.md), which records
the further evaluator result and the newly exposed human convention selecting
which member of an equal-and-opposite pair is canonical.

Read these first, in this order:

1. `CURRENT_STATE.md`
   - The working picture of what Design 2.1 is.

2. `SCOPE.md`
   - What is in scope, what is deferred, and what counts as success.

3. `SOURCE_STATUS.md`
   - Which Design 3 and core VD documents should steer this branch.

4. `EDITING_RULES.md`
   - Practical rules for editing the copied entry ledger.

5. `notes/conversation_captures/CONVERSATION_ENTRY_CONSIDERATIONS_2026-05-14.md`
   - Fresh conceptual capture for wall entries, force asymmetry, gravity
     halving, and mechanical-composition list machinery.

6. `notes/kinematics/KINEMATIC_ENTRY_CANDIDATES.md`
   - Working list of Design 2 kinematic entries still to add or review.

7. `notes/kinematics/KINEMATIC_ENTRIES_FINAL_NOTES.md`
   - Agreed kinematic entry order, dependency notes, and property-status
     markings.

8. `notes/lesson_entry_notes/NEWTON_L1_ENTRY_NOTES_FIRST_PASS.md`
   - First-pass lesson notes for the Newton I / uniform-motion entry unit.

9. `notes/lesson_entry_notes/NEWTON_L2_ENTRY_NOTES_FIRST_PASS.md`
   - First-pass lesson notes for the Newton II / inertial-acceleration entry
     unit.

10. `entry_packets/ENTRY_PACKET_E7_INERTIAL_ACCELERATION_MATERIAL_OBJECT.md`
   - Current E7 chimney packet. Generic acceleration remains kinematic; the
     narrower inertial-acceleration headword begins directly in the
     massive/material-object domain.

11. `entry_packets/ENTRY_PACKET_E8_INERTIAL_ACCELERATION_MATERIAL_OBJECT.md`
    through `ENTRY_PACKET_E11_NET_FORCE_MATERIAL_OBJECT.md`
   - Remaining NML2.1 packet set: E8-E10 complete the Newton-II triplet and E11
     supplies the net-force wall. The outward inertial-mass address wall at E12
     is deferred to NML2.2; ownership of the later measurement/estimation
     operation remains open.

    For the locally stored E10 packet history, first read
    `notes/vd_docs_handoffs/why_the_mass_entry_must_be_long_joint_measurement_d3.md`,
    then `entry_packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d4.md`.
    For the selected active wording, then read
    `entry_writing_passes/E10_ENTRY_WRITING_PASS_2026-08-01_b.md`. The handoff
    distinguishes independent measurement results from the joint
    Newton-II-constrained fit; d4 is the latest packet stored locally, while the
    selected pass records its later d5 source context. The d3 packet is retained
    as the pre-correction state. The unversioned and d2 packets are still earlier
    reasoning states.

12. `entry_writing_passes/README.md`
   - Intake map for the E8-E11 independent writing passes, including the
     selected E10 and E11 wording now used in the active draft.

13. `DESIGN_2_1_DRAFT_1_ENTRIES.md`
   - Active output file for the current Design 2.1 entry-drafting effort.

14. `DESIGN_2_1_ENTRY_STRUCTURE.md`
   - Working entry ledger: existing Newton locations, Force-Sum, Interaction,
     and Action–Reaction proposals, open corners/walls, and historical routing.

15. `../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`
   - Earlier ratified authority for `net-force / impressed-force / interaction-set`.
     The current names are Force-Sum for net-force / contribution / haze and
     Interaction for contribution / impressed-force / interaction-set.
     The user's 17 November correction governs those names; final corner
     wording remains open.

16. `../08_nm_lesson_drafts/nml3/NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`
   - Ratified word-choice authority for `impressed-force`, as semantically
     refined by the 2026-08-26 triplet decision.

17. `../08_nm_lesson_drafts/nml3/NML3_ENTRY_SEQUENCE_DECISION_2026-08-02.md`
   - Historical record of the E13–E17 cut retired by the managed NML3 reset of
     2026-08-17. It is not current numbering authority.

For drafting or revising an individual entry, use an **entry packet** from
`../04_entry_design_guides/VD_NEW_ENTRY_TEMPLATE.md`. In this workspace,
"entry packet" means the copy/paste working card for one entry, not the final
entry text.

Filled entry packets for Design 2.1 live in:

```text
entry_packets/
```

Supporting notes are grouped under:

```text
notes/
```

Superseded working artifacts are preserved under:

```text
superseded/
```

## Why This Exists

Design 3 tried to do several things at once:

- implement object and witness-sheet machinery;
- clean up the entry language;
- implement list behaviour in the design;
- fill missing wall entries;
- develop acting-object dispatch and concrete force clusters.

That proved too ambitious for the next useful design pass.

Design 2.1 narrows the goal:

- implement lists in the design;
- clean up selected language;
- fill missing wall entries, sometimes with explicit placeholders;
- preserve the Design 3 insights that are already stable;
- defer full object/witness-sheet implementation.

This branch should be treated as a consolidation pass. It is not a rejection of
Design 3. It is a smaller working stage made from Design 3's map.
