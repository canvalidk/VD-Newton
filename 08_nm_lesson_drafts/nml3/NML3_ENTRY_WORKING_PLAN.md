# NML3 Entry Working Plan

Status: scaffold only. No NML3 entry wording has been selected.

## First block

The first writing target is the force-sum house:

```text
E9   chimney already present: net-force-material-object
E13  triplet: net-force-material-object November redefine
E14  triplet: interacting-forces-set winter entry
E15  triplet: contributing-force winter entry
E16  wall: interacting-forces-set generator
E17  wall: interacting-forces-set closer / terminator
```

## Decisions to settle before entry wording

- Whether `interacting-forces-set` remains the exact headword despite its
  generator/closer behaviour being list-like.
- The owner and time/interval qualifications shared by the net-force vector,
  collection, and each contributing force.
- The exact membership condition for `contributing-force`.
- How generator state records one-at-a-time unfolding from
  `mechanical-composition_point-particle`.
- How explicit closure works, including the valid empty collection and zero
  vector sum.
- How the force-sum route interacts with E11's currently counted provenance
  statement.

## Suggested production order

Develop E14 and E15 together first, because the collection/member boundary
controls the rest of the block. Then develop E16 and E17, followed by E13 once
the complete force-sum route is known.

For each entry: create an entry packet, run an independent writing pass, place
the selected wording in `07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md`, and add a
trace/evaluator acceptance check before treating it as active.
