# VD Newton Design 2.1 Workspace

Status: working branch space, started 2026-05-14.

Design 2.1 is a scoped fork from the Design 3 work. It keeps the useful
structural progress from Design 3 while avoiding the full object/witness-sheet
implementation burden.

## Fast Reading Order

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
     supplies the net-force wall. The inertial-mass wall at E12 is deferred to
     NML2.2.

12. `DESIGN_2_1_DRAFT_1_ENTRIES.md`
   - Active output file for the current Design 2.1 entry-drafting effort.

13. `DESIGN_2_1_ENTRY_STRUCTURE.md`
   - The forked entry ledger copied from Design 3 and renamed for Design 2.1.

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
