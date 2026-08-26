# Current Design 2.1 State

## One Sentence

Design 2.1 is a conservative branch from Design 3 that aims to make the entry
structure more complete and usable by adding list machinery, cleaning wording,
and filling missing wall entries without fully implementing objects or witness
sheets.

## Ratified Force-Sum Triplet Names — 2026-08-26

The three Force-Sum headwords are settled:

```text
net-force / impressed-force / interaction-set
```

The `interaction-set` contains the target particle's relevant interactions.
Each indexed interaction supplies a target-directed `impressed-force`, and the
vector sum of those impressed forces is the target's `net-force`:

```text
net-force(p | C)
    = sum of impressed-force(i -> p | C)
      for i in interaction-set(p | C)
```

This fixes the names and minimum typed relation only. Entry numbers, wall and
chimney assignments, interaction membership and closure, action/reaction, and
the rest of the NML3 cut remain open. The authority is
`../08_nm_lesson_drafts/nml3/NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`.

## Confirmed Structural Bug — 2026-08-12

`DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md` is the active design
authority for a confirmed error in the force-accounting structure. A condition
on the aggregate produced by a collection cannot, in general, determine whether
one candidate belongs to that collection.

Accordingly, the E13-and-later Force-Sum and dependent action/reaction structure
is under correction. Design work must distinguish the interaction candidate
universe, interaction identity/equality, an individual membership rule, the
constructed and closed `interaction-set`, the target-directed
`impressed-force`, and only then vector aggregation. This does not
invalidate the completed NML2 entry work, whose packets explicitly defer force
enumeration and force-sum production.

## Adopted Force-Sum Abstraction Boundary — 2026-08-14

`FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` is now owned and
maintained by Design 2.1. Its active structural result supplied the distinction
that the 2026-08-26 naming decision now expresses as

```text
net-force / interaction-set / impressed-force
```

Force-Sum consumes an already constructed, identity-bearing `interaction-set`
and obtains a target-directed `impressed-force` from each interaction.
Individual membership and closure remain outside the aggregate equality, which
cannot perform those member-level jobs.

The note was transferred from the managed VD-docs snapshot
`canvalidk/VD-docs@cae6cd109c1dfcae4f6c1f57c89c5b91660351b2`, formerly at
`Newton/Design 3/FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md`.
Its original chronological language is retained as historical evidence. Its
provisional `IFS` and `V(f)` notation translates under the 2026-08-26 decision
to `interaction-set` and target-directed `impressed-force`.

## Starting Point

The starting artifact is:

```text
07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md
```

It was copied from:

```text
DESIGN_3_ENTRY_STRUCTURE.md
```

Only its title and opening ledger description have been renamed so far. The
entry content still mostly reflects the Design 3 structure and must be edited
deliberately.

## What Design 2.1 Keeps From Design 3

- The VD is an answer-producing trace system, not just a retrospective audit.
- Natural-language questions are normalised to headwords before expansion.
- Newton I is a frame bridge and justification layer, not the free-particle
  branch of Newton II.
- `ao0` and the old `Nothing -> Newton I` routing are not revived.
- Force accounting should not begin with a flat human-supplied force set.
- Human/model inputs should land at visible trace locations.
- Walls are allowed to carry recognition hooks, modelling commitments,
  placeholders, and ordinary peripheral meaning.

## What Design 2.1 Adds Or Emphasises

The new emphasis is lists.

The design should be able to talk about structures such as:

```text
list of acting-object candidates
list of interaction candidates
interaction-set as list-like accumulator or closed collection
no-more-items / list closure signal
empty list / zero-sum result where appropriate
```

The exact formal list vocabulary is not settled yet. Design 2.1 should create
enough explicit list treatment to keep force accounting and wall entries from
depending on vague prose.

## What Design 2.1 Defers

Design 2.1 does not attempt to finish:

- formal witness sheets;
- full object schemas;
- acting-object instance dispatch;
- spring, gravity, contact, or friction concrete clusters;
- external object detection;
- full closure reasoning through interaction-pairs;
- prediction-set machinery.

Deferred material can remain as notes or placeholders when needed.

## Working Attitude

Design 2.1 should prefer explicit placeholders over silent gaps.

If a wall entry is needed but the exact final content is not ready, the entry
should say what kind of content must eventually land there and what the current
placeholder allows the trace to do.
