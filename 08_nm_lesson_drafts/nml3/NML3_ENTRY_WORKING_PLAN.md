# NML3 Entry Working Plan

Status: scaffold only. No NML3 entry wording has been selected.

## First block

The first writing target is the force-sum house:

```text
E9   chimney already present: net-force-material-object
E13  triplet: net-force-material-object November redefine
E14  triplet: interacting-forces-set winter entry
E15  triplet: impressed-force winter entry
E16  wall: interacting-forces-set generator
E17  wall: interacting-forces-set closer / terminator
```

## Decisions to settle before entry wording

The member name is settled: E15 uses the ratified headword `impressed-force`
under `NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md`. Do not treat
terminology as a remaining entry decision.

The force-member identity constraint is already settled:

- Each impressed-force member is keyed by one acting-object instance.
- A material object owns or is the target of its IFS; it is not the member key.
- One acting-object instance can occur at most once in a fixed IFS and therefore
  cannot be admitted once as action and again as reaction.
- The generator's duplicate test must compare acting-object-instance keys.

The generator/closer division is also settled:

- Repeated generator success establishes only a warranted subset of the IFS.
- The successor form `R(N) = {W_N} union R(N + 1)` has no terminal case.
- Neither a known number of forces nor a current sum equal to the measured net
  force determines that the final member has been reached; further warranted
  members may form cancelling pairs or collections.
- E17 must supply an independent no-further-member determination as the base
  case that closes the account.

Remaining decisions:

- Whether `interacting-forces-set` remains the exact headword despite its
  generator/closer behaviour being list-like.
- The owner and time/interval qualifications shared by the net-force vector,
  collection, and each impressed force.
- The exact executable warrant procedure by which a candidate earns
  `impressed-force` membership; the headword and its action-on-target meaning
  are already fixed.
- How generator state records one-at-a-time unfolding from
  `mechanical-composition_point-particle`.
- How the generator preserves the acting-object-instance key while adding the
  member's target, vector value, and later action-or-reaction classification.
- What exact evidence and state representation let E17 warrant its independent
  no-further-member determination, including closure at the initial state for
  the valid empty collection.
- How the force-sum route interacts with E11's currently counted provenance
  statement.

## Suggested production order

Develop E14 and E15 together first, because the collection/member boundary
controls the rest of the block. Then develop E16 and E17, followed by E13 once
the complete force-sum route is known.

For each entry: create an entry packet, run an independent writing pass, place
the selected wording in `07_design_2_1/DESIGN_2_1_DRAFT_1_ENTRIES.md`, and add a
trace/evaluator acceptance check before treating it as active.
